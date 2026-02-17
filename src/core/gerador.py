import calendar
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment

def traduzir_dia(dia_em_ingles):
    traducoes = {
        "Monday": "Segunda-feira",
        "Tuesday": "Terça-feira",
        "Wednesday": "Quarta-feira",
        "Thursday": "Quinta-feira",
        "Friday": "Sexta-feira",
        "Saturday": "Sábado",
        "Sunday": "Domingo",
    }
    return traducoes.get(dia_em_ingles, dia_em_ingles)


def gerar_calendario(mes: int, ano: int):
    calendario = calendar.monthcalendar(ano, mes)

    dias_do_mes = []

    for semana in calendario:
        for dia in semana:
            if dia != 0:
                data = datetime(ano, mes, dia)
                dia_semana_en = data.strftime("%A")
                dia_semana_pt = traduzir_dia(dia_semana_en)

                eh_final_de_semana = dia_semana_pt in ["Sábado", "Domingo"]

                dias_do_mes.append({
                    "data": data,
                    "dia_semana": dia_semana_pt,
                    "final_de_semana": eh_final_de_semana
                })

    return dias_do_mes

def gerar_excel(nome_arquivo, dados):
    wb = Workbook()
    ws = wb.active
    ws.title = "Folha de Ponto"

    cabecalho = [
        "Data",
        "Dia da Semana",
        "Entrada Manhã",
        "Saída Manhã",
        "Entrada Tarde",
        "Saída Tarde",
        "Total de Horas",
        "Observação"
    ]

    ws.append(cabecalho)

    for cell in ws[1]:
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal="center")

    for linha in dados:
        ws.append(linha)

    wb.save(nome_arquivo)
