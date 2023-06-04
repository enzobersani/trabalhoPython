def verificar_anagrama(string1, string2):
    return sorted(string1.replace(" ", "").lower()) == sorted(string2.replace(" ", "").lower())

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

resultado = "são anagramas" if verificar_anagrama(string1, string2) else "não são anagramas"
print(f"As strings {resultado}.")

