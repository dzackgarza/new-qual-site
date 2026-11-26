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
- event: solution-written
  by: chatgpt
  date: 2026-11-25
  note: >-
    Corrected the invalid inference in the 2026-11-11 and 2026-11-18
    records that containment in a compact set gives containment in its interior.
    Munkres, Topology, second edition, section 46 Exercise 10 (printed p. 289)
    defines sigma-compactness using a countable cover by open sets contained
    in compact sets. The actual statement is section 47 Exercise 4 (printed
    p. 293). Located Yang Di, Munkres Topology Solution: Chapter 7,
    Ex.47.4 (2025-01-15),
    https://hexo.yougi.top/2025/01/15/Munkres-Topology-Solution-Chapter-7/#Ex-47-4,
    whose proof uses compact closure and metrizability. Replaced the erroneous
    exhaustion proof with a Lamport presentation of that published argument:
    Exercise 46.10(b), Theorem 47.1(a) and Exercise 47.2, and Theorem 28.2,
    with the hypotheses checked. The earlier dated records are preserved.
---

::: {.exercise}

Prove the following.

Theorem (Arzela's theorem, general version).
Let $X$ be a Hausdorff space that is $\sigma$-compact; let $f_n$ be a sequence of functions $f_n: X \to \RR^k$.
If the collection $(f_n)$ is pointwise bounded and equicontinuous, then the sequence $f_n$ has a subsequence that converges, in the topology of compact convergence, to a continuous function.

[Hint: Show that $\mathcal{C}(X, \RR^k)$ is first-countable.]
:::

::: {.solution}

The argument follows [Yang Di, *Munkres Topology Solution: Chapter 7*, §47 Exercise 4](https://hexo.yougi.top/2025/01/15/Munkres-Topology-Solution-Chapter-7/#Ex-47-4), with the definition of $\sigma$-compactness in Munkres, *Topology*, 2nd ed. (2000), §46 Exercise 10. Write $\mathcal F=\theset{f_n:n\ge1}$.

::: pf

::: {.pf-step #compact-convergence-metric}

The function space $\mathcal C(X,\RR^k)$ in the topology of compact convergence is metrizable.

::: pf-proof

By the definition in §46 Exercise 10, there are open sets $U_i$ covering $X$ and compact sets $K_i$ with $U_i\subseteq K_i$. Thus $X$ is locally compact, and the increasing compact sets $A_j=\bigcup_{i=1}^j K_i$ have interiors covering $X$: $U_i\subseteq\operatorname{int}A_j$ whenever $i\le j$. Consequently every compact subset of $X$ lies in some $A_j$, by taking a finite subcover from the $U_i$. Exercise 46.10(b) gives a metric for compact convergence on $(\RR^k)^X$. Its restriction to $\mathcal C(X,\RR^k)$ is a metric for the subspace topology, which is compact convergence.

:::

:::

::: {.pf-step #compact-family}

The closure of $\mathcal F$ in $\mathcal C(X,\RR^k)$ is compact.

::: pf-proof

Equicontinuity implies continuity of each $f_n$, so $\mathcal F$ is a subset of the indicated function space. For each $x\in X$, pointwise boundedness gives that $\theset{f_n(x):n\ge1}$ has compact closure in $\RR^k$ by Heine--Borel. Together with equicontinuity these are the hypotheses of Munkres Theorem 47.1(a), which places $\mathcal F$ in a compact subspace of $\mathcal C(X,\RR^k)$. The function space is Hausdorff by step [](#compact-convergence-metric){.pf-ref}, so that compact subspace is closed. The closure of $\mathcal F$ is a closed subset of it and therefore compact. This is the compact-closure assertion of §47 Exercise 2.

:::

:::

::: pf-qed

By step [](#compact-family){.pf-ref} the sequence lies in a compact subspace that is metrizable by step [](#compact-convergence-metric){.pf-ref}. Compact metric spaces are sequentially compact (Munkres Theorem 28.2). Hence a subsequence converges in the compact-convergence topology to an element of the closure, which is a continuous map $X\to\RR^k$.

:::

:::

:::

