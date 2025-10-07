def speech_therapy_chatbot():
    print("=" * 60)
    print("Speech Therapist - End of Session Follow-up Chatbot")
    print("=" * 60)
    print("\nType 'quit' or 'exit' to end the session\n")
    
    while True:
        user_input = input("Describe the patient's speech condition: ").strip()
        
        print(f"\n[INPUT] {user_input}")
        
        if user_input.lower() in ['quit', 'exit']:
            print("\n[OUTPUT] Session ended. Thank you!")
            break
        
        user_input_lower = user_input.lower()
        
        if 'stuttering' in user_input_lower:
            score = "3/5"
            suggestion = "practice tongue twisters"
            print(f"[OUTPUT] Score: {score}")
            print(f"[OUTPUT] Suggestion: {suggestion}")
            print()
        elif 'calm and clear' in user_input_lower:
            score = "4/5"
            suggestion = "guided paced reading as practice"
            print(f"[OUTPUT] Score: {score}")
            print(f"[OUTPUT] Suggestion: {suggestion}")
            print()
        else:
            print("[OUTPUT] No matching condition found. Please use 'stuttering' or 'calm and clear'")
            print()

if __name__ == "__main__":
    speech_therapy_chatbot()
