---
schema: qual/card@1
id: P-PRELIM82S-11
kind: problem
title: Entire functions of the form $e^x(s(y)+it(y))$
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
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Writing f=u+iv and applying the Cauchy-Riemann equations gives
    s'=-t and t'=s. Thus g=s+it satisfies g'=ig with g(0)=1.
    Differentiating e^{-iy}g(y) shows it is constant, so
    g(y)=e^{iy}=cos y+i sin y.
---

::: {.problem}
Let $s,t:\mathbb R\to\mathbb R$ be differentiable and suppose
\[
f(x+iy)=e^x\bigl(s(y)+it(y)\bigr)
\]
is holomorphic on $\mathbb C$, with
\[
s(0)=1,
\qquad
t(0)=0.
\]
Determine $s(y)$ and $t(y)$.
:::

::: {.solution}
Write
$$
f(x+iy)=u(x,y)+iv(x,y),
$$
where
$$
u(x,y)=e^x s(y),
\qquad
v(x,y)=e^x t(y).
$$

::: pf

::: {.pf-step #s1}

The Cauchy--Riemann equations imply
$$
s'(y)=-t(y),
\qquad
t'(y)=s(y)
$$
for every $y\in\RR$.

::: pf-proof

Since $f$ is holomorphic,
$$
u_x=v_y,
\qquad
u_y=-v_x.
$$
The four partial derivatives are
$$
u_x=e^x s(y),
\qquad
u_y=e^x s'(y),
$$
and
$$
v_x=e^x t(y),
\qquad
v_y=e^x t'(y).
$$
Because $e^x>0$, the first Cauchy--Riemann equation gives
$s=t'$, while the second gives $s'=-t$.

:::

:::

::: {.pf-step #s2}

Define
$$
g(y)=s(y)+it(y).
$$
Then
$$
g'(y)=ig(y)
$$
and
$$
g(0)=1.
$$

::: pf-proof

By step [](#s1){.pf-ref},
$$
\begin{aligned}
g'(y)
&=s'(y)+it'(y)\\
&=-t(y)+is(y)\\
&=i\bigl(s(y)+it(y)\bigr)\\
&=ig(y).
\end{aligned}
$$
The initial conditions give
$$
g(0)=s(0)+it(0)=1.
$$

:::

:::

::: {.pf-step #s3}

One has
$$
g(y)=e^{iy}
$$
for every $y\in\RR$.

::: pf-proof

Set
$$
h(y)=e^{-iy}g(y).
$$
By step [](#s2){.pf-ref},
$$
\begin{aligned}
h'(y)
&=-ie^{-iy}g(y)+e^{-iy}g'(y)\\
&=e^{-iy}\bigl(-ig(y)+ig(y)\bigr)\\
&=0.
\end{aligned}
$$
Hence $h$ is constant. Since
$$
h(0)=g(0)=1,
$$
we have $h(y)=1$, and therefore $g(y)=e^{iy}$.

:::

:::

::: {.pf-step #s4}

The required functions are
$$
\boxed{s(y)=\cos y},
\qquad
\boxed{t(y)=\sin y}.
$$

::: pf-proof

By step [](#s3){.pf-ref} and Euler's formula,
$$
s(y)+it(y)
=
g(y)
=
e^{iy}
=
\cos y+i\sin y.
$$
Equality of real and imaginary parts gives the result.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} determines both functions.

:::

:::

:::
