---
schema: qual/card@1
id: P-TOPS00D
kind: problem
title: "Suspension of RP^2 is not homotopy equivalent to a compact manifold"
classification:
  areas:
  - topology
  topics:
  - Homotopy Type
  - Manifolds
  - Suspensions
relations: []
review: draft
---

::: {.problem}
Let $X$ be the suspension of $\mathbb{RP}^2$, i.e.
$$
X = \mathbb{RP}^2 \times [0, 1] / (\mathbb{RP}^2 \times \{0\}), (\mathbb{RP}^2 \times \{1\}).
$$
Prove that $X$ is not homotopy equivalent to a compact manifold.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The suspension $X=\Sigma\mathbb{RP}^2$ is simply connected.

::: pf-proof

The suspension of any path-connected space is the union of two contractible cones with path-connected intersection, so van Kampen gives trivial fundamental group.

:::

:::

::: {.pf-step #s2}

Its reduced integral homology is
$$
\widetilde H_i(X;\mathbb Z)\cong
\widetilde H_{i-1}(\mathbb{RP}^2;\mathbb Z),
$$
so the only nonzero reduced group is
$$
\widetilde H_2(X;\mathbb Z)\cong\mathbb Z/2.
$$

::: pf-proof

Suspension shifts reduced homology by one degree. Since $\widetilde H_1(\mathbb{RP}^2)=\mathbb Z/2$ and all other reduced integral homology groups vanish, the claim follows.

:::

:::

::: pf-step

Suppose $X$ were homotopy-equivalent to a compact connected manifold $M$ of dimension $m$.

::: pf-proof

Under the standard convention in the problem, “manifold” means without boundary.

:::

:::

::: {.pf-step #s4}

Then $M$ would be simply connected and hence orientable, so
$$
H_m(M;\mathbb Z)\cong\mathbb Z.
$$

::: pf-proof

Homotopy equivalence preserves fundamental groups, so $\pi_1(M)=0$ by step [](#s1){.pf-ref}. A simply connected manifold has trivial orientation character and is orientable. A compact connected orientable boundaryless $m$-manifold has an integral fundamental class generating $H_m$.

:::

:::

::: pf-step

This contradicts step [](#s2){.pf-ref}, since $X$ has no nonzero free reduced homology group in any positive degree. Hence $X$ is not homotopy-equivalent to a compact manifold.

::: pf-proof

Homotopy-equivalent spaces have isomorphic homology groups. The group in step [](#s4){.pf-ref} cannot occur among the homology groups listed in step [](#s2){.pf-ref}.

:::

:::

:::

:::
