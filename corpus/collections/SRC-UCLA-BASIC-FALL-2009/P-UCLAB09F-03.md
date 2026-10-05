---
schema: qual/card@1
id: P-UCLAB09F-03
kind: problem
title: A multivariable-calculus proof of the arithmetic-geometric mean inequality
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
  note: Checked against Problem 3 of the retained UCLA Basic Examination, Fall 2009.
---

::: {.problem}
Let
\[
f(x_1,\ldots,x_n)=x_1+\cdots+x_n+\frac1{x_1x_2\cdots x_n}
\]
on the positive orthant $\mathbb R_+^n$.

<1>1. Explain carefully why $f$ attains a global minimum at some $p\in\mathbb R_+^n$.
(Consider what happens as some $x_i\to0$ or $x_i\to\infty$.)

<1>2. Find $p$.

<1>3. Deduce that if $x_1,\ldots,x_n>0$ and $\prod_i x_i=1$, then
\[
\sum_i x_i\ge n,
\]
with equality if and only if $x_i=1$ for every $i$.
:::

::: {.solution}
Let
\[
P(x_1,\ldots,x_n)=x_1x_2\cdots x_n.
\]

<1>1. The sublevel set
\[
K=
\left\{
x\in\mathbb R_+^n:
f(x)\le n+1
\right\}
\]
is nonempty and compact.

::: {.proof}
The point
\[
\mathbf1=(1,\ldots,1)
\]
belongs to $K$ because
\[
f(\mathbf1)=n+1.
\]
Thus $K$ is nonempty.

If $x\in K$, then every coordinate is positive and
\[
x_i\le
x_1+\cdots+x_n
\le
f(x)
\le
n+1.
\]
Also
\[
\frac1{P(x)}
\le
n+1,
\]
so
\[
P(x)\ge\frac1{n+1}.
\]
Since every coordinate other than $x_i$ is at most $n+1$,
\[
P(x)
=
x_i\prod_{j\ne i}x_j
\le
x_i(n+1)^{n-1}.
\]
Therefore
\[
x_i\ge\frac1{(n+1)^n}.
\]
Hence
\[
K\subseteq
\left[
\frac1{(n+1)^n},\,n+1
\right]^n.
\]
On this closed box, $f$ is continuous. Thus
\[
K=f^{-1}((-\infty,n+1])
\]
relative to the box is closed. Hence $K$ is a closed subset of a compact box, so it is compact.
:::

<1>2. The function $f$ attains a global minimum at some point
\[
p\in\mathbb R_+^n.
\]

::: {.proof}
By step <1>1, the continuous function $f$ attains a minimum on the compact nonempty set $K$.
Outside $K$ one has
\[
f(x)>n+1=f(\mathbf1).
\]
Since $\mathbf1\in K$, no point outside $K$ can have smaller value than the minimum on $K$. Therefore the minimum on $K$ is the global minimum on $\mathbb R_+^n$.
:::

<1>3. At every global minimizer $p=(p_1,\ldots,p_n)$,
\[
\frac{\partial f}{\partial x_i}(p)=0
\]
for each $i$.

::: {.proof}
The positive orthant $\mathbb R_+^n$ is open. Hence a global minimizer $p$ is an interior point of the domain. Since $f$ is differentiable, the gradient must vanish at an interior local minimum.
:::

<1>4. For each $i$,
\[
\frac{\partial f}{\partial x_i}(x)
=
1-\frac1{x_iP(x)}.
\]

::: {.proof}
The derivative of the linear term $x_i$ is $1$. Since
\[
\frac1{P(x)}
=
\frac1{x_i}
\prod_{j\ne i}\frac1{x_j},
\]
differentiating with respect to $x_i$ gives
\[
-\frac1{x_i^2}
\prod_{j\ne i}\frac1{x_j}
=
-\frac1{x_iP(x)}.
\]
Adding the two contributions yields the formula.
:::

<1>5. Every critical point of $f$ in $\mathbb R_+^n$ equals
\[
\boxed{(1,\ldots,1)}.
\]

::: {.proof}
At a critical point, step <1>4 gives
\[
x_iP(x)=1
\]
for every $i$. Hence
\[
x_1=x_2=\cdots=x_n=:c.
\]
Then
\[
P(x)=c^n,
\]
and the equation $x_iP(x)=1$ becomes
\[
c^{n+1}=1.
\]
Since $c>0$,
\[
c=1.
\]
Thus the only critical point is $\mathbf1=(1,\ldots,1)$.
:::

<1>6. The global minimizer is
\[
\boxed{p=(1,\ldots,1)}
\]
and the minimum value is
\[
\boxed{f(p)=n+1}.
\]

::: {.proof}
By steps <1>2--<1>3, every global minimizer is a critical point. Step <1>5 shows that the only critical point is $\mathbf1$. Therefore it is the unique global minimizer. Direct substitution gives
\[
f(\mathbf1)=n+\frac1{1}=n+1.
\]
:::

<1>7. If $x_1,\ldots,x_n>0$ and
\[
\prod_{i=1}^n x_i=1,
\]
then
\[
\boxed{\sum_{i=1}^n x_i\ge n}.
\]

::: {.proof}
Under the product condition,
\[
f(x_1,\ldots,x_n)
=
\sum_{i=1}^n x_i+1.
\]
By step <1>6,
\[
f(x)\ge n+1.
\]
Therefore
\[
\sum_{i=1}^n x_i+1\ge n+1,
\]
which gives the stated inequality.
:::

<1>8. Equality in step <1>7 holds if and only if
\[
x_1=\cdots=x_n=1.
\]

::: {.proof}
Equality
\[
\sum_i x_i=n
\]
under the product condition is equivalent to
\[
f(x)=n+1.
\]
By step <1>6, the global minimum $n+1$ is attained only at
\[
\mathbf1=(1,\ldots,1).
\]
Conversely, at $\mathbf1$ the product is $1$ and the sum is $n$.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 prove existence of a global minimizer, steps <1>3--<1>6 identify it, and steps <1>7--<1>8 prove the stated arithmetic-geometric mean inequality and its equality condition.
:::
:::
