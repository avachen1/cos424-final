library(HTSCluster)
setwd('~/Documents/PrincetonJuniorSpring//COS424/HW/Final Project/')

data <- as.matrix(read.table('training_data.txt'))

model <- PoisMixClus(data, 5, 10)