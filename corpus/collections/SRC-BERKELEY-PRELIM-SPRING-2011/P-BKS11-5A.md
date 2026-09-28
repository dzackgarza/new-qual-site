---
schema: qual/card@1
id: P-BKS11-5A
kind: problem
title: Smoothness and Taylor series of $e^{-1/x^2}$
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
  note: Compared the authored statement with page 2 of the retained Spring 2011 solution PDF and independently reviewed its flat-function induction.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the derivative recurrence, polynomial-times-exponential decay, existence and continuity of every derivative at zero, and the resulting zero Taylor series.
---

::: {.problem}
Show that the function equal to $e ^ { - 1 / x ^ { 2 } }$ for $x \neq 0$ and equal to 0 at $x \ = \ 0$ is infinitely differentiable at all real numbers, and find its Taylor series at $x = 0$
:::

::: {.solution}
Write
$$
f(x)
\coloneqq
\begin{cases}
e^{-1/x^2},&x\neq0,\\
0,&x=0.
\end{cases}
$$

<1>1. For every polynomial $P\in\RR[t]$,
$$
\lim_{x\to0}
P(1/x)e^{-1/x^2}
=
0.
$$

::: {.proof}
It is enough to prove the assertion for a monomial $P(t)=t^d$. Put
$$
u\coloneqq\frac1{x^2}.
$$
Then $u\to\infty$ as $x\to0$, and
$$
\abs{x}^{-d}e^{-1/x^2}
=
u^{d/2}e^{-u}.
$$
Choose an integer $m>d/2$. Since
$$
e^u
\geq
\frac{u^m}{m!}
$$
for $u>0$,
$$
0
\leq
u^{d/2}e^{-u}
\leq
m!\,u^{d/2-m}
\longrightarrow0.
$$
A finite linear combination of such monomials has the same limit.
:::

<1>2. For every $n\geq0$, there is a polynomial $P_n\in\RR[t]$ such that
for $x\neq0$,
$$
f^{(n)}(x)
=
P_n(1/x)e^{-1/x^2}.
$$

::: {.proof}
For $n=0$, take
$$
P_0(t)=1.
$$
Assume the formula holds for some $n$. Put $t=1/x$. Then
$$
\frac{dt}{dx}=-t^2
$$
and
$$
\frac{d}{dt}e^{-t^2}=-2te^{-t^2}.
$$
Thus, for $x\neq0$,
$$
\begin{aligned}
f^{(n+1)}(x)
&=
-t^2
\frac{d}{dt}
\left(
P_n(t)e^{-t^2}
\right)\\
&=
\left(
-t^2P_n'(t)+2t^3P_n(t)
\right)e^{-t^2}.
\end{aligned}
$$
Hence one may take
$$
P_{n+1}(t)
\coloneqq
-t^2P_n'(t)+2t^3P_n(t),
$$
which is again a polynomial.
:::

<1>3. For every $n\geq0$,
$$
f^{(n)}(0)=0,
$$
and $f^{(n)}$ is continuous at $0$.

::: {.proof}
Proceed by induction on $n$. For $n=0$, step <1>1 with $P=1$ gives
$$
\lim_{x\to0}f(x)=0=f(0),
$$
so $f$ is continuous at $0$.

Assume $f^{(n)}$ exists everywhere, satisfies
$$
f^{(n)}(0)=0,
$$
and has the form from step <1>2 away from $0$. Then
$$
\begin{aligned}
f^{(n+1)}(0)
&=
\lim_{x\to0}
\frac{f^{(n)}(x)-f^{(n)}(0)}{x}\\
&=
\lim_{x\to0}
\left(
\frac1xP_n(1/x)
\right)e^{-1/x^2}.
\end{aligned}
$$
The expression in parentheses is again a polynomial in $1/x$, so step
<1>1 shows that this limit is $0$. Thus $f^{(n+1)}(0)$ exists and equals
$0$.

For $x\neq0$, step <1>2 gives
$$
f^{(n+1)}(x)
=
P_{n+1}(1/x)e^{-1/x^2},
$$
which tends to $0$ as $x\to0$ by step <1>1. Hence $f^{(n+1)}$ is
continuous at $0$.
:::

<1>4. The function $f$ is infinitely differentiable on $\RR$.

::: {.proof}
Away from $0$, the function $e^{-1/x^2}$ is smooth. Step <1>3 proves
inductively that every derivative extends across $0$ and is continuous
there. Hence
$$
f\in C^\infty(\RR).
$$
:::

<1>5. The Taylor series of $f$ at $0$ is
$$
\boxed{0}.
$$

::: {.proof}
By step <1>3,
$$
f^{(n)}(0)=0
$$
for every $n\geq0$. Therefore the Taylor series is
$$
\sum_{n=0}^{\infty}
\frac{f^{(n)}(0)}{n!}x^n
=
0.
$$
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>4 proves infinite differentiability, and step <1>5 gives the Taylor
series.
:::
:::
