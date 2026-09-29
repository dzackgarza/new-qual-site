---
schema: qual/card@1
id: P-BKS11-7B
kind: problem
title: Harmonicity of real and imaginary parts; harmonic polynomials of degree 6
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the statement with page 5 of the retained Spring 2011 solution PDF and restored f in the first Laplacian term where the card had an extraction-corrupted tilde f.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the Cauchy--Riemann proof of harmonicity and the two degree-6 homogeneous harmonic polynomials from the real and imaginary parts of (x+iy)^6.
---

::: {.problem}
Prove that the real and imaginary parts of a holomorphic complex function are harmonic (solutions of Laplace's equation $\frac { \partial ^ { 2 } f } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } f } { \partial y ^ { 2 } } = 0$). Find two linearly independent real solutions of Laplace's equation in two variables that are homogeneous polynomials of degree 6.
:::

::: {.solution}
Let
$$
h(z)=u(x,y)+iv(x,y),
\qquad
z=x+iy,
$$
be holomorphic.

::: pf

::: pf-step
The real and imaginary parts satisfy the Cauchy--Riemann equations
$$
u_x=v_y,
\qquad
u_y=-v_x.
$$

::: pf-proof
These are the Cauchy--Riemann equations for the holomorphic function
$h=u+iv$.
:::

:::

::: {.pf-step #u-harmonic}
The real part $u$ is harmonic:
$$
u_{xx}+u_{yy}=0.
$$

::: pf-proof
Holomorphic functions are smooth, so the required second derivatives
exist and mixed partials commute. Differentiate
$$
u_x=v_y
$$
with respect to $x$ and
$$
u_y=-v_x
$$
with respect to $y$. This gives
$$
u_{xx}=v_{yx}
$$
and
$$
u_{yy}=-v_{xy}.
$$
Since
$$
v_{yx}=v_{xy},
$$
their sum is zero.
:::

:::

::: {.pf-step #v-harmonic}
The imaginary part $v$ is harmonic:
$$
v_{xx}+v_{yy}=0.
$$

::: pf-proof
Rewrite the Cauchy--Riemann equations as
$$
v_x=-u_y,
\qquad
v_y=u_x.
$$
Differentiating the first with respect to $x$ and the second with respect
to $y$ gives
$$
v_{xx}=-u_{yx},
\qquad
v_{yy}=u_{xy}.
$$
Equality of the mixed partials of $u$ yields the claim.
:::

:::

::: {.pf-step #pq-harmonic}
The polynomials
$$
P(x,y)
\coloneqq
x^6-15x^4y^2+15x^2y^4-y^6
$$
and
$$
Q(x,y)
\coloneqq
6x^5y-20x^3y^3+6xy^5
$$
are real homogeneous harmonic polynomials of degree $6$.

::: pf-proof
The holomorphic polynomial
$$
z^6=(x+iy)^6
$$
has real and imaginary parts
$$
\operatorname{Re}(z^6)=P(x,y)
$$
and
$$
\operatorname{Im}(z^6)=Q(x,y).
$$
Every monomial displayed has total degree $6$, so both polynomials are
homogeneous of degree $6$. Steps [](#u-harmonic){.pf-ref} and [](#v-harmonic){.pf-ref} show that the real and
imaginary parts of a holomorphic function are harmonic.
:::

:::

::: {.pf-step #pq-independent}
The polynomials $P$ and $Q$ are linearly independent over $\RR$.

::: pf-proof
The coefficient of $x^6$ in $P$ is $1$, while the coefficient of $x^6$
in $Q$ is $0$. Hence a relation
$$
aP+bQ=0
$$
forces $a=0$. Since $Q\neq0$, it then forces $b=0$.
:::

:::

::: pf-qed
Steps [](#u-harmonic){.pf-ref} and [](#v-harmonic){.pf-ref} prove the harmonicity assertion, while steps [](#pq-harmonic){.pf-ref} and
[](#pq-independent){.pf-ref} provide the required pair of linearly independent real homogeneous
harmonic polynomials of degree $6$.
:::

:::

:::
