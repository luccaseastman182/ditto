import os
import json
from swarms import Swarm, Agent

class SwarmLogic:
    def __init__(self):
        self.swarm = Swarm()

    def decompose_task(self, user_input):
        # Decompose the user-defined task into smaller tasks
        tasks = self.swarm.decompose(user_input)
        return tasks

    def create_agents(self, tasks):
        # Create agents for each task
        agents = [Agent(task) for task in tasks]
        return agents

    def assign_tasks(self, agents):
        # Assign tasks to agents
        for agent in agents:
            self.swarm.assign(agent)

    def facilitate_communication(self, agents):
        # Facilitate communication between agents
        for agent in agents:
            self.swarm.communicate(agent)

    def validate_tasks(self, agents):
        # Validate completed tasks
        validated_tasks = []
        for agent in agents:
            if self.swarm.validate(agent):
                validated_tasks.append(agent.task)
        return validated_tasks

    def add_validated_files_to_ide(self, validated_tasks):
        # Add validated files to the IDE
        for task in validated_tasks:
            file_path = os.path.join('ide', task['file_name'])
            with open(file_path, 'w') as f:
                f.write(task['content'])

    def process_user_input(self, user_input):
        tasks = self.decompose_task(user_input)
        agents = self.create_agents(tasks)
        self.assign_tasks(agents)
        self.facilitate_communication(agents)
        validated_tasks = self.validate_tasks(agents)
        self.add_validated_files_to_ide(validated_tasks)
        return validated_tasks
