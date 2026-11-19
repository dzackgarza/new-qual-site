---
schema: qual/card@1
id: P-CFMLS
kind: problem
title: The set of reals with infinitely many rational approximations $\abs{x-p/q}<q^{-3}$ has measure zero
classification:
  areas:
  - real-analysis
  topics:
  - Borel-Cantelli
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the UGA Spring 2018 real-analysis qualifying exam recorded by SRC-UGA-RA-SPRING-2018.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Merged P-ULNGG, a statement reconstructed from a solutions-only document that restricts this problem to numerators 0<=p<=q; its solution proves only that special case and was not carried."
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. The collection is a course examination, so the problem
    statement is the source and the argument is the card's own. Two things are confirmed by hand.
    First, the count of intervals: if |x - p/q| < q^{-3} <= 1 and x in [-N,N] then 0 <= p <=
    (N+1)q, so E_{q,N} is a union of at most (N+1)q + 1 intervals, and the measure bound
    2(N+2)q^{-2} is summable; the earlier prose used Nq + 2, which undercounts by the additive
    term but gives the same conclusion, so the step now carries the correct bound and its
    derivation. Second, measurability of each E_{q,N} and the passage E = union over N of
    E cap [-N,N] are each made a step. Not claimed: any statement about the Hausdorff dimension
    of E, or about the exponent 3 being sharp.
---


::: {.problem}
Define
$$
E:=\left\{x\in\RR:\abs{x-\frac pq}<q^{-3}
\text{ for infinitely many }p,q\in\NN\right\}.
$$
Prove that $m(E)=0$.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card — the collection is a course examination, so the problem statement is the source.

::: pf

::: {.pf-step #sets}
For $N\ge1$ and $q\ge1$ put
$$
E_{q,N}=\Bigl\{x\in[-N,N]:\abs{x-\frac pq}<q^{-3}\ \text{for some }p\in\NN\Bigr\}.
$$
Each $E_{q,N}$ is a finite union of intervals, hence measurable.

::: pf-proof
$E_{q,N}$ is the union over $p$ of the open intervals $(\frac pq-q^{-3},\frac pq+q^{-3})\cap[-N,N]$; only finitely many $p$ give a nonempty intersection, by step [](#count){.pf-ref}. A finite union of intervals is a Borel set.
:::

:::

::: {.pf-step #count}
Only $0\le p\le(N+1)q$ can contribute to $E_{q,N}$, so $E_{q,N}$ is a union of at most $(N+1)q+1$ intervals of length $2q^{-3}$.

::: pf-proof
If $x\in[-N,N]$ and $\abs{x-p/q}<q^{-3}\le1$ then $p/q<x+1\le N+1$ and $p/q\ge x-1\ge-N-1$, so $0\le p\le(N+1)q$ since $p\in\NN$. That is at most $(N+1)q+1$ values of $p$, and the interval attached to $p$ has length $2q^{-3}$.
:::

:::

::: {.pf-step #measure}
$m(E_{q,N})\le 2(N+2)q^{-2}$, and $\sum_{q\ge1}m(E_{q,N})<\infty$.

::: pf-proof
By step [](#count){.pf-ref}, $m(E_{q,N})\le\bigl((N+1)q+1\bigr)\cdot2q^{-3}\le(N+2)q\cdot2q^{-3}=2(N+2)q^{-2}$ for $q\ge1$, using $1\le q$. The series $\sum_{q\ge1}2(N+2)q^{-2}$ converges, so the sum of the measures is finite.
:::

:::

::: {.pf-step #bc}
$m\Bigl(\limsup_{q}E_{q,N}\Bigr)=0$.

::: pf-proof
The sets are measurable by step [](#sets){.pf-ref} and the sum of their measures converges by step [](#measure){.pf-ref}; the first Borel--Cantelli lemma then gives that the set of points lying in infinitely many $E_{q,N}$ has measure zero.
:::

:::

::: {.pf-step #subset}
$E\cap[-N,N]\subseteq\limsup_{q}E_{q,N}$.

::: pf-proof
If $x\in E\cap[-N,N]$ then $\abs{x-p/q}<q^{-3}$ for infinitely many pairs $(p,q)$ with $p,q\in\NN$, hence for infinitely many $q$; for each of those, $x\in E_{q,N}$ by the definition. So $x$ lies in infinitely many of the sets $E_{q,N}$.
:::

:::

::: {.pf-step #union}
$m(E\cap[-N,N])=0$, and hence $m(E)=0$.

::: pf-proof
Step [](#subset){.pf-ref} with step [](#bc){.pf-ref} gives $m(E\cap[-N,N])\le m(\limsup_{q}E_{q,N})=0$. Finally $E=\bigcup_{N\ge1}(E\cap[-N,N])$ is a countable union of null sets, so by countable subadditivity $m(E)=0$:
$$
\boxed{m(E)=0.}
$$
:::

:::

:::
:::
