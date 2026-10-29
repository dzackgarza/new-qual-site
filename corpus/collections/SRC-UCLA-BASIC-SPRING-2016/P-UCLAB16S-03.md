---
schema: qual/card@1
id: P-UCLAB16S-03
kind: problem
title: First-order error of a Riemann sum
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2016, `assets/attachments/basic-16S.pdf`.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source prints $\lim_{n\to\infty} n\bigl(\sum_{k=0}^{n} f(k/n)-n\int_0^1 f\bigr)$, which diverges for $f\equiv1$. The statement now drops the outer factor $n$; the limit is $(f(0)+f(1))/2$.
---

::: {.problem}
Suppose $f:[0,1]\to\RR$ is continuously differentiable.
Show that the limit
\[
\lim_{n\to\infty} \left(\sum_{k=0}^{n} f\!\left(\frac{k}{n}\right)-n\int_0^1 f(x)\,dx\right)
\]
exists and compute its value.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-6}

Set
\[
h=\frac1n
\]
and
\[
x_k=kh.
\]
Then
\[
\begin{aligned}
&\sum_{k=0}^{n}f(x_k)
-
n\int_0^1f(x)\,dx\\
&\qquad=
f(1)
+
\sum_{k=0}^{n-1}
\left(
f(x_k)
-
n\int_{x_k}^{x_{k+1}}f(x)\,dx
\right).
\end{aligned}
\]


::: pf-proof

Split the integral into the $n$ subintervals
\[
[x_k,x_{k+1}]
\]
and separate the final summand
\[
f(x_n)=f(1).
\]

:::

:::

::: {.pf-step #s1-7}

For each $k$,
\[
\begin{aligned}
f(x_k)
-
n\int_{x_k}^{x_{k+1}}f(x)\,dx
+
\frac{f'(x_k)}{2n}
\end{aligned}
\]
has absolute value at most
\[
\frac{\omega(h)}{2n},
\]
where
\[
\omega(h)
=
\sup_{\substack{u,v\in[0,1]\\|u-v|\le h}}
|f'(u)-f'(v)|.
\]


::: pf-proof

Write
\[
x=x_k+t,
\qquad
0\le t\le h.
\]
By the fundamental theorem of calculus,
\[
f(x_k+t)-f(x_k)
=
\int_0^t f'(x_k+s)\,ds.
\]
Hence
\[
\begin{aligned}
&f(x_k)
-
n\int_{x_k}^{x_{k+1}}f(x)\,dx\\
&\qquad=
-
n\int_0^h
\bigl(
f(x_k+t)-f(x_k)
\bigr)\,dt\\
&\qquad=
-
n\int_0^h
\int_0^t
f'(x_k+s)\,ds\,dt\\
&\qquad=
-
n\int_0^h
(h-s)f'(x_k+s)\,ds.
\end{aligned}
\]
Since
\[
n\int_0^h(h-s)\,ds
=
\frac1{2n},
\]
subtracting the constant value $f'(x_k)$ gives an error bounded by
\[
\begin{aligned}
n\int_0^h
(h-s)
|f'(x_k+s)-f'(x_k)|
\,ds
&\le
n\omega(h)\frac{h^2}{2}\\
&=
\frac{\omega(h)}{2n}.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-8}

Summing step [](#s1-7){.pf-ref} over
\[
k=0,\ldots,n-1
\]
gives
\[
\begin{aligned}
&\sum_{k=0}^{n}f\left(\frac{k}{n}\right)
-
n\int_0^1f(x)\,dx\\
&\qquad=
f(1)
-
\frac1{2n}
\sum_{k=0}^{n-1}
f'\left(\frac{k}{n}\right)
+
R_n,
\end{aligned}
\]
where
\[
|R_n|
\le
\frac{\omega(1/n)}{2}.
\]


::: pf-proof

Add the $n$ estimates from step [](#s1-7){.pf-ref} and use step [](#s1-6){.pf-ref}.
The total error is at most
\[
n\cdot
\frac{\omega(1/n)}{2n}
=
\frac{\omega(1/n)}{2}.
\]

:::

:::

::: {.pf-step #s1-9}

One has
\[
\omega(1/n)\to0
\]
and
\[
\frac1n
\sum_{k=0}^{n-1}
f'\left(\frac{k}{n}\right)
\longrightarrow
\int_0^1f'(x)\,dx.
\]


::: pf-proof

The derivative $f'$ is continuous on the compact interval $[0,1]$, hence uniformly continuous.
Therefore
\[
\omega(h)\to0
\]
as
\[
h\to0.
\]

The second limit is the ordinary left-endpoint Riemann-sum convergence for the continuous function $f'$.

:::

:::

::: {.pf-step #s1-10}

Thus the limit exists and equals
\[
\boxed{\frac{f(0)+f(1)}2}.
\]


::: pf-proof

Take limits in step [](#s1-8){.pf-ref} and use step [](#s1-9){.pf-ref}:
\[
\begin{aligned}
\lim
\left(
\sum_{k=0}^{n}f(k/n)
-
n\int_0^1f
\right)
&=
f(1)
-
\frac12
\int_0^1f'(x)\,dx\\
&=
f(1)
-
\frac12
\bigl(f(1)-f(0)\bigr)\\
&=
\frac{f(0)+f(1)}2.
\end{aligned}
\]

:::

:::

:::

:::
