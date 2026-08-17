---
schema: qual/card@1
id: P-AMD-2GG7VEF2
kind: problem
title: $\pi_1(S^n)=1$ for $n\geq 2$
classification:
  areas:
  - topology
  topics:
  - fundamental-group
  - van-kampen
relations: []
review: draft
solved: true
---

::: {.problem}
Show $\pi_1(S^n) = 1$ for $n\geq 2$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Prove that for all integers $n \geq 2$, the fundamental group $\pi_1(S^n, x_0)$ is trivial.

<1>1. Cover $S^n$ by two open subsets $U$ and $V$.
<2>1. Let $N = (0, \dots, 0, 1) \in S^n \subset \mathbb{R}^{n+1}$ (North pole) and $S = (0, \dots, 0, -1) \in S^n$ (South pole).
<2>2. Define $U = S^n \setminus \{S\}$ and $V = S^n \setminus \{N\}$.
<2>3. Since $\{S\}$ and $\{N\}$ are closed singletons in $S^n$, $U$ and $V$ are open in $S^n$.
<2>4. $U \cup V = S^n$ because $N \neq S$, so no point in $S^n$ is equal to both $N$ and $S$.
<2>5. Proof: By construction, $\{U, V\}$ is an open cover of $S^n$.
Q.E.D.

<1>2. $U$ and $V$ are contractible, hence simply connected.
<2>1. Stereographic projection from $S$ is a homeomorphism $U \to \mathbb{R}^n$.
<2>2. Stereographic projection from $N$ is a homeomorphism $V \to \mathbb{R}^n$.
<2>3. $\mathbb{R}^n$ is convex, hence contractible to the origin via straight-line homotopy $H(x, t) = (1-t)x$.
<2>4. Therefore, $U \simeq * \implies \pi_1(U, x_0) = 1$ and $V \simeq * \implies \pi_1(V, x_0) = 1$ for any basepoint $x_0 \in U \cap V$.
<2>5. Proof: Homeomorphisms preserve contractibility, and contractible spaces have trivial fundamental groups.
Q.E.D.

<1>3. The intersection $U \cap V = S^n \setminus \{N, S\}$ is path-connected for $n \geq 2$.
<2>1. Under stereographic projection $\phi \colon U \to \mathbb{R}^n$, the pole $N$ maps to $0 \in \mathbb{R}^n$.
<2>2. Thus $U \cap V = U \setminus \{N\} \cong \mathbb{R}^n \setminus \{0\}$.
<2>3. $\mathbb{R}^n \setminus \{0\}$ deformation retracts to $S^{n-1}$ via $x \mapsto \frac{x}{\|x\|}$.
<2>4. For $n \geq 2$, the sphere $S^{n-1}$ has dimension $n-1 \geq 1$, which is path-connected.
<2>5. Therefore, $\mathbb{R}^n \setminus \{0\}$ is path-connected, which implies $U \cap V$ is path-connected.
<2>6. Proof: By <2>1–<2>5, $U \cap V$ is nonempty and path-connected.
Q.E.D.

<1>4. Apply the Seifert-van Kampen theorem to the cover $\{U, V\}$.
<2>1. Let $x_0 \in U \cap V$ be the basepoint.
<2>2. The hypotheses of the Seifert-van Kampen theorem are satisfied: $U, V$ are open, $U \cup V = S^n$, and $U \cap V$ is path-connected.
<2>3. The theorem gives an isomorphism: $$\pi_1(S^n, x_0) \cong \pi_1(U, x_0) *_{\pi_1(U \cap V, x_0)} \pi_1(V, x_0).$$ <2>4. By <1>2, $\pi_1(U, x_0) = 1$ and $\pi_1(V, x_0) = 1$.
<2>5. The amalgamated free product of two trivial groups is trivial: $1 *_{\pi_1(U \cap V, x_0)} 1 = 1$.
<2>6. Proof: By direct substitution into the van Kampen isomorphism.
Q.E.D.

<1>5. Q.E.D. <2>1. Proof: <1>4 establishes $\pi_1(S^n, x_0) = 1$ for all $n \geq 2$.
:::
