---
schema: qual/card@1
id: P-UCTOP290-S6-4
kind: problem
title: First singular homology is the abelianized fundamental group
classification:
  areas:
  - topology
  topics:
  - Singular Homology
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 6, Problem 4 in its checked-in extraction and page image; its part (d) can only assert injectivity after abelianization.
---

::: {.problem}
For a path-connected space $X$ with basepoint $x_0$,
show that sending a based loop to its singular
one-cycle induces an isomorphism
$$
\pi_1(X,x_0)/[\pi_1(X,x_0),\pi_1(X,x_0)]
\cong H_1(X;\ZZ).
$$
:::

::: {.solution}

Concatenation of loops is homologous to addition
of their singular one-cycles, so the map
$h:\pi_1(X,x_0)\to H_1(X;\ZZ)$ is a
homomorphism and kills commutators.

Write $G=\pi_1(X,x_0)$. For every point $x$ that occurs as a vertex of
a singular simplex under consideration, choose
a path $p_x$ from $x_0$ to $x$, with $p_{x_0}$
constant. For a singular one-simplex
$\sigma:x\to y$, define
$$
\Phi(\sigma)=[p_x\cdot\sigma\cdot p_y^{-1}]
\quad\text{in }G/[G,G].
$$
Extend $\Phi$ linearly to one-chains. The
oriented boundary of each singular two-simplex
maps to zero: its three edge paths form the
boundary of a triangle, and the inserted
$p_x$ paths cancel in the abelian group.
Thus $\Phi$ induces a map from $H_1(X;\ZZ)$
to $G/[G,G]$.

For a based loop $\alpha$, $\Phi(h([\alpha]))$
is $[\alpha]$. Conversely, if
$z=\sum n_\sigma\sigma$ is a one-cycle, the
chain representing $h(\Phi([z]))$ is homologous
to
$$
\sum n_\sigma
(\,p_{\sigma(0)}+\sigma-p_{\sigma(1)}\,).
$$
The path terms cancel because $\partial z=0$,
leaving $z$. Hence $h$ and $\Phi$ induce
inverse maps.
:::

::: {.remark}
The source's final instruction says that $h$
is injective. For a nonabelian fundamental group
this is false: commutators lie in its kernel.
The induced map from the abelianization is
injective.
:::
