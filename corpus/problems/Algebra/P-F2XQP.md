---
schema: qual/card@1
id: P-F2XQP
kind: problem
title: Polar decomposition of operators on a Hilbert space
classification:
  areas:
  - algebra
  topics:
  - Functional Analysis
  - Diagonalization
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Consider the simple operator on $\CC$ given by multiplication by a complex number.
It decomposes into a stretch and a rotation.
What is the generalisation of this to operators on a Hilbert space?
:::

::: {.solution}
The generalization of $z=e^{i\theta}\abs{z}$ is the polar decomposition.
Let $H$ be a complex Hilbert space, $T\in B(H)$, and $\operatorabs{T}=\sqrt{T^*T}$, the unique positive square root of the positive operator $T^*T$.
Recall that a [[D-W4KQ7|partial isometry]] is an operator $U$ that is isometric on $(\ker U)^\perp$.

::: pf

::: {.pf-step #s1}

$\norm{\,\operatorabs{T}x\,}=\norm{Tx}$ for every $x\in H$; hence $\ker\operatorabs{T}=\ker T$ and $\overline{\im\operatorabs{T}}=(\ker T)^\perp$.

::: pf-proof

$\norm{\,\operatorabs{T}x\,}^2=\inner{\operatorabs{T}^2x}{x}=\inner{T^*Tx}{x}=\norm{Tx}^2$.
Since $\operatorabs{T}$ is self-adjoint, $\overline{\im\operatorabs{T}}=(\ker\operatorabs{T})^\perp$.

:::

:::

::: pf-step

There is a partial isometry $U$ with $\ker U=\ker T$ and $T=U\operatorabs{T}$.

::: pf-proof

Define $U_0\colon\im\operatorabs{T}\to\im T$ by $U_0(\operatorabs{T}x)=Tx$; it is well defined and isometric by step [](#s1){.pf-ref}.
It extends by continuity to an isometry $U_1\colon\overline{\im\operatorabs{T}}\to\overline{\im T}$.
Put $U=U_1$ on $\overline{\im\operatorabs{T}}$ and $U=0$ on its orthogonal complement $\ker\operatorabs{T}=\ker T$.
Then $U\operatorabs{T}x=Tx$ for every $x$.

:::

:::

::: pf-step

If $T=WP$ with $P\ge0$ and $W$ a partial isometry with $\ker W=\ker P$, then $P=\operatorabs{T}$ and $W=U$.

::: pf-proof

$W^*W$ is the orthogonal projection onto $(\ker W)^\perp=(\ker P)^\perp=\overline{\im P}$, so $T^*T=PW^*WP=P^2$, and $P=\operatorabs{T}$ by uniqueness of positive square roots.
Then $W(\operatorabs{T}x)=Tx=U(\operatorabs{T}x)$, so $W=U$ on $\overline{\im\operatorabs{T}}$, and both vanish on $\ker\operatorabs{T}$.

:::

:::

::: pf-step

If $T$ is invertible, then $U$ is unitary.

::: pf-proof

Then $\ker T=0$ and $\im T=H$, so $U$ is an isometry of $H$ onto $H$.

:::

:::

:::

:::
