---
schema: qual/card@1
id: E-CT4NT
kind: problem
title: Arzelà's theorem over $\sigma$-compact Hausdorff domains
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §47 Exercise 4 (printed p. 293) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against the book, following the
    exercise's hint: the compact sets A_j with interiors covering X exist by the definition of sigma-compactness
    plus taking finite unions, the weighted sum of the bounded uniform metrics on the A_j gives a metric for
    compact convergence (the same construction as Exercise 46.10(b), which the card cites in substance), so the
    function space is first-countable; on each compact A_j Ascoli's theorem (Theorem 45.4) and Theorem 28.2 give
    a uniformly convergent subsequence, the diagonal subsequence converges uniformly on every A_j, and f is
    continuous because at a point x one takes j with x in the interior of A_j and uses continuity of the
    restriction, which is a uniform limit of continuous functions (Theorem 21.6). Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). The AoPS blog post by cinnamon_e, "Topology by
    Munkres Chapter 7 | Day 17" (2025-09-10,
    https://artofproblemsolving.com/community/c3401823h3646977, text at
    tmp/sources/aops-shooting-star-munkres-ch7-day17.md), answers this exercise at its item 4 of
    §47, and the extraction dropped every inline formula, so the answer cannot be transcribed; the
    site answers an automated request with a Cloudflare human check, which is not worked around.
    Murayama's selection stops at Chapter 4, dbFin has no chapter-7 page, and the Math StackExchange
    queries of this pass for Arzela's theorem over a sigma-compact Hausdorff domain, recorded in the
    COMPLAINTS.md entry for §43--§50, returned only questions about the hypotheses of the classical
    statement and their failure. The card keeps its own proof.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewrote the proof as a Lamport proof with the construction of the exhaustion, the metric, the
    per-level Ascoli step, the diagonal subsequence and the continuity of the limit as separate
    steps; the mathematics is the card's own, no retained set covering the exercise, as the two
    notes above record. Two things the prose left implicit are now proved rather than asserted:
    that uniform convergence on every A_j is the compact-convergence topology (a compact subset of
    X lies in some int A_j, since the increasing interiors cover X), and that f is continuous
    (its restriction to each open set int A_j is continuous, being the restriction of a uniform
    limit of continuous functions on A_j, and continuity is local). The exhaustion is built from a
    countable cover by compact sets by finite unions, so each A_j is compact and the interiors
    cover. In the second note above the statement "Murayama's selection stops at Chapter 4" is
    read only as the earlier session's record and is not re-checked here.
---

::: {.exercise}

Prove the following.

