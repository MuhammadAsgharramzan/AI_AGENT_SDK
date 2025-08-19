from agents import Agent, Runner, RunConfig, OpenAIChatCompletionsModel, AsyncOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")  # Ensure you have set your API key in the environment variable



external_client = AsyncOpenAI(
    api_key= API_KEY,  # Replace with your actual API key
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

external_model = OpenAIChatCompletionsModel(
    model='gemini-2.5-flash',
    openai_client=external_client,
)

config = RunConfig(
    model=external_model,
    model_provider=external_client,
    tracing_disabled=True,
)

agent = Agent( 
    name = "Assistant",
    instructions="Your name is Assistant. You are a helpful assistant. You can answer questions, provide information, and assist with tasks. Always be polite and concise.",
)


result = Runner.run_sync(starting_agent=agent,input="Hello, how can I help you today?", run_config=config)

print(result.final_output)

