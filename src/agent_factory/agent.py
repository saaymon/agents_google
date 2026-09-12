from google.adk.agents import LlmAgent


root_agent = LlmAgent(
    name="simple_agent",
    model="gemini-3.8-flash",
    instruction="Answer the user's prompt clearly and concisely.",
)