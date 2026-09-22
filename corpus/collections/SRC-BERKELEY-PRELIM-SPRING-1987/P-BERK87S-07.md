---
schema: qual/card@1
id: P-BERK87S-07
kind: problem
title: Put a second-order linear ODE into self-adjoint form
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
    Used the positive integrating factor
    a(t)=exp(integral_0^t q(s)/p(s) ds). Since a'/a=q/p, multiplying the
    original equation by a/p turns the x'' and x' terms into (a x')';
    b=ar/p is continuous.
---

::: {.problem}
Let $p,q,r$ be continuous real-valued functions on $\mathbb R$ with $p>0$. Prove that
\[
p(t)x''(t)+q(t)x'(t)+r(t)x(t)=0
\]
has exactly the same solutions as an equation of the form
\[
(a(t)x'(t))'+b(t)x(t)=0,
\]
where $a$ is continuously differentiable and $b$ is continuous.
:::

::: {.solution}
<1>1. The function
$$
c(t)\coloneqq\frac{q(t)}{p(t)}
$$
is continuous on $\RR$.

::: {.proof}
Both $p$ and $q$ are continuous, and the hypothesis
$$
p(t)>0
$$
for every $t$ implies that the denominator never vanishes.
:::

<1>2. Define
$$
a(t)
\coloneqq
\exp\left(
\int_0^t c(s)\,ds
\right).
$$
Then $a$ is continuously differentiable, strictly positive, and satisfies
$$
a'(t)=a(t)\frac{q(t)}{p(t)}.
$$

::: {.proof}
By step <1>1, the fundamental theorem of calculus gives
$$
\frac{d}{dt}
\int_0^t c(s)\,ds
=
c(t).
$$
The chain rule therefore yields
$$
a'(t)
=
a(t)c(t)
=
a(t)\frac{q(t)}{p(t)}.
$$
Continuity of $c$ also gives $a\in C^1(\RR)$, and an exponential is
strictly positive.
:::

<1>3. Define
$$
b(t)\coloneqq a(t)\frac{r(t)}{p(t)}.
$$
Then $b$ is continuous.

::: {.proof}
The functions $a$ and $r$ are continuous, while $p$ is continuous and
nowhere zero. Hence their displayed product and quotient is continuous.
:::

<1>4. For every twice differentiable function $x$,
$$
(a(t)x'(t))'+b(t)x(t)
=
\frac{a(t)}{p(t)}
\left(
p(t)x''(t)+q(t)x'(t)+r(t)x(t)
\right).
$$

::: {.proof}
By the product rule and step <1>2,
$$
\begin{aligned}
(ax')'+bx
&=
ax''+a'x'+bx\\
&=
ax''
+
a\frac{q}{p}x'
+
a\frac{r}{p}x\\
&=
\frac ap
\left(
px''+qx'+rx
\right).
\end{aligned}
$$
:::

<1>5. The two differential equations have exactly the same solutions.

::: {.proof}
By step <1>2 and the hypothesis $p>0$,
$$
\frac{a(t)}{p(t)}>0
$$
for every $t$. Thus the right-hand side in step <1>4 vanishes at every
$t$ if and only if
$$
p(t)x''(t)+q(t)x'(t)+r(t)x(t)=0
$$
at every $t$. Therefore
$$
\boxed{
(a(t)x'(t))'+b(t)x(t)=0
}
$$
has exactly the same solution set as the original equation.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>2 and <1>3 give the required regularity of $a$ and $b$, and
step <1>5 proves equivalence of the equations.
:::
:::
