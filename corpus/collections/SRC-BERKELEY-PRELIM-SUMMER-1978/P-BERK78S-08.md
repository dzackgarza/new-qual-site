---
schema: qual/card@1
id: P-BERK78S-08
kind: problem
title: A union of connected sets with a common point is connected
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
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Argued by contradiction from a separation U∪V of the union. The common
    origin lies in one side, say U. Each connected S_alpha meets U and
    therefore cannot also meet V, so every S_alpha is contained in U; this
    forces V to be empty.
---

::: {.problem}
Let $\{S_\alpha\}$ be a family of connected subsets of $\mathbb R^2$, all containing the origin. Prove that
\[
\bigcup_\alpha S_\alpha
\]
is connected.
:::

::: {.solution}
Set
$$
S=\bigcup_\alpha S_\alpha.
$$

<1>1. Suppose, toward a contradiction, that $S$ is disconnected.
Then there are disjoint nonempty sets $U,V$ open in the subspace topology
on $S$ such that
$$
S=U\cup V.
$$

::: {.proof}
This is the definition of disconnectedness.
:::

<1>2. After interchanging $U$ and $V$ if necessary, the origin lies in
$U$.

::: {.proof}
Every set $S_\alpha$ contains the origin, so
$$
0\in S.
$$
Since $S=U\cup V$ and $U,V$ are disjoint, the origin lies in exactly one of
them.
:::

<1>3. For every index $\alpha$,
$$
S_\alpha\subseteq U.
$$

::: {.proof}
Fix $\alpha$. By step <1>2 and the common-point hypothesis,
$$
0\in S_\alpha\cap U,
$$
so $S_\alpha\cap U$ is nonempty.

Because $U$ and $V$ are open in $S$, the sets
$$
S_\alpha\cap U
\qquad\text{and}\qquad
S_\alpha\cap V
$$
are open in the subspace topology on $S_\alpha$. They are disjoint and
their union is $S_\alpha$. If $S_\alpha\cap V$ were nonempty, they would
form a separation of the connected set $S_\alpha$. Therefore
$$
S_\alpha\cap V=\varnothing,
$$
and hence $S_\alpha\subseteq U$.
:::

<1>4. One has
$$
V=\varnothing.
$$

::: {.proof}
By step <1>3,
$$
S
=
\bigcup_\alpha S_\alpha
\subseteq
U.
$$
But
$$
S=U\cup V
$$
with $U$ and $V$ disjoint. Therefore $V$ contains no point of $S$, so
$V=\varnothing$.
:::

<1>5. The set
$$
\boxed{
\bigcup_\alpha S_\alpha
}
$$
is connected.

::: {.proof}
Step <1>4 contradicts the nonemptiness of $V$ in step <1>1. Hence $S$
cannot be disconnected.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
