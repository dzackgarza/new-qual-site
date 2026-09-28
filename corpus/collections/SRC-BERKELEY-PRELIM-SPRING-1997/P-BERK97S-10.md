---
schema: qual/card@1
id: P-BERK97S-10
kind: problem
title: A bounded real function with closed graph is continuous
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be bounded. Suppose the graph of $f$ is a closed subset of $\mathbb R^2$. Prove that $f$ is continuous.
:::

::: {.solution}
<1>1. If $x_n\to x$ in $\RR$, then $f(x_n)\to f(x)$.

::: {.proof}
Suppose instead that $f(x_n)$ does not converge to $f(x)$. Then there are
$\varepsilon>0$ and a subsequence $(x_{n_k})$ such that
$$
\abs{f(x_{n_k})-f(x)}\geq\varepsilon
$$
for every $k$. Since $f$ is bounded, the real sequence
$(f(x_{n_k}))$ is bounded. By the Bolzano--Weierstrass theorem, it has a
convergent subsequence; write
$$
f(x_{n_{k_j}})\longrightarrow y.
$$
Also $x_{n_{k_j}}\to x$, so
$$
\bigl(x_{n_{k_j}},f(x_{n_{k_j}})\bigr)\longrightarrow(x,y).
$$
Every point on the left lies in the graph of $f$. Since the graph is closed,
$(x,y)$ also lies in it, and therefore $y=f(x)$. But passing to the limit in
$$
\abs{f(x_{n_{k_j}})-f(x)}\geq\varepsilon
$$
gives $\abs{y-f(x)}\geq\varepsilon$, a contradiction.
:::

<1>2. The function $f$ is continuous on $\RR$.

::: {.proof}
Step <1>1 shows that for every $x\in\RR$ and every sequence $x_n\to x$, one
has $f(x_n)\to f(x)$. By the sequential criterion for continuity on
$\RR$, $f$ is continuous at every $x$.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 is the required conclusion.
:::
:::
