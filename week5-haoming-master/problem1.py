import numpy as np
import scipy as sp
from scipy.stats import norm
from scipy.stats import t
import math

# import data
file_n_knowledge = open('eng0.txt')
file_knowledge = open('eng1.txt')
data_n_knowledge = file_n_knowledge.readlines()
data_knowledge = file_knowledge.readlines()
data_n_knowledge = [float(x) for x in data_n_knowledge]
data_knowledge = [float(x) for x in data_knowledge]

# q2
# mean of data
mean_n_knowledge = np.mean(data_n_knowledge)
mean_knowledge = np.mean(data_knowledge)

# standard normal and student's t distribution
size_knowledge = len(data_knowledge)
std_dev_knowledge = np.std(data_knowledge)
std_error_knowledge = std_dev_knowledge / math.sqrt(size_knowledge)
mu = 0.75
std_score_knowledge = (mean_knowledge - mu) / std_error_knowledge
p_value_knowledge = sp.stats.norm.cdf(-abs(std_score_knowledge)) * 2

print("question2:")
print("The size of the knowledgeable student sample is %d."  %(size_knowledge))
print("The mean of the knowledgeable student sample is %f."  %(mean_knowledge))
print("The standard error of the knowledgeable student sample is %f." %(std_error_knowledge))
print("The standard score of the knowledgeable student sample is %f." %(std_score_knowledge))
print("The p-value of the knowledgeable student sample is %f." %(p_value_knowledge))

# q3
z_c = norm.ppf(0.05 / 2)
max_std_erro = abs(mean_knowledge - mu) / abs(z_c)
min_size = np.ceil((std_dev_knowledge / max_std_erro) ** 2)

print("question3:")
print("The largest standard error of knowledgeable student sample when p value is 0.05 is %f." %(max_std_erro))
print("The minimum size of knowledgeable sample when p value is 0.05 is %d." %(min_size))

# q5
size_n_knowledge = len(data_n_knowledge)
mu = 0
delta_x = mean_n_knowledge - mean_knowledge
sigma = math.sqrt(np.var(data_n_knowledge) / len(data_n_knowledge) + np.var(data_knowledge) / len(data_knowledge))
z = (delta_x - mu) / sigma
p_value = sp.stats.norm.cdf(-abs(z)) * 2

print("question5:")
print("The sample size of knowledgeable student sample is %d." %(size_knowledge))
print("The sample size of unknowledgeable student sample is %d." %(size_n_knowledge))
print("The mean of knowledgeable student sample is %f." %(mean_knowledge))
print("The mean of unknowledgeable student sample is %f." %(mean_n_knowledge))
print("The standard error is %f." %(sigma))
print("The z-score of the sample is %f." %(z))
print("The p-value of the sample is %f." %(p_value))

file_n_knowledge.close()
file_knowledge.close()