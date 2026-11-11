---
schema: qual/card@1
id: E-S7K3V
kind: problem
title: Local compactness of balls versus completeness
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
    Transcribed from the located published solution: "Solutions to exercises for Mathematics 205A"
    (University of California, Riverside, Fall 2014), Part 3, the section "III.2: Complete metric
    spaces", answers to Munkres §43, on the set's own printed pp. 4-5 (in
    tmp/sources/munkres-solutions-ucr-math205-gentop.pdf, PDF pp. 45-46; the file names no author, so the
    course and the file are the attribution). Checked against Munkres, Topology (2000), §43 Exercise 1 (printed p. 270),
    printed p. 270, with the definition of completeness and Theorem 28.2 (a subspace of a metric space is
    compact iff it is sequentially compact). Part (a) is the set's argument: choose N so that the tail
    from x_N lies in the ball B(x_N, eps), whose closure is compact, take a convergent subsequence of the
    tail, and use the Cauchy condition to show the whole sequence converges to that limit. Part (b) is the
    card's own example, (0,1) with the usual metric, where for each x the ball of radius r < min{x,1-x}
    has closure [x-r,x+r] inside X and hence compact, while the sequence 1/(n+1) is Cauchy with no limit
    in X; the set's example, the open region {xy < 1} of R^2, which is open, has the same local property
    and is not complete because it is not closed in R^2, is recorded here and not used, the card's being
    shorter for the same point.
---

::: {.exercise}

Let $X$ be a metric space.

(a) Suppose that for some $\epsilon > 0$, every $\epsilon$-ball in $X$ has compact closure.
Show that $X$ is complete.

(b) Suppose that for each $x \in X$ there is an $\epsilon > 0$ such that the ball $B(x, \epsilon)$ has compact closure.
Show by means of an example that $X$ need not be complete.
:::

::: {.solution}
(a) Let $(x_n)$ be a Cauchy sequence. Choose $N$ such that
$$
d(x_n,x_N)<\varepsilon/2\qquad(n\ge N).
$$
Then the tail of the sequence lies in $B(x_N,\varepsilon)$, whose closure is compact by hypothesis. Hence the tail has a convergent subsequence $x_{n_k}\to x$. Since the original sequence is Cauchy, the whole sequence converges to $x$: given $\eta>0$, choose $N_1$ so $d(x_m,x_n)<\eta/2$ for $m,n\ge N_1$, then choose $k$ with $n_k\ge N_1$ and $d(x_{n_k},x)<\eta/2$. For $n\ge N_1$,
$$
d(x_n,x)<\eta.
$$
Thus every Cauchy sequence converges and $X$ is complete.

(b) Take
$$
X=(0,1)
$$
with the usual metric. For each $x\in(0,1)$, choose
$$
0<r<\min\{x,1-x\}.
$$
Then the closure in $X$ of $B(x,r)$ is the ordinary closed interval $[x-r,x+r]$, which is compact. Thus every point has a ball with compact closure.

Nevertheless $X$ is not complete: the sequence $x_n=1/(n+1)$ for $n\ge 1$ is Cauchy in $X$ but has no limit in $X$. Hence the local hypothesis in (b) does not imply completeness.
:::
