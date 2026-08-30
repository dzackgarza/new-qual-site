---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-04
kind: problem
title: Continuity of the distance to a subset
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $(X,d)$ be a metric space and let $A\subset X$.
If $x\in X$ define the distance of $x$ to $A$ to be $\inf\{d(x,a):a\in A\}$.
Prove that the real-valued function on $X$ defined by $x\mapsto d(x,A)$ is continuous.
:::

::: {.solution}
<1>1. Establish the 1-Lipschitz inequality:
<2>1. Let $x, y \in X$ and let $a \in A$ be an arbitrary element.
By the triangle inequality for the metric $d$:
\[
d(x, a) \le d(x, y) + d(y, a).
\]
Proof: metric space axioms.
<2>2. Since $d(x, A) = \inf_{a' \in A} d(x, a') \le d(x, a)$:
\[
d(x, A) \le d(x, y) + d(y, a).
\]
Proof: definition of infimum.
<2>3. Since the left-hand side is a lower bound for $d(x, y) + d(y, a)$ for all $a \in A$, taking the infimum over $a \in A$ on the right yields:
\[
d(x, A) \le d(x, y) + \inf_{a \in A} d(y, a) = d(x, y) + d(y, A).
\]
Proof: infimum property.
<2>4. Rearranging terms gives:
\[
d(x, A) - d(y, A) \le d(x, y).
\]
Proof: subtract $d(y, A)$ from both sides.
<2>5. Symmetrically, swapping the roles of $x$ and $y$ and using symmetry $d(y, x) = d(x, y)$ gives:
\[
d(y, A) - d(x, A) \le d(x, y) \implies -(d(x, A) - d(y, A)) \le d(x, y).
\]
Proof: metric symmetry.
<2>6. Combining <2>4 and <2>5 yields:
\[
|d(x, A) - d(y, A)| \le d(x, y) \quad \text{for all } x, y \in X.
\]
Thus $f(x) = d(x, A)$ is 1-Lipschitz continuous.
Proof: absolute value definition $|u| \le c \iff -c \le u \le c$.

<1>2. Deduce continuity:
<2>1. Let $\varepsilon > 0$. Choose $\delta = \varepsilon > 0$.
Proof: choice of $\delta$.
<2>2. For all $x, y \in X$ with $d(x, y) < \delta$:
\[
|d(x, A) - d(y, A)| \le d(x, y) < \delta = \varepsilon.
\]
Thus $x \mapsto d(x, A)$ is uniformly continuous on $X$.
Proof: <1>1.

<1>3. Conclusion:
The distance function $x \mapsto d(x, A)$ is continuous. Q.E.D.
Proof: <1>2.
:::
