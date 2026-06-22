import ping3
import time
import csv
from datetime import datetime

# ==========================================
# CONFIGURAÇÕES DO TESTE
# ==========================================
ALVO = "192.168.10.1"  # Substitua pelo IP do roteador
TAMANHO_PACOTE = 1000  # Simula pacote gordo de jogo
INTERVALO = 0.01  # 10 milissegundos
DURACAO_TESTE = 120  # Tempo em segundos
NOME_ARQUIVO = "log_picos_wifi.csv"
LIMITE_PICO_MS = 50.0  # Acima desse valor, é contabilizado como "Pico Alto"


# ==========================================

def executar_teste():
    resultados = []
    inicio_teste = time.time()

    contagem = {
        "enviados": 0,
        "perdidos": 0,
        "picos_altos": 0,
        "normais": 0
    }

    print(f"[*] Iniciando teste de rede contra {ALVO}")
    print(f"[*] Critério de Pico: > {LIMITE_PICO_MS}ms")
    print("[*] Pressione Ctrl+C para interromper antes do tempo.\n")

    try:
        while time.time() - inicio_teste < DURACAO_TESTE:
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]

            latencia_segundos = ping3.ping(ALVO, size=TAMANHO_PACOTE, timeout=1)
            contagem["enviados"] += 1

            if latencia_segundos is False or latencia_segundos is None:
                status = "Perdido"
                latencia_ms = 0.0
                contagem["perdidos"] += 1
                print(f"[{timestamp}] ALERTA: Pacote Perdido!")
            else:
                latencia_ms = latencia_segundos * 1000

                if latencia_ms >= LIMITE_PICO_MS:
                    status = "Pico Alto"
                    contagem["picos_altos"] += 1
                    print(f"[{timestamp}] Pico Detectado: {latencia_ms:.2f} ms")
                else:
                    status = "Normal"
                    contagem["normais"] += 1

            resultados.append([timestamp, status, round(latencia_ms, 2)])
            time.sleep(INTERVALO)

    except KeyboardInterrupt:
        print("\n[!] Teste interrompido.")

    # Salvando no CSV e anexando o sumário nas últimas linhas
    print(f"\n[*] Gerando arquivo {NOME_ARQUIVO}...")
    with open(NOME_ARQUIVO, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Cabeçalho dos dados
        writer.writerow(["Horario", "Status", "Latencia_ms"])
        # Dados de cada pacote
        writer.writerows(resultados)

        # Linhas em branco para separar
        writer.writerow([])
        writer.writerow([])

        # Sumário no próprio CSV
        writer.writerow(["--- RESUMO DO TESTE ---", "", ""])
        writer.writerow(["Total Enviados", contagem["enviados"], ""])
        writer.writerow(["Total Normais", contagem["normais"], ""])
        writer.writerow(["Total Picos Altos", contagem["picos_altos"], f"(> {LIMITE_PICO_MS}ms)"])
        writer.writerow(["Total Perdidos", contagem["perdidos"], ""])

        perda_pct = (contagem["perdidos"] / contagem["enviados"]) * 100 if contagem["enviados"] > 0 else 0
        picos_pct = (contagem["picos_altos"] / contagem["enviados"]) * 100 if contagem["enviados"] > 0 else 0
        writer.writerow(["Taxa de Perda", f"{perda_pct:.2f}%", ""])
        writer.writerow(["Taxa de Picos", f"{picos_pct:.2f}%", ""])

    # Exibindo no console
    print("-" * 40)
    print("RESUMO DO TESTE FINALIZADO")
    print(f"Enviados:  {contagem['enviados']}")
    print(f"Picos (> {LIMITE_PICO_MS}ms): {contagem['picos_altos']} ({picos_pct:.2f}%)")
    print(f"Perdidos:  {contagem['perdidos']} ({perda_pct:.2f}%)")
    print("-" * 40)


if __name__ == "__main__":
    executar_teste()