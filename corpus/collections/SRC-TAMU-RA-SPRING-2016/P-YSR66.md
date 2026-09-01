---
schema: qual/card@1
id: P-YSR66
kind: problem
title: Riesz's lemma and noncompactness of the infinite-dimensional unit ball
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
  - Norms
  - Compactness
relations: []
review: draft
---

::: {.problem}
(a) Let $X$ be a normed vector space and $Y$ be a closed liner subspace of $X$.
Assume $Y$ is a proper subspace, that is, $Y\ne X$.
Show that, for arbitrary $\epsilon\in(0,1)$, there is an element $x\in X$ such that $\|x\|=1$ and $\inf_{y\in Y}\|x-y\|>1-\epsilon$.

(b) Use part (a) to prove that, if $X$ is an infinite dimensional normed vector space, then the unit ball of $X$ is not compact.
:::

:::{.solution}
For all $\epsilon$, and a $x\notin Y$, $\inf_{y\in Y}\|x-y\|=d>0$. Now, choose a $\delta>0$ such that $\frac{d}{d+\delta}>1-\epsilon$. For this $\delta$, choose $y_0\in Y$ such that $\|x-y_0\|<d+\delta$. Define $u=\frac{x-y_0}{\|x-y_0\|}$. Then $\|u\|=1$ and $\|u+Y\|=\inf_{y\in Y}\|\frac{x-y_0}{\|x-y_0\|}-y\|=\frac{\|x+Y\|}{\|x-y_0\|}>\frac{d}{d+\delta}>1-\epsilon$.

If $X$ is infinite dimensional, we can choose a sequence $\{x_n\}$ by induction in the unit ball. We begin with any element $x_1$ in the unit ball. Then If $\{x_1,x_2,\dots,x_{n-1}\}$ has been defined, then by (a), there is an element $x_n$ of norm 1 such that $\|x_n+Y\|>\frac{1}{2}$ where $Y=\text{span}\{x_1,\dots,x_{n-1}\}$. Then $\{x_n\}$ witnesses that the unit ball is not compact since $\|x_n-x_m\|>\frac{1}{2}$ for all $n,m$.
:::
