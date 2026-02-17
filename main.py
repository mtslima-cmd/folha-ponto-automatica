import tkinter as tk
from tkinter import ttk
import datetime as dt

from src.core.gerador import gerar_calendario, gerar_excel
from src.utils.horarios import gerar_jornada, gerar_horario
from src.utils.feriados import obter_feriados_2026


def gerar_folha():
    mes_selecionado = combo_mes.get()
    ano_atual = dt.datetime.now().year

    # Extrair número do mês (01 - Janeiro → 1)
    mes_numero = int(mes_selecionado.split(" - ")[0])

    dias = gerar_calendario(mes_numero, ano_atual)
    feriados = obter_feriados_2026()

    dados_excel = []

    for dia in dias:
        data_atual = dia["data"].date()
        data_str = dia["data"].strftime("%d/%m/%Y")
        dia_semana = dia["dia_semana"]

        # Final de semana
        if dia["final_de_semana"]:
            dados_excel.append([
                data_str, dia_semana, "", "", "", "", "", "Final de Semana"
            ])
            continue

        # Feriados / pontos facultativos
        if data_atual in feriados:
            tipo = feriados[data_atual]

            if tipo == "feriado":
                dados_excel.append([
                    data_str, dia_semana, "", "", "", "", "", "Feriado"
                ])
                continue

            if tipo == "ponto_facultativo":
                dados_excel.append([
                    data_str, dia_semana, "", "", "", "", "", "Ponto Facultativo"
                ])
                continue

            if tipo == "ponto_facultativo_parcial":
                # Somente tarde (4h)
                entrada_t = gerar_horario(14, 0)

                dt_base = dt.datetime(2000, 1, 1)
                entrada_dt = dt.datetime.combine(dt_base.date(), entrada_t)
                saida_dt = entrada_dt + dt.timedelta(hours=4)
                saida_t = saida_dt.time()

                dados_excel.append([
                    data_str,
                    dia_semana,
                    "", "",
                    entrada_t.strftime("%H:%M"),
                    saida_t.strftime("%H:%M"),
                    "04:00",
                    "Meio Expediente"
                ])
                continue

        # Dia útil normal (8h)
        entrada_m, saida_m, entrada_t, saida_t = gerar_jornada()

        dados_excel.append([
            data_str,
            dia_semana,
            entrada_m.strftime("%H:%M"),
            saida_m.strftime("%H:%M"),
            entrada_t.strftime("%H:%M"),
            saida_t.strftime("%H:%M"),
            "08:00",
            ""
        ])

    nome_arquivo = f"Folha_Ponto_{mes_numero:02d}_{ano_atual}.xlsx"
    gerar_excel(nome_arquivo, dados_excel)

    print(f"Arquivo {nome_arquivo} gerado com sucesso!")


# Janela principal
janela = tk.Tk()
janela.title("Folha de Ponto Automática")
janela.geometry("300x150")
janela.resizable(False, False)

label = tk.Label(janela, text="Selecione o mês:", font=("Arial", 12))
label.pack(pady=10)

meses = [
    "01 - Janeiro", "02 - Fevereiro", "03 - Março", "04 - Abril",
    "05 - Maio", "06 - Junho", "07 - Julho", "08 - Agosto",
    "09 - Setembro", "10 - Outubro", "11 - Novembro", "12 - Dezembro"
]

combo_mes = ttk.Combobox(janela, values=meses, state="readonly")
combo_mes.pack(pady=5)
combo_mes.current(0)

botao = tk.Button(janela, text="Gerar", command=gerar_folha)
botao.pack(pady=10)

janela.mainloop()