Theorem (Arzela's theorem, general version).
Let $X$ be a Hausdorff space that is $\sigma$-compact; let $f_n$ be a sequence of functions $f_n: X \to \RR^k$.
If the collection $(f_n)$ is pointwise bounded and equicontinuous, then the sequence $f_n$ has a subsequence that converges, in the topology of compact convergence, to a continuous function.

[Hint: Show that $\mathcal{C}(X, \RR^k)$ is first-countable.]
:::

::: {.solution}
No retained published solution covers this exercise, so the argument is the card's own; the hint is the book's. Write $\mathcal{C}(X,\RR^{k})$ for the set of continuous maps with the topology of compact convergence, and $\norm{\cdot}$ for the Euclidean norm on $\RR^{k}$.

::: pf

::: {.pf-step #exhaustion}
There are compact sets $A_{1}\subset A_{2}\subset\cdots$ in $X$ whose interiors cover $X$.

::: pf-proof
Since $X$ is $\sigma$-compact, $X=\bigcup_{n}K_{n}$ with each $K_{n}$ compact. Put $A_{j}=K_{1}\cup\cdots\cup K_{j}$, a finite union of compact sets, hence compact, and $A_{j}\subset A_{j+1}$. Each $K_{n}$ lies in $A_{n}$ and hence in the interior of $A_{n}$, so $X=\bigcup_{n}K_{n}\subset\bigcup_{j}\operatorname{int}A_{j}$.
:::

:::

::: {.pf-step #metric}
$\rho(f,g)=\sum_{j\ge1}2^{-j}\min\theset{1,\sup_{A_{j}}\norm{f-g}}$ defines a metric on $\mathcal{C}(X,\RR^{k})$ whose topology is the topology of compact convergence.

::: pf-proof
Each $\sup_{A_{j}}\norm{f-g}$ is finite because $f-g$ is continuous and $A_{j}$ is compact, so every term is at most $2^{-j}$ and the series converges; symmetry and the triangle inequality hold termwise, and $\rho(f,g)=0$ forces $f=g$ on every $A_{j}$, hence on $X$ because the $A_{j}$ cover $X$. For the topology, let $f_{n},f\in\mathcal{C}(X,\RR^{k})$. If $\rho(f_{n},f)\to0$ then for each $j$ the $j$-th term is at most $2^{j}\rho(f_{n},f)$, so $\sup_{A_{j}}\norm{f_{n}-f}$ stays below any $\varepsilon<1$ eventually. Conversely, if $\sup_{A_{j}}\norm{f_{n}-f}\to0$ for every $j$, then given $\varepsilon>0$ choose $J$ with $\sum_{j>J}2^{-j}<\varepsilon/2$ and $N$ beyond which the first $J$ terms are each below $\varepsilon/(2J)$, so $\rho(f_{n},f)<\varepsilon$ for $n\ge N$. Finally, a compact $C\subset X$ is covered by the increasing open sets $\operatorname{int}A_{j}$, so $C\subset\operatorname{int}A_{j}\subset A_{j}$ for some $j$ by compactness, and uniform convergence on $A_{j}$ gives uniform convergence on $C$. Hence convergence in $\rho$ is convergence uniformly on every compact set.
:::

:::

::: {.pf-step #per-level-subsets}
For each $j$ the restricted family $\theset{f_{n}\restrict_{A_{j}}}$ is pointwise bounded and equicontinuous on the compact space $A_{j}$.

::: pf-proof
Pointwise boundedness: for $x\in A_{j}$ the set $\theset{f_{n}(x)}$ is bounded because the family is pointwise bounded on $X$. Equicontinuity: given $x\in A_{j}$ and $\varepsilon>0$, equicontinuity on $X$ supplies a neighbourhood $U$ of $x$ in $X$ with $\norm{f_{n}(y)-f_{n}(x)}<\varepsilon$ for all $n$ and all $y\in U$; then $U\cap A_{j}$ is a neighbourhood of $x$ in $A_{j}$ with the same property.
:::

:::

::: {.pf-step #level-subsequence}
For each $j$, every sequence of members of the family has a subsequence converging uniformly on $A_{j}$.

::: pf-proof
A subsequence of a pointwise bounded equicontinuous family is again pointwise bounded and equicontinuous, so by step [](#per-level-subsets){.pf-ref} the restrictions to $A_{j}$ of its members form a pointwise bounded equicontinuous family of continuous maps on the compact space $A_{j}$. By Ascoli's theorem (Theorem 45.4) the closure of that family in $\mathcal{C}(A_{j},\RR^{k})$ with the uniform metric is compact, and a compact metric space is sequentially compact (Theorem 28.2), so the sequence has a subsequence converging uniformly on $A_{j}$.
:::

:::

::: {.pf-step #diagonal}
There is a subsequence of $(f_{n})$ converging uniformly on each $A_{j}$.

::: pf-proof
Choose indices $n_{1,1}<n_{1,2}<\cdots$ such that $(f_{n_{1,i}})$ converges uniformly on $A_{1}$, which step [](#level-subsequence){.pf-ref} provides; then from it choose a subsequence $(f_{n_{2,i}})$ converging uniformly on $A_{2}$, again by step [](#level-subsequence){.pf-ref}, and continue inductively, so that $(f_{n_{j,i}})_{i}$ is a subsequence of $(f_{n_{j-1,i}})_{i}$ and converges uniformly on $A_{j}$. Let $m_{i}=n_{i,i}$. For fixed $j$, the tail $m_{j},m_{j+1},\dots$ is a subsequence of $(n_{j,i})_{i}$, so $(f_{m_{i}})_{i\ge j}$ converges uniformly on $A_{j}$, and the finitely many earlier terms do not affect convergence.
:::

:::

::: {.pf-step #continuous-limit}
The diagonal subsequence converges uniformly on each $A_{j}$ to a continuous $f:X\to\RR^{k}$.

::: pf-proof
Step [](#diagonal){.pf-ref} gives a function $f$ on each $A_{j}$ as the uniform limit of the continuous maps $f_{m_{i}}\restrict_{A_{j}}$, and these definitions agree where the $A_{j}$ overlap, so $f$ is defined on $X=\bigcup_{j}A_{j}$. On $A_{j}$ it is a uniform limit of continuous functions, hence continuous (Theorem 21.6). For $x\in X$ choose $j$ with $x\in\operatorname{int}A_{j}$; the set $\operatorname{int}A_{j}$ is an open neighbourhood of $x$ on which $f$ agrees with the continuous map $f\restrict_{A_{j}}$, so $f$ is continuous at $x$, and $x$ was arbitrary.
:::

:::

::: {.pf-step #answer}
The diagonal subsequence converges to the continuous $f$ in the topology of compact convergence.

::: pf-proof
Step [](#continuous-limit){.pf-ref} gives uniform convergence on every $A_{j}$ to the continuous $f$, and step [](#metric){.pf-ref} identifies uniform convergence on every $A_{j}$ with convergence in the topology of compact convergence. That is the subsequence the theorem asserts.
:::

:::

:::
:::
