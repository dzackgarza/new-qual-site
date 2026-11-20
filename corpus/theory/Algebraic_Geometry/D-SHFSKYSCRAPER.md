---
schema: qual/card@1
id: D-SHFSKYSCRAPER
kind: definition
title: The skyscraper sheaf at a point
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Examples
  - Cohomology
relations:
- kind: uses
  target: D-COHFLQ
- kind: related-to
  target: D-UDIVH
review: draft
prompts:
- What is the skyscraper sheaf at a point?
- What are the stalks of a skyscraper sheaf?
- Why is a skyscraper sheaf acyclic?
---

::: {.definition title="skyscraper sheaf"}
Let $X$ be a topological space, $p\in X$ a point, and $A$ an abelian group.
The \dfn{skyscraper sheaf} $i_p(A)$ at $p$ with value $A$ is the sheaf with
$$
i_p(A)(U)=\begin{cases} A & p\in U,\\ 0 & p\notin U,\end{cases}
$$
with restriction the identity or zero map as the open sets contain $p$ [@Har77, Exercise II.1.17].
Equivalently $i_p(A)=i_*A$, where $i\colon \closure{\theset{p}}\injects X$ is the inclusion of the closure of $\theset{p}$ and $A$ is the constant sheaf on that closed subspace.
:::

::: {.proposition}
The stalk of $i_p(A)$ is $A$ at every point of the closure $\closure{\theset{p}}$ and $0$ at every other point, so a skyscraper sheaf is carried by the closed set $\closure{\theset{p}}$ and is determined by one group there.
The identification of stalks is the colimit over the opens containing the point: at $q\in\closure{\theset{p}}$ every neighbourhood of $q$ meets $\theset{p}$, while at $q\notin\closure{\theset{p}}$ the complement of $\closure{\theset{p}}$ is a neighbourhood on which every section is zero.

The sheaf is flabby: for $V\subseteq U$ the restriction $i_p(A)(U)\to i_p(A)(V)$ is the identity $A\to A$ when $p\in V$, the zero map $A\to 0$ when $p\in U\sm V$, and $0\to 0$ when $p\notin U$, so it is surjective in every case.
By the acyclicity of flasque sheaves it is therefore $\Gamma$-acyclic, and $H^i(X,i_p(A))=0$ for $i>0$ ([[D-COHFLQ]]).

On an affine scheme $\Spec R$ the skyscraper at a closed point $p$, with $\mfm_p$ the corresponding maximal ideal, is the quasicoherent sheaf $\widetilde{R/\mfm_p}$, whose stalk at $p$ is the residue field $k(p)=R_{\mfm_p}/\mfm_pR_{\mfm_p}$, and whose support is $\theset{p}$ ([[D-UDIVH]], [[D-QNTZY]]).
:::
