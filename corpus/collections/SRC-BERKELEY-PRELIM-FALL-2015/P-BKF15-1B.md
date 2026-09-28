---
schema: qual/card@1
id: P-BKF15-1B
kind: problem
title: Solutions of the Euler equation $y''=ay/x^2$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Statement checked against F15_Exam.pdf problem 1B; restored the derivative prime and put all mathematics in math mode.
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2015 solution packet: the
    indicial equation is lambda(lambda-1)=a, with the repeated-root and
    complex-root cases giving the logarithmic and trigonometric bases.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the logarithmic change of variables, all three parameter cases,
    linear independence of the displayed bases, and the initial conditions
    when a=-1/4.
---

::: {.problem}
For $a$ real, find a $2$-dimensional space of real-valued solutions of $y'' = ay/x^2$ for $x > 0$.
When $a = -1/4$, find the solution with $y = 0$, $y' = 1$ at $x = 1$.
:::

::: {.solution}
Put
$$
t\coloneqq\log x,
\qquad
y(x)\coloneqq x^{1/2}u(t).
$$

<1>1. Under this substitution,
$$
y''=\frac{ay}{x^2}
$$
is equivalent to
$$
u''=(a+\tfrac14)u.
$$

::: {.proof}
Since $dt/dx=1/x$,
$$
y'
=
x^{-1/2}
\left(
\frac12u+u'
\right),
$$
where primes on $u$ denote derivatives with respect to $t$. Differentiating
once more,
$$
y''
=
x^{-3/2}
\left(
u''-\frac14u
\right).
$$
Also
$$
\frac{ay}{x^2}
=
ax^{-3/2}u.
$$
Cancelling $x^{-3/2}$ gives
$$
u''-\frac14u=au,
$$
which is the stated equation.
:::

<1>2. If
$$
a>-\frac14,
$$
put
$$
\mu\coloneqq\sqrt{a+\frac14}>0.
$$
Then the real solution space is
$$
\boxed{
\operatorname{span}_{\RR}
\left\{
x^{1/2+\mu},
x^{1/2-\mu}
\right\}.
}
$$

::: {.proof}
By step <1>1,
$$
u''=\mu^2u.
$$
The two independent solutions are
$$
e^{\mu t},
\qquad
e^{-\mu t}.
$$
Since $t=\log x$,
$$
x^{1/2}e^{\pm\mu t}
=
x^{1/2\pm\mu}.
$$
Their Wronskian is
$$
\begin{aligned}
W
&=
x^{1/2+\mu}
\left(\frac12-\mu\right)x^{-1/2-\mu}
-
\left(\frac12+\mu\right)x^{-1/2+\mu}
x^{1/2-\mu}\\
&=
-2\mu\ne0.
\end{aligned}
$$
Thus they are linearly independent and form a basis of the
$2$-dimensional solution space.
:::

<1>3. If
$$
a=-\frac14,
$$
the real solution space is
$$
\boxed{
\operatorname{span}_{\RR}
\left\{
x^{1/2},
x^{1/2}\log x
\right\}.
}
$$

::: {.proof}
By step <1>1, the transformed equation is
$$
u''=0,
$$
whose solution space is
$$
u(t)=c_1+c_2t.
$$
Substituting $t=\log x$ gives the displayed basis. Its Wronskian is
$$
W
\left(
x^{1/2},
x^{1/2}\log x
\right)
=
1,
$$
so the two solutions are linearly independent.
:::

<1>4. If
$$
a<-\frac14,
$$
put
$$
\tau\coloneqq\sqrt{-\frac14-a}>0.
$$
Then the real solution space is
$$
\boxed{
\operatorname{span}_{\RR}
\left\{
x^{1/2}\cos(\tau\log x),
x^{1/2}\sin(\tau\log x)
\right\}.
}
$$

::: {.proof}
Step <1>1 gives
$$
u''=-\tau^2u.
$$
Its real solution space has basis
$$
\cos(\tau t),
\qquad
\sin(\tau t).
$$
Multiplication by $x^{1/2}$ and substitution $t=\log x$ give the
displayed functions. Their Wronskian is
$$
\tau\ne0,
$$
so they are linearly independent.
:::

<1>5. When $a=-1/4$, the unique solution satisfying
$$
y(1)=0,
\qquad
y'(1)=1
$$
is
$$
\boxed{y(x)=x^{1/2}\log x}.
$$

::: {.proof}
By step <1>3, every solution has the form
$$
y(x)
=
c_1x^{1/2}
+
c_2x^{1/2}\log x.
$$
At $x=1$,
$$
y(1)=c_1,
$$
so the first initial condition gives $c_1=0$.

Moreover,
$$
\frac{d}{dx}
\left(
x^{1/2}\log x
\right)
=
x^{-1/2}
\left(
1+\frac12\log x
\right),
$$
whose value at $x=1$ is $1$. Therefore the condition $y'(1)=1$
forces $c_2=1$.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>2--<1>4 give the real solution space for every real $a$, and
step <1>5 gives the requested solution in the repeated-root case.
:::
:::
