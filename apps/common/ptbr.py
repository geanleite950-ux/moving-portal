"""Nomes de meses e dias em português do Brasil (independe do locale do SO)."""

MESES = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
MESES_ABREV = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
DIAS = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]


def month_year(d):
    return f"{MESES[d.month - 1]} {d.year}"


def week_range(first, last):
    return f"{first.day:02d} {MESES_ABREV[first.month - 1]} – {last.day:02d} {MESES_ABREV[last.month - 1]} {last.year}"


def full_day(d):
    return f"{DIAS[d.weekday()]}, {d.day} de {MESES[d.month - 1].lower()} de {d.year}"
