---
schema: qual/card@1
id: P-GTJDX
kind: problem
title: The maps $z\mapsto(w-z)/(1-\bar{w}z)$ send the disc to itself
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Schwarz Lemma
  - Biholomorphisms
relations: []
review: draft
---

::: {.problem}
(a) Let $z, w \in \CC$ with $\bar z w \neq 1$.
Prove that
$$
\abs{w-z \over 1 - \bar w z} < 1 \quad\text{ if } \abs{z}<1,~ \abs{w} < 1
$$
with equality when $\abs{z} = 1$ or $\abs{w} = 1$.

(b) Prove that for a fixed $w\in \DD$, the mapping $F: z\mapsto {w-z \over 1 - \bar w z}$ satisfies

- $F$ maps $\DD$ to itself and is holomorphic.
- $F(0) = w$ and $F(w) = 0$.
- $\abs{z} = 1$ implies $\abs{F(z)} = 1$.
:::

::: {.solution}
::: pf

::: {.pf-step #identity}
$\abs{1-\bar w z}^2-\abs{w-z}^2 = (1-\abs w^2)(1-\abs z^2)$.

::: pf-proof
Expand: $\abs{w-z}^2 = \abs w^2+\abs z^2-2\Re(\bar w z)$ and $\abs{1-\bar w z}^2 = 1+\abs w^2\abs z^2-2\Re(\bar w z)$, and subtract.
:::

:::

::: {.pf-step #part-a}
(a) If $\abs z,\abs w<1$ the quotient has modulus $<1$; if $\abs z=1$ or $\abs w=1$ it has modulus $1$.

::: pf-proof
The denominator is nonzero since $\overline{1-\bar w z}=1-w\bar z\neq 0$. If $\abs z,\abs w<1$, the right side of step [](#identity){.pf-ref} is positive, so $\abs{w-z}<\abs{1-\bar w z}$. If $\abs z=1$ or $\abs w=1$, it is zero, so $\abs{w-z}=\abs{1-\bar w z}$.
:::

:::

::: pf-step
(b) For $w\in\DD$: $F$ is holomorphic on $\DD$ with $F(\DD)\subseteq\DD$; $F(0)=w$ and $F(w)=0$; and $\abs{F(z)}=1$ when $\abs z=1$.

::: pf-proof
For $\abs z\le 1$ we have $\abs{\bar w z}\le\abs w<1$, so $1-\bar w z\neq 0$ and $F$, a rational function, is holomorphic on a neighborhood of the closed disk. Step [](#part-a){.pf-ref} gives $\abs{F(z)}<1$ for $\abs z<1$ and $\abs{F(z)}=1$ for $\abs z=1$. Finally $F(0)=w/1=w$ and $F(w)=0/(1-\abs w^2)=0$.
:::

:::

:::

:::

::: {.remark}
$F$ is a bijection of $\DD$, since it is its own inverse:
$$
F(F(z)) = \frac{w(1-\bar w z)-(w-z)}{(1-\bar w z)-\bar w(w-z)} = \frac{z(1-\abs w^2)}{1-\abs w^2} = z.
$$
:::
