---
schema: qual/card@1
id: P-VAJSW
kind: problem
title: Compact Hausdorff spaces are normal
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 2 of the official UGA Spring 2006 topology exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Repaired the compactness justification: F and G are compact because they
    are closed subsets of compact X, not because X is Hausdorff. Recast the
    finite-separation argument in proof blocks and handled the empty-set case.
---

::: {.problem}
Prove that every compact, Hausdorff topological space is normal.
:::

::: {.solution}
Let $F,G\subseteq X$ be disjoint closed subsets of a compact Hausdorff space $X$.

<1>1. It suffices to consider the case in which both $F$ and $G$ are nonempty, and in that case both are compact.
::: {.proof}
If one of $F,G$ is empty, then $\varnothing$ and $X$ are disjoint open neighborhoods of the two sets in the appropriate order.

Now assume $F,G\ne\varnothing$.
Since $F$ and $G$ are closed subsets of the compact space $X$, each is compact.
:::

<1>2. For every $x\in F$ there are disjoint open sets $U_x,V_x\subseteq X$ such that
\[
x\in U_x
\qquad\text{and}\qquad
G\subseteq V_x.
\]
::: {.proof}
Fix $x\in F$.
For each $y\in G$, Hausdorffness gives disjoint open neighborhoods
\[
x\in U_{x,y},
\qquad
y\in V_{x,y}.
\]
The family $\{V_{x,y}:y\in G\}$ is an open cover of the compact set $G$.
Choose $y_1,\ldots,y_r\in G$ such that
\[
G\subseteq\bigcup_{i=1}^r V_{x,y_i}.
\]
Set
\[
U_x=\bigcap_{i=1}^r U_{x,y_i},
\qquad
V_x=\bigcup_{i=1}^r V_{x,y_i}.
\]
These sets are open, $x\in U_x$, and $G\subseteq V_x$.

If $z\in U_x\cap V_x$, then $z\in V_{x,y_i}$ for some $i$, while $z\in U_x\subseteq U_{x,y_i}$.
This contradicts
\[
U_{x,y_i}\cap V_{x,y_i}=\varnothing.
\]
Thus $U_x\cap V_x=\varnothing$.
:::

<1>3. There are disjoint open sets $U,V\subseteq X$ with
\[
F\subseteq U,
\qquad
G\subseteq V.
\]
::: {.proof}
The sets $\{U_x:x\in F\}$ from <1>2 form an open cover of the compact set $F$.
Choose $x_1,\ldots,x_m\in F$ such that
\[
F\subseteq\bigcup_{j=1}^m U_{x_j}.
\]
Define
\[
U=\bigcup_{j=1}^m U_{x_j},
\qquad
V=\bigcap_{j=1}^m V_{x_j}.
\]
Both are open; $F\subseteq U$; and, since $G\subseteq V_{x_j}$ for every $j$, one has $G\subseteq V$.

If $z\in U\cap V$, then $z\in U_{x_j}$ for some $j$, while $z\in V\subseteq V_{x_j}$.
This contradicts $U_{x_j}\cap V_{x_j}=\varnothing$.
Hence $U\cap V=\varnothing$.
:::

<1>4. Therefore $X$ is normal.
::: {.proof}
The disjoint closed subsets $F,G$ were arbitrary, and <1>3 gives disjoint open neighborhoods of them.
This is the normality condition.
:::
:::
