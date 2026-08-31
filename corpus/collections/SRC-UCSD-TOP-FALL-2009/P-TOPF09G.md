---
schema: qual/card@1
id: P-TOPF09G
kind: problem
title: "Suspension of a homology 3-sphere is homotopy equivalent to S^4"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Suspensions
  - Homotopy Type
  - Manifolds
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Let $M^3$ be a homology sphere: a connected closed compact $3$-manifold with the same homology groups as $S^3$.
Calculate the fundamental group and homology of the suspension $\Sigma M$.
Use this to show that the suspension is homotopy-equivalent to $S^4$.
:::

::: solution
**Goal:** Compute the fundamental group $\pi_1(\Sigma M)$ and homology groups $H_*(\Sigma M)$ of the suspension of a homology 3-sphere $M$, and prove that $\Sigma M \simeq S^4$.

<1>1. Fundamental group of $\Sigma M$:
    *Proof:*
    <2>1. The suspension $\Sigma M$ is the quotient of $M \times [-1, 1]$ identifying $M \times \{1\}$ to a north cone point $N$ and $M \times \{-1\}$ to a south cone point $S$.
    <2>2. Decompose $\Sigma M = U \cup V$ with open sets $U = \Sigma M \setminus \{S\}$ and $V = \Sigma M \setminus \{N\}$.
    <2>3. The open cone $U$ deformation retracts to the point $N$, and $V$ deformation retracts to $S$, so both $U$ and $V$ are contractible ($\pi_1(U) = \pi_1(V) = \{e\}$).
    <2>4. The intersection $U \cap V = M \times (-1, 1)$ deformation retracts to $M$, which is path-connected by hypothesis.
    <2>5. By the Seifert–van Kampen Theorem:
    $$\pi_1(\Sigma M) \cong \pi_1(U) *_{\pi_1(U \cap V)} \pi_1(V) \cong \{e\} *_{\pi_1(M)} \{e\} \cong \{e\}.$$
    <2>6. Thus $\Sigma M$ is simply connected: $\pi_1(\Sigma M) = 0$.

<1>2. Homology groups of $\Sigma M$:
    *Proof:*
    <2>1. Apply the Mayer–Vietoris sequence to the open cover $\{U, V\}$ of $\Sigma M$:
    $$\cdots \to \widetilde{H}_k(U) \oplus \widetilde{H}_k(V) \to \widetilde{H}_k(\Sigma M) \xrightarrow{\partial_*} \widetilde{H}_{k-1}(U \cap V) \to \widetilde{H}_{k-1}(U) \oplus \widetilde{H}_{k-1}(V) \to \cdots$$
    <2>2. Since $U$ and $V$ are contractible, $\widetilde{H}_k(U) = \widetilde{H}_k(V) = 0$ for all $k$, yielding the suspension isomorphism:
    $$\widetilde{H}_k(\Sigma M) \cong \widetilde{H}_{k-1}(U \cap V) \cong \widetilde{H}_{k-1}(M) \quad \text{for all } k \ge 1.$$
    <2>3. Since $M$ is a homology 3-sphere, its reduced homology is $\widetilde{H}_3(M) \cong \mathbb{Z}$ and $\widetilde{H}_j(M) = 0$ for all $j \neq 3$.
    <2>4. Therefore, the reduced homology groups of $\Sigma M$ are:
    $$\widetilde{H}_k(\Sigma M) \cong \begin{cases} \mathbb{Z} & k = 4, \\ 0 & k \neq 4. \end{cases}$$

<1>3. Homotopy equivalence $\Sigma M \simeq S^4$ via Hurewicz and Whitehead:
    *Proof:*
    <2>1. Since $\Sigma M$ is simply connected ($\pi_1(\Sigma M) = 0$) and $\widetilde{H}_k(\Sigma M) = 0$ for $1 \le k \le 3$, the Hurewicz Theorem implies that:
    $$\pi_2(\Sigma M) = 0, \qquad \pi_3(\Sigma M) = 0,$$
    and the Hurewicz homomorphism $h: \pi_4(\Sigma M) \to H_4(\Sigma M) \cong \mathbb{Z}$ is an isomorphism.
    <2>2. Choose a continuous map $f: S^4 \to \Sigma M$ representing a generator of $\pi_4(\Sigma M) \cong \mathbb{Z}$.
    <2>3. By construction, $f_*: H_4(S^4; \mathbb{Z}) \to H_4(\Sigma M; \mathbb{Z})$ is an isomorphism.
    <2>4. In all other degrees $k \neq 4$, $H_k(S^4) \cong H_k(\Sigma M)$ are either $\mathbb{Z}$ (for $k = 0$) or $0$ (for $k \neq 0, 4$), so $f_*: H_k(S^4; \mathbb{Z}) \to H_k(\Sigma M; \mathbb{Z})$ is an isomorphism for every $k \ge 0$.
    <2>5. By Moise's Theorem, every compact 3-manifold is triangulable as a finite simplicial complex, so the suspension $\Sigma M$ is a finite 4-dimensional CW complex.
    <2>6. By Whitehead's Theorem (homological version for simply connected CW complexes), a homology isomorphism between simply connected CW complexes is a homotopy equivalence.
    <2>7. Therefore $f: S^4 \to \Sigma M$ is a homotopy equivalence, so $\Sigma M \simeq S^4$.

<1>4. Conclusion:
    *Proof:*
    $\pi_1(\Sigma M) = 0$, $\widetilde{H}_*(\Sigma M) \cong \widetilde{H}_*(S^4)$, and $\Sigma M \simeq S^4$.
:::
