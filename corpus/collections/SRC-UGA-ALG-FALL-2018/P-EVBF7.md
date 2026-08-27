---
schema: qual/card@1
id: P-EVBF7
kind: problem
title: Galois-ness of $K/F$ and of $L/K$ when $L/F$ is Galois, and of $L/F$ when $K/F$
  and $L/K$ are Galois
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Counterexamples
relations: []
review: draft
---

Let $F \subset K \subset L$ be finite degree field extensions.
For each of the following assertions, give a proof or a counterexample.

a. If $L/F$ is Galois, then so is $K/F$.

b. If $L/F$ is Galois, then so is $L/K$.

c. If $K/F$ and $L/K$ are both Galois, then so is $L/F$.

::: {.concept}
\envlist

- Every quadratic extension over $\QQ$ is Galois.
:::

::: {.solution}
Let $L/K/F$.

::: {.proof}
**False**: Take $L/K/F = \QQ(\zeta_3, \sqrt[3] 2) \to \QQ(\sqrt[3] 2) \to \QQ$.

Then $L/F$ is Galois, since it is the splitting field of $x^3 - 2$ and $\QQ$ has characteristic zero.

But $K/F$ is not Galois, since it is not normal: it contains the real root $\sqrt[3]2$ of $x^3-2$ and neither of the two complex roots.

> The root of unity here must be $\zeta_3$, not $\zeta_2 = -1$, which lies in $\QQ$ and would collapse $L$ onto $K$.
:::

::: {.proof}
**True**: If $L/F$ is Galois, then $L/K$ is normal and separable:

- $L/K$ is normal, since if $\sigma: L \injects \overline K$ lifts the identity on $K$ and fixes $L$, i-t also lifts the identity on $F$ and fixes $L$ (and $\overline K = \overline F$).

- $L/K$ is separable, since $F[x] \subseteq K[x]$, and so if $\alpha \in L$ where $f(x) \definedas \min(\alpha, F)$ has no repeated roots, then $g(x) \definedas \min(\alpha, K)$ divides $f$ and thus can not have repeated roots either.
:::

::: {.proof}
**False**: Use the fact that every quadratic extension is Galois, and take $L/K/F = \QQ(\sqrt[4] 2) \to \QQ(\sqrt 2) \to \QQ$.

Then each successive extension is quadratic (thus Galois) but $\QQ(\sqrt[4] 2)$ is not the splitting field of any polynomial (noting that it does not split $x^4 - 2$ completely.)
:::
:::
