---
schema: qual/card@1
id: E-HAT-1.1-12
kind: exercise
title: Every homomorphism $\pi_1(S^1) \to \pi_1(S^1)$ is induced by a map
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Circle
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Show that every homomorphism $\pi_1(S^1) \to \pi_1(S^1)$ can be realized as the induced homomorphism $\varphi_*$ of a map $\varphi: S^1 \to S^1$.

::: {.solution}
<1>1. $\pi_1(S^1) = \ZZ$, so a homomorphism $\pi_1(S^1) \to \pi_1(S^1)$ is multiplication by some integer $n$.
::: {.proof}
$\operatorname{Hom}(\ZZ, \ZZ) = \ZZ$.
:::

<1>2. Define $\varphi_n: S^1 \to S^1$ by $\varphi_n(z) = z^n$ (viewing $S^1 \subset \CC$).
::: {.proof}
definition.
:::

<1>3. $\varphi_n$ has degree $n$, so $(\varphi_n)_*$ is multiplication by $n$ on $\pi_1(S^1) = \ZZ$.
::: {.proof}
the map $z \mapsto z^n$ has degree $n$, and the induced map on $\pi_1$ is multiplication by the degree.
:::

<1>4. Hence every homomorphism (multiplication by $n$) is realized by $\varphi_n$.
::: {.proof}
<1>1 and <1>3.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4.
:::
:::
