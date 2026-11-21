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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 2.1, Exercise 12.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the three properties: the zero homotopy, the negated homotopy for symmetry, and the sum of two homotopies for transitivity, each verified against the defining equation.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 12 of §2.1, printed p. 131. Correct: with the defining identity
    $f_n-g_n=d_DP_n+P_{n-1}d_C$, the zero family is a homotopy from a map to itself, $-P$ reverses
    one, and $P+Q$ composes two. Removed one thing only: a closing step that restated the
    conclusion and was proved by naming the three steps above it, which STYLE-08 forbids; the three
    substantive steps remain and the statement is unchanged. Not claimed: a published solution,
    and no certificate.
---

::: {.problem}
Show that chain homotopy of chain maps is an equivalence relation.
:::

::: {.solution}
Fix chain complexes $(C_*,d_C)$ and $(D_*,d_D)$. A chain homotopy from $f$ to $g$ is a degree-one family $P_n:C_n\to D_{n+1}$ satisfying
$$
f_n-g_n=d_D P_n+P_{n-1}d_C
$$
in every degree.

::: pf

::: {.pf-step #s1}

Chain homotopy is reflexive.

::: pf-proof

For any chain map $f$, take $P_n=0$ in every degree. Then $f_n-f_n=d_D P_n+P_{n-1}d_C=0$.

:::

:::

::: {.pf-step #s2}

Chain homotopy is symmetric.

::: pf-proof

If $P$ is a chain homotopy from $f$ to $g$, then
$$
g_n-f_n=d_D(-P_n)+(-P_{n-1})d_C.
$$
Thus $-P$ is a chain homotopy from $g$ to $f$.

:::

:::

::: {.pf-step #s3}

Chain homotopy is transitive.

::: pf-proof

If $P$ is a chain homotopy from $f$ to $g$ and $Q$ is one from $g$ to $h$, add their defining identities:
$$
f_n-h_n=d_D(P_n+Q_n)+(P_{n-1}+Q_{n-1})d_C.
$$
Thus $P+Q$ is a chain homotopy from $f$ to $h$.

:::

:::

:::
:::
