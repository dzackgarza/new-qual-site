---
schema: qual/card@1
id: P-UCLAB07F-04
kind: problem
title: Midpoint quadrature error from a bounded second derivative
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 4 of the retained UCLA Basic Examination, Fall 2007 PDF.
---

::: {.problem}
Suppose $f:\RR\to\RR$ is twice differentiable and $|f''(x)|\le B$.

(a) Prove that \[\left|2Af(0)-\int_{-A}^{A}f(x)\,dx\right|\le \frac{A^3}{3}B.\]

(b) Use part (a) to justify \[\left|\int_a^b f(x)\,dx-\frac{b-a}{n}\sum_{k=1}^n f\!\left(a+\frac{2k-1}{2n}(b-a)\right)\right|\le Cn^{-2},\] where $C$ is independent of $n$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $x\in\RR$,
\[
|f'(x)-f'(0)|\le B|x|.
\]


::: pf-proof

If $x=0$, the inequality is immediate. If $x\ne0$, apply the mean value theorem to $f'$ on the interval with endpoints $0$ and $x$. Since $f''$ exists everywhere, there is a point $\xi$ between $0$ and $x$ such that
\[
f'(x)-f'(0)=f''(\xi)x.
\]
Therefore
\[
|f'(x)-f'(0)|
\le
B|x|.
\]

:::

:::

::: {.pf-step #s1-2}

For every $x\in\RR$,
\[
\left|f(x)-f(0)-xf'(0)\right|
\le
\frac B2x^2.
\]


::: pf-proof

Since $f'$ is differentiable, it is continuous. Hence
\[
f(x)-f(0)-xf'(0)
=
\int_0^x\bigl(f'(t)-f'(0)\bigr)\,dt.
\]
Using step [](#s1-1){.pf-ref},
\[
\left|f(x)-f(0)-xf'(0)\right|
\le
\int_0^{|x|}Bt\,dt
=
\frac B2x^2.
\]

:::

:::

::: {.pf-step #s1-3}

For every $A>0$,
\[
\boxed{
\left|
2Af(0)-\int_{-A}^{A}f(x)\,dx
\right|
\le
\frac{A^3}{3}B
}.
\]


::: pf-proof

By step [](#s1-2){.pf-ref},
\[
\left|f(x)-f(0)-xf'(0)\right|
\le
\frac B2x^2.
\]
Integrate over $[-A,A]$. Since
\[
\int_{-A}^{A}xf'(0)\,dx=0,
\]
one obtains
\[
\begin{aligned}
\left|
\int_{-A}^{A}f(x)\,dx-2Af(0)
\right|
&\le
\int_{-A}^{A}\frac B2x^2\,dx\\
&=
\frac B2\cdot\frac{2A^3}{3}\\
&=
\frac{A^3}{3}B.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-4}

For part (b), set
\[
h=\frac{b-a}{n}
\]
and
\[
c_k=a+\left(k-\frac12\right)h,
\qquad
k=1,\ldots,n.
\]
Then
\[
[a,b]
=
\bigcup_{k=1}^n
\left[c_k-\frac h2,c_k+\frac h2\right]
\]
with disjoint interiors.


::: pf-proof

The $k$th interval is
\[
\left[a+(k-1)h,\ a+kh\right].
\]
These are exactly the $n$ equal subintervals of the uniform partition of $[a,b]$.

:::

:::

::: {.pf-step #s1-5}

For each $k$,
\[
\left|
\int_{c_k-h/2}^{c_k+h/2}f(x)\,dx
-hf(c_k)
\right|
\le
\frac{Bh^3}{24}.
\]


::: pf-proof

Apply step [](#s1-3){.pf-ref} to the translated function
\[
g_k(t)=f(c_k+t)
\]
with
\[
A=\frac h2.
\]
Since
\[
|g_k''(t)|=|f''(c_k+t)|\le B,
\]
step [](#s1-3){.pf-ref} gives
\[
\left|
h f(c_k)
-
\int_{-h/2}^{h/2}f(c_k+t)\,dt
\right|
\le
\frac{B}{3}\left(\frac h2\right)^3
=
\frac{Bh^3}{24}.
\]
Changing variables $x=c_k+t$ gives the stated estimate.

:::

:::

::: {.pf-step #s1-6}

The midpoint quadrature error satisfies
\[
\boxed{
\left|
\int_a^b f(x)\,dx
-
\frac{b-a}{n}
\sum_{k=1}^n
f\!\left(a+\frac{2k-1}{2n}(b-a)\right)
\right|
\le
\frac{B(b-a)^3}{24}\,n^{-2}
}.
\]


::: pf-proof

By step [](#s1-4){.pf-ref},
\[
\int_a^b f(x)\,dx
=
\sum_{k=1}^n
\int_{c_k-h/2}^{c_k+h/2}f(x)\,dx.
\]
Subtract
\[
h\sum_{k=1}^n f(c_k)
\]
and apply the triangle inequality together with step [](#s1-5){.pf-ref}:
\[
\begin{aligned}
\left|
\int_a^b f
-h\sum_{k=1}^n f(c_k)
\right|
&\le
\sum_{k=1}^n\frac{Bh^3}{24}\\
&=
\frac{Bn h^3}{24}\\
&=
\frac{B(b-a)^3}{24n^2}.
\end{aligned}
\]
Substituting the definitions of $h$ and $c_k$ gives exactly the displayed formula.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), and step [](#s1-6){.pf-ref} proves part (b) with
\[
C=\frac{B(b-a)^3}{24},
\]
which is independent of $n$.

:::

:::

:::
