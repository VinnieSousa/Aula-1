from plyer import notification
from datetime import datetime

def alerta(nivel, base, etapa):
  if nivel == 1:
    alarme ='Alerta Baixo'
  elif nivel == 2:
    alarme ='Alerta Médio'
  elif nivel == 3:
    alarme ='Alerta Alto'
  falha = (f"Falha no carregamento da base {base} na etapa {etapa}. \n {datetime.today()}")

  notification.notify(
    title = alarme,
    message = falha,
    app_name = "Python",
    timeout = 10
  )

alerta(1,'pessoa','correr')