print("JARVIS: Good morning, sir. I am online.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("JARVIS: Shutting down. Goodbye, sir.")
        break

    print(f"JARVIS: You said, '{user_input}'")
   
