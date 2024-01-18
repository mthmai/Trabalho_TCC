# TCC BIOTECNOLOGIA ÊNFASE EM BIOINFORMÁTICA


<img src="https://www.thoughtco.com/thmb/ekbqfxW7pRkCaMj_-VxSR3w6lBQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/3-D_DNA-56a09ae45f9b58eba4b20266.jpg" width="700" height="400">

---
***
___

### ALGUMAS INFORMAÇÕES IMPORTANTE PRO MOMENTO
* Esse script no momento está pegando um banco de dados específico e gerando tabelas com estatísticas
* Essas tabelas estão incluidas no .gitignore, **portanto não são commitadas aqui no REPOSITÓRIO**



## Como executar o trabalho:

##### - Primeiramente deve ser feito o download do banco de dados dbNSFP4.2a (link: )

##### - Após o download, deve-se rodar o arquivo ***setup.sh***, porém devemos nos atentar a algumas coisas:
- Deve-se fazer o unzip do banco baixado e colocar os arquivos em uma pasta específica;
- Após isso, edite no arquivo ***setup.sh*** a variavel ***pasta*** e coloque o caminho absoluto para o local onde o banco de dados;
- OBS: rodar o ***setup.sh*** demora bastante e ocupa uma certa memória da maquina, então atente-se a isso;

##### - Depois de organizar as coisas e ***rodar o setup.sh***. Você terá vários arquivos nessa pasta, referente a cada um dos cromossomos. Cada arquivo ocupa cerca de **3GB de memória**. Arquivos gerados (chr 1 ao Y - mostramos apenas alguns), exemplo: 
- ###### dbNSFP4.2a_variant.chr1_cortado.csv
- ###### dbNSFP4.2a_variant.chr2_cortado.csv
- ###### dbNSFP4.2a_variant.chr3_cortado.csv
- ###### dbNSFP4.2a_variant.chr4_cortado.csv
- ###### ...
- ###### ...
- ###### dbNSFP4.2a_variant.chrX_cortado.csv
- ###### dbNSFP4.2a_variant.chrY_cortado.csv

##### - Após ter todos os arquivos corretos, o ideal é que 