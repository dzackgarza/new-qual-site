---
title: Counterexamples
order: 9
topics:
- Counterexamples
---

# Counterexamples

Each example refutes the statement in its title.

## Point-set

::: {.example title="A compact subset need not be closed"}
In the line with two origins, $[-1,1]$ together with one of the two origins is compact and is not closed, since the other origin lies in its closure.
In a [[D-ZFRV4|Hausdorff space]], every [[D-EILKJ|compact]] subset is closed.

:::

::: {.example title="A closed and bounded set need not be compact"}
The closed unit ball of an infinite-dimensional normed space is closed and bounded, and it is not compact.
By the Heine--Borel theorem, closed and bounded subsets of $\RR^n$ are compact.

:::

::: {.example title="A continuous image of a closed set need not be closed"}
The projection $\RR^2\to\RR$, $(x,y)\mapsto x$, sends the closed hyperbola $\ts{xy=1}$ onto $\RR\sm\ts0$, which is not closed.
Continuous images of compact sets are compact, and continuous images of connected sets are connected.

:::

::: {.example title="A quotient of a Hausdorff space need not be Hausdorff"}
The line with two origins is the quotient of two copies of $\RR$ obtained by identifying $x$ in the first copy with $x$ in the second for every $x\neq 0$.
Each copy of $\RR$ is Hausdorff, and the two origins have no disjoint neighborhoods in the quotient.

:::

::: {.example title="A connected space need not be path connected"}
The topologist's sine curve $\ts{(x,\sin(1/x)) \st 0<x\leq 1}\union \ts{0}\times[-1,1]$ is [[D-YO6NZ|connected]] and not [[D-X73EB|path connected]].
It is also not [[D-GYBZ2|locally connected]].

:::

::: {.example title="A product of connected spaces need not be connected in the box topology"}
$\RR^\omega$ is connected in the product topology and not connected in the box topology: the set of bounded sequences is open and closed in the box topology.
An arbitrary product of connected spaces is connected in the [[D-JKH35|product topology]].

:::

::: {.example title="Completeness is not a topological property"}
$(0,1)$ and $\RR$ with their standard metrics are homeomorphic, $\RR$ is complete, and $(0,1)$ is not.

:::

## Fundamental group and covering spaces

::: {.example title="The fundamental group does not determine the homotopy type"}
$S^1\vee S^2$ and $S^1$ both have fundamental group $\ZZ$, and $H_2(S^1\vee S^2)\cong\ZZ$ while $H_2(S^1)=0$.

:::

::: {.example title="A simply connected space need not be contractible"}
$S^2$ is [[D-GFM35|simply connected]], and $H_2(S^2)\cong\ZZ$ shows that it is not [[D-K43GA|contractible]].

:::

::: {.example title="A space need not have a universal cover"}
The Hawaiian earring is path connected and locally path connected, and it is not [[D-EPQ54|semilocally simply connected]], so it has no [[D-BX3WD|universal cover]].

:::

::: {.remark}
For a path-connected, locally path-connected, semilocally simply connected space $X$ with basepoint $x_0$, conjugacy classes of subgroups of $\pi_1(X,x_0)$ correspond to isomorphism classes of connected [[D-ANO2D|covering spaces]] of $X$.
For the Hawaiian earring the trivial subgroup corresponds to no covering space.

:::

## Homology

::: {.example title="Homology does not determine the homeomorphism type"}
The Poincaré homology sphere has the homology of $S^3$, and its fundamental group is the binary icosahedral group of order $120$, so it is not homeomorphic to $S^3$.

:::

::: {.example title="Homology does not determine the fundamental group"}
For path-connected $X$, $H_1(X)$ is the abelianization of $\pi_1(X)$.
The fundamental group of the Poincaré homology sphere is perfect and nontrivial, so $H_1 = 0$ while $\pi_1\neq 1$.

:::

::: {.example title="A homology isomorphism need not be a homotopy equivalence"}
Collapsing the complement of an open $3$-ball in the Poincaré homology sphere $P$ gives a map $P\to S^3$ of degree $1$, which induces isomorphisms on all homology groups.
It is not a homotopy equivalence, since $\pi_1(P)\neq 1$.
By Whitehead's theorem, a map between simply connected CW complexes inducing isomorphisms on all homology groups is a homotopy equivalence.

:::

::: {.example title="Singular homology does not commute with infinite products"}
Let $X=\prod_{n\geq 1}\ts{0,1}$ be a countable product of two-point discrete spaces, the Cantor set.
Its path components are its points, so $H_0(X)$ is free abelian of uncountable rank, whereas $\prod_{n\geq1} H_0(\ts{0,1}) \cong \prod_{n\geq 1}\ZZ^2$ is not free by the Baer--Specker theorem.

:::

::: {.remark}
For good pointed spaces $X_\alpha$, $\tilde H_*(\bigvee_\alpha X_\alpha)\cong\bigoplus_\alpha \tilde H_*(X_\alpha)$.

:::

## Manifolds

::: {.example title="A closed manifold need not have top homology $\ZZ$"}
For a connected closed $n$-manifold $M$, $H_n(M)\cong\ZZ$ if $M$ is [[D-K5MLW|orientable]] and $H_n(M)=0$ otherwise.
The Klein bottle is non-orientable and has $H_2=0$, while the torus has $H_2\cong\ZZ$.

:::

::: {.example title="A manifold need not be triangulable"}
Every topological manifold of dimension at most $3$ is triangulable.
Freedman's $E_8$ manifold is a closed topological $4$-manifold that admits no triangulation.

:::

::: {.example title="Homotopy equivalent manifolds need not be homeomorphic"}
The lens spaces $L(7,1)$ and $L(7,2)$ are homotopy equivalent closed $3$-manifolds that are not homeomorphic.

:::
