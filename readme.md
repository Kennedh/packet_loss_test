# Wi-Fi Stability Tester 📡

Um script em Python leve e direto ao ponto para monitorar a estabilidade da sua conexão com o roteador (ou qualquer outro IP). Ele dispara pacotes de ping em alta frequência para identificar perda de pacotes e picos de latência (lag spikes), gerando um log detalhado em `.csv` ao final do teste.

Ideal para diagnosticar instabilidades locais no Wi-Fi que podem causar desconexões ou atrasos em jogos online e aplicações em tempo real.

## 🚀 Funcionalidades

- **Alta Frequência:** Testa a conexão em intervalos de milissegundos.
- **Simulação de Carga:** Permite alterar o tamanho do pacote para simular tráfego pesado (ex: pacotes de jogos).
- **Detecção de Picos:** Define um limite aceitável de latência e contabiliza tudo o que ultrapassar esse valor.
- **Relatório Automático:** Exporta todos os resultados para um arquivo CSV, incluindo um sumário com taxas de perda e picos.
- **Interrupção Segura:** O teste pode ser interrompido a qualquer momento com `Ctrl+C` sem perder os dados já coletados.

## 📋 Pré-requisitos

O projeto requer o Python 3 instalado e a biblioteca `ping3`.

Você pode instalar a dependência executando:

```bash
pip install ping3
Aviso de Permissão: A biblioteca ping3 envia pacotes ICMP, o que em alguns sistemas operacionais (como Linux ou macOS) pode exigir execução com privilégios de administrador (ex: sudo python main.py).

🛠️ Como usar
Clone o repositório:

Bash
git clone [https://github.com/SEU-USUARIO/wifi-stability-tester.git](https://github.com/SEU-USUARIO/wifi-stability-tester.git)
cd wifi-stability-tester
Abra o arquivo do script e ajuste as Configurações do Teste conforme sua necessidade:

Python
ALVO = "192.168.10.1"  # IP do seu roteador ou destino
TAMANHO_PACOTE = 1000  # Tamanho do pacote em bytes
INTERVALO = 0.01       # Intervalo entre os pings em segundos
DURACAO_TESTE = 120    # Duração total em segundos
LIMITE_PICO_MS = 50.0  # Limite para considerar a latência como "Pico"
Execute o script:

Bash
python main.py
📊 Exemplo de Saída (Console)
Plaintext
[*] Iniciando teste de rede contra 192.168.10.1
[*] Critério de Pico: > 50.0ms
[*] Pressione Ctrl+C para interromper antes do tempo.

[20:15:33.123] Pico Detectado: 65.40 ms
[20:15:35.456] ALERTA: Pacote Perdido!

[*] Gerando arquivo log_picos_wifi.csv...
----------------------------------------
RESUMO DO TESTE FINALIZADO
Enviados:  12000
Picos (> 50.0ms): 12 (0.10%)
Perdidos:  2 (0.02%)