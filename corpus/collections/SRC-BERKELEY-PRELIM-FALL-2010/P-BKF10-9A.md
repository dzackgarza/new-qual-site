---
schema: qual/card@1
id: P-BKF10-9A
kind: problem
title: Nonuniqueness of solutions of $y'=y^{2/3}$, $y(0)=1$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 9A of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked both global solutions, including differentiability of the
    piecewise solution at x=-3 and the real interpretation of y^(2/3).
---

::: {.problem}
Show that there is more than one real-valued differentiable function $y$ with domain $\RR$ such that
$$
\frac{dy}{dx}=y^{2/3},\qquad y(0)=1.
$$
:::

::: {.solution}
For a real number $u$, interpret $u^{2/3}$ as
$$
u^{2/3}=(\sqrt[3]{u})^2.
$$

::: pf

::: {.pf-step #s1}

The function
$$
y_1(x)\coloneqq\left(\frac{x+3}{3}\right)^3
$$
is a differentiable solution on all of $\RR$ with $y_1(0)=1$.

::: pf-proof

Differentiating gives
$$
y_1'(x)=\frac{(x+3)^2}{9}.
$$
Since the real cube root of $y_1(x)$ is $(x+3)/3$,
$$
y_1(x)^{2/3}=\left(\frac{x+3}{3}\right)^2
=\frac{(x+3)^2}{9}=y_1'(x).
$$
Also
$$
y_1(0)=\left(\frac33\right)^3=1.
$$

:::

:::

::: {.pf-step #s2}

Define a second function by
$$
y_2(x)\coloneqq
\begin{cases}
0,&x\le-3,\\[3pt]
\left(\dfrac{x+3}{3}\right)^3,&x\ge-3.
\end{cases}
$$
Then $y_2$ is differentiable at $x=-3$ and $y_2'(-3)=0$.

::: pf-proof

Both pieces have value $0$ at $x=-3$, so $y_2$ is continuous there.
Moreover,
$$
\frac{y_2(-3+h)-y_2(-3)}{h}
=
\begin{cases}
0,&h<0,\\[3pt]
\dfrac{h^2}{27},&h>0.
\end{cases}
$$
Both one-sided expressions tend to $0$ as $h\to0$. Hence the derivative
exists at $-3$ and equals $0$.

:::

:::

::: {.pf-step #s3}

The function $y_2$ satisfies
$$
y_2'=y_2^{2/3}
$$
on all of $\RR$ and satisfies $y_2(0)=1$.

::: pf-proof

For $x<-3$, one has $y_2(x)=0$, so
$$
y_2'(x)=0=y_2(x)^{2/3}.
$$
For $x>-3$, the function agrees with $y_1$, so the differential equation
holds by step [](#s1){.pf-ref}. At $x=-3$, step [](#s2){.pf-ref} gives
$$
y_2'(-3)=0=y_2(-3)^{2/3}.
$$
Finally, since $0>-3$,
$$
y_2(0)=\left(\frac33\right)^3=1.
$$

:::

:::

::: {.pf-step #s4}

The two solutions are distinct.

::: pf-proof

For example,
$$
y_1(-4)=-\frac1{27},
\qquad
y_2(-4)=0.
$$
Thus $y_1\ne y_2$.

:::

:::

::: {.pf-step #s5}

Therefore there is more than one real-valued differentiable
solution of the initial-value problem.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s3){.pf-ref} give two global differentiable solutions with the
same initial value, and step [](#s4){.pf-ref} shows that they are different.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is exactly the required conclusion.

:::

:::

:::
