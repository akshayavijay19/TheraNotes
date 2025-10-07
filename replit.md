# Speech Therapist Follow-up Chatbot

## Overview
A simple Python rule-based chatbot for speech therapists to conduct end-of-session follow-ups. The chatbot recognizes speech condition keywords and provides scores with practice suggestions.

## Current Features
- Rule-based keyword detection for speech conditions
- Score assignment: 3/5 for stuttering, 4/5 for calm and clear speech
- Practice suggestions: tongue twisters for stuttering, guided paced reading for calm/clear
- All inputs and outputs are printed to console for record keeping

## Project Structure
- `main.py` - Main chatbot script with rule-based logic

## How to Use
Run the chatbot and describe the patient's speech condition:
- Type "stuttering" → Score: 3/5, Suggestion: practice tongue twisters
- Type "calm and clear" → Score: 4/5, Suggestion: guided paced reading as practice
- Type "quit" or "exit" to end session

## Last Updated
October 7, 2025 - Initial implementation
