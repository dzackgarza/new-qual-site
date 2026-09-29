---
schema: qual/card@1
id: P-AMD-YTDBSOKB
kind: problem
title: $\pi_1(S^n/\ZZ_2)$ for three $\ZZ_2$-actions
classification:
  areas:
  - topology
  topics:
  - Group Actions
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
For each of these actions of $\mathbb{Z}_2$ on $S^n$, compute $\pi_1(S^n/\mathbb{Z}_2)$

1. $S^1, z\mapsto -z$

2. $S^2, (x,y,z) \mapsto (-x,-y,z)$

3. $S^3, (z,w) \mapsto (-z, -w)$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Case 1: $S^1$ with $z \mapsto -z$.

::: pf-proof

::: pf-step

The action is free (no fixed points).

::: pf-proof

$z = -z$ implies $z = 0 \notin S^1$.

:::

:::

::: {.pf-step #s1-2}

Hence $S^1 \to S^1/\ZZ_2$ is a $2$-sheeted covering, and $S^1/\ZZ_2 \cong S^1$.

::: pf-proof

the quotient of $S^1$ by the antipodal map is again $S^1$ (the map $z \mapsto z^2$ identifies antipodal points).

:::

:::

::: pf-step

Therefore $\pi_1(S^1/\ZZ_2) = \pi_1(S^1) = \ZZ$.

::: pf-proof

Step [](#s1-2){.pf-ref}.

:::

:::

:::

:::

::: {.pf-step #s2}

Case 2: $S^2$ with $(x,y,z) \mapsto (-x,-y,z)$.

::: pf-proof

::: pf-step

The fixed points are the two poles $(0,0,\pm 1)$.

::: pf-proof

$(-x,-y,z) = (x,y,z)$ iff $x = y = 0$.

:::

:::

::: {.pf-step #s2-2}

The quotient $S^2/\ZZ_2$ is homeomorphic to $S^2$.

::: pf-proof

Write a point of $S^2$ as $(re^{i\theta},z)\in\CC\times\RR$ with $r^2+z^2=1$. The action sends $(re^{i\theta},z)$ to $(re^{i(\theta+\pi)},z)$. Define
$$
Q(re^{i\theta},z)=(re^{2i\theta},z).
$$
At the poles $r=0$ this is independent of $\theta$, and the formula is continuous there because the horizontal coordinate has norm $r$. It is constant exactly on the two-point orbits of the rotation away from the poles and fixes each pole. Hence it factors through a continuous bijection
$$
\overline Q:S^2/\ZZ_2\longrightarrow S^2.
$$
The domain is compact and the target Hausdorff, so $\overline Q$ is a homeomorphism.

:::

:::

::: pf-step

Therefore $\pi_1(S^2/\ZZ_2) = \pi_1(S^2) = 0$.

::: pf-proof

Step [](#s2-2){.pf-ref} and $\pi_1(S^2) = 0$.

:::

:::

:::

:::

::: {.pf-step #s3}

Case 3: $S^3$ with $(z,w) \mapsto (-z,-w)$.

::: pf-proof

::: pf-step

The action is free (no fixed points).

::: pf-proof

$(-z,-w) = (z,w)$ iff $z = w = 0 \notin S^3$.

:::

:::

::: pf-step

Hence $S^3 \to S^3/\ZZ_2$ is a $2$-sheeted covering, and $S^3/\ZZ_2 = \RP^3$.

::: pf-proof

the antipodal map on $S^3$ has quotient the real projective space $\RP^3$.

:::

:::

::: pf-step

Therefore $\pi_1(S^3/\ZZ_2) = \pi_1(\RP^3) = \ZZ/2$.

::: pf-proof

$\pi_1(\RP^3) = \ZZ/2$ (its universal cover is $S^3$ with deck group $\ZZ/2$).

:::

:::

:::

:::

::: pf-qed

$\pi_1 = \ZZ$, $0$, $\ZZ/2$ respectively (steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}).

:::

:::

:::
