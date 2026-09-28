---
schema: qual/card@1
id: P-CASP13F
kind: problem
title: "Identity theorem from boundary vanishing on an arc of a simply connected domain"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $U \subset \mathbb{C}$ be the "rounded square" given by the intersection of the four open disks $$U = \mathbb{D}(1, 2) \cap \mathbb{D}(-1, 2) \cap \mathbb{D}(i, 2) \cap \mathbb{D}(-i, 2).$$ Let $S \subset \partial U$ be the curve $S = \{-i + 2e^{it} : t \in (\pi/4, \pi/2)\}$.
Suppose that $f \in \operatorname{Hol}(U)$, and that for any sequence $z_n \in U$ such that $\lim_{n \to \infty} z_n \in S$, it follows that $\lim_{n \to \infty} f(z_n) = 0$.
Prove that $f \equiv 0$.
:::

::: {.solution}
Fix a smaller open subarc $S_0\Subset S$. By hypothesis, $f(z)\to0$ as
$z\to\zeta$ from within $U$, uniformly in the sequential sense, for each
$\zeta\in S_0$. Define
\[
F(z)=
\begin{cases}
f(z),&z\in U,\\
0,&z\text{ in the reflected cap across the circle }|z+i|=2.
\end{cases}
\]
Across $S_0$, the two definitions match continuously.

To prove that $F$ is holomorphic across $S_0$, apply Morera's theorem on a
small neighborhood of any point of $S_0$. For a triangle crossing the arc,
split it into the portions on the two sides. The integral over the reflected
side is zero because $F=0$ there, while the integral over the $U$ side is zero
by Cauchy's theorem after approximating its boundary away from the arc; the
boundary contribution along the arc vanishes because the continuous extension
there is $0$. Hence $F$ is holomorphic across the arc.

The extended function vanishes on the open reflected side, so by the identity
theorem it vanishes on a neighborhood intersecting $U$. Therefore $f$ vanishes
on a nonempty open subset of the connected domain $U$, and another application
of the identity theorem gives
\[
\boxed{f\equiv0\text{ on }U.}
\]
:::
