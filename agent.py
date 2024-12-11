from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_MODEL_NAME'] = 'gpt-4-0125-preview'

# Debugging: print the loaded API key
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

#Creating a senior researcher agent with memory and verbose moderate researcher agent
researcher_agent = Agent(
    role="Blogs Creator from Youtube Videos",
    goal= "Provide the relevant video suggestions from the topic {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion.",
    ),
    llm=llm,
    allow_delegation=True,
    tools=[yt_tool]
)


#creating a content writer agent 
blog_writer = Agent(
    role='Writer',
    goal="Narrate compelling tech stories about the videos {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    llm=llm,
    tools=[yt_tool],
    allow_delegation=False
)