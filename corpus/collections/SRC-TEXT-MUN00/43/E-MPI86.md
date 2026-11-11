---
schema: qual/card@1
id: E-MPI86
kind: problem
title: Metrically equivalent metrics and completeness
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Transcribed from two located published solutions, one per part. Part (a) from "Tze Heng", *Munkres'
    Topology: Self-study Notes and Exercises Attempts*, Chapter 7, "Exercises Attempts", the item numbered
    3(a) under "Exercise after §43" (URL
    https://blog.ttheng.com/docs/mathematics/munkres-topology-self-study/chapt-7/exercises/, read
    2026-11-11): the identity is uniformly continuous both ways because d-bar <= d, and conversely
    d-bar(x,y) < min{eps,1} forces d(x,y) = d-bar(x,y). Part (b) from "Solutions to exercises for
    Mathematics 205A" (University of California, Riverside, Fall 2014), Part 3, section "III.2: Complete
    metric spaces", answer to §43 Exercise 3(b) on the set's own printed p. 4 (in
    tmp/sources/munkres-solutions-ucr-math205-gentop.pdf, PDF p. 45): uniform continuity carries Cauchy
    sequences both ways, completeness under d gives the limit, and continuity of the identity gives
    convergence under d-prime. Checked against Munkres, Topology (2000), §43 Exercise 3, printed p. 270,
    with the definition of metric equivalence, the standard bounded metric of §20, and the fact that a
    uniformly continuous map carries Cauchy sequences to Cauchy sequences. What was corrected: the blog's
    part (b) is a single paragraph that reuses "delta = eps" from part (a) and never records that the
    limit found under d must be the same point as the d-prime limit; the card's part (b) is the
    Riverside argument, with the identity's continuity supplying the last step. The card also has the
    printed statement's part (a), which the Riverside set does not answer.
---

::: {.exercise}

Two metrics $d$ and $d'$ on a set $X$ are said to be metrically equivalent if the identity map $i: (X, d) \to (X, d')$ and its inverse are both uniformly continuous.

(a) Show that $d$ is metrically equivalent to the standard bounded metric $\bar{d}$ derived from $d$.

(b) Show that if $d$ and $d'$ are metrically equivalent, then $X$ is complete under $d$ if and only if it is complete under $d'$.
:::

::: {.solution}
(a) Recall that the standard bounded metric is
$$
\bar d(x,y)=\min\{d(x,y),1\}.
$$
The identity
$$
i:(X,d)\to(X,\bar d)
$$
is uniformly continuous because $\bar d\le d$: given $\varepsilon>0$, take $\delta=\varepsilon$.

For the inverse identity, given $\varepsilon>0$, choose
$$
\delta=\tfrac12\min\{\varepsilon,1\}.
$$
If $\bar d(x,y)<\delta<1$, then necessarily $d(x,y)<1$, so $\bar d(x,y)=d(x,y)<\delta\le\varepsilon$. Thus the inverse identity is uniformly continuous. Hence $d$ and $\bar d$ are metrically equivalent.

(b) Suppose $d$ and $d'$ are metrically equivalent. A uniformly continuous map sends Cauchy sequences to Cauchy sequences. Since both identity maps
$$
(X,d)\rightleftarrows(X,d')
$$
are uniformly continuous, a sequence is $d$-Cauchy if and only if it is $d'$-Cauchy.

Assume $(X,d)$ is complete and let $(x_n)$ be $d'$-Cauchy. Then it is $d$-Cauchy, hence $x_n\to x$ in $d$ for some $x\in X$. Continuity of the identity $(X,d)\to(X,d')$ gives $x_n\to x$ in $d'$. Thus $(X,d')$ is complete. The converse is symmetric.
:::
