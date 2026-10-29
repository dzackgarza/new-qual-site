---
schema: qual/card@1
id: P-WESRA10-II1
kind: problem
title: 'Borel–Cantelli without independence and a converse counterexample'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $(X,\mathcal B,\mu)$ be a measure space and let $(A_n)$ be measurable.

(a) Prove that if
\[
\sum_{n=1}^\infty\mu(A_n)<\infty,
\]
then the set of points belonging to infinitely many $A_n$ has measure zero.

(b) Give an example in which $\sum_n\mu(A_n)=\infty$ but the set of points belonging to infinitely many $A_n$ still has measure zero.
:::

::: {.solution}

::: pf

::: pf-step

The set of points that belong to infinitely many $A_n$ is
\[
\limsup_{n\to\infty}A_n
=\bigcap_{N=1}^\infty\bigcup_{n\ge N}A_n.
\]


::: pf-proof

A point lies in the right-hand side exactly when, for every $N$, it belongs
to some $A_n$ with $n\ge N$, which is equivalent to belonging to infinitely
many of the sets $A_n$.

:::

:::

::: {.pf-step #s1-2}

If
\[
\sum_{n=1}^\infty\mu(A_n)<\infty,
\]
then
\[
\boxed{\mu\!\left(\limsup_{n\to\infty}A_n\right)=0}.
\]


::: pf-proof

For every $N$,
\[
\limsup_{n\to\infty}A_n
\subseteq
\bigcup_{n\ge N}A_n.
\]
By monotonicity and countable subadditivity,
\[
\mu\!\left(\limsup_{n\to\infty}A_n\right)
\le
\mu\!\left(\bigcup_{n\ge N}A_n\right)
\le
\sum_{n\ge N}\mu(A_n).
\]
Since the series converges, its tails tend to $0$. Letting $N\to\infty$
gives the result.

:::

:::

::: {.pf-step #s1-3}

For part (b), take Lebesgue measure on $\RR$ and
\[
A_n=(0,1/n).
\]
Then
\[
\sum_{n=1}^\infty\mu(A_n)=\infty.
\]


::: pf-proof

Here
\[
\mu(A_n)=\frac1n,
\]
so the sum is the harmonic series and diverges.

:::

:::

::: {.pf-step #s1-4}

For the same example,
\[
\boxed{\limsup_{n\to\infty}A_n=\varnothing}.
\]


::: pf-proof

If $x\le0$, then $x$ belongs to no $A_n$. If $x>0$, choose
$N>1/x$. Then for all $n\ge N$,
\[
\frac1n<x,
\]
so $x\notin(0,1/n)=A_n$. Thus every point belongs to only finitely many
$A_n$, and the limsup is empty.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part (a), while steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} give the requested
counterexample in part (b).

:::

:::

:::
