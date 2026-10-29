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

Show that the one-point compactification of $\ZZ_+$ is homeomorphic with the subspace $\theset{0} \cup \theset{1/n \mid n \in \ZZ_+}$ of $\RR$.
:::

::: {.solution}

Write $\ZZ_+^* = \ZZ_+ \cup \{\infty\}$ for the one-point compactification of the discrete space $\ZZ_+$, and $K = \{0\} \cup \{1/n \mid n \in \ZZ_+\} \subset \RR$.

::: pf

::: pf-step
Structure of the one-point compactification $\ZZ_+^*$:

::: pf-proof

::: pf-step
The positive integers $\ZZ_+$ carry the discrete topology, where every subset is open and compact subsets are precisely the finite subsets.
:::

::: pf-step
The one-point compactification $\ZZ_+^* = \ZZ_+ \cup \{\infty\}$ is a compact Hausdorff space whose topology consists of all subsets of $\ZZ_+$ together with all sets of the form $(\ZZ_+ \setminus F) \cup \{\infty\}$ where $F \subset \ZZ_+$ is finite.
:::

:::

:::

::: pf-step
Construction and bijectivity of the candidate map:
Define $f: \ZZ_+^* \to K$ by:
$$f(n) = \frac{1}{n} \quad \text{for } n \in \ZZ_+, \qquad f(\infty) = 0.$$

::: pf-proof

::: pf-step
$f$ maps $\ZZ_+$ bijectively onto $\{1/n \mid n \in \ZZ_+\}$.
:::

::: pf-step
$f$ maps $\infty$ to $0 \notin \{1/n \mid n \in \ZZ_+\}$.
:::

::: pf-step
Thus $f: \ZZ_+^* \to K$ is a well-defined bijection.
:::

:::

:::

::: pf-step
Continuity of $f$:

::: pf-proof

::: pf-step
For each $n \in \ZZ_+$, $\{n\}$ is an open singleton in $\ZZ_+^*$, so $f$ is continuous at $n$.
:::

::: pf-step
Let $V \subseteq K$ be an open neighborhood of $f(\infty) = 0$ in the subspace topology of $K$.
:::

::: pf-step
There exists $\varepsilon > 0$ such that $(-\varepsilon, \varepsilon) \cap K \subseteq V$.
:::

::: pf-step
Choose $N \in \ZZ_+$ such that $\frac{1}{N} < \varepsilon$.
:::

::: pf-step
For all $n \ge N$, $0 < f(n) = \frac{1}{n} \le \frac{1}{N} < \varepsilon$, so $f(n) \in V$.
:::

::: pf-step
Thus $f^{-1}(V) \supseteq (\ZZ_+ \setminus \{1, \dots, N-1\}) \cup \{\infty\}$.
:::

::: pf-step
Because $\{1, \dots, N-1\}$ is finite, this preimage is an open neighborhood of $\infty$ in $\ZZ_+^*$.
:::

::: pf-step
Hence $f$ is continuous at $\infty$, and thus continuous on all of $\ZZ_+^*$.
:::

:::

:::

::: pf-step
Homeomorphism conclusion:

::: pf-proof

::: pf-step
The domain $\ZZ_+^*$ is compact.
:::

::: pf-step
The codomain $K \subset \RR$ is Hausdorff.
:::

::: pf-step
Any continuous bijection from a compact space to a Hausdorff space is a homeomorphism.
:::

::: pf-step
Therefore, $f: \ZZ_+^* \to K$ is a homeomorphism. Q.E.D.
:::

:::

:::

:::

:::
