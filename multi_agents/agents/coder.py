from multi_agents.agents.utils.views import print_agent_output
from interpreter import interpreter

class CoderAgent:
    def __init__(self, websocket=None, stream_output=None, headers=None):
        self.websocket = websocket
        self.stream_output = stream_output
        self.headers = headers or {}
        
        self.interpreter = interpreter.Interpreter()

    async def generate_data_visuals(self, research_state: dict):
        """
        Generates graphs and charts based on research data.
        """
        print_agent_output("Generating graphs and charts...", agent="CODER")

        research_data = research_state.get("research_data")
        graphs = []

        for section_data in research_data:
            for section_title, section_content in section_data.items():
                try:
                    # Extract data suitable for visualization
                    data_for_graph = self.extract_data(section_content)  # Implement this method based on your data format

                    if data_for_graph:
                        # Use Open Interpreter to generate graphs
                        graph_code = self.generate_graph_code(data_for_graph)  # Implement this method to generate code for Open Interpreter
                        await self.interpreter.run(graph_code)
                        graph_path = await self.interpreter.get_file("graph.png")  # Assuming the graph is saved as graph.png

                        graphs.append((section_title, graph_path))
                except Exception as e:
                    print_agent_output(f"Error generating graph for section {section_title}: {e}", agent="CODER")

        return graphs

    def extract_data(self, section_content):
        """
        Extract data suitable for visualization from the section content.
        This method needs to be implemented based on the specific format of your research data.
        """
        # TODO: Implement logic to extract data for graph generation
        return None

    def generate_graph_code(self, data):
        """
        Generate code for Open Interpreter to create a graph based on the provided data.
        This method needs to be implemented based on the type of graph you want to create.
        """
        # TODO: Implement logic to generate graph code for Open Interpreter
        return None

    async def run(self, research_state: dict):
        graphs = await self.generate_data_visuals(research_state)
        return {"graphs": graphs}
import os
from .utils.views import print_agent_output

class CoderAgent:
    def __init__(self, code_dir, websocket=None, stream_output=None, headers=None):
        self.code_dir = code_dir
        self.websocket = websocket
        self.stream_output = stream_output
        self.headers = headers or {}

    async def run(self, state):
        if self.websocket and self.stream_output:
            await self.stream_output("logs", "coder_start", "Starting code generation...", self.websocket)
        else:
            print_agent_output("Starting code generation...", "CODER")

        # Here you would implement the logic for code generation
        # For now, we'll just create a placeholder file
        placeholder_code = "# This is a placeholder for generated code\n\ndef main():\n    print('Hello from the Coder Agent!')\n\nif __name__ == '__main__':\n    main()"
        
        file_path = os.path.join(self.code_dir, "generated_code.py")
        with open(file_path, "w") as f:
            f.write(placeholder_code)

        if self.websocket and self.stream_output:
            await self.stream_output("logs", "coder_complete", f"Code generation complete. File saved at {file_path}", self.websocket)
        else:
            print_agent_output(f"Code generation complete. File saved at {file_path}", "CODER")

        # Update the state with the path to the generated code
        state.generated_code_path = file_path
        return state
