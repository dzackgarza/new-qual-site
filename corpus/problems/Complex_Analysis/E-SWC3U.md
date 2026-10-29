---
schema: qual/card@1
id: E-SWC3U
kind: problem
title: $\bigl|\frac{w-z}{1-\bar{w}z}\bigr|$ on the closed disk, and $z\mapsto\frac{w-z}{1-\bar{w}z}$
  is an automorphism of $\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Biholomorphisms
  - Schwarz Lemma
relations: []
review: draft
---

::: {.problem}
(a) Let $z, w$ be complex numbers, such that $\bar{z} w \neq 1$.
Prove that
$$\abs{\frac{w - z}{1 - \bar{w} z}} < 1 \quad \text{if } \abs{z} < 1 \text{ and } \abs{w} < 1,$$
and also that
$$\abs{\frac{w - z}{1 - \bar{w} z}} = 1 \quad \text{if } \abs{z} = 1 \text{ or } \abs{w} = 1.$$

(b) Prove that for fixed $w$ in the unit disk $\DD$, the
mapping $$F: z \mapsto \frac{w - z}{1 - \bar{w} z}$$ satisfies the following conditions:

- $F$ maps $\DD$ to itself and is holomorphic.

- $F$ interchanges $0$ and $w$, namely, $F(0) = w$ and $F(w) = 0$.

- $\abs{F(z)} = 1$ if $\abs{z} = 1$.

- $F: \DD \to \DD$ is bijective.
:::

::: {.hint}
For the bijectivity in (b), calculate $F \circ F$.
:::

::: {.solution}

::: pf

::: {.pf-step #identity}
$\abs{1-\bar wz}^2-\abs{w-z}^2 = (1-\abs{w}^2)(1-\abs{z}^2)$ for all $z,w\in\CC$.

::: pf-proof
Expanding both squared moduli,
$$
\abs{1-\bar wz}^2-\abs{w-z}^2 = \left(1-\bar wz-w\bar z+\abs{w}^2\abs{z}^2\right) - \left(\abs{w}^2-w\bar z-\bar wz+\abs{z}^2\right) = 1 - \abs{w}^2 - \abs{z}^2 + \abs{w}^2\abs{z}^2,
$$
which factors as claimed.
:::

:::

::: {.pf-step #part-a}
Part (a) holds.

::: pf-proof
The hypothesis $\bar zw\neq 1$ is equivalent to $\bar wz\neq 1$, so the quotient is defined. If $\abs{z}<1$ and $\abs{w}<1$, the right side of step [](#identity){.pf-ref} is positive, so $\abs{w-z}<\abs{1-\bar wz}$. If $\abs{z}=1$ or $\abs{w}=1$, the right side is $0$, so the two moduli are equal.
:::

:::

::: {.pf-step #holo}
For $w\in\DD$, $F$ is holomorphic on $\DD$, maps $\DD$ to $\DD$, and satisfies $\abs{F(z)}=1$ for $\abs{z}=1$.

::: pf-proof
For $\abs{z}\leq 1$, $\abs{\bar wz}<1$, so the denominator does not vanish on the closed disk and $F$ is holomorphic there. The remaining two claims are step [](#part-a){.pf-ref}.
:::

:::

::: pf-step
$F(0) = w$ and $F(w) = 0$.

::: pf-proof
$F(0) = w/1$ and $F(w) = 0/(1-\abs{w}^2)$.
:::

:::

::: pf-step
$F\circ F = \mathrm{id}_\DD$, so $F:\DD\to\DD$ is bijective.

::: pf-proof
For $z\in\DD$, multiplying numerator and denominator of $F(F(z))$ by $1-\bar wz$ gives
$$
F(F(z)) = \frac{w(1-\bar wz) - (w-z)}{(1-\bar wz) - \bar w(w-z)} = \frac{z(1-\abs{w}^2)}{1-\abs{w}^2} = z.
$$
By step [](#holo){.pf-ref}, $F$ maps $\DD$ into $\DD$, so $F$ is its own inverse on $\DD$.
:::

:::

:::

:::
