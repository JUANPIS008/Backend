from operators import insertUsuarios, get_horarios_disponibles
insertUsuarios("JuanJose", "Juanjo", "CC", 123454634, "2000-01-01")

horarios = get_horarios_disponibles()
for h in horarios:
    print (h)
