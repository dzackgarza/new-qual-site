---
schema: qual/card@1
id: P-TOPF25G
kind: problem
title: $\mathbb{CP}^2$ not homotopy equivalent to $S^2 \vee S^4$; nontriviality of $\pi_3(S^2)$
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
Show that $\mathbb{CP}^2$ is not homotopy equivalent to $S^2 \vee S^4$.
Now, by considering the attaching map of the 4-cell in the standard cell decomposition of $\mathbb{CP}^2$, show that $\pi_3(S^2)$ is not trivial.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The integral cohomology ring of $\mathbb{CP}^2$ is
$$H^*(\mathbb{CP}^2;\mathbb Z)\cong\mathbb Z[u]/(u^3),\qquad |u|=2,$$
so $u^2\ne0$.

::: pf-proof

This is the standard cellular/cohomological computation for complex projective space.

:::

:::

::: {.pf-step #s2}

In $S^2\vee S^4$, every product of two positive-degree cohomology classes is zero.

::: pf-proof

The only degree-$2$ class comes from the $S^2$ summand, and its square vanishes because the inclusion/retraction to that summand factors the product through $H^4(S^2)=0$; products between distinct wedge summands vanish as well.

:::

:::

::: {.pf-step #s3}

Hence $\mathbb{CP}^2$ is not homotopy equivalent to $S^2\vee S^4$.

::: pf-proof

A homotopy equivalence induces an isomorphism of graded cohomology rings, contradicting steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

::: pf-step

The standard CW decomposition is
$$\mathbb{CP}^2=S^2\cup_\eta e^4$$
for an attaching map $\eta:S^3\to S^2$.

::: pf-proof

Complex projective space has one cell in each even dimension $0,2,4$.

:::

:::

::: {.pf-step #s5}

If $\pi_3(S^2)=0$, then $\eta$ would be null-homotopic and
$$\mathbb{CP}^2\simeq S^2\vee S^4,$$
contradicting step [](#s3){.pf-ref}.

::: pf-proof

Attaching a cell by a null-homotopic map yields, up to homotopy, the wedge with the corresponding sphere.

:::

:::

::: pf-step

Therefore
$$\boxed{\pi_3(S^2)\ne0.}$$

::: pf-proof

This is the contrapositive of step [](#s5){.pf-ref}.

:::

:::

:::

:::
