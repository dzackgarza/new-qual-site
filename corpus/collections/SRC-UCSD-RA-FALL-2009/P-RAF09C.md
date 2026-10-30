---
schema: qual/card@1
id: P-RAF09C
kind: problem
title: "Comparison of norms via continuous dual functionals"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the official UCSD Fall 2009 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $\norm{\cdot}_1$ and $\norm{\cdot}_2$ be two norms on the linear vector space $X$.
Assume that every continuous linear functional of $(X, \norm{\cdot}_1)$ is also a continuous linear functional of $(X, \norm{\cdot}_2)$.
Prove that there exists $\alpha > 0$ such that $\norm{x}_1 \leq \alpha \norm{x}_2$ for all $x \in X$.
:::

::: {.solution}

::: pf

::: pf-step

Compare the two continuous duals.

::: pf-proof

Write
$$
X_1^*:=(X,\norm{\cdot}_1)^*,
\qquad
X_2^*:=(X,\norm{\cdot}_2)^*.
$$
By hypothesis,
$$
X_1^*\subseteq X_2^*.
$$
Consider the identity map
$$
J:X_1^*\to X_2^*,
\qquad
J(f)=f.
$$
Both dual spaces are Banach spaces with their operator norms.

:::

:::

::: pf-step

Show that $J$ has closed graph.

::: pf-proof

Suppose
$$
f_n\to f\quad\text{in }X_1^*
$$
and
$$
Jf_n\to g\quad\text{in }X_2^*.
$$
For every fixed $x\in X$,
$$
\abs{f_n(x)-f(x)}
\le \norm{f_n-f}_{1,*}\,\norm{x}_1\longrightarrow0,
$$
while
$$
\abs{f_n(x)-g(x)}
\le \norm{f_n-g}_{2,*}\,\norm{x}_2\longrightarrow0.
$$
Hence $f(x)=g(x)$ for every $x\in X$, so $g=Jf$. Thus the graph of $J$ is closed.

By the Closed Graph Theorem, there exists $C>0$ such that
$$
\norm{f}_{2,*}\le C\norm{f}_{1,*}
\qquad(f\in X_1^*).
$$

:::

:::

::: pf-step

Recover the norm $\norm{\cdot}_1$ from the dual unit ball.

::: pf-proof

By the Hahn--Banach theorem, for every $x\in X$,
$$
\norm{x}_1
=\sup\{\abs{f(x)}:f\in X_1^*,\ \norm{f}_{1,*}\le1\}.
$$
If $\norm{f}_{1,*}\le1$, then Step 2 gives
$$
\norm{f}_{2,*}\le C,
$$
and therefore
$$
\abs{f(x)}\le C\norm{x}_2.
$$
Taking the supremum over the $\norm{\cdot}_{1,*}$-unit ball yields
$$
\boxed{\norm{x}_1\le C\norm{x}_2\qquad(x\in X).}
$$
Thus the conclusion holds with $\alpha=C$.

:::

:::

:::

:::
