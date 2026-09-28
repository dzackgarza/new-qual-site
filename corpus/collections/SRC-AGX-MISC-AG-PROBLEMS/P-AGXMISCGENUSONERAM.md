---
schema: qual/card@1
id: P-AGXMISCGENUSONERAM
kind: problem
title: Maps of finite degree between genus one curves are unramified
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann--Hurwitz
  - Ramification
  - Elliptic Curves
relations: []
review: draft
---

::: {.problem}
What is the maximum number of ramification points that a mapping of finite degree from one smooth projective curve over $\CC$ of genus 1 to another smooth projective curve of genus 1 can have?
Give an explanation for your answer.
:::

::: {.solution}
Let $f\colon X\to Y$ be a finite morphism of degree $d$ between smooth irreducible projective curves over $\CC$ of genus $1$, and let $e_p\geq 1$ be the ramification index of $f$ at $p\in X$.

<1>1. $\sum_{p\in X}(e_p-1)=0$.

::: {.proof}
The Riemann--Hurwitz formula gives
$$
2g(X)-2 = d\,\bigl(2g(Y)-2\bigr) + \sum_{p\in X}(e_p-1).
$$
With $g(X)=g(Y)=1$ both sides of $2g-2$ vanish, so the sum is $0$.
:::

<1>2. Q.E.D.

::: {.proof}
Each term $e_p-1$ is nonnegative, so step <1>1 forces $e_p=1$ for every $p$. The maximum number of ramification points is $\boxed{0}$: every such map is unramified.
:::
:::
