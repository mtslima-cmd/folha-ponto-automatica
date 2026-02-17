# 🕒 Folha de Ponto Automática

Aplicativo desktop para geração automática de folha de ponto mensal em Excel, com interface moderna e regras oficiais de jornada de trabalho.

Desenvolvido em Python com interface gráfica e geração automatizada de planilha formatada.

---

## ✨ Funcionalidades

- Interface gráfica moderna (ttkbootstrap)
- Seleção de mês
- Escolha da pasta onde o arquivo será salvo
- Geração automática de planilha Excel (.xlsx)
- Layout profissional do Excel:
  - Cabeçalho formatado
  - Bordas e alinhamento automático
  - Ajuste automático de largura de colunas
  - Destaque visual para finais de semana
  - Destaque visual para feriados e pontos facultativos
  - Total mensal calculado automaticamente
- Regras de jornada:
  - Horário padrão: 08:00–12:00 e 14:00–18:00
  - Variação automática de ±5 minutos
  - Total diário fixo de 8 horas
  - Ponto facultativo parcial: apenas período da tarde (4h)
- Considera automaticamente:
  - Sábados
  - Domingos
  - Feriados nacionais 2026
  - Pontos facultativos 2026
  - Pontos facultativos parciais 2026

---

## 🧰 Tecnologias Utilizadas

- Python 3.12+
- ttkbootstrap (Interface gráfica moderna)
- openpyxl (Geração e formatação do Excel)
- PyInstaller (Geração do executável)

---

## 🚀 Como Executar em Modo Desenvolvimento

Clone o repositório:

    git clone https://github.com/SEU_USUARIO/folha-ponto-automatica.git
    cd folha-ponto-automatica

Crie o ambiente virtual:

    python -m venv .venv

Ative o ambiente (Windows):

    .venv\Scripts\activate

Instale as dependências:

    pip install -r requirements.txt

Execute o aplicativo:

    python main.py

---

## 🏗️ Gerar Executável (.exe)

Com o ambiente virtual ativado:

    pyinstaller --onefile --windowed --name "FolhaPontoAutomatica" --icon assets/icon.ico main.py

O executável será gerado em:

    dist/FolhaPontoAutomatica.exe

---

## 📦 Distribuição

Você pode compartilhar o arquivo:

    dist/FolhaPontoAutomatica.exe

Recomenda-se enviar compactado em `.zip`.

⚠️ Em alguns computadores o Windows pode exibir aviso do SmartScreen por ser um executável não assinado.  
Basta clicar em:

- Mais informações  
- Executar assim mesmo  

Ou:

- Botão direito no arquivo  
- Propriedades  
- Marcar "Desbloquear"  

---

## 📂 Estrutura do Projeto

folha-ponto-automatica/
│
├── assets/
│   └── icon.ico
│
├── src/
│   ├── core/
│   │   └── gerador.py
│   │
│   └── utils/
│       ├── feriados.py
│       └── horarios.py
│
├── main.py
├── requirements.txt
└── README.md

---

## 📌 Observações Importantes

- A lista de feriados e pontos facultativos está configurada para o ano de 2026.
- Para atualizar para outro ano, basta editar o arquivo:

    src/utils/feriados.py

---

## 👨‍💻 Autor

Projeto desenvolvido para automação e geração profissional de folha de ponto mensal.
- Mateus Lima | Desenvolvedor Python

---

## 📄 Licença

Este projeto está licenciado sob os termos da licença MIT.

Permissão é concedida, gratuitamente, a qualquer pessoa que obtenha uma cópia deste software e dos arquivos de documentação associados, para usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias do software, desde que o aviso de copyright e esta permissão sejam incluídos em todas as cópias ou partes substanciais do software.

O software é fornecido "como está", sem garantia de qualquer tipo, expressa ou implícita, incluindo, mas não se limitando às garantias de comercialização, adequação a um propósito específico e não violação. Em nenhum caso os autores ou detentores dos direitos autorais serão responsáveis por qualquer reclamação, dano ou outra responsabilidade, seja em ação contratual, delito ou de outra forma, decorrente de, fora de ou em conexão com o software ou o uso ou outras negociações no software.

