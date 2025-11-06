# backend/tests/test_prompt_builder.py

import pytest
from ai.prompt_builder import build_prompt

def test_build_prompt_contains_user():
    prompt = build_prompt(
        "Terve! Miten menee?",
        history=[{"role": "user", "text": "Hei"}],
        max_context_turns=6
    )
    assert "USER: Terve! Miten menee?" in prompt
    assert "USER: Hei" in prompt

def test_build_prompt_no_history():
    prompt = build_prompt("Moi!")
    assert "USER: Moi!" in prompt
    assert "CONTEXT:" not in prompt
