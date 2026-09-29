---
schema: qual/card@1
id: P-BERK78S-17
kind: problem
title: Solution space and decaying solutions of $f'''+f''-2f=0$
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
    Linearity of the differential operator makes E a vector space, while
    the third-order initial-value theorem identifies a solution uniquely by
    f(0),f'(0),f''(0), so dim E=3. Factoring the characteristic polynomial
    gives the basis e^t, e^{-t}cos t, e^{-t}sin t. The decaying subspace
    excludes e^t, and the two initial conditions then give
    g(t)=2e^{-t}sin t.
---

::: {.problem}
Let $E$ be the set of functions $f:\mathbb R\to\mathbb R$ satisfying
\[
f'''+f''-2f=0.
\]

1. Prove that $E$ is a vector space and find its dimension.
2. Let
   \[
   E_0=\{g\in E:\lim_{t\to\infty}g(t)=0\}.
   \]
   Find $g\in E_0$ such that $g(0)=0$ and $g'(0)=2$.
:::

::: {.solution}
Define the linear differential operator
$$
L(f)=f'''+f''-2f.
$$

::: pf

::: pf-step

The set
$$
E=\ker L
$$
is a real vector space.

::: pf-proof

The operator $L$ is linear. Thus if
$$
f,g\in E
$$
and $a,b\in\RR$, then
$$
L(af+bg)
=
aL(f)+bL(g)
=
0.
$$
Hence $af+bg\in E$.

:::

:::

::: {.pf-step #s2}

The map
$$
\Phi:E\longrightarrow\RR^3,
\qquad
\Phi(f)=\bigl(f(0),f'(0),f''(0)\bigr),
$$
is a linear isomorphism.

::: pf-proof

Linearity is immediate.

For injectivity, if
$$
\Phi(f)=(0,0,0),
$$
then $f$ solves the third-order linear initial-value problem
$$
f'''+f''-2f=0,
\qquad
f(0)=f'(0)=f''(0)=0.
$$
Uniqueness for linear ordinary differential equations implies that the
only such solution is $f\equiv0$.

For surjectivity, given any
$$
(a,b,c)\in\RR^3,
$$
the standard existence theorem for linear ordinary differential equations
gives a solution of
$$
f'''+f''-2f=0
$$
with
$$
f(0)=a,\qquad f'(0)=b,\qquad f''(0)=c.
$$
The coefficients of the equation are constant, so the solution is defined
for every $t\in\RR$. Thus every element of $\RR^3$ lies in the image.

:::

:::

::: {.pf-step #s3}

The vector space $E$ has dimension
$$
\boxed{3}.
$$

::: pf-proof

Step [](#s2){.pf-ref} gives
$$
E\cong\RR^3.
$$

:::

:::

::: {.pf-step #s4}

The characteristic polynomial of the differential equation factors
as
$$
r^3+r^2-2
=
(r-1)(r^2+2r+2)
=
(r-1)\bigl((r+1)^2+1\bigr).
$$

::: pf-proof

Direct multiplication gives
$$
(r-1)(r^2+2r+2)
=
r^3+r^2-2.
$$
Completing the square gives the second factorization.

:::

:::

::: {.pf-step #s5}

The three functions
$$
u_1(t)=e^t,
\qquad
u_2(t)=e^{-t}\cos t,
\qquad
u_3(t)=e^{-t}\sin t
$$
belong to $E$.

::: pf-proof

Step [](#s4){.pf-ref} gives the characteristic roots
$$
1,\qquad -1+i,\qquad -1-i.
$$
The corresponding real solutions are exactly the three displayed
functions. Direct differentiation also verifies
$$
L(u_j)=0
$$
for each $j$.

:::

:::

::: {.pf-step #s6}

The functions $u_1,u_2,u_3$ are linearly independent.

::: pf-proof

Suppose
$$
A e^t
+
e^{-t}(B\cos t+C\sin t)
=
0
$$
for every $t$. Multiply by $e^{-t}$:
$$
A
+
e^{-2t}(B\cos t+C\sin t)
=
0.
$$
Letting $t\to\infty$ gives
$$
A=0.
$$
Then
$$
B\cos t+C\sin t=0
$$
for every $t$. Evaluating at $t=0$ gives $B=0$, and evaluating at
$t=\pi/2$ gives $C=0$.

:::

:::

::: pf-step

Every element of $E$ has a unique expression
$$
f(t)
=
A e^t
+
e^{-t}(B\cos t+C\sin t).
$$

::: pf-proof

Steps [](#s3){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} show that $u_1,u_2,u_3$ are three linearly
independent vectors in the three-dimensional space $E$. Hence they form a
basis.

:::

:::

::: {.pf-step #s8}

A solution
$$
f(t)
=
A e^t
+
e^{-t}(B\cos t+C\sin t)
$$
lies in $E_0$ exactly when
$$
A=0.
$$

::: pf-proof

If $A=0$, then
$$
\abs{f(t)}
\leq
e^{-t}(\abs{B}+\abs{C})
\longrightarrow
0
$$
as $t\to\infty$.

If $A\neq0$, then
$$
e^{-t}f(t)
=
A
+
e^{-2t}(B\cos t+C\sin t)
\longrightarrow
A\neq0.
$$
Thus $f(t)$ grows on the scale of $e^t$ and cannot tend to zero.

:::

:::

::: {.pf-step #s9}

The unique element $g\in E_0$ satisfying
$$
g(0)=0,
\qquad
g'(0)=2
$$
is
$$
\boxed{
g(t)=2e^{-t}\sin t.
}
$$

::: pf-proof

By step [](#s8){.pf-ref}, write
$$
g(t)=e^{-t}(B\cos t+C\sin t).
$$
Then
$$
g(0)=B,
$$
so the condition $g(0)=0$ gives
$$
B=0.
$$
Thus
$$
g(t)=Ce^{-t}\sin t,
$$
and
$$
g'(t)
=
Ce^{-t}(\cos t-\sin t).
$$
Hence
$$
g'(0)=C.
$$
The condition $g'(0)=2$ gives $C=2$, proving the formula.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} answers part (1), and step [](#s9){.pf-ref} answers part (2).

:::

:::

:::
