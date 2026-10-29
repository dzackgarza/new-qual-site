---
schema: qual/card@1
id: P-XWO5N
kind: problem
title: The Blaschke factor $z\mapsto\frac{w-z}{1-\bar{w}z}$ as a biholomorphism of
  $\DD$
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
(a) Let $z, w \in \CC$ with $\bar z w \neq 1$.
Prove that
$$
\abs{\frac{w-z}{1 - \bar w z}} < 1 \quad\text{ if } \abs{z}<1,~ \abs{w} < 1
$$
with equality when $\abs{z} = 1$ or $\abs{w} = 1$.

(b) Prove that for a fixed $w\in \DD$, the mapping $F: z\mapsto \frac{w-z}{1 - \bar w z}$ satisfies

- $F$ maps $\DD$ to itself and is holomorphic.

- $F(0) = w$ and $F(w) = 0$.

- $\abs{z} = 1$ implies $\abs{F(z)} = 1$.

- $F$ is a bijection.

:::

::: {.solution}

::: pf

::: {.pf-step #identity}
If $\bar w z\ne1$, then $\abs{1-\bar wz}^2-\abs{w-z}^2=(1-\abs{w}^2)(1-\abs{z}^2)$.

::: pf-proof
Expanding,
$$
\begin{aligned}
\abs{1-\bar wz}^2&=1-\bar wz-w\bar z+\abs{w}^2\abs{z}^2,\\
\abs{w-z}^2&=\abs{w}^2-\bar wz-w\bar z+\abs{z}^2,
\end{aligned}
$$
and the difference is $1-\abs{w}^2-\abs{z}^2+\abs{w}^2\abs{z}^2=(1-\abs{w}^2)(1-\abs{z}^2)$.
The condition $\bar zw\ne1$ is equivalent to $\bar wz\ne1$, since the two numbers are complex conjugates, so the denominator does not vanish.
:::

:::

::: {.pf-step #part-a}
Part (a) holds.

::: pf-proof
If $\abs{z}<1$ and $\abs{w}<1$, the right side of step [](#identity){.pf-ref} is positive, so $\abs{w-z}<\abs{1-\bar wz}$.
If $\abs{z}=1$ or $\abs{w}=1$, it is zero, so $\abs{w-z}=\abs{1-\bar wz}$.
:::

:::

::: {.pf-step #holo}
For $w\in\DD$, $F$ is holomorphic on $\DD$ and $F(\DD)\subseteq\DD$.

::: pf-proof
$F$ is a rational function whose only pole is $z=1/\bar w$ when $w\ne0$, and it has no pole when $w=0$. Since $\abs{1/\bar w}>1$, $F$ is holomorphic on a neighborhood of $\overline{\DD}$.
For $z\in\DD$, step [](#part-a){.pf-ref} gives $\abs{F(z)}<1$.
:::

:::

::: pf-step
$F(0)=w$ and $F(w)=0$.

::: pf-proof
$F(0)=\frac{w-0}{1-0}=w$, and the numerator of $F(w)$ is $w-w=0$ while its denominator is $1-\abs{w}^2\ne0$.
:::

:::

::: pf-step
If $\abs{z}=1$, then $\abs{F(z)}=1$.

::: pf-proof
This is the equality case of step [](#part-a){.pf-ref}; the denominator is nonzero because $\abs{\bar wz}=\abs{w}<1$.
:::

:::

::: pf-step
$F\colon\DD\to\DD$ is a bijection.

::: pf-proof
For $z\in\DD$, step [](#holo){.pf-ref} puts $F(z)$ in $\DD$, and
$$
F(F(z))=\frac{w(1-\bar wz)-(w-z)}{(1-\bar wz)-\bar w(w-z)}
=\frac{z(1-\abs{w}^2)}{1-\abs{w}^2}=z.
$$
So $F\circ F=\id_\DD$, and $F$ is its own inverse.
:::

:::

:::

:::
