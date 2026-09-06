---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F07-11
kind: problem
title: Connected components are connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part One, question 11 of the Topology Ph.D. Qualifying Exam in assets/attachments/F07phdtop.pdf.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Replaced the incorrect claim that both sides of a separation would contain
    the common point. If x lies in one side, each connected subset containing x
    must lie wholly in that side; taking the union then forces the other side
    to be empty.
---

::: {.problem}
Define the term “connected component” for a topological space.
Prove that a connected component is connected.
:::

::: {.solution}
Fix $x\in X$ and let
\[
\mathcal C_x
=\{C\subseteq X:C\text{ is connected and }x\in C\}.
\]
Define the connected component of $x$ to be
\[
K_x=\bigcup_{C\in\mathcal C_x}C.
\]

<1>1. The family $\mathcal C_x$ is nonempty.
::: {.proof}
The singleton $\{x\}$ is connected and contains $x$, so
\[
\{x\}\in\mathcal C_x.
\]
:::

<1>2. The set $K_x$ is connected.
::: {.proof}
Suppose, for contradiction, that
\[
K_x=U\cup V
\]
is a separation of $K_x$, so $U$ and $V$ are disjoint nonempty sets open in the subspace $K_x$.
By <1>1, $x\in K_x$.
Since $U$ and $V$ are disjoint and cover $K_x$, exactly one contains $x$; after interchanging them if necessary, assume
\[
x\in U.
\]

Take any $C\in\mathcal C_x$.
Then
\[
C=(C\cap U)\cup(C\cap V),
\]
where $C\cap U$ and $C\cap V$ are disjoint sets open in the subspace $C$.
Moreover,
\[
x\in C\cap U,
\]
so $C\cap U$ is nonempty.
Because $C$ is connected, $C\cap V$ must therefore be empty.
Hence
\[
C\subseteq U
\]
for every $C\in\mathcal C_x$.
Taking the union over all such $C$ gives
\[
K_x\subseteq U,
\]
so $V=\varnothing$, contradicting that $U,V$ form a separation.
Thus $K_x$ is connected.
:::

<1>3. The set $K_x$ is maximal among connected subsets of $X$ containing $x$.
::: {.proof}
Let $D\subseteq X$ be connected with
\[
K_x\subseteq D.
\]
Since $x\in K_x$, we have $x\in D$, and therefore
\[
D\in\mathcal C_x.
\]
By the definition of $K_x$ as the union of all members of $\mathcal C_x$,
\[
D\subseteq K_x.
\]
Together with $K_x\subseteq D$, this gives $D=K_x$.
Thus no strictly larger connected subset containing $x$ exists.
:::

<1>4. Consequently, connected components are exactly the maximal connected subsets of $X$, and every connected component is connected.
::: {.proof}
By <1>2--<1>3, $K_x$ is connected and maximal connected for every $x\in X$.
Conversely, if $M\subseteq X$ is maximal connected and $x\in M$, then $M\in\mathcal C_x$, so
\[
M\subseteq K_x.
\]
Since $K_x$ is connected by <1>2 and contains $M$, maximality of $M$ gives
\[
M=K_x.
\]
Hence the two standard descriptions agree, and in particular every connected component is connected.
:::
:::
