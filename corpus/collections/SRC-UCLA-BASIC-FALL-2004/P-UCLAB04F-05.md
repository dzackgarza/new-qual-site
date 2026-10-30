---
schema: qual/card@1
id: P-UCLAB04F-05
kind: problem
title: Completeness of continuous functions with the supremum norm
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 of the official UCLA Basic Exam Fall 2004 PDF.
---

::: {.problem}
Prove that $C[0,1]$, the space of continuous functions from $[0,1]$ to $\RR$, is complete for the supremum norm
$$
\norm{f}_\infty=\sup_{x\in[0,1]}\abs{f(x)}.
$$

You may use without proof that a uniform limit of continuous functions is continuous.
:::

::: {.solution}

Let $(f_n)$ be a Cauchy sequence in $C[0,1]$ with respect to the supremum norm.

::: pf

::: {.pf-step #s1-1}

For each $x\in[0,1]$, the real sequence $(f_n(x))$ is Cauchy.


::: pf-proof

Let $\varepsilon>0$. Since $(f_n)$ is Cauchy in the supremum norm, there is $N$ such that
$$
\norm{f_n-f_m}_\infty<\varepsilon
$$
whenever $m,n\ge N$. Hence for every $x\in[0,1]$,
$$
\abs{f_n(x)-f_m(x)}
\le
\norm{f_n-f_m}_\infty
<
\varepsilon.
$$
Thus $(f_n(x))$ is Cauchy in $\RR$.

:::

:::

::: {.pf-step #s1-2}

Define
$$
f(x)=\lim_{n\to\infty}f_n(x)
$$
for each $x\in[0,1]$.


::: pf-proof

By step [](#s1-1){.pf-ref} and completeness of $\RR$, the displayed limit exists for every $x\in[0,1]$.

:::

:::

::: {.pf-step #s1-3}

The convergence $f_n\to f$ is uniform on $[0,1]$.


::: pf-proof

Let $\varepsilon>0$. Choose $N$ such that
$$
\norm{f_n-f_m}_\infty<\frac{\varepsilon}{2}
$$
whenever $m,n\ge N$. Fix $n\ge N$ and $x\in[0,1]$. For every $m\ge N$,
$$
\abs{f_n(x)-f_m(x)}<\frac{\varepsilon}{2}.
$$
Letting $m\to\infty$ and using step [](#s1-2){.pf-ref} gives
$$
\abs{f_n(x)-f(x)}
\le
\frac{\varepsilon}{2}
<
\varepsilon.
$$
This bound is independent of $x$, so
$$
\norm{f_n-f}_\infty<\varepsilon
$$
for every $n\ge N$.

:::

:::

::: {.pf-step #s1-4}

The function $f$ is continuous on $[0,1]$.


::: pf-proof

Fix $x_0\in[0,1]$ and $\varepsilon>0$. By step [](#s1-3){.pf-ref}, choose $N$ such that
$$
\norm{f-f_N}_\infty<\frac{\varepsilon}{3}.
$$
Since $f_N$ is continuous at $x_0$, there is $\delta>0$ such that, whenever $x\in[0,1]$ and $\abs{x-x_0}<\delta$,
$$
\abs{f_N(x)-f_N(x_0)}<\frac{\varepsilon}{3}.
$$
Then
$$
\begin{aligned}
\abs{f(x)-f(x_0)}
&\le
\abs{f(x)-f_N(x)}
+
\abs{f_N(x)-f_N(x_0)}
+
\abs{f_N(x_0)-f(x_0)}\\
&<
\varepsilon.
\end{aligned}
$$
Thus $f$ is continuous at every $x_0\in[0,1]$.

:::

:::

::: {.pf-step #s1-5}

The Cauchy sequence $(f_n)$ converges in $C[0,1]$.


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
f\in C[0,1].
$$
By step [](#s1-3){.pf-ref},
$$
\norm{f_n-f}_\infty\to0.
$$
Thus $(f_n)$ converges to an element of the metric space $C[0,1]$.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{C[0,1]\text{ is complete for }\norm{\cdot}_\infty}.
$$


::: pf-proof

The Cauchy sequence $(f_n)$ was arbitrary, and step [](#s1-5){.pf-ref} proves that every such sequence converges in $C[0,1]$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required completeness statement.

:::

:::

:::
