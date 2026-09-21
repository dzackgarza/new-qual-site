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

<1>1. If $z$ is a root with $x\ge0$, then
$$
y=e^{-x}\sin y.
$$

::: {.proof}
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

<1>2. Every root in the half-plane $\operatorname{Re}z\ge0$ is
real.

::: {.proof}
Suppose $y\neq0$. By step <1>1 and $x\ge0$,
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

<1>3. A real number $x\ge0$ is a root exactly when
$$
h(x)
\coloneqq
x+e^{-x}-\lambda
=
0.
$$

::: {.proof}
With $y=0$, the original equation is
$$
x=\lambda-e^{-x},
$$
which is equivalent to the displayed equation.
:::

<1>4. The function $h$ has at least one zero in $(0,\lambda)$.

::: {.proof}
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

<1>5. The function $h$ has at most one zero in $[0,\infty)$.

::: {.proof}
For $x>0$,
$$
h'(x)=1-e^{-x}>0.
$$
Thus $h$ is strictly increasing on $(0,\infty)$. Since $h(0)<0$,
it can have at most one zero in $[0,\infty)$.
:::

<1>6. Consequently, the original equation has
$$
\boxed{\text{exactly one root in $\operatorname{Re}z\ge0$, and it is real}.}
$$

::: {.proof}
Step <1>2 shows that every root in the closed right half-plane is
real. Steps <1>4 and <1>5 show that the corresponding real equation
has exactly one nonnegative root.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
