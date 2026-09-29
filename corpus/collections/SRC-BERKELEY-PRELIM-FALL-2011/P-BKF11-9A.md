---
schema: qual/card@1
id: P-BKF11-9A
kind: problem
title: Power series coefficients of the Bessel function $J_1$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 9A of the retained Berkeley Fall 2011 preliminary-exam solution packet f11solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the coefficient recurrence, the exceptional n=0 and n=1
    equations, and the closed factorial form for the odd coefficients.
---

::: {.problem}
The Bessel function
$$
J_1(x)=a_0+a_1x+a_2x^2+\cdots
$$
satisfies
$$
x^2\frac{d^2J_1}{dx^2}+x\frac{dJ_1}{dx}+(x^2-1)J_1=0
$$
and has derivative $1$ at $0$.
Find the coefficients $a_n$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Comparing coefficients in the differential equation gives
$$
-a_0=0
$$
for $n=0$, no condition for $n=1$, and
$$
(n^2-1)a_n+a_{n-2}=0
$$
for every $n\ge2$.

::: pf-proof

From
$$
J_1(x)=\sum_{n=0}^{\infty}a_nx^n
$$
one obtains
$$
x^2J_1''+xJ_1'-J_1
=\sum_{n=0}^{\infty}(n^2-1)a_nx^n
$$
and
$$
x^2J_1
=\sum_{n=2}^{\infty}a_{n-2}x^n.
$$
Therefore the coefficient of $x^0$ is $-a_0$, the coefficient of
$x^1$ is
$$
(1^2-1)a_1=0,
$$
and for $n\ge2$ the coefficient of $x^n$ is
$$
(n^2-1)a_n+a_{n-2}.
$$
Each coefficient must vanish, proving the claim.

:::

:::

::: {.pf-step #s2}

The initial coefficients are
$$
a_0=0,
\qquad
a_1=1,
$$
and for $n\ge2$,
$$
a_n=-\frac{a_{n-2}}{(n-1)(n+1)}.
$$

::: pf-proof

Step [](#s1){.pf-ref} gives $a_0=0$. Since
$$
J_1'(x)=\sum_{n=1}^{\infty}na_nx^{n-1},
$$
the condition $J_1'(0)=1$ gives $a_1=1$. For $n\ge2$, solve the
recurrence in step [](#s1){.pf-ref} for $a_n$, using
$$
n^2-1=(n-1)(n+1).
$$

:::

:::

::: {.pf-step #s3}

Every even coefficient vanishes:
$$
a_{2m}=0
\qquad(m\ge0).
$$

::: pf-proof

The initial even coefficient is $a_0=0$. If $a_{2m}=0$, then the
recurrence in step [](#s2){.pf-ref} gives
$$
a_{2m+2}
=-\frac{a_{2m}}{(2m+1)(2m+3)}
=0.
$$
Induction proves the claim.

:::

:::

::: {.pf-step #s4}

For every $m\ge0$,
$$
a_{2m+1}
=\frac{(-1)^m}{4^m m!(m+1)!}.
$$

::: pf-proof

The formula gives $a_1=1$ when $m=0$. For $m\ge1$, repeated use of
step [](#s2){.pf-ref} yields
$$
\begin{aligned}
a_{2m+1}
&=(-1)^m a_1
  \prod_{k=1}^m\frac1{(2k)(2k+2)}\\
&=\frac{(-1)^m}
        {4^m\left(\prod_{k=1}^m k\right)
              \left(\prod_{k=1}^m(k+1)\right)}\\
&=\frac{(-1)^m}{4^m m!(m+1)!}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s5}

Hence the coefficients are
$$
\boxed{
a_n=
\begin{cases}
0,&n=2m,\\[2mm]
\displaystyle\frac{(-1)^m}{4^m m!(m+1)!},&n=2m+1,
\end{cases}
\qquad m\ge0
}.
$$

::: pf-proof

Step [](#s3){.pf-ref} gives all even coefficients and step [](#s4){.pf-ref} gives all odd
coefficients.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} gives every requested coefficient.

:::

:::

:::
