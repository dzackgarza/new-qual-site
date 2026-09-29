---
schema: qual/card@1
id: P-BKF06-5A
kind: problem
title: The Volterra integration operator on $C^0[0,1]$ has no eigenvectors
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 5A of the retained Berkeley Fall 2006 preliminary-exam solution packet f06solution.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained fundamental-theorem-of-calculus
    argument, including the lambda=0 case and the initial condition at zero.
---

::: {.problem}
Let $C^0[0,1]$ be the real vector space of continuous functions $[0,1]\to\mathbb R$.
Show that the linear operator $T:C^0[0,1]\to C^0[0,1]$ defined by
\[
(Tf)(x)=\int_0^x f(y)\,dy
\]
has no nonzero eigenvectors.
:::

::: {.solution}

::: pf

::: {.pf-step #lambda-zero-implies-f-zero}
If $Tf=\lambda f$ with $\lambda=0$, then $f=0$.

::: pf-proof
The equation $Tf=0$ means
$$
\int_0^x f(y)\,dy=0
$$
for every $x\in[0,1]$. By the fundamental theorem of calculus, the
left-hand side is differentiable with derivative $f(x)$. Hence
$f(x)=0$ for every $x$.
:::

:::

::: {.pf-step #differentiable-and-ode}
If $Tf=\lambda f$ with $\lambda\ne0$, then $f$ is
differentiable and satisfies
$$
f'(x)=\frac1\lambda f(x),
\qquad
f(0)=0.
$$

::: pf-proof
The function $Tf$ is differentiable, with
$$
(Tf)'=f.
$$
Since $Tf=\lambda f$ and $\lambda\ne0$, it follows that $f$ is
differentiable and
$$
f=(Tf)'=\lambda f'.
$$
Thus $f'=f/\lambda$. Evaluating $Tf=\lambda f$ at $x=0$ gives
$$
0=(Tf)(0)=\lambda f(0),
$$
so $f(0)=0$.
:::

:::

::: {.pf-step #f-forced-zero}
The equations in step [](#differentiable-and-ode){.pf-ref} force $f=0$.

::: pf-proof
Define
$$
h(x)=e^{-x/\lambda}f(x).
$$
Then step [](#differentiable-and-ode){.pf-ref} gives
$$
h'(x)
=
e^{-x/\lambda}
\left(f'(x)-\frac1\lambda f(x)\right)
=
0.
$$
Hence $h$ is constant. Since
$$
h(0)=f(0)=0,
$$
one has $h=0$ and therefore $f=0$.
:::

:::

::: {.pf-step #no-nonzero-eigenvectors}
The operator $T$ has no nonzero eigenvectors.

::: pf-proof
If $f$ were an eigenvector with eigenvalue $\lambda$, then step
[](#lambda-zero-implies-f-zero){.pf-ref} would give $f=0$ when $\lambda=0$, while steps [](#differentiable-and-ode){.pf-ref} and [](#f-forced-zero){.pf-ref}
would give $f=0$ when $\lambda\ne0$. Both contradict the
requirement that an eigenvector be nonzero.
:::

:::

::: pf-qed
Step [](#no-nonzero-eigenvectors){.pf-ref} is the required conclusion.
:::

:::

:::
