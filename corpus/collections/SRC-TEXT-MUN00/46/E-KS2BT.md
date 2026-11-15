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
(a) Let $\mathcal B$ be a countable basis for the locally compact space $X$. For each $x$, choose an open $U_x$ and compact $K_x$ with $x\in U_x\subset K_x$. Choose a basis element $B_x$ with $x\in B_x\subset U_x$. Only countably many distinct $B_x$ occur; choosing one compact $K_x$ for each such basis element gives countably many compact sets whose interiors cover $X$. Thus $X$ is $\sigma$-compact.

(b) Choose compact $A_1,A_2,\dots$ whose interiors cover $X$, and replace them by finite unions so that $A_i\subset A_{i+1}$. Put on $Y_i=Y^{A_i}$ the bounded uniform metric
$$
\rho_i(u,v)=\min\{1,\sup_{A_i}d(u,v)\}.
$$
Define
$$
\rho(f,g)=\sum_{i=1}^\infty2^{-i}\rho_i(f\restrict_{A_i},g\restrict_{A_i}).
$$
This induces exactly compact convergence, in both directions. Let $f\in Y^X$, let $C\subset X$ be compact and let $0<\epsilon\le1$. The interiors $\operatorname{Int}A_i$ cover $C$, so finitely many of them cover it, and since the $A_i$ increase, $C\subset A_N$ for some $N$. If $\rho(f,g)<2^{-N}\min\{\epsilon,1\}$ then $2^{-N}\rho_N(f,g)<2^{-N}\min\{\epsilon,1\}$, so $\rho_N(f,g)<\min\{\epsilon,1\}\le1$, and a minimum of $1$ and a number below $1$ being that number, $\sup_{A_N}d(f,g)=\rho_N(f,g)<\epsilon$; then $\sup_Cd(f,g)\le\sup_{A_N}d(f,g)<\epsilon$ because $C\subset A_N$. So
$$
B_\rho\bigl(f,2^{-N}\min\{\epsilon,1\}\bigr)\subset B_C(f,\epsilon).
$$
Conversely, choose $N$ with $2^{-N}<\epsilon/2$ and suppose $\sup_{A_N}d(f,g)<\epsilon/2$. For $i\le N$ the inclusion $A_i\subset A_N$ gives $\rho_i(f\restrict_{A_i},g\restrict_{A_i})\le\sup_{A_N}d(f,g)<\epsilon/2$, a bound that is below $1$, and for $i>N$ one has $\rho_i\le1$; hence
$$
\rho(f,g)\le\sum_{i=1}^{N}2^{-i}\frac{\epsilon}{2}+\sum_{i>N}2^{-i}<\frac{\epsilon}{2}+2^{-N}<\epsilon,
$$
that is $B_{A_N}(f,\epsilon/2)\subset B_\rho(f,\epsilon)$. A ball of radius at least $1$ is the whole space, so the two topologies have the same neighbourhoods of each point.

The restriction map
$$
R:Y^X\to\prod_iY_i,\qquad f\mapsto(f\restrict_{A_i})
$$
is injective, and its image is the set of points $u$ with $u_{i+1}\restrict_{A_i}=u_i$ for every $i$. That image is closed. For fixed $i$ the restriction $\varphi_i:Y_{i+1}\to Y_i$ is $1$-Lipschitz, since $\sup_{A_i}d\le\sup_{A_{i+1}}d$, hence continuous, so $u\mapsto(u_i,\varphi_i(u_{i+1}))$ is a continuous map $\prod_jY_j\to Y_i\times Y_i$; the diagonal of $Y_i\times Y_i$ is closed there, $Y_i$ being a metric space; so the $i$-th compatibility condition is a closed subset of the product, and their intersection, the image of $R$, is closed. Moreover $R$ is an isometry onto its image, since $\rho$ was defined as a series of the coordinate metrics.

If $Y$ is complete then each uniform function space $Y_i$ is complete: a $\rho_i$-Cauchy sequence is uniformly Cauchy on $A_i$ because $\rho_i$ is $1$-bounded, it converges pointwise by completeness of $Y$, and the pointwise limit is the uniform limit, a uniform Cauchy sequence converging uniformly to its pointwise limit. The metric $\sum_i2^{-i}\rho_i$ on $\prod_iY_i$ is then complete: a Cauchy sequence in it is Cauchy in each coordinate, since $2^{-i}\rho_i\le\rho$, so it converges coordinatewise, to $f$ say, and it converges in $\rho$ as well, because for a given $\epsilon$ one takes $N$ with $2^{-N}<\epsilon/2$, and then for every $k$ beyond an index at which the first $N$ coordinates are within $\epsilon/2$ of their limits,
$$
\rho(f_k,f)\le\sum_{i\le N}2^{-i}\frac{\epsilon}{2}+\sum_{i>N}2^{-i}<\frac{\epsilon}{2}+\frac{\epsilon}{2}=\epsilon.
$$
A closed subspace of a complete metric space is complete, so the compatibility subspace is complete, and $R^{-1}$ carries $\rho$ back, $(Y^X,\rho)$ being isometric to it. Hence $(Y^X,\rho)$ is complete.
:::
