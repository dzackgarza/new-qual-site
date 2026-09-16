---
schema: qual/card@1
id: D-SHFLOCSYS
kind: definition
title: Local systems and monodromy
classification:
  areas:
  - algebraic-geometry
  topics:
  - Local Systems
  - Sheaves
  - Fundamental Group
relations:
- kind: related-to
  target: FE-SHFISOSTALKS
review: draft
prompts:
- What is a local system?
---

::: {.definition title="Locally constant sheaf and local system"}
A sheaf $\mathcal{L}$ of abelian groups on a topological space $X$ is \dfn{locally constant} if every point has an open neighbourhood $U$ with $\mathcal{L}|_U$ isomorphic to a constant sheaf.
A \dfn{local system} is a locally constant sheaf of abelian groups, or of $k$-vector spaces, whose stalks are finitely generated, respectively finite-dimensional.
:::

::: {.theorem title="Monodromy"}
Let $X$ be connected, locally path-connected and semilocally simply connected, with base point $x$.
Taking the stalk at $x$ with its action by parallel transport along loops gives an equivalence between local systems of $k$-vector spaces on $X$ and finite-dimensional representations $\pi_1(X, x) \to \GL(\mathcal{L}_x)$.
The constant local systems correspond to the trivial representations, and $\Gamma(X, \mathcal{L}) = \mathcal{L}_x^{\pi_1(X,x)}$.
:::

::: {.example}
For the double cover $f \colon S^1 \to S^1$, $z \mapsto z^2$, the pushforward $f_* \ul{\QQ}$ is the local system of rank $2$ whose monodromy sends the generator of $\pi_1(S^1) = \ZZ$ to the swap of the two coordinates of $\QQ^2$.
It decomposes as the constant local system $\ul{\QQ}$ plus the rank-one local system with monodromy $-1$, which has no nonzero global sections.
:::
