---
schema: qual/card@1
id: P-S07TY
kind: problem
title: Taylor series of $\ln(2+x)$ about the origin
classification:
  areas:
  - prelim
  topics:
  - Power Series
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
a) Find the Taylor expansion of $f(x) = \ln(2 + x)$ about the origin.

b) Find the radius of convergence $R$ of that series.

c) Use Taylor's theorem to show that the series converges to $f(x)$ on $[0, R/2]$.
:::


::: {.solution}
<1>1. For $|x|<2$,
\[
\ln(2+x)
=\ln 2+\ln\left(1+\frac x2\right)
=\ln2+\sum_{n=1}^\infty (-1)^{n+1}\frac{x^n}{n2^n}.
\]
::: {.proof}
The standard expansion
\[
\ln(1+u)=\sum_{n=1}^\infty (-1)^{n+1}\frac{u^n}{n}
\]
holds for $|u|<1$. Substituting $u=x/2$ gives the stated series.
:::

<1>2. The radius of convergence is
\[
\boxed{R=2}.
\]
::: {.proof}
For the coefficient $a_n=(-1)^{n+1}/(n2^n)$,
\[
\lim_{n\to\infty}\left|\frac{a_n}{a_{n+1}}\right|
=\lim_{n\to\infty}2\frac{n+1}{n}=2.
\]
Hence the power series has radius $2$.
:::

<1>3. For every integer $m\ge1$,
\[
f^{(m)}(x)=(-1)^{m-1}\frac{(m-1)!}{(2+x)^m}.
\]
::: {.proof}
This follows by differentiating $f(x)=\ln(2+x)$ repeatedly; the formula is immediate for $m=1$ and is preserved by one further differentiation.
:::

<1>4. Let $T_N(x)$ be the Taylor polynomial of degree $N$ at $0$. For each $x\in[0,1]$, Taylor's theorem gives
\[
|f(x)-T_N(x)|
\le \frac{x^{N+1}}{(N+1)2^{N+1}}
\le \frac1{(N+1)2^{N+1}}.
\]
::: {.proof}
Taylor's theorem with Lagrange remainder gives some $\xi$ between $0$ and $x$ such that
\[
f(x)-T_N(x)=\frac{f^{(N+1)}(\xi)}{(N+1)!}x^{N+1}.
\]
By <1>3,
\[
|f^{(N+1)}(\xi)|=\frac{N!}{(2+\xi)^{N+1}}\le \frac{N!}{2^{N+1}},
\]
because $0\le\xi\le x\le1$. Substitution yields the displayed bound.
:::

<1>5. Therefore the Taylor series converges to $f(x)=\ln(2+x)$ for every $x\in[0,R/2]=[0,1]$.
::: {.proof}
The bound in <1>4 tends to $0$ as $N\to\infty$, so $T_N(x)\to f(x)$ for every $x\in[0,1]$.
:::
:::
