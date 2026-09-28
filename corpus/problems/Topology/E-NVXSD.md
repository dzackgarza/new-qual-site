---
schema: qual/card@1
id: E-NVXSD
kind: problem
title: The continuous image of a compact space is compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuity
relations: []
review: draft
---

::: {.exercise}
Show that if $f:X\to Y$ is continuous and $X$ is compact then $f(X)$ is compact.

#### Exercise
:::

::: {.solution}
<1>1. Let $\mathcal U$ be an open cover of $f(X)$. Then $\{f^{-1}(U):U\in\mathcal U\}$ is an open cover of $X$.
::: {.proof}
Continuity makes each preimage open, and every $x\in X$ maps into some member of $\mathcal U$.
:::

<1>2. Compactness of $X$ gives finitely many $U_1,\dots,U_r\in\mathcal U$ whose preimages cover $X$.
::: {.proof}
Apply the definition of compactness to the cover in <1>1.
:::

<1>3. Then $U_1,\dots,U_r$ cover $f(X)$, so $f(X)$ is compact.
::: {.proof}
For $y=f(x)$, some $f^{-1}(U_i)$ contains $x$, hence $y\in U_i$.
:::
:::
