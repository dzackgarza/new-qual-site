---
schema: qual/card@1
id: P-AMD-3MWMRPVS
kind: problem
title: Path-connected 2-fold covers of $S^1\vee\RP^2$
classification:
  areas:
  - topology
  topics:
  - covering-spaces
  - fundamental-group
relations: []
review: draft
solved: true
---

::: {.problem}
How many path-connected 2-fold covering spaces does $S^1 \vee \RP 2$ have?
What are the total spaces?
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Determine the number of connected 2-fold covering spaces of $X = S^1 \vee \mathbb{RP}^2$ and identify the total space for each covering.

<1>1. Compute the fundamental group of $X = S^1 \vee \mathbb{RP}^2$.
<2>1. $S^1$ has fundamental group $\pi_1(S^1, s_0) \cong \langle a \rangle \cong \mathbb{Z}$.
<2>2. $\mathbb{RP}^2$ has fundamental group $\pi_1(\mathbb{RP}^2, p_0) \cong \langle b \mid b^2 = 1 \rangle \cong \mathbb{Z}/2\mathbb{Z}$.
<2>3. Since $S^1$ and $\mathbb{RP}^2$ are locally contractible CW complexes, their wedge sum $X = S^1 \vee \mathbb{RP}^2$ at basepoint $x_0$ has fundamental group given by the free product: $$G = \pi_1(X, x_0) \cong \pi_1(S^1, s_0) * \pi_1(\mathbb{RP}^2, p_0) \cong \langle a, b \mid b^2 = 1 \rangle \cong \mathbb{Z} * (\mathbb{Z}/2\mathbb{Z}).$$ <2>4. Proof: By the Seifert-van Kampen theorem for wedge sums of nice spaces.
Q.E.D.

<1>2. Classification of path-connected 2-fold covering spaces.
<2>1. By covering space theory, isomorphism classes of path-connected 2-fold covering spaces of $X$ correspond bijectively to index 2 subgroups $H \le G$, which in turn correspond bijectively to non-trivial homomorphisms $\phi \colon G \to \mathbb{Z}/2\mathbb{Z} = \{\pm 1\}$ via $H = \ker(\phi)$.
<2>2. A homomorphism $\phi \colon G \to \{\pm 1\}$ is determined uniquely by the images of the generators $a$ and $b$:

- $\phi(a) \in \{\pm 1\}$,

- $\phi(b) \in \{\pm 1\}$ (which always satisfies $(\phi(b))^2 = 1$). <2>3. There are $2 \times 2 = 4$ homomorphisms in total.
  Exactly 3 of them are non-trivial (surjective onto $\mathbb{Z}/2\mathbb{Z}$):

- Case 1: $\phi_1(a) = -1, \phi_1(b) = 1$.
  Subgroup $H_1 = \ker \phi_1 = \langle a^2, b, a b a^{-1} \rangle$.

- Case 2: $\phi_2(a) = 1, \phi_2(b) = -1$.
  Subgroup $H_2 = \ker \phi_2 = \langle a, b a b^{-1}, b^2 \rangle$.

- Case 3: $\phi_3(a) = -1, \phi_3(b) = -1$.
  Subgroup $H_3 = \ker \phi_3 = \langle a^2, b^2, ab, ba \rangle$.
  <2>4. Thus, there are exactly 3 distinct path-connected 2-fold covering spaces of $S^1 \vee \mathbb{RP}^2$.
  <2>5. Proof: By the Galois correspondence for covering spaces.
  Q.E.D.

