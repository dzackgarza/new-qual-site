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
---

::: {.exercise}

Criticize the following "proof" that $S^2$ is simply connected.
Let $f$ be a loop in $S^2$ based at $x_0$.
Choose a point $p$ of $S^2$ not lying in the image of $f$.
Since $S^2 - \ts{p}$ is homeomorphic with $\mathbb{R}^2$, and $\mathbb{R}^2$ is simply connected, the loop $f$ is path homotopic to the constant loop.
:::

::: solution
**Goal:** Identify and critique the fundamental flaw in the proposed proof that $S^2$ is simply connected, and explain how the gap is rigorously resolved.

<1>1. Identification of the logical fallacy:
    *The flaw:* The step *"Choose a point $p$ of $S^2$ not lying in the image of $f$"* assumes without justification that the continuous loop $f: [0, 1] \to S^2$ cannot be surjective.

<1>2. Existence of space-filling curves:
    *Proof of non-triviality:*
    <2>1. Continuous surjective paths exist: By Peano's Theorem, there exists a continuous surjective map from the unit interval $[0, 1]$ onto the unit square $[0, 1]^2$.
    <2>2. By post-composing with the standard quotient map $[0, 1]^2 \to S^2$, one can construct a continuous closed loop $f: [0, 1] \to S^2$ whose image is the entire 2-sphere, $\operatorname{im}(f) = S^2$.
    <2>3. For such a space-filling loop, $S^2 \setminus \operatorname{im}(f) = \emptyset$. No such missing point $p$ exists, so the punctured-sphere homeomorphism $S^2 \setminus \{p\} \cong \mathbb{R}^2$ cannot be directly applied to the loop $f$.

<1>3. Rigorous resolution:
    To prove $\pi_1(S^2, x_0) = 0$ rigorously, one must circumvent this issue via either:
    1. **Homotopic Perturbation / Approximation:** Use the Lebesgue Covering Lemma on an open cover of small charts to approximate $f$ by a homotopic piecewise-linear or smooth loop $g \simeq f$ that is not surjective, and then contract $g$ in $S^2 \setminus \{p\} \cong \mathbb{R}^2$.
    2. **Seifert-van Kampen Theorem:** Cover $S^2$ by two overlapping open hemispheres $U = S^2 \setminus \{(0, 0, 1)\}$ and $V = S^2 \setminus \{(0, 0, -1)\}$, each homeomorphic to $\mathbb{R}^2$ (simply connected) with path-connected intersection $U \cap V \simeq S^1$, directly concluding $\pi_1(S^2) \cong \pi_1(U) \ast_{\pi_1(U \cap V)} \pi_1(V) = 0$. Q.E.D.
:::
