---
schema: qual/card@1
id: E-5VNUL
kind: problem
title: The Borsuk lemma fails without injectivity
classification:
  areas:
  - topology
  topics:
  - Invariance of Domain
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Give an example to show that the conclusion of the Borsuk lemma need not hold if $f$ is not injective.
:::

::: solution
**Goal:** Provide an explicit counterexample demonstrating that the conclusion of the Borsuk Lemma (that an image of a non-separating compact planar set does not separate the plane) fails when the continuous map $f$ is not injective.

<1>1. Statement of the Borsuk Lemma:
    The Borsuk Lemma (Munkres §62 Lemma 62.4) states that if $A \subset \mathbb{R}^2$ is a compact subspace that does not separate $\mathbb{R}^2$ (i.e. $\mathbb{R}^2 \setminus A$ is connected), and $f: A \to \mathbb{R}^2$ is an **injective** continuous map (an imbedding), then $f(A)$ does not separate $\mathbb{R}^2$ (i.e. $\mathbb{R}^2 \setminus f(A)$ is connected).

<1>2. Construction of non-injective counterexample:
    *Proof:*
    <2>1. Let $A = [0, 1] \times \{0\} \subset \mathbb{R}^2$ be the unit interval on the $x$-axis.
    <2>2. The set $A$ is compact, convex, and homeomorphic to the interval $[0, 1]$.
    <2>3. Its complement $\mathbb{R}^2 \setminus A$ is connected (path-connected), so $A$ does not separate the plane.
    <2>4. Define the continuous map $f: A \to \mathbb{R}^2$ by:
        $$f(t, 0) = (\cos 2\pi t, \sin 2\pi t).$$
    <2>5. The map $f$ is continuous, but fails to be injective since $f(0, 0) = f(1, 0) = (1, 0)$.

<1>3. Failure of the Borsuk conclusion for the image:
    *Proof:*
    <2>1. The image $f(A)$ is the unit circle $S^1 = \{(x, y) \in \mathbb{R}^2 \mid x^2 + y^2 = 1\}$.
    <2>2. By the Jordan Curve Theorem, the complement $\mathbb{R}^2 \setminus S^1$ consists of exactly two connected components: the bounded open disk $B_1(\mathbf{0})$ and the unbounded region $\mathbb{R}^2 \setminus \overline{B_1(\mathbf{0})}$.
    <2>3. Thus $f(A)$ separates the plane into 2 components, whereas $\mathbb{R}^2 \setminus A$ had only 1 component.

<1>4. Conclusion:
    The conclusion of the Borsuk lemma fails without the hypothesis of injectivity. Q.E.D.
:::
