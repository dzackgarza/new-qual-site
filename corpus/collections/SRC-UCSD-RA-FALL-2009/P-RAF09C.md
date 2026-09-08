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

::: problem
Let $\|\cdot\|_1$ and $\|\cdot\|_2$ be two norms on the linear vector space $X$.
Assume that every continuous linear functional of $(X, \|\cdot\|_1)$ is also a continuous linear functional of $(X, \|\cdot\|_2)$.
Prove that there exists $\alpha > 0$ such that $\|x\|_1 \leq \alpha \|x\|_2$ for all $x \in X$.
:::

::: solution
<1>1. Compare the two continuous duals.
::: proof
Write
\[
X_1^*:=(X,\|\cdot\|_1)^*,
\qquad
X_2^*:=(X,\|\cdot\|_2)^*.
\]
By hypothesis,
\[
X_1^*\subseteq X_2^*.
\]
Consider the identity map
\[
J:X_1^*\to X_2^*,
\qquad
J(f)=f.
\]
Both dual spaces are Banach spaces with their operator norms.
:::

<1>2. Show that $J$ has closed graph.
::: proof
Suppose
\[
f_n\to f\quad\text{in }X_1^*
\]
and
\[
Jf_n\to g\quad\text{in }X_2^*.
\]
For every fixed $x\in X$,
\[
|f_n(x)-f(x)|
\le \|f_n-f\|_{1,*}\,\|x\|_1\longrightarrow0,
\]
while
\[
|f_n(x)-g(x)|
\le \|f_n-g\|_{2,*}\,\|x\|_2\longrightarrow0.
\]
Hence $f(x)=g(x)$ for every $x\in X$, so $g=Jf$. Thus the graph of $J$ is closed.

By the Closed Graph Theorem, there exists $C>0$ such that
\[
\|f\|_{2,*}\le C\|f\|_{1,*}
\qquad(f\in X_1^*).
\]
:::

<1>3. Recover the norm $\|\cdot\|_1$ from the dual unit ball.
::: proof
By the Hahn--Banach theorem, for every $x\in X$,
\[
\|x\|_1
=\sup\{|f(x)|:f\in X_1^*,\ \|f\|_{1,*}\le1\}.
\]
If $\|f\|_{1,*}\le1$, then Step 2 gives
\[
\|f\|_{2,*}\le C,
\]
and therefore
\[
|f(x)|\le C\|x\|_2.
\]
Taking the supremum over the $\|\cdot\|_{1,*}$-unit ball yields
\[
\boxed{\|x\|_1\le C\|x\|_2\qquad(x\in X).}
\]
Thus the conclusion holds with $\alpha=C$.
:::
:::
