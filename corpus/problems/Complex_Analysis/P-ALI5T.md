---
schema: qual/card@1
id: P-ALI5T
kind: problem
title: A holomorphic function real-valued on a closed curve is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Open Mapping Theorem
  - Maximum Modulus Principle
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Assume $f(z)$ is analytic in a region $D$ and $\Gamma$ is a simple closed rectifiable curve in $D$ whose interior $\Omega$ is contained in $D$.
Prove that if $f(z)$ is real-valued for all $z \in \Gamma$, then $f(z)$ is constant on $D$.
:::

::: {.solution}
Write $f=u+iv$.
Then $v$ is harmonic on $D$, $v=0$ on $\Gamma=\partial\Omega$, and $\overline\Omega=\Omega\cup\Gamma\subset D$ is compact.
By the Jordan curve theorem, $\Omega$ is a nonempty connected open set.

::: pf

::: {.pf-step #v-zero}
$v\equiv0$ on $\Omega$.

::: pf-proof
The maximum principle for the harmonic functions $v$ and $-v$ on the bounded domain $\Omega$, which are continuous on $\overline\Omega$ and vanish on $\partial\Omega$, gives $v\le0$ and $-v\le0$ on $\Omega$.
:::

:::

::: {.pf-step #constant-on-omega}
$f$ is constant on $\Omega$.

::: pf-proof
By step [](#v-zero){.pf-ref}, $f(\Omega)\subseteq\RR$.
If $f$ were nonconstant on the domain $\Omega$, the open mapping theorem would make $f(\Omega)$ a nonempty open subset of $\CC$, which cannot lie in $\RR$.
:::

:::

::: pf-step
$f$ is constant on $D$.

::: pf-proof
By step [](#constant-on-omega){.pf-ref}, $f\equiv c$ on the nonempty open set $\Omega$, so $f-c$ vanishes there, and the identity theorem on the connected set $D$ gives $f\equiv c$ on $D$.
:::

:::

:::

:::
