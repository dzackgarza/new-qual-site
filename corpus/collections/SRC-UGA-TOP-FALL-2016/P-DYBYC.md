---
schema: qual/card@1
id: P-DYBYC
kind: problem
title: Metric spaces are normal
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 2 of the official UGA Fall 2016 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the half-radius neighborhood construction and the triangle-inequality contradiction, including the empty-set cases.
---

::: {.problem}
Prove that a metric space $X$ is **normal**, i.e. if $A, B \subset X$ are closed and disjoint then there exist open sets $A \subset U \subset X, ~B \subset V \subset X$ such that $U \cap V = \emptyset$.
:::

::: {.solution}
Let $d$ be the metric on $X$, and let $A,B\subseteq X$ be disjoint closed sets.

<1>1. If $A=\emptyset$ or $B=\emptyset$, the required open neighborhoods exist.
::: {.proof}
If $A=\emptyset$, take
\[
U=\emptyset,
\qquad
V=X.
\]
If $B=\emptyset$, interchange the two choices.
Hence assume below that both $A$ and $B$ are nonempty.
:::

<1>2. For every $a\in A$, choose $\varepsilon_a>0$ such that
\[
B_d(a,\varepsilon_a)\cap B=\emptyset,
\]
and for every $b\in B$, choose $\delta_b>0$ such that
\[
B_d(b,\delta_b)\cap A=\emptyset.
\]
::: {.proof}
Because $B$ is closed, $X\setminus B$ is open and contains every $a\in A$.
Thus some metric ball centered at $a$ lies in $X\setminus B$.
The same argument with $A$ and $B$ interchanged gives the radii $\delta_b$.
:::

<1>3. Define
\[
U=\bigcup_{a\in A}B_d\left(a,\frac{\varepsilon_a}{2}\right),
\qquad
V=\bigcup_{b\in B}B_d\left(b,\frac{\delta_b}{2}\right).
\]
Then $U$ and $V$ are open, with
\[
A\subseteq U,
\qquad
B\subseteq V.
\]
::: {.proof}
Each metric ball is open, so both unions are open.
Every $a\in A$ belongs to its ball $B_d(a,\varepsilon_a/2)$, and every $b\in B$ belongs to $B_d(b,\delta_b/2)$.
:::

<1>4. The open sets $U$ and $V$ are disjoint.
::: {.proof}
Suppose instead that $z\in U\cap V$.
Then for some $a\in A$ and $b\in B$,
\[
d(a,z)<\frac{\varepsilon_a}{2},
\qquad
d(z,b)<\frac{\delta_b}{2}.
\]
The triangle inequality gives
\[
d(a,b)
\le d(a,z)+d(z,b)
<\frac{\varepsilon_a+\delta_b}{2}.
\]

If $\varepsilon_a\le\delta_b$, then
\[
d(a,b)<\delta_b,
\]
so $a\in B_d(b,\delta_b)$, contradicting the choice of $\delta_b$ in <1>2.
If $\delta_b\le\varepsilon_a$, then
\[
d(a,b)<\varepsilon_a,
\]
so $b\in B_d(a,\varepsilon_a)$, contradicting the choice of $\varepsilon_a$.
Thus $U\cap V=\emptyset$.
:::

<1>5. Therefore every metric space is normal.
::: {.proof}
For arbitrary disjoint closed subsets $A,B$, steps <1>1--<1>4 produce disjoint open neighborhoods $U\supseteq A$ and $V\supseteq B$, which is the stated definition of normality.
:::
:::
