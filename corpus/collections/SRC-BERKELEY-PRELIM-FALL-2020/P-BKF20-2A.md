---
schema: qual/card@1
id: P-BKF20-2A
kind: problem
title: Uniform convergence and products of functions
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2020 solution: uniform convergence
    makes the tail of (f_n) uniformly bounded, which controls the product
    error, while f_n(x)=x and g_n(x)=1+1/n give the required unbounded
    counterexample.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the uniform tail bound, the epsilon estimate for products, uniform
    convergence of both counterexample factors, and failure of uniform
    convergence of their products.
---

::: {.problem}
Let $S$ be a set and let $(f_n)$ and $(g_n)$ be sequences of functions $S\to\mathbb R$.

(a) Show that if $f_n\to f$ and $g_n\to g$ uniformly and $f,g$ are bounded, then $f_ng_n\to fg$ uniformly.

(b) Give a counterexample showing the conclusion can fail when $f$ is unbounded.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Suppose the hypotheses of part (a) hold. Choose constants
$B,C\ge0$ such that
$$
|f(s)|\le B,
\qquad
|g(s)|\le C
$$
for every $s\in S$.

::: pf-proof

Such constants exist because $f$ and $g$ are bounded by hypothesis.

:::

:::

::: {.pf-step #s2}

There is $N_0$ such that
$$
|f_n(s)|\le B+1
$$
for every $n\ge N_0$ and every $s\in S$.

::: pf-proof

Since $f_n\to f$ uniformly, there is $N_0$ such that
$$
|f_n(s)-f(s)|<1
$$
for all $n\ge N_0$ and all $s\in S$. Then step [](#s1){.pf-ref} and the triangle
inequality give
$$
|f_n(s)|
\le
|f(s)|+|f_n(s)-f(s)|
<
B+1.
$$

:::

:::

::: {.pf-step #s3}

The sequence $(f_ng_n)$ converges uniformly to $fg$ on $S$.

::: pf-proof

Let $\varepsilon>0$. Uniform convergence supplies integers $N_1,N_2$
such that, for every $s\in S$,
$$
|g_n(s)-g(s)|
<
\frac{\varepsilon}{2(B+1)}
$$
when $n\ge N_1$, and
$$
|f_n(s)-f(s)|
<
\frac{\varepsilon}{2(C+1)}
$$
when $n\ge N_2$.

Take
$$
N\coloneqq\max\{N_0,N_1,N_2\}.
$$
For $n\ge N$ and every $s\in S$, steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give
$$
\begin{aligned}
|f_n(s)g_n(s)-f(s)g(s)|
&=
|f_n(s)(g_n(s)-g(s))+(f_n(s)-f(s))g(s)|\\
&\le
|f_n(s)|\,|g_n(s)-g(s)|
+
|f_n(s)-f(s)|\,|g(s)|\\
&<
(B+1)\frac{\varepsilon}{2(B+1)}
+
C\frac{\varepsilon}{2(C+1)}\\
&<
\varepsilon.
\end{aligned}
$$
The same $N$ works for every $s\in S$, so the convergence is uniform.
This proves part (a).

:::

:::

::: {.pf-step #s4}

For part (b), take
$$
S=\RR,
\qquad
f_n(x)=x,
\qquad
g_n(x)=1+\frac1n.
$$
Then
$$
f_n\to f,
\qquad
f(x)=x,
$$
and
$$
g_n\to g,
\qquad
g(x)=1,
$$
uniformly on $\RR$, while $f$ is unbounded.

::: pf-proof

For every $n$,
$$
\sup_{x\in\RR}|f_n(x)-f(x)|=0.
$$
Also
$$
\sup_{x\in\RR}|g_n(x)-g(x)|
=
\frac1n
\longrightarrow
0.
$$
Thus both convergences are uniform, and $f(x)=x$ is unbounded.

:::

:::

::: {.pf-step #s5}

The products in step [](#s4){.pf-ref} do not converge uniformly to $fg$.

::: pf-proof

For every $x\in\RR$,
$$
f_n(x)g_n(x)-f(x)g(x)
=
\frac{x}{n}.
$$
Hence for every fixed $n$,
$$
\sup_{x\in\RR}
|f_n(x)g_n(x)-f(x)g(x)|
=
\sup_{x\in\RR}\frac{|x|}{n}
=
\infty.
$$
In particular, these suprema do not tend to $0$, so convergence is not
uniform. This proves part (b).

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves part (a), and steps [](#s4){.pf-ref} and [](#s5){.pf-ref} give the required
counterexample for part (b).

:::

:::

:::
