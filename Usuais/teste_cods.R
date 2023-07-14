library(car)
library(emmeans)
library(multcomp)

dados <- read.table("/home/matheus_mai/Trabalho_TCC/Tabela_geral_exemplo.csv", header = TRUE, sep = ",")
print(dados)

# Verificar se a coluna "coluna_nome" contém valores inteiros
# Verificar se a coluna "coluna_nome" contém valores strings
# Substituir vírgula por ponto na coluna "coluna_nome"
dados$Youden <- as.numeric(gsub(",", ".", dados$Youden))

is_int <- sapply(dados$Youden, is.numeric)
print(is_int)



anova2 <- lm(
  Youden ~ PANTHER_CLASS*Programs,
  data = dados
)

post1 <- emmeans(
  anova2, 
  specs = ~Programs|PANTHER_CLASS
)
post1

pairs(
  post1, 
  adjust = "bonferroni",
  infer = c(TRUE, TRUE)
)

pairs(
  post1, 
  adjust = "BH",
  infer = c(TRUE, TRUE)
)

cld(
  post1, 
  Letters = letters,
  decreasing = TRUE,
  adjust = "BH"
) 

summary(anova2)