---
schema: qual/card@1
id: P-RAF24C
kind: problem
title: First-countable TVS with sequential Cauchy completeness is net-complete
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
  - Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the official UCSD Fall 2024 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $X$ be a topological vector space.
A net (or, less generally, a sequence) $\langle x_\alpha \rangle_{\alpha \in A}$ in $X$ is *Cauchy* if the net of pairwise differences $\langle x_\alpha - x_\beta \rangle_{(\alpha,\beta) \in A \times A}$, with $A \times A$ directed by the rule $(\alpha, \beta) \preceq (\alpha', \beta') \Leftrightarrow (\alpha \preceq \alpha' \text{ and } \beta \preceq \beta')$, converges to $0 \in X$.
Prove that if $X$ is first countable and every Cauchy sequence in $X$ converges, then every Cauchy net in $X$ converges.
:::

::: solution
<1>1. Choose a nested local base at the origin.
::: proof
Because $X$ is first countable, there is a countable local base at $0$. Using continuity of addition and negation, refine it to a decreasing sequence of symmetric neighborhoods
\[
V_1\supset V_2\supset\cdots
\]
such that
\[
V_{n+1}+V_{n+1}\subset V_n
\qquad(n\ge1).
\]
This is still a local base at $0$.
:::

<1>2. Extract a Cauchy sequence from the Cauchy net.
::: proof
Let $(x_\alpha)_{\alpha\in A}$ be a Cauchy net. For each $n$, there exists $\gamma_n\in A$ such that
\[
\alpha,\beta\succeq\gamma_n
\quad\Longrightarrow\quad
x_\alpha-x_\beta\in V_n.
\]
Recursively choose indices $\alpha_n\in A$ so that
\[
\alpha_n\succeq\gamma_n
\qquad\text{and}\qquad
\alpha_{n+1}\succeq\alpha_n.
\]

Then $(x_{\alpha_n})$ is a Cauchy sequence. Indeed, if $m,n\ge N$, then
\[
\alpha_m,\alpha_n\succeq\alpha_N\succeq\gamma_N,
\]
so
\[
x_{\alpha_m}-x_{\alpha_n}\in V_N.
\]
By hypothesis, every Cauchy sequence converges; hence there exists $x\in X$ such that
\[
x_{\alpha_n}\to x.
\]
:::

<1>3. Show that the original net converges to the same limit.
::: proof
Let $U$ be any neighborhood of $0$. Choose $N$ so large that
\[
V_N+V_N\subset U.
\]
Since $x_{\alpha_n}\to x$, choose $m\ge N$ such that
\[
x_{\alpha_m}-x\in V_N.
\]

Now let $\alpha\succeq\alpha_N$. Since
\[
\alpha,\alpha_m\succeq\alpha_N\succeq\gamma_N,
\]
the Cauchy property gives
\[
x_\alpha-x_{\alpha_m}\in V_N.
\]
Therefore
\[
x_\alpha-x
=(x_\alpha-x_{\alpha_m})+(x_{\alpha_m}-x)
\in V_N+V_N
\subset U.
\]
Thus $x_\alpha\to x$.

Hence every Cauchy net in $X$ converges.
:::
:::
