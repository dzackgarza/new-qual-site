---
schema: qual/card@1
id: P-G6GOO
kind: problem
title: The infinite $3$-regular tree as a universal cover
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $X$ be a finite connected graph whose fundamental group is the free group on generators (e.g. the wedge sum $S^1 \vee S^1$ or the theta graph with 3 edges).
(1) Construct the **universal covering space** $\widetilde{X}$ of $X$ as the tree $T$ of non-backtracking reduced paths from a basepoint $x_0 \in X$.
(2) Prove that $\widetilde{X}$ is a connected, acyclic tree (hence simply connected: $\pi_1(\widetilde{X}) = 0$).
(3) Explain why for a 3-valent graph (like the theta graph), the universal cover is the **infinite 3-regular tree** $T_3$.
:::

::: solution
**Goal:** Construct the universal cover of a graph as a tree of non-backtracking paths and prove that the universal cover of a 3-valent graph is the infinite 3-regular tree $T_3$.

<1>1. Universal Cover Construction via Path Space:
    *Proof:*
    <2>1. Let $X$ be a connected graph (CW 1-complex) and choose a base vertex $x_0 \in X$.
    <2>2. The **universal cover** $\widetilde{X}$ has vertices:
        $$V(\widetilde{X}) \coloneqq \{[\gamma] \mid \gamma \text{ is a path in } X \text{ starting at } x_0 \text{ modulo homotopy rel endpoints}\}.$$
    <2>3. On a graph, every path homotopy class $[\gamma]$ contains a **unique non-backtracking (reduced) edge-path** $\gamma = e_1 e_2 \cdots e_k$ starting at $x_0$, where $e_{i+1} \ne \bar{e}_i$.
    <2>4. Two vertices $[\gamma_1]$ and $[\gamma_2]$ in $\widetilde{X}$ are connected by an edge if and only if $\gamma_2$ is obtained from $\gamma_1$ by appending a single directed edge $e$ of $X$.
    <2>5. The covering projection $p: \widetilde{X} \to X$ maps each path $[\gamma]$ to its endpoint $\gamma(1) \in X$, and maps edges of $\widetilde{X}$ to their corresponding edges in $X$.

<1>2. Proof that $\widetilde{X}$ is a Tree (Acyclic and Connected):
    *Proof:*
    <2>1. **Connectedness:** Every vertex $[\gamma]$ is connected to the basepoint $[c_{x_0}]$ by the unique sequence of initial subpaths of the reduced word $\gamma$.
    <2>2. **Acyclicity (No non-trivial cycles):**
        - Suppose there exists a simple non-trivial cycle $C = v_0 v_1 \cdots v_m v_0$ in $\widetilde{X}$.
        - Projecting $C$ to $X$ via $p$ gives a non-backtracking closed loop $\omega = p(C)$ in $X$ based at $p(v_0)$.
        - Lifting $\omega$ to $\widetilde{X}$ starting at $v_0$ traces the path $C$, so its terminal point is $v_0$.
        - By the Unique Path Lifting Property, a closed loop lifts to a closed loop if and only if its homotopy class $[\omega] = e \in \pi_1(X, p(v_0))$.
        - But on a graph, the only reduced loop homotopic to the constant loop is the empty path.
        - This contradicts the assumption that $C$ was a non-trivial cycle.
    <2>3. Thus $\widetilde{X}$ contains no cycles, so $\widetilde{X}$ is a **tree** ($1$-dimensional contractible CW-complex).
    <2>4. Since every tree is contractible, $\pi_1(\widetilde{X}) = \{0\}$, so $\widetilde{X}$ is **simply connected**.
    <2>5. Since $p: \widetilde{X} \to X$ is a covering map and $\widetilde{X}$ is simply connected and locally path-connected, $\widetilde{X}$ is the **universal cover** of $X$.

<1>3. The 3-Valent Graph and the Infinite 3-Regular Tree $T_3$:
    *Proof:*
    <2>1. A covering projection $p: \widetilde{X} \to X$ is a **local homeomorphism**.
    <2>2. In particular, for any vertex $\tilde{v} \in \widetilde{X}$, the valence (degree) of $\tilde{v}$ equals the valence of its image $p(\tilde{v}) \in X$:
        $$\operatorname{deg}_{\widetilde{X}}(\tilde{v}) = \operatorname{deg}_X(p(\tilde{v})).$$
    <2>3. If $X$ is a **3-valent (cubic) graph** (every vertex in $X$ has degree 3, e.g. the theta graph $\Theta$ with 2 vertices of degree 3, or the figure-8 with a midpoint):
        $$\operatorname{deg}(\tilde{v}) = 3 \quad \text{for all } \tilde{v} \in V(\widetilde{X}).$$
    <2>4. Since $\widetilde{X}$ is a connected, acyclic graph where every vertex has degree 3, $\widetilde{X}$ is the unique **infinite 3-regular tree $T_3$** (also known as the Cayley graph of the free group $F_2$ with modified generators or the universal covering tree of 3-valent networks).

<1>4. Conclusion:
    The path-tree construction gives a simply connected acyclic graph $\widetilde{X}$, which for any 3-valent graph is the infinite 3-regular tree $T_3$. Q.E.D.
:::
