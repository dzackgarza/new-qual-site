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

::: pf

::: {.pf-step #s1}

Suppose, toward a contradiction, that $S$ is disconnected.
Then there are disjoint nonempty sets $U,V$ open in the subspace topology
on $S$ such that
$$
S=U\cup V.
$$

::: pf-proof

This is the definition of disconnectedness.

:::

:::

::: {.pf-step #s2}

After interchanging $U$ and $V$ if necessary, the origin lies in
$U$.

::: pf-proof

Every set $S_\alpha$ contains the origin, so
$$
0\in S.
$$
Since $S=U\cup V$ and $U,V$ are disjoint, the origin lies in exactly one of
them.

:::

:::

::: {.pf-step #s3}

For every index $\alpha$,
$$
S_\alpha\subseteq U.
$$

::: pf-proof

Fix $\alpha$. By step [](#s2){.pf-ref} and the common-point hypothesis,
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

:::

::: {.pf-step #s4}

One has
$$
V=\varnothing.
$$

::: pf-proof

By step [](#s3){.pf-ref},
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

:::

::: {.pf-step #s5}

The set
$$
\boxed{
\bigcup_\alpha S_\alpha
}
$$
is connected.

::: pf-proof

Step [](#s4){.pf-ref} contradicts the nonemptiness of $V$ in step [](#s1){.pf-ref}. Hence $S$
cannot be disconnected.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
