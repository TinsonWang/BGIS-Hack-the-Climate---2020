setwd("C:/Users/tinso/PycharmProjects/BGIS-HackTheClimate2020/dataset/us_energy_census_gdp_10-14/")

library("readxl")
library("editData")

#my_data <- read.csv(file = 'Energy Census and Economic Data US 2010-2014.csv')

consumption <- read_excel("use_ng_capita.xlsx", sheet="Btu")
prodexpnd <- read_excel("pr_ex_pa_ng.xlsx")

#attach(my_data)
attach(consumption)

#coal_data <- subset(my_data, select=-c(Region:Great.Lakes, TotalP2010:BiomassC2014, ElecC2010:RNETMIG2014))

#Trimming and editing here
consumption_trimmed <- consumption[-c(1, 2),]
names(consumption_trimmed)[1] <- "States"
names(consumption_trimmed)[2:50] <- "1960":"2008"
states <- subset(consumption_trimmed, select=c("States"))
states$Position_X <- c("1":"52")
states = edit(states)
write.csv(states,'StatesXPositions.csv' )
states$Position_Y <- c("1":"52")
states <- edit(states)
write.csv(states, 'StatesXYPositions.csv')
combined = combined[,c(1, 60, 61, 2:59)]
write.csv(combined, 'TransformInExcel.csv')

