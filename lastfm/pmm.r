library(HTSCluster)
setwd('~/Documents/PrincetonJuniorSpring//COS424/HW/Final Project/')

data <- as.matrix(read.table('train.txt'))

model <- PoisMixClus(data, 5, 10)