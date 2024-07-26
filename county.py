countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

# Unión de todos los conjuntos
new_set = countries | northAm | centralAm | southAm
print(new_set)  # Debería imprimir todos los países únicos en estos conjuntos


