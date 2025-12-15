paevad = ["Esmaspäev", "Teisipäev", "Kolmapäev", "Neljapäev", "Reede"]
print(paevad)
print(len(paevad))
paevad.append("Laupäev")
paevad.append("Pühapäev")
print(paevad)
paevad.sort(reverse=True)
print(paevad[-1])