from crewai import Task
from tools import yt_tool
from agent import researcher_agent, blog_writer


#creating a task assigned for agent
researchers_task = Task(
    description=(
        "identify the video {topic}."
        "Get detailed information about the video from the channel."
    ),
    expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content.',
    tools=[yt_tool],
    agent=researcher_agent,
    output_file='researcher_task_output.txt'
)


#creating a task for blog writer agent 
writer_task = Task(
    description=(
        "get the info from the youtube channel on the topic {topic}."
    ),
    expected_output='Summarize the info from the youtube channel video on the topic{topic}',
    tools=[yt_tool],
    agent=blog_writer,
    output_file='blog_writer_post.md'
)