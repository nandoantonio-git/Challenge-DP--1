
# Controle e Análise de Estoque – DASA 

Uma ferramenta em Python para calcular consumo diário de insumos, sugerir níveis ideais de estoque (lead time + safety stock) e detectar faltas/excessos automaticamente. 

## 🎯 Objetivo

O objetivo deste projeto é **identificar anomalias nos registros de consumo de materiais** em unidades operacionais de um hospital (ou outro setor) para detectar inconsistências que possam impactar a eficiência do estoque. Muitas vezes, falhas nos registros de consumo podem resultar em **estoques incorretos**, seja por **excesso** ou **falta** de materiais, afetando diretamente a operação e os custos da instituição. 

Neste projeto, são simulados registros de **entrada e saída de materiais**, e **técnicas de análise estatística** são aplicadas para detectar desvios significativos e **identificar padrões fora do comportamento esperado**. São usadas métricas como **Z-score**, **intervalo interquartil (IQR)**, e **desvios padrão** para detectar outliers e garantir a visibilidade dos estoques.

No final, o código cria um relatório de **alertas** para indicar itens que estão **em falta** ou **em excesso**, e uma simulação de impacto financeiro é realizada para destacar como falhas de registro podem afetar o custo operacional.

### Como Funciona:

1. **Carregamento dos Dados**:
   O código carrega os dados do arquivo Excel que contém informações sobre o consumo de materiais e o estoque de cada um.

2. **Cálculo do Consumo Diário**:
   Para cada material, é calculado o **consumo diário**. O consumo é obtido subtraindo o estoque no final do dia pelo estoque inicial, garantindo que o valor do consumo não seja negativo.

3. **Cálculo do Estoque Ideal**:
   O estoque ideal é calculado com base em um **lead time** (tempo de reposição) de 7 dias, além de um fator de segurança baseado no desvio padrão do consumo.

4. **Comparação entre Estoque Real e Ideal**:
   O código compara o estoque real (último valor registrado) com o estoque ideal e identifica itens que estão **em falta** (estoque real abaixo do ideal) e **em excesso** (estoque real acima do ideal).

5. **Relatório de Alertas**:
   A função de análise gera um relatório com a lista de itens em falta e em excesso, e imprime essas informações no console.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **[Implantação](#-implantação)** para saber como implantar o projeto.

### 📋 Pré-requisitos

De que coisas você precisa para instalar o software e como instalá-lo?

```
- Python 3.10 ou superior
- pip (gerenciador de pacotes do Python)
```

Instale as dependências do projeto:

```
pip install pandas numpy openpyxl
```

### 🔧 Instalação

```
1. Clone ou copie o repositório para sua máquina local.
2. Coloque o arquivo DasaMatHosp.xlsx na mesma pasta onde está o script main.py.
3. Navegue até o diretório do projeto no terminal.
4. Execute o arquivo main.py com o Python.
```

E repita:

```
python main.py
```
Ao executar o script, o console exibirá:

- Estoque ideal calculado por material.
- Estoque atual com base no último registro.
- Lista de materiais em falta.
- Lista de materiais em excesso.

## 📦 Implantação

O projeto foi desenvolvido para ser executado localmente, podendo ser adaptado para uso em rotinas de ETL, painéis de BI hospitalar, ou integração com sistemas de gestão de estoque.

## 🛠️ Construído com

* [Python](https://www.python.org/) - Linguagem de programação
* [Pandas](https://pandas.pydata.org/) - Manipulação de dados
* [NumPy](https://numpy.org/) - Cálculos numéricos
* [OpenPyXL](https://openpyxl.readthedocs.io/) - Leitura de arquivos Excel

## ✒️ Integrantes

*  Eduardo Dallabella - 556803
*  Fernando Luiz - 555201
*  Heloísa Real - 554535
*  Mariana Dourado - 550494
*  Thomas Reichmann - 554812

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.


