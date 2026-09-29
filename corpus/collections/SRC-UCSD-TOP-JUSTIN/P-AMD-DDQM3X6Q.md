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
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Show $\tilde H_i(\Sigma X) \cong \tilde H_{i-1}(X)$

1. Show $\Sigma S^n \cong S^{n+1}$
:::

::: {.solution}
**Goal:** Let $X$ be a topological space.
Prove that the suspension $\Sigma X = (X \times [-1, 1]) / (X \times \{1\} \sim N, X \times \{-1\} \sim S)$ satisfies $\widetilde{H}_i(\Sigma X) \cong \widetilde{H}_{i-1}(X)$ for all $i \in \mathbb{Z}$, and prove that $\Sigma S^n \cong S^{n+1}$ for all $n \ge 0$.

::: pf

::: {.pf-step #s1}
Prove the suspension isomorphism $\widetilde{H}_i(\Sigma X) \cong \widetilde{H}_{i-1}(X)$.

::: pf-proof

::: pf-step
Decompose $\Sigma X$ into two open cones:

- $U = (X \times (-1, 1]) / (X \times \{1\} \sim N) = C_+ X \setminus \{S\}$,

- $V = (X \times [-1, 1)) / (X \times \{-1\} \sim S) = C_- X \setminus \{N\}$.
:::

::: pf-step
$U$ and $V$ are open in $\Sigma X$, and $U \cup V = \Sigma X$.
:::

::: {.pf-step #s1-3}
$U$ deformation retracts to the north cone vertex $N$, and $V$ deformation retracts to the south cone vertex $S$.
Thus $\widetilde{H}_k(U) = 0$ and $\widetilde{H}_k(V) = 0$ for all $k \ge 0$.
:::

::: pf-step
The intersection $U \cap V = X \times (-1, 1)$ deformation retracts onto $X \times \{0\} \cong X$.
Thus $\widetilde{H}_k(U \cap V) \cong \widetilde{H}_k(X)$ for all $k \ge 0$.
:::

::: pf-step
Write the Mayer-Vietoris sequence in reduced homology for $(\Sigma X; U, V)$: $$\cdots \to \widetilde{H}_i(U) \oplus \widetilde{H}_i(V) \to \widetilde{H}_i(\Sigma X) \xrightarrow{\partial} \widetilde{H}_{i-1}(U \cap V) \to \widetilde{H}_{i-1}(U) \oplus \widetilde{H}_{i-1}(V) \to \cdots$$
:::

::: pf-step
Substituting the vanishing groups from step [](#s1-3){.pf-ref} gives exact sequences: $$0 \longrightarrow \widetilde{H}_i(\Sigma X) \xrightarrow{\partial} \widetilde{H}_{i-1}(X) \longrightarrow 0.$$
:::

::: pf-step
Therefore, the connecting homomorphism $\partial \colon \widetilde{H}_i(\Sigma X) \xrightarrow{\cong} \widetilde{H}_{i-1}(X)$ is an isomorphism for all $i \in \mathbb{Z}$.
:::

::: pf-qed
Substituting $\widetilde{H}_*(U) = \widetilde{H}_*(V) = 0$ into the Mayer–Vietoris sequence of the suspension open cover leaves the short exact sequence $0 \to \widetilde{H}_i(\Sigma X) \xrightarrow{\partial} \widetilde{H}_{i-1}(X) \to 0$, so $\partial$ is an isomorphism.
:::

:::

:::

::: {.pf-step #s2}
Prove $\Sigma S^n \cong S^{n+1}$.

::: pf-proof

::: pf-step
Realize $S^n \subset \mathbb{R}^{n+1}$ as $\{x \in \mathbb{R}^{n+1} \mid \|x\| = 1\}$, and $S^{n+1} \subset \mathbb{R}^{n+2} = \mathbb{R}^{n+1} \times \mathbb{R}$ as $\{(x, t) \in \mathbb{R}^{n+1} \times \mathbb{R} \mid \|x\|^2 + t^2 = 1\}$.
:::

::: pf-step
Define a map $f \colon S^n \times [-1, 1] \to S^{n+1}$ by: $$f(u, t) = \left( \sqrt{1 - t^2} \, u, \, t \right) \in \mathbb{R}^{n+1} \times \mathbb{R}.$$
:::

::: pf-step
Verify the image and continuity of $f$:

- For any $u \in S^n$ and $t \in [-1, 1]$, $\|\sqrt{1-t^2} u\|^2 + t^2 = (1-t^2)\|u\|^2 + t^2 = (1-t^2)(1) + t^2 = 1$.

- Thus $f(u, t) \in S^{n+1}$, and $f$ is continuous as a composition of elementary continuous functions.
:::

::: pf-step
Check the fibers of $f$:

- At $t = 1$: $f(u, 1) = (0, 1) = N \in S^{n+1}$ for all $u \in S^n$.

- At $t = -1$: $f(u, -1) = (0, -1) = S \in S^{n+1}$ for all $u \in S^n$.

- For $t \in (-1, 1)$: $f(u, t) = (x, t) \implies \sqrt{1-t^2} u = x \implies u = \frac{x}{\sqrt{1-t^2}}$, which determines $u$ uniquely because $\sqrt{1-t^2} > 0$.
:::

::: pf-step
$f$ is surjective: For any $(x, t) \in S^{n+1}$, $|t| \le 1$.
If $|t| < 1$, set $u = x / \sqrt{1-t^2} \in S^n$, then $f(u, t) = (x, t)$.
If $t = \pm 1$, $(x, t) = (0, \pm 1) = f(u, \pm 1)$.
:::

::: pf-step
Thus $f$ induces a continuous bijection from the quotient space $\Sigma S^n = (S^n \times [-1, 1]) / (S^n \times \{1\} \sim N, S^n \times \{-1\} \sim S)$ onto $S^{n+1}$.
:::

::: pf-step
Since $\Sigma S^n$ is compact (quotient of compact $S^n \times [-1, 1]$) and $S^{n+1}$ is Hausdorff, any continuous bijection $\overline{f} \colon \Sigma S^n \to S^{n+1}$ is a homeomorphism.

::: pf-proof
A continuous bijection from a compact space to a Hausdorff space is a homeomorphism, so $\overline{f}$ is a homeomorphism.
:::

:::

:::

:::

::: pf-qed
Step [](#s1){.pf-ref} establishes the suspension isomorphism and step [](#s2){.pf-ref} establishes $\Sigma S^n \cong S^{n+1}$.
:::

:::
:::
