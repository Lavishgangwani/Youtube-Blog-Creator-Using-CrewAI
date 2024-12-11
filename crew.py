from crewai import Crew, Process
from agent import researcher_agent, blog_writer
from tasks import researchers_task, writer_task

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[researcher_agent, blog_writer],
  tasks=[researchers_task, writer_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

# Starting the task execution process with enhanced feedback
result = crew.kickoff(inputs={'topic': 'AI vs ML VS DL VS Data Science'})
print(result)