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
<1>1. The total ramification of the map is zero.
::: {.proof}
Let $f:C\to D$ have finite degree $d$, with $g(C)=g(D)=1$. The Riemann--Hurwitz formula gives
$$
2g(C)-2=d\bigl(2g(D)-2\bigr)+\sum_{p\in C}(e_p-1),
$$
where $e_p\ge1$ is the ramification index at $p$. Since both genera are $1$,
$$
0=\sum_{p\in C}(e_p-1).
$$
Each summand is nonnegative, so every summand is zero.
:::

<1>2. The maximum number of ramification points is $\boxed{0}$.
::: {.proof}
By step <1>1, $e_p=1$ for every $p\in C$. Thus $f$ is unramified and has no ramification points.
:::

<1>3. Q.E.D.
::: {.proof}
Step <1>2 gives the requested maximum and its justification.
:::
:::
