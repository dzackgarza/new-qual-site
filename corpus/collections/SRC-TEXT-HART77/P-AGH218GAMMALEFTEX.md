---
schema: qual/card@1
id: P-AGH218GAMMALEFTEX
kind: problem
title: The global sections functor is left exact
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Exact Sequences
  - Global Sections
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise II.1.8 and the preceding definitions of exactness and kernel sheaf in Hartshorne II.1. The proof identifies the first sheaf with the kernel subsheaf and then takes sections, where kernels are computed objectwise.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
For any open subset $U \subseteq X$, show that the functor $\Gamma(U, \wait)$ from sheaves on $X$ to abelian groups is left exact.
That is, if
\[
0 \to \mcf' \to \mcf \to \mcf''
\]
is an exact sequence of sheaves, then
\[
0 \to \Gamma(U, \mcf') \to \Gamma(U, \mcf) \to \Gamma(U, \mcf'')
\]
is an exact sequence of groups.
:::

::: {.solution}
Let
$$
0\longrightarrow\mcf'\xrightarrow{i}\mcf\xrightarrow{p}\mcf''
$$
be an exact sequence of sheaves on $X$, and fix an open subset $U\subseteq X$.

<1>1. The map
$$
\Gamma(U,\mcf')\xrightarrow{\Gamma(U,i)}\Gamma(U,\mcf)
$$
is injective.

::: {.proof}
Exactness at $\mcf'$ says that $i$ is an injective morphism of sheaves.
By definition of injectivity for sheaf morphisms, for every open set $V\subseteq X$ the map
$$
i(V):\mcf'(V)\longrightarrow\mcf(V)
$$
is injective.
Taking $V=U$ gives the claim.
:::

<1>2. After identifying $\mcf'$ with the kernel subsheaf $\ker p\subseteq\mcf$, one has
$$
\Gamma(U,\mcf')
=
\ker\bigl(\Gamma(U,\mcf)\to\Gamma(U,\mcf'')\bigr).
$$

::: {.proof}
Exactness at $\mcf$ gives
$$
\operatorname{im}i=\ker p.
$$
By [[P-AGH216QUOTSEQ|Exercise II.1.6]], the injection $i$ identifies $\mcf'$ with the subsheaf $\operatorname{im}i$, hence with $\ker p$.

The kernel sheaf is computed sectionwise:
$$
(\ker p)(U)
=
\ker\bigl(p(U):\mcf(U)\to\mcf''(U)\bigr).
$$
Therefore
$$
\Gamma(U,\mcf')
=\Gamma(U,\ker p)
=\ker\bigl(\Gamma(U,\mcf)\to\Gamma(U,\mcf'')\bigr).
$$
:::

<1>3. The sequence
$$
\boxed{
0\longrightarrow\Gamma(U,\mcf')
\longrightarrow\Gamma(U,\mcf)
\longrightarrow\Gamma(U,\mcf'')}
$$
is exact.

::: {.proof}
Step <1>1 gives exactness at the first nonzero term.
Step <1>2 identifies the image of the first map with the kernel of the second map, giving exactness at $\Gamma(U,\mcf)$.
This is precisely left exactness of the global-sections functor $\Gamma(U,\wait)$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required left-exact sequence.
:::
:::

::: {.remark}
The functor $\Gamma(U, \wait)$ is not exact in general; Hartshorne II.1.21 supplies a counterexample on $\PP^1$.
:::
