library(car)
library(emmeans)
library(multcomp)

dados <- read.table("/home/matheus_mai/Trabalho_TCC/Usuais/testando_1_2_3.csv", header = TRUE, sep = ";")
print(dados)

# Verificar se a coluna "coluna_nome" contém valores inteiros
# Verificar se a coluna "coluna_nome" contém valores strings
# Substituir vírgula por ponto na coluna "coluna_nome"
#dados$Youden <- as.numeric(gsub(",", ".", dados$Youden))

#is_int <- sapply(dados$Youden, is.numeric)
#print(is_int)



anova2 <- lm(
  Youden ~ PANTHER_CLASS*programs,
  data = dados
)

post1 <- emmeans(
  anova2, 
  specs = ~programs|PANTHER_CLASS
)
post1

pairs_bonferroni <- pairs(
  post1, 
  adjust = "bonferroni",
  infer = c(TRUE, TRUE)
)

pairs_bh <- pairs(
  post1, 
  adjust = "BH",
  infer = c(TRUE, TRUE)
)

cld_result <- cld(
  post1, 
  Letters = letters,
  decreasing = TRUE,
  adjust = "BH"
) 

#print da ANOVA
summary(anova2)

#print dos contrastes emmeans
print(post1[1:200, ])

#print a comparações entre grupos usando bonferroni
print(pairs_bonferroni[1:200, ])
print(pairs_bonferroni[1000:2000, ])

#print a comparações entre grupos usando BH
print(pairs_bh[1:200, ])

#print a comparação entre grupo ordenados 
print(cld_result[1:200, ])
print(cld_result[201:304, ])
print(cld_result[401:800, ])
print(cld_result[801:1300, ])
print(cld_result[1301:1500, ])
print(cld_result[1501:1800, ])
print(cld_result[1801:2015, ])


#Gráfico de barras
install.packages("ggplot2")
library(ggplot2)
ggplot(cld_result, aes(x = reorder(programs, emmean), y = emmean, fill = PANTHER_CLASS)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Comparação entre Grupos Ordenados",
       x = "Programas",
       y = "Média dos Valores",
       fill = "PANTHER_CLASS") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

#Gráfico de pontos
install.packages("ggplot2")
library(ggplot2)

ggplot(cld_result, aes(x = reorder(programs, emmean), y = emmean, color = PANTHER_CLASS)) +
  geom_point() +
  labs(title = "Comparação entre Grupos Ordenados",
       x = "Programas",
       y = "Média dos Valores",
       color = "PANTHER_CLASS") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
