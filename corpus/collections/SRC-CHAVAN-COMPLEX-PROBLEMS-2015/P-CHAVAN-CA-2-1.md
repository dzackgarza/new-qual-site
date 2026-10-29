---
schema: qual/card@1
id: P-CHAVAN-CA-2-1
kind: problem
title: Fundamental theorem of algebra from a minimum-modulus estimate
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $f:\CC\to\CC$ be entire and nowhere zero.
For $r>0$:

1. Show that, with the circle $|z|=r$ traversed counterclockwise,
   \[
   \int_{|z|=r}\frac{dz}{zf(z)}=\frac{2\pi i}{f(0)}.
   \]

2. Show that
   \[
   \left|\int_{|z|=r}\frac{dz}{zf(z)}\right|
   \le \frac{2\pi}{\min_{|z|=r}|f(z)|},
   \]
   and hence
   \[
   \min_{|z|=r}|f(z)|\le |f(0)|.
   \]

Deduce the fundamental theorem of algebra by applying this to a monic polynomial and verifying
\[
|a_0+a_1z+\cdots+a_{n-1}z^{n-1}+z^n|
\ge |z|^n\left(1-\frac{|a_{n-1}|}{|z|}-\cdots-\frac{|a_0|}{|z|^n}\right).
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $r>0$,
$$
\int_{|z|=r}\frac{dz}{zf(z)}=\frac{2\pi i}{f(0)}.
$$


::: pf-proof

Since $f$ is entire and nowhere zero, the reciprocal
$$
g(z)=\frac1{f(z)}
$$
is entire. Applying the Cauchy integral formula to $g$ at the origin on
the positively oriented circle $|z|=r$ gives
$$
\int_{|z|=r}\frac{g(z)}{z}\,dz=2\pi i\,g(0)=\frac{2\pi i}{f(0)}.
$$
This is the required identity.

:::

:::

::: {.pf-step #s1-2}

For every $r>0$,
$$
\left|\int_{|z|=r}\frac{dz}{zf(z)}\right|
\le \frac{2\pi}{\min_{|z|=r}|f(z)|}.
$$


::: pf-proof

Because $f$ has no zeros and the circle $|z|=r$ is compact, the
positive continuous function $|f|$ has a positive minimum there. On
the circle,
$$
\left|\frac1{zf(z)}\right|
=\frac1{r|f(z)|}
\le\frac1{r\min_{|w|=r}|f(w)|}.
$$
The circle has length $2\pi r$, so the $ML$ inequality gives
$$
\left|\int_{|z|=r}\frac{dz}{zf(z)}\right|
\le 2\pi r\cdot\frac1{r\min_{|w|=r}|f(w)|}
=\frac{2\pi}{\min_{|w|=r}|f(w)|}.
$$

:::

:::

::: {.pf-step #s1-3}

For every $r>0$,
$$
\min_{|z|=r}|f(z)|\le |f(0)|.
$$


::: pf-proof

Taking absolute values in step [](#s1-1){.pf-ref} and combining with step [](#s1-2){.pf-ref} gives
$$
\frac{2\pi}{|f(0)|}
\le
\frac{2\pi}{\min_{|z|=r}|f(z)|}.
$$
Both denominators are positive, so this inequality is equivalent to
$$
\min_{|z|=r}|f(z)|\le |f(0)|.
$$

:::

:::

::: {.pf-step #s1-4}

If
$$
p(z)=a_0+a_1z+\cdots+a_{n-1}z^{n-1}+z^n
$$
is monic of degree $n\ge1$, then for every $z\ne0$,
$$
|p(z)|
\ge |z|^n\left(1-\frac{|a_{n-1}|}{|z|}-\cdots-\frac{|a_0|}{|z|^n}\right).
$$


::: pf-proof

By the reverse triangle inequality and then the triangle inequality,
$$
\begin{aligned}
|p(z)|
&=\left|z^n+\sum_{k=0}^{n-1}a_kz^k\right|\\
&\ge |z|^n-\left|\sum_{k=0}^{n-1}a_kz^k\right|\\
&\ge |z|^n-\sum_{k=0}^{n-1}|a_k||z|^k.
\end{aligned}
$$
Factoring $|z|^n$ gives exactly the displayed estimate.

:::

:::

::: {.pf-step #s1-5}

Every nonconstant complex polynomial has a zero.


::: pf-proof

It is enough to treat a monic polynomial, since dividing a nonzero
polynomial by its leading coefficient does not change its zeros. Let
$p$ be monic of degree $n\ge1$ and suppose for contradiction that $p$
has no zero in $\CC$. Then step [](#s1-3){.pf-ref}, applied to $f=p$, gives
$$
\min_{|z|=r}|p(z)|\le |p(0)|=|a_0|
$$
for every $r>0$.

On the other hand, step [](#s1-4){.pf-ref} implies for $|z|=r$ that
$$
|p(z)|
\ge r^n\left(1-\frac{|a_{n-1}|}{r}-\cdots-\frac{|a_0|}{r^n}\right).
$$
The expression in parentheses tends to $1$ as $r\to\infty$. Hence for
all sufficiently large $r$ it is at least $1/2$, and then
$$
\min_{|z|=r}|p(z)|\ge\frac{r^n}{2}.
$$
For sufficiently large $r$, this lower bound is greater than $|a_0|$,
contradicting the preceding upper bound. Therefore $p$ has a zero.
This is the fundamental theorem of algebra.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} prove the minimum-modulus estimate, step [](#s1-4){.pf-ref} proves
the requested polynomial inequality, and step [](#s1-5){.pf-ref} deduces the
fundamental theorem of algebra.

:::

:::

:::
