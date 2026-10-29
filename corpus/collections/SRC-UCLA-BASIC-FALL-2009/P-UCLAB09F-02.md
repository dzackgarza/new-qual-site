---
schema: qual/card@1
id: P-UCLAB09F-02
kind: problem
title: Contractions and a fixed point for a prescribed derivative
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Fall 2009.
---
::: {.problem}

::: pf

::: {.pf-step #p1-s1}

Let $(X,d)$ be a complete metric space.
A map $T\colon X\to X$ is a contraction if there is $0<\lambda<1$ such that
$$
d(Tx,Ty)\le \lambda d(x,y)
$$
for all $x,y\in X$.
Prove that every contraction has a fixed point.

:::

::: pf-step

Using step [](#p1-s1){.pf-ref}, show that if $f\colon\RR\to\RR$ is differentiable and

:::

:::

$$
f'(x)=e^{-x^2}-e^{-x^4},
$$
then there exists $\alpha\in\RR$ such that $f(\alpha)=\alpha$.
:::

::: {.solution}

::: pf

::: {.pf-step #p2-s1}

Let $x_0\in X$ and define recursively
$$
x_{n+1}=T(x_n).
$$
Then
$$
d(x_{n+1},x_n)
\le
\lambda^n d(x_1,x_0)
$$
for every $n\ge0$.

::: pf-proof

For $n=0$, the claim is equality. If it holds for $n-1$, then the contraction estimate gives
$$
\begin{aligned}
d(x_{n+1},x_n)
&=
d(Tx_n,Tx_{n-1})\\
&\le
\lambda d(x_n,x_{n-1})\\
&\le
\lambda^n d(x_1,x_0).
\end{aligned}
$$
Thus the estimate follows by induction.

:::

:::

::: {.pf-step #p2-s2}

The sequence $(x_n)$ is Cauchy.

::: pf-proof

For $m>n$, the triangle inequality and step [](#p2-s1){.pf-ref} give
$$
\begin{aligned}
d(x_m,x_n)
&\le
\sum_{j=n}^{m-1}d(x_{j+1},x_j)\\
&\le
d(x_1,x_0)\sum_{j=n}^{m-1}\lambda^j\\
&\le
d(x_1,x_0)\frac{\lambda^n}{1-\lambda}.
\end{aligned}
$$
Since $0<\lambda<1$, the last quantity tends to $0$ as $n\to\infty$.

:::

:::

::: {.pf-step #p2-s3}

There exists $x\in X$ such that
$$
x_n\to x.
$$

::: pf-proof

The space $X$ is complete, and step [](#p2-s2){.pf-ref} shows that $(x_n)$ is Cauchy.

:::

:::

::: {.pf-step #p2-s4}

The limit $x$ is a fixed point of $T$:
$$
\boxed{T(x)=x}.
$$

::: pf-proof

The contraction estimate implies that $T$ is continuous, because
$$
d(Tu,Tv)\le\lambda d(u,v).
$$
Therefore
$$
T(x)
=
T\left(\lim_{n\to\infty}x_n\right)
=
\lim_{n\to\infty}T(x_n)
=
\lim_{n\to\infty}x_{n+1}
=
x.
$$
This proves part step [](#p2-s1){.pf-ref}.

:::

:::

::: {.pf-step #p2-s5}

The function
$$
g(x)=e^{-x^2}-e^{-x^4}
$$
satisfies
$$
|g(x)|<1
$$
for every $x\in\RR$, and
$$
g(x)\to0
$$
as $|x|\to\infty$.

::: pf-proof

For every finite $x$,
$$
0<e^{-x^2}\le1
\qquad\text{and}\qquad
0<e^{-x^4}\le1.
$$
The difference of two numbers in $(0,1]$ has absolute value strictly less than $1$. Also both exponentials tend to $0$ as $|x|\to\infty$, so their difference does as well.

:::

:::

::: {.pf-step #p2-s6}

There exists a constant
$$
0<\lambda<1
$$
such that
$$
|f'(x)|\le\lambda
$$
for every $x\in\RR$.

::: pf-proof

By step [](#p2-s5){.pf-ref}, choose $R>0$ such that
$$
|g(x)|<\frac12
$$
whenever $|x|>R$. On the compact interval $[-R,R]$, the continuous function $|g|$ attains a maximum $M$. Step [](#p2-s5){.pf-ref} gives
$$
M<1.
$$
Set
$$
\lambda=\max\left\{M,\frac12\right\}.
$$
Then $0<\lambda<1$ and
$$
|f'(x)|=|g(x)|\le\lambda
$$
for every $x\in\RR$.

:::

:::

::: {.pf-step #p2-s7}

The map
$$
f:\RR\to\RR
$$
is a contraction.

::: pf-proof

For $x\ne y$, the mean value theorem gives some $\xi$ between $x$ and $y$ such that
$$
f(x)-f(y)=f'(\xi)(x-y).
$$
Using step [](#p2-s6){.pf-ref},
$$
|f(x)-f(y)|
\le
\lambda|x-y|.
$$
The same inequality is trivial when $x=y$.

:::

:::

::: {.pf-step #p2-s8}

There exists $\alpha\in\RR$ such that
$$
\boxed{f(\alpha)=\alpha}.
$$

::: pf-proof

The real line with its usual metric is complete. By step [](#p2-s7){.pf-ref}, $f$ is a contraction. Applying part step [](#p2-s1){.pf-ref}, proved in steps [](#p2-s1){.pf-ref}, [](#p2-s2){.pf-ref}, [](#p2-s3){.pf-ref} and [](#p2-s4){.pf-ref}, gives a fixed point $\alpha$.

:::

:::

::: pf-qed

Steps [](#p2-s1){.pf-ref}, [](#p2-s2){.pf-ref}, [](#p2-s3){.pf-ref} and [](#p2-s4){.pf-ref} prove the contraction fixed-point theorem, and steps [](#p2-s5){.pf-ref}, [](#p2-s6){.pf-ref}, [](#p2-s7){.pf-ref} and [](#p2-s8){.pf-ref} apply it to the prescribed derivative.

:::

:::

:::
