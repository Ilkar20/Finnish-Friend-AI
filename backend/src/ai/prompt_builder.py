from flask import current_app

SYSTEM_PROMPT = """
You are Finnish Friend AI, a friendly and patient Finnish language tutor for beginner-to-intermediate learners.
Return a clear conversational reply. If the user wrote Finnish and there are errors, provide a short correction and a one-sentence explanation.
Keep reply <= 150 words.
"""

EXAMPLE_USER = "USER: Minä olla opettaja."
EXAMPLE_ASSISTANT = "ASSISTANT: Hyvä yritys! Correction: 'Minä olen opettaja.' Explanation: Use 'olen' for 'I am'."

def build_prompt(user_message, history=None, max_context_turns=6):
    parts = [SYSTEM_PROMPT, "EXAMPLE:", EXAMPLE_USER, EXAMPLE_ASSISTANT]
    if history:
        parts.append("\nCONTEXT:")
        for turn in history[-max_context_turns:]:
            role = turn.get("role", "user")
            text = turn.get("text", "")
            parts.append(f"{role.upper()}: {text}")
    parts.append("\nUSER: " + user_message)
    parts.append("\nASSISTANT:")
    return "\n".join(parts)
