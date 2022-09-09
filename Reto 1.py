salarioMensual, horasExtras, bonificacion = input().split()
salarioMensual= float(salarioMensual)
horasExtras= int(horasExtras)
bonificacion= int(bonificacion)
horasTrabajo = 192
valorHora = salarioMensual / horasTrabajo
valorHoraExtra = valorHora * 1.25
valorbonificacion = bonificacion*(salarioMensual*0.05)
salarioTotal= (horasTrabajo*valorHora+valorHoraExtra*horasExtras+valorbonificacion)
descuentos= 0.085*salarioTotal
salarioFinal = salarioTotal-descuentos
print(round(salarioFinal,1))








