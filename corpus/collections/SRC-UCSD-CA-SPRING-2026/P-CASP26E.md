---
schema: qual/card@1
id: P-CASP26E
kind: problem
title: 'A bounded harmonic function on $\abs z>1$ with $u\leq 0$ on $\abs z=1$ is nonpositive'
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Maximum Principle
  - Boundary Values
relations: []
review: draft
---

::: {.problem}
Let $G = \{z \in \CC : \abs{z} > 1\}$.
Let $u : \overline{G} \to \RR$ be a continuous bounded function, such that $u$ is harmonic in $G$.
Assume $u(z) \leq 0$ for all $\abs{z} = 1$.
Show that $u(z) \leq 0$ for all $z \in G$.
:::

::: {.solution}

The argument is the card's own, by inversion and the removable singularity theorem; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $G=\{z\in\CC:\abs{z}>1\}$, and let $u$ be continuous and bounded on $\overline{G}$ and harmonic on $G$, with $u\le0$ on the circle $\abs{z}=1$.

::: pf

::: {.pf-step #inversion}
$v(w)=u(1/w)$ is harmonic on the punctured disc $0<\abs{w}<1$ and bounded there.

::: pf-proof
The map $w\mapsto1/w$ is holomorphic on $\CC\setminus\{0\}$ with nonzero derivative $-1/w^{2}$, hence conformal, and the composition of a harmonic function with a conformal map is harmonic; so $v$ is harmonic on $\{0<\abs{w}<1\}$, which the inversion carries onto $G$. Since $u$ is bounded on $\overline{G}$ by some $M$, $\abs{v}\le M$ on the punctured disc.
:::

:::

::: {.pf-step #removable}
$v$ extends to a harmonic function on the whole disc $\DD=\{w:\abs{w}<1\}$, continuous on $\overline{\DD}$.

::: pf-proof
A function harmonic and bounded on a punctured disc extends harmonically across the puncture: the removable singularity theorem for harmonic functions, applied to $v$ at $0$. Its extension is continuous on $\abs{w}\le1$ because $u$ is continuous on $\overline{G}$, hence on $\abs{w}=1$, and the extension is continuous at $0$ by construction. So the extension, again written $v$, is continuous on the closed disc and harmonic in its interior.
:::

:::

::: {.pf-step #boundary}
$v\le0$ on $\abs{w}=1$.

::: pf-proof
For $\abs{w}=1$ one has $\abs{1/w}=1$, so $v(w)=u(1/w)\le0$ by hypothesis.
:::

:::

::: {.pf-step #maximum}
$v\le0$ on $\DD$.

::: pf-proof
$v$ is harmonic on $\DD$ and continuous on $\overline{\DD}$, so by the maximum principle it attains its maximum on $\overline{\DD}$ at a boundary point, that is $\max_{\overline{\DD}}v=\max_{\abs{w}=1}v\le0$ by step [](#boundary){.pf-ref}. Hence $v\le0$ throughout $\DD$.
:::

:::

::: {.pf-step #conclusion}
$u(z)\le0$ for all $z\in G$.

::: pf-proof
Let $z\in G$ and put $w=1/z$, which lies in $\DD$. Then $u(z)=u(1/w)=v(w)\le0$ by step [](#maximum){.pf-ref}. So $u\le0$ on $G$, which is the assertion.
:::

:::

:::
:::
