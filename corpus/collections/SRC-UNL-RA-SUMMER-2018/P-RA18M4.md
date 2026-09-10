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
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Problem 4 of the preserved UNL May 31, 2018 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Replaced the invalid nonclosedness example, whose limit M|x| belongs to S on [0,1], by a sequence converging to an interior cusp at x=1/2.
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
        Proof: define
        \[
        f_n(x)=M\left(\sqrt{(x-\tfrac12)^2+n^{-2}}-\sqrt{\tfrac14+n^{-2}}\right).
        \]
        Then $f_n(0)=0$, and on $(0,1)$
        \[
        f_n'(x)=M\frac{x-\tfrac12}{\sqrt{(x-\tfrac12)^2+n^{-2}}},
        \]
        so $|f_n'(x)|\le M$. Hence $f_n\in S$.

        Since $|\sqrt{t^2+n^{-2}}-|t||\le n^{-1}$ uniformly in $t$, we have uniform convergence
        \[
        f_n(x)\longrightarrow f(x):=M\left(|x-\tfrac12|-\tfrac12\right)
        \]
        on $[0,1]$. The limit satisfies $f(0)=0$ but is not differentiable at the interior point $x=1/2$. Thus $f\notin S$, so $S$ is not closed.
    <2>2. Compact subsets of metric spaces are closed.
        Proof: A compact subset of a Hausdorff space is closed; every metric space is Hausdorff.
    <2>3. Q.E.D.
        Proof: <2>1 and <2>2 show $S$ is not compact.

:::
