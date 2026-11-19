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
with restriction the identity or zero map as the open sets contain $p$ [@Har77, Exercise II.1.17, p. 68].
Equivalently $i_p(A)=(i_p)_*A$, the direct image of the constant sheaf on the one-point space $\theset{p}$.
:::

::: {.proposition}
The stalk of $i_p(A)$ is $A$ at $p$ and $0$ at every other point, so a skyscraper sheaf is determined by one group at one point.
It is flabby, since every open set containing $p$ restricts to an isomorphism on sections of $A$; hence it is $\Gamma$-acyclic and $H^i(X,i_p(A))=0$ for $i>0$ ([[D-COHFLQ]]).
On an affine scheme, the skyscraper at a closed point is the quasicoherent sheaf attached to $A/\mfm$ with $A=k(p)$, and its support is that point ([[D-UDIVH]], [[D-QNTZY]]).
:::
