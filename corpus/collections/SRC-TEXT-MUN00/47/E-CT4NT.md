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
    No complete published solution of Munkres §47 Exercise 4 was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against the book, following the
    exercise's hint: the compact sets A_j with interiors covering X exist by the definition of sigma-compactness
    plus taking finite unions, the weighted sum of the bounded uniform metrics on the A_j gives a metric for
    compact convergence (the same construction as Exercise 46.10(b), which the card cites in substance), so the
    function space is first-countable; on each compact A_j Ascoli's theorem (Theorem 45.4) and Theorem 28.2 give
    a uniformly convergent subsequence, the diagonal subsequence converges uniformly on every A_j, and f is
    continuous because at a point x one takes j with x in the interior of A_j and uses continuity of the
    restriction, which is a uniform limit of continuous functions (Theorem 21.6). Nothing needed correction.
---

::: {.exercise}

Prove the following.

Theorem (Arzela's theorem, general version).
Let $X$ be a Hausdorff space that is $\sigma$-compact; let $f_n$ be a sequence of functions $f_n: X \to \RR^k$.
If the collection $(f_n)$ is pointwise bounded and equicontinuous, then the sequence $f_n$ has a subsequence that converges, in the topology of compact convergence, to a continuous function.

[Hint: Show that $\mathcal{C}(X, \RR^k)$ is first-countable.]
:::

::: {.solution}
Choose compact sets $A_1\subset A_2\subset\cdots$ whose interiors cover the $\sigma$-compact Hausdorff space $X$. On $C(X,\RR^k)$ the compact-convergence topology is metrizable, for example by
$$
\rho(f,g)=\sum_{j\ge1}2^{-j}\min\{1,\sup_{A_j}\norm{f-g}\},
$$
so it is first-countable.

For each compact $A_j$, the restricted family $\{f_n\restrict_{A_j}\}$ is pointwise bounded and equicontinuous. By Ascoli on the compact domain $A_j$, its closure in the uniform topology is compact; hence every sequence has a uniformly convergent subsequence on $A_j$. Starting with the original sequence, choose successively subsequences converging uniformly on $A_1,A_2,\dots$. The diagonal subsequence converges uniformly on every $A_j$, hence on every compact subset of $X$, to a function $f$. The function $f$ is continuous: its restriction to each $A_j$ is a uniform limit of continuous functions, and the interiors of the $A_j$ form an open cover of $X$. Thus the diagonal subsequence converges to $f$ in compact convergence.
:::
