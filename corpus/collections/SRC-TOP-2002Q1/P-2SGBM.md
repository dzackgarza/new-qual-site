---
schema: qual/card@1
id: P-2SGBM
kind: problem
title: $\overline{U}\setminus U$ is nowhere dense for $U$ open
classification:
  areas:
  - topology
  topics:
  - Density
  - Closure
  - Point-Set Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked the statement against Section A, problem A2 of the January 18, 2002 topology qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Used only the closure-neighborhood criterion. The set is closed because U
    is open, and a nonempty open subset of its interior would simultaneously
    lie outside U and, as an open subset of cl(U), have to meet U.
---

::: {.problem}
Let $X$ be a topological space.
A set $A \subseteq X$ is called *nowhere dense* if the closure $\overline{A}$ of $A$ has empty interior, i.e., $\operatorname{int}(\overline{A}) = \varnothing$.
Show that if $U \subseteq X$ is open, then $A = \overline{U} \setminus U$ is nowhere dense.
:::

::: {.solution}
<1>1. The set
\[
A=\overline U\setminus U
\]
is closed in $X$, and therefore $\overline A=A$.
::: {.proof}
Since $U$ is open, $X\setminus U$ is closed.
Also $\overline U$ is closed by definition of closure.
Hence
\[
A=\overline U\cap(X\setminus U)
\]
is an intersection of closed sets, so it is closed.
Thus $\overline A=A$.
:::

<1>2. The interior of $A$ is empty.
::: {.proof}
Suppose instead that $\operatorname{int}(A)\neq\varnothing$.
Choose
\[
x\in\operatorname{int}(A)
\]
and put $V=\operatorname{int}(A)$.
Then $V$ is an open neighborhood of $x$ and
\[
V\subseteq A\subseteq\overline U.
\]
In particular $x\in\overline U$.
By the defining neighborhood characterization of closure, every open neighborhood of $x$ meets $U$; since $V$ is such a neighborhood,
\[
V\cap U\neq\varnothing.
\]
But also
\[
V\subseteq A=\overline U\setminus U\subseteq X\setminus U,
\]
so $V\cap U=\varnothing$, a contradiction.
Hence $\operatorname{int}(A)=\varnothing$.
:::

<1>3. Therefore $A$ is nowhere dense.
::: {.proof}
By <1>1 and <1>2,
\[
\operatorname{int}(\overline A)
=\operatorname{int}(A)
=\varnothing.
\]
This is precisely the definition of nowhere dense given in the problem.
:::
:::
