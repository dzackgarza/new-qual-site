---
schema: qual/card@1
id: P-UCLAB01F-03
kind: problem
title: Uniform limits of continuous functions are continuous
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 of the retained UCLA Basic Exam, Fall 2001 PDF.
---

::: {.problem}
Let $E\subseteq\RR$, and let $(f_n)$ be a sequence of continuous real-valued functions on $E$.
Suppose $f_n\to f$ uniformly on $E$.
Prove that $f$ is continuous on $E$.
:::

::: {.solution}

::: pf

::: pf-step

Fix $x_0\in E$ and $\varepsilon>0$.


::: pf-proof

To prove continuity of $f$ on $E$, it is enough to prove continuity at an arbitrary point $x_0\in E$. Let $\varepsilon>0$ be arbitrary.

:::

:::

::: {.pf-step #s1-2}

There exists $N$ such that
\[
|f_N(x)-f(x)|<\frac{\varepsilon}{3}
\]
for every $x\in E$.


::: pf-proof

The convergence $f_n\to f$ is uniform on $E$. Apply the definition of uniform convergence with tolerance $\varepsilon/3$.

:::

:::

::: {.pf-step #s1-3}

There exists $\delta>0$ such that, whenever $x\in E$ and $|x-x_0|<\delta$,
\[
|f_N(x)-f_N(x_0)|<\frac{\varepsilon}{3}.
\]


::: pf-proof

The function $f_N$ is continuous at $x_0$, because every $f_n$ is continuous on $E$. Apply continuity of $f_N$ at $x_0$ with tolerance $\varepsilon/3$.

:::

:::

::: {.pf-step #s1-4}

Whenever $x\in E$ and $|x-x_0|<\delta$,
\[
|f(x)-f(x_0)|<\varepsilon.
\]


::: pf-proof

For such $x$, the triangle inequality and steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} give
\[
\begin{aligned}
|f(x)-f(x_0)|
&\le |f(x)-f_N(x)|
   +|f_N(x)-f_N(x_0)|
   +|f_N(x_0)-f(x_0)|\\
&<\frac{\varepsilon}{3}
  +\frac{\varepsilon}{3}
  +\frac{\varepsilon}{3}
=\varepsilon.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-5}

The function $f$ is continuous on $E$.


::: pf-proof

Step [](#s1-4){.pf-ref} proves continuity of $f$ at the arbitrary point $x_0\in E$. Therefore $f$ is continuous at every point of $E$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