<1>3. Identify the total space $\widetilde{X}_1$ for $\phi_1$ ($\phi_1(a) = -1, \phi_1(b) = 1$). <2>1. The loop $a$ has non-trivial monodromy (swaps the two sheets), while $b$ lifts to closed loops on both sheets.
<2>2. The basepoint lifts to 2 points $x_1, x_2$.
<2>3. The circle $S^1$ lifts to a single circle of twice the length connecting $x_1$ and $x_2$ (a single circle $\widetilde{S}^1 \cong S^1$). <2>4. The $\mathbb{RP}^2$ lifts trivially to two disjoint copies of $\mathbb{RP}^2$, one attached at $x_1$ and one attached at $x_2$.
<2>5. Thus, the total space is a circle with an $\mathbb{RP}^2$ attached at each of two distinct points: $$\widetilde{X}_1 \cong S^1 \cup_{p_1} \mathbb{RP}^2 \cup_{p_2} \mathbb{RP}^2 \simeq S^1 \vee \mathbb{RP}^2 \vee \mathbb{RP}^2.$$ <2>6. Proof: By analyzing the fiber lift of the cell structure / graph of spaces.
Q.E.D.

<1>4. Identify the total space $\widetilde{X}_2$ for $\phi_2$ ($\phi_2(a) = 1, \phi_2(b) = -1$). <2>1. The loop $a$ has trivial monodromy (lifts to two separate circles), while $b$ has non-trivial monodromy (the standard 2-fold cover of $\mathbb{RP}^2$ is $S^2$). <2>2. The basepoint lifts to 2 points $x_1, x_2$.
<2>3. $\mathbb{RP}^2$ lifts to the connected 2-fold cover $S^2$, with antipodal basepoints $x_1, x_2$.
<2>4. The circle $S^1$ lifts to two disjoint circles, one attached at $x_1$ and one attached at $x_2$.
<2>5. Thus, the total space is the 2-sphere $S^2$ with a circle attached at each of two antipodal points: $$\widetilde{X}_2 \cong S^2 \cup_{x_1} S^1 \cup_{x_2} S^1 \simeq S^2 \vee S^1 \vee S^1.$$ <2>6. Proof: By analyzing the fiber lift of the cell structure.
Q.E.D.

<1>5. Identify the total space $\widetilde{X}_3$ for $\phi_3$ ($\phi_3(a) = -1, \phi_3(b) = -1$). <2>1. Both $a$ and $b$ act non-trivially (swap the sheets).
<2>2. The basepoint lifts to 2 points $x_1, x_2$.
<2>3. The circle $S^1$ lifts to a single arc/segment connecting $x_1$ and $x_2$ in both directions, forming a single circle $\widetilde{S}^1$ containing $x_1$ and $x_2$.
<2>4. The $\mathbb{RP}^2$ lifts to the connected 2-fold cover $S^2$, with basepoints $x_1$ and $x_2$ on $S^2$ (antipodal points).
<2>5. The total space is formed by taking $S^2$ and connecting two distinct points $x_1, x_2 \in S^2$ by an arc (or equivalently attaching a 1-handle / joining $S^2$ with a circle at two points): $$\widetilde{X}_3 \cong S^2 \cup_{\{x_1, x_2\}} [0, 1] \simeq S^2 \vee S^1.$$ <2>6. Proof: Collapsing the connecting arc in $S^2 \cup [0, 1]$ yields a homotopy equivalence $\widetilde{X}_3 \simeq S^2 \vee S^1$ (the wedge of $S^2$ and $S^1$). Q.E.D.

<1>6. Conclusion.
<2>1. There are exactly 3 path-connected 2-fold covering spaces of $S^1 \vee \mathbb{RP}^2$.
<2>2. Their total spaces are:

1. $S^1$ with two copies of $\mathbb{RP}^2$ attached (homotopy equivalent to $S^1 \vee \mathbb{RP}^2 \vee \mathbb{RP}^2$),

2. $S^2$ with two copies of $S^1$ attached (homotopy equivalent to $S^2 \vee S^1 \vee S^1$),

3. $S^2$ with an arc connecting two points (homotopy equivalent to $S^2 \vee S^1$). <2>3. Proof: By <1>1–<1>5. Q.E.D.
:::
