---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F07-12
kind: problem
title: Separating a closed set and a compact set in a regular space
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part One, question 12 of the Topology Ph.D. Qualifying Exam in assets/attachments/F07phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Separated each point of the compact set from the closed set by disjoint
    open neighborhoods, extracted a finite subcover on the compact side, then
    used the union of the point neighborhoods and the finite intersection of
    the closed-set neighborhoods.
---

::: {.problem}
A topological space $X$ is said to be regular if disjoint singleton and closed sets can be separated by disjoint open sets.
Prove that in a regular space disjoint closed and compact sets can be separated by disjoint open sets.
:::

::: {.solution}
Let $F,K\subseteq X$ be disjoint, with $F$ closed and $K$ compact.

<1>1. For each $x\in K$, there are disjoint open sets $U_x,V_x\subseteq X$ such that
\[
x\in U_x
\qquad\text{and}\qquad
F\subseteq V_x.
\]
::: {.proof}
For each $x\in K$, disjointness of $F$ and $K$ gives
\[
x\notin F.
\]
Thus the singleton $\{x\}$ and the closed set $F$ are disjoint.
By regularity, they can be separated by disjoint open sets.
Hence there are open $U_x,V_x$ with
\[
x\in U_x,
\qquad
F\subseteq V_x,
\qquad
U_x\cap V_x=\varnothing.
\]
:::

<1>2. Finitely many of the sets $U_x$ cover $K$.
::: {.proof}
The family
\[
\{U_x:x\in K\}
\]
is an open cover of $K$ by <1>1.
Since $K$ is compact, there exist points
\[
x_1,\ldots,x_n\in K
\]
such that
\[
K\subseteq U_{x_1}\cup\cdots\cup U_{x_n}.
\]
:::

<1>3. Define
\[
U=U_{x_1}\cup\cdots\cup U_{x_n},
\qquad
V=V_{x_1}\cap\cdots\cap V_{x_n}.
\]
Then $U$ and $V$ are open, with
\[
K\subseteq U
\qquad\text{and}\qquad
F\subseteq V.
\]
::: {.proof}
The set $U$ is a finite union of open sets, hence open, and contains $K$ by <1>2.
The set $V$ is a finite intersection of open sets, hence open.
By <1>1, every $V_{x_i}$ contains $F$, so their intersection $V$ also contains $F$.
:::

<1>4. The open sets $U$ and $V$ are disjoint.
::: {.proof}
Suppose $y\in U\cap V$.
Since $y\in U$, there is some $i$ such that
\[
y\in U_{x_i}.
\]
Since $y\in V$, and
\[
V\subseteq V_{x_i},
\]
we also have $y\in V_{x_i}$.
This contradicts
\[
U_{x_i}\cap V_{x_i}=\varnothing
\]
from <1>1.
Therefore
\[
U\cap V=\varnothing.
\]
:::

<1>5. Hence the closed set $F$ and the compact set $K$ can be separated by disjoint open sets.
::: {.proof}
By <1>3, $U$ and $V$ are open neighborhoods of $K$ and $F$, respectively, and by <1>4 they are disjoint.
This is exactly the required separation.
:::
:::
