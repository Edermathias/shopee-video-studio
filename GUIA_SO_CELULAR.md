# Shopee Video Studio — fazer tudo pelo celular Android

Este fluxo usa o navegador do celular e serviços em nuvem. Não precisa instalar Android Studio no telefone. É necessário ter uma conta GitHub e uma hospedagem compatível com Docker para o servidor de IA. A hospedagem e as APIs podem ter custos.

## A. Preparar o servidor
1. No navegador do celular, entre no GitHub e crie um repositório privado chamado `shopee-video-studio`.
2. Envie os arquivos deste projeto ao repositório (pode usar o site GitHub no navegador; para muitos arquivos, o app GitHub não é suficiente em todos os aparelhos).
3. No serviço de hospedagem Docker, conecte o repositório e selecione o `Dockerfile` da raiz. Configure a porta 8000 e HTTPS.
4. Configure no servidor as variáveis de ambiente necessárias a partir de `.env.example`. Não envie `.env` nem coloque chaves de API no GitHub ou no APK.
5. Crie a variável `ACCESS_PASSWORD` com uma senha forte (é obrigatória). Só quem tiver a senha consegue gerar vídeos. O estado dos trabalhos fica em memória, então reinícios podem interromper vídeos em andamento. Faça primeiro um teste privado.
6. Copie a URL pública HTTPS do backend e teste `https://SUA-URL/docs` no navegador.

## B. Gerar APK na nuvem pelo celular
1. Envie todo o conteúdo do projeto para o repositório GitHub, incluindo a pasta `.github/workflows/build-android.yml`.
2. No repositório, abra **Settings → Secrets and variables → Actions → Variables → New repository variable**.
3. Nome: `API_BASE_URL`. Valor: a URL HTTPS do seu servidor, sem barra no final (ex.: `https://seu-servidor.example.com`). Não use `localhost`.
4. Abra a aba **Actions**, selecione **Build Android APK** e toque em **Run workflow**. Se a aba Actions pedir autorização, habilite workflows para o repositório.
5. Aguarde o workflow terminar com sucesso. Abra a execução concluída e baixe o artefato `Shopee-Video-Studio-debug-APK`.
6. Extraia o ZIP do artefato no celular e toque em `app-debug.apk`. Se o Android bloquear, permita temporariamente instalar apps dessa fonte nas configurações. Instale apenas o APK gerado no seu próprio repositório.

## C. Observações
- O APK do workflow é de teste (debug), não é uma versão assinada para publicação na Play Store.
- Se o build falhar, abra a execução em Actions e leia o primeiro erro em vermelho.
- A geração de vídeos depende do servidor, das chaves válidas e dos modelos de IA disponíveis. Gerar APK não significa que o serviço de IA esteja automaticamente configurado.
- Proteja as chaves API como variáveis secretas do serviço de hospedagem. Nunca as escreva no JavaScript do app.
- Para produção, adicione autenticação, rate limits, validação de uploads, limpeza de arquivos, fila persistente e monitoramento antes de distribuir o app.
