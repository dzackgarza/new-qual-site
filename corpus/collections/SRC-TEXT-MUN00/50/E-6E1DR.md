---
schema: qual/card@1
id: E-6E1DR
kind: exercise
title: Characterization of closed imbeddings into euclidean space
classification:
  areas:
  - topology
  topics:
  - Dimension
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Corollary.
A space $X$ can be imbedded as a closed subspace of $\mathbb{R}^N$ for some $N$ if and only if $X$ is locally compact and Hausdorff with a countable basis, and has finite topological dimension.
:::

::: solution
**Goal:** Prove that a topological space $X$ embeds as a closed subspace of some Euclidean space $\mathbb{R}^N$ if and only if $X$ is locally compact Hausdorff, second-countable, and of finite topological dimension $\dim X = m < \infty$.

<1>1. Direct implication ($\implies$):
    Suppose $h: X \to \mathbb{R}^N$ is an embedding onto a closed subspace $h(X) \subseteq \mathbb{R}^N$.
    *Proof:*
    <2>1. **Locally compact Hausdorff:** $\mathbb{R}^N$ is locally compact and Hausdorff. Closed subspaces of locally compact Hausdorff spaces are locally compact Hausdorff, so $X \cong h(X)$ is locally compact Hausdorff.
    <2>2. **Second-countable:** $\mathbb{R}^N$ is second-countable. Second-countability is hereditary to all subspaces, so $X$ has a countable basis.
    <2>3. **Finite topological dimension:** By the dimension properties of Euclidean space, $\dim \mathbb{R}^N = N$. Topological dimension is monotonic on subspaces, so $\dim X = \dim h(X) \le N < \infty$.

<1>2. Converse implication ($\impliedby$):
    Suppose $X$ is locally compact Hausdorff, second-countable, with topological dimension $\dim X = m < \infty$.
    *Proof:*
    <2>1. **One-point compactification:** Let $X^* = X \cup \{\infty\}$ be the one-point compactification of $X$. Since $X$ is locally compact Hausdorff and second-countable, $X^*$ is a compact metrizable space with $\dim X^* = \dim X = m$.
    <2>2. **Embedding of compactification:** By the Munkres / Nagami / Pontryagin Imbedding Theorem (Theorem 50.5), there exists a topological embedding $g: X^* \to \mathbb{R}^{2m+1}$.
    <2>3. **Construction of closed embedding into $\mathbb{R}^{2m+2}$:**
        Let $p_0 = g(\infty) \in \mathbb{R}^{2m+1}$. For $x \in X$, $g(x) \neq p_0$.
        Define $F: X \to \mathbb{R}^{2m+1} \times \mathbb{R} = \mathbb{R}^{2m+2}$ by:
        $$F(x) = \left( g(x), \frac{1}{\|g(x) - p_0\|} \right).$$
    <2>4. **Embedding and properness:**
        - Since $g$ and $\|\cdot - p_0\|^{-1}$ are continuous, $F$ is continuous.
        - Since $g|_X$ is injective, $F$ is injective.
        - If a sequence $(x_k)$ in $X$ leaves every compact set of $X$, then $x_k \to \infty$ in $X^*$.
        - Then $g(x_k) \to g(\infty) = p_0$, so $\|g(x_k) - p_0\| \to 0$, which forces the last coordinate $\frac{1}{\|g(x_k) - p_0\|} \to \infty$.
        - Hence $\|F(x_k)\| \to \infty$, showing that $F$ is a proper map.
    <2>5. Any proper continuous injection into a Hausdorff space is a closed embedding, so $F(X)$ is closed in $\mathbb{R}^{2m+2}$.

<1>3. Conclusion:
    $X$ embeds as a closed subspace of $\mathbb{R}^{2m+2}$ with $N = 2m+2$. Q.E.D.
:::
