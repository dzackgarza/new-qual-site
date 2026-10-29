---
schema: qual/card@1
id: P-TFO34
kind: problem
title: $z\mapsto\overline{f(\bar z)}$ is analytic if $f$ is
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Reflection
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Prove that if $z\mapsto f(z)$ is analytic, then $z \mapsto \overline{f(\bar z)}$ is analytic.
:::

::: {.solution}
Let $f$ be analytic on an open set $\Omega$, put $\Omega^* \coloneqq \{\bar z : z \in \Omega\}$, and define $g(z) \coloneqq \overline{f(\bar z)}$ for $z \in \Omega^*$. Fix $w_0 \in \Omega^*$ and put $z_0 = \bar w_0 \in \Omega$.

::: pf

::: {.pf-step #taylor}

There are $r > 0$ and coefficients $a_n$ with $f(z) = \sum_{n=0}^{\infty} a_n (z - z_0)^n$ for $\abs{z - z_0} < r$.

::: pf-proof

An analytic function is represented by its Taylor series on a disc about each point of its domain.

:::

:::

::: {.pf-step #conj}

For $\abs{z - w_0} < r$, $g(z) = \sum_{n=0}^{\infty} \bar a_n (z - w_0)^n$.

::: pf-proof

If $\abs{z - w_0} < r$, then $\abs{\bar z - z_0} = \abs{z - w_0} < r$, so step [](#taylor){.pf-ref} applies at $\bar z$. Complex conjugation is continuous and additive, so it passes through the convergent series term by term, and $\overline{a_n(\bar z - z_0)^n} = \bar a_n (z - w_0)^n$.

:::

:::

::: pf-step

$g$ is analytic on $\Omega^*$.

::: pf-proof

By step [](#conj){.pf-ref}, $g$ is given by a convergent power series on a disc about $w_0$, so $g$ is analytic at $w_0$. The point $w_0 \in \Omega^*$ was arbitrary.

:::

:::

:::

:::
