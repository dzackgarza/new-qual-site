---
schema: qual/card@1
id: P-UCTOP-SU11-6
kind: problem
title: Space with free fundamental group and no higher homotopy is a bouquet of circles
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
---

For any topological space $X$, let $X$ be a path-connected space with $\pi_{\geq 2}(X) = 0$ and whose fundamental group is a free group on a set $S$.
Show that there is a homotopy equivalence between a bouquet of circles, indexed by $S$, and $X$.

::: {.solution}
<1>1. As printed for an arbitrary topological space, the statement is false.
::: {.proof}
Take the basis set $S=\varnothing$. Then the free group on $S$ is trivial and the bouquet indexed by $S$ is a point. The Warsaw circle $W$ is a standard path-connected weakly contractible but noncontractible compact space: all of its homotopy groups vanish, but $W$ is not homotopy equivalent to a point. Thus $W$ satisfies the printed homotopy-group hypotheses with $S=\varnothing$ but not the asserted conclusion. This is exactly the failure of Whitehead's theorem outside spaces of CW type.
:::

<1>2. The intended statement is correct if $X$ is a CW complex (more generally, if $X$ has the homotopy type of a CW complex).
::: {.proof}
Assume first that $X$ is a CW complex. Let
$$B=\bigvee_{s\in S}S^1_s.$$
Choose for each free generator $s\in\pi_1(X)$ a based loop $\gamma_s:S^1\to X$, and let
$$f:B\to X$$
be the map whose restriction to the $s$-th circle is $\gamma_s$.
:::

<1>3. The map $f$ induces an isomorphism on every homotopy group.
::: {.proof}
By construction,
$$f_*:\pi_1(B)\cong F(S)\longrightarrow\pi_1(X)\cong F(S)$$
is the isomorphism sending each standard free generator to the chosen generator with the same name. The universal cover of a graph is a tree, so $\pi_n(B)=0$ for every $n\ge2$. These groups agree with the assumed groups $\pi_n(X)=0$ for $n\ge2$. Both spaces are path connected, so $f$ is a weak homotopy equivalence.
:::

<1>4. Therefore
$$\boxed{X\simeq\bigvee_{s\in S}S^1}$$
under the CW-type hypothesis.
::: {.proof}
Both $B$ and $X$ are CW complexes, so Whitehead's theorem upgrades the weak homotopy equivalence $f$ from <1>3 to a homotopy equivalence. If $X$ merely has CW type, replace it by a homotopy-equivalent CW complex and apply the same argument.
:::
:::
