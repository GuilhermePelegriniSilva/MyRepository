from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Relatório Financeiro em Python', align='C', ln=True)
        self.ln(10)
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', align='C')
    def add_table(self, data):
        self.set_font('Arial', '', 10)
        col_width = 190 / len(data[0])
        for row in data:
            for item in row:
                self.cell(col_width, 10, str(item), border=1, align='C')
            self.ln()

def gera_relatorio(dados_financeiros, arquivo_pdf):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, 'Resumo do Relatório Financeiro gerado com Python com extensão FPDF feito por ', ln=True)
    pdf.cell(0, 10, 'Guilherme Pelegrini da Silva:', ln=True)
    pdf.ln(5)
    pdf.add_table(dados_financeiros)
    pdf.output(arquivo_pdf)
    print("Relatório gerado em {arquivo_pdf}. Abra o arquivo .pdf para visualizar o relatório.")

dados_financeiros = []
linhas = int(input("Digite o número de linhas (incluindo cabeçalhos): "))
colunas = int(input("Digite o número de colunas: "))
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = input(f"Digite o dado para a posição [{i}][{j}]: ")
        linha.append(valor)
    dados_financeiros.append(linha)

arquivo_pdf = input("Digite o nome do arquivo com extensão .pdf ao final:")
gera_relatorio(dados_financeiros, arquivo_pdf)