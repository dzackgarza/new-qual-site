---
schema: qual/card@1
id: P-TOP-WORKSHOP-D2-W1
kind: problem
title: A connected space has only trivial clopen sets (workshop warm-up)
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: >-
    Checked against the first warm-up in assets/attachments/Day_2_-_Connectedness_Problems.pdf.
    The source includes a stray initial "If"; the intended biconditional is clear from context.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
If $X$ is a connected space if and only if $X$ and the empty set are the only open and closed sets.
:::

::: {.solution}
We interpret the printed sentence as the standard biconditional: $X$ is connected if and only if the only subsets of $X$ that are both open and closed are $\varnothing$ and $X$.

<1>1. Suppose $X$ is connected, and let $C\subseteq X$ be both open and closed.
Then $C=\varnothing$ or $C=X$.
::: {.proof}
Because $C$ is closed, its complement $X\setminus C$ is open.
If both $C$ and $X\setminus C$ were nonempty, then
\[
X=C\cup(X\setminus C)
\]
would be a union of two disjoint nonempty open sets, which would disconnect $X$.
Thus one of them is empty, giving $C=\varnothing$ or $C=X$.
:::

<1>2. Conversely, suppose $\varnothing$ and $X$ are the only clopen subsets of $X$.
Then $X$ is connected.
::: {.proof}
Assume for contradiction that $X$ is disconnected.
Then there are disjoint nonempty open sets $U,V\subseteq X$ with
\[
X=U\cup V.
\]
Since $X\setminus U=V$ is open, $U$ is closed as well as open.
Thus $U$ is a nontrivial clopen subset of $X$, contradicting the hypothesis.
:::

<1>3. Hence the two conditions are equivalent.
::: {.proof}
The forward implication is <1>1 and the reverse implication is <1>2.
:::
:::
