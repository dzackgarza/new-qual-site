---
schema: qual/card@1
id: P-AZOFF-A06
kind: problem
title: Distance between disjoint compact sets is attained
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Compactness, connectedness, and functions of one real variable, Problem 6, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Minimized the continuous distance function on the compact product A x B.
    The extreme value theorem gives a pair attaining the infimum directly.
    The source compilation contains no worked solution for this problem.
---

::: {.problem}
Suppose $A$, $B$ are disjoint non-empty compact subsets of $\RR^n$. Prove that there exist $a \in A$ and $b \in B$ satisfying $\norm{a - b} = \inf \{ \norm{x - y} : x \in A, y \in B \}$.
:::

::: {.solution}
Define
$$
D:A\times B\longrightarrow\RR,
\qquad
D(x,y)=\norm{x-y}.
$$

<1>1. The space $A\times B$ is nonempty and compact, and $D$ is continuous.

::: {.proof}
The sets $A$ and $B$ are nonempty, so their product is nonempty. Since both
are compact subsets of $\RR^n$, their finite product $A\times B$ is compact.

The subtraction map
$$
(x,y)\longmapsto x-y
$$
is continuous, and the Euclidean norm is continuous. Hence their composition
$D$ is continuous.
:::

<1>2. There exist $a\in A$ and $b\in B$ such that
$$
\boxed{
\norm{a-b}
=
\inf\{\norm{x-y}:x\in A,\ y\in B\}
}.
$$

::: {.proof}
By step <1>1, $D$ is a continuous real-valued function on the nonempty compact
space $A\times B$. The extreme value theorem therefore gives
$$
(a,b)\in A\times B
$$
at which $D$ attains its minimum. Thus
$$
D(a,b)
=
\min_{(x,y)\in A\times B}D(x,y)
=
\inf_{(x,y)\in A\times B}D(x,y),
$$
which is the displayed equality.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 supplies the required points.
:::
:::
