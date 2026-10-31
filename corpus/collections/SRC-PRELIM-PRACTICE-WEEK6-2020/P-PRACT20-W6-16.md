---
schema: qual/card@1
id: P-PRACT20-W6-16
kind: problem
title: Maximum of two independent geometric random variables
classification:
  areas:
  - prelim
  topics:
  - Probability
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed a stray brace and restored the question mark, checked against Week6_solns.pdf (Problem 16).
---

::: {.problem}
Suppose $X, Y$ are i.i.d. random variables taking value $n \in \NN$ with probability $\frac{1}{2^n}$. What is the probability that $\max\{X, Y\} > 3$?
:::

::: {.solution}
$\max\{X,Y\}>3$ iff $X>3$ or $Y>3$, so by independence

$$
P(X>3\text{ or }Y>3)=1-P(X\leq3\text{ and }Y\leq3)=1-P(X\leq3)\,P(Y\leq3).
$$

Now

$$
P(X\leq3)=\sum_{i=1}^3P(X=i)=\frac12+\frac14+\frac18=\frac78,
$$

and likewise for $Y$, since the two are identically distributed. Thus

$$
P(\max\{X,Y\}>3)=1-\left(\frac78\right)^2=\frac{15}{64}.
$$
:::
