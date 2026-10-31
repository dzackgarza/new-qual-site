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
Let $i\colon S^1\to S^1\vee S^1$ be the inclusion of the first circle and $j\colon S^1\to S^1\vee S^1$ the inclusion of the second, chosen so that the wedge point is the basepoint of all three spaces; write $\alpha=i_*(\omega)$ and $\beta=j_*(\omega)$ for the images of a generator $\omega$ of $\pi_1(S^1)$, and $\zeta$ for a generator of $\pi_1(S^1)$ at the target copy.

::: pf

::: {.pf-step #free}
$\pi_1(S^1\vee S^1)$ is the free group on the two generators $\alpha$ and $\beta$.

::: pf-proof
By Hatcher, *Algebraic Topology*, §1.2, Example 1.21, the fundamental group of a wedge of circles is the free product of the fundamental groups of the summands, so $\pi_1(S^1\vee S^1)\cong\ZZ*\ZZ$ with one free generator per circle, namely $\alpha$ and $\beta$.
The exercise stands in §1.1, before van Kampen's theorem is available, so this step is the later theorem used out of order; the problem cannot be solved inside §1.1's toolkit, since it needs two independent classes in $\pi_1(S^1\vee S^1)$.
:::

:::

::: {.pf-step #family}
For each $n\in\ZZ$ there is a retraction $r_n\colon S^1\vee S^1\to S^1$ with $(r_n)_*(\alpha)=\zeta$ and $(r_n)_*(\beta)=\zeta^n$.

::: pf-proof
Define $r_n$ to be the identity on the first circle and $z\mapsto z^n$ on the second; these agree at the wedge point, so $r_n$ is a well-defined continuous map, and it restricts to the identity on the first circle, which is the target.
Hence $r_n\circ i=\mathrm{id}_{S^1}$, and $r_n$ is a retraction.
On fundamental groups $(r_n)_*(\alpha)=\zeta$ because $r_n$ is the identity on the first circle, and $(r_n)_*(\beta)=\zeta^n$ because $z\mapsto z^n$ induces multiplication by $n$ on $\pi_1(S^1)$.
:::

:::

::: {.pf-step #distinct}
$r_m$ and $r_n$ are not homotopic when $m\ne n$.

::: pf-proof
Suppose $H\colon S^1\vee S^1\times I\to S^1$ is a homotopy, not necessarily based, from $r_m$ to $r_n$, and let $x_0$ be the wedge point.
The track $\gamma(t)=H(x_0,t)$ is a path in $S^1$ from $r_m(x_0)$ to $r_n(x_0)$, and by Hatcher, §1.1, Proposition 1.5, the induced homomorphisms satisfy
$$
(r_n)_*=\beta_\gamma\circ(r_m)_*
$$
as maps into $\pi_1(S^1,r_n(x_0))$.
The fundamental group of $S^1$ is abelian, so the basepoint-change isomorphism $\beta_\gamma$ is the identity after identifying both groups with $\ZZ$ through $\zeta$.
Applying the resulting equality to $\beta$ gives $\zeta^n=\zeta^m$, hence $n=m$.
:::

:::

::: {.pf-step #result}
The retractions $\{\,r_n:n\in\ZZ\,\}$ are pairwise nonhomotopic retractions $S^1\vee S^1\to S^1$, and there are infinitely many of them.

::: pf-proof
By step [](#family){.pf-ref} each $r_n$ is a retraction, and by step [](#distinct){.pf-ref} distinct indices give nonhomotopic maps.
The index $n$ ranges over the infinite set $\ZZ$, so the family is infinite.
:::

:::

:::
:::
