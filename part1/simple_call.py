import os
from openai import AzureOpenAI

os.environ["AZURE_OPENAI_API_KEY"]="" # TODO copy your AZURE OPENAI KEY
os.environ["AZURE_OPENAI_ENDPOINT"]="" # TODO copy your AZURE OPENAI ENDPOINT URL
os.environ["AZURE_DEPLOYMENT_NAME"]="" # TODO copy your Azure OPENAI DEPLOYMENT NAME

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_KEY"),    
  api_version="2023-12-01-preview",
)

response = client.chat.completions.create(
    model= os.getenv("AZURE_DEPLOYMENT_NAME"),
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure AI services support this too?"}
    ]
)

print (response)

print(response.choices[0].message.content)
