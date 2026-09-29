---
schema: qual/card@1
id: P-AGH34DUPLEISO
kind: problem
title: The $d$-uple embedding is an isomorphism onto its image
classification:
  areas:
  - algebraic-geometry
  topics:
  - Veronese Embedding
  - Morphisms
  - Isomorphism
relations:
- kind: uses
  target: P-AGH212DUPLE
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the statement with Hartshorne I.3.4 and its reference to I.2.12. The inverse is written on the pure-power charts using the coordinates corresponding to x_i^{d-1}x_j.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked the chart cover, regularity, overlap agreement, and both inverse identities against independent published solutions.'
---

::: {.problem}
Show that the $d$-uple embedding of $\PP^n$ is an isomorphism onto its image.
:::

::: {.solution}
Let
$$
\rho_d:\PP^n\longrightarrow\PP^N
$$
be the $d$-uple embedding from [[P-AGH212DUPLE]], and let $Y=\rho_d(\PP^n)$.
For $0\le i,j\le n$, write $y_{ij}$ for the homogeneous coordinate of $\PP^N$ corresponding to the monomial $x_i^{d-1}x_j$; in particular $y_{ii}$ corresponds to $x_i^d$.

::: pf

::: pf-step

The open subsets
$$
U_i=Y\cap D_+(y_{ii})
$$
cover $Y$.

::: pf-proof

Every point of $Y$ has the form $\rho_d([a_0:\cdots:a_n])$.
Some $a_i$ is nonzero, and then its $y_{ii}$-coordinate is $a_i^d\ne0$.
Thus the point lies in $U_i$.

:::

:::

::: pf-step

On $U_i$, the formula
$$
\psi_i([y])=[y_{i0}:\cdots:y_{in}]
$$
defines a morphism $\psi_i:U_i\to\PP^n$.

::: pf-proof

On $U_i$ the coordinate $y_{ii}$ is nonzero, so the displayed homogeneous coordinates are not all zero.
On the affine target chart where the $i$th coordinate is nonzero, the coordinate ratios of $\psi_i$ are
$$
\frac{y_{ij}}{y_{ii}},
$$
which are regular functions on $D_+(y_{ii})$.
Hence $\psi_i$ is a morphism.

:::

:::

::: {.pf-step #s3}

The maps $\psi_i$ are the restrictions of one inverse morphism $\psi:Y\to\PP^n$.

::: pf-proof

Let $[a]=[a_0:\cdots:a_n]$ with $a_i\ne0$.
For $y=\rho_d([a])$, the defining coordinates satisfy
$$
y_{ij}=a_i^{d-1}a_j,
$$
and therefore
$$
\psi_i(y)
=[a_i^{d-1}a_0:\cdots:a_i^{d-1}a_n]
=[a_0:\cdots:a_n].
$$
Thus each $\psi_i$ is the set-theoretic inverse of $\rho_d$ on $U_i$.
In particular the $\psi_i$ agree on overlaps $U_i\cap U_j$, so they glue to a morphism $\psi:Y\to\PP^n$.
The same computation gives $\psi\circ\rho_d=\operatorname{id}_{\PP^n}$ and $\rho_d\circ\psi=\operatorname{id}_Y$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} exhibits a morphism inverse to $\rho_d$, so the $d$-uple embedding is an isomorphism onto its image.

:::

:::

:::
