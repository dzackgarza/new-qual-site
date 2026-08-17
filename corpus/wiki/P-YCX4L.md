---
schema: qual/card@1
id: P-YCX4L
kind: problem
title: "- Show that a continuous function on a compact set is uniformly contin\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - uniform-continuity
  - compactness
  - continuity
relations: []
review: draft
solved: true
---

::: problem
- Show that a continuous function on a compact set is uniformly continuous.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. Suppose, toward a contradiction, that $f$ is not uniformly continuous.
Proof: then there is $\eps > 0$ such that for every $n \in \NN$ there exist $x_n, y_n \in K$ with $d(x_n, y_n) < 1/n$ but $|f(x_n) - f(y_n)| \ge \eps$.
<1>2. Extract a convergent subsequence of $(x_n)$.
Proof: $K$ is compact, hence sequentially compact (metric space), so $(x_n)$ has a subsequence $(x_{n_j})$ converging to some $x \in K$.
<1>3. The corresponding subsequence $(y_{n_j})$ also converges to $x$.
Proof: $d(y_{n_j}, x) \le d(y_{n_j}, x_{n_j}) + d(x_{n_j}, x) < 1/n_j + d(x_{n_j}, x) \to 0$.
<1>4. Contradiction.
Proof: $f$ is continuous at $x$, so $f(x_{n_j}) \to f(x)$ and $f(y_{n_j}) \to f(x)$ by <1>2 and <1>3; hence $|f(x_{n_j}) - f(y_{n_j})| \to 0$, contradicting $|f(x_{n_j}) - f(y_{n_j})| \ge \eps > 0$ for all $j$ (from <1>1). <1>5. Hence $f$ is uniformly continuous on $K$.
Proof: <1>1--<1>4 rule out the failure of uniform continuity.
<1>6. Q.E.D.
:::
