---
schema: qual/card@1
id: E-HAT-1.1-17
kind: exercise
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

Construct infinitely many nonhomotopic retractions $S^1 \lor S^1 \longrightarrow S^1$.

::: {.solution}
<1>1. $\pi_1(S^1 \vee S^1) = \ZZ * \ZZ = \langle a, b \rangle$ (free on two generators), and $\pi_1(S^1) = \ZZ$.
::: {.proof}
standard computation.
:::

<1>2. A retraction $r: S^1 \vee S^1 \to S^1$ induces a homomorphism $r_*: \ZZ * \ZZ \to \ZZ$ that is a retraction of the inclusion $i_*: \ZZ \to \ZZ * \ZZ$ (sending the generator of $\ZZ$ to $a$).
::: {.proof}
$r \circ i = \id_{S^1}$, so $r_* \circ i_* = \id$.
:::

<1>3. Hence $r_*(a) = 1$ (the generator of $\ZZ$), while $r_*(b)$ can be any integer $n$.
::: {.proof}
$r_*(a) = 1$ is forced by the retraction condition; $r_*(b) = n$ is arbitrary.
:::

<1>4. For each $n \in \ZZ$, define $r_n: S^1 \vee S^1 \to S^1$ by $r_n(a) = a$ (identity on the first circle) and $r_n(b) = a^n$ (the $n$-fold power on the second circle).
::: {.proof}
this is a well-defined continuous map (it is the identity on the first $S^1$ and the map $z \mapsto z^n$ on the second $S^1$).
:::

<1>5. Each $r_n$ is a retraction.
::: {.proof}
$r_n$ restricts to the identity on the first $S^1$ (the target).
:::

<1>6. The $r_n$ are pairwise nonhomotopic.
::: {.proof}
$r_n$ induces the homomorphism $a \mapsto 1$, $b \mapsto n$ on $\pi_1$; distinct $n$ give distinct homomorphisms, so the $r_n$ are pairwise nonhomotopic (homotopic maps induce equal homomorphisms on $\pi_1$).
:::

<1>7. Hence there are infinitely many nonhomotopic retractions.
::: {.proof}
<1>4–<1>6.
:::

<1>8. Q.E.D.
::: {.proof}
<1>7.
:::
:::
