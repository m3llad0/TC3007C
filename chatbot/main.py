from openAIAssitant import Assistant
import time


def check_status(client, thread_id, run_id):
    while True:
        run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)

        if run.status != "completed":
            print("Status: ", run.status)
            time.sleep(3)
        else:
            break

def main():
    # Create assistant
    assistant = Assistant(
        assistant_name="My Assistant",
        assistant_instructions="Support the user in practicing a new language. Engage in conversations, provide translations, and offer language-learning tips.",
    )

    # Create thread
    thread = assistant.create_thread()

    # Create chat

    while True:
        print("User: ", end="")
        user_input = input()
        if user_input == "exit":
            break
        
        message = assistant.return_client().beta.threads.messages.create(
            thread_id = thread.id,
            role = "user",
            content = user_input
        )

        # Ejecutar asistente

        run = assistant.return_client().beta.threads.runs.create(
            thread_id = thread.id,
            assistant_id = assistant.get_assistant().id
        )

        check_status(assistant.return_client(), thread.id, run.id)

        messages = assistant.return_client().beta.threads.messages.list(
            thread_id=thread.id)
        
        assistant_message = messages.data[0].content[0].text.value
        print("Assistant: ", assistant_message)




if __name__ == "__main__":
    main()