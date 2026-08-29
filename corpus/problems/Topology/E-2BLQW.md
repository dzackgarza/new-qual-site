---
schema: qual/card@1
id: E-2BLQW
kind: exercise
title: Connectedness versus path-connectedness
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: exercise
Show that:

- Connected does not imply path connected

- Connected and locally path connected *does* imply path connected

- Path connected implies connected
:::

::: solution
**Goal:** Prove the standard topological relationships and distinctions between connectedness, path-connectedness, and local path-connectedness.

<1>1. Path-connected implies connected: *Proof:* <2>1. Let $X$ be a path-connected space, and fix a basepoint $x_0 \in X$.
<2>2. For every point $x \in X$, there exists a continuous path $\gamma_x: [0, 1] \to X$ such that $\gamma_x(0) = x_0$ and $\gamma_x(1) = x$.
<2>3. The unit interval $[0, 1]$ is connected, so the continuous image $P_x = \gamma_x([0, 1])$ is connected.
<2>4. The whole space $X = \bigcup_{x \in X} P_x$ is a union of connected subsets sharing the common point $x_0 \in \bigcap_{x \in X} P_x \neq \emptyset$.
<2>5. The union of any collection of connected sets with non-empty intersection is connected.
Therefore $X$ is connected.

<1>2. Connected does not imply path-connected (Topologist's Sine Curve): *Proof:* <2>1. Consider the topologist's sine curve $\bar{S} = S \cup L \subset \mathbb{R}^2$, where: $$S = \ts{\left(x, \sin\frac{1}{x}\right) \mid x \in (0, 1]} \quad \text{and} \quad L = \{0\} \times [-1, 1].$$ <2>2. $S$ is the continuous image of the connected interval $(0, 1]$ under $x \mapsto (x, \sin(1/x))$, hence $S$ is connected.
<2>3. Since $L$ is in the closure of $S$ in $\mathbb{R}^2$, $\bar{S} = \overline{S}$ is connected.
<2>4. However, $\bar{S}$ is not path-connected: no continuous path $\gamma: [0, 1] \to \bar{S}$ can connect $(0, 0) \in L$ to $(1/\pi, 0) \in S$.
(If such a path $\gamma(t) = (x(t), y(t))$ existed with $\gamma(0) = (0, 0)$, by intermediate value theorem $x(t)$ would oscillate infinitely often across points where $\sin(1/x) = \pm 1$ as $t \to 0^+$, violating continuity of $y(t)$ at $t=0$).

<1>3. Connected and locally path-connected implies path-connected: *Proof:* <2>1. Let $X$ be connected and locally path-connected.
If $X = \emptyset$, it is vacuously path-connected.
<2>2. Fix $x_0 \in X$ and let $P(x_0)$ denote the path component of $x_0$ in $X$.
Since $x_0 \in P(x_0)$, $P(x_0) \neq \emptyset$.
<2>3. $P(x_0)$ is open in $X$: For any $x \in P(x_0)$, local path-connectedness provides a path-connected open neighborhood $U$ of $x$.
For every $y \in U$, concatenating the path from $x_0$ to $x$ with the path from $x$ to $y$ gives a path from $x_0$ to $y$, so $U \subseteq P(x_0)$.
<2>4. $X \setminus P(x_0)$ is open in $X$: For any $z \in X \setminus P(x_0)$, choose a path-connected open neighborhood $V$ of $z$.
If $V \cap P(x_0) \neq \emptyset$, picking $w \in V \cap P(x_0)$ gives a path from $x_0$ to $w$ and a path from $w$ to $z$, placing $z \in P(x_0)$, a contradiction.
Thus $V \subseteq X \setminus P(x_0)$.
<2>5. Thus $P(x_0)$ is a non-empty clopen subset of the connected space $X$, which forces $P(x_0) = X$.
<2>6. Hence $X$ is path-connected.
Q.E.D.
:::
