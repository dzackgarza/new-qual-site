---
schema: qual/card@1
id: P-LRCVT
kind: problem
title: Blaschke factors as automorphisms of the disk
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
- event: copy-repaired
  by: Claude Opus 5.5
  date: 2026-10-29
  note: "Removed a duplicated extraction heading (Tie's Extra Questions: Fall 2015) from the statement and moved the source hint into a hint block."
---

::: {.problem}
(a) Let $z, w$ be complex numbers, such that $\bar{z} w \neq 1$.
Prove that
$$\abs{\frac{w - z}{1 - \bar{w} z}} < 1 \quad \text{if } \abs{z} < 1 \text{ and } \abs{w} < 1,$$
and also that
$$\abs{\frac{w - z}{1 - \bar{w} z}} = 1 \quad \text{if } \abs{z} = 1 \text{ or } \abs{w} = 1.$$

(b) Prove that for fixed $w$ in the unit disk $\DD$, the
mapping $$F: z \mapsto \frac{w - z}{1 - \bar{w} z}$$ satisfies the
following conditions:

(i) $F$ maps $\DD$ to itself and is holomorphic.

(ii) $F$ interchanges $0$ and $w$, namely, $F(0) = w$ and
$F(w) = 0$.

(iii) $\abs{F(z)} = 1$ if $\abs{z} = 1$.

(iv) $F: \DD \to \DD$ is bijective.
:::

::: {.hint}
Calculate $F \circ F$.
:::

::: {.solution}
::: pf

::: {.pf-step #identity}
$\abs{1-\bar wz}^2-\abs{w-z}^2=(1-\abs{w}^2)(1-\abs{z}^2)$.

::: pf-proof
Expand: $\abs{1-\bar wz}^2 = 1 - \bar w z - w\bar z + \abs{w}^2\abs{z}^2$ and $\abs{w-z}^2 = \abs{w}^2 - \bar w z - w\bar z + \abs{z}^2$. The difference is $1-\abs{w}^2-\abs{z}^2+\abs{w}^2\abs{z}^2$.
:::

:::

::: {.pf-step #part-a}
(a) holds.

::: pf-proof
Since $1-\bar w z$ is the conjugate of $1-w\bar z\neq 0$, the denominator is nonzero. If $\abs{z},\abs{w}<1$, the right side of step [](#identity){.pf-ref} is positive, so $\abs{w-z}<\abs{1-\bar wz}$. If $\abs{z}=1$ or $\abs{w}=1$, it is zero, so $\abs{w-z}=\abs{1-\bar wz}$.
:::

:::

::: {.pf-step #part-b-iii}
(b)(i)--(iii) hold.

::: pf-proof
For $\abs{w}<1$ and $\abs{z}\le 1$, $\abs{\bar w z}<1$, so the denominator does not vanish on a neighbourhood of $\overline{\DD}$ and $F$ is holomorphic on $\DD$. Part (a) gives $F(\DD)\subseteq\DD$ and $\abs{F(z)}=1$ for $\abs{z}=1$. Substitution gives $F(0)=w$ and $F(w)=0$.
:::

:::

::: pf-step
(b)(iv) holds.

::: pf-proof
For $z\in\DD$,
$$
F(F(z))=\frac{w-\frac{w-z}{1-\bar wz}}{1-\bar w\frac{w-z}{1-\bar wz}}
=\frac{w-\abs{w}^2z-w+z}{1-\bar wz-\abs{w}^2+\bar wz}
=\frac{z(1-\abs{w}^2)}{1-\abs{w}^2}=z.
$$
So $F\circ F$ is the identity on $\DD$, and with step [](#part-b-iii){.pf-ref} $F$ is a bijection of $\DD$ onto itself, its own inverse.
:::

:::

:::
:::
