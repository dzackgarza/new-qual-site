---
schema: qual/card@1
id: E-1QY2X
kind: problem
title: A flawed proof that the sphere is simply connected
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 59 Exercise 2, printed p. 370,
    with Theorem 57.3 and Theorem 59.3. The card names the flaw, that the flawed proof chooses a point of $S^2$ off the image of a loop, which a continuous loop need not miss; it justifies that with a space-filling curve and repairs the argument in the two ways available after this chapter. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
---

::: {.exercise}

Criticize the following "proof" that $S^2$ is simply connected.
Let $f$ be a loop in $S^2$ based at $x_0$.
Choose a point $p$ of $S^2$ not lying in the image of $f$.
Since $S^2 - \theset{p}$ is homeomorphic with $\RR^2$, and $\RR^2$ is simply connected, the loop $f$ is path homotopic to the constant loop.
:::

::: {.solution}

::: pf

::: pf-step

Identification of the logical fallacy:
    *The flaw:* The step *"Choose a point $p$ of $S^2$ not lying in the image of $f$"* assumes without justification that the continuous loop $f: [0, 1] \to S^2$ cannot be surjective.

:::

::: pf-step

Existence of space-filling curves:
    *Proof of non-triviality:*

::: pf-proof

::: pf-step

Continuous surjective paths exist: By Peano's Theorem, there exists a continuous surjective map from the unit interval $[0, 1]$ onto the unit square $[0, 1]^2$.

:::

::: pf-step

Post-compose with a continuous surjection $[0,1]^2\to S^2$ to obtain a surjective path $q:I\to S^2$. Choose a path $\alpha$ from the prescribed basepoint $x_0$ to $q(0)$. The loop $f=\alpha*q*\bar q*\bar\alpha$ is based at $x_0$ and has image $S^2$.

:::

::: pf-step

For such a space-filling loop, $S^2 \setminus \operatorname{im}(f) = \emptyset$. No such missing point $p$ exists, so the punctured-sphere homeomorphism $S^2 \setminus \{p\} \cong \RR^2$ cannot be directly applied to the loop $f$.

:::

:::

:::

::: pf-step

Rigorous resolution:

:::

:::

    To prove $\pi_1(S^2, x_0) = 0$ rigorously, one must circumvent this issue via either:
    1. **Homotopic Perturbation / Approximation:** Use the Lebesgue Covering Lemma on an open cover of small charts to approximate $f$ by a homotopic piecewise-linear or smooth loop $g \simeq f$ that is not surjective, and then contract $g$ in $S^2 \setminus \{p\} \cong \RR^2$.
    2. **Seifert-van Kampen Theorem:** Cover $S^2$ by two overlapping open hemispheres $U = S^2 \setminus \{(0, 0, 1)\}$ and $V = S^2 \setminus \{(0, 0, -1)\}$, each homeomorphic to $\RR^2$ (simply connected) with path-connected intersection $U \cap V \simeq S^1$, directly concluding $\pi_1(S^2) \cong \pi_1(U) \ast_{\pi_1(U \cap V)} \pi_1(V) = 0$. Q.E.D.
:::
