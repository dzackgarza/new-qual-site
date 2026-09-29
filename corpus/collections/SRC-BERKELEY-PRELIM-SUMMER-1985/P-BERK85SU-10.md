---
schema: qual/card@1
id: P-BERK85SU-10
kind: problem
title: The equation $z=\lambda-e^{-z}$ has one root in the closed right half-plane
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Writing z=x+iy gives y=e^{-x}sin y. For x>=0, any nonzero y would imply
    |y|<=|sin y|<|y|, so every right-half-plane root is real. The real
    equation is h(x)=x+e^{-x}-lambda=0; h(0)<0<h(lambda) and h'(x)>0 for
    x>0, so there is exactly one root.
---

::: {.problem}
For each $\lambda>1$, prove that the equation
\[
z=\lambda-e^{-z}
\]
has exactly one root in the half-plane $\operatorname{Re}z\ge0$, and that this root is real.
:::

::: {.solution}
Write
$$
z=x+iy,
\qquad
x,y\in\RR.
$$

::: pf

::: {.pf-step #s1}

If $z$ is a root with $x\ge0$, then
$$
y=e^{-x}\sin y.
$$

::: pf-proof

The equation
$$
x+iy
=
\lambda-e^{-x}e^{-iy}
$$
becomes
$$
x+iy
=
\lambda-e^{-x}\cos y
+i e^{-x}\sin y.
$$
Equality of imaginary parts gives the displayed identity.

:::

:::

::: {.pf-step #s2}

Every root in the half-plane $\operatorname{Re}z\ge0$ is
real.

::: pf-proof

Suppose $y\neq0$. By step [](#s1){.pf-ref} and $x\ge0$,
$$
\abs{y}
=
e^{-x}\abs{\sin y}
\le
\abs{\sin y}.
$$
For every nonzero real $y$,
$$
\abs{\sin y}<\abs{y}.
$$
Combining these two inequalities gives the contradiction
$$
\abs{y}<\abs{y}.
$$
Hence $y=0$.

:::

:::

::: pf-step

A real number $x\ge0$ is a root exactly when
$$
h(x)
\coloneqq
x+e^{-x}-\lambda
=
0.
$$

::: pf-proof

With $y=0$, the original equation is
$$
x=\lambda-e^{-x},
$$
which is equivalent to the displayed equation.

:::

:::

::: {.pf-step #s4}

The function $h$ has at least one zero in $(0,\lambda)$.

::: pf-proof

Since $\lambda>1$,
$$
h(0)=1-\lambda<0,
$$
while
$$
h(\lambda)=e^{-\lambda}>0.
$$
The intermediate value theorem therefore gives a zero in
$(0,\lambda)$.

:::

:::

::: {.pf-step #s5}

The function $h$ has at most one zero in $[0,\infty)$.

::: pf-proof

For $x>0$,
$$
h'(x)=1-e^{-x}>0.
$$
Thus $h$ is strictly increasing on $(0,\infty)$. Since $h(0)<0$,
it can have at most one zero in $[0,\infty)$.

:::

:::

::: {.pf-step #s6}

Consequently, the original equation has
$$
\boxed{\text{exactly one root in $\operatorname{Re}z\ge0$, and it is real}.}
$$

::: pf-proof

Step [](#s2){.pf-ref} shows that every root in the closed right half-plane is
real. Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} show that the corresponding real equation
has exactly one nonnegative root.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is the required conclusion.

:::

:::

:::
