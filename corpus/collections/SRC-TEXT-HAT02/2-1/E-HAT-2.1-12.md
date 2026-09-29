---
schema: qual/card@1
id: E-HAT-2.1-12
kind: problem
title: Chain homotopy is an equivalence relation
classification:
  areas:
  - topology
  topics:
  - Homology
  - Chain Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Show that chain homotopy of chain maps is an equivalence relation.
:::

::: {.solution}

::: pf

::: pf-step

Definition of chain homotopy:

::: pf-proof

::: pf-step

Let $(C_*, \partial^C)$ and $(D_*, \partial^D)$ be chain complexes. Two chain maps $f, g: C_* \to D_*$ are **chain homotopic** (denoted $f \simeq g$) if there exists a sequence of homomorphisms $P_n: C_n \to D_{n+1}$ such that:
\[
f_n - g_n = \partial^D_{n+1} P_n + P_{n-1} \partial^C_n \quad \text{for all } n \in \mathbb{Z}.
\]

::: pf-proof

standard definition of chain homotopy.

:::

:::

:::

:::

::: {.pf-step #s2}

Reflexivity:

::: pf-proof

::: pf-step

For any chain map $f: C_* \to D_*$, define $P_n = 0: C_n \to D_{n+1}$ for all $n$.
Then:
\[
\partial^D_{n+1} P_n + P_{n-1} \partial^C_n = 0 = f_n - f_n.
\]
Thus $f \simeq f$.

::: pf-proof

zero homomorphism satisfies the chain homotopy identity for $f - f = 0$.

:::

:::

:::

:::

::: {.pf-step #s3}

Symmetry:

::: pf-proof

::: pf-step

Suppose $f \simeq g$ via chain homotopy $P = \{P_n\}$.
Then $f_n - g_n = \partial^D_{n+1} P_n + P_{n-1} \partial^C_n$.
Define $Q_n = -P_n: C_n \to D_{n+1}$.
Then:
\[
g_n - f_n = -(f_n - g_n) = -\big(\partial^D_{n+1} P_n + P_{n-1} \partial^C_n\big) = \partial^D_{n+1} (-P_n) + (-P_{n-1}) \partial^C_n = \partial^D_{n+1} Q_n + Q_{n-1} \partial^C_n.
\]
Thus $g \simeq f$.

::: pf-proof

linearity of boundary operators and negation.

:::

:::

:::

:::

::: {.pf-step #s4}

Transitivity:

::: pf-proof

::: pf-step

Suppose $f \simeq g$ via chain homotopy $P = \{P_n\}$ and $g \simeq h$ via chain homotopy $Q = \{Q_n\}$.
Then:
\[
f_n - g_n = \partial^D_{n+1} P_n + P_{n-1} \partial^C_n \quad \text{and} \quad g_n - h_n = \partial^D_{n+1} Q_n + Q_{n-1} \partial^C_n.
\]

::: pf-proof

definitions of $P$ and $Q$.

:::

:::

::: pf-step

Define $R_n = P_n + Q_n: C_n \to D_{n+1}$.
Adding the two equations yields:
\[
f_n - h_n = (f_n - g_n) + (g_n - h_n) = \partial^D_{n+1} (P_n + Q_n) + (P_{n-1} + Q_{n-1}) \partial^C_n = \partial^D_{n+1} R_n + R_{n-1} \partial^C_n.
\]
Thus $f \simeq h$.

::: pf-proof

linearity of boundary operators.

:::

:::

:::

:::

::: pf-step

Conclusion:
Chain homotopy is reflexive, symmetric, and transitive; hence it is an equivalence relation on chain maps. Q.E.D.

::: pf-proof

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

:::

:::
