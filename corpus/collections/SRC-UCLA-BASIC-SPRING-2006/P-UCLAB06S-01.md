---
schema: qual/card@1
id: P-UCLAB06S-01
kind: problem
title: Uniform limits of Riemann integrable functions are Riemann integrable
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 1 of the retained UCLA Basic Examination Spring 2006 PDF.
---

::: {.problem}
(A) Define precisely the notion of Riemann integrability for a function $f(x)$ on $[0, 1]$.

(B) Suppose that $f_n(x)$ is a sequence of Riemann integrable functions on $[0, 1]$ such that $\{f_n(x)\}$ converges uniformly to $f(x)$. Prove that $f(x)$ is Riemann integrable.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let
\[
P:\quad 0=x_0<x_1<\cdots<x_m=1
\]
be a partition of $[0,1]$.
For each subinterval
\[
I_i=[x_{i-1},x_i],
\]
define
\[
M_i(f)=\sup_{x\in I_i}f(x),
\qquad
m_i(f)=\inf_{x\in I_i}f(x),
\]
and the Darboux sums
\[
U(f,P)
=
\sum_{i=1}^m M_i(f)(x_i-x_{i-1}),
\]
\[
L(f,P)
=
\sum_{i=1}^m m_i(f)(x_i-x_{i-1}).
\]


::: pf-proof

These are the upper and lower Darboux sums associated to the partition $P$.

:::

:::

::: {.pf-step #s1-2}

A bounded function
\[
f:[0,1]\to\RR
\]
is Riemann integrable if
\[
\inf_P U(f,P)
=
\sup_P L(f,P).
\]
Equivalently, $f$ is Riemann integrable if for every $\varepsilon>0$ there exists a partition $P$ such that
\[
U(f,P)-L(f,P)<\varepsilon.
\]


::: pf-proof

The equality of the upper and lower Darboux integrals is the definition.
The stated $\varepsilon$-criterion follows because for every partition
\[
L(f,P)
\le
\underline{\int_0^1}f
\le
\overline{\int_0^1}f
\le
U(f,P),
\]
and common refinements can only increase lower sums and decrease upper sums.

:::

:::

::: {.pf-step #s1-3}

The uniform limit $f$ is bounded.


::: pf-proof

Choose $N$ such that
\[
\|f-f_N\|_\infty<1.
\]
Since $f_N$ is Riemann integrable, it is bounded; let
\[
|f_N(x)|\le M.
\]
Then
\[
|f(x)|
\le
|f(x)-f_N(x)|+|f_N(x)|
<
1+M
\]
for every $x\in[0,1]$.

:::

:::

::: {.pf-step #s1-4}

Fix $\varepsilon>0$.
Choose $N$ such that
\[
\|f-f_N\|_\infty<\frac{\varepsilon}{4}.
\]


::: pf-proof

This is possible because
\[
f_n\to f
\]
uniformly.

:::

:::

::: {.pf-step #s1-5}

Since $f_N$ is Riemann integrable, there exists a partition $P$ such that
\[
U(f_N,P)-L(f_N,P)<\frac{\varepsilon}{2}.
\]


::: pf-proof

Apply the Darboux criterion from step [](#s1-2){.pf-ref} to the Riemann integrable function $f_N$ with tolerance $\varepsilon/2$.

:::

:::

::: {.pf-step #s1-6}

For every subinterval $I_i$ of $P$,
\[
M_i(f)
\le
M_i(f_N)+\frac{\varepsilon}{4}
\]
and
\[
m_i(f)
\ge
m_i(f_N)-\frac{\varepsilon}{4}.
\]


::: pf-proof

For every $x\in I_i$,
\[
f(x)
\le
f_N(x)+\frac{\varepsilon}{4}.
\]
Taking the supremum over $I_i$ gives the first inequality.

Similarly,
\[
f(x)
\ge
f_N(x)-\frac{\varepsilon}{4},
\]
and taking the infimum gives the second.

:::

:::

::: {.pf-step #s1-7}

For the partition $P$ from step [](#s1-5){.pf-ref},
\[
U(f,P)-L(f,P)
<
\varepsilon.
\]


::: pf-proof

By step [](#s1-6){.pf-ref},
\[
\begin{aligned}
U(f,P)-L(f,P)
&=
\sum_{i=1}^m
\bigl(M_i(f)-m_i(f)\bigr)
(x_i-x_{i-1})\\
&\le
\sum_{i=1}^m
\left(
M_i(f_N)-m_i(f_N)
+
\frac{\varepsilon}{2}
\right)
(x_i-x_{i-1})\\
&=
U(f_N,P)-L(f_N,P)
+
\frac{\varepsilon}{2}
\sum_{i=1}^m(x_i-x_{i-1}).
\end{aligned}
\]
Since
\[
\sum_{i=1}^m(x_i-x_{i-1})=1,
\]
and step [](#s1-5){.pf-ref} gives
\[
U(f_N,P)-L(f_N,P)<\frac{\varepsilon}{2},
\]
one obtains
\[
U(f,P)-L(f,P)<\varepsilon.
\]

:::

:::

::: {.pf-step #s1-8}

Therefore $f$ is Riemann integrable on $[0,1]$.


::: pf-proof

Step [](#s1-3){.pf-ref} gives boundedness.
Step [](#s1-7){.pf-ref} shows that for every $\varepsilon>0$ there is a partition with upper-minus-lower sum less than $\varepsilon$.
By the criterion in step [](#s1-2){.pf-ref},
\[
\boxed{f\text{ is Riemann integrable}.}
\]

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} answer part (A), and steps [](#s1-3){.pf-ref} through [](#s1-8){.pf-ref} prove part (B).

:::

:::

:::
