# 🎙️ Whisper Audio Transcriber

Este projeto utiliza o [OpenAI Whisper](https://github.com/openai/whisper) para transcrever arquivos de áudio em texto, gerando também **timestamps** por segmento reconhecido.

## 🚀 Funcionalidade
- Aceita arquivos de áudio (`.mp3`, `.wav`, `.m4a`, etc.).
- Carrega um modelo do Whisper (versão `base` por padrão).
- Gera automaticamente um arquivo `.txt` **no diretório atual**, com o mesmo nome do áudio de entrada.
- Inclui os **tempos de início e fim** de cada trecho falado.

## 📦 Requisitos
- Python 3.8 ou superior
- Dependências listadas em [Whisper](https://github.com/openai/whisper)
- `ffmpeg` instalado no sistema (necessário para processamento de áudio)

## 🔧 Instalação

Clone este repositório:

```bash
git clone https://github.com/SEU_USUARIO/whisper-transcriber.git
cd whisper-transcriber
```

Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

Instale as dependências:

```bash
pip install openai-whisper
pip install torch  # caso ainda não tenha
```

⚠️ Lembre-se de instalar também o ffmpeg:

- Linux (Debian/Ubuntu): sudo apt install ffmpeg
- Mac (brew): brew install ffmpeg
- Windows: [https://ffmpeg.org/download.html?utm_source=chatgpt.com]Download aqui

▶️ Uso

Coloque seu arquivo .mp3 no diretório do projeto e execute:

```bash
python transcribe.py caminho/para/meu_audio.mp3
```

O script:

- Lerá o arquivo de áudio no caminho informado
- Criará o arquivo meu_audio.txt no diretório atual

📂 Exemplos

Áudio na mesma pasta:

```python
python transcribe.py meu_audio.mp3
```
# Saída: ./meu_audio.txt

Áudio em subpasta:

```python
python transcribe.py audios/meu_audio.mp3
```
# Saída: ./meu_audio.txt

Áudio em outro diretório:

```python
python transcribe.py "C:/Users/Usuario/Music/meu_audio.mp3"
```
# Saída: ./meu_audio.txt

📂 Exemplo de saída:

[0.00s - 5.20s] Olá, bem-vindo ao projeto!
[5.21s - 10.85s] Este é um teste de transcrição usando Whisper.

⚙️ Configurações

Para trocar o modelo (tiny, base, small, medium, large), edite no código:

```python
model = whisper.load_model("base")
```

Para alterar o arquivo de entrada/saída, modifique os nomes no código.