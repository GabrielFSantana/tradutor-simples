from deep_translator import GoogleTranslator

def traduzir_texto(texto, idioma_destino='en'):
    try:
        traducao = GoogleTranslator(target=idioma_destino).translate(texto)
        print(f"\nTexto original: {texto}")
        print(f"Tradução ({idioma_destino}): {traducao}")
    except Exception as e:
        print("Erro ao traduzir:", e)

def main():
    print("Bem-vindo ao Tradutor Simples!")
    print("Digite 'sair' para encerrar o programa.\n")

    while True:
        texto = input("Digite o texto para traduzir: ")
        if texto.lower() == 'sair':
            print("Encerrando o programa. Até logo!")
            break

        idioma_destino = input("Digite o idioma de destino (ex.: 'en' para inglês, 'es' para espanhol): ").strip()
        traduzir_texto(texto, idioma_destino)

if __name__ == "__main__":
    main()
