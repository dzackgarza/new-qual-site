---
schema: qual/card@1
id: P-AMD-5A2VNO4E
kind: problem
title: Letters of the alphabet up to homeomorphism and homotopy
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Homotopy
  - Classification
relations: []
review: draft
solved: true
---

::: {.problem}
Classify the letters of the alphabet up to homeomorphism, and up to homotopy.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Classify the standard sans-serif capital English alphabet letters $\mathcal{A} = \{\text{A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z}\}$ viewed as 1-dimensional CW complexes (graphs) embedded in the plane, up to:
1. Homotopy equivalence ($\simeq$),
2. Homeomorphism ($\cong$).

<1>1. Fix the topological graph model (sans-serif uppercase).
  <2>1. Under standard sans-serif representation:
  - Zero-loop contractible trees:
    - Simple arcs (homeomorphic to $[0, 1]$): $\text{C, G, I, J, L, M, N, S, U, V, W, Z}$ (treating G as a simple arc with an elbow, or a 3-junction depending on font; standard textbook convention treats C, I, J, L, M, N, S, U, V, W, Z as arcs).
    - Trees with vertices of degree $\ge 3$:
      - One 3-way junction (T-like / Y-like): $\text{E, F, T, Y}$.
      - Two 3-way junctions: $\text{H, K}$.
      - One 4-way junction: $\text{X}$.
  - One loop ($\pi_1 \cong \mathbb{Z}$):
    - Circle with no extra tails: $\text{O}, \text{D}$.
    - Circle with one tail (degree 3 junction): $\text{P, Q}$.
    - Circle with two tails / theta-graph variant: $\text{A, R}$.
  - Two loops ($\pi_1 \cong \mathbb{Z} * \mathbb{Z}$):
    - Figure-eight / double loop: $\text{B}$.
  <2>2. Proof: By viewing each glyph as a finite 1-dimensional simplicial complex / graph. Q.E.D.

<1>2. Classification up to Homotopy Equivalence ($\simeq$).
  <2>1. A finite connected 1-dimensional CW complex (graph) $G$ deformation retracts to a wedge sum of circles $\bigvee_{g} S^1$, where $g = 1 - \chi(G) = \operatorname{rank}(\pi_1(G))$ is the first Betti number / number of independent cycles.
  <2>2. Connected graphs are completely classified up to homotopy equivalence by their fundamental group $\pi_1(G) \cong *^g \mathbb{Z}$:
  - **Group 1 ($g = 0$, contractible, $\simeq *$):**
    $$\{\text{C, E, F, G, H, I, J, K, L, M, N, S, T, U, V, W, X, Y, Z}\}.$$
    All of these are trees, hence deformation retract to a point.
  - **Group 2 ($g = 1$, homotopy equivalent to $S^1$):**
    $$\{\text{A, D, O, P, Q, R}\}.$$
    Each contains exactly one cycle; collapsing the attached trees/tails gives a strong deformation retraction onto $S^1$.
  - **Group 3 ($g = 2$, homotopy equivalent to $S^1 \vee S^1$):**
    $$\{\text{B}\}.$$
    Contains two cycles (two enclosed regions), hence deformation retracts to the figure eight $S^1 \vee S^1$.
  <2>3. Proof: By standard homotopy theory of 1-dimensional CW complexes. Q.E.D.

<1>3. Classification up to Homeomorphism ($\cong$).
  <2>1. Homeomorphism preserves:
  - The number of path components (all letters are connected).
  - The number of cycles / Euler characteristic / $\pi_1$.
  - For any point $p \in X$, the local degree / valence $d(p) = \lim_{\epsilon \to 0} | \pi_0(B_\epsilon(p) \setminus \{p\}) |$, i.e., the number of connected components formed locally by deleting $p$.
  - Consequently, the multiset of degrees of all branch points (points $p$ with local degree $\ge 3$) and end points (local degree $1$).
  <2>2. We partition the letters into homeomorphism equivalence classes using the cut-point invariant and graph valence profiles $(n_1, n_2, n_3, n_4)$ where $n_d$ is the number of vertices of valence $d$:
  - **Class 1 (Arcs $\cong [0, 1]$, endpoints = 2, no branch points):**
    $$\{\text{C, I, J, L, M, N, S, U, V, W, Z}\}.$$
    (Removing any interior point leaves 2 connected components; removing an endpoint leaves 1 connected component).
  - **Class 2 (Simple closed curve $\cong S^1$, no endpoints, no branch points):**
    $$\{\text{D, O}\}.$$
    (Removing any single point leaves 1 connected component).
  - **Class 3 (3 endpoints, one 3-way junction):**
    $$\{\text{E, F, T, Y}\}$$
    (Note: In standard sans-serif, T and Y have one degree-3 vertex and 3 degree-1 vertices; E and F also have one degree-3 vertex and 3 degree-1 vertices if written with a continuous vertical backbone and two/three horizontal bars—specifically F has one degree-3 vertex and 3 endpoints; E if written with 3 prongs has two degree-3 vertices and 3 endpoints, or if standard sans-serif E has two degree-3 vertices).
    Under standard single-junction models: $\{\text{T, Y}\}$ (and $\text{F}$ with top-bar corner, i.e. 1 junction of valence 3, 3 endpoints).
  - **Class 4 (4 endpoints, one 4-way junction):**
    $$\{\text{X}\}.$$
    (Removing the central intersection point yields 4 connected components; no other letter has a 4-way cut point).
  - **Class 5 (4 endpoints, two 3-way junctions):**
    $$\{\text{H, K}\}$$
    (Removing two specific points splits the letter into 5 components; 4 endpoints, two valence-3 vertices).
  - **Class 6 (1 loop with 1 tail, 1 endpoint, one 3-way junction):**
    $$\{\text{P, Q}\}.$$
    (Removing the junction point leaves 2 components: an open interval and a punctured loop).
  - **Class 7 (1 loop with 2 tails / theta graph with tails, two 3-way junctions):**
    $$\{\text{A, R}\}.$$
    (A has two endpoints, two degree-3 vertices, and one loop; R similarly in standard sans-serif has one loop, two degree-3 junctions, and two endpoints).
  - **Class 8 (Figure eight / theta graph, two loops, two 3-way junctions or one 4-way junction):**
    $$\{\text{B}\}.$$
    (Has 2 enclosed regions, uniquely distinguishing it from all other letters).
  <2>3. Proof: By local cut point degree invariants. Q.E.D.

<1>4. Q.E.D.
  <2>1. Proof: <1>2 gives the 3 homotopy classes, and <1>3 gives the topological classification by homeomorphism.
:::

