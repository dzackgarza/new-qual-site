---
schema: qual/card@1
id: E-0LZE7
kind: exercise
title: The figure eight and the theta space are homotopy equivalent
classification:
  areas:
  - topology
  topics:
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $X$ be the figure eight and let $Y$ be the theta space.
Describe maps $f: X \to Y$ and $g: Y \to X$ that are homotopy inverse to each other.
:::

::: solution
**Goal:** Explicitly construct continuous maps $f: X \to Y$ and $g: Y \to X$ between the figure-eight space $X = S^1 \vee S^1$ and the theta space $Y = S^1 \cup ([-1, 1] \times \{0\})$, and prove they are homotopy inverses.

<1>1. Geometric models for $X$ and $Y$:
    1. Figure eight $X = C_1 \cup C_2 \subset \mathbb{R}^2$, where $C_1$ and $C_2$ are circles intersecting at the single basepoint $p = (0, 0)$.
    2. Theta space $Y = U \cup L \cup I_0 \subset \mathbb{R}^2$, where:
       - $U = \{(x, y) \in S^1 : y \ge 0\}$ is the upper semicircle from $a = (-1, 0)$ to $b = (1, 0)$,
       - $L = \{(x, y) \in S^1 : y \le 0\}$ is the lower semicircle from $a$ to $b$,
       - $I_0 = \{(x, 0) \in \mathbb{R}^2 : -1 \le x \le 1\}$ is the horizontal diameter from $a$ to $b$.

<1>2. Construction of $g: Y \to X$ (collapsing the central segment):
    Define $g: Y \to X$ by the quotient map that collapses the contractible segment $I_0$ to the basepoint $p$:
    - For $z \in I_0$: $g(z) = p$.
    - For $z \in U$: $g(z)$ maps $U$ homeomorphically onto $C_1$ with $g(a) = g(b) = p$.
    - For $z \in L$: $g(z)$ maps $L$ homeomorphically onto $C_2$ with $g(a) = g(b) = p$.
    By the Pasting Lemma, $g$ is continuous.

<1>3. Construction of $f: X \to Y$ (attaching loops):
    Define $f: X \to Y$ by sending the basepoint $p \in X$ to $a \in Y$:
    - On $C_1$: $f$ traces the loop formed by following $U$ from $a$ to $b$, then returning along $I_0$ from $b$ to $a$.
    - On $C_2$: $f$ traces the loop formed by following $L$ from $a$ to $b$, then returning along $I_0$ from $b$ to $a$.
    By the Pasting Lemma on $X = C_1 \cup C_2$, $f$ is continuous with $f(p) = a$.

<1>4. Homotopy $g \circ f \simeq \operatorname{id}_X$:
    *Proof:*
    <2>1. The composition $(g \circ f)|_{C_1}$ traverses $g(U) = C_1$ followed by the constant path $g(I_0) = c_p$.
    <2>2. Since concatenation with the constant path is homotopic to the original loop ($C_1 \ast c_p \simeq C_1$), $(g \circ f)|_{C_1} \simeq \operatorname{id}_{C_1}$.
    <2>3. Similarly, $(g \circ f)|_{C_2}$ traverses $g(L) \ast g(I_0) = C_2 \ast c_p \simeq C_2$, so $(g \circ f)|_{C_2} \simeq \operatorname{id}_{C_2}$.
    <2>4. Combining these homotopies fixes the basepoint $p$, yielding $g \circ f \simeq \operatorname{id}_X$.

<1>5. Homotopy $f \circ g \simeq \operatorname{id}_Y$:
    *Proof:*
    <2>1. The segment $I_0$ is a deformation retract of $Y$ onto the tree segment $I_0$ connecting $a$ and $b$, which itself deformation retracts to $a$.
    <2>2. Explicitly, define $H: Y \times [0, 1] \to Y$ by linearly sliding the segment $I_0$ onto the point $a$:
        $$H((x, 0), t) = ((1-t)x - t, 0) \quad \text{for } (x, 0) \in I_0,$$
        while keeping points on $U$ and $L$ stationary up to reparametrization.
    <2>3. At $t = 0$, $H_0 = \operatorname{id}_Y$.
    <2>4. At $t = 1$, $H_1 = f \circ g$.
    <2>5. Thus $f \circ g \simeq \operatorname{id}_Y$.

<1>6. Conclusion:
    $f$ and $g$ are homotopy inverse to each other, establishing that the figure eight and the theta space are homotopy equivalent: $X \simeq Y$. Q.E.D.
:::
