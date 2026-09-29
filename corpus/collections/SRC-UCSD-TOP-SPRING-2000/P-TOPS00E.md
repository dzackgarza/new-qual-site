---
schema: qual/card@1
id: P-TOPS00E
kind: problem
title: "Any continuous map from S^2 x S^2 to CP^2 has even degree"
classification:
  areas:
  - topology
  topics:
  - Degree
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Prove that any continuous map $f : S^2 \times S^2 \to \mathbb{CP}^2$ has even degree.
:::

::: {.solution}

::: pf

::: pf-step

Let $x\in H^2(\mathbb{CP}^2;\mathbb Z)$ be the standard generator, normalized by
$$
\langle x^2,[\mathbb{CP}^2]\rangle=1.
$$

::: pf-proof

The integral cohomology ring is $\mathbb Z[x]/(x^3)$ with $|x|=2$.

:::

:::

::: {.pf-step #s2}

If $a,b$ are the degree-two generators pulled back from the two factors of $S^2\times S^2$, then
$$
a^2=b^2=0,\qquad \langle ab,[S^2\times S^2]\rangle=1.
$$

::: pf-proof

This is the product cohomology ring of two $2$-spheres.

:::

:::

::: pf-step

Write
$$
f^*x=ra+sb
$$
for integers $r,s$.

::: pf-proof

$H^2(S^2\times S^2;\mathbb Z)\cong\mathbb Z a\oplus\mathbb Z b$.

:::

:::

::: {.pf-step #s4}

Then
$$
f^*(x^2)=(ra+sb)^2=2rs\,ab.
$$

::: pf-proof

Use graded commutativity and $a^2=b^2=0$ from step [](#s2){.pf-ref}; since both classes have even degree, $ab=ba$.

:::

:::

::: pf-step

Therefore
$$
\deg f=2rs,
$$
so every such map has even degree.

::: pf-proof

Evaluate step [](#s4){.pf-ref} on $[S^2\times S^2]$:
$$
\langle f^*(x^2),[S^2\times S^2]\rangle
=\deg(f)\langle x^2,[\mathbb{CP}^2]\rangle.
$$
The left side is $2rs$ and the final factor on the right is $1$.

:::

:::

:::

:::
