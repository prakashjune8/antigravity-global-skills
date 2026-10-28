---
name: character-voiced-audio-synthesis
description: >-
  Generate character-voiced motivational audio, study reminders, and verbal walkthroughs using Edge TTS, SAPI, and PowerShell speech engines. Use when creating interactive study audio, pedagogical voice prompts, or habit-reinforcing verbal feedback.
---

# Character-Voiced Audio Synthesis & Motivational Pacing

## Overview
Originated from the Tharun ScholasticPulse project (`D:\THARUN PROJECT\generate_naruto_audio.py`), this skill provides the mechanics for synthesizing character-driven audio prompts (e.g., Naruto Uzumaki, gentle academic coach) to eliminate procrastination, sustain student focus, and announce study checkpoints.

---

## 1. Speech Normalization for Natural Breathing
Raw text sounds robotic when synthesized directly. Apply phonetic speech preprocessing:
1. **Contraction Expansion**: Expand contractions (`"I'm"` $\rightarrow$ `"I am"`, `"Let's"` $\rightarrow$ `"Let us"`).
2. **Punctuation Pauses**: Insert ellipses (`...`) or commas before key affirmations to create natural oratorical pauses.
3. **Phonetic Spelling**: Spell out unfamiliar names phonetically (e.g., `"Dattebayo"` $\rightarrow$ `"Dat-te-ba-yo"`).
4. **Volume & Pitch Modulation**: Set pitch to $+5\text{Hz}$ to $+10\text{Hz}$ and rate to $+10\%$ for energetic character delivery.

---

## 2. Multi-Engine Synthesis Cascade
- **Edge TTS (Primary)**: High-fidelity neural voice synthesis (`en-US-GuyNeural`, `en-US-ChristopherNeural`, `en-IN-PrabhatNeural`).
- **PowerShell / SAPI Fallback (Offline)**:
  ```powershell
  Add-Type -AssemblyName System.Speech
  $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
  $synth.SelectVoice("Microsoft David Desktop")
  $synth.Rate = 1
  $synth.SetOutputToWaveFile("$PSScriptRoot\assets\quote.wav")
  $synth.Speak("I am not gonna run away! That is my ninja way!")
  $synth.Dispose()
  ```

---

## 3. Storage & Metadata Catalog
- Save audio assets to `<project_root>/assets/<voice_id>/<quote_id>.wav`.
- Accompany with an auditable JSON metadata index containing:
  - `character`, `role`, `theme`, `quote_text`, `speech_text`, `audio_file`, `duration_sec`.
