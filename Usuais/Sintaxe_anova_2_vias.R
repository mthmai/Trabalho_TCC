# install.packages("car")
library(car)
library(emmeans)
library(multcomp)


# Inventando um banco de dados
bd <- data.frame(
  PANTHER_CLASS = c("A", "A", "B", "B", "B", "A", "A", "A", "B", "B", "B", "A"),
  Programs = c("a", "b", "a", "b", "a", "b", "c", "c", "c", "c", "a", "b"),
  youden = runif(12)
)
bd


# ANOVA de duas vias

anova2 <- lm(
  youden ~ PANTHER_CLASS*Programs,
  data = bd
)

Anova(anova2, type = 3)
# PANTHER_CLASS:Programs, efeito da interacao



# Post hoc considerando que ha efeito de interacao
post1 <- emmeans(
  anova2, 
  specs = ~Programs|PANTHER_CLASS
)
post1

# Comparacoes duas a duas
# estimate: diferenca entre as medias do indice de Youden
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


# cld(
#   post1, 
#   Letters = letters,
#   decreasing = TRUE,
#   adjust = "sidak"
# ) 

cld(
  post1, 
  Letters = letters,
  decreasing = TRUE,
  adjust = "BH"
) 



