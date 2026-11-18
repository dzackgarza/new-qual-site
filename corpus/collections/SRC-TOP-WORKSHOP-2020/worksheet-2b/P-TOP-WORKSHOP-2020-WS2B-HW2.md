---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS2B-HW2
kind: problem
title: Radial deformation retraction $\RR^n\setminus\{0\}\to S^{n-1}$
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Homotopy
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the homotopy defined and shown to land in the
    punctured space, its two endpoints, and its fixing the sphere pointwise. No retained solution set
    covers this exercise (the collection retains the worksheets, not solutions), so the argument is the
    card's own; the formula was checked for this pass at $t=0,1$ and on $S^{n-1}$.
---

::: {.problem}
Construct an explicit deformation retraction from $\RR^n\setminus\{0\}$ onto $S^{n-1}$.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, and the formula below was checked for this pass at both endpoints and on the sphere.

A deformation retraction of $\RR^{n}\setminus\{0\}$ onto $S^{n-1}$ is a homotopy $H$ from the identity to a map into $S^{n-1}$ that fixes $S^{n-1}$ pointwise at every time.

::: pf

::: {.pf-step #well-defined}
$H(x,t)=\left((1-t)+\frac{t}{\norm{x}}\right)x$ defines a continuous map $(\RR^{n}\setminus\{0\})\times[0,1]\to\RR^{n}\setminus\{0\}$.

::: pf-proof
The scalar $\lambda(x,t)=(1-t)+t/\norm{x}$ is a continuous function of $(x,t)$ on $(\RR^{n}\setminus\{0\})\times[0,1]$, being built from $t$ and the continuous function $1/\norm{x}$, so $H=\lambda\cdot x$ is continuous. For $x\ne0$ and $0\le t\le1$ the scalar is a convex combination of $1$ and $1/\norm{x}$, both positive, hence $\lambda(x,t)>0$; therefore $H(x,t)\ne0$ and $H$ takes values in $\RR^{n}\setminus\{0\}$.
:::

:::

::: {.pf-step #endpoints}
$H(x,0)=x$ and $H(x,1)=x/\norm{x}\in S^{n-1}$.

::: pf-proof
At $t=0$ the scalar is $1$, so $H(x,0)=x$. At $t=1$ it is $1/\norm{x}$, so $H(x,1)=x/\norm{x}$, whose norm is $1$. Hence $H_{0}$ is the identity and $H_{1}$ maps into the unit sphere.
:::

:::

::: {.pf-step}
$H$ fixes $S^{n-1}$ pointwise: $H(y,t)=y$ for every $y\in S^{n-1}$ and every $t$.

::: pf-proof
For $y\in S^{n-1}$ one has $\norm{y}=1$, so the scalar is $(1-t)+t=1$ and $H(y,t)=y$. Hence $H$ is a homotopy from the identity of $\RR^{n}\setminus\{0\}$ to a retraction onto $S^{n-1}$ which fixes the sphere at every time, that is a deformation retraction as required.
:::

:::

:::
:::
