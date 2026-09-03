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

::: solution
**Goal:** Prove that the one-point compactification $\mathbb{Z}_+^* = \mathbb{Z}_+ \cup \{\infty\}$ of the discrete space $\mathbb{Z}_+$ is homeomorphic to the subspace $K = \{0\} \cup \{1/n \mid n \in \mathbb{Z}_+\} \subset \mathbb{R}$.

<1>1. Structure of the one-point compactification $\mathbb{Z}_+^*$:
    *Proof:*
    <2>1. The positive integers $\mathbb{Z}_+$ carry the discrete topology, where every subset is open and compact subsets are precisely the finite subsets.
    <2>2. The one-point compactification $\mathbb{Z}_+^* = \mathbb{Z}_+ \cup \{\infty\}$ is a compact Hausdorff space whose topology consists of all subsets of $\mathbb{Z}_+$ together with all sets of the form $(\mathbb{Z}_+ \setminus F) \cup \{\infty\}$ where $F \subset \mathbb{Z}_+$ is finite.

<1>2. Construction and bijectivity of the candidate map:
    Define $f: \mathbb{Z}_+^* \to K$ by:
    $$f(n) = \frac{1}{n} \quad \text{for } n \in \mathbb{Z}_+, \qquad f(\infty) = 0.$$
    *Proof:*
    <2>1. $f$ maps $\mathbb{Z}_+$ bijectively onto $\{1/n \mid n \in \mathbb{Z}_+\}$.
    <2>2. $f$ maps $\infty$ to $0 \notin \{1/n \mid n \in \mathbb{Z}_+\}$.
    <2>3. Thus $f: \mathbb{Z}_+^* \to K$ is a well-defined bijection.

<1>3. Continuity of $f$:
    *Proof:*
    <2>1. For each $n \in \mathbb{Z}_+$, $\{n\}$ is an open singleton in $\mathbb{Z}_+^*$, so $f$ is continuous at $n$.
    <2>2. Let $V \subseteq K$ be an open neighborhood of $f(\infty) = 0$ in the subspace topology of $K$.
    <2>3. There exists $\varepsilon > 0$ such that $(-\varepsilon, \varepsilon) \cap K \subseteq V$.
    <2>4. Choose $N \in \mathbb{Z}_+$ such that $\frac{1}{N} < \varepsilon$.
    <2>5. For all $n \ge N$, $0 < f(n) = \frac{1}{n} \le \frac{1}{N} < \varepsilon$, so $f(n) \in V$.
    <2>6. Thus $f^{-1}(V) \supseteq (\mathbb{Z}_+ \setminus \{1, \dots, N-1\}) \cup \{\infty\}$.
    <2>7. Because $\{1, \dots, N-1\}$ is finite, this preimage is an open neighborhood of $\infty$ in $\mathbb{Z}_+^*$.
    <2>8. Hence $f$ is continuous at $\infty$, and thus continuous on all of $\mathbb{Z}_+^*$.

<1>4. Homeomorphism conclusion:
    *Proof:*
    <2>1. The domain $\mathbb{Z}_+^*$ is compact.
    <2>2. The codomain $K \subset \mathbb{R}$ is Hausdorff.
    <2>3. Any continuous bijection from a compact space to a Hausdorff space is a homeomorphism.
    <2>4. Therefore, $f: \mathbb{Z}_+^* \to K$ is a homeomorphism. Q.E.D.
:::
