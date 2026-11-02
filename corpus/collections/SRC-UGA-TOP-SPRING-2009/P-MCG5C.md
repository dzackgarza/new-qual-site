---
schema: qual/card@1
id: P-MCG5C
kind: problem
title: Compactness and Euler characteristic of covering spaces, and coverings of even-dimensional
  $\RP^N$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Euler Characteristic
  - Cell Complexes
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-02
  note: >-
    The solution was an outline: five steps whose proof blocks were single hints ("covering of compact
    is compact iff finite sheeted", "lift cell structure", "chi(RP^2k) = 1", "d divides 1"), which is
    what issue #96 flagged. Replaced by proofs, not restyled. The compactness direction that the
    outline skipped entirely is now an elementary finite-subcover argument that also fixes what the
    hint elided: a fibre is a closed discrete subset of Y, hence finite when Y is compact, which is
    the only way finiteness of the degree follows from compactness. The Euler-characteristic step now
    names its hypothesis (X finite CW, which is where the alternating sum is an integer) and derives
    the cell count of Y from the lifted cell structure. The RP conclusion now says why the base is
    finite CW: the problem's standing hypothesis makes X a CW complex, and a compact CW complex has
    finitely many cells, so chi(X) is an integer and d divides 1. A remark records that scope, since
    the printed part (c) renames only the total space and omits it. The statement is unchanged from
    the printed Problem 6 of the Spring 2009 UGA topology qualifying exam.
---

::: {.problem}
Let $X$ be a CW complex and let $\pi : Y \to X$ be a covering space.

Show that $Y$ is compact iff $X$ is compact and $\pi$ has finite degree.

Assume that $\pi$ has finite degree $d$.
Show that $\chi (Y ) = d \chi (X)$.

Let $\pi :\RP^N \to X$ be a covering map.
Show that if $N$ is even, $\pi$ is a homeomorphism.

:::

::: {.remark}
The problem's standing hypothesis is that $X$ is a **connected CW complex**, and each part uses it. Connectedness is what makes the sheet number a single integer instead of one number per component, and the CW hypothesis is what makes $\chi$ defined and integral.

Parts (a) and (b) are stated for a CW base, and (b) needs it finite, since the alternating sum over cells is an integer only then. Part (c) renames only the total space, so the base is still a CW complex; that is what turns compactness of $X$ into $\chi(X)\in\ZZ$, as step [](#finite-base){.pf-ref} records. For a base space with no such structure, (a) still gives $d<\infty$ but $\chi(X)$ need not be defined, so (c) does not follow by this route.

:::

::: {.solution}

::: pf

::: {.pf-step #sheet-count}
The fibre cardinality is locally constant, so on the connected space $X$ there is $d\in\NN\cup\{\infty\}$, the degree, with $\abs{\pi^{-1}(x)}=d$ for every $x\in X$.

::: pf-proof
Let $U$ be an evenly covered neighbourhood of $x$, so that $\pi^{-1}(U)$ is a disjoint union of open subsets each mapped homeomorphically onto $U$ by $\pi$. For $x'\in U$, each such sheet meets $\pi^{-1}(x')$ in exactly one point: the sheet is homeomorphic to $U$ over $U$, so it contains exactly one point over $x'$. Hence $\abs{\pi^{-1}(x')}=\abs{\pi^{-1}(x)}$, and the function $x\mapsto\abs{\pi^{-1}(x)}$ is locally constant. A locally constant function from a connected space to a discrete set is constant.

:::

:::

