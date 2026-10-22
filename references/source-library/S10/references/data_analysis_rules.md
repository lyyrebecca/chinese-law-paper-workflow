# Data Analysis Rules

Use this reference when reviewing data cleaning, coding, descriptive statistics, inferential statistics, test selection, regression strategy, and statistical overclaiming. These rules come from `第八讲 如何开展数据分析.pdf` and extend the existing research design and data collection rules.

## Data Cleaning And Preparation

- [course norm] Questionnaire data should be received and checked with records, unique questionnaire IDs, preserved original questionnaires, and explicit checking rules. Source: `第八讲 如何开展数据分析.pdf`, p.1.
- [course norm] Generally unacceptable questionnaires include damaged questionnaires, very incomplete responses, abnormal answers such as choosing the same option throughout, and respondents who do not meet the study requirements. Source: `第八讲 如何开展数据分析.pdf`, p.1.
- [course norm] Questionnaire checking should examine whether open-ended answers are legible, all required questions are answered, answers are internally consistent, and response instructions are followed. Source: `第八讲 如何开展数据分析.pdf`, p.2.
- [course norm] Problematic questionnaires may be returned for follow-up, treated as missing values for nonconforming items, or invalidated as a whole. Source: `第八讲 如何开展数据分析.pdf`, p.2.
- [course norm] Data coding includes pre-coding and post-coding; post-coding is usually needed for "other" options in mixed questions and for open-ended questions, using manual or automatic coding. Source: `第八讲 如何开展数据分析.pdf`, p.2.
- [course norm] A coding manual should specify variable number, variable name, variable label, column position, and coding explanation. Source: `第八讲 如何开展数据分析.pdf`, p.2.
- [course norm] Data entry should determine variable type, value range, number of digits, decimal places, and number of variables corresponding to each question; multi-select questions should be split into multiple single-choice variables. Source: `第八讲 如何开展数据分析.pdf`, p.2.
- [course norm] About 25% of data entry should be checked. Source: `第八讲 如何开展数据分析.pdf`, p.2.
- [course norm] Data auditing includes validity checks, consistency checks, distribution checks, and outlier checks; common methods include frequency statistics, variable statistics, and crosstabs. Source: `第八讲 如何开展数据分析.pdf`, p.3.
- [course norm] Missing values may be imputed by deduction, median, or statistical model estimation; deleting cases is not recommended; the most common approach is to keep cases with missing values and exclude them only in the specific analysis where needed. Source: `第八讲 如何开展数据分析.pdf`, p.3.
- [course norm] Raw data or variables may need recoding, redefinition, or transformation; right-skewed economic variables such as income may use log transformation. Source: `第八讲 如何开展数据分析.pdf`, p.3.

## Descriptive Statistics

- [course norm] Central tendency can be described with mode, median, and mean; median is not suitable for nominal variables. Source: `第八讲 如何开展数据分析.pdf`, p.4.
- [course norm] Dispersion can be described with range, variance, and standard deviation. Source: `第八讲 如何开展数据分析.pdf`, p.4.

## Inferential Statistics And Test Selection

- [course norm] Statistical hypothesis testing is not the same as a research hypothesis; it tests assumptions about population parameters using sample statistics. Source: `第八讲 如何开展数据分析.pdf`, p.5.
- [course norm] Hypothesis testing should establish null hypothesis H0 and alternative hypothesis H1, choose significance level such as 0.05, 0.01, or 0.001, calculate the statistic, compare with the critical value, and decide whether to accept or reject H0. Source: `第八讲 如何开展数据分析.pdf`, p.5.
- [course norm] T-test is used for mean comparison where the independent variable has two categories. Single-sample, independent-sample, and paired-sample T-tests serve different comparison scenarios. Source: `第八讲 如何开展数据分析.pdf`, p.5.
- [course norm] ANOVA is used when the independent variable has three or more categories and the dependent variable is ordinal or above, preferably interval or ratio; homogeneity of variance should not be violated. Source: `第八讲 如何开展数据分析.pdf`, p.5.
- [course norm] Interaction/crosstab analysis classifies cases by two variables and is the simplest bivariate analysis, suitable for two nominal variables. Source: `第八讲 如何开展数据分析.pdf`, p.6.
- [course norm] Chi-square tests independence/association between two nominal variables. Limits: categories should not be too many, sample size should not be too large or too small, and expected frequencies should not be below 5 beyond allowed tolerance. Source: `第八讲 如何开展数据分析.pdf`, p.6.
- [course norm] Pearson correlation applies when both variables are interval or ratio; if one variable is ordinal, use Spearman correlation. Source: `第八讲 如何开展数据分析.pdf`, p.6.
- [course norm] Regression model choice should match the dependent variable: multiple linear regression for continuous dependent variables, logistic regression for 0/1 dependent variables, multinomial logistic regression for multicategory dependent variables, and ordinal logistic regression for ordered multicategory dependent variables such as Likert scales. Source: `第八讲 如何开展数据分析.pdf`, p.7.
- [course norm] Regression requires diagnostic checks, such as IIA assumption checks before multinomial logit and VIF checks for multicollinearity in multiple linear regression. Source: `第八讲 如何开展数据分析.pdf`, p.7.
- [course norm] Regression strategy should be chosen deliberately, such as simultaneous, stepwise, or hierarchical regression. Source: `第八讲 如何开展数据分析.pdf`, p.7.
- [course norm] Independent variables in regression must have theoretical justification. Source: `第八讲 如何开展数据分析.pdf`, p.7.
- [course norm] Variable level and method should match: chi-square for nominal-nominal, T-test for two-category nominal to interval, ANOVA for three-or-more-category nominal to interval, Pearson for interval-interval, Spearman for ordinal-interval. Source: `第八讲 如何开展数据分析.pdf`, p.8.

## Pass / Partial / Fail Criteria

| Criterion | Pass | Partial | Fail |
|---|---|---|---|
| Data cleaning | Receipt, ID, original preservation, screening rules, and audit steps are specified | Some cleaning steps are named but incomplete | No cleaning/checking process |
| Coding manual | Variable IDs, names, labels, positions, and coding explanations are documented | Coding exists but documentation is incomplete | Coding rules absent |
| Missing values | Missing-value treatment is explicit and justified | Treatment mentioned but not tied to analysis | Missing values ignored |
| Descriptive statistics | Central tendency/dispersion match variable type | Statistics reported but not fully suited to variable type | Statistics inappropriate or absent |
| Test selection | Test matches variable levels and comparison structure | Test plausible but assumptions not checked | Test incompatible with variables |
| Regression choice | Model matches dependent variable and strategy is justified | Model type named but rationale thin | Model incompatible with dependent variable |
| Diagnostic checks | Needed assumptions/diagnostics are checked or acknowledged | Diagnostics mentioned but incomplete | No diagnostics despite model need |
| Theory-based predictors | Independent variables have theoretical support | Some predictors justified | Predictors chosen only because data exist |

## Conflict / Applicability Notes

- This file does not override prior causal caution. Statistical significance or regression association does not by itself prove causality.
- T-tests, ANOVA, chi-square, correlation, and regression rules apply to quantitative analysis; they should not be forced onto qualitative interviews, ethnography, or interpretive textual analysis.
- The course's missing-value guidance says case deletion is not recommended and keeping cases while excluding them only for specific analyses is most common; this should be marked as course guidance, while any alternative missing-data strategy should be justified by the user's field/method requirements.

