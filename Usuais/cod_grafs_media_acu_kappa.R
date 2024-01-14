install.packages("ggplot2")
install.packages("ggrepel")
library(ggrepel)
library(ggplot2)
library(RColorBrewer)
#library(ggalt)

dados <- read.table("/home/matheus_mai/Trabalho_TCC/Usuais/medias_acu_kappa.csv", header = TRUE, sep = ";")

print(dados)

# Dividir o dataframe por PANTHER_CLASS e criar gráficos
for (panther_class in unique(dados$PANTHER_CLASS)) {
  df_subset <- dados[dados$PANTHER_CLASS == panther_class, ]
  
  # Resgatar a primeira palavra da PANTHER_CLASS
  first_word <- strsplit(panther_class, " ")[[1]][1]
  
  # Remover caracteres inválidos para nomes de arquivos
  file_name <- gsub("[^A-Za-z0-9_]", "_", first_word)
  
  p <- ggplot(df_subset, aes(x = MEDIA_ACURACIA, y = MEDIA_KAPPA, label = PREDITOR, color = PREDITOR)) +
    geom_point(size = 4, alpha = 0.7) +
    geom_text_repel(size = 3, nudge_x = 0.02, nudge_y = 0.02, force = 2, segment.color = "grey50") +
    labs(title = first_word, x = "Média Acurácia", y = "Média Kappa") +
    theme_minimal() +
    theme(legend.position = "none", panel.background = element_rect(fill = "white"), plot.background = element_rect(fill = "white")) +
    scale_color_manual(values = c("BayesDel_addAF" = "darkblue", "ClinPred" = "darkgreen", "Meta_RNN" = "darkred", 
                                  "REVEL" = "darkorange", "BayesDel_noAF" = "darkmagenta", "PROVEAN" = "darkcyan",
                                  "VEST4" = "darkviolet", "Meta_RNN" = "darkbrown"))
  
  ggsave(paste0(file_name, "_plot.png"), plot = p, width = 7, height = 7)
}


# Definir cores para os preditores
preditors <- unique(dados$PREDITOR)
color_palette <- brewer.pal(length(preditors), "Set1")
color_map <- setNames(color_palette, preditors)

# Definir formas para as classes PANTHER_CLASS
class_shapes <- c(16, 17, 15, 18, 0, 1, 2, 3, 4)  # Você pode adicionar mais formas se necessário
shape_map <- setNames(class_shapes, unique(dados$PANTHER_CLASS))

p <- ggplot(dados, aes(x = MEDIA_ACURACIA, y = MEDIA_KAPPA, label = PREDITOR, color = PREDITOR)) +
  geom_point(size = 4, alpha = 0.7, shape = 19) +
  geom_text_repel(size = 3, nudge_x = 0.02, nudge_y = 0.02, force = 2, segment.color = "grey50", 
                  box.padding = 0.5) +
  labs(x = "Média Acurácia", y = "Média Kappa") +
  theme_minimal() +
  theme(legend.position = "bottom", strip.text = element_text(size = 12, face = "bold"),
        strip.text.x = element_text(size = 7)) +
  scale_color_manual(values = color_map) +
  facet_wrap(~ PANTHER_CLASS, scales = "free", ncol = 3)

# Salvar o gráfico
ggsave("combined_plot_faceted.png", plot = p, width = 12, height = 8, dpi = 300)

# Mensagem indicando que o gráfico foi salvo
cat("Gráfico combinado com facetas salvo com sucesso!\n")