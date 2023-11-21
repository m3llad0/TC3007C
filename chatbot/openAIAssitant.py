from openai import OpenAI
from config import API_KEY

class Assistant:
    _instance = None

    def __new__(cls, assistant_name, assistant_instructions, model='gpt-3.5-turbo'):
            if not cls._instance:
                cls._instance = super(Assistant, cls).__new__(cls)
                
                # Initialize OpenAI client
                cls._instance.client = OpenAI(api_key=API_KEY)

                # Create assistant
                cls._instance.assistant = cls._instance.client.beta.assistants.create(
                    name=assistant_name,
                    instructions=assistant_instructions,
                    tools=[{"type": "code_interpreter"}],
                    model=model
                )

                print("OpenAI Assistant created.")
            
            return cls._instance

    def get_assistant(self):
        return self.assistant

    def create_thread(self):
        return self._instance.client.beta.threads.create() 
    
    def return_client(self):
        return self._instance.client