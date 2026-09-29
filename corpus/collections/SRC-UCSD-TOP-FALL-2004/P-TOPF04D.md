---
schema: qual/card@1
id: P-TOPF04D
kind: problem
title: "First homology of a compact nonorientable 3-manifold is infinite"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Manifolds
  - Orientation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $M$ be a compact connected nonorientable $3$-manifold.
Show the first integral homology group of $M$ is infinite.
:::

::: {.solution}

::: pf

::: pf-step
The statement is correct under the standard convention that “manifold” means a manifold without boundary; under that convention compactness makes $M$ closed.

::: pf-proof
This convention is necessary. If manifolds with boundary are allowed, the statement is false: $M=\mathbb{RP}^2\times I$ is compact, connected, and nonorientable, but
$$
H_1(M;\mathbb Z)\cong H_1(\mathbb{RP}^2;\mathbb Z)\cong\mathbb Z/2,
$$
which is finite.
:::

:::

::: {.pf-step #h3-zero}
Assume therefore that $M$ is closed. Then
$$
H_3(M;\mathbb Q)=0.
$$

::: pf-proof
For a connected closed manifold, top integral homology is $\mathbb Z$ when the manifold is orientable and $0$ when it is nonorientable. Since $M$ is nonorientable, $H_3(M;\mathbb Z)=0$, hence also $H_3(M;\mathbb Q)=0$.
:::

:::

::: pf-step
One has
$$
\chi(M)=0.
$$

::: pf-proof
Let $\widetilde M\to M$ be the orientation double cover. It is a closed orientable $3$-manifold, so Poincaré duality gives $\chi(\widetilde M)=0$. Euler characteristic multiplies by the degree of a finite covering, hence
$$
0=\chi(\widetilde M)=2\chi(M).
$$
:::

:::

::: {.pf-step #b1-bound}
Therefore the first Betti number satisfies
$$
b_1(M)=1+b_2(M)\ge1.
$$

::: pf-proof
Since $M$ is connected, $b_0=1$, and by step [](#h3-zero){.pf-ref}, $b_3=0$. Hence
$$
0=\chi(M)=b_0-b_1+b_2-b_3=1-b_1+b_2,
$$
so $b_1=1+b_2$.
:::

:::

::: pf-step
Thus $H_1(M;\mathbb Z)$ is infinite.

::: pf-proof
A compact manifold has the homotopy type of a finite CW complex, so $H_1(M;\mathbb Z)$ is finitely generated. Its free rank is
$$
\operatorname{rank}H_1(M;\mathbb Z)=\dim_{\mathbb Q}H_1(M;\mathbb Q)=b_1(M)\ge1
$$
by step [](#b1-bound){.pf-ref}. Therefore it contains a copy of $\mathbb Z$ and is infinite.
:::

:::

:::

:::
