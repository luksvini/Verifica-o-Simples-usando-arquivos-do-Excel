import pandas as pd

# Passo a passo de solução

# Abrir os 6 arquivos em Excel

lista_meses = ["janeiro", 
               "fevereiro",
                "março", 
                "abril", 
                "maio", 
                "junho"]

# Para cada arquivo: 
    # Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
    
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    
    #2. Para cada arquivo: 
    # 2.1 Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000,"Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000,"Vendas"].values[0]
        print(f"No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")
