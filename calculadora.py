from math import floor

class NumeroViews():

    def calculadora (valor):

        COMPARTILHAMENTO = 4

        numero_cliques = (valor / 100) * 12
        numero_compartilhamento = (numero_cliques / 20) * 3
        views_de_compartilhamento = numero_compartilhamento * 40 * COMPARTILHAMENTO

        total = views_de_compartilhamento + valor

        return floor(total)



    if __name__ == "__main__":


            
        investimento = int(input('Informe por gentileza um valor inteiro a ser investido: R$'))



        while (investimento <= 0):
            print ('O Sr(a) informou um valor menor ou igual a zero, por gentileza insira um valor inteiro maior que zero.')
            investimento = int(input('Informe por gentileza um valor inteiro a ser investido: R$'))

            
        vizualizacao_inicial = investimento * 30

        total_views = calculadora(vizualizacao_inicial)
        
        print (f'O Sr(a) investiu R${investimento},00 reais e a projeção aproximada da quantidade máxima de visualizações é {total_views} visualizações.') 

        

        






