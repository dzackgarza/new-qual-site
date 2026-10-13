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
---

::: {.problem}
Suppose $f:[0,1]\to\mathbb R$ is continuously differentiable.
Show that the limit
\[
\lim_{n\to\infty} n\left(\sum_{k=0}^{n} f\!\left(\frac{k}{n}\right)-n\int_0^1 f(x)\,dx\right)
\]
exists and compute its value.
:::

::: {.solution}
The statement is false as printed.

<1>1. Take the continuously differentiable function
\[
\boxed{f(x)=1}
\]
on $[0,1]$.

::: {.proof}
Constant functions are continuously differentiable.
:::

<1>2. For this function,
\[
\sum_{k=0}^{n}f\left(\frac{k}{n}\right)
=
n+1
\]
and
\[
n\int_0^1f(x)\,dx
=
n.
\]

::: {.proof}
There are exactly
\[
n+1
\]
terms in the sum, each equal to $1$.
Also,
\[
\int_0^1 1\,dx=1.
\]
:::

<1>3. Hence the expression in the source equals
\[
\boxed{n}
\]
for every positive integer $n$.

::: {.proof}
By step <1>2,
\[
n
\left(
(n+1)-n
\right)
=
n.
\]
:::

<1>4. Therefore the displayed limit does not exist as a finite real number.

::: {.proof}
Step <1>3 gives
\[
n\to+\infty.
\]
Thus the literal claim that the limit exists is false.
:::

<1>5. The natural corrected statement is obtained by removing the outer factor $n$:
\[
\boxed{
\lim_{n\to\infty}
\left(
\sum_{k=0}^{n}f\left(\frac{k}{n}\right)
-
n\int_0^1f(x)\,dx
\right)
=
\frac{f(0)+f(1)}{2}.
}
\]

::: {.proof}
The remaining steps prove this corrected first-order Riemann-sum formula.
:::

<1>6. Set
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

::: {.proof}
Split the integral into the $n$ subintervals
\[
[x_k,x_{k+1}]
\]
and separate the final summand
\[
f(x_n)=f(1).
\]
:::

<1>7. For each $k$,
\[
\begin{aligned}
f(x_k)
-
n\int_{x_k}^{x_{k+1}}f(x)\,dx

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

::: {.proof}
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

<1>8. Summing step <1>7 over
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

::: {.proof}
Add the $n$ estimates from step <1>7 and use step <1>6.
The total error is at most
\[
n\cdot
\frac{\omega(1/n)}{2n}
=
\frac{\omega(1/n)}{2}.
\]
:::

<1>9. One has
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

::: {.proof}
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

<1>10. Thus the corrected expression converges to
\[
\frac{f(0)+f(1)}2.
\]

::: {.proof}
Take limits in step <1>8 and use step <1>9:
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

<1>11. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 disprove the literal source statement.
Steps <1>5--<1>10 prove the natural corrected first-order Riemann-sum formula.
:::
:::
