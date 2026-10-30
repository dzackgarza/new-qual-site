---
schema: qual/card@1
id: E-6E1DR
kind: problem
title: Characterization of closed imbeddings into $\RR^N$
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
A space $X$ can be imbedded as a closed subspace of $\RR^N$ for some $N$ if and only if $X$ is locally compact and Hausdorff with a countable basis, and has finite topological dimension.
:::

::: {.solution}
::: pf

::: {.pf-step #s1}
Direct implication ($\implies$): Suppose $h: X \to \RR^N$ is an embedding onto a closed subspace $h(X) \subseteq \RR^N$.

::: pf-proof

::: pf-step
**Locally compact Hausdorff:** $\RR^N$ is locally compact and Hausdorff.
Closed subspaces of locally compact Hausdorff spaces are locally compact Hausdorff, so $X \cong h(X)$ is locally compact Hausdorff.
:::

::: pf-step
**Second-countable:** $\RR^N$ is second-countable.
Second-countability is hereditary to all subspaces, so $X$ has a countable basis.
:::

::: pf-step
**Finite topological dimension:** By the dimension properties of Euclidean space, $\dim \RR^N = N$.
Topological dimension is monotonic on subspaces, so $\dim X = \dim h(X) \le N < \infty$.
:::

:::

:::

::: {.pf-step #s2}
Converse implication ($\impliedby$): Suppose $X$ is locally compact Hausdorff, second-countable, with topological dimension $\dim X = m < \infty$.

::: pf-proof

::: pf-step
**One-point compactification:** Let $X^* = X \cup \{\infty\}$ be the one-point compactification of $X$.
Since $X$ is locally compact Hausdorff and second-countable, $X^*$ is a compact metrizable space with $\dim X^* = \dim X = m$.
:::

::: pf-step
**Embedding of compactification:** By the imbedding theorem for compact metrizable spaces (Theorem 50.5), a compact metrizable space of topological dimension $m$ imbeds in $\RR^{2m+1}$, so there exists a topological embedding $g: X^* \to \RR^{2m+1}$.
:::

::: pf-step
**Construction of closed embedding into $\RR^{2m+2}$:** Let $p_0 = g(\infty) \in \RR^{2m+1}$.
For $x \in X$, $g(x) \neq p_0$.
Define $F: X \to \RR^{2m+1} \times \RR = \RR^{2m+2}$ by: $$F(x) = \left( g(x), \frac{1}{\norm{g(x) - p_0}} \right).$$
:::

::: pf-step
**Embedding and properness:**
- Since $g$ and $\norm{\cdot - p_0}^{-1}$ are continuous, $F$ is continuous.

- Since $g\restrict_X$ is injective, $F$ is injective.

- If a sequence $(x_k)$ in $X$ leaves every compact set of $X$, then $x_k \to \infty$ in $X^*$.

- Then $g(x_k) \to g(\infty) = p_0$, so $\norm{g(x_k) - p_0} \to 0$, which forces the last coordinate $\frac{1}{\norm{g(x_k) - p_0}} \to \infty$.

- Hence $\norm{F(x_k)} \to \infty$, showing that $F$ is a proper map.
:::

::: pf-step
Any proper continuous injection into a Hausdorff space is a closed embedding, so $F(X)$ is closed in $\RR^{2m+2}$.
:::

:::

:::

::: pf-qed
Step [](#s1){.pf-ref} proves the forward implication, and step [](#s2){.pf-ref} imbeds $X$ as a closed subspace of $\RR^N$ with $N = 2m+2$.
:::

:::

:::
