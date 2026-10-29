---
schema: qual/card@1
id: P-UCLAB03F-04
kind: problem
title: Riemann integrability of a continuous function
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4 of the official UCLA Basic Exam Fall 2003 PDF.
---

::: {.problem}
Let $f:\RR\to\RR$ be continuous.
State the definition of the Riemann integral
$$
\int_0^1 f(x)\,dx
$$
and prove that it exists.
:::

::: {.solution}

Use the Darboux definition of the Riemann integral.

::: pf

::: {.pf-step #s1-1}

For a partition
$$
P:\quad 0=x_0<x_1<\cdots<x_n=1,
$$
define
$$
M_i=\sup_{x\in[x_{i-1},x_i]}f(x),
\qquad
m_i=\inf_{x\in[x_{i-1},x_i]}f(x),
$$
and
$$
U(f,P)=\sum_{i=1}^{n}M_i(x_i-x_{i-1}),
\qquad
L(f,P)=\sum_{i=1}^{n}m_i(x_i-x_{i-1}).
$$


::: pf-proof

Since $f$ is continuous on the compact interval $[0,1]$, it is bounded. Hence every $M_i$ and $m_i$ is a finite real number, so the upper and lower sums are well-defined.

:::

:::

::: {.pf-step #s1-2}

The upper and lower Riemann integrals are
$$
\overline{\int_0^1}f
=
\inf_P U(f,P)
$$
and
$$
\underline{\int_0^1}f
=
\sup_P L(f,P),
$$
where the infimum and supremum range over all partitions $P$ of $[0,1]$.


::: pf-proof

For any partitions $P,Q$, passing to the common refinement $P\cup Q$ can only decrease the upper sum and increase the lower sum. Hence
$$
L(f,P)\le U(f,Q)
$$
for all $P,Q$. Therefore the set of lower sums is bounded above and the set of upper sums is bounded below, so the two quantities are defined in $\RR$.

:::

:::

::: {.pf-step #s1-3}

The function $f$ is Riemann integrable on $[0,1]$ exactly when
$$
\underline{\int_0^1}f
=
\overline{\int_0^1}f.
$$
When this equality holds, their common value is denoted
$$
\int_0^1 f(x)\,dx.
$$


::: pf-proof

This is the Darboux definition of Riemann integrability.

:::

:::

::: {.pf-step #s1-4}

For every $\varepsilon>0$, there exists $\delta>0$ such that
$$
|x-y|<\delta
\quad\Longrightarrow\quad
|f(x)-f(y)|<\varepsilon
$$
for all $x,y\in[0,1]$.


::: pf-proof

The function $f$ is continuous on the compact interval $[0,1]$, so it is uniformly continuous.

:::

:::

::: {.pf-step #s1-5}

For every $\varepsilon>0$, there exists a partition $P$ such that
$$
U(f,P)-L(f,P)<\varepsilon.
$$


::: pf-proof

Fix $\varepsilon>0$ and choose $\delta>0$ from step [](#s1-4){.pf-ref}. Choose a partition
$$
P:\quad 0=x_0<\cdots<x_n=1
$$
whose mesh satisfies
$$
\max_i(x_i-x_{i-1})<\delta.
$$
If $x,y$ lie in the same subinterval $[x_{i-1},x_i]$, then $|x-y|<\delta$, so
$$
|f(x)-f(y)|<\varepsilon.
$$
Hence
$$
M_i-m_i\le\varepsilon.
$$
Therefore
$$
\begin{aligned}
U(f,P)-L(f,P)
&=
\sum_{i=1}^{n}(M_i-m_i)(x_i-x_{i-1})\\
&\le
\varepsilon\sum_{i=1}^{n}(x_i-x_{i-1})\\
&=\varepsilon.
\end{aligned}
$$
If strict inequality is desired, apply step [](#s1-4){.pf-ref} with $\varepsilon/2$ instead.

:::

:::

::: {.pf-step #s1-6}

The upper and lower Riemann integrals are equal.


::: pf-proof

Let
$$
L=\underline{\int_0^1}f,
\qquad
U=\overline{\int_0^1}f.
$$
By step [](#s1-2){.pf-ref},
$$
L\le U.
$$
For every partition $P$,
$$
L(f,P)\le L\le U\le U(f,P),
$$
so
$$
0\le U-L\le U(f,P)-L(f,P).
$$
Given $\varepsilon>0$, choose $P$ from step [](#s1-5){.pf-ref} with
$$
U(f,P)-L(f,P)<\varepsilon.
$$
Then
$$
0\le U-L<\varepsilon.
$$
Since this holds for every $\varepsilon>0$, one has $U=L$.

:::

:::

::: {.pf-step #s1-7}

The Riemann integral
$$
\boxed{\int_0^1 f(x)\,dx}
$$
exists.


::: pf-proof

By step [](#s1-6){.pf-ref}, the upper and lower Riemann integrals coincide. By the definition in step [](#s1-3){.pf-ref}, $f$ is Riemann integrable and their common value is the displayed integral.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} state the definition, and steps [](#s1-4){.pf-ref} through [](#s1-7){.pf-ref} prove existence for continuous $f$.

:::

:::

:::
