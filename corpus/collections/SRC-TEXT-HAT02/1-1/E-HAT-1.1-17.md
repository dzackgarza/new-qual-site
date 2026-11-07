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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Checked against Hatcher, Algebraic Topology, Section 1.1, Exercise 17; the stored statement matches.
- event: solution-written
  by: claude
  date: 2026-10-31
  note: >-
    Rewrote the proof. The previous version opened by calling
    pi_1(S^1 vee S^1) = Z * Z a "standard computation" inside a one-line proof
    block, and closed with a pf-qed that only named earlier steps. The proof now
    cites Hatcher Section 1.2, Example 1.21 for the free product (the exercise
    itself sits in Section 1.1, before van Kampen), constructs the retractions,
    and carries the nonhomotopy argument in full sentences.
---

::: {.problem}
Construct infinitely many nonhomotopic retractions $S^1 \lor S^1 \longrightarrow S^1$.
:::

::: {.solution}
Let $i\colon S^1\to S^1\vee S^1$ be the inclusion of the first circle into the wedge, $j\colon S^1\to S^1\vee S^1$ the inclusion of the second, with the wedge point the basepoint of all three spaces, and let $\zeta$ be a generator of $\pi_1(S^1)$.

::: pf

::: {.pf-step #family}

For each $n\in\ZZ$ there is a retraction $r_n\colon S^1\vee S^1\to S^1$ restricting to the identity on the first circle and to $z\mapsto z^n$ on the second.

::: pf-proof

The two formulas agree at the wedge point, where $z=1$ and $z^n=1$, so they define a continuous map $r_n$ on the quotient space $S^1\vee S^1$.
Since $r_n\circ i=\mathrm{id}_{S^1}$, the map $r_n$ is a retraction onto the first circle.

:::

:::

::: {.pf-step #distinct}

$r_m$ and $r_n$ are not homotopic when $m\ne n$.

::: pf-proof

The composite $r_n\circ j:S^1\to S^1$ is $z\mapsto z^n$, and $(r_n\circ j)_*$ is multiplication by $n$ on $\pi_1(S^1)=\ZZ$ (Theorem 1.7, p. 29).
A homotopy $H:r_m\simeq r_n$ restricts to a homotopy from $r_m\circ j$ to $r_n\circ j$, so by Lemma 1.19 (p. 37) the induced homomorphisms satisfy $(r_n\circ j)_*=\beta_\gamma\circ(r_m\circ j)_*$ for the track $\gamma$ of the basepoint.
A basepoint-change map is conjugation (p. 28), and $\pi_1(S^1)$ is abelian, so $\beta_\gamma$ is the identity on $\ZZ$.
Hence multiplication by $m$ equals multiplication by $n$, that is $m=n$.

:::

:::

::: {.pf-step #result}

The retractions $\{\,r_n:n\in\ZZ\,\}$ are pairwise nonhomotopic, so there are infinitely many.

::: pf-proof

Each $r_n$ is a retraction by step [](#family){.pf-ref}, and distinct indices give nonhomotopic maps by step [](#distinct){.pf-ref}; the index set $\ZZ$ is infinite.

:::

:::

:::

:::
