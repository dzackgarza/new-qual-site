---
schema: qual/card@1
id: P-AMD-2GG7VEF2
kind: problem
title: $\pi_1(S^n)=1$ for $n\geq 2$
classification:
  areas:
  - topology
  topics:
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
Show $\pi_1(S^n) = 1$ for $n\geq 2$.
:::

::: {.solution}
**Goal:** Prove that for all integers $n \geq 2$, the fundamental group $\pi_1(S^n, x_0)$ is trivial.

::: pf

::: pf-step
Cover $S^n$ by two open subsets $U$ and $V$.

::: pf-proof

::: pf-step
Let $N = (0, \dots, 0, 1) \in S^n \subset \mathbb{R}^{n+1}$ (North pole) and $S = (0, \dots, 0, -1) \in S^n$ (South pole).
:::

::: pf-step
Define $U = S^n \setminus \{S\}$ and $V = S^n \setminus \{N\}$.
:::

::: pf-step
Since $\{S\}$ and $\{N\}$ are closed singletons in $S^n$, $U$ and $V$ are open in $S^n$.
:::

::: pf-step
$U \cup V = S^n$ because $N \neq S$, so no point in $S^n$ is equal to both $N$ and $S$.

::: pf-proof
Every point of $S^n$ is either not equal to $S$ (so it lies in $U$) or not equal to $N$ (so it lies in $V$); since $N \neq S$, the two sets cover $S^n$.
:::

:::

:::

:::

::: {.pf-step #s2}
$U$ and $V$ are contractible, hence simply connected.

::: pf-proof

::: pf-step
Stereographic projection from $S$ is a homeomorphism $U \to \mathbb{R}^n$.
:::

::: pf-step
Stereographic projection from $N$ is a homeomorphism $V \to \mathbb{R}^n$.
:::

::: pf-step
$\mathbb{R}^n$ is convex, hence contractible to the origin via straight-line homotopy $H(x, t) = (1-t)x$.
:::

::: pf-step
Therefore, $U \simeq * \implies \pi_1(U, x_0) = 1$ and $V \simeq * \implies \pi_1(V, x_0) = 1$ for any basepoint $x_0 \in U \cap V$.

::: pf-proof
A homeomorphism preserves contractibility, and a contractible space is simply connected, so $\pi_1(U, x_0) = \pi_1(V, x_0) = 1$.
:::

:::

:::

:::

::: pf-step
The intersection $U \cap V = S^n \setminus \{N, S\}$ is path-connected for $n \geq 2$.

::: pf-proof

::: {.pf-step #s3-1}
Under stereographic projection $\phi \colon U \to \mathbb{R}^n$, the pole $N$ maps to $0 \in \mathbb{R}^n$.
:::

::: {.pf-step #s3-2}
Thus $U \cap V = U \setminus \{N\} \cong \mathbb{R}^n \setminus \{0\}$.
:::

::: {.pf-step #s3-3}
$\mathbb{R}^n \setminus \{0\}$ deformation retracts to $S^{n-1}$ via $x \mapsto \frac{x}{\|x\|}$.
:::

::: {.pf-step #s3-4}
For $n \geq 2$, the sphere $S^{n-1}$ has dimension $n-1 \geq 1$, which is path-connected.
:::

::: pf-step
Therefore, $\mathbb{R}^n \setminus \{0\}$ is path-connected, which implies $U \cap V$ is path-connected.

::: pf-proof
By steps [](#s3-1){.pf-ref} and [](#s3-2){.pf-ref}, $U \cap V \cong \mathbb{R}^n \setminus \{0\}$; by steps [](#s3-3){.pf-ref} and [](#s3-4){.pf-ref}, $\mathbb{R}^n \setminus \{0\}$ deformation retracts to the path-connected sphere $S^{n-1}$ for $n \ge 2$, so $U \cap V$ is nonempty and path-connected.
:::

:::

:::

:::

::: {.pf-step #s4}
Apply the Seifert-van Kampen theorem to the cover $\{U, V\}$.

::: pf-proof

::: pf-step
Let $x_0 \in U \cap V$ be the basepoint.
:::

::: pf-step
The hypotheses of the Seifert-van Kampen theorem are satisfied: $U, V$ are open, $U \cup V = S^n$, and $U \cap V$ is path-connected.
:::

::: {.pf-step #s4-3}
The theorem gives an isomorphism: $$\pi_1(S^n, x_0) \cong \pi_1(U, x_0) *_{\pi_1(U \cap V, x_0)} \pi_1(V, x_0).$$
:::

::: pf-step
By step [](#s2){.pf-ref}, $\pi_1(U, x_0) = 1$ and $\pi_1(V, x_0) = 1$.
:::

::: pf-step
The amalgamated free product of two trivial groups is trivial: $1 *_{\pi_1(U \cap V, x_0)} 1 = 1$.

::: pf-proof
Substituting $\pi_1(U, x_0) = 1$ and $\pi_1(V, x_0) = 1$ from step [](#s2){.pf-ref} into the van Kampen isomorphism of step [](#s4-3){.pf-ref} gives $\pi_1(S^n, x_0) \cong 1 *_{\pi_1(U \cap V, x_0)} 1 = 1$.
:::

:::

:::

:::

::: pf-qed
Step [](#s4){.pf-ref} establishes $\pi_1(S^n, x_0) = 1$ for all $n \geq 2$.
:::

:::
:::
