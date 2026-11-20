---
schema: qual/card@1
id: E-KS2BT
kind: problem
title: Completeness of the compact convergence topology over $\sigma$-compact domains
classification:
  areas:
  - topology
  topics:
  - Function Spaces
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §46 Exercise 10 (printed p. 289) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked against the definition of sigma-compactness
    given in the exercise, Theorem 43.5 and Theorem 43.6 (completeness of the uniform function space over a
    complete target), the metric for a countable product of metric spaces (§20, Exercise 20.3) and the
    description of compact convergence by Theorem 46.2. Part (a) is the standard countability argument: each
    point has a basis element inside an open set with compact closure, and only countably many basis elements
    occur. Part (b) is the exercise's hint carried out: take compact A_i with interiors covering X and closed
    under finite unions so that they increase; the sum of the bounded uniform metrics on the Y^{A_i}, weighted
    by 2^{-i}, induces compact convergence because every compact subset of X lies in some A_i (its interiors
    form a cover) and each A_i is compact; the restriction map is an isometry onto the closed compatibility
    subspace of the product, each factor is complete when Y is, the product metric is complete, and a closed
    subspace of a complete space is complete. Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Math StackExchange 431747, "Construct a metric for the
    topology of compact convergence on Y^X so that Y^X is complete when (Y,d) is complete and X is
    sigma-compact" (2013-06-28), is this exercise. Answer 432280 by Daniel Fischer builds the metric
    sup_n eps_n min{1, sup_{K_n} d(f,g)} on an exhaustion of X by compact sets and proves that it
    induces the topology of compact convergence in both directions, for its supremum construction
    only, leaving the sum construction to the reader, and it treats completeness in two sentences:
    the pointwise limit of a delta-Cauchy sequence exists, and that the convergence is compact is
    "an easy exercise". Answer 3353044 by tadejsv shows that a space sigma-compact in Munkres'
    sense is hemicompact, so that the exhaustion catches every compact set: with A_i the compact sets
    of the definition, K_n the union of the first n, every compact subset of X lies in some K_n
    because it is covered by finitely many interiors. The card's part (b) is the same construction by
    the exercise's hint, the embedding into the closed compatibility subspace of the product of the
    uniform spaces Y^{A_i}, and it uses that hemicompactness step; its part (a) is not in either
    answer. Nothing needed correction. The AoPS blog post by cinnamon_e, "Topology by Munkres Chapter
    7 | Day 17" (2025-09-10, https://artofproblemsolving.com/community/c3401823h3646977, text at
    tmp/sources/aops-shooting-star-munkres-ch7-day17.md), also answers the exercise at its item 10 of
    §46 with its formulas lost; the queries of this pass are in the COMPLAINTS.md entry for
    §43--§50.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Part (b) asserted three things it did not prove, reported by a reader of this card: that the
    series metric induces compact convergence, that the image of the restriction map is closed, and
    that each product factor is complete. It now proves the two inclusions of neighbourhoods in the
    two topologies by explicit radii, B_rho(f, 2^{-N} min{eps,1}) inside B_C(f, eps) once C is
    contained in A_N and B_{A_N}(f, eps/2) inside B_rho(f, eps) once 2^{-N} < eps/2, both using
    A_i contained in A_N; it now proves closedness of the compatibility subspace from the fact that
    each restriction Y_{i+1} -> Y_i is 1-Lipschitz and each Y_i is Hausdorff, so that the diagonal
    of Y_i x Y_i is closed; and it now says why the countable product of the complete Y_i is
    complete. The same pass corrects the 2026-11-15 note above, which credited Fischer's answer
    with a proof of the topology for both of his constructions and with the Cauchy step: he proves
    the topology for the supremum construction only, leaves the sum construction to the reader, and
    leaves the compactness of the convergence of a Cauchy sequence as an exercise. The text of his
    answer was read from the Stack Exchange API in this pass. Part (a) is unchanged and was not
    re-read.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    A reader of this card reported that "a ball of radius at least 1 is the whole space" is false at
    radius 1: rho is a sum over i of 2^{-i} times a term of size at most 1, so rho(f, g) is at most 1,
    and it is 1 whenever sup_{A_i} d(f, g) is at least 1 for every i, as for the functions 0 and 2 when
    Y = X = R. The sentence now says that a ball of radius greater than 1 is the whole space, and that
    the balls of radius at most 1 determine the neighbourhoods, which is what the two inclusions are
    used for. Nothing else on the card was changed.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf` with
    nine steps covering (a) and (b), each carrying a `pf-proof`. Cited by numbered statement only:
    Munkres, Topology, §46 Exercise 9, Theorem 26.1 (a finite union of compact subspaces is
    compact), §21 (the bounded uniform metric), §46 (the basis $B_C(f,\varepsilon)$ of the topology
    of compact convergence), Theorem 17.8 (metric spaces are Hausdorff, so diagonals are closed) and
    §43 (a closed subspace of a complete metric space is complete). The proof remains the card's
    own: the self-study notes that reach Chapter 7 state this exercise without answering it.
    Checked: that the countable family of basis elements chosen in (a) has compact supersets whose
    interiors cover, that $C\subseteq A_N$ for some $N$ because the interiors increase and cover the
    compact $C$, the two inclusions between $\rho$-balls and $B_C(f,\varepsilon)$-balls with the
    truncation at $1$ accounted for, and that the compatibility set is an intersection of preimages
    of diagonals.
---

::: {.exercise}

A space is locally compact if it can be covered by open sets each of which is contained in a compact subspace of $X$.
It is said to be $\sigma$-compact if it can be covered by countably many such open sets.

(a) Show that if $X$ is locally compact and second-countable, it is $\sigma$-compact.

(b) Let $(Y, d)$ be a metric space.
Show that if $X$ is $\sigma$-compact, there is a metric for the topology of compact convergence on $Y^X$ such that if $(Y, d)$ is complete, $Y^X$ is complete in this metric.
[Hint: Let $A_1, A_2, \ldots$ be a countable collection of compact subspaces of $X$ whose interiors cover $X$. Let $Y_i$ denote the set of all functions from $A_i$ to $Y$, in the uniform topology. Define a homeomorphism of $Y^X$ with a closed subspace of the product space $Y_1 \times Y_2 \times \cdots$.]
:::

::: {.solution}

No retained published solution of Munkres, *Topology*, §46 Exercise 9 was located: the sets searched are listed in the `COMPLAINTS.md` entry for §43--§50 of `SRC-TEXT-MUN00`, and the self-study notes that reach Chapter 7 state this exercise without answering it. The proof is the card's own, checked against the numbered statements of §20, §21 and §46 it cites, and it follows the printed hint.

::: pf

::: {.pf-step #sigma-compact}
(a) A locally compact second-countable space $X$ is $\sigma$-compact.

::: pf-proof
Let $\mathcal B$ be a countable basis. For $x\in X$ local compactness gives an open $U_x\ni x$ and a compact $K_x$ with $U_x\subseteq K_x$, and then a basis element $B_x$ with $x\in B_x\subseteq U_x$. The set of distinct $B_x$ is a subset of $\mathcal B$, hence countable; picking one compact $K$ for each $B$ occurring gives a countable family of compact subspaces, and each $x$ lies in $B_x\subseteq K_{B_x}\subseteq\operatorname{Int}K_{B_x}$, so their interiors cover $X$.
:::

:::

::: {.pf-step #setup}
(b) There are compact subspaces $A_1\subseteq A_2\subseteq\cdots$ of $X$ whose interiors cover $X$.

::: pf-proof
$\sigma$-compactness gives compact subspaces $C_1,C_2,\dots$ whose interiors cover $X$. Put $A_i=C_1\cup\cdots\cup C_i$; a finite union of compact subspaces is compact (Munkres, Theorem 26.1 for the finite case), the family increases, and $\operatorname{Int}C_j\subseteq\operatorname{Int}A_i$ for $j\le i$, so the interiors of the $A_i$ cover $X$.
:::

:::

::: {.pf-step #metric}
(b) For $u,v\in Y^{A_i}$ put $\rho_i(u,v)=\min\{1,\sup_{a\in A_i}d(u(a),v(a))\}$, and for $f,g\in Y^X$ put
$$
\rho(f,g)=\sum_{i=1}^\infty2^{-i}\rho_i(f\restrict_{A_i},g\restrict_{A_i}).
$$
Then $\rho$ is a metric on $Y^X$.

::: pf-proof
Each $\rho_i$ is the bounded uniform metric of Munkres, §21, hence a metric on $Y^{A_i}$, and it takes values in $[0,1]$. The series converges because its terms are bounded by $2^{-i}$, it vanishes only when every $\rho_i$ vanishes, that is, when $f$ and $g$ agree on every $A_i$ and hence on $\bigcup_iA_i$; symmetry is clear; and the triangle inequality holds termwise and passes to the sum, absolute convergence permitting.
:::

:::

::: {.pf-step #rho-fine}
(b) For $f\in Y^X$, compact $C\subseteq X$ and $0<\varepsilon\le1$ there is $\delta>0$ with $B_\rho(f,\delta)\subseteq B_C(f,\varepsilon)$.

::: pf-proof
The interiors of the $A_i$ cover $C$, and $C$ is compact, so finitely many of them cover $C$; the $A_i$ increase, so $C\subseteq A_N$ for some $N$. Take $\delta=2^{-N}\varepsilon\le2^{-N}$. If $\rho(f,g)<\delta$ then $2^{-N}\rho_N(f,g)\le\rho(f,g)<\delta$, so $\rho_N(f,g)<\varepsilon\le1$; a minimum of $1$ and a number below $1$ equals that number, so $\sup_{A_N}d(f,g)=\rho_N(f,g)<\varepsilon$. Since $C\subseteq A_N$, $\sup_Cd(f,g)<\varepsilon$, that is, $g\in B_C(f,\varepsilon)$.
:::

:::

::: {.pf-step #compact-fine}
(b) For $f\in Y^X$, $N$ and $0<\varepsilon\le1$ there is a compact $B$ with $B_B(f,\varepsilon/2)\subseteq B_\rho(f,\varepsilon)$; in particular every $\rho$-ball about $f$ with radius at most $1$ contains a ball of the compact-convergence basis.

::: pf-proof
Fix $N$ with $2^{-N}<\varepsilon/2$ and take $B=A_N$; the choice of $N$ depends on $\varepsilon$ alone. Let $g$ satisfy $\sup_{A_N}d(f,g)<\varepsilon/2$. For $i\le N$ the inclusion $A_i\subseteq A_N$ bounds $\sup_{A_i}d(f,g)$ by $\varepsilon/2$, which is below $1$, so $\rho_i(f\restrict_{A_i},g\restrict_{A_i})=\sup_{A_i}d(f,g)<\varepsilon/2$; for $i>N$ one has $\rho_i\le1$. Hence
$$
\rho(f,g)\le\sum_{i=1}^{N}2^{-i}\frac{\varepsilon}{2}+\sum_{i>N}2^{-i}<\frac{\varepsilon}{2}+2^{-N}<\varepsilon .
$$
So $B_{A_N}(f,\varepsilon/2)\subseteq B_\rho(f,\varepsilon)$. Since $\rho\le1$, a ball of radius above $1$ is all of $Y^X$, so the balls of radius at most $1$ determine the topology, and the two families refine each other by this step and step [](#rho-fine){.pf-ref}.
:::

:::

::: {.pf-step #induces}
(b) $\rho$ induces the topology of compact convergence on $Y^X$.

::: pf-proof
By Munkres, §46, the topology of compact convergence has as a basis the sets $B_C(f,\varepsilon)$ with $C$ compact and $\varepsilon>0$. Steps [](#rho-fine){.pf-ref} and [](#compact-fine){.pf-ref} show that each $\rho$-ball about $f$ of radius at most $1$ contains a basis element about $f$ and is contained in one, so the two topologies have the same neighbourhoods at every point.
:::

:::

::: {.pf-step #closed-image}
(b) The restriction map $R:Y^X\to\prod_iY^{A_i}$, $R(f)=(f\restrict_{A_i})_i$, is injective with closed image, and it is an isometry onto that image when the product carries the metric $\sum_i2^{-i}\rho_i$.

::: pf-proof
Injectivity: functions agreeing on every $A_i$ agree on their union, which is $X$. The image consists of the points $u$ with $u_{i+1}\restrict_{A_i}=u_i$ for every $i$. For fixed $i$ the restriction $\varphi_i:Y^{A_{i+1}}\to Y^{A_i}$ is $1$-Lipschitz because $\sup_{A_i}d\le\sup_{A_{i+1}}d$ after truncation at $1$, hence continuous; so $u\mapsto(u_i,\varphi_i(u_{i+1}))$ is continuous into $Y^{A_i}\times Y^{A_i}$, whose diagonal is closed because $Y^{A_i}$ is metric (Munkres, Theorem 17.8 for metric spaces being Hausdorff); the $i$-th compatibility set is the preimage of that diagonal, hence closed, and the image of $R$ is the intersection of countably many closed sets. The isometry statement is the definition of $\rho$ as the sum of the coordinate metrics.
:::

:::

::: {.pf-step #coordinate-complete}
(b) If $(Y,d)$ is complete, then $Y^{A_i}$ is complete in $\rho_i$, and $\prod_iY^{A_i}$ is complete in $\sum_i2^{-i}\rho_i$.

::: pf-proof
A $\rho_i$-Cauchy sequence is uniformly Cauchy on $A_i$, hence pointwise Cauchy, hence pointwise convergent by completeness of $Y$; the pointwise limit is the uniform limit of a uniformly Cauchy sequence, so the sequence $\rho_i$-converges and $Y^{A_i}$ is complete. For the product, a Cauchy sequence in the sum metric is Cauchy in each coordinate because $2^{-i}\rho_i\le\rho$, so it converges coordinatewise to some $u$; given $\varepsilon>0$ choose $N$ with $2^{-N}<\varepsilon/2$ and then $k$ large enough that the first $N$ coordinates are within $\varepsilon/2$ of their limits, giving $\rho(u_k,u)\le\sum_{i\le N}2^{-i}\varepsilon/2+\sum_{i>N}2^{-i}<\varepsilon$.
:::

:::

::: {.pf-step #complete}
(b) If $(Y,d)$ is complete, then $Y^X$ is complete in $\rho$.

::: pf-proof
By step [](#closed-image){.pf-ref} $Y^X$ is isometric to a closed subspace of the complete space $\prod_iY^{A_i}$, and a closed subspace of a complete metric space is complete (Munkres, Theorem 43.1's statement that closed subspaces of complete spaces are complete), so $Y^X$ is complete. With step [](#induces){.pf-ref} this gives a metric for the compact-convergence topology in which $Y^X$ is complete, which is (b).
:::

:::

:::

:::
