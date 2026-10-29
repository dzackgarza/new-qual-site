---
schema: qual/card@1
id: P-UCLAB07S-10
kind: problem
title: Increasing functions converging pointwise to a continuous distribution function converge uniformly
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
  note: Checked against Problem 10 of the retained UCLA Basic Examination, Spring 2007.
---

::: {.problem}
Suppose $f_n\colon\RR\to\RR$ satisfy:

- $0\le f_n(x)\le1$ for all $x$ and $n$;

- each $f_n$ is increasing;

- $f_n(x)\to f(x)$ pointwise, where $f$ is continuous on $\RR$;

- $f(x)\to0$ as $x\to-\infty$ and $f(x)\to1$ as $x\to\infty$.

Prove that $f_n\to f$ uniformly on $\RR$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The limit function $f$ is increasing.


::: pf-proof

If
\[
x<y,
\]
then for every $n$,
\[
f_n(x)\le f_n(y)
\]
because $f_n$ is increasing.
Passing to the pointwise limit gives
\[
f(x)\le f(y).
\]

:::

:::

::: {.pf-step #s1-2}

Fix $\varepsilon>0$.
There exists $M>0$ such that
\[
f(-M)<\frac{\varepsilon}{4}
\]
and
\[
f(M)>1-\frac{\varepsilon}{4}.
\]


::: pf-proof

By hypothesis,
\[
f(x)\to0
\]
as
\[
x\to-\infty
\]
and
\[
f(x)\to1
\]
as
\[
x\to+\infty.
\]
Choose $M$ large enough that both inequalities hold.

:::

:::

::: {.pf-step #s1-3}

There exists $N_0$ such that for every $n\ge N_0$,
\[
|f_n(-M)-f(-M)|<\frac{\varepsilon}{4}
\]
and
\[
|f_n(M)-f(M)|<\frac{\varepsilon}{4}.
\]


::: pf-proof

This follows from pointwise convergence at the two fixed points
\[
-M
\quad\text{and}\quad
M.
\]

:::

:::

::: {.pf-step #s1-4}

For every $n\ge N_0$ and every $x\le -M$,
\[
|f_n(x)-f(x)|<\varepsilon.
\]


::: pf-proof

Since both $f_n$ and $f$ are increasing and nonnegative,
\[
0\le f_n(x)\le f_n(-M)
\]
and
\[
0\le f(x)\le f(-M).
\]
By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref},
\[
f_n(-M)
\le
|f_n(-M)-f(-M)|+f(-M)
<
\frac{\varepsilon}{2}.
\]
Also
\[
f(-M)<\frac{\varepsilon}{4}.
\]
Therefore
\[
|f_n(x)-f(x)|
\le
f_n(x)+f(x)
<
\frac{3\varepsilon}{4}
<
\varepsilon.
\]

:::

:::

::: {.pf-step #s1-5}

For every $n\ge N_0$ and every $x\ge M$,
\[
|f_n(x)-f(x)|<\varepsilon.
\]


::: pf-proof

Because
\[
0\le f_n,f\le1
\]
and both are increasing,
\[
f_n(x)\ge f_n(M)
\]
and
\[
f(x)\ge f(M).
\]
Hence
\[
1-f_n(x)
\le
1-f_n(M)
\]
and
\[
1-f(x)
\le
1-f(M).
\]
By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref},
\[
1-f_n(M)
\le
|f_n(M)-f(M)|
+
(1-f(M))
<
\frac{\varepsilon}{2},
\]
while
\[
1-f(M)
<
\frac{\varepsilon}{4}.
\]
Therefore
\[
\begin{aligned}
|f_n(x)-f(x)|
&=
|(1-f_n(x))-(1-f(x))|\\
&\le
(1-f_n(x))+(1-f(x))\\
&<
\frac{3\varepsilon}{4}
<
\varepsilon.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-6}

The continuous function $f$ is uniformly continuous on the compact interval $[-M,M]$.


::: pf-proof

Apply the Heine--Cantor theorem.

:::

:::

::: pf-step

Choose a partition
\[
-M=x_0<x_1<\cdots<x_r=M
\]
such that
\[
f(x_j)-f(x_{j-1})
<
\frac{\varepsilon}{3}
\]
for every $j$.


::: pf-proof

By step [](#s1-6){.pf-ref}, choose $\delta>0$ such that
\[
|x-y|<\delta
\]
implies
\[
|f(x)-f(y)|<\frac{\varepsilon}{3}.
\]
Take a partition with mesh less than $\delta$.
Since $f$ is increasing by step [](#s1-1){.pf-ref},
\[
0\le
f(x_j)-f(x_{j-1})
<
\frac{\varepsilon}{3}.
\]

:::

:::

::: pf-step

There exists $N_1$ such that for every $n\ge N_1$ and every partition point $x_j$,
\[
|f_n(x_j)-f(x_j)|
<
\frac{\varepsilon}{3}.
\]


::: pf-proof

For each fixed $j$, pointwise convergence gives such an index.
There are finitely many partition points, so take the maximum of those indices.

:::

:::

::: {.pf-step #s1-9}

For every $n\ge N_1$ and every $x\in[-M,M]$,
\[
|f_n(x)-f(x)|<\varepsilon.
\]


::: pf-proof

Choose $j$ such that
\[
x_{j-1}\le x\le x_j.
\]
Monotonicity gives
\[
f_n(x_{j-1})
\le
f_n(x)
\le
f_n(x_j)
\]
and
\[
f(x_{j-1})
\le
f(x)
\le
f(x_j).
\]
Hence
\[
\begin{aligned}
f_n(x)-f(x)
&\le
f_n(x_j)-f(x_{j-1})\\
&=
\bigl(f_n(x_j)-f(x_j)\bigr)
+
\bigl(f(x_j)-f(x_{j-1})\bigr)\\
&<
\frac{2\varepsilon}{3},
\end{aligned}
\]
and similarly
\[
\begin{aligned}
f(x)-f_n(x)
&\le
f(x_j)-f_n(x_{j-1})\\
&=
\bigl(f(x_j)-f(x_{j-1})\bigr)
+
\bigl(f(x_{j-1})-f_n(x_{j-1})\bigr)\\
&<
\frac{2\varepsilon}{3}.
\end{aligned}
\]
Therefore
\[
|f_n(x)-f(x)|
<
\varepsilon.
\]

:::

:::

::: {.pf-step #s1-10}

For every
\[
n\ge\max\{N_0,N_1\}
\]
and every
\[
x\in\RR,
\]
one has
\[
|f_n(x)-f(x)|<\varepsilon.
\]


::: pf-proof

If
\[
x\le-M,
\]
apply step [](#s1-4){.pf-ref}.
If
\[
-M\le x\le M,
\]
apply step [](#s1-9){.pf-ref}.
If
\[
x\ge M,
\]
apply step [](#s1-5){.pf-ref}.
These three regions cover $\RR$.

:::

:::

::: {.pf-step #s1-11}

Therefore
\[
\boxed{f_n\to f\text{ uniformly on }\RR}.
\]


::: pf-proof

Step [](#s1-10){.pf-ref} is exactly the definition of uniform convergence.

:::

:::

::: pf-qed

Step [](#s1-11){.pf-ref} is the required conclusion.

:::

:::

:::
