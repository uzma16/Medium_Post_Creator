class Agent:
    def __init__(self, role, tools=None):
        self.role = role
        self.tools = tools if tools is not None else []

# Assuming the creation of the agent instance is correct
agent = Agent(role="Image Generator")

# Define Task class properly to expect an Agent instance
class Task:
    def __init__(self, description, agent, expected_output):
        if not isinstance(agent, Agent):
            raise TypeError("agent must be an instance of Agent")
        self.description = description
        self.agent = agent
        self.expected_output = expected_output

# Ensure you're passing the agent instance correctly
def create_and_optimize_images_task(agent, keywords):
    if not isinstance(agent, Agent):
        raise ValueError("Provided 'agent' must be an instance of the Agent class")
    return Task(
        description=f"""
            Generate visually appealing and relevant images based on the specified keywords or themes: {keywords}.
            This task involves using advanced AI-driven graphic design tools to create compelling images for articles,
            social media posts, and advertisements.
            Provided Keywords: {keywords}
            Note: Utilize the tools for image creation, optimization, and formatting to ensure the images are high-quality and platform-ready.
        """,
        agent=agent,
        expected_output='A set of high-quality, optimized, and well-formatted images that are ready to be published on various digital marketing channels.'
    )

# Example usage:
try:
    # Instantiate an Agent and create a Task
    image_generator_agent = Agent(role="Image Generator")
    task = create_and_optimize_images_task(image_generator_agent, "futuristic cityscape")
    print(task.description)
except Exception as e:
    print(f"An error occurred: {str(e)}")
