from src.ai.prompt_builder import build_prompt

def test_build_prompt_contains_user():
    p = build_prompt("Terve! Miten menee?", history=[{"role":"user","text":"Hei"}])
    assert "USER: Terve! Miten menee?" in p
    assert "CONTEXT:" in p
