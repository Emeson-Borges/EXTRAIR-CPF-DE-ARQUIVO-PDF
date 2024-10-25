import pdfplumber


def extract_cpfs_from_pdf(pdf_path, output_txt_path):
    # Abrir o PDF
    with pdfplumber.open(pdf_path) as pdf:
        cpfs = []

        # Iterar por todas as páginas do PDF (se houver mais de uma)
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.split("\n")

                # Procurar a coluna de CPFs
                for line in lines:
                    # Verificar se a linha tem um CPF válido (usando o comprimento como filtro básico)
                    # Aqui, estamos considerando que os CPFs têm 11 dígitos
                    parts = line.split()
                    for part in parts:
                        if len(part) == 11 and part.isdigit():
                            cpfs.append(part)

    # Salvar os CPFs no formato desejado (cpf1, cpf2, cpf3,...)
    with open(output_txt_path, "w") as f:
        f.write(",".join(cpfs))
    print(f"CPFs extraídos e salvos em: {output_txt_path}")


# Exemplo de uso
pdf_path = "C:/Users/itarg/Downloads/pasta_do_arquivo/ARQUIVO.pdf"
output_txt_path = "C:/Users/itarg/Downloads/CPFs.txt"
extract_cpfs_from_pdf(pdf_path, output_txt_path)
