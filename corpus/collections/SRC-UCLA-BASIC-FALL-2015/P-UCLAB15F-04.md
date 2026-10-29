---
schema: qual/card@1
id: P-UCLAB15F-04
kind: problem
title: Limit of a recursively defined Volterra sequence
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
  note: Transcribed from the retained UCLA Basic Examination, Fall 2015, `assets/attachments/basic-15F.pdf`; the PDF is image-only and the preserved extraction supplies the statement text.
---

::: {.problem}
Define $f_n:[0,\infty)\to\RR$ recursively by $f_1(x)=0$ and
\[
f_{n+1}(x)=e^{-2x}+\int_0^x f_n(t)e^{-2t}\,dt,
\qquad n\ge1.
\]
Show that
\[
f(x):=\lim_{n\to\infty}f_n(x)
\]
exists for all $x\ge0$ and identify $f$ explicitly.
:::

::: {.solution}

Define the Volterra operator
\[
(Kh)(x)=\int_0^x h(t)e^{-2t}\,dt
\]
and
\[
g(x)=e^{-2x}.
\]

::: pf

::: {.pf-step #s1-1}

For every $n\ge2$,
\[
f_n
=
\sum_{j=0}^{n-2}K^jg.
\]


::: pf-proof

For $n=2$,
\[
f_2=g+Kf_1=g,
\]
which is the stated sum with only the term $j=0$.
If the formula holds for $f_n$, then the recursion gives
\[
\begin{aligned}
f_{n+1}
&=
g+Kf_n\\
&=
g+
K\left(
\sum_{j=0}^{n-2}K^jg
\right)\\
&=
\sum_{j=0}^{n-1}K^jg.
\end{aligned}
\]
Thus the formula follows by induction.

:::

:::

::: {.pf-step #s1-2}

Fix $R>0$.
For every integer $j\ge0$ and every $x\in[0,R]$,
\[
|K^jg(x)|
\le
\frac{x^j}{j!}
\le
\frac{R^j}{j!}.
\]


::: pf-proof

Proceed by induction on $j$.
For $j=0$,
\[
|g(x)|=e^{-2x}\le1.
\]
Assume
\[
|K^jg(t)|
\le
\frac{t^j}{j!}
\]
for $0\le t\le R$.
Then
\[
\begin{aligned}
|K^{j+1}g(x)|
&=
\left|
\int_0^x K^jg(t)e^{-2t}\,dt
\right|\\
&\le
\int_0^x\frac{t^j}{j!}\,dt\\
&=
\frac{x^{j+1}}{(j+1)!},
\end{aligned}
\]
because $e^{-2t}\le1$.

:::

:::

::: {.pf-step #s1-3}

The series
\[
\sum_{j=0}^{\infty}K^jg
\]
converges uniformly on every compact interval $[0,R]$.


::: pf-proof

By step [](#s1-2){.pf-ref},
\[
|K^jg(x)|
\le
\frac{R^j}{j!}
\]
for all $x\in[0,R]$.
The scalar series
\[
\sum_{j=0}^{\infty}\frac{R^j}{j!}
=
e^R
\]
converges.
The Weierstrass $M$-test therefore gives uniform convergence.

:::

:::

::: {.pf-step #s1-4}

For every $x\ge0$, the limit
\[
f(x)=\lim_{n\to\infty}f_n(x)
\]
exists, and
\[
f=\sum_{j=0}^{\infty}K^jg.
\]


::: pf-proof

Given $x\ge0$, choose $R\ge x$.
By step [](#s1-1){.pf-ref}, $f_n$ is the sequence of partial sums of the series in step [](#s1-3){.pf-ref}.
Uniform convergence on $[0,R]$ therefore gives convergence at the point $x$.

:::

:::

::: {.pf-step #s1-5}

The limit function satisfies the integral equation
\[
f(x)
=
e^{-2x}
+
\int_0^x f(t)e^{-2t}\,dt.
\]


::: pf-proof

Fix $R>0$.
By step [](#s1-3){.pf-ref}, $f_n\to f$ uniformly on $[0,R]$.
The recursion gives
\[
f_{n+1}(x)
=
e^{-2x}
+
\int_0^x f_n(t)e^{-2t}\,dt.
\]
Since multiplication by $e^{-2t}$ preserves uniform convergence, the integrands converge uniformly on $[0,R]$.
Passing to the limit yields the displayed equation for every $x\in[0,R]$.
Since $R$ is arbitrary, it holds for all $x\ge0$.

:::

:::

::: {.pf-step #s1-6}

The function $f$ is continuously differentiable and satisfies
\[
f'(x)
=
-2e^{-2x}
+
e^{-2x}f(x),
\qquad
f(0)=1.
\]


::: pf-proof

The integral equation in step [](#s1-5){.pf-ref} shows that $f$ is continuous.
Therefore
\[
t\mapsto f(t)e^{-2t}
\]
is continuous.
The fundamental theorem of calculus gives
\[
\frac d{dx}
\int_0^x f(t)e^{-2t}\,dt
=
f(x)e^{-2x}.
\]
Differentiating step [](#s1-5){.pf-ref} yields the ODE.
At $x=0$,
\[
f(0)=1.
\]

:::

:::

::: {.pf-step #s1-7}

Put
\[
u(x)=2-f(x).
\]
Then
\[
u'(x)=e^{-2x}u(x),
\qquad
u(0)=1.
\]


::: pf-proof

From step [](#s1-6){.pf-ref},
\[
\begin{aligned}
u'(x)
&=
-f'(x)\\
&=
2e^{-2x}-e^{-2x}f(x)\\
&=
e^{-2x}(2-f(x))\\
&=
e^{-2x}u(x).
\end{aligned}
\]
Also
\[
u(0)=2-f(0)=1.
\]

:::

:::

::: {.pf-step #s1-8}

The solution of the equation in step [](#s1-7){.pf-ref} is
\[
u(x)
=
\exp\left(
\frac{1-e^{-2x}}2
\right).
\]


::: pf-proof

Since $u(0)=1\ne0$, solve the separable equation:
\[
\frac{u'(x)}{u(x)}
=
e^{-2x}.
\]
Integrating from $0$ to $x$ gives
\[
\log u(x)-\log u(0)
=
\int_0^x e^{-2t}\,dt
=
\frac{1-e^{-2x}}2.
\]
Since $u(0)=1$,
\[
\log u(x)
=
\frac{1-e^{-2x}}2.
\]
Exponentiation gives the formula.

:::

:::

::: {.pf-step #s1-9}

Therefore
\[
\boxed{
f(x)
=
2-
\exp\left(
\frac{1-e^{-2x}}2
\right)
}.
\]


::: pf-proof

By definition,
\[
f=2-u.
\]
Substitute the formula from step [](#s1-8){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves existence of the pointwise limit for all $x\ge0$, and step [](#s1-9){.pf-ref} identifies it explicitly.

:::

:::

:::
