---
schema: qual/card@1
id: P-BERK81S-20
kind: problem
title: Evenness and zeros of the solution of $y''=-|y|$
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
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Rewrote the equation as the first-order system
    (y,v)'=(v,-|y|), whose vector field is globally Lipschitz, so the IVP is
    unique. Reflection x↦-x preserves the equation and initial data, proving
    evenness. On the positive axis the explicit C^2 solution is cos x up to
    pi/2 and -sinh(x-pi/2) thereafter; uniqueness identifies it with y, so
    pi/2 is the unique positive zero.
---

::: {.problem}
Let $y:\mathbb R\to\mathbb R$ solve
\[
y''=-|y|,
\qquad
y(0)=1,
\qquad
y'(0)=0.
\]

1. Show that $y$ is even.

2. Show that $y$ has exactly one zero on the positive real axis.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The initial-value problem
$$
y''=-\abs{y},
\qquad
y(0)=1,
\qquad
y'(0)=0
$$
has at most one solution.

::: pf-proof

Introduce
$$
v=y'
$$
and rewrite the equation as the first-order system
$$
\begin{pmatrix}
y\\
v
\end{pmatrix}'
=
\begin{pmatrix}
v\\
-\abs{y}
\end{pmatrix}.
$$
The vector field
$$
F(y,v)
=
(v,-\abs{y})
$$
is globally Lipschitz because
$$
\abs{\abs{y_1}-\abs{y_2}}
\leq
\abs{y_1-y_2}.
$$
The uniqueness theorem for ordinary differential equations therefore gives
uniqueness for the stated initial data.

:::

:::

::: {.pf-step #s2}

Define
$$
\widetilde y(x)=y(-x).
$$
Then $\widetilde y$ satisfies the same differential equation and initial
conditions as $y$.

::: pf-proof

Differentiating twice,
$$
\widetilde y''(x)
=
y''(-x)
=
-\abs{y(-x)}
=
-\abs{\widetilde y(x)}.
$$
Moreover,
$$
\widetilde y(0)=y(0)=1
$$
and
$$
\widetilde y'(0)=-y'(0)=0.
$$

:::

:::

::: {.pf-step #s3}

The function $y$ is even:
$$
\boxed{
y(-x)=y(x)
}
$$
for every $x\in\RR$.

::: pf-proof

By step [](#s2){.pf-ref}, the functions $y$ and $\widetilde y$ solve the same
initial-value problem. Uniqueness from step [](#s1){.pf-ref} gives
$$
\widetilde y=y.
$$
This is exactly the displayed identity.

:::

:::

::: {.pf-step #s4}

Define $\phi:[0,\infty)\to\RR$ by
$$
\phi(x)
=
\begin{cases}
\cos x,
&
0\leq x\leq\pi/2,
\\
-\sinh(x-\pi/2),
&
x\geq\pi/2.
\end{cases}
$$
Then $\phi$ is $C^2$ on $[0,\infty)$.

::: pf-proof

Each branch is smooth away from $x=\pi/2$. At the joining point,
$$
\cos(\pi/2)=0
=
-\sinh0,
$$
so the values agree. The first derivatives are
$$
-\sin x
$$
and
$$
-\cosh(x-\pi/2),
$$
and both equal $-1$ at $x=\pi/2$. The second derivatives are
$$
-\cos x
$$
and
$$
-\sinh(x-\pi/2),
$$
and both equal $0$ there. Hence the two branches join with matching first
and second derivatives.

:::

:::

::: {.pf-step #s5}

The function $\phi$ satisfies
$$
\phi''=-\abs{\phi}
$$
on $[0,\infty)$ and
$$
\phi(0)=1,
\qquad
\phi'(0)=0.
$$

::: pf-proof

For
$$
0\leq x\leq\pi/2,
$$
one has $\cos x\geq0$, so
$$
\phi''(x)
=
-\cos x
=
-\abs{\phi(x)}.
$$

For $x\geq\pi/2$,
$$
\phi(x)=-\sinh(x-\pi/2)\leq0.
$$
Thus
$$
\abs{\phi(x)}
=
\sinh(x-\pi/2),
$$
while
$$
\phi''(x)
=
-\sinh(x-\pi/2)
=
-\abs{\phi(x)}.
$$
Step [](#s4){.pf-ref} handles the joining point. Finally,
$$
\phi(0)=\cos0=1
$$
and
$$
\phi'(0)=-\sin0=0.
$$

:::

:::

::: {.pf-step #s6}

For every $x\geq0$,
$$
y(x)=\phi(x).
$$

::: pf-proof

The functions $y$ and $\phi$ satisfy the same differential equation and
the same initial conditions at $0$ by step [](#s5){.pf-ref}. Uniqueness from step
[](#s1){.pf-ref} therefore gives equality on their common interval
$$
[0,\infty).
$$

:::

:::

::: {.pf-step #s7}

The function $y$ has exactly one zero on the positive real axis,
namely
$$
\boxed{
x=\frac\pi2.
}
$$

::: pf-proof

By step [](#s6){.pf-ref},
$$
y(x)=\cos x
$$
for $0\leq x\leq\pi/2$. Hence
$$
y(x)>0
$$
for $0\leq x<\pi/2$, while
$$
y(\pi/2)=0.
$$
For $x>\pi/2$, step [](#s6){.pf-ref} gives
$$
y(x)
=
-\sinh(x-\pi/2)
<
0.
$$
Thus there is no other positive zero.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves part (1), and step [](#s7){.pf-ref} proves part (2).

:::

:::

:::
