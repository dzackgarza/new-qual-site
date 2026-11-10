---
schema: qual/card@1
id: E-3SU0X
kind: problem
title: Quotient topology on a three-point image of the line
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §22 Exercise 1, printed p. 144, with Example 3 of
    §22 and its Figure 22.3; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 22.1, PDF p. 27. The six preimages are computed
    and the three that are open in R give the topology {empty, A, {a}, {b}, {a,b}}, which is
    the one in Figure 22.3. The published list of proper subsets of A is printed with {a,b}
    replaced by {a,c} twice; the card lists all six. (tmp/sources/munkres-solutions-
    positron-ch2.pdf).
---

::: {.exercise}

Check the details of Example 3 of §22: for the map $p: \RR \to A = \theset{a, b, c}$ defined by

$$
p(x) =
\begin{cases}
a & \text{if } x > 0, \\
b & \text{if } x < 0, \\
c & \text{if } x = 0,
\end{cases}
$$

determine the quotient topology on $A$ induced by $p$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 22.1, PDF p. 27** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the computation of the six preimages is theirs, with the list of subsets of $A$ corrected.

Let $p:\RR\to A=\{a,b,c\}$ be $p(x)=a$ for $x>0$, $p(x)=b$ for $x<0$ and $p(0)=c$. A subset $U\subset A$ is open in the quotient topology exactly when $p^{-1}(U)$ is open in $\RR$. The six proper nonempty subsets of $A$ give
$$
p^{-1}(\{a\})=(0,\infty),\quad p^{-1}(\{b\})=(-\infty,0),\quad p^{-1}(\{a,b\})=\RR-\{0\},
$$
$$
p^{-1}(\{c\})=\{0\},\quad p^{-1}(\{a,c\})=[0,\infty),\quad p^{-1}(\{b,c\})=(-\infty,0].
$$
The first three are open in $\RR$ and the last three are not. Adding $\varnothing$ and $A$, whose preimages are $\varnothing$ and $\RR$, the quotient topology is
$$
\mathcal{T}=\big\{\varnothing,\ A,\ \{a\},\ \{b\},\ \{a,b\}\big\},
$$
which is the topology drawn in Figure 22.3 of §22.
:::
