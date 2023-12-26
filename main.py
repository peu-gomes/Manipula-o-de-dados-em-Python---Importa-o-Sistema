import pandas as pd

# Leia o arquivo Excel e armazene os dados em dois DataFrames
unificada_aba_recebidas_df = pd.read_excel('09.2023 - Impostos e Retidos.xlsx', sheet_name=0, header=8)
unificada_aba_devolucoes_df = pd.read_excel('09.2023 - Impostos e Retidos.xlsx', sheet_name=2, header=6)

# Manipulação dos dados gerais da aba recebidas
# Exclua as linhas em branco da primeira coluna
unificada_aba_recebidas_apagar_zaradas_df = unificada_aba_recebidas_df.dropna(subset=['Prestador'])
unificada_aba_devolucoes_apagar_zaradas_df = unificada_aba_devolucoes_df.dropna(subset=['Prestador'])

# Lista de colunas para excluir
unificada_aba_recebidas_colunas_para_excluir_df = ['CNPJ Prestador', 'Simples',
'Serviço', 'Pagamentos', 'IRRF', 'CSRF',
'INSS', 'ISS', 'Cód IRRF', 'Cód PCC',
'Base Cal. INSS', 'Base Cal. ISS',
'Descontos', 'Valor Líquido', 'P.A IR', 'P.A PCC', 'P.A INSS',
'P.A ISS', 'Descrição']

unificada_aba_devolucoes_colunas_para_excluir_df = ['CNPJ Prestador',
'Nota Referenciada','Pagamentos', 'Valor Líquido', 'Centro de Custo', 'Descrição']

# Exclua as colunas especificadas na lista anterior
unificada_aba_recebidas_colunas_excluir_colunas_df = unificada_aba_recebidas_apagar_zaradas_df.drop(columns=unificada_aba_recebidas_colunas_para_excluir_df)
unificada_aba_devolucoes_colunas_excluir_colunas_df = unificada_aba_devolucoes_apagar_zaradas_df.drop(columns=unificada_aba_devolucoes_colunas_para_excluir_df)

# Adicione novas colunas
unificada_aba_recebidas_colunas_excluir_colunas_df['CÓD'] = ""
unificada_aba_recebidas_colunas_excluir_colunas_df['Débito'] = ""
unificada_aba_recebidas_colunas_excluir_colunas_df['Crédito'] = ""
unificada_aba_recebidas_colunas_excluir_colunas_df['Histórico'] = ""
unificada_aba_recebidas_colunas_excluir_colunas_df['H1'] = " "

unificada_aba_devolucoes_colunas_excluir_colunas_df['CÓD'] = ""
unificada_aba_devolucoes_colunas_excluir_colunas_df['Débito'] = ""
unificada_aba_devolucoes_colunas_excluir_colunas_df['Crédito'] = ""
unificada_aba_devolucoes_colunas_excluir_colunas_df['Histórico'] = ""
unificada_aba_devolucoes_colunas_excluir_colunas_df['H1'] = "S/"

#alterar nome de variavel para finalizar a manipulacao geral (foi idicionado como a versao 2)
unificada_aba_recebidas_v2_df = unificada_aba_recebidas_colunas_excluir_colunas_df
unificada_aba_devolucoes_v2_df = unificada_aba_devolucoes_colunas_excluir_colunas_df
#print(unificada_aba_devolucoes_v2_df.to_string())
#manipulação notas

notas_columns_para_exclusive = ['Valor IRRF', 'Valor CSRF', 'Valor INSS', 'Valor ISS', 'Caução']
notas = unificada_aba_recebidas_v2_df.drop(columns=notas_columns_para_exclusive)
notas = notas.rename(columns={'Valor Bruto': 'Valor'})
notas = notas[['CÓD', 'Débito', 'Crédito', 'Emissão', 'Valor', 'Histórico', 'Tipo', 'H1', 'Nº Nota Fiscal', 'Prestador']]
notas['H1'] = 'Nº'
notas['Crédito'] = '2.01.02.01.0001'

notas['Valor'] = notas['Valor'].round(2)
#notas['Histórico'] = '=CONCATENAR(H2;" ";I2;" ";J2;" ";K2)'

#manipulação impostos
#manipulação irrf
irrf_colunas_para_excluir = ['Valor Bruto', 'Valor CSRF', 'Valor INSS','Valor ISS', 'Caução']
irrf = unificada_aba_recebidas_v2_df.drop(columns=irrf_colunas_para_excluir)
irrf = irrf.dropna(subset='Valor IRRF')
irrf = irrf[irrf['Valor IRRF'] != 0]
irrf = irrf.rename(columns={'Valor IRRF': 'Valor'})
irrf['H1'] = 'IRRF S/ '

