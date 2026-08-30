---
schema: qual/card@1
id: E-FNMUB
kind: exercise
title: Uniqueness of continuous extensions into Hausdorff spaces
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Let $A \subset X$; let $f: A \to Y$ be continuous; let $Y$ be Hausdorff.
Show that if $f$ may be extended to a continuous function $g: \overline{A} \to Y$, then $g$ is uniquely determined by $f$.
:::

::: {.solution}
<1>1. Agreement set of two continuous extensions:
<2>1. Suppose $g_1, g_2: \overline{A} \to Y$ are two continuous functions such that $g_1|_A = f$ and $g_2|_A = f$.
Define the agreement set:
\[
E = \{x \in \overline{A} \mid g_1(x) = g_2(x)\}.
\]
Proof: setup.
<2>2. Since $g_1(a) = f(a) = g_2(a)$ for all $a \in A$, we have $A \subseteq E$.
Proof: both functions extend $f$ on $A$.

<1>2. Proof that $E$ is closed:
<2>1. Define the product map $h: \overline{A} \to Y \times Y$ by $h(x) = (g_1(x), g_2(x))$.
Since $g_1$ and $g_2$ are continuous, $h$ is continuous with respect to the product topology on $Y \times Y$.
Proof: universal property of product spaces.
<2>2. Since $Y$ is Hausdorff, the diagonal $\Delta = \{(y, y) \in Y \times Y \mid y \in Y\}$ is a closed subset of $Y \times Y$.
Proof: standard characterization of Hausdorff spaces by closed diagonal.
<2>3. The agreement set $E$ is the preimage of the diagonal:
\[
E = h^{-1}(\Delta).
\]
Since $h$ is continuous and $\Delta$ is closed, $E$ is a closed subset of $\overline{A}$.
Proof: preimage of a closed set under a continuous map is closed.

<1>3. Coincidence on $\overline{A}$:
<2>1. By <1>1 (<2>2), $A \subseteq E$.
Taking closures in the subspace $\overline{A}$, and using the fact that $E$ is closed in $\overline{A}$:
\[
\overline{A} = \operatorname{cl}_{\overline{A}}(A) \subseteq \operatorname{cl}_{\overline{A}}(E) = E.
\]
Proof: closure monotonicity and $E$ is closed.
<2>2. Since $E \subseteq \overline{A}$ by definition, we have $E = \overline{A}$.
Therefore $g_1(x) = g_2(x)$ for all $x \in \overline{A}$, so $g_1 = g_2$.
Proof: set equality $E = \overline{A}$.

<1>4. Conclusion:
Any continuous extension $g: \overline{A} \to Y$ of $f$ is uniquely determined. Q.E.D.
Proof: <1>1 through <1>3.
:::
