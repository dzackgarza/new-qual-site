---
schema: qual/card@1
id: P-BKS10-9B
kind: problem
title: Ramsey bound $R(m+1,n+1)\le\binom{m+n}{m}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2010 preliminary-exam solution packet, which reproduces the problem statement before its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the Pascal-identity neighbor threshold, both induction branches, and the boundary cases.
---

::: {.problem}
Prove that if every edge of the complete graph on
$$
\binom{m+n}{m}
$$
vertices is colored red or blue, then there is either a complete red subgraph on $m+1$ vertices or a complete blue subgraph on $n+1$ vertices.

Hint: choose a vertex, partition the remaining vertices according to the color of their edge to it, and induct on $m+n$.
:::

::: {.solution}

::: pf

::: {.pf-step #boundary-case}
If $m=0$ or $n=0$, the assertion holds.

::: pf-proof
If $m=0$, then a complete red subgraph on
$$
m+1=1
$$
vertex is just any vertex. Similarly, if $n=0$, any vertex is a complete
blue subgraph on $n+1=1$ vertex.
:::

:::

::: {.pf-step #partition-bound}
Suppose $m,n>0$ and set
$$
N\coloneqq\binom{m+n}{m}.
$$
For any chosen vertex $v$, let $R$ be the set of vertices joined to $v$ by
a red edge and $B$ the set joined to $v$ by a blue edge. Then either
$$
\abs{R}
\geq
\binom{m+n-1}{m-1}
$$
or
$$
\abs{B}
\geq
\binom{m+n-1}{m}.
$$

::: pf-proof
The sets $R$ and $B$ partition the other $N-1$ vertices, so
$$
\abs{R}+\abs{B}=N-1.
$$
Pascal's identity gives
$$
N
=
\binom{m+n-1}{m-1}
+
\binom{m+n-1}{m}.
$$
If both displayed lower bounds failed, integrality would give
$$
\abs{R}
\leq
\binom{m+n-1}{m-1}-1
$$
and
$$
\abs{B}
\leq
\binom{m+n-1}{m}-1.
$$
Adding would yield
$$
\abs{R}+\abs{B}\leq N-2,
$$
contradicting $\abs{R}+\abs{B}=N-1$.
:::

:::

::: {.pf-step #red-branch}
Assume inductively that the theorem holds for every pair of
nonnegative integers whose sum is less than $m+n$. If
$$
\abs{R}
\geq
\binom{m+n-1}{m-1},
$$
then the desired red or blue clique exists.

::: pf-proof
Choose a subset
$$
R_0\subseteq R
$$
with
$$
\abs{R_0}
=
\binom{m+n-1}{m-1}
=
\binom{(m-1)+n}{m-1}.
$$
Apply the induction hypothesis to the complete graph on $R_0$ with
parameters $m-1$ and $n$. It contains either a complete red subgraph on
$m$ vertices or a complete blue subgraph on $n+1$ vertices.

In the blue case the required blue clique already exists. In the red case,
every vertex of that red $m$-clique lies in $R$, so all its edges to $v$
are red. Adding $v$ produces a complete red subgraph on $m+1$ vertices.
:::

:::

::: {.pf-step #blue-branch}
Under the same induction hypothesis, if
$$
\abs{B}
\geq
\binom{m+n-1}{m},
$$
then the desired red or blue clique exists.

::: pf-proof
Choose
$$
B_0\subseteq B
$$
with
$$
\abs{B_0}
=
\binom{m+n-1}{m}
=
\binom{m+(n-1)}{m}.
$$
Apply the induction hypothesis with parameters $m$ and $n-1$. The complete
graph on $B_0$ contains either a complete red subgraph on $m+1$ vertices
or a complete blue subgraph on $n$ vertices.

In the red case the required red clique already exists. In the blue case,
all edges from $v$ to that blue $n$-clique are blue because its vertices
lie in $B$. Adding $v$ produces a complete blue subgraph on $n+1$
vertices.
:::

:::

::: {.pf-step #induction-complete}
The theorem holds for all nonnegative integers $m,n$.

::: pf-proof
Proceed by induction on $m+n$. Step [](#boundary-case){.pf-ref} supplies the boundary cases. For
$m,n>0$, step [](#partition-bound){.pf-ref} guarantees that one of the hypotheses of step [](#red-branch){.pf-ref} or
step [](#blue-branch){.pf-ref} holds, and either step yields the required clique. This completes
the induction.
:::

:::

::: pf-qed
Step [](#induction-complete){.pf-ref} gives the asserted red $K_{m+1}$ or blue $K_{n+1}$ in every
two-coloring of the edges of the specified complete graph.
:::

:::

:::
