---
schema: qual/card@1
id: P-SAEXG
kind: problem
title: Path-connected $2$-fold covering spaces of $S^1\vee\RP^2$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
  - van Kampen
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
How many path-connected 2-fold covering spaces does $S^1 \vee \RP 2$ have?
What are the total spaces?
:::

::: {.solution}
**Goal:** Determine the number of connected 2-fold covering spaces of $X = S^1 \vee \mathbb{RP}^2$ and identify the total space for each covering.

<1>1. Compute the fundamental group of $X = S^1 \vee \mathbb{RP}^2$.
<2>1. $S^1$ has fundamental group $\pi_1(S^1, s_0) \cong \langle a \rangle \cong \mathbb{Z}$.
<2>2. $\mathbb{RP}^2$ has fundamental group $\pi_1(\mathbb{RP}^2, p_0) \cong \langle b \mid b^2 = 1 \rangle \cong \mathbb{Z}/2\mathbb{Z}$.
<2>3. Since $S^1$ and $\mathbb{RP}^2$ are locally contractible CW complexes, their wedge sum $X = S^1 \vee \mathbb{RP}^2$ at basepoint $x_0$ has fundamental group given by the free product: $$G = \pi_1(X, x_0) \cong \pi_1(S^1, s_0) * \pi_1(\mathbb{RP}^2, p_0) \cong \langle a, b \mid b^2 = 1 \rangle \cong \mathbb{Z} * (\mathbb{Z}/2\mathbb{Z}).$$
::: {.proof}
<2>4. The Seifert–van Kampen theorem for the wedge of two nice spaces gives the free product of their fundamental groups, which is $\mathbb{Z} * (\mathbb{Z}/2\mathbb{Z})$.
:::

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
::: {.proof}
  <2>5. The Galois correspondence identifies connected 2-fold covers with index-2 subgroups, equivalently with surjective homomorphisms to $\mathbb{Z}/2\mathbb{Z}$; there are exactly 3 such homomorphisms, listed in <2>3.
:::

<1>3. Identify the total space $\widetilde{X}_1$ for $\phi_1$ ($\phi_1(a) = -1, \phi_1(b) = 1$). <2>1. The loop $a$ has non-trivial monodromy (swaps the two sheets), while $b$ lifts to closed loops on both sheets.
<2>2. The basepoint lifts to 2 points $x_1, x_2$.
<2>3. The circle $S^1$ lifts to a single circle of twice the length connecting $x_1$ and $x_2$ (a single circle $\widetilde{S}^1 \cong S^1$). <2>4. The $\mathbb{RP}^2$ lifts to two disjoint copies of $\mathbb{RP}^2$ (the monodromy of $\phi_1$ on the $\mathbb{RP}^2$ factor is the identity), one attached at $x_1$ and one attached at $x_2$.
<2>5. Thus, the total space is a circle with an $\mathbb{RP}^2$ attached at each of two distinct points: $$\widetilde{X}_1 \cong S^1 \cup_{p_1} \mathbb{RP}^2 \cup_{p_2} \mathbb{RP}^2 \simeq S^1 \vee \mathbb{RP}^2 \vee \mathbb{RP}^2.$$
::: {.proof}
<2>6. Since $\phi_1(a) = -1$, the circle lifts to a single circle of double length; since $\phi_1(b) = 1$, each copy of $\mathbb{RP}^2$ lifts to two disjoint copies, one over each sheet, attached at the two basepoint lifts.
:::

<1>4. Identify the total space $\widetilde{X}_2$ for $\phi_2$ ($\phi_2(a) = 1, \phi_2(b) = -1$). <2>1. The loop $a$ has trivial monodromy (lifts to two separate circles), while $b$ has non-trivial monodromy (the standard 2-fold cover of $\mathbb{RP}^2$ is $S^2$). <2>2. The basepoint lifts to 2 points $x_1, x_2$.
<2>3. $\mathbb{RP}^2$ lifts to the connected 2-fold cover $S^2$, with antipodal basepoints $x_1, x_2$.
<2>4. The circle $S^1$ lifts to two disjoint circles, one attached at $x_1$ and one attached at $x_2$.
<2>5. Thus, the total space is the 2-sphere $S^2$ with a circle attached at each of two antipodal points: $$\widetilde{X}_2 \cong S^2 \cup_{x_1} S^1 \cup_{x_2} S^1 \simeq S^2 \vee S^1 \vee S^1.$$
::: {.proof}
<2>6. Since $\phi_2(b) = -1$, the 2-fold cover of $\mathbb{RP}^2$ is $S^2$; since $\phi_2(a) = 1$, the circle lifts to two disjoint circles, one attached at each of the two antipodal basepoints.
:::

<1>5. Identify the total space $\widetilde X_3$ for $\phi_3(a)=\phi_3(b)=-1$.
<2>1. The preimage of the $\mathbb{RP}^2$ summand is its connected double cover $S^2$, and the two points over the wedge point are antipodal points $x_1,x_2\in S^2$.
::: {.proof}
The restriction of the monodromy to $\pi_1(\mathbb{RP}^2)=\langle b\rangle$ is nontrivial, so the restricted cover is the universal double cover $S^2\to\mathbb{RP}^2$.
:::
<2>2. The preimage of the $S^1$ summand is its connected double cover, hence a circle $C\cong S^1$ containing the two fiber points $x_1,x_2$.
::: {.proof}
The monodromy of $a$ swaps the two sheets, so the restricted $2$-fold cover of $S^1$ is connected. Its fiber over the wedge point consists of the two points where $C$ meets the lifted $S^2$.
:::
<2>3. Thus the total space is
$$
\widetilde X_3\cong S^2\cup_{\{x_1,x_2\}} C,
$$
where the two selected points of $C$ are identified with the two antipodal points of $S^2$.
::: {.proof}
The original wedge is obtained by identifying the basepoints of the two summands, so its covering is obtained by gluing the restricted covers along the two points lying over that basepoint.
:::
<2>4. This space has homotopy type
$$\boxed{\widetilde X_3\simeq S^2\vee S^1\vee S^1}.$$
::: {.proof}
The two points $x_1,x_2$ divide $C$ into two arcs $\alpha,\beta$, each joining $x_1$ to $x_2$. Choose an embedded arc $\gamma\subset S^2$ joining $x_1$ to $x_2$. Collapsing the contractible tree $\gamma$ to a point converts each of $\alpha$ and $\beta$ into a loop and leaves the sphere homotopy equivalent to $S^2$. Thus the quotient is $S^2\vee S^1\vee S^1$, and collapsing a contractible subcomplex is a homotopy equivalence here.
:::

<1>6. Therefore there are exactly three connected double covers, with total spaces
$$
\boxed{
\begin{aligned}
\widetilde X_1&\cong S^1\text{ with two copies of }\mathbb{RP}^2\text{ attached at the two fiber points},\\
\widetilde X_2&\cong S^2\text{ with one circle attached at each of the two fiber points},\\
\widetilde X_3&\cong S^2\cup_{\{x_1,x_2\}}S^1.
\end{aligned}}
$$
Their homotopy types are respectively
$$
S^1\vee\mathbb{RP}^2\vee\mathbb{RP}^2,
\qquad
S^2\vee S^1\vee S^1,
\qquad
S^2\vee S^1\vee S^1.
$$
::: {.proof}
The three nonzero homomorphisms $G\to\ZZ/2$ in <1>2 give all index-$2$ subgroups, and <1>3--<1>5 identify their corresponding total spaces.
:::
:::
