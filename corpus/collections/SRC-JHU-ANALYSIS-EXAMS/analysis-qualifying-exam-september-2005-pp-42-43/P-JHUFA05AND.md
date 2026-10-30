---
schema: qual/card@1
id: P-JHUFA05AND
kind: problem
title: Weak lower semicontinuity of the norm and strong convergence
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - Hilbert Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the JHU Analysis Qualifying Exam, September 2005, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $(f_n)$ be a sequence in a Hilbert space $X$ such that $f_n\rightharpoonup f$, meaning
$$
\langle f_n,g\rangle\to\langle f,g\rangle
\qquad(g\in X).
$$

(a) Prove that
$$
\norm{f}\le \liminf_{n\to\infty}\norm{f_n},
$$
and give an example where the inequality is strict.

(b) If in addition $\norm{f_n}\to\norm{f}$, prove that $f_n\to f$ in norm.
:::

::: {.solution}

::: pf

::: pf-step

The norm is weakly lower semicontinuous.

::: pf-proof

If $f=0$, the claimed inequality is immediate. Assume $f\ne0$ and set
$$
g=\frac{f}{\norm{f}}.
$$
Then $\norm{g}=1$, so by Cauchy--Schwarz
$$
\abs{\langle f_n,g\rangle}\le\norm{f_n}.
$$
Weak convergence gives
$$
\langle f_n,g\rangle\longrightarrow\langle f,g\rangle=\norm{f}.
$$
Therefore
$$
\norm{f}
=\lim_{n\to\infty}\abs{\langle f_n,g\rangle}
\le\liminf_{n\to\infty}\norm{f_n}.
$$

:::

:::

::: pf-step

Strict inequality can occur.

::: pf-proof

Take $X=\ell^2(\NN)$ and let $e_n$ be the standard orthonormal basis. For every $g=(g_k)\in\ell^2$, one has $g_n\to0$, hence
$$
\langle e_n,g\rangle=g_n\longrightarrow0.
$$
Thus $e_n\rightharpoonup0$. But
$$
\norm{e_n}=1
\qquad\text{for all }n,
$$
so
$$
0=\norm{0}<1=\liminf_n\norm{e_n}.
$$

:::

:::

::: pf-step

Weak convergence plus convergence of norms implies norm convergence.

::: pf-proof

Since $f_n\rightharpoonup f$, taking the test vector $g=f$ gives
$$
\langle f_n,f\rangle\longrightarrow\langle f,f\rangle=\norm{f}^2.
$$
Using the Hilbert-space identity,
$$
\norm{f_n-f}^2
=\norm{f_n}^2+\norm{f}^2-2\operatorname{Re}\langle f_n,f\rangle.
$$
By hypothesis, $\norm{f_n}\to\norm{f}$, so the right-hand side tends to
$$
\norm{f}^2+\norm{f}^2-2\norm{f}^2=0.
$$
Hence
$$
\norm{f_n-f}\longrightarrow0,
$$
which is exactly strong convergence.

:::

:::

:::

:::
