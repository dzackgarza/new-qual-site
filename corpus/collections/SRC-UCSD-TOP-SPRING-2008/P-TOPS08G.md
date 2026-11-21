---
schema: qual/card@1
id: P-TOPS08G
kind: problem
title: 'A degree-one self-map of the torus induces an element of $\SL_2(\ZZ)$ on $H^1$'
classification:
  areas:
  - topology
  topics:
  - Degree
  - Surfaces
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained exam assets/attachments/SP08_290_Topology_Qual.pdf,
    problem 7: for a degree-one self-map of the two-torus, the induced map on
    first cohomology defines an element of SL_2(Z) with respect to the basis
    coming from the product decomposition. The card agrees. The extraction's
    optical character recognition prints the induced map as "J*" in place of
    "f*", which is a rendering artifact of the scan.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    The argument is correct. Choosing a basis of H^1 with alpha cup beta equal to
    the orientation class, the induced map is given by a two by two integer
    matrix, and naturality together with graded commutativity turns the cup
    product of the two images into the determinant of that matrix times the
    orientation class; since the self-map has degree one, the induced map on top
    cohomology is the identity, so the determinant is 1 and the matrix lies in
    SL_2(Z). Nothing was changed.
---

::: {.problem}
Let $T^2 = S^1 \times S^1$ be the $2$-torus.
Let $f : T^2 \to T^2$ be a self-map of degree $1$.
Show that the map $f^* : H^1(T^2, \ZZ) \to H^1(T^2, \ZZ)$ defines an element of $SL_2(\ZZ)$.
Here, we identify $H^1(T^2, \ZZ)$ with $\ZZ \oplus \ZZ$ using the identification $T^2 = S^1 \times S^1$.
:::

::: {.solution}

::: pf

::: pf-step

Let $\alpha,\beta$ be the standard basis of $H^1(T^2;\ZZ)$, chosen so that
$$
\alpha\smile\beta=[T^2]^*\in H^2(T^2;\ZZ).
$$

::: pf-proof

Take the degree-one classes pulled back from the two circle factors with the product orientation.

:::

:::

::: pf-step

Write the matrix of $f^*:H^1(T^2;\ZZ)\to H^1(T^2;\ZZ)$ in this basis as
$$
A=\begin{pmatrix}a&b\\ c&d\end{pmatrix}.
$$
Then
$$
f^*\alpha=a\alpha+c\beta,\qquad f^*\beta=b\alpha+d\beta.
$$

::: pf-proof

This is just the coordinate description of an endomorphism of the free abelian group $H^1(T^2;\ZZ)\cong\ZZ^2$.

:::

:::

::: {.pf-step #s3}

Naturality and graded-commutativity give
$$
f^*(\alpha\smile\beta)=(ad-bc)\,\alpha\smile\beta.
$$

::: pf-proof

Expand
$$
(a\alpha+c\beta)\smile(b\alpha+d\beta).
$$
The squares $\alpha^2$ and $\beta^2$ vanish, while $\beta\smile\alpha=-\alpha\smile\beta$, leaving $(ad-bc)\alpha\smile\beta$.

:::

:::

::: {.pf-step #s4}

Since $\deg f=1$, the induced map on $H^2(T^2;\ZZ)$ is the identity.

::: pf-proof

On the top cohomology of a closed oriented manifold, $f^*$ is multiplication by the degree.

:::

:::

::: pf-step

Thus $\det A=1$, and therefore
$$
\boxed{f^*\restrict_{H^1}\in SL_2(\ZZ).}
$$

::: pf-proof

Compare step [](#s3){.pf-ref} with step [](#s4){.pf-ref}.

:::

:::

:::

:::
