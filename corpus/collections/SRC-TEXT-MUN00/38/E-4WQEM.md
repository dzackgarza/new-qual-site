---
schema: qual/card@1
id: E-4WQEM
kind: problem
title: Verifying the one-point compactification example for (0,1)
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Verify the statements made in Example 4 of §38 concerning the one-point compactification of $X = (0, 1)$ obtained from the imbedding $h: (0, 1) \to \mathbb{R}^2$ with component functions $x$ and $\sin(1/x)$.
:::

::: solution
**Goal:** Verify the topological properties of the compactification of $X = (0, 1)$ formed by the closure of the embedding $h(x) = (x, \sin(1/x))$ in $\mathbb{R}^2$, its remainder structure, and its relationship to the one-point compactification.

<1>1. Embedding and closure in $\mathbb{R}^2$:
    *Proof:*
    <2>1. The map $h: (0, 1) \to \mathbb{R}^2$ defined by $h(x) = (x, \sin(1/x))$ is continuous and injective.
    <2>2. The inverse projection $\pi_1: h(X) \to (0, 1)$ is continuous, so $h$ is a topological embedding onto the planar subspace $S = h((0, 1))$.
    <2>3. The closure $Y = \overline{S}$ in $\mathbb{R}^2$ is:
        $$Y = S \cup (\{0\} \times [-1, 1]) \cup \{(1, \sin 1)\}.$$
    <2>4. The space $Y$ is closed and bounded in $\mathbb{R}^2$, hence compact by the Heine-Borel theorem. Thus $Y$ is a compactification of $(0, 1)$.

<1>2. Structure of the remainder and non-extendability:
    *Proof:*
    <2>1. The remainder $Y \setminus S = (\{0\} \times [-1, 1]) \cup \{(1, \sin 1)\}$ contains an entire continuum of limit points $\{0\} \times [-1, 1]$ corresponding to the end $x \to 0^+$.
    <2>2. For any $y \in [-1, 1]$, the sequence $x_n = \frac{1}{\arcsin(y) + 2\pi n} \to 0^+$ satisfies $h(x_n) \to (0, y)$.
    <2>3. Consequently, $\lim_{x \to 0^+} h(x)$ does not exist in $\mathbb{R}^2$.
    <2>4. Therefore, the embedding $h$ cannot be extended continuously to the one-point compactification $X^* = (0, 1) \cup \{\infty\} \cong S^1$.

<1>3. Quotient relationship to the one-point compactification:
    *Proof:*
    <2>1. The one-point compactification of $(0, 1)$ is the circle $S^1$, obtained by adding a single point $\infty$ with open neighborhoods being complements of compact subsets of $(0, 1)$.
    <2>2. If one forms the quotient space $Y / (Y \setminus S)$ by collapsing the entire compact remainder $(\{0\} \times [-1, 1]) \cup \{(1, \sin 1)\}$ to a single point, the resulting quotient space is homeomorphic to the one-point compactification $X^* \cong S^1$.
    <2>3. This illustrates that any compactification of a locally compact Hausdorff space $X$ projects onto the one-point compactification $X^*$ by collapsing the remainder to a point. Q.E.D.
:::
