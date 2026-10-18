"""Confere a configuração sem mostrar nenhuma chave: python check_env.py"""
import os, shutil
from dotenv import load_dotenv
load_dotenv()
ok = True
def item(nome, bom, dica):
    global ok
    print(("✅ " if bom else "❌ ") + nome + ("" if bom else "  -> " + dica)); ok &= bom
item("FFmpeg", bool(shutil.which("ffmpeg") and shutil.which("ffprobe")), "instale o FFmpeg (brew install ffmpeg / apt install ffmpeg)")
prov = os.getenv("LLM_PROVIDER", "anthropic").lower()
var = {"anthropic": "ANTHROPIC_API_KEY", "gemini": "GEMINI_API_KEY", "groq": "GROQ_API_KEY", "github": "GITHUB_TOKEN"}.get(prov, "?")
item(f"Roteiro ({prov})", bool(os.getenv(var)), f"preencha {var} no .env")
if os.getenv("VIDEO_PROVIDER", "local") == "fal":
    item("Clipes (fal.ai)", bool(os.getenv("FAL_KEY")), "preencha FAL_KEY no .env")
else:
    print("ℹ️  Clipes: modo local (zoom/pan, sem IA)")
item("Senha de acesso (ACCESS_PASSWORD)", bool(os.getenv("ACCESS_PASSWORD")), "defina uma senha forte no .env; sem ela o servidor recusa todos os pedidos")
voz = bool(os.getenv("ELEVENLABS_API_KEY") and os.getenv("ELEVENLABS_VOICE_ID"))
print("✅ Voz (ElevenLabs)" if voz else "⚠️  Voz desligada: preencha ELEVENLABS_API_KEY e ELEVENLABS_VOICE_ID")
print("\nTudo certo! Rode start.sh (Mac/Linux) ou start.bat (Windows)." if ok else "\nCorrija os itens ❌ e rode de novo.")
