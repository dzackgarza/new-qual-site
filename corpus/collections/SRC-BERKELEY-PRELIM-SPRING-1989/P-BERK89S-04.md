---
schema: qual/card@1
id: P-BERK89S-04
kind: problem
title: $z+\lambda-e^z$ has exactly one zero in the left half-plane
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    The imaginary-part equation forces every left-half-plane zero to be real;
    strict monotonicity and the intermediate value theorem then give the unique
    real zero.
---

::: {.problem}
Let $1<\lambda<\infty$. Prove that
\[
f_\lambda(z)=z+\lambda-e^z
\]
has exactly one zero in the half-plane
\[
\operatorname{Re}z<0,
\]
and that this zero is real.
:::

::: {.solution}
For real $x$, set
$$
h(x)=x+\lambda-e^x.
$$

<1>1. Every zero of $f_\lambda$ in the half-plane $\operatorname{Re}z<0$ is real.

::: {.proof}
Let $z=x+iy$ with $x<0$, and suppose that $f_\lambda(z)=0$. Then
$$
x+\lambda+iy=e^{x+iy}=e^x(\cos y+i\sin y),
$$
so comparison of imaginary parts gives
$$
y=e^x\sin y.
$$
If $y\neq0$, then
$$
\abs{y}=e^x\abs{\sin y}\leq e^x\abs{y}<\abs{y},
$$
because $x<0$ implies $e^x<1$. This is impossible. Hence $y=0$, so $z$ is real.
:::

<1>2. The function $h$ is strictly increasing on $(-\infty,0]$.

::: {.proof}
For $x<0$,
$$
h'(x)=1-e^x>0.
$$
If $x_1<x_2\leq0$, the mean value theorem gives some
$c\in(x_1,x_2)$ such that
$$
h(x_2)-h(x_1)=h'(c)(x_2-x_1)>0.
$$
Thus $h$ is strictly increasing on $(-\infty,0]$.
:::

<1>3. There is a unique $x_\lambda\in(-\lambda,0)$ such that $h(x_\lambda)=0$.

::: {.proof}
Since $\lambda>1$,
$$
h(-\lambda)=-e^{-\lambda}<0
\qquad\text{and}\qquad
h(0)=\lambda-1>0.
$$
The intermediate value theorem therefore gives
$x_\lambda\in(-\lambda,0)$ with $h(x_\lambda)=0$. Uniqueness follows from the
strict monotonicity in step <1>2.
:::

<1>4. The function $f_\lambda$ has exactly one zero in
$\operatorname{Re}z<0$, namely the real number $x_\lambda$ from step <1>3.

::: {.proof}
For real $x$, one has $f_\lambda(x)=h(x)$, so step <1>3 shows that
$x_\lambda$ is a zero of $f_\lambda$ in the left half-plane. Conversely, step
<1>1 shows that every zero of $f_\lambda$ in that half-plane is real, and step
<1>3 shows that $h$ has only the one real zero $x_\lambda$ there.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 proves both required assertions.
:::
:::
