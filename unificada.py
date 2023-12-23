import pandas as pd

# importar arquivo
caminho_unificada = "09.2023 - Impostos e Retidos.xlsx"
unificada_df = pd.read_excel(caminho_unificada, header=8)
#print(unificada_df.to_string())

# fazer limpeza geral e criar função padrão

#apagar linhas em branco da primeira coluna
# Remover linhas com valores NaN na coluna "Prestador"
dados_unificada_sem_nan = unificada_df.dropna(subset=['Prestador'])
#print(dados_unificada_sem_nan)

# Exibir os nomes das colunas
#nomes_colunas = unificada_df.columns
#print(nomes_colunas)

#excluir colunas não usáveis
colunas_para_excluir = ['CNPJ Prestador', 'Simples',
       'Serviço', 'Pagamentos', 'IRRF', 'CSRF',
       'INSS', 'ISS', 'Cód IRRF', 'Cód PCC',
       'Base Cal. INSS', 'Base Cal. ISS',
       'Descontos', 'Valor Líquido', 'P.A IR', 'P.A PCC', 'P.A INSS',
       'P.A ISS', 'Descrição']
dados_sem_colunas = unificada_df.drop(columns=colunas_para_excluir)
dadosv2_df = dados_sem_colunas
dadosv2_df['CÓD'] = ""
dadosv2_df['Débito'] = ""
dadosv2_df['Crédito'] = ""
dadosv2_df['Histórico'] = ""
dadosv2_df['H1'] = ""
#print(dadosv2_df.to_string())

# fazer a limpeza para notas
notas_colunas_para_excluir = ['Valor IRRF', 'Valor CSRF', 'Valor INSS','Valor ISS', 'Caução']
notas = dadosv2_df.drop(columns=notas_colunas_para_excluir)
notas = notas.rename(columns={'Valor Bruto': 'Valor'})
print(notas.to_string())

# fazer a limpeza para irrf
irrf_colunas_para_excluir = ['Valor Bruto', 'Valor CSRF', 'Valor INSS','Valor ISS', 'Caução']
irrf = dadosv2_df.drop(columns=irrf_colunas_para_excluir)
irrf = irrf.dropna(subset='Valor IRRF')
irrf = irrf[irrf['Valor IRRF'] != 0]
irrf = irrf.rename(columns={'Valor IRRF': 'Valor'})
irrf['H1'] = 'IRRF S/ '
#print(irrf.to_string())

# fazer a limpeza para pcc
pcc_colunas_para_excluir = ['Valor Bruto', 'Valor IRRF', 'Valor INSS','Valor ISS', 'Caução']
pcc = dadosv2_df.drop(columns=pcc_colunas_para_excluir)
pcc = pcc.dropna(subset='Valor CSRF')
pcc = pcc[pcc['Valor CSRF'] != 0]
pcc = pcc.rename(columns={'Valor CSRF': 'Valor'})
pcc['H1'] = 'PCC S/ '
#print(pcc.to_string())

# fazer a limpeza para inss
inss_colunas_para_excluir = ['Valor Bruto', 'Valor IRRF', 'Valor CSRF','Valor ISS', 'Caução']
inss = dadosv2_df.drop(columns=inss_colunas_para_excluir)
inss = inss.dropna(subset='Valor INSS')
inss = inss[inss['Valor INSS'] != 0]
inss = inss.rename(columns={'Valor INSS': 'Valor'})
inss['H1'] = 'INSS S/ '
#print(inss.to_string())

# fazer a limpeza para iss
iss_colunas_para_excluir = ['Valor Bruto', 'Valor IRRF', 'Valor CSRF', 'Valor INSS', 'Caução']
iss = dadosv2_df.drop(columns=iss_colunas_para_excluir)
iss = iss.dropna(subset='Valor ISS')
iss = iss[iss['Valor ISS'] != 0]
iss = iss.rename(columns={'Valor ISS': 'Valor'})
iss['H1'] = 'ISS S/ '
#print(iss.to_string())

# fazer a limpeza para caução
caucao_colunas_para_excluir = ['Valor Bruto', 'Valor IRRF', 'Valor CSRF', 'Valor INSS', 'Valor ISS']
caucao = dadosv2_df.drop(columns=caucao_colunas_para_excluir)
caucao = caucao.dropna(subset='Caução')
caucao = caucao[caucao['Caução'] != 0]
caucao = caucao.rename(columns={'Caução': 'Valor'})
#print(caucao.to_string())

# fazer a limpeza para devoluções

# juntar irrf, pcc, iss, inss
lista_impostos = [irrf, pcc, inss, iss]
impostos = pd.concat(lista_impostos)
impostos['Débito'] = '2.01.02.01.0001'
def mapear_credito(valor_h1):
    if 'IRRF' in valor_h1:
        return '1.02.04.02.001'
    elif 'INSS' in valor_h1:
        return '1.02.04.02.003'
    elif 'PCC' in valor_h1:
        return '1.02.04.02.004'
    elif 'ISS' in valor_h1:
        return '1.02.04.02.005'
    else:
        return None

impostos['Crédito'] = impostos['H1'].apply(mapear_credito)
impostos['Histórico'] = ""
impostos = impostos[['CÓD', 'Débito', 'Crédito','Emissão', 'Valor', 'Histórico', 'H1', 'Tipo', 'Nº Nota Fiscal', 'Prestador']]
print(impostos.to_string())

#formatar para ficar igual o modelo de cargas
#notas
#impostos

#Ordenação: df.sort_values(by='coluna', ascending=False).



# fazer a cópia de cada um: notas, retidos, caução, devolução separados