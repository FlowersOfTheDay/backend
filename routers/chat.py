from fastapi import APIRouter

from llm.chat import build
from llm.model import ChatGPTModel

from pydantic import BaseModel, Field

## restrict the input and output of the API
class InputModel(BaseModel):
  chat: str = Field(
    alias='chat',
    description='필요한 꽃을 유추하기 위한 문장'
  )

  context: str = Field(
    alias='context',
    description='대화의 문맥'
  )

class OutputModel(BaseModel):
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

  return OutputModel(
    output=chain.invoke({
       'input_context': f'''
                * 현재까지의 대화: {input.context}
                * 사용자 입력: {input.chat}
            '''
        }),
  )
