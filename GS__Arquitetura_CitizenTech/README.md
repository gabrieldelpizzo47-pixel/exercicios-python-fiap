# CitizenTech — Sistema de Alerta Inteligente de Enchentes

**Global Solution 2026.2 — Computer Organization and Architecture**

## Simulação online

**Projeto do grupo no Wokwi:** https://wokwi.com/projects/480964155293854721

Este endereço foi compartilhado pelo grupo. O funcionamento foi testado pelo aluno no Wokwi; o link não foi acessível para verificação externa nesta sessão.

## Problema
Alagamentos urbanos podem surpreender moradores e pedestres. O protótipo didático monitora o nível estimado de água e sinaliza estados de normalidade, atenção e perigo.

## Solução
O sensor ultrassônico HC-SR04 é instalado *conceitualmente* a 100 cm do fundo de uma área monitorada. Quanto menor a distância medida até a água, maior o nível estimado. O Raspberry Pi Pico interpreta essa informação, acende um dos três LEDs e ativa o buzzer no estado de perigo. O monitor serial mostra distância, percentual e status.

**Importante:** o Wokwi apenas simula essa instalação. Os limites são ilustrativos, não representam níveis oficiais de alagamento e **não podem ser usados para segurança real**. O protótipo não envia alertas pela internet (uma futura extensão IoT poderia transmitir os dados).

## Componentes
- 1 Raspberry Pi Pico (RP2040)
- 1 sensor ultrassônico HC-SR04
- 3 LEDs: verde, amarelo e vermelho
- 3 resistores de 220 ohms
- 1 buzzer piezoelétrico

## Ligações
| Componente | Pino | Raspberry Pi Pico |
|---|---|---|
| HC-SR04 | TRIG | GP2 |
| HC-SR04 | ECHO | GP3 |
| HC-SR04 | VCC | VBUS (5 V) |
| HC-SR04 | GND | GND |
| LED verde (via 220 ohms) | Ânodo | GP13 |
| LED amarelo (via 220 ohms) | Ânodo | GP14 |
| LED vermelho (via 220 ohms) | Ânodo | GP15 |
| LEDs | Cátodos | GND |
| Buzzer | + | GP16 |
| Buzzer | - | GND |

> Atenção para protótipo físico: o ECHO de um HC-SR04 alimentado a 5 V pode exceder os 3,3 V tolerados pelo Pico. É obrigatório adaptar o nível lógico (ex.: divisor resistivo), além de testar e proteger o circuito. O arquivo diagram.json é destinado à **simulação** no Wokwi.

## Como executar no Wokwi
1. Acesse [a simulação online](https://wokwi.com/projects/480964155293854721).
2. Clique em **Start Simulation**.
3. Clique no sensor HC-SR04 e ajuste o controle de distância.
4. Observe o LED correspondente e o monitor serial; para PERIGO, o buzzer apita.

**Se quiser abrir uma cópia local:** crie um projeto MicroPython Raspberry Pi Pico no Wokwi e substitua `main.py` e `diagram.json` pelos arquivos deste repositório.

## Cálculo
Consideramos a altura de referência de 100 cm:
- `altura_agua_cm = max(0, min(100, 100 - distancia_cm))`
- `nivel_percentual = 100 * altura_agua_cm / 100`

Faixas hipotéticas, aplicadas ao **valor calculado pelo código**:
- **Normal:** percentual < 40%.
- **Atenção:** 40% ≤ percentual < 75%.
- **Perigo:** percentual ≥ 75%.

**Observação nos limites:** o valor configurado no controle do Wokwi pode diferir ligeiramente da distância calculada pelo tempo do eco. O aluno observou verde em 60 cm, amarelo em 59 cm, amarelo em 25 cm e vermelho em 24 cm. Por isso, a demonstração usa valores afastados dos limiares (100, 50 e 10 cm).

## Conceitos de arquitetura de computadores
- **Entrada (I/O):** o ECHO do HC-SR04 gera um pulso digital medido pelo Pico.
- **Processamento:** CPU RP2040 executa MicroPython e converte duração do pulso em distância, altura e classe.
- **Memória:** constantes, variáveis e instruções permanecem em memória durante o processamento.
- **Saída (I/O):** GPIOs controlam os LEDs e PWM produz o sinal para o buzzer.
- **Representação de dados:** valores numéricos de duração, distância e nível; classificação textual do status.

## Testes
Ver `TESTES.md` para os testes e observações comunicadas pelo aluno. Os cenários ainda não registrados devem ser preenchidos depois da execução.

## Demonstração
Veja `ROTEIRO_VIDEO.md` para um roteiro curto da apresentação técnica.

## Referências
- https://docs.wokwi.com/parts/wokwi-hc-sr04
- https://docs.wokwi.com/parts/wokwi-pi-pico
- https://docs.wokwi.com/parts/wokwi-led
- https://docs.wokwi.com/parts/wokwi-buzzer
- https://docs.wokwi.com/guides/micropython
