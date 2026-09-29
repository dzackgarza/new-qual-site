---
schema: qual/card@1
id: P-TOPF20F
kind: problem
title: "A map of nonzero degree induces injection on rational cohomology"
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Degree
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Let $M, N$ be two connected, closed, oriented $n$-dimensional manifolds ($n \geq 1$). Consider a continuous map $f : M \to N$ that has nonzero mapping degree.
Show that the induced map $f^* : H^k(N; \mathbb{Q}) \to H^k(M; \mathbb{Q})$ is injective for any $k$.
:::

::: {.solution}

::: pf

::: pf-step

Fix a degree $k$ and a nonzero class $0\ne\alpha\in H^k(N;F)$.

::: pf-proof

It suffices to prove that $f^*(\alpha)\ne0$ for every nonzero homogeneous class; injectivity of the total graded map then follows degree by degree.

:::

:::

::: pf-step

By Poincaré duality over the field $F$, there is a class $\beta\in H^{n-k}(N;F)$ such that
$$
\langle \alpha\smile\beta,[N]_F\rangle\ne0.
$$

::: pf-proof

For a closed connected oriented $n$-manifold, the cup-product pairing
$$
H^k(N;F)\times H^{n-k}(N;F)\longrightarrow F,
\qquad (u,v)\longmapsto\langle u\smile v,[N]_F\rangle
$$
is nondegenerate.

:::

:::

::: {.pf-step #s3}

Naturality of cup product and the definition of degree give
$$
\begin{aligned}
\langle f^*\alpha\smile f^*\beta,[M]_F\rangle
&=\langle f^*(\alpha\smile\beta),[M]_F\rangle\\
&=\langle \alpha\smile\beta,f_*[M]_F\rangle\\
&=(\deg f)_F\,\langle \alpha\smile\beta,[N]_F\rangle,
\end{aligned}
$$
where $(\deg f)_F$ is the image of the integer $\deg f$ in $F$.

::: pf-proof

The first equality is naturality of the cup product, the second is naturality of the Kronecker pairing, and $f_*[M]=\deg(f)[N]$ by definition of the degree.

:::

:::

::: pf-step

Consequently the stated claim is valid over $F$ provided $(\deg f)_F\ne0$.

::: pf-proof

Under this condition, both factors on the right-hand side of step [](#s3){.pf-ref} are nonzero, so the displayed pairing is nonzero. Hence $f^*\alpha\ne0$.

:::

:::

::: pf-step

As written, however, the assertion “for any field $F$” is false when the characteristic of $F$ divides $\deg f$.

::: pf-proof

Take the degree-$p$ map $f:S^1\to S^1$, $z\mapsto z^p$, and $F=\mathbb F_p$. Then $\deg f=p\ne0$ as an integer, but
$$
f^*:H^1(S^1;\mathbb F_p)\longrightarrow H^1(S^1;\mathbb F_p)
$$
is multiplication by $p=0$ in $\mathbb F_p$, hence is the zero map and is not injective. Thus the correct hypothesis is that $\operatorname{char}F$ does not divide $\deg f$ (in particular, any field works when $\deg f=\pm1$).

:::

:::

:::

:::
