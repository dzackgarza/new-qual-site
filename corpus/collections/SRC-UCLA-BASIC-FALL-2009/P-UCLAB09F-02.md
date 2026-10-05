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
<1>1. Let $(X,d)$ be a complete metric space.
A map $T\colon X\to X$ is a contraction if there is $0<\lambda<1$ such that
\[
d(Tx,Ty)\le \lambda d(x,y)
\]
for all $x,y\in X$.
Prove that every contraction has a fixed point.

<1>2. Using <1>1, show that if $f\colon\mathbb R\to\mathbb R$ is differentiable and
\[
f'(x)=e^{-x^2}-e^{-x^4},
\]
then there exists $\alpha\in\mathbb R$ such that $f(\alpha)=\alpha$.
:::

::: {.solution}
<1>1. Let $x_0\in X$ and define recursively
\[
x_{n+1}=T(x_n).
\]
Then
\[
d(x_{n+1},x_n)
\le
\lambda^n d(x_1,x_0)
\]
for every $n\ge0$.

::: {.proof}
For $n=0$, the claim is equality. If it holds for $n-1$, then the contraction estimate gives
\[
\begin{aligned}
d(x_{n+1},x_n)
&=
d(Tx_n,Tx_{n-1})\\
&\le
\lambda d(x_n,x_{n-1})\\
&\le
\lambda^n d(x_1,x_0).
\end{aligned}
\]
Thus the estimate follows by induction.
:::

<1>2. The sequence $(x_n)$ is Cauchy.

::: {.proof}
For $m>n$, the triangle inequality and step <1>1 give
\[
\begin{aligned}
d(x_m,x_n)
&\le
\sum_{j=n}^{m-1}d(x_{j+1},x_j)\\
&\le
d(x_1,x_0)\sum_{j=n}^{m-1}\lambda^j\\
&\le
d(x_1,x_0)\frac{\lambda^n}{1-\lambda}.
\end{aligned}
\]
Since $0<\lambda<1$, the last quantity tends to $0$ as $n\to\infty$.
:::

<1>3. There exists $x\in X$ such that
\[
x_n\to x.
\]

::: {.proof}
The space $X$ is complete, and step <1>2 shows that $(x_n)$ is Cauchy.
:::

<1>4. The limit $x$ is a fixed point of $T$:
\[
\boxed{T(x)=x}.
\]

::: {.proof}
The contraction estimate implies that $T$ is continuous, because
\[
d(Tu,Tv)\le\lambda d(u,v).
\]
Therefore
\[
T(x)
=
T\left(\lim_{n\to\infty}x_n\right)
=
\lim_{n\to\infty}T(x_n)
=
\lim_{n\to\infty}x_{n+1}
=
x.
\]
This proves part <1>1.
:::

<1>5. The function
\[
g(x)=e^{-x^2}-e^{-x^4}
\]
satisfies
\[
|g(x)|<1
\]
for every $x\in\mathbb R$, and
\[
g(x)\to0
\]
as $|x|\to\infty$.

::: {.proof}
For every finite $x$,
\[
0<e^{-x^2}\le1
\qquad\text{and}\qquad
0<e^{-x^4}\le1.
\]
The difference of two numbers in $(0,1]$ has absolute value strictly less than $1$. Also both exponentials tend to $0$ as $|x|\to\infty$, so their difference does as well.
:::

<1>6. There exists a constant
\[
0<\lambda<1
\]
such that
\[
|f'(x)|\le\lambda
\]
for every $x\in\mathbb R$.

::: {.proof}
By step <1>5, choose $R>0$ such that
\[
|g(x)|<\frac12
\]
whenever $|x|>R$. On the compact interval $[-R,R]$, the continuous function $|g|$ attains a maximum $M$. Step <1>5 gives
\[
M<1.
\]
Set
\[
\lambda=\max\left\{M,\frac12\right\}.
\]
Then $0<\lambda<1$ and
\[
|f'(x)|=|g(x)|\le\lambda
\]
for every $x\in\mathbb R$.
:::

<1>7. The map
\[
f:\mathbb R\to\mathbb R
\]
is a contraction.

::: {.proof}
For $x\ne y$, the mean value theorem gives some $\xi$ between $x$ and $y$ such that
\[
f(x)-f(y)=f'(\xi)(x-y).
\]
Using step <1>6,
\[
|f(x)-f(y)|
\le
\lambda|x-y|.
\]
The same inequality is trivial when $x=y$.
:::

<1>8. There exists $\alpha\in\mathbb R$ such that
\[
\boxed{f(\alpha)=\alpha}.
\]

::: {.proof}
The real line with its usual metric is complete. By step <1>7, $f$ is a contraction. Applying part <1>1, proved in steps <1>1--<1>4, gives a fixed point $\alpha$.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 prove the contraction fixed-point theorem, and steps <1>5--<1>8 apply it to the prescribed derivative.
:::
:::
