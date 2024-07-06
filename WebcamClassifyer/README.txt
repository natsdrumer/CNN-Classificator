# Reconhecimento de Faces - Aplicação Flask

Este repositório contém um aplicativo web Flask que utiliza um modelo de aprendizado de máquina para reconhecer faces e classificar as imagens capturadas de uma câmera.

## Pré-requisitos

- Python 3.x
- Flask
- OpenCV
- Numpy
- TensorFlow

## Instalação

1. Clone este repositório: `git clone https://github.com/seunghoon/face-recognition-app.git`
2. Navegue até a pasta do repositório: `cd face-recognition-app`
3. Crie um ambiente virtual (opcional): `python -m venv venv` e ative-o:
   - Windows: `.\\venv\\Scripts\\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`

## Uso

1. Coloque o modelo pré-treinado no diretório do repositório com o nome `model_natanael_recognition_TL.h5`.
2. Execute o aplicativo: `python app.py`
3. Acesse a aplicação em seu navegador web em `http://localhost:5000/`

## Funcionamento

A aplicação carrega um modelo pré-treinado de TensorFlow para reconhecer faces. Quando você abrir a página inicial, uma câmera será iniciada e os quadros capturados serão processados pelo modelo. As predições serão exibidas no quadro e podem ser visualizadas em tempo real.

Você pode acessar as seguintes rotas na aplicação:

- `/`: Página inicial que exibe a câmera e as predições.
- `/about`: Página sobre a aplicação.
- `/model`: Página que exibe informações sobre o modelo utilizado.
- `/webcam`: Página que contém apenas a câmera.
- `/video_feed`: Rota que fornece o feed de vídeo processado pelo modelo.

## Atualizações

Para atualizar o código da aplicação, siga estas etapas:

1. Faça as alterações necessárias no código fonte.
2. Salve as alterações.
3. Execute o comando `git pull` para atualizar o repositório local.
4. Execute o comando `pip install -r requirements.txt` para atualizar as dependências, se necessário.
5. Reinicie a aplicação: `python app.py`

## Contribuições

Este repositório é um esboço inicial e pode ser melhorado com contribuições de outras pessoas. Se você deseja contribuir com o código, siga estas etapas:

1. Crie um fork do repositório.
2. Faça as alterações necessárias no código fonte.
3. Envie um pull request para o repositório original.

Obrigado por usar este aplicativo!