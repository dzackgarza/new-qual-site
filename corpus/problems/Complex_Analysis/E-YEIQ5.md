---
schema: qual/card@1
id: E-YEIQ5
kind: problem
title: An analytic function sending a simple closed curve into $\RR$ is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Open Mapping Theorem
  - Maximum Modulus Principle
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source did not require the inside of gamma to lie in Omega, and f(z) = z + 1/z on the annulus 1/2 < |z| < 2 is real on the unit circle; the statement now requires the bounded component of C minus gamma to lie in Omega.'
---

::: {.problem}
Let $f$ be an analytic function on a region $\Omega$.
Show that $f$ is a constant if there is a simple closed curve $\gamma$ in $\Omega$ whose inside, the bounded component of $\CC\setminus\gamma$, is contained in $\Omega$, such that its image $f(\gamma)$ is contained in the real axis.
:::

::: {.solution}
Let $U$ be the bounded component of $\CC\setminus\gamma$. By the Jordan curve theorem $U$ is a nonempty bounded open set with $\partial U = \gamma$, and $\overline U = U\cup\gamma\subseteq\Omega$.

::: pf

::: {.pf-step #im-zero}

$\Im f = 0$ on $U$.

::: pf-proof

$v = \Im f$ is harmonic on $U$ and continuous on the compact set $\overline U$, and $v = 0$ on $\partial U = \gamma$. The maximum and minimum principles for harmonic functions give $0 \le v \le 0$ on $U$.

:::

:::

::: {.pf-step #const-on-u}

$f$ is constant on each component of $U$.

::: pf-proof

By step [](#im-zero){.pf-ref}, $f$ maps each component of $U$ into $\RR$, which contains no nonempty open subset of $\CC$. By the open mapping theorem, $f$ is constant there.

:::

:::

::: pf-qed

By step [](#const-on-u){.pf-ref}, $f$ is constant on a nonempty open subset of the connected region $\Omega$, so the identity theorem makes $f$ constant on $\Omega$.

:::

:::

:::
