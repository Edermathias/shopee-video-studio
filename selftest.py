"""Testa a renderização (FFmpeg + legendas) sem APIs: python selftest.py [foto.jpg]"""
import subprocess, sys
from pathlib import Path
from app.pipeline import renderizar_versao

work = Path("data/selftest"); work.mkdir(parents=True, exist_ok=True)
foto = Path(sys.argv[1]) if len(sys.argv) > 1 else work / "foto.png"
if not foto.exists():  # imagem de teste gerada pelo FFmpeg
    subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "testsrc2=s=800x800", "-frames:v", "1", str(foto)],
                   check=True, capture_output=True)
versao = {"cta": "Compre agora na Shopee", "cenas": [
    {"fala": "", "legenda": "Olha o que chegou", "video_prompt": ""},
    {"fala": "", "legenda": "Abrindo a caixa", "video_prompt": ""},
    {"fala": "", "legenda": "Garanta o seu", "video_prompt": ""}]}
out = renderizar_versao([foto], versao, work / "v0", "local", on_step=print)
print("OK:", out)
