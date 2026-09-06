---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-03
kind: problem
title: Monotonicity of closure
classification:
  areas:
  - topology
  topics:
  - Closure
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part One, question 3 of the Topology Ph.D. Qualifying Exam dated January 17, 2009 in assets/attachments/F08phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Defined the closure as the intersection of all closed subsets of X
    containing A. Since B is one member of that family, the defining
    intersection is contained in B.
---

::: {.problem}
Define the term closure $\overline A$ of a subset $A$ of a topological space $X$.
Prove that if $B$ is a closed subset of $X$ such that $A\subset B$ then $\overline A\subset B$.
:::

::: {.solution}
<1>1. Define the closure of $A$ by
\[
\overline A
=\bigcap\{F\subseteq X:F\text{ is closed in }X\text{ and }A\subseteq F\}.
\]
Thus $\overline A$ is the smallest closed subset of $X$ containing $A$.
::: {.proof}
The family being intersected is nonempty because $X$ itself is closed and contains $A$.
An arbitrary intersection of closed sets is closed, so $\overline A$ is closed.
Every member of the family contains $A$, hence their intersection contains $A$.
Finally, if $F$ is any closed subset of $X$ containing $A$, then $F$ is one of the sets in the defining family, so
\[
\overline A\subseteq F.
\]
This proves the stated minimality.
:::

<1>2. If $B$ is closed and $A\subseteq B$, then
\[
\overline A\subseteq B.
\]
::: {.proof}
Since $B$ is closed and contains $A$, it belongs to the family of closed supersets occurring in the definition in <1>1. An intersection is contained in each set being intersected.
Therefore
\[
\overline A
=\bigcap\{F\subseteq X:F\text{ is closed and }A\subseteq F\}
\subseteq B.
\]
:::
:::
