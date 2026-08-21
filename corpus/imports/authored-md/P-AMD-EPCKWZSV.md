---
schema: qual/card@1
id: P-AMD-EPCKWZSV
kind: problem
title: $S^1 \times I \simeq$ the Möbius strip
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Retracts
  - Surfaces
relations: []
review: draft
solved: true
---

::: {.problem}
Show that $S^1 \times I \simeq M$, the Mobius strip.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Prove that the cylinder $S^1 \times [0, 1]$ is homotopy equivalent to the Möbius strip $M = ([0, 1] \times [0, 1]) / ((0, y) \sim (1, 1-y))$.

<1>1. Show that the cylinder $S^1 \times [0, 1]$ deformation retracts to the circle $S^1$.
<2>1. Realize $S^1 \times [0, 1]$ with inclusion $\iota_1 \colon S^1 \hookrightarrow S^1 \times [0, 1]$ given by $z \mapsto (z, 1/2)$, and retraction $r_1 \colon S^1 \times [0, 1] \to S^1$ given by $(z, t) \mapsto z$.
<2>2. Define the straight-line homotopy $H_1 \colon (S^1 \times [0, 1]) \times [0, 1] \to S^1 \times [0, 1]$ by $H_1((z, t), s) = (z, (1-s)t + s(1/2))$.
<2>3. $H_1$ is continuous, $H_1((z, t), 0) = (z, t) = \operatorname{id}_{S^1 \times I}$, $H_1((z, t), 1) = (z, 1/2) = \iota_1(r_1(z, t))$, and $H_1((z, 1/2), s) = (z, 1/2)$ for all $s \in [0, 1]$.
<2>4. Thus $H_1$ is a strong deformation retraction of $S^1 \times [0, 1]$ onto the circle $S^1 \times \{1/2\} \cong S^1$.
<2>5. Consequently, $S^1 \times [0, 1] \simeq S^1$.
<2>6. Proof: By construction of the deformation retraction.
Q.E.D.

<1>2. Show that the Möbius strip $M$ deformation retracts to the circle $S^1$.
<2>1. Let $M = ([0, 1] \times [0, 1]) / ((0, y) \sim (1, 1-y))$, and let $C = \{[(x, 1/2)] \mid x \in [0, 1]\} \subset M$ be the core circle.
<2>2. The map $\gamma \colon [0, 1] / (0 \sim 1) \to C$ given by $x \mapsto [(x, 1/2)]$ is a homeomorphism, so $C \cong S^1$.
<2>3. Define $H_2 \colon M \times [0, 1] \to M$ by $H_2([(x, y)], s) = [(x, (1-s)y + s(1/2))]$.
<2>4. $H_2$ respects the quotient identification because at $x = 1$, $H_2([(1, 1-y)], s) = [(1, (1-s)(1-y) + s/2)] = [(0, 1 - ((1-s)(1-y) + s/2))] = [(0, (1-s)y + s/2)] = H_2([(0, y)], s)$.
<2>5. $H_2$ is a strong deformation retraction of $M$ onto the core circle $C \cong S^1$.
<2>6. Consequently, $M \simeq S^1$.
<2>7. Proof: By construction of the deformation retraction.
Q.E.D.

<1>3. Combine homotopy equivalences.
<2>1. Homotopy equivalence ($\simeq$) is an equivalence relation on topological spaces.
<2>2. By <1>1, $S^1 \times [0, 1] \simeq S^1$.
<2>3. By <1>2, $M \simeq S^1$.
<2>4. By transitivity and symmetry, $S^1 \times [0, 1] \simeq M$.
<2>5. Proof: By <2>1–<2>4. Q.E.D.

<1>4. Q.E.D. <2>1. Proof: <1>3 establishes $S^1 \times [0, 1] \simeq M$.
:::
