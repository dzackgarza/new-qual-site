---
schema: qual/card@1
id: P-TOPS08G
kind: problem
title: "A degree-one self-map of the torus induces an SL(2,Z) action on H_1"
classification:
  areas:
  - topology
  topics:
  - Degree
  - Surfaces
  - Linear Algebra
relations: []
review: draft
---

::: problem
Let $T^2 = S^1 \times S^1$ be the $2$-torus.
Let $f : T^2 \to T^2$ be a self-map of degree $1$.
Show that the map $f^* : H^1(T^2, \mathbb{Z}) \to H^1(T^2, \mathbb{Z})$ defines an element of $SL_2(\mathbb{Z})$.
Here, we identify $H^1(T^2, \mathbb{Z})$ with $\mathbb{Z} \oplus \mathbb{Z}$ using the identification $T^2 = S^1 \times S^1$.
:::

::: {.solution}
<1>1. Let $\alpha,\beta$ be the standard basis of $H^1(T^2;\mathbb Z)$, chosen so that
$$
\alpha\smile\beta=[T^2]^*\in H^2(T^2;\mathbb Z).
$$
::: {.proof}
Take the degree-one classes pulled back from the two circle factors with the product orientation.
:::

<1>2. Write the matrix of $f^*:H^1(T^2;\mathbb Z)\to H^1(T^2;\mathbb Z)$ in this basis as
$$
A=\begin{pmatrix}a&b\\ c&d\end{pmatrix}.
$$
Then
$$
f^*\alpha=a\alpha+c\beta,\qquad f^*\beta=b\alpha+d\beta.
$$
::: {.proof}
This is just the coordinate description of an endomorphism of the free abelian group $H^1(T^2;\mathbb Z)\cong\mathbb Z^2$.
:::

<1>3. Naturality and graded-commutativity give
$$
f^*(\alpha\smile\beta)=(ad-bc)\,\alpha\smile\beta.
$$
::: {.proof}
Expand
$$
(a\alpha+c\beta)\smile(b\alpha+d\beta).
$$
The squares $\alpha^2$ and $\beta^2$ vanish, while $\beta\smile\alpha=-\alpha\smile\beta$, leaving $(ad-bc)\alpha\smile\beta$.
:::

<1>4. Since $\deg f=1$, the induced map on $H^2(T^2;\mathbb Z)$ is the identity.
::: {.proof}
On the top cohomology of a closed oriented manifold, $f^*$ is multiplication by the degree.
:::

<1>5. Thus $\det A=1$, and therefore
$$
\boxed{f^*|_{H^1}\in SL_2(\mathbb Z).}
$$
::: {.proof}
Compare <1>3 with <1>4.
:::
:::
