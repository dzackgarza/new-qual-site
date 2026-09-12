---
schema: qual/card@1
id: P-TOPS23F
kind: problem
title: "Degree pm 1 map from S^n to a closed orientable manifold forces homology isomorphism"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Degree
  - Manifolds
  - Poincaré Duality
relations: []
review: draft
---

::: problem
Let $M^n$ be a path-connected closed orientable manifold such that there exists a map $f : S^n \to M$ of degree $\pm 1$.
Show that $H^*(M; \mathbb{F}) = H^*(S^n; \mathbb{F})$ whenever $\mathbb{F}$ is a field, and hence that $H^*(M; \mathbb{Z}) \cong H^*(S^n; \mathbb{Z})$.
:::

::: {.solution}
<1>1. For every field $\mathbb F$, the degree-$\pm1$ map $f:S^n\to M$ induces an injection
$$f^*:H^k(M;\mathbb F)\hookrightarrow H^k(S^n;\mathbb F).$$
::: {.proof}
If $0\ne\alpha\in H^k(M;\mathbb F)$, Poincaré duality over $\mathbb F$ gives $\beta\in H^{n-k}(M;\mathbb F)$ with $\langle\alpha\smile\beta,[M]_{\mathbb F}\rangle\ne0$. Naturality gives
$$\langle f^*\alpha\smile f^*\beta,[S^n]_{\mathbb F}\rangle
=(\deg f)_{\mathbb F}\langle\alpha\smile\beta,[M]_{\mathbb F}\rangle.$$
Since $\deg f=\pm1$, its image in every field is nonzero, so $f^*\alpha\ne0$.
:::

<1>2. Hence
$$\boxed{H^*(M;\mathbb F)\cong H^*(S^n;\mathbb F)}$$
for every field $\mathbb F$.
::: {.proof}
The sphere has zero cohomology in degrees $0<k<n$, so injectivity forces the same vanishing for $M$. Connectedness and orientability give one-dimensional cohomology in degrees $0,n$.
:::

<1>3. The integral cohomology groups of the closed manifold $M$ are finitely generated. The vanishing in <1>2 for $\mathbb Q$ rules out free summands in intermediate degrees, and the vanishing for every $\mathbb F_p$ rules out torsion there.
::: {.proof}
A nonzero free summand would survive after tensoring with $\mathbb Q$. If a $p$-primary torsion summand occurred in integral cohomology or adjacent integral homology, the universal coefficient theorem with $\mathbb F_p$ coefficients would produce a nonzero intermediate mod-$p$ cohomology group, contradicting <1>2.
:::

<1>4. Therefore
$$\boxed{H^*(M;\mathbb Z)\cong H^*(S^n;\mathbb Z)}$$
as graded abelian groups.
::: {.proof}
Only $H^0\cong H^n\cong\mathbb Z$ remain, with all intermediate groups zero.
:::
:::
