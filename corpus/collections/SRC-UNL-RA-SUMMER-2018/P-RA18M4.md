---
schema: qual/card@1
id: P-RA18M4
kind: problem
title: The supremum metric on bounded functions
classification:
  areas:
  - real-analysis
  topics:
  - Metric Spaces
  - Function Spaces
  - Arzelà-Ascoli
relations: []
review: draft
---

:::{.problem}
(a) Given a set $S$, show that the function
$$\rho_\infty:\mathcal B(S)\times\mathcal B(S)\to\mathbb R,\qquad
\rho_\infty(f,g):=\operatorname{lub}(\{|f(x)-g(x)|:x\in S\})$$
is a metric on $\mathcal B(S)$.

(b) Let $M>0$ be given. Set
$$S:=\{f\in C_b([0,1]):f(0)=0,\ f\text{ is differentiable on }(0,1),\
\text{and }|f'(x)|\le M\text{ for each }x\in(0,1)\}.$$
Determine whether the set $S$ is compact in $(C_b([0,1]),\rho_\infty)$.
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** (a) Show $\rho_\infty(f,g) = \operatorname{lub}\{|f(x) - g(x)| : x \in S\}$ is a metric on $\mathcal B(S)$; (b) decide compactness of $S = \{f \in C_b[0,1] : f(0) = 0, f \text{ differentiable on } (0,1), |f'| \le M\}$ in $(C_b[0,1], \rho_\infty)$.

<1>1. (a) $\rho_\infty$ is a metric.
    <2>1. $\rho_\infty(f,g) \ge 0$, finite, and $\rho_\infty(f,g) = 0 \Leftrightarrow f = g$.
        Proof: $|f(x) - g(x)| \ge 0$; finiteness because $f, g$ are bounded on $S$; $\rho_\infty = 0$ iff $|f(x) - g(x)| = 0$ for all $x$ iff $f = g$ pointwise.
    <2>2. Symmetry: $\rho_\infty(f,g) = \rho_\infty(g,f)$.
        Proof: $|f(x) - g(x)| = |g(x) - f(x)|$ for each $x$.
    <2>3. Triangle inequality: $\rho_\infty(f,h) \le \rho_\infty(f,g) + \rho_\infty(g,h)$.
        Proof: for each $x$, $|f(x) - h(x)| \le |f(x) - g(x)| + |g(x) - h(x)| \le \rho_\infty(f,g) + \rho_\infty(g,h)$; take the lub over $x$.
    <2>4. Q.E.D.
        Proof: <2>1–<2>3 are the metric axioms.

<1>2. (b) $S$ is NOT compact.
    <2>1. $S$ is not closed in $C_b[0,1]$.
        Proof: define $f_n(x) = M\sqrt{x^2 + 1/n^2} - M/n$. Each $f_n$ is differentiable on $(0,1)$ with $f_n'(x) = \frac{Mx}{\sqrt{x^2 + 1/n^2}}$, so $|f_n'| \le M$; and $f_n(0) = M/n - M/n = 0$, so $f_n \in S$. But $f_n \to M|x|$ uniformly on $[0,1]$ (since $\sqrt{x^2 + 1/n^2} \to |x|$ uniformly and $M/n \to 0$), and $M|x|$ is not differentiable at $0$, so $M|x| \notin S$. A sequence in $S$ converges to a point outside $S$: $S$ is not closed.
    <2>2. Compact subsets of metric spaces are closed.
        Proof: standard fact.
    <2>3. Q.E.D.
        Proof: <2>1 and <2>2 show $S$ is not compact.

:::
