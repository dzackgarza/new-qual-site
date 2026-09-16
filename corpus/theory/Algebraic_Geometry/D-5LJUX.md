---
schema: qual/card@1
id: D-5LJUX
kind: definition
title: Dimension of a variety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dimension
  - Varieties
relations:
- kind: uses
  target: D-9DIKB
review: draft
prompts:
- What is the dimension of a variety?
- How does dimension relate to the function field?
- How does dimension relate to Krull dimension of the coordinate ring?
---

::: {.definition title="Dimension"}
The \dfn{dimension} of a topological space is the supremum of the lengths $n$ of chains
\[
Z_0 \subsetneq Z_1 \subsetneq \cdots \subsetneq Z_n
\]
of irreducible closed subsets.
:::

::: {.proposition}
If $Y \subseteq \AA^n$ is an affine algebraic set, then $\dim Y = \krulldim A(Y)$.
[@Har10a, Proposition I.1.7]
:::

::: {.theorem}
Let $k$ be any field and $B$ a finitely generated $k$-algebra that is a domain.
Then $\krulldim B = \trdeg_k \Frac B$.
[@Har10a, Theorem I.1.8A]
:::

::: {.proposition}
If $Y$ is a quasi-affine variety, then $\dim Y = \dim \closure{Y}$, where $\closure{Y}$ is the closure of $Y$ in $\AA^n$.
[@Har10a, Proposition I.1.10]
:::

::: {.remark}
Hence for an affine variety $X$ over $k$,
\[
\dim X = \krulldim A(X) = \trdeg_k k(X) ,
\]
and in particular $\dim \AA^n = n$ [@Har10a, Proposition I.1.9].
A computation usually wants the last description: the dimension of $V(f) \subseteq \AA^n$ for $f$ nonconstant is $n-1$ because one algebraic relation drops the transcendence degree by one.
:::
