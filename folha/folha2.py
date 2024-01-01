import tabula

df = tabula.read_pdf("C:\Users\ph6br\Documents\GitHub\VersatoCopyCargas\folha\Folha Mensal v1.pdf", stream=True)
print(df)