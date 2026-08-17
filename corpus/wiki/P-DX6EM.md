---
schema: qual/card@1
id: P-DX6EM
kind: problem
title: "Let $f \\colon [a,b] \\to \\mathbb{R}$. Suppose"
classification:
  areas:
  - real-analysis
  topics:
  - variation
relations: []
review: draft
solved: true
---

::: problem
Let $f \colon [a,b] \to \mathbb{R}$.
Suppose $f \in \text{BV}[a,b]$.
Prove $f$ is the difference of two increasing functions.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. Define the total variation $V(x) = \sup \sum_{i=1}^n |f(x_i) - f(x_{i-1})|$ over all partitions $a = x_0 < \cdots < x_n = x$ of $[a, x]$, for $a \le x \le b$.
Proof: $V$ is well-defined and finite because $f \in \text{BV}[a,b]$ (so $V(b) < \infty$), and $V(a) = 0$.

<1>2. $V$ is increasing on $[a,b]$: for $a \le x < y \le b$, $V(y) \ge V(x)$.
Proof: partitions of $[a,x]$ extend to partitions of $[a,y]$ by adding the point $y$, so the sup over the larger interval is $\ge$.

<1>3. $V + f$ and $V - f$ are increasing on $[a,b]$.
<2>1. For $a \le x < y \le b$: $V(y) - V(x) \ge |f(y) - f(x)|$.
Proof: $V(y) \ge V(x) + |f(y) - f(x)|$: a partition of $[a,x]$ achieving within $\eps$ of $V(x)$, extended by $y$, gives a partition of $[a,y]$ with variation $\ge V(x) + |f(y)-f(x)| - \eps$; let $\eps \to 0$.
<2>2. $(V + f)(y) - (V + f)(x) = (V(y) - V(x)) + (f(y) - f(x)) \ge |f(y)-f(x)| + (f(y)-f(x)) \ge 0$.
Proof: <2>1 and $|u| + u \ge 0$.
<2>3. $(V - f)(y) - (V - f)(x) = (V(y) - V(x)) - (f(y) - f(x)) \ge |f(y)-f(x)| - (f(y)-f(x)) \ge 0$.
Proof: <2>1 and $|u| - u \ge 0$.

<1>4. Q.E.D.: $f = \frac12(V + f) - \frac12(V - f)$ is a difference of two increasing functions.
Proof: <1>2 and <1>3 show both $V + f$ and $V - f$ are increasing (multiplying by $1/2$ preserves monotonicity), and the identity is trivial.
:::
