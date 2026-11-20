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
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The card used the author macro $\mcf$, which is defined in the MathJax tier-1 file but not in the
    pandoc preamble `dzg-macros.sty` that the corpus gate renders with, so the whole-corpus check failed
    with "raw TeX the page cannot show" and the page would have shown the command literally. Every
    occurrence was replaced by the standard `\mathcal{F}`, which is what the macro expands to; no
    mathematics was changed.

- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The whole-corpus check rejected this card twice with "raw TeX the page cannot show": once for the
    author macro $\mcf$, used forty times, which the Pandoc preamble does not define, and once for the
    sentence "has been replaced by \mathcal{F}", where the command stands in plain prose rather than in
    mathematics and so reaches the reader literally. The forty occurrences now read `\mathcal{F}`, and
    that sentence now names the macro inside math. No mathematics was changed.

- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The remark's provenance sentence called `\wait` an undefined control word that "has been
    replaced by the macro this card uses everywhere else, $\mathcal{F}$". `vocabularies/macros.json`
    defines `\wait` as `{-}`, so it is not undefined, and the sentence itself wrote the argument of
    $\Gamma(U,-)$ as a dash rather than as $\mathcal{F}$. The sentence is deleted and the duplicate
    provenance paragraph that commit dfba611652 added beside it is collapsed into one. No mathematics
    was changed.

---

::: {.problem}
For any open subset $U \subseteq X$, show that the functor $\Gamma(U, \mathcal{F})$ from sheaves on $X$ to abelian groups is left exact.
That is, if
$$
0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}''
$$
is an exact sequence of sheaves, then
$$
0 \to \Gamma(U, \mathcal{F}') \to \Gamma(U, \mathcal{F}) \to \Gamma(U, \mathcal{F}'')
$$
is an exact sequence of groups.
:::

::: {.solution}
Let
$$
0\longrightarrow\mathcal{F}'\xrightarrow{i}\mathcal{F}\xrightarrow{p}\mathcal{F}''
$$
be an exact sequence of sheaves on $X$, and fix an open subset $U\subseteq X$.

::: pf

::: {.pf-step #injective-on-sections}
The map
$$
\Gamma(U,\mathcal{F}')\xrightarrow{\Gamma(U,i)}\Gamma(U,\mathcal{F})
$$
is injective.

::: pf-proof
Exactness at $\mathcal{F}'$ says that $i$ is an injective morphism of sheaves.
By definition of injectivity for sheaf morphisms, for every open set $V\subseteq X$ the map
$$
i(V):\mathcal{F}'(V)\longrightarrow\mathcal{F}(V)
$$
is injective.
Taking $V=U$ gives the claim.
:::

:::

::: {.pf-step #kernel-identification}
After identifying $\mathcal{F}'$ with the kernel subsheaf $\ker p\subseteq\mathcal{F}$, one has
$$
\Gamma(U,\mathcal{F}')
=
\ker\bigl(\Gamma(U,\mathcal{F})\to\Gamma(U,\mathcal{F}'')\bigr).
$$

::: pf-proof
Exactness at $\mathcal{F}$ gives
$$
\im i=\ker p.
$$
By [[P-AGH216QUOTSEQ|Exercise II.1.6]], the injection $i$ identifies $\mathcal{F}'$ with the subsheaf $\im i$, hence with $\ker p$.

The kernel sheaf is computed sectionwise:
$$
(\ker p)(U)
=
\ker\bigl(p(U):\mathcal{F}(U)\to\mathcal{F}''(U)\bigr).
$$
Therefore
$$
\Gamma(U,\mathcal{F}')
=\Gamma(U,\ker p)
=\ker\bigl(\Gamma(U,\mathcal{F})\to\Gamma(U,\mathcal{F}'')\bigr).
$$
:::

:::

::: {.pf-step #exact-sequence}
The sequence
$$
\boxed{
0\longrightarrow\Gamma(U,\mathcal{F}')
\longrightarrow\Gamma(U,\mathcal{F})
\longrightarrow\Gamma(U,\mathcal{F}'')}
$$
is exact.

::: pf-proof
Step [](#injective-on-sections){.pf-ref} gives exactness at the first nonzero term.
Step [](#kernel-identification){.pf-ref} identifies the image of the first map with the kernel of the second map, giving exactness at $\Gamma(U,\mathcal{F})$.
This is precisely left exactness of the global-sections functor $\Gamma(U,\mathcal{F})$.
:::

:::

::: pf-qed
Step [](#exact-sequence){.pf-ref} is the required left-exact sequence.
:::

:::

:::

::: {.remark}
The exercise stands on printed p. 66 of Hartshorne, read in `tmp/sources/hartshorne-1977-algebraic-geometry.pdf`, where printed p. $N$ is PDF p. $N+15$; the statement above is that page's text, the left exactness of $\Gamma(X,\cdot)$ on sheaves of abelian groups and the counterexample on presheaves included.

The functor $\Gamma(U, \mathcal{F})$ is not exact in general; Hartshorne II.1.21 supplies a counterexample on $\PP^1$.
:::

::: {.remark title="Published solution"}
Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Chapter II §1, Exercise 1.8, text version `tmp/sources/hartshorne-solutions-kim.md`, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`: he observes that the kernel sheaf of $\mathcal{F}\to\mathcal{F}''$ is the kernel presheaf, so its sections over $U$ are exactly the kernel of $\Gamma(U,\mathcal{F})\to\Gamma(U,\mathcal{F}'')$, and left exactness follows.
The proof above is that identity, together with the injectivity of $\Gamma(U,\mathcal{F}')\to\Gamma(U,\mathcal{F})$ taken from the definition of injectivity for a morphism of sheaves (Hartshorne's Caution 1.2.1).
Agree.
:::
