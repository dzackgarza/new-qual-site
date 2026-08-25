---
schema: qual/card@1
id: P-AMD-DDQM3X6Q
kind: problem
title: $\tilde H_i(\Sigma X)\cong\tilde H_{i-1}(X)$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
relations: []
review: draft
---

::: {.problem}
Show $\tilde H_i(\Sigma X) \cong \tilde H_{i-1}(X)$

1. Show $\Sigma S^n \cong S^{n+1}$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $X$ be a topological space.
Prove that the suspension $\Sigma X = (X \times [-1, 1]) / (X \times \{1\} \sim N, X \times \{-1\} \sim S)$ satisfies $\widetilde{H}_i(\Sigma X) \cong \widetilde{H}_{i-1}(X)$ for all $i \in \mathbb{Z}$, and prove that $\Sigma S^n \cong S^{n+1}$ for all $n \ge 0$.

<1>1. Prove the suspension isomorphism $\widetilde{H}_i(\Sigma X) \cong \widetilde{H}_{i-1}(X)$.
<2>1. Decompose $\Sigma X$ into two open cones:

- $U = (X \times (-1, 1]) / (X \times \{1\} \sim N) = C_+ X \setminus \{S\}$,

- $V = (X \times [-1, 1)) / (X \times \{-1\} \sim S) = C_- X \setminus \{N\}$.
  <2>2. $U$ and $V$ are open in $\Sigma X$, and $U \cup V = \Sigma X$.
  <2>3. $U$ deformation retracts to the north cone vertex $N$, and $V$ deformation retracts to the south cone vertex $S$.
  Thus $\widetilde{H}_k(U) = 0$ and $\widetilde{H}_k(V) = 0$ for all $k \ge 0$.
  <2>4. The intersection $U \cap V = X \times (-1, 1)$ deformation retracts onto $X \times \{0\} \cong X$.
  Thus $\widetilde{H}_k(U \cap V) \cong \widetilde{H}_k(X)$ for all $k \ge 0$.
  <2>5. Write the Mayer-Vietoris sequence in reduced homology for $(\Sigma X; U, V)$: $$\cdots \to \widetilde{H}_i(U) \oplus \widetilde{H}_i(V) \to \widetilde{H}_i(\Sigma X) \xrightarrow{\partial} \widetilde{H}_{i-1}(U \cap V) \to \widetilde{H}_{i-1}(U) \oplus \widetilde{H}_{i-1}(V) \to \cdots$$ <2>6. Substituting the vanishing groups from <2>3 gives exact sequences: $$0 \longrightarrow \widetilde{H}_i(\Sigma X) \xrightarrow{\partial} \widetilde{H}_{i-1}(X) \longrightarrow 0.$$ <2>7. Therefore, the connecting homomorphism $\partial \colon \widetilde{H}_i(\Sigma X) \xrightarrow{\cong} \widetilde{H}_{i-1}(X)$ is an isomorphism for all $i \in \mathbb{Z}$.
  <2>8. Proof: By Mayer-Vietoris sequence for the suspension open cover.
  Q.E.D.

<1>2. Prove $\Sigma S^n \cong S^{n+1}$.
<2>1. Realize $S^n \subset \mathbb{R}^{n+1}$ as $\{x \in \mathbb{R}^{n+1} \mid \|x\| = 1\}$, and $S^{n+1} \subset \mathbb{R}^{n+2} = \mathbb{R}^{n+1} \times \mathbb{R}$ as $\{(x, t) \in \mathbb{R}^{n+1} \times \mathbb{R} \mid \|x\|^2 + t^2 = 1\}$.
<2>2. Define a map $f \colon S^n \times [-1, 1] \to S^{n+1}$ by: $$f(u, t) = \left( \sqrt{1 - t^2} \, u, \, t \right) \in \mathbb{R}^{n+1} \times \mathbb{R}.$$ <2>3. Verify the image and continuity of $f$:

- For any $u \in S^n$ and $t \in [-1, 1]$, $\|\sqrt{1-t^2} u\|^2 + t^2 = (1-t^2)\|u\|^2 + t^2 = (1-t^2)(1) + t^2 = 1$.

- Thus $f(u, t) \in S^{n+1}$, and $f$ is continuous as a composition of elementary continuous functions.
  <2>4. Check the fibers of $f$:

- At $t = 1$: $f(u, 1) = (0, 1) = N \in S^{n+1}$ for all $u \in S^n$.

- At $t = -1$: $f(u, -1) = (0, -1) = S \in S^{n+1}$ for all $u \in S^n$.

- For $t \in (-1, 1)$: $f(u, t) = (x, t) \implies \sqrt{1-t^2} u = x \implies u = \frac{x}{\sqrt{1-t^2}}$, which determines $u$ uniquely because $\sqrt{1-t^2} > 0$.
  <2>5. $f$ is surjective: For any $(x, t) \in S^{n+1}$, $|t| \le 1$.
  If $|t| < 1$, set $u = x / \sqrt{1-t^2} \in S^n$, then $f(u, t) = (x, t)$.
  If $t = \pm 1$, $(x, t) = (0, \pm 1) = f(u, \pm 1)$.
  <2>6. Thus $f$ induces a continuous bijection from the quotient space $\Sigma S^n = (S^n \times [-1, 1]) / (S^n \times \{1\} \sim N, S^n \times \{-1\} \sim S)$ onto $S^{n+1}$.
  <2>7. Since $\Sigma S^n$ is compact (quotient of compact $S^n \times [-1, 1]$) and $S^{n+1}$ is Hausdorff, any continuous bijection $\overline{f} \colon \Sigma S^n \to S^{n+1}$ is a homeomorphism.
  <2>8. Proof: By compact-to-Hausdorff homeomorphism theorem.
  Q.E.D.

<1>3. Q.E.D. <2>1. Proof: <1>1 establishes the suspension isomorphism and <1>2 establishes $\Sigma S^n \cong S^{n+1}$.
:::
