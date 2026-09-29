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

::: pf

::: {.pf-step #a-connected-in-closure}
Regard $A$ as a subspace of $\overline A$.
It is connected with this subspace topology.

::: pf-proof
The topology that $A$ inherits from $\overline A$ is the same as the topology that it inherits directly from $X$: if $U$ is open in $X$, then
\[
A\cap(U\cap\overline A)=A\cap U,
\]
because $A\subseteq\overline A$.
Thus the given connectedness of $A$ is unchanged when $A$ is viewed as a subspace of $\overline A$.
:::

:::

::: {.pf-step #assume-separation}
Suppose, for contradiction, that $\overline A$ is disconnected.
Then there are nonempty disjoint subsets $U,V\subseteq\overline A$ that are open in $\overline A$ and satisfy
\[
\overline A=U\cup V.
\]

::: pf-proof
This is exactly the definition of a separation of the subspace $\overline A$.
:::

:::

::: {.pf-step #a-subset-of-u}
The connected set $A$ is contained entirely in one of $U$ or $V$.

::: pf-proof
We have
\[
A=(A\cap U)\cup(A\cap V).
\]
The two sets on the right are disjoint and open in $A$, because $U$ and $V$ are open in $\overline A$.
If both were nonempty, they would separate $A$, contradicting step [](#a-connected-in-closure){.pf-ref}. Hence one is empty.
After interchanging $U$ and $V$ if necessary, assume
\[
A\subseteq U.
\]
:::

:::

::: {.pf-step #u-closed}
The set $U$ is closed in $\overline A$.

::: pf-proof
Since
\[
\overline A\setminus U=V
\]
and $V$ is open in $\overline A$, the set $U$ is closed in $\overline A$.
:::

:::

::: {.pf-step #closure-of-a-is-closure}
The closure of $A$ taken inside the subspace $\overline A$ is all of $\overline A$.

::: pf-proof
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

:::

::: {.pf-step #contradiction-reached}
The assumed separation is impossible.

::: pf-proof
By step [](#a-subset-of-u){.pf-ref}, $A\subseteq U$.
By step [](#u-closed){.pf-ref}, $U$ is closed in $\overline A$.
Therefore $U$ contains the closure of $A$ in $\overline A$.
By step [](#closure-of-a-is-closure){.pf-ref}, that closure is all of $\overline A$, so
\[
\overline A\subseteq U.
\]
Hence $U=\overline A$, forcing $V=\varnothing$, contrary to step [](#assume-separation){.pf-ref}.
:::

:::

::: pf-step
Therefore $\overline A$ is connected.

::: pf-proof
The assumption that $\overline A$ admits a separation leads to the contradiction in step [](#contradiction-reached){.pf-ref}. Thus no separation exists, so $\overline A$ is connected.
:::

:::

:::

:::
