---
schema: qual/card@1
id: E-HAT-3.3-19
kind: problem
title: Countability of homology of open subsets of $\RR^n$
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 19; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 19; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both parts: a countable disjoint union modulo a relation is countable, and an open set in
    $\RR^n$ is exhausted by finite subcomplexes so that chains and homology are the direct limits
    of the compact stages.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170's continuation, §3.3. Read against Hatcher, Exercise 19 of §3.3, printed p. 259, and
    the printed page is added, the card having had none. Checked: the direct limit over a countable
    index set of countable groups is a quotient of the countable disjoint union, hence countable; and
    for $X\subset\RR^n$ open an exhaustion $K_1\subset\operatorname{int}K_2\subset\cdots$ by finite
    cubical polyhedra, so that every compact subset — in particular every singular simplex and every
    finite chain — lies in a stage; then $C_*(X)=\varinjlim C_*(K_j)$ and Exercise 17 (card
    `E-HAT-3.3-17`) gives $H_i(X)=\varinjlim H_i(K_j)$, a direct limit of finitely generated, hence
    countable, groups over a countable set. No defect. The exhaustion's existence is stated rather
    than proved on the card, as a standard cubulation argument.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Converted from prose to numbered steps under #2. No retained solution set covers §3.3 Exercise
    19 (Sam's §3.3 has 8, 17 and 32; Stanford 215C has 9-11, 21, 22 and 24; Kottke is 3.3.21), so
    the argument is the card's own and the card says so. Two things the prose left as an assertion
    are now proved: the exhaustion by finite subcomplexes is built from the dyadic cubical grids,
    so that a compact set lies in one stage and a stage lies in the next, and the countability of
    each $H_i(K_j;\ZZ)$ is the finite generation of the cellular chains of a finite complex. The
    direct limit is cited as §3.3 Exercise 17, which is the exercise stating that homology commutes
    with direct limits. Not checked: no certificate, and the case $n=0$ is not separated.

---
::: {.solution}
No retained solution set covers §3.3 Exercise 19, so the argument is the card's own. It has two parts: a set-theoretic lemma about direct limits, and the exhaustion of an open subset of $\RR^n$ by finite complexes, which is where the countability of the indexing set comes from.

::: pf

::: {.pf-step #limit-countable}
If the indexing set $A$ of a directed system of abelian groups is countable and every $G_\alpha$ is countable, then $\varinjlim_\alpha G_\alpha$ is countable.

::: pf-proof
By the definition of the direct limit in §3.3 it is a quotient of the direct sum $\bigoplus_\alpha G_\alpha$, and that is a quotient of the disjoint union $\coprod_\alpha G_\alpha$. A countable disjoint union of countable sets is countable, and a quotient of a countable set is countable, so the limit is countable.
:::

:::

::: {.pf-step #exhaustion}
An open $X\subseteq\RR^n$ is the union of an increasing sequence $K_1\subseteq K_2\subseteq\cdots$ of finite subcomplexes of a cubical cell structure, and every compact subset of $X$ lies in some $K_j$.

::: pf-proof
For $j\ge1$ let $\mathcal Q_j$ be the grid of closed cubes of side $2^{-j}$ whose vertices lie in $2^{-j}\ZZ^n$, and let $K_j$ be the union of the cubes $Q\in\mathcal Q_j$ with $Q\subseteq X\cap[-j,j]^n$. There are finitely many such $Q$, since they all lie in the bounded box, so $K_j$ is a finite subcomplex of the cubical structure of $\RR^n$. It is contained in $X$, and $K_j\subseteq K_{j+1}$ because a cube of $\mathcal Q_j$ is a union of cubes of $\mathcal Q_{j+1}$ and $[-j,j]^n\subseteq[-(j+1),j+1]^n$.

Let $C\subseteq X$ be compact. Each $x\in C$ has $d(x,\RR^n-X)>0$, so by compactness there is $j$ with $d(x,\RR^n-X)>2^{-j}\sqrt n$ and $\abs x<j-1$ for every $x\in C$. If $Q\in\mathcal Q_j$ contains $x\in C$ and $y\in Q$, then $\abs{x-y}\le2^{-j}\sqrt n<d(x,\RR^n-X)$, so $y\in X$, and $\abs y\le\abs x+2^{-j}\sqrt n<j$. Hence $Q\subseteq X\cap[-j,j]^n$, so $Q\subseteq K_j$ and $x\in K_j$. Therefore $C\subseteq K_j$, and in particular $X=\bigcup_jK_j$.
:::

:::

::: {.pf-step #chains}
$C_*(X;\ZZ)=\varinjlim_jC_*(K_j;\ZZ)$.

::: pf-proof
A singular simplex of $X$ has compact image, so by step [](#exhaustion){.pf-ref} it is a simplex of some $K_j$; a chain is a finite sum of simplices, so it lies in some $C_*(K_j;\ZZ)$, and the same argument applies to a finite chain homotopy. Hence the union of the images of the inclusions $C_*(K_j;\ZZ)\to C_*(X;\ZZ)$ is all of $C_*(X;\ZZ)$, and since the $K_j$ are nested the chain complexes form a directed system with direct limit $C_*(X;\ZZ)$.
:::

:::

::: {.pf-step #homology}
$H_i(X;\ZZ)\cong\varinjlim_jH_i(K_j;\ZZ)$ for every $i$.

::: pf-proof
This is §3.3 Exercise 17, that homology commutes with direct limits: applied to the directed system of chain complexes of step [](#chains){.pf-ref}, it identifies the homology of the limit with the limit of the homologies.
:::

:::

::: {.pf-step #stages}
Each $H_i(K_j;\ZZ)$ is finitely generated, hence countable.

::: pf-proof
$K_j$ is a finite cubical complex, so its cellular chain group in each degree is a finitely generated free abelian group; a subgroup of such a group is again finitely generated and free, so each homology group is finitely generated. A finitely generated abelian group is countable.
:::

:::

::: {.pf-step}
$H_i(X;\ZZ)$ is countable for every $i$ when $X\subseteq\RR^n$ is open, and a direct limit of countable abelian groups over a countable indexing set is countable.

::: pf-proof
The general statement is step [](#limit-countable){.pf-ref}. For $X$ open, step [](#homology){.pf-ref} exhibits $H_i(X;\ZZ)$ as the direct limit of the $H_i(K_j;\ZZ)$ over the countable indexing set $\{1,2,\ldots\}$, and step [](#stages){.pf-ref} makes each of them countable, so step [](#limit-countable){.pf-ref} applies.
:::

:::

:::

:::
