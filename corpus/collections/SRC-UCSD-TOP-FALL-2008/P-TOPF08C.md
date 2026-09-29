---
schema: qual/card@1
id: P-TOPF08C
kind: problem
title: "No degree pm 1 map from CP^n to S^{n+1} x S^{n-1} for n > 1"
classification:
  areas:
  - topology
  topics:
  - Degree
  - Projective Spaces
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Can there exist a map $f$ of degree $\pm 1$ of the form:
$$
f : \mathbb{CP}^n \to S^{n+1} \times S^{n-1}, \quad n > 1.
$$
Prove your answer.
:::

::: {.solution}

::: pf

::: pf-step

Assume for contradiction that
$$
f:\mathbb{CP}^n\to S^{n+1}\times S^{n-1}
$$
has degree $\pm1$.

::: pf-proof

We derive a contradiction from the induced cohomology map.

:::

:::

::: {.pf-step #s2}

A degree-$\pm1$ map between closed oriented manifolds induces an injection on integral cohomology.

::: pf-proof

If $0\ne\alpha\in H^k(N;\mathbb Z)$, Poincaré duality gives $\beta$ with $\langle\alpha\smile\beta,[N]\rangle\ne0$. Naturality then gives
$$
\langle f^*\alpha\smile f^*\beta,[M]\rangle
=\pm\langle\alpha\smile\beta,[N]\rangle\ne0,
$$
so $f^*\alpha\ne0$.

:::

:::

::: {.pf-step #s3}

If $n$ is even, the target has a nonzero class in odd degree $n-1$, but
$$
H^{n-1}(\mathbb{CP}^n;\mathbb Z)=0,
$$
contradicting step [](#s2){.pf-ref}.

::: pf-proof

The class pulled back from $S^{n-1}$ generates $H^{n-1}$ of the product, while $\mathbb{CP}^n$ has cohomology only in even degrees.

:::

:::

::: {.pf-step #s4}

Suppose $n$ is odd. Let $x\in H^{n-1}(S^{n+1}\times S^{n-1})$ be the generator from the $S^{n-1}$ factor. Then $x^2=0$.

::: pf-proof

The class $x$ is pulled back from $S^{n-1}$, whose cohomology vanishes in degree $2n-2>n-1$.

:::

:::

::: {.pf-step #s5}

Injectivity forces
$$
f^*x=k\,u^{(n-1)/2}
$$
for some nonzero integer $k$, where $u\in H^2(\mathbb{CP}^n)$ is the standard generator. But then
$$
(f^*x)^2=k^2u^{n-1}\ne0.
$$

::: pf-proof

We have $H^*(\mathbb{CP}^n;\mathbb Z)=\mathbb Z[u]/(u^{n+1})$. Since $n>1$, the power $u^{n-1}$ is nonzero. The coefficient $k$ is nonzero by injectivity from step [](#s2){.pf-ref}.

:::

:::

::: pf-step

This contradicts
$$
(f^*x)^2=f^*(x^2)=0.
$$
Therefore no such degree-$\pm1$ map exists for any $n>1$.

::: pf-proof

Combine step [](#s3){.pf-ref} for even $n$ and steps [](#s4){.pf-ref} and [](#s5){.pf-ref} for odd $n$.

:::

:::

:::

:::
