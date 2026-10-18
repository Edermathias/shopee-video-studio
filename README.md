# Shopee Video Studio

Foto do produto → roteiros (Claude) → clipes → voz → legendas → MP4 vertical 1080x1920.
Cada execução gera várias versões com ganchos diferentes, para você testar qual converte mais.

## Rodar
1. Instale Python 3.11+ e FFmpeg (com libass). No Mac: `brew install ffmpeg`.
2. `pip install -r requirements.txt`
3. `cp .env.example .env` e escolha `LLM_PROVIDER` (anthropic, gemini, groq ou github) e preencha a chave correspondente.
4. `uvicorn app.main:app --reload` e abra http://localhost:8000
5. Teste só a montagem, sem APIs: `python selftest.py`

Ou com Docker: `docker build -t shopee-studio .` e
`docker run -p 8000:8000 --env-file .env -v $PWD/data:/data shopee-studio`

## Provedores de clipe
- `local` (padrão): grátis, usa a foto real com zoom/pan. Fiel ao produto, mas sem mãos nem caixa.
- `fal`: IA imagem-para-vídeo (Kling etc.) via fal.ai. Defina `FAL_KEY` e confira `FAL_MODEL`
  no catálogo da fal.ai. Esse adaptador não foi testado com a API real.

## Voz e música
- Com `ELEVENLABS_API_KEY` e `ELEVENLABS_VOICE_ID`, cada cena ganha narração e a duração se ajusta à fala.
- `MUSIC_FILE`: use só música livre de direitos.

## Antes de postar
- Confira na Central do Vendedor Shopee os limites atuais de duração, tamanho e formato.
- Mostre o produto fiel ao real e não prometa o que ele não faz.
- Poste as versões em dias/horários parecidos e compare views, cliques e pedidos.

## Próximos passos
Fila persistente (Redis/RQ), login, upload direto para a nuvem, métricas por versão.

## Acabamento profissional (automático)
Transições entre cenas, correção de cor e nitidez, legendas com animação, cartela final com CTA,
música que abaixa quando há voz e áudio normalizado (-14 LUFS). Ajuste com `TRANSITION_SEC` no `.env`.
Para ter mãos, caixa e movimento realista, use `VIDEO_PROVIDER=fal` (IA imagem-para-vídeo).

## Roteiros com Gemini, Groq ou GitHub Models
Usam a API compatível com OpenAI. Gemini e GitHub leem a foto; Groq (Llama) usa só o texto. Troque o modelo com `LLM_MODEL` se o padrão mudar. Esses adaptadores não foram testados com as APIs reais.

## Início rápido
Cole suas chaves no `.env` e rode `./start.sh` (Mac/Linux) ou `start.bat` (Windows).
Ele cria o ambiente, instala tudo, confere a configuração e abre o app em http://localhost:8000.

## Gerar APK usando somente o celular
Consulte `GUIA_SO_CELULAR.md`. O workflow `.github/workflows/build-android.yml` compila o APK em um runner do GitHub Actions e publica o APK de teste como artefato para baixar no celular. Configure a variável de repositório `API_BASE_URL` com a URL HTTPS do backend antes de executar o workflow.
