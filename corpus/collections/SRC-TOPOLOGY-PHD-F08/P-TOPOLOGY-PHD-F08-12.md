---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-12
kind: problem
title: Infinite sets and limit points in compact spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Limits
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part One, question 12 of the Topology Ph.D. Qualifying Exam dated January 17, 2009 in assets/attachments/F08phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Proved the statement without any separation axiom. If an infinite subset A
    had no limit point, every x would have a neighborhood meeting A in at most
    {x}. A finite subcover would then force A to lie in a finite set.
---

::: {.problem}
True or false: in a compact topological space every infinite set has a limit point.
Justify your answer.
:::

::: {.solution}
The statement is true.

<1>1. Let $A$ be an infinite subset of a compact space $X$ and suppose, for contradiction, that $A$ has no limit point.
Then for every $x\in X$ there is an open neighborhood $U_x$ of $x$ such that
\[
U_x\cap(A\setminus\{x\})=\varnothing.
\]
::: {.proof}
A point $x\in X$ is a limit point of $A$ if every open neighborhood of $x$ meets
\[
A\setminus\{x\}.
\]
If $x$ is not a limit point, the negation of this condition gives an open neighborhood $U_x$ with
\[
U_x\cap(A\setminus\{x\})=\varnothing.
\]
By the assumption that $A$ has no limit point, this holds for every $x\in X$.
:::

<1>2. The family
\[
\{U_x:x\in X\}
\]
is an open cover of $X$, so finitely many members
\[
U_{x_1},\ldots,U_{x_n}
\]
cover $X$.
::: {.proof}
Each $x$ belongs to its own neighborhood $U_x$, so the family covers $X$.
Compactness gives a finite subcover.
:::

<1>3. The finite subcover forces
\[
A\subseteq\{x_1,\ldots,x_n\}.
\]
::: {.proof}
Take $a\in A$.
Since the chosen neighborhoods cover $X$, there is an $i$ with
\[
a\in U_{x_i}.
\]
By <1>1,
\[
U_{x_i}\cap(A\setminus\{x_i\})=\varnothing.
\]
Because $a\in A\cap U_{x_i}$, it follows that
\[
a=x_i.
\]
Thus every point of $A$ lies among $x_1,\ldots,x_n$.
:::

<1>4. Therefore every infinite subset of a compact topological space has a limit point.
::: {.proof}
By <1>3, the assumption in <1>1 would make $A$ a subset of a finite set, hence finite, contradicting the hypothesis that $A$ is infinite.
Therefore $A$ must have a limit point.
:::
:::
