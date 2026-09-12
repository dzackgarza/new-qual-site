---
schema: qual/card@1
id: P-TOP-WORKSHOP-D2-W2
kind: problem
title: Path-connected spaces are connected (workshop warm-up)
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
  note: Checked against the second warm-up in assets/attachments/Day_2_-_Connectedness_Problems.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
If $X$ is a path connected space, then $X$ is connected.
:::

::: {.solution}
<1>1. The interval $[0,1]$ is connected.
::: {.proof}
Suppose instead that
\[
[0,1]=U\cup V
\]
with $U$ and $V$ disjoint nonempty sets open in the subspace topology.
Choose $u\in U$ and $v\in V$ with $u<v$ after exchanging the names if necessary.
Let
\[
s=\sup\bigl(U\cap[u,v]\bigr).
\]
Then $u\le s\le v$.

If $s\in U$, openness of $U$ gives an interval around $s$ contained in $U$ relative to $[0,1]$; since $s<v$, this produces a point of $U\cap[u,v]$ larger than $s$, contradicting the definition of $s$.
Thus $s\notin U$, so $s\in V$.
Openness of $V$ gives an interval around $s$ contained in $V$ relative to $[0,1]$.
By the definition of supremum, there is a point of $U\cap[u,v]$ arbitrarily close to $s$ from below, hence inside that interval, contradicting $U\cap V=\varnothing$.
Therefore no such separation exists.
:::

<1>2. Suppose for contradiction that the path-connected space $X$ is disconnected.
Then there are disjoint nonempty open sets $U,V\subseteq X$ with
\[
X=U\cup V.
\]
::: {.proof}
This is the definition of disconnectedness.
:::

<1>3. Choose $x\in U$ and $y\in V$, and let
\[
\gamma:[0,1]\to X
\]
be a path from $x$ to $y$.
::: {.proof}
The sets $U$ and $V$ are nonempty, and path connectedness supplies a path between any two points of $X$.
:::

<1>4. The sets $\gamma^{-1}(U)$ and $\gamma^{-1}(V)$ form a separation of $[0,1]$.
::: {.proof}
They are open because $\gamma$ is continuous.
They are disjoint because $U$ and $V$ are disjoint, and together they cover $[0,1]$ because $U\cup V=X$.
They are both nonempty since
\[
0\in\gamma^{-1}(U),
\qquad
1\in\gamma^{-1}(V).
\]
:::

<1>5. This contradicts <1>1, so $X$ is connected.
::: {.proof}
The separation in <1>4 cannot exist because $[0,1]$ is connected.
:::
:::
