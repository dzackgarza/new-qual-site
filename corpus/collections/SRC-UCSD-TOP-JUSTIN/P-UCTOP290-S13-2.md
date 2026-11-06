---
schema: qual/card@1
id: P-UCTOP290-S13-2
kind: problem
title: Canonical orientation of the orientation double cover
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 13, Problem 2 in its checked-in extraction.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against UCSD Math 290 Fall 2014 problem sheet 13, problem 2
    (assets/attachments/UCSD_290_F14_sheet13.pdf, printed page 389), from the
    checked-in extraction and a 300 dpi render. The printed problem asks to show
    that the orientation double cover M-tilde -> M of any manifold is orientable
    and that it has a canonical orientation. The card states exactly this, so no
    repair was needed.
---

::: {.problem}
Show that the orientation double cover
$\widetilde M\to M$ of a manifold $M$ is orientable.
Show that it has a canonical orientation.
:::

::: {.solution}

Let $M$ be an $n$-manifold and $p\colon\widetilde M\to M$ its orientation
double cover. A point of $\widetilde M$ is a pair $(x,o_x)$ with $x\in M$ and
$o_x$ a local orientation of $M$ at $x$, that is a generator of
$H_n(M,M\setminus\{x\};\ZZ)\cong\ZZ$ at an interior point, and analogously a
generator of the local homology at a boundary point.

::: pf

::: {.pf-step #cover}

$\widetilde M\to M$ is a two-sheeted covering, and over an evenly covered
coordinate ball the two sheets are the two continuous choices of local
orientation.

::: pf-proof

For each point $x$ there are exactly two local orientations $o_x,-o_x$, and a
neighbourhood $U$ of $x$ homeomorphic to $\RR^n$ (or to a half-space) has
exactly two continuous orientations, related by a sign; the preimage of $U$ is
the union of the two corresponding open sets, by the definition of the
topology of $\widetilde M$ as the set of germs of orientations. So $p$ is a
local homeomorphism with two points in each fibre.

:::

:::

::: {.pf-step #orient}

The assignment $(x,o_x)\mapsto o_x$ is a continuous choice of local
orientation on $\widetilde M$, hence an orientation of $\widetilde M$.

::: pf-proof

Fix $(x,o_x)$ and its image $x$. The local orientation of $\widetilde M$ at
$(x,o_x)$ to be used is the one that $p$ carries to $o_x$: $p$ is a local
homeomorphism at $(x,o_x)$ between neighbourhoods of equal dimension, so it
induces an isomorphism $H_n(\widetilde M,\widetilde M\setminus\{(x,o_x)\})\to
H_n(M,M\setminus\{x\})$, and there is a unique generator mapping to $o_x$. On
a sheet over a coordinate ball $U$ this generator is the same at every point,
because that sheet is by definition a continuous choice of orientation on $U$;
so the choice is locally constant in the point, which is the definition of an
orientation.

:::

:::

::: {.pf-step #canonical}

The orientation is canonical, and the deck involution $(x,o_x)\mapsto(x,-o_x)$
reverses it.

::: pf-proof

The construction used only the covering projection and the point $(x,o_x)$,
with no further choice: an orientation of $\widetilde M$ is a continuous
section of the orientation bundle, and this one is the tautological section,
so it is determined by $p$. It makes $p$ orientation-preserving at every
point. The deck transformation sends $(x,o_x)$ to $(x,-o_x)$, and the chosen
local orientation there is the preimage of $-o_x$, which is the negative of
the preimage of $o_x$ under the isomorphism induced by $p$; hence the deck
involution reverses the orientation.

:::

:::

:::


:::
