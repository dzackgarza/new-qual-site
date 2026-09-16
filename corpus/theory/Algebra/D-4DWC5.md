---
schema: qual/card@1
id: D-4DWC5
kind: definition
title: Resolvent cubic of a quartic
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
relations: []
review: draft
---

::: {.definition}
Let $k$ be a field and let
$$
f(x)=x^{4}+a_{3} x^{3}+a_{2} x^{2}+a_{1} x+a_{0} \in k[x].
$$
The \dfn{resolvent cubic} of $f$ is
$$
R_{4}(t) \coloneqq t^{3}-a_{2} t^{2}+\left(a_{1} a_{3}-4 a_{0}\right) t+4 a_{0} a_{2}-a_{1}^{2}-a_{0} a_{3}^{2} \in k[t].
$$
:::

::: {.proposition}
Let $f\in k[x]$ be as in the definition, and let $r_1, r_2, r_3, r_4$ be the roots of $f$, with multiplicity, in a splitting field of $f$ over $k$.
Then
$$
R_4(t) = \left(t-\left(r_{1} r_{2}+r_{3} r_{4}\right)\right)\left(t-\left(r_{1} r_{3}+r_{2} r_{4}\right)\right)\left(t-\left(r_{1} r_{4}+r_{2} r_{3}\right)\right).
$$
:::

::: {.example}
For $f(x) = x^4 + cx + d$, that is, $a_3 = a_2 = 0$, $a_1 = c$, and $a_0 = d$, the resolvent cubic is $R_4(t) = t^3 - 4dt - c^2$.
:::
