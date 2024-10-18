from django.shortcuts import render
from .models import Piscina

def calcular_dosificacion(request):
    if request.method == "POST":
        largo = float(request.POST.get("largo"))
        ancho = float(request.POST.get("ancho"))
        profundidad = float(request.POST.get("profundidad"))
        conc_inicial = float(request.POST.get("conc_inicial"))
        tipo_piscina = request.POST.get("tipo_piscina")  # Público o privado

        # Crea un objeto 'Piscina' y calcula el volumen
        piscina = Piscina(largo=largo, ancho=ancho, profundidad=profundidad)
        volumen = piscina.volumen  # Volumen en metros cúbicos

        # Convertimos el volumen de metros cúbicos a litros
        litros = volumen * 1000

        # Definir la concentración deseada según el tipo de piscina
        if tipo_piscina == "publica":
            conc_deseada = 5.0  # 5 ppm para piscina pública
        else:
            conc_deseada = 3.0  # 3 ppm para piscina privada

        # Cálculo de cloro necesario para alcanzar la concentración deseada en gramos
        cloro_gramos = (conc_deseada - conc_inicial) * (litros / 1000)
        # Convertir de gramos a onzas
        cloro_onzas = cloro_gramos / 28.3495

        # Cálculo de alguicida
        # Alguicida (shock): 80 mL por 1,000 litros
        # Alguicida (mantenimiento): 5 mL por 1,000 litros
        alguicida_ml_shock = (80 / 1000) * litros
        alguicida_ml_mantenimiento = (5 / 1000) * litros

        # Cálculo de clarificador
        # Clarificador (shock): 10 mL por 1,000 litros
        # Clarificador (mantenimiento): 3 mL por 1,000 litros
        clarificador_ml_shock = (10 / 1000) * litros
        clarificador_ml_mantenimiento = (3 / 1000) * litros

        # Renderizar los resultados
        return render(request, 'calculos/resultados_cloro.html', {
            "cloro_onzas": cloro_onzas,
            "alguicida_ml_shock": alguicida_ml_shock,
            "alguicida_ml_mantenimiento": alguicida_ml_mantenimiento,
            "clarificador_ml_shock": clarificador_ml_shock,
            "clarificador_ml_mantenimiento": clarificador_ml_mantenimiento,
            "tipo_piscina": tipo_piscina,
        })

    return render(request, 'calculos/calculadora_cloro.html')