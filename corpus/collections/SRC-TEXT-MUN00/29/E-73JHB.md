---
schema: qual/card@1
id: E-73JHB
kind: problem
title: The one-point compactification of the positive integers
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that the one-point compactification of $\mathbb{Z}_+$ is homeomorphic with the subspace $\ts{0} \cup \ts{1/n \mid n \in \mathbb{Z}_+}$ of $\mathbb{R}$.
:::

::: {.solution}
**Goal:** Prove that the one-point compactification $\mathbb{Z}_+^* = \mathbb{Z}_+ \cup \{\infty\}$ of the discrete space $\mathbb{Z}_+$ is homeomorphic to the subspace $K = \{0\} \cup \{1/n \mid n \in \mathbb{Z}_+\} \subset \mathbb{R}$.

::: pf

::: pf-step
Structure of the one-point compactification $\mathbb{Z}_+^*$:

::: pf-proof

::: pf-step
The positive integers $\mathbb{Z}_+$ carry the discrete topology, where every subset is open and compact subsets are precisely the finite subsets.
:::

::: pf-step
The one-point compactification $\mathbb{Z}_+^* = \mathbb{Z}_+ \cup \{\infty\}$ is a compact Hausdorff space whose topology consists of all subsets of $\mathbb{Z}_+$ together with all sets of the form $(\mathbb{Z}_+ \setminus F) \cup \{\infty\}$ where $F \subset \mathbb{Z}_+$ is finite.
:::

:::

:::

::: pf-step
Construction and bijectivity of the candidate map:
Define $f: \mathbb{Z}_+^* \to K$ by:
$$f(n) = \frac{1}{n} \quad \text{for } n \in \mathbb{Z}_+, \qquad f(\infty) = 0.$$

::: pf-proof

::: pf-step
$f$ maps $\mathbb{Z}_+$ bijectively onto $\{1/n \mid n \in \mathbb{Z}_+\}$.
:::

::: pf-step
$f$ maps $\infty$ to $0 \notin \{1/n \mid n \in \mathbb{Z}_+\}$.
:::

::: pf-step
Thus $f: \mathbb{Z}_+^* \to K$ is a well-defined bijection.
:::

:::

:::

::: pf-step
Continuity of $f$:

::: pf-proof

::: pf-step
For each $n \in \mathbb{Z}_+$, $\{n\}$ is an open singleton in $\mathbb{Z}_+^*$, so $f$ is continuous at $n$.
:::

::: pf-step
Let $V \subseteq K$ be an open neighborhood of $f(\infty) = 0$ in the subspace topology of $K$.
:::

::: pf-step
There exists $\varepsilon > 0$ such that $(-\varepsilon, \varepsilon) \cap K \subseteq V$.
:::

::: pf-step
Choose $N \in \mathbb{Z}_+$ such that $\frac{1}{N} < \varepsilon$.
:::

::: pf-step
For all $n \ge N$, $0 < f(n) = \frac{1}{n} \le \frac{1}{N} < \varepsilon$, so $f(n) \in V$.
:::

::: pf-step
Thus $f^{-1}(V) \supseteq (\mathbb{Z}_+ \setminus \{1, \dots, N-1\}) \cup \{\infty\}$.
:::

::: pf-step
Because $\{1, \dots, N-1\}$ is finite, this preimage is an open neighborhood of $\infty$ in $\mathbb{Z}_+^*$.
:::

::: pf-step
Hence $f$ is continuous at $\infty$, and thus continuous on all of $\mathbb{Z}_+^*$.
:::

:::

:::

::: pf-step
Homeomorphism conclusion:

::: pf-proof

::: pf-step
The domain $\mathbb{Z}_+^*$ is compact.
:::

::: pf-step
The codomain $K \subset \mathbb{R}$ is Hausdorff.
:::

::: pf-step
Any continuous bijection from a compact space to a Hausdorff space is a homeomorphism.
:::

::: pf-step
Therefore, $f: \mathbb{Z}_+^* \to K$ is a homeomorphism. Q.E.D.
:::

:::

:::

:::

:::
