from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set API key and model
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_MODEL_NAME'] = 'gpt-3.5-turbo'  # Specify the allowed model

# Debugging: Print the loaded API key (only for testing, remove in production)
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

# Create a senior researcher agent
researcher_agent = Agent(
    role="Blogs Creator from Youtube Videos",
    goal="Provide relevant video suggestions based on the topic {topic}",
    verbose=True,
    memory=True,
    backstory="Expert in understanding AI, Data Science, Machine Learning, and GEN AI videos to provide recommendations.",
    llm='gpt-3.5-turbo',  # Use the allowed model
    allow_delegation=True,
    tools=[yt_tool]
)

# Create a content writer agent
blog_writer = Agent(
    role='Writer',
    goal="Create compelling blogs based on YouTube videos related to {topic}.",
    verbose=True,
    memory=True,
    backstory="An expert writer skilled at turning complex topics into engaging blogs for a broad audience.",
    llm='gpt-3.5-turbo',  # Use the allowed model
    tools=[yt_tool],
    allow_delegation=False
)
