---
schema: qual/card@1
id: P-TQBRQ
kind: problem
title: A nonvanishing holomorphic function with $|f|=1$ on the unit circle is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Schwarz Reflection
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Suppose $f$ is continuous and nonvanishing on $\bar \DD$, and holomorphic in $\DD$.
Prove that if $\abs{z} = 1 \implies \abs{f(z)} = 1$, then $f$ is constant.

> Hint: Extend $f$ to all of $\CC$ by $f(z) = 1/ \bar{f(1/\bar z)}$ for any $\abs{z} > 1$, and argue as in the Schwarz reflection principle.
:::

::: {.solution}
**Goal:** If $f$ is continuous and nonvanishing on $\bar\DD$, holomorphic in $\DD$, and $\abs{f(z)} = 1$ for $\abs{z} = 1$, prove $f$ is constant.

::: pf

::: {.pf-step #s1}

$\abs{f(z)} \leq 1$ for $z \in \DD$.

::: pf-proof

By the maximum modulus principle applied to $f$ on $\DD$, since $\abs f = 1$ on the boundary $\abs{z} = 1$.

:::

:::

::: {.pf-step #s2}

$\abs{f(z)} \geq 1$ for $z \in \DD$.

::: pf-proof

$f$ is nonvanishing on $\bar\DD$, so $1/f$ is holomorphic on a neighborhood of $\bar\DD$; the maximum modulus principle applied to $1/f$ gives $\abs{1/f(z)} \leq \max_{\abs{\zeta}=1}\abs{1/f(\zeta)} = 1$, i.e. $\abs{f(z)} \geq 1$.

:::

:::

::: pf-step

$\abs{f(z)} = 1$ for all $z \in \DD$.

::: pf-proof

Combine steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

::: pf-step

Define the reflection $F$ on $\CC$ by $F(z) = f(z)$ for $\abs{z} \leq 1$ and $F(z) = \frac{1}{\overline{f(1/\bar z)}}$ for $\abs{z} > 1$; then $F$ is well defined and continuous.

::: pf-proof

For $\abs{z} > 1$, $1/\bar z$ lies in $\DD \setminus \theset{0}$ (indeed $\abs{1/\bar z} = 1/\abs z < 1$), where $f \neq 0$ by assumption, so the formula makes sense.

As $\abs{z} \to 1^+$, $1/\bar z \to 1/z = \bar z$ ... precisely, $1/\bar z \to \bar\zeta$ with $\abs\zeta = 1$; using $\abs{f} = 1$ on the circle, $F(z) = 1/\overline{f(1/\bar z)} \to 1/\overline{f(\bar\zeta)} = f(\zeta)$, so $F$ matches $f$ continuously across $\abs{z} = 1$.

:::

:::

::: {.pf-step #s5}

$F$ is holomorphic on $\CC \setminus \partial\DD$ and satisfies $F(z) = \overline{F(1/\bar z)}^{-1}$ (the reflection functional equation); by the Schwarz reflection principle $F$ is entire.

::: pf-proof

On $\abs{z} < 1$, $F = f$ is holomorphic.

On $\abs{z} > 1$, $z \mapsto 1/\bar z$ is antiholomorphic, so $f(1/\bar z)$ is antiholomorphic and its conjugate $\overline{f(1/\bar z)}$ is holomorphic; since $f \neq 0$ there, $F = 1/\overline{f(1/\bar z)}$ is holomorphic.
The identity $F(z) = 1/\overline{F(1/\bar z)}$ holds by definition (and extends across the circle), and $\abs F = 1$ on $\partial\DD$, so the Schwarz reflection principle applies: the two holomorphic pieces glue into a single entire function.

:::

:::

::: {.pf-step #s6}

$F$ is bounded on $\CC$.

::: pf-proof

On $\abs z \leq 1$, $\abs F = \abs f \leq 1$ by step [](#s1){.pf-ref} (or by compactness, $f$ bounded).

On $\abs z > 1$, $\abs{F(z)} = \frac{1}{\abs{f(1/\bar z)}} \leq 1$ by step [](#s2){.pf-ref} applied to $1/\bar z \in \DD$.
Hence $\abs F \leq 1$ everywhere.

:::

:::

::: {.pf-step #s7}

$F$ is constant, hence $f$ is constant.

::: pf-proof

By Liouville's theorem, the bounded entire function $F$ from steps [](#s5){.pf-ref} and [](#s6){.pf-ref} is constant; restricting to $\DD$ shows $f$ is constant.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} proves the claim.

:::

:::

:::
