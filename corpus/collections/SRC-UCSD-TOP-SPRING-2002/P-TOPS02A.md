---
schema: qual/card@1
id: P-TOPS02A
kind: problem
title: "A free group action on S^{2n} has order at most 2"
classification:
  areas:
  - topology
  topics:
  - Group Actions
  - Spheres
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $G$ be a group of homeomorphisms acting freely on $S^{2n}$ so that for all $g \in G$, $gx = x$ for some $x$ if and only if $g = 1$.
Prove $|G| \leq 2$.
:::

::: {.solution}
<1>1. Homology of $S^{2n}$ and the degree map: <2>1. The rational homology groups of the even-dimensional sphere $S^{2n}$ ($n \ge 1$) are:
\[
H_k(S^{2n}; \mathbb{Q}) \cong \begin{cases} \mathbb{Q} & k = 0, 2n \\ 0 & \text{otherwise}. \end{cases}
\]
Proof: homology of spheres.
<2>2. For any homeomorphism $g: S^{2n} \to S^{2n}$, the induced map $g_*: H_0(S^{2n}; \mathbb{Q}) \to H_0(S^{2n}; \mathbb{Q})$ is the identity (trace $1$), and $g_*: H_{2n}(S^{2n}; \mathbb{Q}) \to H_{2n}(S^{2n}; \mathbb{Q})$ is multiplication by $\deg(g) \in \{\pm 1\}$.
Proof: $S^{2n}$ is connected and $g$ is a homeomorphism.
<2>3. The map $d: G \to \{\pm 1\}$ given by $d(g) = \deg(g)$ is a group homomorphism.
Proof: functoriality of induced maps $(g \circ h)_* = g_* \circ h_* \implies \deg(gh) = \deg(g)\deg(h)$.

<1>2. Compute the Lefschetz number for fixed-point-free homeomorphisms: <2>1. The Lefschetz number of $g$ is defined as:
\[
\Lambda(g) = \sum_{k=0}^{2n} (-1)^k \operatorname{tr}\left(g_*|_{H_k(S^{2n}; \mathbb{Q})}\right) = \operatorname{tr}\left(g_*|_{H_0}\right) + (-1)^{2n} \operatorname{tr}\left(g_*|_{H_{2n}}\right) = 1 + \deg(g),
\]
since $(-1)^{2n} = 1$ for even dimension $2n$.
Proof: definition of the Lefschetz number and <1>1. <2>2. By hypothesis, the action of $G$ is free, so for every $g \in G \setminus \{1\}$, $g(x) \neq x$ for all $x \in S^{2n}$.
Proof: freeness of the group action.
<2>3. By the Lefschetz Fixed Point Theorem, if $g$ has no fixed points, then $\Lambda(g) = 0$.
Proof: Lefschetz Fixed Point Theorem.
<2>4. Thus $1 + \deg(g) = 0 \implies \deg(g) = -1$ for every $g \in G \setminus \{1\}$.
Proof: <2>1 and <2>3.

<1>3. Show that $|G| \le 2$: <2>1. By <1>1 and <1>2, the homomorphism $d: G \to \{\pm 1\}$ maps the identity $1 \mapsto 1$ and every non-identity element $g \neq 1 \mapsto -1$.
Proof: $\deg(\operatorname{id}) = 1$ and <2>4. <2>2. Thus $\ker(d) = \{1\}$, which means $d$ is an injective group homomorphism.
Proof: a homomorphism is injective if and only if its kernel is trivial.
<2>3. Since the target group $\{\pm 1\}$ has order $2$, the subgroup $G \cong d(G) \le \{\pm 1\}$ must have order dividing $2$:
\[
|G| \le 2.
\]
Proof: Lagrange's Theorem on subgroups of order 2 groups.

<1>4. Conclusion: $|G| \le 2$ (so $G \cong \{1\}$ or $G \cong \mathbb{Z}_2$). Q.E.D. Proof: <1>3.
:::
