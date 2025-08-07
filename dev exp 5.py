# Load required libraries
set.seed(123) # for reproducibility
library(ggplot2)
# Create the data frame
ID <- 1:10
Age <- sample(18:60, 10, replace = TRUE)
Income <- sample(30000:90000, 10, replace = TRUE)
Gender <- c('Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male',
'Male')
Education <- c('High School', 'Bachelor', 'Master', 'PhD', 'Bachelor', 'Master', 'Bachelor',
'PhD', 'High School', 'Master')
df <- data.frame(ID, Age, Income, Gender, Education)
# Print the first few rows
print(head(df))
# Check for missing values
print(colSums(is.na(df)))
# Select Age and Income columns
selected_columns <- df[, c("Age", "Income")]
print(selected_columns)
# Filter: Age > 30
age_above_30 <- df[df$Age > 30, ]
print(age_above_30)
# Filter: Gender == "Male"
male_only <- df[df$Gender == "Male", ]
print(male_only)
# Plot: Histogram of Age
hist(df$Age, breaks = 5, col = "skyblue", border = "black",
 main = "Age Distribution", xlab = "Age", ylab = "Frequency")
# Plot: Boxplot of Income
boxplot(df$Income, main = "Income Distribution", ylab = "Income", col = "lightgreen")
