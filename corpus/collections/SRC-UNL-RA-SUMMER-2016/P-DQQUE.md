---
schema: qual/card@1
id: P-DQQUE
kind: problem
title: $\limsup a_k=\inf\{s:\text{only finitely many }a_k\ge s\}$
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked directly against Problem 2 of the preserved UNL May 2016 qualifying-exam source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Replaced the false claim that every tail supremum belongs to E; a constant sequence is a counterexample to that step.
---

::: {.problem}
Let $\{a_k\}_{k=1}^\infty$ be a bounded sequence of real numbers and set
\[
E:=\left\{s\in\mathbb R:\{k\in\mathbb N:a_k\ge s\}\text{ is finite}\right\}.
\]
Prove that
\[
\limsup_{k\to\infty}a_k=\inf E.
\]
:::

::: {.solution}
Let
\[
L:=\limsup_{k\to\infty}a_k
 =\lim_{N\to\infty}\sup_{k\ge N}a_k.
\]
Since $(a_k)$ is bounded above, $E\ne\varnothing$: every number larger than $\sup_k a_k$ lies in $E$.

<1>1. $L\le \inf E$.
::: {.proof}
Fix $s\in E$. By definition of $E$, there is $N$ such that
\[
a_k<s\qquad(k\ge N).
\]
Therefore
\[
\sup_{k\ge N}a_k\le s.
\]
Since the tail suprema decrease to $L$,
\[
L\le \sup_{k\ge N}a_k\le s.
\]
Thus $L$ is a lower bound for $E$, and hence $L\le\inf E$.
:::

<1>2. $\inf E\le L$.
::: {.proof}
Let $\varepsilon>0$. Since
\[
\sup_{k\ge N}a_k\downarrow L,
\]
there is $N$ such that
\[
\sup_{k\ge N}a_k<L+\varepsilon.
\]
Hence
\[
a_k<L+\varepsilon\qquad(k\ge N),
\]
so only the finitely many indices $k<N$ can satisfy $a_k\ge L+\varepsilon$. Therefore
\[
L+\varepsilon\in E.
\]
It follows that
\[
\inf E\le L+\varepsilon.
\]
Letting $\varepsilon\downarrow0$ gives $\inf E\le L$.
:::

Combining the two inequalities,
\[
\boxed{\limsup_{k\to\infty}a_k=\inf E}.
\]
:::
