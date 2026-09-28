---
schema: qual/card@1
id: P-AGXMISCIRROPENCONN
kind: problem
title: A space is irreducible exactly when its nonempty open subsets are connected
classification:
  areas:
  - algebraic-geometry
  topics:
  - Irreducibility
  - Connectedness
relations:
- kind: related-to
  target: P-AGHOPENDENSE
review: draft
audit:
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked both implications directly from the open-set characterization of
    irreducibility. In the converse, a decomposition X=F∪G produces the
    disconnected nonempty open subset X∖(F∩G).
---

::: {.problem}
Let $X \neq \emptyset$ be a topological space.
Prove that $X$ is irreducible if and only if every nonempty open subset of $X$ is connected.
:::

::: {.solution}
<1>1. If $X$ is irreducible, then any two nonempty open subsets of $X$
intersect.

::: {.proof}
Suppose $U,V\subseteq X$ are nonempty open subsets with
$$
U\cap V=\emptyset.
$$
Then
$$
X=(X\sm U)\cup(X\sm V),
$$
where both closed subsets are proper. This contradicts irreducibility.
:::

<1>2. If $X$ is irreducible, every nonempty open subset of $X$ is
connected.

::: {.proof}
Let
$$
\emptyset\ne U\subseteq X
$$
be open. Suppose $U$ were disconnected. Then there would be nonempty
disjoint subsets $A,B\subseteq U$, both open in $U$, with
$$
U=A\sqcup B.
$$
Because $U$ is open in $X$, the sets $A$ and $B$ are also open in $X$.
They are nonempty and disjoint, contradicting step <1>1. Hence $U$ is
connected.
:::

<1>3. Conversely, suppose every nonempty open subset of $X$ is connected.
Then $X$ is irreducible.

::: {.proof}
Suppose instead that
$$
X=F\cup G
$$
for proper closed subsets $F,G\subsetneq X$. Then
$$
A=X\sm F,
\qquad
B=X\sm G
$$
are nonempty open subsets of $X$. Moreover,
$$
A\cap B
=
X\sm(F\cup G)
=
\emptyset.
$$
Their union is
$$
A\cup B
=
X\sm(F\cap G),
$$
which is a nonempty open subset of $X$. Since $A$ and $B$ are disjoint
nonempty open subsets whose union is $A\cup B$, this open subset is
disconnected, contradicting the hypothesis.

Therefore no such decomposition $X=F\cup G$ exists, and $X$ is
irreducible.
:::

<1>4. Hence
$$
\boxed{
X\text{ is irreducible}
\iff
\text{every nonempty open subset of }X\text{ is connected}.
}
$$

::: {.proof}
Step <1>2 proves the forward implication and step <1>3 proves the reverse
implication.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is exactly the asserted equivalence.
:::
:::
