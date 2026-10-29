---
schema: qual/card@1
id: P-TOPS23F
kind: problem
title: 'A map of degree $\pm1$ from $S^n$ to a closed orientable manifold forces a homology isomorphism'
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

::: {.problem}
Let $M^n$ be a path-connected closed orientable manifold such that there exists a map $f : S^n \to M$ of degree $\pm 1$.
Show that $H^*(M; \FF) = H^*(S^n; \FF)$ whenever $\FF$ is a field, and hence that $H^*(M; \ZZ) \cong H^*(S^n; \ZZ)$.
:::

::: {.solution}

::: pf

::: pf-step
For every field $\FF$, the degree-$\pm1$ map $f:S^n\to M$ induces an injection
$$f^*:H^k(M;\FF)\hookrightarrow H^k(S^n;\FF).$$

::: pf-proof
If $0\ne\alpha\in H^k(M;\FF)$, Poincaré duality over $\FF$ gives $\beta\in H^{n-k}(M;\FF)$ with $\langle\alpha\smile\beta,[M]_{\FF}\rangle\ne0$. Naturality gives
$$\langle f^*\alpha\smile f^*\beta,[S^n]_{\FF}\rangle
=(\deg f)_{\FF}\langle\alpha\smile\beta,[M]_{\FF}\rangle.$$
Since $\deg f=\pm1$, its image in every field is nonzero, so $f^*\alpha\ne0$.
:::

:::

::: {.pf-step #field-cohomology-iso}
Hence
$$\boxed{H^*(M;\FF)\cong H^*(S^n;\FF)}$$
for every field $\FF$.

::: pf-proof
The sphere has zero cohomology in degrees $0<k<n$, so injectivity forces the same vanishing for $M$. Connectedness and orientability give one-dimensional cohomology in degrees $0,n$.
:::

:::

::: pf-step
The integral cohomology groups of the closed manifold $M$ are finitely generated. The vanishing in step [](#field-cohomology-iso){.pf-ref} for $\QQ$ rules out free summands in intermediate degrees, and the vanishing for every $\FF_p$ rules out torsion there.

::: pf-proof
A nonzero free summand would survive after tensoring with $\QQ$. If a $p$-primary torsion summand occurred in integral cohomology or adjacent integral homology, the universal coefficient theorem with $\FF_p$ coefficients would produce a nonzero intermediate mod-$p$ cohomology group, contradicting step [](#field-cohomology-iso){.pf-ref}.
:::

:::

::: pf-step
Therefore
$$\boxed{H^*(M;\ZZ)\cong H^*(S^n;\ZZ)}$$
as graded abelian groups.

::: pf-proof
Only $H^0\cong H^n\cong\ZZ$ remain, with all intermediate groups zero.
:::

:::

:::

:::
