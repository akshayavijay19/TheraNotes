import os
from openai import OpenAI

# the newest OpenAI model is "gpt-5" which was released August 7, 2025.
# do not change this unless explicitly requested by the user
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai = OpenAI(api_key=OPENAI_API_KEY)

def generate_tongue_twisters():
    print("\n[OUTPUT] Generating 10 tongue twisters using AI...")
    print()
    
    if not OPENAI_API_KEY or len(OPENAI_API_KEY) < 20:
        print("[OUTPUT] Error: Valid OpenAI API key is required to generate tongue twisters.")
        print("[OUTPUT] Please add a valid API key in the Secrets tab (Tools > Secrets).")
        print()
        return
    
    try:
        response = openai.chat.completions.create(
            model="gpt-5",
            messages=[
                {
                    "role": "system",
                    "content": "You are a speech therapy assistant. Generate tongue twisters that are helpful for stuttering practice."
                },
                {
                    "role": "user",
                    "content": "Generate 10 unique tongue twisters suitable for speech therapy practice. Make them varied in difficulty and focus on different sound patterns. Number them 1-10."
                }
            ],
        )
        
        tongue_twisters = response.choices[0].message.content
        print(f"[OUTPUT] AI-Generated Tongue Twisters:")
        print(f"[OUTPUT] {tongue_twisters}")
        print()
        
    except Exception as e:
        error_msg = str(e)
        if "401" in error_msg or "invalid_api_key" in error_msg:
            print("[OUTPUT] Error: The OpenAI API key is invalid.")
            print("[OUTPUT] Please update your API key in the Secrets tab (Tools > Secrets).")
            print("[OUTPUT] Get a valid key from: https://platform.openai.com/api-keys")
        else:
            print(f"[OUTPUT] Error generating tongue twisters: {e}")
        print()

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
            
            option = input("Would you like to generate tongue twisters? (Type 'yes' or press Enter to continue): ").strip()
            print(f"\n[INPUT] {option}")
            
            if option.lower() == 'yes':
                generate_tongue_twisters()
            else:
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
