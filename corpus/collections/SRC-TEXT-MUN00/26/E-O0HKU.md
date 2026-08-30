---
schema: qual/card@1
id: E-O0HKU
kind: exercise
title: Maps from compact to Hausdorff spaces are closed
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Show that if $f: X \to Y$ is continuous, where $X$ is compact and $Y$ is Hausdorff, then $f$ is a closed map (that is, $f$ carries closed sets to closed sets).
:::

::: {.solution}
<1>1. Let $C \subseteq X$ be an arbitrary closed subset.
Proof: setup.

<1>2. $C$ is a compact subspace of $X$.
<2>1. $X$ is compact by hypothesis.
Proof: hypothesis.
<2>2. Every closed subset of a compact topological space is compact.
Proof: if $\mathcal{U}$ is an open cover of $C$, then $\mathcal{U} \cup \{X \setminus C\}$ is an open cover of $X$; the finite subcover of $X$ yields a finite subcover of $C$.
<2>3. Hence $C$ is compact.
Proof: <2>1 and <2>2.

<1>3. The image $f(C)$ is a compact subspace of $Y$.
<2>1. $f: X \to Y$ is continuous.
Proof: hypothesis.
<2>2. The continuous image of any compact space is compact.
Proof: if $\{V_\alpha\}$ is an open cover of $f(C)$, then $\{f^{-1}(V_\alpha)\}$ is an open cover of $C$; a finite subcover of $C$ maps under $f$ to a finite subcover of $f(C)$.
<2>3. Hence $f(C)$ is compact in $Y$.
Proof: <1>2, <2>1, and <2>2.

<1>4. $f(C)$ is a closed subset of $Y$.
<2>1. $Y$ is Hausdorff by hypothesis.
Proof: hypothesis.
<2>2. Every compact subset of a Hausdorff space is closed.
Proof: for any $y_0 \notin f(C)$, Hausdorff separation gives disjoint open neighborhoods $U_x$ of $x \in f(C)$ and $V_x$ of $y_0$; compactness of $f(C)$ yields a finite subcover $\bigcup_{i=1}^n U_{x_i} \supset f(C)$, and the intersection $\bigcap_{i=1}^n V_{x_i}$ is an open neighborhood of $y_0$ disjoint from $f(C)$.
<2>3. Hence $f(C)$ is closed in $Y$.
Proof: <1>3, <2>1, and <2>2.

<1>5. Conclusion: $f$ maps every closed set $C \subseteq X$ to a closed set $f(C) \subseteq Y$, so $f$ is a closed map.
Q.E.D. Proof: <1>1 and <1>4.
:::
