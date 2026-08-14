---
schema: qual/card@1
id: P-EVBF7
kind: problem
title: "Let $F \\subset K \\subset L$ be finite degree field extensions."
classification:
  areas:
  - algebra
  topics:
  - galois-theory
  - field-extensions
  - counterexamples
relations: []
review: draft
---
Let $F \subset K \subset L$ be finite degree field extensions.
For each of the following assertions, give a proof or a counterexample.

a.
If $L/F$ is Galois, then so is $K/F$.

b.
If $L/F$ is Galois, then so is $L/K$.

c.
If $K/F$ and $L/K$ are both Galois, then so is $L/F$.

:::{.concept}
\envlist

- Every quadratic extension over $\QQ$ is Galois.
:::

:::{.solution}
Let $L/K/F$.

:::{.proof title="of a"}
**False**: 
Take $L/K/F = \QQ(\zeta_2, \sqrt[3] 2) \to \QQ(\sqrt[3] 2) \to \QQ$.

Then $L/F$ is Galois, since it is the splitting field of $x^3 - 2$ and $\QQ$ has characteristic zero.

But $K/F$ is not Galois, since it is not the splitting field of any irreducible polynomial.
:::

:::{.proof title="of b"}
**True**: 
If $L/F$ is Galois, then $L/K$ is normal and separable:

- $L/K$ is normal, since if $\sigma: L \injects \overline K$ lifts the identity on $K$ and fixes $L$, i-t also lifts the identity on $F$ and fixes $L$ (and $\overline K = \overline F$).

- $L/K$ is separable, since $F[x] \subseteq K[x]$, and so if $\alpha \in L$ where $f(x) \definedas \min(\alpha, F)$ has no repeated factors, then $f'(x) \definedas \min(\alpha, K)$ divides $f$ and thus can not have repeated factors.


:::

:::{.proof title="of c"}
**False**: 
Use the fact that every quadratic extension is Galois, and take $L/K/F = \QQ(\sqrt[4] 2) \to \QQ(\sqrt 2) \to \QQ$.

Then each successive extension is quadratic (thus Galois) but $\QQ(\sqrt[4] 2)$ is not the splitting field of any polynomial (noting that it does not split $x^4 - 2$ completely.)


:::

:::


