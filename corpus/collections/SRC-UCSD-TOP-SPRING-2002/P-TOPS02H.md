---
schema: qual/card@1
id: P-TOPS02H
kind: problem
title: "Degree-one map from S^n to a closed oriented manifold forces homology isomorphism"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Degree
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Let $M$ be an $n$-dimensional compact connected orientable manifold.
Let $[M] \in H_n(M; \ZZ)$ be the fundamental class.
Suppose $f : S^n \to M$ is a continuous function with $f_*([S^n]) = [M]$.
Prove $H_*(S^n; \ZZ) \cong H_*(M; \ZZ)$.
:::

::: {.solution}

::: pf

::: pf-step

The hypothesis says that $f$ has degree $1$.

::: pf-proof

By definition, $f_*[S^n]=\deg(f)[M]$, and the hypothesis gives coefficient $1$.

:::

:::

::: {.pf-step #s2}

For every field $F$, the induced map
$$
f^*:H^k(M;F)\to H^k(S^n;F)
$$
is injective.

::: pf-proof

If $0\ne\alpha\in H^k(M;F)$, Poincaré duality gives $\beta\in H^{n-k}(M;F)$ with $\langle\alpha\smile\beta,[M]\rangle\ne0$. Naturality gives
$$
\langle f^*\alpha\smile f^*\beta,[S^n]\rangle
=\langle\alpha\smile\beta,f_*[S^n]\rangle
=\langle\alpha\smile\beta,[M]\rangle\ne0,
$$
so $f^*\alpha\ne0$.

:::

:::

::: {.pf-step #s3}

Hence $H^k(M;F)=0$ for $0<k<n$ and every field $F$.

::: pf-proof

The target $H^k(S^n;F)$ vanishes in these degrees, so injectivity from step [](#s2){.pf-ref} forces the source to vanish.

:::

:::

::: {.pf-step #s4}

Therefore $H_k(M;\ZZ)=0$ for $0<k<n$.

::: pf-proof

The homology groups of a compact manifold are finitely generated. If some $H_k(M;\ZZ)$ were nonzero in an intermediate degree, then either it had a free summand, detected after tensoring with $\QQ$, or nonzero $p$-torsion, detected with $\FF_p$ coefficients via the universal coefficient theorem. Both contradict step [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

Since $M$ is connected and orientable,
$$
H_0(M;\ZZ)\cong H_n(M;\ZZ)\cong\ZZ.
$$

::: pf-proof

Connectedness gives $H_0\cong\ZZ$, and the fundamental class gives $H_n\cong\ZZ$.

:::

:::

::: pf-step

Thus
$$
\boxed{H_*(M;\ZZ)\cong H_*(S^n;\ZZ).}
$$

::: pf-proof

Combine steps [](#s4){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

:::

:::
