# Billboard-Hot-100
Analyzing song features both in terms of lyrics and audio in Billboard Hot 100 from 1950 to 2015. I identified the heterogeneity of Billboard Hot 100 songs over time in different aspects. Moreover, by linking song lyrics and marriage rate in the US, I identified the positive correlation between the weight of the romance/heartbreak theme (topic modeling) and marriage rate.

Author: Jiayan Li

data (folder): contains all the datasets I used in this assignment

Part I_Homogeneity.ipynb

Part II_Testing Theory.ipynb 

utils.py: contains a helper function I write to fit data into a OLS regression model and produce a summary and a scatter plot with a regression line

music.py: helper functions provided by Prof. Jon Clindaniel for the MACS40400 course (Uchicago)

lyric_lemmas.pkl: lemma series of lyrics stored locally to save running time

lda5p20_i400.model: LDA model stored locally to save running time