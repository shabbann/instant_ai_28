# **Data distribution**
It’s important to determine the population’s distribution so we can apply the correct statistical methods when analyzing it.
and they are separated into two types 
## **discrete distribution
### **binomial distribution
- The binomial distribution measures the probability of the number of successes or failure outcomes in an experiment on each try.
- Characteristics are classified into two mutually exclusive and exhaustive classes, such as the number of successes/failures and the number accepted/rejected that follow a binomial distribution.
and it's probability function is
$$
p(x)=\binom{n}{x}.p^x.(1-p)^{1-x}

$$
*where is **n** is the number of trails ,**x** is the number of occurrence*
![[Pasted image 20230913170508.png]]
### **Poisson distribution
- The Poisson distribution is the discrete probability distribution that measures the likelihood of a number of events occurring in a given period when the events occur one after another in a well-defined manner.
- Characteristics that can theoretically take large values but actually take small values have Poisson distribution.
- Ex: Number of defects, errors, accidents, absentees, etc.
it's probability function is
$$
p(x)=\frac{\lambda^x .e^{-\lambda} }{x!}
$$
where is lambda is the mean and x is the number of occurrence

![[Pasted image 20230913172824.png]]
## **Continuous Distributions**
### **Normal Distribution
- Some people also refer to normal distributions as Gaussian distributions. It is a symmetrical bell shape curve with higher frequency (probability density) around the central value. The frequency sharply decreases as values are away from the central value on either side.
- In other words, we expect a normal distribution to have characteristics like dimensions that fall on either side of the aimed-at value with equal probability.
- The Mean, Median, and Mode are equal for normal distribution.
![[Pasted image 20230913173648.png]]
In a normal distribution, 68% of the data will occur within +/- 1 standard deviation.
![[Pasted image 20230913174334.png]]
- e = constant (2.71828) – Poisson constant
- x = control variable – (data being studied)
- µ = population mean
- σ = population standard deviation
![[Pasted image 20230913174424.png]]

### **Lognormal distribution**
