# MissPred - v1.2


<img src="https://www.thoughtco.com/thmb/ekbqfxW7pRkCaMj_-VxSR3w6lBQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/3-D_DNA-56a09ae45f9b58eba4b20266.jpg" width="700" height="400">

---
***
___

## Como executar a funcionalidade:

#### A funcionalidade busca através de uma ***COMMAND LINE INTERFACE*** (CLI) proporcionar para o seu usuário algumas maneiras de aplicar o algoritmo. Dúvidas podem surgir referentes a isso, portanto leia com calma as instruções e siga exatamente o passo a passo e a lógica dos diretórios.

##### - Faça o clone do projeto, crie um ambiente virtual com o seguinte comando: python3 -m venv ~/.venv/MissPred;
##### - Ative o ambiente virtual: source ~/.venv/MissPred/bin/activate
##### - Instale as dependências: pip install -r requirements.txt

##### - Com o ambiente configurado, deve ser feito o download do banco de dados dbNSFP4.2a (link: https://drive.google.com/file/d/1OfAx1SrJVPPNYWfDpQd43S9Aqro3C6aA/view) - PS: o banco de dados zipado apresenta um tamanho de 32GB, então reserve um espaço adequado em seu disco para isso.

##### - Após o download, deve-se rodar o arquivo ***setup.sh***. Porém devemos nos atentar a algumas coisas:
- Deve-se fazer o unzip do banco baixado e colocar os arquivos em uma pasta específica;
- Após isso, edite no arquivo ***setup.sh*** a variavel ***pasta*** e coloque o caminho absoluto para o local onde está o banco de dados;
- OBS: rodar o ***setup.sh*** demora bastante e ocupa uma certa memória da máquina, então atente-se a isso;

##### - Depois de organizar as coisas e ***rodar o setup.sh***. Você terá vários arquivos nessa pasta, referente a cada um dos cromossomos. Cada arquivo ocupa cerca de **3GB de memória**. Arquivos gerados (chr 1 ao Y - mostramos apenas alguns), exemplo: 
- ###### dbNSFP4.2a_variant.chr1_cortado.csv
- ###### dbNSFP4.2a_variant.chr2_cortado.csv
- ###### dbNSFP4.2a_variant.chr3_cortado.csv
- ###### dbNSFP4.2a_variant.chr4_cortado.csv
- ###### ...
- ###### ...
- ###### dbNSFP4.2a_variant.chrX_cortado.csv
- ###### dbNSFP4.2a_variant.chrY_cortado.csv

##### - Após ter todos os arquivos corretos, o ideal é que saiba quais genes deseja avaliar, pois como os arquivos apresentam muitos dados, fica difícil de trabalhar com eles via python. Portanto, é necessário criar um arquivo de formato csv com duas colunas. Ex: arquivo ***genes_utilizados.csv***:
- chr - representando o cromossomo
- gene - representando o gene desejado;
    ###### Esse arquivo criado deverá ser passado para o ***grep_genes.sh***. Nesse arquivo, primeiramente modifique o trecho **pasta="/home/matheus_mai/Trabalho_TCC/dbNSFP4.2a"** para o diretório onde você colocou os coortes realizado com o ***setup.sh***. Segundamente, modifique o trecho **arquivo_nomes="/home/matheus_mai/Trabalho_TCC/genes_utilizados.csv"** para o caminho absoluto do arquivo criado com os cromossomos e genes;

    ###### Após isso, será gerado um diretório para cada gene, e dentro desses diretórios terão as tabelas para cada um dos genes desejado com o seguinte nome: **{GENE}_ocorrencia** . Ex:
    - ###### chr_1
        - ###### ABCA4_ocorrencia.csv
        - ###### FLG_ocorrencia.csv
    - ###### chr_2
        - ###### COL3A1_ocorrencia.csv
        - ###### SCN1A_ocorrencia.csv
    - ###### ...
        - ###### ...

##### - Após isso então será gerado arquivos que desejamos trabalhar, e então podemos executar o programa de fato.
- Primeiramente deve-se entrar na pasta ***src/*** do projeto e então executar o seguinte comando: ***cli.py cleanup -d {CAMINHO DO DIRETÓRIO COM OS GENES QUE RECÉM FOI CRIADO}***. Esse comando vai gerar um arquivo ***_cleanup.csv*** para cada um dos genes, e esses arquivos cleanup serão utilizados no comando abaixo;

- Após termos as tabelas dos genes limpos, podemos rodar então os cálculos estatísticos. Nesse caso, temos três opções:
    - Podemos realizar as estatísticas para todos genes de uma vez só utilizando o arquivo ***run.py***. Apenas deve-se modificar a variável ***absolute_path*** que deve ser passado o diretório geral com os subdiretórios representando os cromossomos com arquivos limpos representando os genes. E então rodar ***python3 run.py***;
    - Podemos realizar as estatísticas para apenas um gene de interesse. Então deve se rodar o seguinte comando: ***python3 cli.py calcgene -f {NOME DO ARQUIVO DO GENE (lembrando que devem ser os arquivos __cleanup.csv gerados)} -sf {NOME DO ARQUIVO QUE DESEJA SALVAR AS ESTATÍSTICAS}***;
    - E também podemos checar as estatísticas a partir de dados separados (algumas mutações específicas e classificação padrão própria). Para isso, devemos rodar dois comandos. Primeiro rodar o ***python3 cli.py populate -f {CAMINHO DO ARQUIVO DO GENE DESEJA AVALIAR (lembrando que devem ser os arquivos __cleanup.csv gerados)}***. Após rodar esse comando deve-se rodar o seguinte comando ***python3 cli.py staatsdb -f {CAMINHO DO ARQUIVO COM AS MUTAÇÕES DESEJADAS. Ex: table_example_entry_search.csv} -sd {NUMERO 1 OU 2. 1- SE QUISER USAR O CLINVAR COMO PADRÃO. 2- SE QUISER USAR CLASSIFICAÇÕES PRÓPRIAS COMO PADRÃO} -fr {CAMINHO DO ARQUIVO GERADO}***;


##### Podes verificar as informações de cli.py através do comando: ***python3 cli.py -h***