#manipulação pcc
pcc_colunas_para_excluir = ['Valor Bruto', 'Valor IRRF', 'Valor INSS','Valor ISS', 'Caução']
pcc = unificada_aba_recebidas_v2_df.drop(columns=pcc_colunas_para_excluir)
pcc = pcc.dropna(subset='Valor CSRF')
pcc = pcc[pcc['Valor CSRF'] != 0]
pcc = pcc.rename(columns={'Valor CSRF': 'Valor'})
pcc['H1'] = 'PCC S/ '

#manipulação inss
inss_colunas_para_excluir = ['Valor Bruto', 'Valor IRRF', 'Valor CSRF','Valor ISS', 'Caução']
inss = unificada_aba_recebidas_v2_df.drop(columns=inss_colunas_para_excluir)
inss = inss.dropna(subset='Valor INSS')
inss = inss[inss['Valor INSS'] != 0]
inss = inss.rename(columns={'Valor INSS': 'Valor'})
inss['H1'] = 'INSS S/ '

#manipulação iss
iss_colunas_para_excluir = ['Valor Bruto', 'Valor IRRF', 'Valor CSRF', 'Valor INSS', 'Caução']
iss = unificada_aba_recebidas_v2_df.drop(columns=iss_colunas_para_excluir)
iss = iss.dropna(subset='Valor ISS')
iss = iss[iss['Valor ISS'] != 0]
iss = iss.rename(columns={'Valor ISS': 'Valor'})
iss['H1'] = 'ISS S/ '

#juntar tudo
# Lista de DataFrames
lista_impostos = [irrf, pcc, inss, iss]

# Concatenar os DataFrames em um único DataFrame
impostos = pd.concat(lista_impostos)

# Adicionar uma coluna 'Débito' com o valor '2.01.02.01.0001'
impostos['Débito'] = '2.01.02.01.0001'

# Função para mapear valores da coluna 'H1' para a coluna 'Crédito'
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

# Aplicar a função mapear_credito à coluna 'H1' e criar uma nova coluna 'Crédito'
impostos['Crédito'] = impostos['H1'].apply(mapear_credito)

# Adicionar uma coluna 'Histórico' com valores vazios
impostos['Histórico'] = ""

# Selecionar colunas relevantes
impostos = impostos[['CÓD', 'Débito', 'Crédito', 'Emissão', 'Valor', 'Histórico', 'H1', 'Tipo', 'Nº Nota Fiscal', 'Prestador']]
impostos['Valor'] = impostos['Valor'].round(2)
#impostos['Histórico'] = '=CONCATENAR(H2;" ";I2;" ";J2;" ";K2)'

#manipulação caucao

caucao_colunas_para_excluir = ['Valor Bruto', 'Valor IRRF', 'Valor CSRF', 'Valor INSS', 'Valor ISS']
caucao = unificada_aba_recebidas_v2_df.drop(columns=caucao_colunas_para_excluir)
#print(caucao.to_string())
caucao = caucao.dropna(subset='Caução')
caucao = caucao[caucao['Caução'] != 0]
caucao = caucao.rename(columns={'Caução': 'Valor'})
caucao = caucao[['CÓD', 'Débito', 'Crédito', 'Emissão', 'Valor', 'Histórico', 'H1', 'Tipo', 'Nº Nota Fiscal', 'Prestador']]
caucao['Valor'] = caucao['Valor'].round(2)
caucao['H1'] = 'RETENÇÃO CONTRATUAL S/'
#caucao['Histórico'] = '=CONCATENAR(H2;" ";I2;" ";J2;" ";K2)'

#manipulação devolucao
#print(unificada_aba_devolucoes_df.to_string())
#devolucoes_colunas_para_excluir = ['CNPJ Prestador', 'Nota Referenciada', 'Pagamentos', 'Valor Líquido', 'Centro de Custo', 'Descrição']
#devolucoes = unificada_aba_devolucoes_v2_df.drop(columns=devolucoes_colunas_para_excluir)


devolucoes = unificada_aba_devolucoes_v2_df.rename(columns={'Valor Bruto': 'Valor'})
#print(devolucoes.to_string())

devolucoes = devolucoes[['CÓD', 'Débito', 'Crédito', 'Emissão', 'Valor', 'Histórico', 'Natureza Da OP.', 'H1', 'Tipo', 'Nº Nota Fiscal', 'Prestador']]
devolucoes['Valor'] = devolucoes['Valor'].round(2)
#caucao['Histórico'] = '=CONCATENAR(H2;" ";I2;" ";J2;" ";K2)'

#exportar arquivo unificada
#pasta
writer = pd.ExcelWriter(r"C:\Users\ph6br\Desktop\unificada\v2\exportação_unificada.xlsx", engine='xlsxwriter')

notas.to_excel(writer, sheet_name='Notas')
impostos.to_excel(writer, sheet_name='Impostos Retidos')
caucao.to_excel(writer, sheet_name='Retenções Contratuais')
devolucoes.to_excel(writer, sheet_name='Devoluções')

writer.close()