from fastapi import APIRouter

from prisma import enums
from utils.prisma import prisma

from llm.chat import build
from llm.model import ChatGPTModel

from pydantic import BaseModel, Field

## restrict the input and output of the API
class InputModel(BaseModel):
  chat: str = Field(
    alias='chat',
    description='필요한 꽃을 유추하기 위한 문장'
  )

  id: int | None = Field(
    alias='id',
    description='사용자 식별자, 처음 대화에서는 자동으로 생성되어 반환된다.',
    default=None
  )

class OutputModel(BaseModel):
  id: int = Field(
    alias='id',
    description='사용자 식별자, input과 동일하게 반환된다.'
  )

  output: str = Field(
    alias='output',
    description='생성된 문장'
  )

router = APIRouter(
  tags=['chat']
)

model = ChatGPTModel()

@router.post('/chat')
async def chat(input: InputModel) -> OutputModel:
  chain = build(model.build())
  if input.id == None:
    log = await prisma.log.create(
      data={
        'model': 'gpt-4o'
      }, include={
        'chat': True
      }
    )
  else:
    log = await prisma.log.find_unique(where  = {
      'id': input.id
    }, include={
      'chat': True
    })

  context = ''
  for chat in log.chat:
    if chat.role == 'USER':
      context += f'사용자: {chat.text}\n'
    else:
      context += f'봇: {chat.text}\n'

  output = chain.invoke({
       'input_context': f'''
                * 현재까지의 대화: {context}
                * 사용자 입력: {input.chat}
            '''
        })

  await prisma.chat.create(
    data={
      'role': enums.ChatRole.USER,
      'text': input.chat,
      'log': {
        'connect': {
          'id': log.id
        }
      }
    }
  )

  await prisma.chat.create(
    data={
      'role': enums.ChatRole.AI,
      'text': output,
      'log': {
        'connect': {
          'id': log.id
        }
      }
    }
  )

  return OutputModel(
    output=output, id=log.id
  )
