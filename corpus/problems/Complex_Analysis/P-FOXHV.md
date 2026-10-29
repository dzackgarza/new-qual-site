---
schema: qual/card@1
id: P-FOXHV
kind: problem
title: The disk automorphism $z\mapsto\frac{w-z}{1-\bar{w}z}$
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Schwarz Lemma
  - Biholomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
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

- $F: \DD \to \DD$ is bijective.
:::

::: {.hint}
Calculate $F \circ F$.
:::

::: {.solution}
::: pf

::: {.pf-step #identity}
$\abs{1 - \bar w z}^2 - \abs{w - z}^2 = (1-\abs w^2)(1 - \abs z^2)$ for all $z,w\in\CC$.

::: pf-proof
We have $\abs{w - z}^2 = \abs w^2 + \abs z^2 - w\bar z - \bar w z$ and $\abs{1 - \bar w z}^2 = 1 + \abs w^2 \abs z^2 - \bar w z - w \bar z$. Subtracting gives $1 - \abs w^2 - \abs z^2 + \abs w^2\abs z^2 = (1-\abs w^2)(1 - \abs z^2)$.
:::

:::

::: {.pf-step #part-a}
(a) For $\bar z w\neq 1$: if $\abs z,\abs w<1$ then $\abs{\frac{w - z}{1 - \bar w z}} < 1$, and if $\abs z = 1$ or $\abs w = 1$ then $\abs{\frac{w - z}{1 - \bar w z}} = 1$.

::: pf-proof
The denominator is nonzero because $\overline{1-\bar w z} = 1 - w\bar z \neq 0$.
If $\abs z,\abs w<1$, the right side of step [](#identity){.pf-ref} is positive, so $\abs{w-z}<\abs{1-\bar w z}$.
If $\abs z = 1$ or $\abs w = 1$, the right side is zero, so $\abs{w-z}=\abs{1-\bar w z}$.
Divide by $\abs{1-\bar w z}>0$.
:::

:::

::: pf-step
(b) Fix $w\in\DD$. Then $F$ is holomorphic on $\DD$ and maps $\DD$ into $\DD$; $F(0)=w$ and $F(w)=0$; $\abs{F(z)}=1$ when $\abs z = 1$; and $F:\DD\to\DD$ is bijective.

::: pf-proof

::: pf-step
$F$ is holomorphic on $\DD$, $F(\DD)\subseteq\DD$, and $\abs{F(z)} = 1$ for $\abs z = 1$.

::: pf-proof
$F$ is rational, with its only pole at $z = 1/\bar w$ (or none if $w=0$), and $\abs{1/\bar w}>1$; so $F$ is holomorphic on a neighborhood of the closed disk.
For $\abs z\leq 1$ we have $\abs{\bar z w}<1$, so step [](#part-a){.pf-ref} applies and gives both remaining claims.
:::

:::

::: pf-step
$F(0) = w$ and $F(w) = 0$.

::: pf-proof
Substitute: $F(0) = w/1$ and $F(w) = 0/(1-\abs w^2)$.
:::

:::

::: pf-step
$F\circ F = \id_{\DD}$, so $F:\DD\to\DD$ is bijective.

::: pf-proof
Multiplying numerator and denominator of $F(F(z)) = \frac{w - F(z)}{1 - \bar w F(z)}$ by $1 - \bar w z$ gives
$$
F(F(z)) = \frac{w(1 - \bar w z) - (w - z)}{(1 - \bar w z) - \bar w(w - z)} = \frac{z(1 - \abs w^2)}{1 - \abs w^2} = z.
$$
A self-map of $\DD$ that is its own inverse is a bijection.
:::

:::

:::

:::

:::

:::
