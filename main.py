import os
import datetime as dt
import tkinter as tk
from tkinter import filedialog, messagebox

import ttkbootstrap as tb
from ttkbootstrap.constants import *

from src.core.gerador import gerar_calendario, gerar_excel
from src.utils.horarios import gerar_jornada, gerar_horario
from src.utils.feriados import obter_feriados_2026


def montar_dados_excel(mes_numero: int, ano: int):
    dias = gerar_calendario(mes_numero, ano)
    feriados = obter_feriados_2026()

    dados_excel = []

    for dia in dias:
        data_atual = dia["data"].date()
        data_str = dia["data"].strftime("%d/%m/%Y")
        dia_semana = dia["dia_semana"]

        # Final de semana
        if dia["final_de_semana"]:
            dados_excel.append([data_str, dia_semana, "", "", "", "", "", "Final de Semana"])
            continue

        # Feriados / pontos facultativos
        if data_atual in feriados:
            tipo = feriados[data_atual]

            if tipo == "feriado":
                dados_excel.append([data_str, dia_semana, "", "", "", "", "", "Feriado"])
                continue

            if tipo == "ponto_facultativo":
                dados_excel.append([data_str, dia_semana, "", "", "", "", "", "Ponto Facultativo"])
                continue

            if tipo == "ponto_facultativo_parcial":
                # Somente tarde (4h)
                entrada_t = gerar_horario(14, 0)
                dt_base = dt.datetime(2000, 1, 1)
                entrada_dt = dt.datetime.combine(dt_base.date(), entrada_t)
                saida_dt = entrada_dt + dt.timedelta(hours=4)
                saida_t = saida_dt.time()

                dados_excel.append([
                    data_str, dia_semana, "", "",
                    entrada_t.strftime("%H:%M"), saida_t.strftime("%H:%M"),
                    "04:00", "Meio Expediente"
                ])
                continue

        # Dia útil normal (8h)
        entrada_m, saida_m, entrada_t, saida_t = gerar_jornada()
        dados_excel.append([
            data_str, dia_semana,
            entrada_m.strftime("%H:%M"), saida_m.strftime("%H:%M"),
            entrada_t.strftime("%H:%M"), saida_t.strftime("%H:%M"),
            "08:00", ""
        ])

    return dados_excel


def escolher_pasta():
    pasta = filedialog.askdirectory(title="Selecione a pasta para salvar o Excel")
    if pasta:
        pasta_var.set(pasta)
        set_status("", style="secondary")
        btn_abrir.grid_remove()


def abrir_pasta():
    pasta = pasta_var.get().strip()
    if pasta and os.path.isdir(pasta):
        os.startfile(pasta)


def set_status(msg: str, style: str = "secondary"):
    status_var.set(msg)
    status_label.configure(bootstyle=style)


def limpar():
    combo_mes.current(0)
    pasta_var.set("")
    set_status("", style="secondary")
    btn_abrir.grid_remove()


def gerar():
    mes_selecionado = combo_mes.get()
    mes_numero = int(mes_selecionado.split(" - ")[0])
    ano_atual = dt.datetime.now().year

    pasta = pasta_var.get().strip()
    if not pasta:
        set_status("⚠️ Escolha uma pasta para salvar o arquivo.", style="warning")
        return

    set_status("Gerando... aguarde", style="info")
    app.update_idletasks()

    dados = montar_dados_excel(mes_numero, ano_atual)

    nome_arquivo = f"Folha_Ponto_{mes_numero:02d}_{ano_atual}.xlsx"
    caminho = os.path.join(pasta, nome_arquivo)

    try:
        gerar_excel(caminho, dados)
    except Exception as e:
        set_status(f"❌ Erro ao gerar: {e}", style="danger")
        return

    # ✅ Feedback forte
    set_status("✅ Arquivo gerado e salvo com sucesso na pasta selecionada.", style="success")

    # Popup confirmando
    messagebox.showinfo(
    "Sucesso!",
    f"Arquivo gerado com sucesso!\n\nNome:\n{nome_arquivo}\n\nSalvo em:\n{pasta}"
    )

    # Mostrar botão abrir pasta
    btn_abrir.grid(row=6, column=0, columnspan=2, sticky=W, pady=(10, 0))


# ===== UI CLEAN + CENTRAL =====
app = tb.Window(themename="litera")
app.title("Folha de Ponto Automática")
app.geometry("680x380")
app.resizable(False, False)

container = tb.Frame(app)
container.place(relx=0.5, rely=0.5, anchor="center")

card = tb.Frame(container, padding=26, bootstyle="light")
card.grid(row=0, column=0)

# Header
tb.Label(
    card,
    text="Folha de Ponto Automática",
    font=("Segoe UI", 20, "bold"),
    bootstyle="dark"
).grid(row=0, column=0, columnspan=2, sticky=W)

tb.Label(
    card,
    text="Selecione o mês, escolha a pasta e clique em Gerar.",
    font=("Segoe UI", 11),
    bootstyle="secondary"
).grid(row=1, column=0, columnspan=2, sticky=W, pady=(6, 18))

# Mês
tb.Label(card, text="Mês", font=("Segoe UI", 11, "bold")).grid(row=2, column=0, sticky=W, pady=(0, 10))

meses = [
    "01 - Janeiro", "02 - Fevereiro", "03 - Março", "04 - Abril",
    "05 - Maio", "06 - Junho", "07 - Julho", "08 - Agosto",
    "09 - Setembro", "10 - Outubro", "11 - Novembro", "12 - Dezembro"
]
combo_mes = tb.Combobox(card, values=meses, state="readonly", width=30)
combo_mes.grid(row=2, column=1, sticky=W, pady=(0, 10))
combo_mes.current(0)

# Pasta
tb.Label(card, text="Salvar em", font=("Segoe UI", 11, "bold")).grid(row=3, column=0, sticky=W, pady=(0, 10))

pasta_var = tb.StringVar(value="")
entry_pasta = tb.Entry(card, textvariable=pasta_var, width=32)
entry_pasta.grid(row=3, column=1, sticky=W, pady=(0, 10))

btn_pasta = tb.Button(card, text="Escolher…", command=escolher_pasta, bootstyle="secondary-outline", width=12)
btn_pasta.grid(row=3, column=1, sticky=E, pady=(0, 10))

# Botões
btns = tb.Frame(card)
btns.grid(row=4, column=0, columnspan=2, sticky=W, pady=(10, 0))

tb.Button(btns, text="Gerar Excel", command=gerar, bootstyle="success", width=18).grid(row=0, column=0)
tb.Button(btns, text="Limpar", command=limpar, bootstyle="secondary-outline", width=10).grid(row=0, column=1, padx=(10, 0))

# Status
status_var = tb.StringVar(value="")
status_label = tb.Label(
    card,
    textvariable=status_var,
    font=("Segoe UI", 11, "bold"),
    bootstyle="secondary"
)
status_label.grid(row=5, column=0, columnspan=2, sticky=W, pady=(14, 0))

# Abrir pasta (aparece só após gerar)
btn_abrir = tb.Button(
    card,
    text="Abrir Pasta",
    command=abrir_pasta,
    bootstyle="info-outline",
    width=18
)
btn_abrir.grid_remove()

app.mainloop()
