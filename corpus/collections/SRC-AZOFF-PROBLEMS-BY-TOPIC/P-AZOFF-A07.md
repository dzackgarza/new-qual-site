---
schema: qual/card@1
id: P-AZOFF-A07
kind: problem
title: Union of intersecting connected sets is connected
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Compactness, connectedness, and functions of one real variable, Problem 7, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used the separation definition of connectedness. Any separation of A union
    B restricts to a separation of each connected subset, so A and B must each
    lie in one side; a point of A intersect B forces them into the same side,
    contradicting nonemptiness of the other side. The source compilation
    contains no worked solution for this problem.
---

::: {.problem}
Suppose $A$, $B$ are connected subsets of $\RR^n$ which are not disjoint.
Prove that their union $A \cup B$ is also connected.
:::

::: {.solution}
<1>1. Suppose, for contradiction, that $A\cup B$ is disconnected. Then there
are disjoint nonempty subsets $U,V\subseteq A\cup B$, open in the subspace
topology, such that
$$
A\cup B=U\cup V.
$$

::: {.proof}
This is the definition of disconnectedness.
:::

<1>2. The connected set $A$ is contained entirely in $U$ or entirely in $V$.

::: {.proof}
We have
$$
A=(A\cap U)\cup(A\cap V).
$$
The two sets on the right are disjoint and open in the subspace topology on
$A$. If both were nonempty, they would separate $A$, contradicting the
connectedness of $A$. Hence one is empty, so $A\subseteq U$ or $A\subseteq V$.
:::

<1>3. The connected set $B$ is contained entirely in $U$ or entirely in $V$.

::: {.proof}
The same argument as in step <1>2, applied to
$$
B=(B\cap U)\cup(B\cap V),
$$
uses the connectedness of $B$.
:::

<1>4. The sets $A$ and $B$ must lie in the same member of the separation.

::: {.proof}
Choose
$$
p\in A\cap B,
$$
which exists because $A$ and $B$ are not disjoint. Since $U$ and $V$ are
disjoint, the point $p$ belongs to exactly one of them. Steps <1>2--<1>3 then
force both $A$ and $B$ to lie in that same set.
:::

<1>5. The union $A\cup B$ is connected.

::: {.proof}
By step <1>4, either
$$
A\cup B\subseteq U
$$
or
$$
A\cup B\subseteq V.
$$
Since $A\cup B=U\cup V$, this makes the other member of the purported
separation empty, contradicting step <1>1. Therefore no separation exists,
so $A\cup B$ is connected.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
