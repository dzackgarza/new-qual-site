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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured both parts into numbered steps. In (a) the pieces the transcription ran together are
    separated: the choice of N from the Cauchy condition, the containment of the tail in the ball
    whose closure is compact, sequential compactness of that closure, and the argument that a Cauchy
    sequence with a convergent subsequence converges. In (b) the closure of the ball in X is
    identified and shown compact, and the sequence is shown Cauchy with no limit in X. The
    mathematics is the earlier reading's. Not re-read this session: the UCR sheet, PDF pp. 45-46,
    and Munkres printed p. 270.
---

::: {.exercise}

Let $X$ be a metric space.

(a) Suppose that for some $\epsilon > 0$, every $\epsilon$-ball in $X$ has compact closure.
Show that $X$ is complete.

(b) Suppose that for each $x \in X$ there is an $\epsilon > 0$ such that the ball $B(x, \epsilon)$ has compact closure.
Show by means of an example that $X$ need not be complete.
:::

::: {.solution}

Part (a) is the argument of **"Solutions to exercises for Mathematics 205A" (University of California, Riverside, Fall 2014), the Munkres §43 answers, printed pp. 4--5 of that part** (`tmp/sources/munkres-solutions-ucr-math205-gentop.pdf`, PDF pp. 45--46); part (b) is the card's own example. The statement was checked against Munkres, *Topology* (2000), §43 Exercise 1, printed p. 270.

::: pf

::: {.pf-step #a-cauchy}
For a Cauchy sequence $(x_{n})$ in $X$ there is $N$ with $d(x_{n},x_{N})<\varepsilon/2$ for all $n\geq N$.

::: pf-proof
The Cauchy condition applied to $\varepsilon/2>0$ gives $N$ with $d(x_{m},x_{n})<\varepsilon/2$ whenever $m,n\geq N$; take $m=N$.
:::

:::

::: {.pf-step #a-tail}
The tail $\{x_{n}\mid n\geq N\}$ lies in $B(x_{N},\varepsilon)$, whose closure is compact.

::: pf-proof
For $n\geq N$, $d(x_{n},x_{N})<\varepsilon/2<\varepsilon$, so $x_{n}$ lies in the ball; its closure is compact by hypothesis.
:::

:::

::: {.pf-step #a-subsequence}
Some subsequence of $(x_{n})$ converges to a point $x\in X$.

::: pf-proof
$\overline{B(x_{N},\varepsilon)}$ is a compact metric space, hence sequentially compact (Theorem 28.2), so the sequence $x_{N},x_{N+1},\dots$ of its points has a subsequence converging to a point $x$ of it; that point lies in $X$ because the closure is a subset of $X$.
:::

:::

::: {.pf-step #a-converges}
The whole sequence converges to $x$.

::: pf-proof
Let $\eta>0$. Choose $N_{1}$ with $d(x_{m},x_{n})<\eta/2$ for $m,n\geq N_{1}$, then $k$ with $n_{k}\geq N_{1}$ and $d(x_{n_{k}},x)<\eta/2$. For $n\geq N_{1}$, $d(x_{n},x)\leq d(x_{n},x_{n_{k}})+d(x_{n_{k}},x)<\eta$.
:::

:::

::: {.pf-step #a}
If every $\varepsilon$-ball of $X$ has compact closure for some $\varepsilon>0$, then $X$ is complete.

::: pf-proof
Steps [](#a-cauchy){.pf-ref} to [](#a-converges){.pf-ref} show that every Cauchy sequence converges.
:::

:::

::: {.pf-step #b-local}
In $X=(0,1)$ with the usual metric every point has a ball with compact closure.

::: pf-proof
For $x\in(0,1)$ choose $0<r<\min\{x,1-x\}$, so $0<x-r$ and $x+r<1$. The ball $B(x,r)=(x-r,x+r)$ has closure $[x-r,x+r]$ in $X$, the endpoints lying in $(0,1)$, and that interval is compact.
:::

:::

::: {.pf-step #b-incomplete}
$X=(0,1)$ is not complete.

::: pf-proof
The sequence $x_{n}=1/(n+1)$ lies in $X$ and converges in $\RR$ to $0$, hence is Cauchy. It has no limit in $X$: a limit $x\in(0,1)$ would also be a limit in $\RR$, where limits are unique, forcing $x=0$.
:::

:::

::: {.pf-step #b}
The hypothesis of part (b) does not imply completeness.

::: pf-proof
Steps [](#b-local){.pf-ref} and [](#b-incomplete){.pf-ref} give a metric space with the local hypothesis which is not complete.
:::

:::

:::

:::
