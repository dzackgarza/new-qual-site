---
schema: qual/card@1
id: E-HAT-1.1-17
kind: problem
title: Infinitely many nonhomotopic retractions $S^1 \lor S^1 \to S^1$
classification:
  areas:
  - topology
  topics:
  - Retractions
  - Fundamental Group
  - Free Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Construct infinitely many nonhomotopic retractions $S^1 \lor S^1 \longrightarrow S^1$.
:::

::: {.solution}

::: pf

::: pf-step

$\pi_1(S^1 \vee S^1) = \ZZ * \ZZ = \langle a, b \rangle$ (free on two generators), and $\pi_1(S^1) = \ZZ$.

::: pf-proof

standard computation.

:::

:::

::: pf-step

A retraction $r: S^1 \vee S^1 \to S^1$ induces a homomorphism $r_*: \ZZ * \ZZ \to \ZZ$ that is a retraction of the inclusion $i_*: \ZZ \to \ZZ * \ZZ$ (sending the generator of $\ZZ$ to $a$).

::: pf-proof

$r \circ i = \id_{S^1}$, so $r_* \circ i_* = \id$.

:::

:::

::: pf-step

Hence $r_*(a) = 1$ (the generator of $\ZZ$), while $r_*(b)$ can be any integer $n$.

::: pf-proof

$r_*(a) = 1$ is forced by the retraction condition; $r_*(b) = n$ is arbitrary.

:::

:::

::: {.pf-step #s4}

For each $n \in \ZZ$, define $r_n: S^1 \vee S^1 \to S^1$ by $r_n(a) = a$ (identity on the first circle) and $r_n(b) = a^n$ (the $n$-fold power on the second circle).

::: pf-proof

this is a well-defined continuous map (it is the identity on the first $S^1$ and the map $z \mapsto z^n$ on the second $S^1$).

:::

:::

::: {.pf-step #s5}

Each $r_n$ is a retraction.

::: pf-proof

$r_n$ restricts to the identity on the first $S^1$ (the target).

:::

:::

::: {.pf-step #s6}

The $r_n$ are pairwise nonhomotopic.

::: pf-proof

$r_n$ induces the homomorphism $a \mapsto 1$, $b \mapsto n$ on $\pi_1$; distinct $n$ give distinct homomorphisms, so the $r_n$ are pairwise nonhomotopic (homotopic maps induce equal homomorphisms on $\pi_1$).

:::

:::

::: {.pf-step #s7}

Hence there are infinitely many nonhomotopic retractions.

::: pf-proof

Steps [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref}.

:::

:::

:::
