# Shopee Video Studio — implantação Android + servidor de IA

Este projeto usa o Android como interface e o servidor para chamadas de IA e renderização FFmpeg. **Não coloque chaves de API no aplicativo Android.** As chaves ficam apenas nas variáveis de ambiente do servidor.

## 1. Publicar o servidor

1. Crie um serviço de contêiner em um provedor que aceite Docker e ofereça armazenamento persistente (volume montado em `/data`).
2. Envie este projeto sem o arquivo `.env` e use o `Dockerfile` incluído.
3. Configure as variáveis de ambiente a partir de `.env.example`, preenchendo pelo menos `GEMINI_API_KEY` e `LLM_PROVIDER=gemini` (ou outro provedor suportado).
4. Para narração, configure `ELEVENLABS_API_KEY` e `ELEVENLABS_VOICE_ID`. Para clipes com IA, configure `FAL_KEY` e confirme no catálogo da fal.ai o modelo e os parâmetros vigentes. O modo `local` gera movimento de câmera a partir da foto sem criar mãos ou cenas novas.
5. Ative HTTPS e armazenamento persistente para `/data`. Faça um teste em `/docs` e envie uma imagem de teste.
6. Defina `ACCESS_PASSWORD` (senha forte, 12+ caracteres) nas variáveis de ambiente do servidor. Sem ela, o servidor recusa todos os pedidos. O app pede essa senha ao abrir. Há limite de 5 tentativas erradas por 10 minutos, fotos de até 10 MB (só JPG/PNG/WEBP), no máximo 3 vídeos simultâneos (`MAX_ACTIVE_JOBS`) e limpeza automática dos arquivos após 48 h (`RETENTION_HOURS`). Isso protege contra uso casual, mas para abrir ao público ainda faltam contas por usuário e cobrança.

## 2. Conectar o Android ao servidor

Edite `app/static/config.js` e substitua `https://COLOQUE-A-URL-DO-SEU-SERVIDOR` pela URL HTTPS publicada, sem barra no final. Exemplo:

```js
window.SHOPEE_API_BASE = "https://seu-app.exemplo.com";
```

A URL deve ser HTTPS. Não use `localhost` no celular, pois isso apontaria para o próprio aparelho.

## 3. Gerar o projeto Android

Requisitos: Node.js LTS, Android Studio, Android SDK e JDK compatível com a versão do Android Gradle Plugin instalada pelo Capacitor.

No terminal, dentro da pasta do projeto:

```bash
npm install
npx cap add android
npx cap sync android
npx cap open android
```

No Android Studio, aguarde a sincronização do Gradle. Para testar, use **Run** com um aparelho conectado ou emulador. Para criar o APK: **Build > Build Bundle(s) / APK(s) > Build APK(s)**. O APK de teste normalmente fica em `android/app/build/outputs/apk/debug/app-debug.apk`.

Para uma versão de distribuição, gere um APK/AAB assinado em **Build > Generate Signed Bundle / APK**. Guarde a chave de assinatura em local seguro e nunca a inclua no ZIP ou repositório.

## 4. Como o app funciona

- O app envia até 3 fotos e os dados do produto ao servidor.
- O servidor gera roteiros, cria os clipes, aplica voz/legendas/transições e monta MP4 vertical.
- O app consulta o andamento e permite reproduzir/baixar os MP4.

## Limitações importantes

- Este pacote contém a base para gerar o projeto Android, mas não inclui um APK compilado ou assinado.
- A hospedagem do servidor é separada e pode ter custos de CPU, armazenamento e APIs de IA.
- O backend original guarda o estado dos trabalhos em memória e permite apenas um render por vez; reinícios podem interromper trabalhos ativos. Para produção, recomenda-se fila persistente, autenticação, limites de upload, limpeza automática de arquivos e monitoramento.
- A compatibilidade real com cada modelo de IA deve ser testada com chaves próprias no servidor.
