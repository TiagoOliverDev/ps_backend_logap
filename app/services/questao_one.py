import time

def encontrar_vogal_especial(entrada: str):
    inicio = time.time()
    
    vogais = 'aeiouAEIOU'
    contagem_vogais = {}
    encontrou_consoante_apos_vogal = False
    primeira_consoante_apos_vogal = None
    
    for char in entrada:
        if char in vogais:
            if char in contagem_vogais:
                contagem_vogais[char] += 1
            else:
                contagem_vogais[char] = 1
    
    for i in range(len(entrada) - 1):
        char = entrada[i]
        if char in vogais:
            if entrada[i + 1] not in vogais:
                if not encontrou_consoante_apos_vogal:
                    primeira_consoante_apos_vogal = i + 1
                    encontrou_consoante_apos_vogal = True
                    break
    
    vogal_alvo = None
    if primeira_consoante_apos_vogal is not None:
        for i in range(primeira_consoante_apos_vogal, len(entrada)):
            char = entrada[i]
            if char in vogais and contagem_vogais[char] == 1:
                vogal_alvo = char
                break
    
    fim = time.time()
    tempo_total_ms = int((fim - inicio) * 1000)
    
    return {
        "string": entrada,
        "vogal": vogal_alvo,
        "tempoTotal": f"{tempo_total_ms}ms"
    }

