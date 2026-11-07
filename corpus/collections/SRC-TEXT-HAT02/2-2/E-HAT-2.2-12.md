---
schema: qual/card@1
id: E-HAT-2.2-12
kind: problem
title: Quotient map $S^1 \times S^1 \to S^2$ inducing isomorphism on $H_2$; all maps $S^2 \to S^1 \times S^1$ nullhomotopic
classification:
  areas:
  - topology
  topics:
  - Homology
  - Degree
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 12; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof checked via cellular homology, covering spaces, and degree.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both halves: collapsing the 1-skeleton collapses the boundary of the unique 2-cell, and
    the cellular chain map is the identity on $C_2$ while both differentials vanish, so $q_*$ is an
    isomorphism on $H_2$ and $q$ is not nullhomotopic; the lift to the universal cover $\RR^2$
    exists since $S^2$ is simply connected, and contractibility of $\RR^2$ together with the
    covering map gives the nullhomotopy.
---

::: {.problem}
Show that the quotient map $S^1 \times S^1 \to S^2$ collapsing the subspace $S^1 \lor S^1$ to a point is not nullhomotopic by showing that it induces an isomorphism on $H_2$.
On the other hand, show via covering spaces that any map $S^2 \to S^1 \times S^1$ is nullhomotopic.
:::

::: {.solution}
Let
$$
T^2=S^1\times S^1
$$
with its standard CW structure consisting of one $0$-cell, two $1$-cells, and one $2$-cell. Its $1$-skeleton is $S^1\vee S^1$.

::: pf

::: pf-step

Collapsing the $1$-skeleton gives
$$
T^2/(S^1\vee S^1)\cong S^2.
$$

::: pf-proof

The quotient collapses the boundary of the unique $2$-cell to a point, so the quotient of its closed characteristic disk is
$$
D^2/\partial D^2\cong S^2.
$$

:::

:::

::: pf-step

The quotient map
$$
q:T^2\to S^2
$$
induces an isomorphism on $H_2$.

::: pf-proof

The cellular chain complex of $T^2$ is
$$
0\to\ZZ\xrightarrow{0}\ZZ^2\xrightarrow{0}\ZZ\to0,
$$
so the unique $2$-cell represents a generator of $H_2(T^2)\cong\ZZ$ by Theorem 2.35 (p. 139), the same theorem that gives $H_2(S^2)\cong\ZZ$ for the quotient structure, which has the same unique $2$-cell and no $1$-cells. The cellular map induced by $q$ is the identity on the top cellular chain group $\ZZ$, hence
$$
q_*:H_2(T^2)\xrightarrow{\cong}H_2(S^2).
$$
A nullhomotopic map induces the same homomorphism on homology as a constant map (Theorem 2.10, p. 111), which is not surjective onto $S^2$ and so is zero on $H_2$ by property (b) of degree (p. 134); hence $q$ is not nullhomotopic.

:::

:::

::: pf-step

Every map
$$
f:S^2\to T^2
$$
is nullhomotopic.

::: pf-proof

The universal covering map
$$
p:\RR^2\to T^2
$$
has contractible total space, a contraction being $(x,t)\mapsto(1-t)x$. Since $S^2$ is simply connected by Proposition 1.14 (p. 35) and locally path-connected, the lifting criterion of Proposition 1.33 (p. 61) gives a lift
$$
\widetilde f:S^2\to\RR^2
$$
with $p\widetilde f=f$. The lift is nullhomotopic because $\RR^2$ is contractible. Composing such a nullhomotopy with $p$ gives a nullhomotopy of $f$.

:::

:::

:::

:::