::: {.pf-step #fibre-finite}
If $Y$ is compact then every fibre $\pi^{-1}(x)$ is finite.

::: pf-proof
The fibre is closed: it is the preimage of the point $x$, and points of the CW complex $X$ are closed. It is discrete in its subspace topology: every $y\in\pi^{-1}(x)$ has an evenly covered neighbourhood whose sheet through $y$ meets $\pi^{-1}(x)$ only in $y$. Now let $F=\pi^{-1}(x)$. Each $\{y\}$ with $y\in F$ is open in $F$, so there are open $V_y\subseteq Y$ with $V_y\cap F=\{y\}$, and $Y\setminus F$ is open because $F$ is closed. The sets $Y\setminus F$ and the $V_y$ cover $Y$, so by compactness finitely many of them cover $Y$; a finite such subcover uses finitely many $V_y$, and those $y$ exhaust $F$.

:::

:::

::: {.pf-step #base-compact}
If $Y$ is compact then $X$ is compact.

::: pf-proof
The map $\pi$ is continuous and surjective, so $X=\pi(Y)$ is a continuous image of a compact space.

:::

:::

::: {.pf-step #total-compact}
If $X$ is compact and $d<\infty$ then $Y$ is compact.

::: pf-proof
Let $\mathcal{U}$ be an open cover of $Y$. Fix $x\in X$ and write $\pi^{-1}(x)=\{y_1,\dots,y_d\}$. For each $i$ choose $U_i\in\mathcal{U}$ with $y_i\in U_i$, and an evenly covered neighbourhood $V_i$ of $x$ with sheet $S_i$ through $y_i$. Then $\pi(S_i\cap U_i)$ is an open neighbourhood of $x$ inside $V_i$, because $\pi$ maps $S_i$ homeomorphically onto the open set $V_i$; put $W_i=\pi(S_i\cap U_i)$ and $W=\bigcap_i W_i$, an open neighbourhood of $x$. Over $W$ the sheet through $y_i$ is $S_i\cap\pi^{-1}(W)$, and it lies in $U_i$: if $z\in S_i$ has $\pi(z)\in W\subseteq\pi(S_i\cap U_i)$ then $z$, being the unique point of $S_i$ over $\pi(z)$, lies in $S_i\cap U_i$. These $d$ sheets cover $\pi^{-1}(W)$. The sets $W$, one for each $x$, cover the compact $X$, so finitely many $W_{x_1},\dots,W_{x_m}$ cover $X$; the finitely many sets $U_i$ used for these $m$ points cover $Y$, and each lies in $\mathcal{U}$.

:::

:::

::: {.pf-step #compactness}
$Y$ is compact if and only if $X$ is compact and $d$ is finite.

::: pf-proof
If $Y$ is compact then $X$ is compact by step [](#base-compact){.pf-ref} and $d$ is finite by steps [](#fibre-finite){.pf-ref} and [](#sheet-count){.pf-ref}. Conversely if $X$ is compact and $d$ is finite then $Y$ is compact by step [](#total-compact){.pf-ref}.

:::

:::

::: {.pf-step #lifted-cells}
Let $X$ be a finite CW complex and $d$ finite. Then $Y$ is a finite CW complex, and the number of $k$-cells of $Y$ is $d$ times the number of $k$-cells of $X$, for every $k$.

::: pf-proof
Take a cell $e\subseteq X$ with characteristic map $\Phi\colon D^k\to X$. Since $D^k$ is compact and connected and $X$ is evenly covered over the interior of $e$, the preimage $\pi^{-1}(e)$ is a disjoint union of $d$ open sets, each mapping homeomorphically onto $e$; their closures are obtained by adjoining the lifts of the attaching sphere, and the composites $D^k\to\pi^{-1}(e)\to e\subseteq X$ serve as characteristic maps. The lifted cells cover $Y$, and their intersections are the lifted skeleta, so this is a CW structure on $Y$. Counting, $c_k(Y)=d\,c_k(X)$ for every $k$, and both are finite because $X$ has finitely many cells.

:::

:::

::: {.pf-step #chi-multiplicative}
If $X$ is a finite CW complex and $d$ is finite then $\chi(Y)=d\,\chi(X)$.

::: pf-proof
By step [](#lifted-cells){.pf-ref},
$$
\chi(Y)=\sum_k(-1)^k c_k(Y)=\sum_k(-1)^k d\,c_k(X)=d\sum_k(-1)^k c_k(X)=d\,\chi(X),
$$
both sums being finite.

:::

:::

::: {.pf-step #rp-chi}
$\chi(\RP^N)=1$ when $N$ is even, and $\chi(\RP^N)=0$ when $N$ is odd.

::: pf-proof
The standard CW structure on $\RP^N$ has exactly one cell in each dimension $0,\dots,N$, so $c_k=1$ for $k\le N$ and $c_k=0$ otherwise. Hence $\chi(\RP^N)=\sum_{k=0}^N(-1)^k$, which is $1$ for even $N$ and $0$ for odd $N$.

:::

:::

::: {.pf-step #finite-base}
Let $\pi\colon\RP^N\to X$ be a covering with $X$ a connected CW complex and $N$ even. Then $X$ is a finite CW complex and $\chi(X)$ is an integer.

::: pf-proof
$\RP^N$ is compact, so $X$ is compact by step [](#base-compact){.pf-ref}. A compact CW complex has finitely many cells: if $X$ had infinitely many, it would be the union of a strictly increasing sequence of finite subcomplexes, each closed and proper, and a compact subset of a CW complex lies in a finite subcomplex, so no strictly increasing sequence can exhaust it. Hence $X$ is a finite CW complex and $\chi(X)$ is an integer.

:::

:::

::: {.pf-step #degree-one}
Let $\pi\colon\RP^N\to X$ be a covering with $X$ a connected CW complex and $N$ even. Then $d=1$.

::: pf-proof
By steps [](#compactness){.pf-ref}, [](#finite-base){.pf-ref} and [](#chi-multiplicative){.pf-ref},
$$
1=\chi(\RP^N)=d\,\chi(X)
$$
with $d$ a positive integer and $\chi(X)$ an integer, by step [](#rp-chi){.pf-ref}. A positive integer dividing $1$ is $1$, so $d=1$.

:::

:::

::: {.pf-step #homeomorphism}
A covering $\pi\colon Y\to X$ of finite degree $1$ is a homeomorphism.

::: pf-proof
Every fibre is a single point, so $\pi$ is a bijection; it is continuous by hypothesis and a local homeomorphism, hence open, because a local homeomorphism carries open sets to open sets. A continuous open bijection is a homeomorphism.

:::

:::

::: pf-qed
Part (a) is step [](#compactness){.pf-ref}: compactness of $Y$ is equivalent to compactness of $X$ together with finiteness of the degree, with compactness of $X$ coming from the continuous surjection and finiteness of the degree from the fibres being closed discrete subsets of the compact $Y$. Part (b) is step [](#chi-multiplicative){.pf-ref}: for a finite CW complex the lifted cell structure has $d$ times as many cells in every dimension, so the alternating sums differ by the factor $d$. Part (c) is steps [](#degree-one){.pf-ref} and [](#homeomorphism){.pf-ref}: for even $N$ the compactness of $\RP^N$ forces the base to be a finite CW complex, its Euler characteristic is then an integer, and $1=\chi(\RP^N)=d\,\chi(X)$ forces $d=1$, so $\pi$ is a bijective local homeomorphism and therefore a homeomorphism.

:::

:::

:::
