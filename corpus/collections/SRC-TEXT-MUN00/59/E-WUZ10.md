---
schema: qual/card@1
id: E-WUZ10
kind: problem
title: Two spheres touching at a point
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Let $X$ be the union of two copies of $S^2$ having a single point in common.
What is the fundamental group of $X$?
Prove that your answer is correct.
[Be careful! The union of two simply connected spaces having a point in common is not necessarily simply connected. See [S], p. 59.]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Open cover construction:

::: pf-proof

::: pf-step

Let $X = S_1 \cup S_2$ with $S_1 \cap S_2 = \{p\}$, where each $S_i \cong S^2$.
Choose points $q_1 \in S_1 \setminus \{p\}$ and $q_2 \in S_2 \setminus \{p\}$ (e.g. the antipodal points to $p$ on each sphere).

::: pf-proof

each $S_i \setminus \{p\}$ contains points distinct from $p$.

:::

:::

::: pf-step

Define the open sets in $X$:
\[
U = X \setminus \{q_1\} = (S_1 \setminus \{q_1\}) \cup S_2, \qquad V = X \setminus \{q_2\} = S_1 \cup (S_2 \setminus \{q_2\}).
\]
Since $\{q_1\}$ and $\{q_2\}$ are closed singletons in Hausdorff spaces, $U$ and $V$ are open in $X$, and $U \cup V = X \setminus \emptyset = X$.

::: pf-proof

complements of closed points in $X$ are open.

:::

:::

:::

:::

::: {.pf-step #s2}

Fundamental groups of $U, V$, and $U \cap V$:

::: pf-proof

::: {.pf-step #s2-1}

**Fundamental group of $U$:**
$S_1 \setminus \{q_1\}$ is homeomorphic to $\mathbb{R}^2$, which deformation retracts onto the point $p$.
This radial deformation retraction extends to $U$ by fixing $S_2$ pointwise.
Thus $S_2$ is a deformation retract of $U$, so:
\[
\pi_1(U, p) \cong \pi_1(S_2, p) \cong \pi_1(S^2) = 0.
\]

::: pf-proof

$\pi_1(S^2) = 0$ and homotopy invariance.

:::

:::

::: pf-step

**Fundamental group of $V$:**
Symmetrically, $V$ deformation retracts onto $S_1$, so:
\[
\pi_1(V, p) \cong \pi_1(S_1, p) \cong \pi_1(S^2) = 0.
\]

::: pf-proof

symmetry with step [](#s2-1){.pf-ref}.

:::

:::

::: pf-step

**Fundamental group of $U \cap V$:**
The intersection is $U \cap V = (S_1 \setminus \{q_1\}) \cup (S_2 \setminus \{q_2\})$.
Both pieces are homeomorphic to $\mathbb{R}^2$ and share the common point $p$.
The simultaneous radial retraction onto $p$ on each piece shows that $U \cap V$ deformation retracts to the point $\{p\}$.
Thus $U \cap V$ is contractible, hence path-connected with $\pi_1(U \cap V, p) = 0$.

::: pf-proof

union of two contractible open sets sharing a point.

:::

:::

:::

:::

::: {.pf-step #s3}

Seifert–van Kampen Theorem:

::: pf-proof

::: pf-step

Since $U$ and $V$ are open, $U \cup V = X$, and $U \cap V$ is path-connected, the Seifert–van Kampen Theorem gives:
\[
\pi_1(X, p) \cong \pi_1(U, p) *_{\pi_1(U \cap V, p)} \pi_1(V, p) \cong 0 *_0 0 = 0.
\]

::: pf-proof

Seifert–van Kampen Theorem for an open cover.

:::

:::

:::

:::

::: pf-step

Conclusion:
The fundamental group of the wedge sum of two 2-spheres is the trivial group: $\pi_1(X) \cong 0$. Q.E.D.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
