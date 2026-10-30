---
schema: qual/card@1
id: P-UMNCP-F11-05
kind: problem
title: A periodic entire function with exponential radial bound is constant
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Fall 2011, 5 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Let $f$ be entire.
Suppose
$$
f(z+1)=f(z)
$$
for every $z\in\CC$, and
$$
\abs{f(z)}\le e^{\abs{z}}
$$
for every $z\in\CC$. Prove that $f$ is constant.
:::

::: {.solution}

For each integer
$$
n\in\ZZ
$$
and each real number
$$
y,
$$
define
$$
c_n(y)
\coloneqq
\int_0^1
f(x+iy)
e^{-2\pi i n(x+iy)}
\,dx.
$$

::: pf

::: {.pf-step #s1-1}

For every
$$
n\in\ZZ,
$$
the quantity
$$
c_n(y)
$$
is independent of $y$.


::: pf-proof

Fix real numbers
$$
y_0<y_1
$$
and consider the entire function
$$
F_n(z)
\coloneqq
f(z)e^{-2\pi inz}.
$$
Because
$$
f(z+1)=f(z)
$$
and
$$
e^{-2\pi in(z+1)}
=
e^{-2\pi inz},
$$
the function $F_n$ is also $1$-periodic.

Integrate $F_n$ around the rectangle with vertices
$$
iy_0,\quad
1+iy_0,\quad
1+iy_1,\quad
iy_1.
$$
By Cauchy's theorem, the total integral is zero. The integrals over the two vertical sides cancel because of $1$-periodicity. Hence the two horizontal integrals are equal:
$$
\int_0^1
F_n(x+iy_0)
\,dx
=
\int_0^1
F_n(x+iy_1)
\,dx.
$$
These are exactly
$$
c_n(y_0)
\quad\text{and}\quad
c_n(y_1).
$$

:::

:::

::: {.pf-step #s1-2}

For
$$
0\le x\le1,
$$
one has
$$
\abs{f(x+iy)}
\le
e^{1+\abs{y}}.
$$


::: pf-proof

By the triangle inequality,
$$
\abs{x+iy}
\le
\abs{x}+\abs{y}
\le
1+\abs{y}.
$$
The assumed growth bound therefore gives
$$
\abs{f(x+iy)}
\le
e^{\abs{x+iy}}
\le
e^{1+\abs{y}}.
$$

:::

:::

::: {.pf-step #s1-3}

If
$$
n>0,
$$
then
$$
\boxed{c_n=0}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, write simply
$$
c_n
$$
for the common value of $c_n(y)$. For
$$
y<0,
$$
steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} give
$$
\begin{aligned}
\abs{c_n}
&\le
\int_0^1
\abs{f(x+iy)}
\abs{
e^{-2\pi in(x+iy)}
}
dx\\
&\le
e^{1-y}
e^{2\pi ny}.
\end{aligned}
$$
Thus
$$
\abs{c_n}
\le
e^{1+(2\pi n-1)y}.
$$
Since
$$
2\pi n-1>0,
$$
letting
$$
y\to-\infty
$$
forces the right-hand side to tend to $0$. Hence
$$
c_n=0.
$$

:::

:::

::: {.pf-step #s1-4}

If
$$
n<0,
$$
then
$$
\boxed{c_n=0}.
$$


::: pf-proof

For
$$
y>0,
$$
steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} give
$$
\begin{aligned}
\abs{c_n}
&\le
e^{1+y}
e^{2\pi ny}\\
&=
e^{1+(1+2\pi n)y}.
\end{aligned}
$$
Since
$$
n\le-1,
$$
one has
$$
1+2\pi n<0.
$$
Letting
$$
y\to+\infty
$$
forces the right-hand side to $0$. Therefore
$$
c_n=0.
$$

:::

:::

::: {.pf-step #s1-5}

For each fixed real $y$, the ordinary Fourier coefficients of the continuous $1$-periodic function
$$
x\longmapsto f(x+iy)
$$
vanish in every nonzero degree.


::: pf-proof

Its $n$th Fourier coefficient is
$$
\widehat f_y(n)
\coloneqq
\int_0^1
f(x+iy)e^{-2\pi inx}
\,dx.
$$
By definition of $c_n$,
$$
c_n
=
e^{2\pi ny}
\widehat f_y(n).
$$
Steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} give
$$
c_n=0
$$
for
$$
n\ne0,
$$
and the exponential factor is nonzero. Hence
$$
\widehat f_y(n)=0
$$
for every nonzero integer $n$.

:::

:::

::: {.pf-step #s1-6}

For every fixed $y$, the function
$$
x\longmapsto f(x+iy)
$$
is constant in $x$.


::: pf-proof

By step [](#s1-5){.pf-ref}, all nonconstant Fourier coefficients of this continuous $1$-periodic function vanish. Uniqueness of Fourier coefficients for continuous periodic functions therefore implies that the function equals its constant Fourier mode.

:::

:::

::: {.pf-step #s1-7}

The constant from step [](#s1-6){.pf-ref} is independent of $y$.


::: pf-proof

The constant Fourier mode is
$$
\widehat f_y(0)
=
\int_0^1
f(x+iy)
\,dx
=
c_0(y).
$$
By step [](#s1-1){.pf-ref},
$$
c_0(y)
$$
is independent of $y$.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{f\text{ is constant on }\CC}.
$$


::: pf-proof

Step [](#s1-6){.pf-ref} says that $f$ is constant along every horizontal line, and step [](#s1-7){.pf-ref} says that these constants are all the same.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required conclusion.

:::

:::

:::
