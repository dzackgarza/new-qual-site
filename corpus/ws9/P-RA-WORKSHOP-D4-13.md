---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-13
kind: problem
title: Prove Theorem 3.3
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Continuity
  - Compactness
  - Continuity
relations:
- kind: uses
  target: T-RA-WORKSHOP-D4-3-3
review: draft
solved: true
---

::: {.problem title="?"}
Prove Theorem 3.3.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Suppose, toward a contradiction, that $f$ is not uniformly continuous on $K$.
Proof: then there is $\epsilon > 0$ such that for every $\delta > 0$ there are $x, y \in K$ with $|x - y| < \delta$ but $|f(x) - f(y)| \ge \epsilon$.
Taking $\delta = 1/n$, we get sequences $x_n, y_n \in K$ with $|x_n - y_n| < 1/n$ and $|f(x_n) - f(y_n)| \ge \epsilon$ for all $n$.
<1>2. Extract a convergent subsequence.
Proof: $K$ is compact, hence sequentially compact (in $\mathbb{R}^n$ compact ⟹ every sequence has a convergent subsequence), so a subsequence $x_{n_j} \to x \in K$.
Since $|x_{n_j} - y_{n_j}| < 1/n_j \to 0$, the corresponding subsequence $y_{n_j}$ also converges to $x$.
<1>3. Contradict continuity.
Proof: $f$ is continuous at $x$, so $f(x_{n_j}) \to f(x)$ and $f(y_{n_j}) \to f(x)$; hence $|f(x_{n_j}) - f(y_{n_j})| \to 0$.
But by construction $|f(x_{n_j}) - f(y_{n_j})| \ge \epsilon$ for all $j$, contradiction.
<1>4. Q.E.D. Proof: hence $f$ is uniformly continuous on $K$.
:::
