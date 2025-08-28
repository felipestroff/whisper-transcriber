import sys
import os
import whisper

def main():
    # Verifica se o usuário passou o arquivo de áudio como argumento
    if len(sys.argv) < 2:
        print("Uso: python transcribe.py <arquivo_de_audio>")
        sys.exit(1)

    audio_file = sys.argv[1]

    # Verifica se o arquivo existe
    if not os.path.isfile(audio_file):
        print(f"Erro: arquivo '{audio_file}' não encontrado.")
        sys.exit(1)

    # Define nome de saída (.txt) sempre no diretório atual
    base_name, _ = os.path.splitext(os.path.basename(audio_file))
    output_file = base_name + ".txt"

    # Carrega o modelo Whisper (pode ser 'tiny', 'base', 'small', 'medium', 'large')
    model = whisper.load_model("base")

    # Transcreve o arquivo de áudio
    result = model.transcribe(audio_file, verbose=True)

    # Salva a transcrição segmentada em arquivo .txt no diretório atual
    with open(output_file, "w", encoding="utf-8") as f:
        for segment in result["segments"]:
            start = segment["start"]
            end = segment["end"]
            text = segment["text"].strip()
            timestamp = f"[{start:0.2f}s - {end:0.2f}s]"
            f.write(f"{timestamp} {text}\n")

    print(f"✅ Transcrição concluída! Arquivo salvo em: {output_file}")


if __name__ == "__main__":
    main()
