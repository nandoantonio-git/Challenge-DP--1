import pandas as pd
import bisect
import numpy as np

df = pd.read_excel('DasaMatHosp.xlsx')
df['Data e Hora'] = pd.to_datetime(df['DataHora'])
df['dia'] = df['Data e Hora'].dt.date

consumo_diario = {}
for material, grupo in df.sort_values('Data e Hora').groupby('Material'):
    
    consumo = grupo.groupby('dia')['Estoque'].agg(
        lambda x: max(0, x.iloc[0] - x.iloc[-1])
    )
    media = consumo.mean()
    desvio = consumo.std(ddof=0) if len(consumo) > 1 else 0.0
    dias = consumo.size
    consumo_diario[material] = {
        'media_diaria': round(media, 2),
        'desvio_diario': round(desvio, 2),
        'dias_observados': int(dias)
    }

lead_time = 7
fator_seguranca = 1.0
estoque_ideal = {
    mat: int(np.ceil(dados['media_diaria'] * lead_time + fator_seguranca * dados['desvio_diario']))
    for mat, dados in consumo_diario.items()
}

estoque_real = {
    material: grupo.sort_values('Data e Hora')['Estoque'].iloc[-1]
    for material, grupo in df.groupby('Material')
}

def analisar_estoque(real, ideal):
    """
    real: dict(material -> qtd_real)
    ideal: dict(material -> qtd_ideal)
    Retorna duas listas: (faltando, excedente)
    """
    diffs = []
    materiais = set(real) | set(ideal)
    for mat in materiais:
        q_real = real.get(mat, 0)
        q_ideal = ideal.get(mat, 0)
        diffs.append((q_real - q_ideal, mat))
    
    diffs.sort(key=lambda x: x[0])  
    valores = [d for d,_ in diffs]
   
    idx = bisect.bisect_right(valores, 0) 
    faltando  = [m for d,m in diffs[:idx] if d < 0]
    excedente = [m for d,m in diffs[idx:] if d > 0]
    return faltando, excedente

faltas, excessos = analisar_estoque(estoque_real, estoque_ideal)

print("=== Estoque Ideal Calculado ===")
for mat, qt in estoque_ideal.items():
    print(f"{mat}: ideal = {qt}")

print("\n=== Estoque Atual ===")
for mat, qt in estoque_real.items():
    print(f"{mat}: real  = {qt}")

print("\n=== Itens EM FALTA ===")
print(faltas)

print("\n=== Itens EM EXCESSO ===")
print(excessos)
