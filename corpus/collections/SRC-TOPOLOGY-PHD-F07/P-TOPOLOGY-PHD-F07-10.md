---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F07-10
kind: problem
title: The closure of a connected set is connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Closure
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part One, question 10 of the Topology Ph.D. Qualifying Exam in assets/attachments/F07phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Argued by contradiction from a separation of the closure. Connectedness
    forces A into one side; that side is closed in the closure, so it must also
    contain the closure of A, contradicting nonemptiness of the other side.
---

::: {.problem}
Let $X$ be a topological space.
Let $A\subset X$ be connected.
Prove that the closure $\overline A$ of $A$ is connected.
:::

::: {.solution}
<1>1. Regard $A$ as a subspace of $\overline A$.
It is connected with this subspace topology.
::: {.proof}
The topology that $A$ inherits from $\overline A$ is the same as the topology that it inherits directly from $X$: if $U$ is open in $X$, then
\[
A\cap(U\cap\overline A)=A\cap U,
\]
because $A\subseteq\overline A$.
Thus the given connectedness of $A$ is unchanged when $A$ is viewed as a subspace of $\overline A$.
:::

<1>2. Suppose, for contradiction, that $\overline A$ is disconnected.
Then there are nonempty disjoint subsets $U,V\subseteq\overline A$ that are open in $\overline A$ and satisfy
\[
\overline A=U\cup V.
\]
::: {.proof}
This is exactly the definition of a separation of the subspace $\overline A$.
:::

<1>3. The connected set $A$ is contained entirely in one of $U$ or $V$.
::: {.proof}
We have
\[
A=(A\cap U)\cup(A\cap V).
\]
The two sets on the right are disjoint and open in $A$, because $U$ and $V$ are open in $\overline A$.
If both were nonempty, they would separate $A$, contradicting <1>1.
Hence one is empty.
After interchanging $U$ and $V$ if necessary, assume
\[
A\subseteq U.
\]
:::

<1>4. The set $U$ is closed in $\overline A$.
::: {.proof}
Since
\[
\overline A\setminus U=V
\]
and $V$ is open in $\overline A$, the set $U$ is closed in $\overline A$.
:::

<1>5. The closure of $A$ taken inside the subspace $\overline A$ is all of $\overline A$.
::: {.proof}
The closure of a subset $B\subseteq Z\subseteq X$ in the subspace $Z$ is
\[
\operatorname{Cl}_Z(B)=Z\cap\operatorname{Cl}_X(B).
\]
Taking $B=A$ and $Z=\overline A$ gives
\[
\operatorname{Cl}_{\overline A}(A)
=\overline A\cap\operatorname{Cl}_X(A)
=\overline A\cap\overline A
=\overline A.
\]
:::

<1>6. The assumed separation is impossible.
::: {.proof}
By <1>3, $A\subseteq U$.
By <1>4, $U$ is closed in $\overline A$.
Therefore $U$ contains the closure of $A$ in $\overline A$.
By <1>5, that closure is all of $\overline A$, so
\[
\overline A\subseteq U.
\]
Hence $U=\overline A$, forcing $V=\varnothing$, contrary to <1>2.
:::

<1>7. Therefore $\overline A$ is connected.
::: {.proof}
The assumption that $\overline A$ admits a separation leads to the contradiction in <1>6.
Thus no separation exists, so $\overline A$ is connected.
:::
:::
