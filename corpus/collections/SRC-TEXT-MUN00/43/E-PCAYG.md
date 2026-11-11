---
schema: qual/card@1
id: E-PCAYG
kind: problem
title: Banach fixed point theorem for contractions of complete metric spaces
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
- event: source-corrected
  by: gpt-6.1-sol
  date: 2026-10-31
  note: 'The printed fixed-point claim needs X nonempty; the empty metric space is complete and has no fixed point.'
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §43 Exercise 5 was located in any set searched; the search
    is recorded in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00, and the proof on the card is
    checked line by line against the book. Checked against Munkres, Topology (2000), §43 Exercise 5,
    printed p. 270, with the definition of a contraction stated in the exercise, the definition of
    completeness in §43, the triangle inequality, and the convergence of the geometric series in R
    (Theorem 43.2 for the completeness of R). The steps are the standard ones: d(x_{n+1},x_n) <=
    alpha^n d(x_1,x_0) by induction on the contraction inequality, the triangle inequality bounds
    d(x_m,x_n) for m > n by c alpha^n/(1-alpha), completeness gives the limit x, continuity of the
    Lipschitz map f gives f(x) = x, and uniqueness follows from d(x,y) <= alpha d(x,y) with alpha < 1.
    The hypothesis "nonempty" retained in the statement is the repair recorded in the source-corrected
    event above: without it the theorem is false at the empty metric space, which is complete and
    carries the unique map, and that map has no fixed point.
---

::: {.exercise}

If $(X, d)$ is a metric space, recall that a map $f: X \to X$ is called a contraction if there is a number $\alpha < 1$ such that

$$
d(f(x), f(y)) \leq \alpha \, d(x, y)
$$

for all $x, y \in X$.
Show that if $f$ is a contraction of a nonempty complete metric space, then there is a unique point $x \in X$ such that $f(x) = x$.
Compare [[E-70TGS]].
:::

::: {.solution}
Choose $x_0\in X$ and define
$$
x_{n+1}=f(x_n).
$$
If $c=d(x_1,x_0)$, repeated use of the contraction inequality gives
$$
d(x_{n+1},x_n)\le \alpha^n c.
$$
Hence for $m>n$,
$$
d(x_m,x_n)
\le\sum_{k=n}^{m-1}d(x_{k+1},x_k)
\le c\sum_{k=n}^{m-1}\alpha^k
\le \frac{c\alpha^n}{1-\alpha}.
$$
The right side tends to $0$, so $(x_n)$ is Cauchy. Completeness gives $x_n\to x\in X$.

The contraction inequality implies that $f$ is Lipschitz, hence continuous. Therefore
$$
f(x)=f\left(\lim_nx_n\right)
 =\lim_nf(x_n)
 =\lim_nx_{n+1}
 =x.
$$
Thus a fixed point exists.

If $x$ and $y$ are fixed points, then
$$
d(x,y)=d(f(x),f(y))\le\alpha d(x,y).
$$
Since $\alpha<1$, this forces $d(x,y)=0$, hence $x=y$. The fixed point is unique.
:::
