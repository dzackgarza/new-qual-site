---
schema: qual/card@1
id: PR-DIVZEROPOLE
kind: proposition
title: Zeros and poles of a rational function
slogan: 'Codimension-one valuations detect only finitely many zeros and poles; on a normal scheme, no poles means regular.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Divisors
  - Discrete Valuation Rings
  - Normal Schemes
relations:
- kind: uses
  target: D-5PQ5W
- kind: uses
  target: D-QJ5M9
review: draft
prompts:
- Why does a rational function on an integral Noetherian scheme have only finitely many zeros and poles?
- Why is a rational function with no poles on a normal Noetherian scheme regular?
---

::: {.proposition}
Let $X$ be an integral Noetherian scheme with function field $K$ and let $t\in K^\times$.

1. There are only finitely many codimension-one points $y\in X$ for which $t\notin\OO_{X,y}^\times$.

2. If $X$ is regular in codimension one and $Y\subseteq X$ is a prime divisor with generic point $\eta_Y$, then $\OO_{X,\eta_Y}$ is a discrete valuation ring. Writing its normalized valuation as $v_Y$, the sum
$$
\operatorname{div}_X(t)=\sum_Y v_Y(t)Y
$$
has finite support and hence is a Weil divisor [@Har77, Lemma II.6.1]. The terms with $v_Y(t)>0$ are the zeros of $t$ and those with $v_Y(t)<0$ are its poles.

3. If $X$ is normal, then
$$
t\in\Gamma(X,\OO_X)
\quad\Longleftrightarrow\quad
v_Y(t)\geq0\text{ for every prime divisor }Y\subseteq X.
$$
Equivalently, a rational function on a normal Noetherian integral scheme is regular exactly when it has no codimension-one poles [@Har77, Proposition II.6.3A].
:::

::: {.remark}
For the finiteness statement, cover $X$ by finitely many affine opens $U=\Spec A$. On such a $U$, write $t=a/b$ with nonzero $a,b\in A$. If a height-one prime $\mathfrak p$ satisfies $t\notin A_\mathfrak p^\times$, then $\mathfrak p$ contains $a$ or $b$. A height-one prime containing a nonzero principal ideal is minimal over that ideal, and a Noetherian ring has only finitely many minimal primes over a fixed ideal. Thus only finitely many height-one primes occur on each $U$.

For the normality statement, on every affine open $U=\Spec A$, the Noetherian normal domain $A$ satisfies
$$
A=\bigcap_{\operatorname{ht}\mathfrak p=1}A_\mathfrak p
$$
inside $K$ [@Har77, Proposition II.6.3A]. Hence nonnegative valuation at every prime divisor makes $t$ regular on every affine open and therefore on $X$.
:::
