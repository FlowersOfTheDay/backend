from langchain_openai import ChatOpenAI

# define ChatGPTModel class
class ChatGPTModel():
  model: str = 'gpt-4o'
  temperature: float = 0.7

  def build(self):
    return ChatOpenAI(
      model=self.model,
      temperature=self.temperature
    )