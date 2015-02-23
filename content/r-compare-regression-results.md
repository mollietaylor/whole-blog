Title: Compare Regression Results to a Specific Factor Level in R
Date: 2014-02-06
Tags: lm, R, relevel
Category: R
Slug: 2014/02/compare-regression-results-to-specific
Author: Mollie Taylor
Summary: Including a series of dummy variables in a regression in R is very simple.

Including a series of dummy variables in a regression in R is very simple. For example,

	:::r
	ols <- lm(weight ~ Time + Diet,
		data = ChickWeight)
	summary(ols)

The above regression automatically includes a dummy variable for all but the first level of the factor of the ```Diet``` variable.

	:::r
	Call:
	lm(formula = weight ~ Time + Diet, data = ChickWeight)

	Residuals:
	     Min       1Q   Median       3Q      Max 
	-136.851  -17.151   -2.595   15.033  141.816 

	Coefficients:
	            Estimate Std. Error t value Pr(>|t|)    
	(Intercept)  10.9244     3.3607   3.251  0.00122 ** 
	Time          8.7505     0.2218  39.451  < 2e-16 ***
	Diet2        16.1661     4.0858   3.957 8.56e-05 ***
	Diet3        36.4994     4.0858   8.933  < 2e-16 ***
	Diet4        30.2335     4.1075   7.361 6.39e-13 ***
	---
	Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

	Residual standard error: 35.99 on 573 degrees of freedom
	Multiple R-squared:  0.7453,  Adjusted R-squared:  0.7435 
	F-statistic: 419.2 on 4 and 573 DF,  p-value: < 2.2e-16

This is great, and it's often what you want. But in this case, it's comparing each of the diets to Diet1. In some cases, you might want to compare to a specific diet that isn't the first in the factor list.

How can we choose which dummy to compare to? Fortunately, it's simple to compare to a specific dummy in R. We can just ```relevel``` the factor so the dummy we want to compare to is first.

	:::r
	ChickWeight$Diet <- relevel(ChickWeight$Diet,
		ref = 4)

	olsRelevel <- lm(weight ~ Time + Diet,
		data = ChickWeight)
	summary(olsRelevel)

The ```ref``` argument allows us to change the reference level of the factor variable. This means that when we perform regression analysis

You can use ```table``` or ```str``` to find the factor levels, if you don't already know them.

After releveling the factor variable, we can simply perform the same regression again, and this time it will compare the results to the new reference level:

	:::r
	olsRelevel <- lm(weight ~ Time + Diet,
		data = ChickWeight)
	summary(olsRelevel)

	:::r
	Call:
	lm(formula = weight ~ Time + Diet, data = ChickWeight)

	Residuals:
	     Min       1Q   Median       3Q      Max 
	-136.851  -17.151   -2.595   15.033  141.816 

	Coefficients:
	            Estimate Std. Error t value Pr(>|t|)    
	(Intercept)  41.1578     4.0828  10.081  < 2e-16 ***
	Time          8.7505     0.2218  39.451  < 2e-16 ***
	Diet1       -30.2335     4.1075  -7.361 6.39e-13 ***
	Diet2       -14.0674     4.6665  -3.015  0.00269 ** 
	Diet3         6.2660     4.6665   1.343  0.17989    
	---
	Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

	Residual standard error: 35.99 on 573 degrees of freedom
	Multiple R-squared:  0.7453,  Adjusted R-squared:  0.7435 
	F-statistic: 419.2 on 4 and 573 DF,  p-value: < 2.2e-16

Now we can choose any factor level as the reference for the series of dummies in the regression analysis. The code is available in [a gist](https://gist.github.com/mollietaylor/8214220).

##Reference

* <http://stackoverflow.com/a/3872213/2926101>

