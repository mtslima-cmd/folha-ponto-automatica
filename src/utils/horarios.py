import random
from datetime import datetime, timedelta


def gerar_horario(base_hora, base_minuto):
    """
    Gera horário com variação de -5 a +5 minutos
    """
    variacao = random.randint(-5, 5)
    horario_base = datetime(2000, 1, 1, base_hora, base_minuto)
    horario_final = horario_base + timedelta(minutes=variacao)

    return horario_final.time()


def gerar_jornada():
    """
    Gera os 4 horários do dia garantindo total de 8 horas
    """

    # Manhã
    entrada_manha = gerar_horario(8, 0)
    saida_manha = gerar_horario(12, 0)

    # Tarde
    entrada_tarde = gerar_horario(14, 0)
    saida_tarde = gerar_horario(18, 0)

    # Garantir que total seja exatamente 8 horas
    dt_base = datetime(2000, 1, 1)

    periodo_manha = (
        datetime.combine(dt_base, saida_manha)
        - datetime.combine(dt_base, entrada_manha)
    )

    periodo_tarde = (
        datetime.combine(dt_base, saida_tarde)
        - datetime.combine(dt_base, entrada_tarde)
    )

    total = periodo_manha + periodo_tarde

    # Ajustar se não der exatamente 8h
    if total != timedelta(hours=8):
        diferenca = timedelta(hours=8) - total
        saida_tarde_dt = datetime.combine(dt_base, saida_tarde) + diferenca
        saida_tarde = saida_tarde_dt.time()

    return entrada_manha, saida_manha, entrada_tarde, saida_tarde
