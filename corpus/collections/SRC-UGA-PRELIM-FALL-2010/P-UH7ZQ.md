---
schema: qual/card@1
id: P-UH7ZQ
kind: problem
title: Negations of statements about odd integers and a sequential limit
classification:
  areas:
  - prelim
  topics:
  - Logic and Quantifiers
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Negate each of the following statements in the most informative way possible (i.e., without using the words "no" or "not").

a. There is an integer $x$ so that $x + y$ is odd for each integer $y$.
b. If $x$ is an odd integer, then $xy$ is odd for every integer $y$.
c. Given $\varepsilon > 0$, there is $N \in \mathbb{N}$ so that whenever $n > N$, we have $\left| \dfrac{2+n}{1+n} - 1 \right| < \varepsilon$.
:::

::: {.solution}
(a) The negation is:
\[
\text{For every integer }x\text{ there is an integer }y\text{ such that }x+y\text{ is even.}
\]

(b) The negation is:
\[
\text{There is an odd integer }x\text{ and an integer }y\text{ such that }xy\text{ is even.}
\]

(c) The negation is:
\[
\text{There exists }\varepsilon>0\text{ such that for every }N\in\mathbb N
\text{ there is }n>N\text{ with }
\left|\frac{n+2}{n+1}-1\right|\ge\varepsilon.
\]
These follow by replacing each quantifier by its opposite and negating the final predicate.
:::
