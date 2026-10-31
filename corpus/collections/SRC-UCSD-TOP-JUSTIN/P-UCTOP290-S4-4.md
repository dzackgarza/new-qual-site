---
schema: qual/card@1
id: P-UCTOP290-S4-4
kind: problem
title: Topological group structure on a connected cover
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 4, Problem 4 against the checked-in extraction and PDF page image.
---

::: {.problem}
Let $G$ be a path-connected, locally path-connected topological group,
and let $p:\widetilde G\to G$ be a path-connected covering. Show, using
existence and uniqueness of lifts, that after choosing
$\widetilde e\in p^{-1}(e)$ there is a unique topological group
structure on $\widetilde G$ with identity $\widetilde e$ for which $p$
is a homomorphism.
:::

::: {.solution}

Put
$$
H=p_*\pi_1(\widetilde G,\widetilde e)
\le\pi_1(G,e).
$$
The group $\pi_1(G,e)$ is abelian by
[[P-AMD-SLP2J4M6|the topological-group fundamental-group theorem]].
For the multiplication $m:G\times G\to G$, its induced map on
fundamental groups is addition:
$$
m_*(\alpha,\beta)=\alpha+\beta.
$$
Hence the image of $\pi_1(\widetilde G\times\widetilde G)$ under
$m\circ(p\times p)$ is $H+H=H$. The covering-space lifting criterion
gives a unique continuous lift
$$
\widetilde m:\widetilde G\times\widetilde G\to\widetilde G
$$
that takes $(\widetilde e,\widetilde e)$ to $\widetilde e$.

Inversion $i:G\to G$ acts on $\pi_1(G,e)$ by negation, so
$i_*(H)=H$. It likewise has a unique continuous lift
$\widetilde i:\widetilde G\to\widetilde G$ fixing $\widetilde e$.

The two associative products on $\widetilde G^3$ lift the same
product map to $G$ and agree at
$(\widetilde e,\widetilde e,\widetilde e)$, so uniqueness of lifts
makes them equal. The maps
$\widetilde m(\widetilde e,-)$ and
$\widetilde m(-,\widetilde e)$ lift the identity map of $G$
and fix $\widetilde e$, so both equal
$\operatorname{id}_{\widetilde G}$. The maps
$\widetilde m(-,\widetilde i(-))$ and
$\widetilde m(\widetilde i(-),-)$ lift the constant map with value
$e$ and take $\widetilde e$ to $\widetilde e$, so both are constant
at $\widetilde e$. Thus $\widetilde G$ is a topological group and
$p$ is a homomorphism.

Any other such multiplication and inversion lift the same maps and
agree at the chosen identity. Uniqueness of lifts gives the same
operations.

:::
