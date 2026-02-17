from datetime import date


def obter_feriados_2026():
    """
    Retorna um dicionário com as datas da Portaria 2026
    Tipos:
    - "feriado"
    - "ponto_facultativo"
    - "ponto_facultativo_parcial"
    """

    return {
        # Feriados Nacionais
        date(2026, 1, 1): "feriado",
        date(2026, 4, 3): "feriado",     # Sexta-feira Santa
        date(2026, 4, 21): "feriado",
        date(2026, 5, 1): "feriado",
        date(2026, 9, 7): "feriado",
        date(2026, 10, 12): "feriado",
        date(2026, 11, 2): "feriado",
        date(2026, 11, 15): "feriado",
        date(2026, 12, 25): "feriado",

        # Pontos facultativos integrais
        date(2026, 2, 16): "ponto_facultativo",  # Carnaval
        date(2026, 2, 17): "ponto_facultativo",
        date(2026, 6, 4): "ponto_facultativo",   # Corpus Christi

        # Pontos facultativos parciais (meio expediente)
        date(2026, 2, 18): "ponto_facultativo_parcial",  # Quarta Cinzas
        date(2026, 12, 24): "ponto_facultativo_parcial",
        date(2026, 12, 31): "ponto_facultativo_parcial",
    }
