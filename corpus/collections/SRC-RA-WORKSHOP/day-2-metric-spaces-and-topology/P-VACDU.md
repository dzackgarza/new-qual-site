---
schema: qual/card@1
id: P-VACDU
kind: problem
title: (b) Show by example that the union of infinitely
classification:
  areas:
  - real-analysis
  topics:
  - Compactness
  - Metric Spaces
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
(b) Show by example that the union of infinitely
many compact subsets of a metric space need not be compact. (c) If
$(X,d)$ is a metric space and $K\subset X$ is compact, define
$d(x_0,K)=\inf_{y\in K} d(x_0,y)$. Prove that there exists a point
$y_0\in K$ such that $d(x_0,K)=d(x_0,y_0)$.
:::
::: {.solution}
<1>1. (b) The union of infinitely many compact sets need not be compact.
    ::: {.proof}
    in $\RR$ (a metric space), the singletons $K_n = \{n\}$ are compact (finite, hence compact). Their union $\cup_n K_n = \NN$ is not compact: the open cover $\{(n - 1/2, n + 1/2) : n \in \NN\}$ has no finite subcover, since each open interval contains exactly one point of $\NN$. (Equivalently, $\NN$ is closed but unbounded, hence not compact.)
    :::
<1>2. (c) Setup: the function $x \mapsto d(x_0, x)$ is continuous.
    ::: {.proof}
    by the triangle inequality, $|d(x_0,x) - d(x_0,y)| \le d(x,y)$, so the map is $1$-Lipschitz.
    :::
<1>3. (c) The distance to $K$ is attained.
    ::: {.proof}
    $K$ is compact and $d(x_0, \cdot)$ is continuous (<1>2), so $d(x_0,\cdot)$ attains its minimum on $K$: there is $y_0 \in K$ with $d(x_0, y_0) = \min_{y \in K} d(x_0, y) = d(x_0, K)$, where the last equality is the definition of $d(x_0, K)$ as an infimum (attained by <1>2).
    :::
<1>4. Q.E.D.
:::
