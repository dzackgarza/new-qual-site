---
schema: qual/card@1
id: D-SHFCONSTR
kind: definition
title: Constructible sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Constructible Sheaves
  - Local Systems
  - Stratifications
relations:
- kind: uses
  target: D-SHFLOCSYS
review: draft
prompts:
- What is a constructible sheaf?
- What is a constructible $\ell$-adic sheaf on the étale site?
---

::: {.definition title="Constructible sheaf"}
Let $X$ be a complex algebraic variety with its analytic topology.
A sheaf $\mathcal{F}$ of $k$-vector spaces on $X$ is \dfn{constructible} if there is a finite partition $X = \coprod_i X_i$ into Zariski locally closed subvarieties such that each restriction $\mathcal{F}\restrict_{X_i}$ is a local system.
:::

::: {.remark}
The same definition with the Zariski or étale topology on a Noetherian scheme, and locally constant sheaves with finite stalks in place of local systems, gives constructible étale sheaves.
Constructible sheaves are preserved by $f^{-1}$, by $f_*$ and $f_!$ for morphisms of varieties, and by $\otimes$ and $\mathcal{H}om$, in the derived sense: for a morphism of complex varieties, the six operations ([[D-SHFSIX]]) carry bounded complexes with constructible cohomology sheaves to bounded complexes with constructible cohomology sheaves.
:::

::: {.definition title="Constructible $\ell$-adic sheaf"}
Let $X$ be a scheme on which the prime $\ell$ is invertible. A \dfn{constructible $\ell$-adic sheaf} on $X_{\acute{e}tale}$ is an inverse system
$$
\mcf=(\mcf_n)_{n\geq1}
$$
such that each $\mcf_n$ is a constructible sheaf of $\ZZ/\ell^n\ZZ$-modules and the transition maps induce isomorphisms
$$
\mcf_{n+1}\tensor_{\ZZ/\ell^{n+1}\ZZ}\ZZ/\ell^n\ZZ
\xrightarrow{\sim}
\mcf_n.
$$
The associated $\QQ_\ell$-sheaves are obtained from the corresponding adic systems by inverting $\ell$.
:::

::: {.example}
Let $j \colon U = \AA^1 \setminus \{0\} \hookrightarrow \AA^1$ and $i \colon \{0\} \hookrightarrow \AA^1$ over $\CC$.
The sheaf $j_! \underline{\CC}_U$ has stalk $\CC$ on $U$ and $0$ at $0$, and $i_* \CC$ has stalk $\CC$ at $0$ and $0$ elsewhere.
Both are constructible with respect to the partition $\AA^1 = U \amalg \{0\}$, and neither is a local system on $\AA^1$.
:::
