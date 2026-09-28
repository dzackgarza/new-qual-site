---
schema: qual/card@1
id: P-BERK92S-16
kind: problem
title: Limit of the iteration $x_{n+1}=(3+2x_n)/(3+x_n)$
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let
\[
x_0=1,
\qquad
x_{n+1}=\frac{3+2x_n}{3+x_n}
\quad(n\ge0).
\]
Prove that
\[
x_\infty=\lim_{n\to\infty}x_n
\]
exists, and find its value.
:::

::: {.solution}
Put
$$
T(x)\coloneqq\frac{3+2x}{3+x},
\qquad
\alpha\coloneqq\frac{\sqrt{13}-1}{2}.
$$
Then $\alpha>1$ and $T(\alpha)=\alpha$.

<1>1. The interval $[1,\alpha]$ is invariant under $T$.

::: {.proof}
For $x>-3$,
$$
T'(x)=\frac3{(3+x)^2}>0,
$$
so $T$ is increasing there. Hence for $1\le x\le\alpha$,
$$
T(1)\le T(x)\le T(\alpha)=\alpha.
$$
Since $T(1)=5/4>1$, this gives
$T(x)\in[1,\alpha]$.
:::

<1>2. The sequence $(x_n)$ is increasing and bounded above by
$\alpha$.

::: {.proof}
By step <1>1 and $x_0=1$, induction gives
$x_n\in[1,\alpha]$ for every $n$. Moreover,
$$
T(x)-x
=\frac{3-x-x^2}{3+x}
=-\frac{(x-\alpha)(x-\beta)}{3+x},
$$
where
$$
\beta\coloneqq\frac{-1-\sqrt{13}}2<0.
$$
For $1\le x<\alpha$, the last expression is positive. Thus
$x_{n+1}\ge x_n$ for all $n$, with equality only if
$x_n=\alpha$. Therefore $(x_n)$ is increasing and bounded above by
$\alpha$.
:::

<1>3. The limit exists and equals
$$
\boxed{\frac{\sqrt{13}-1}{2}}.
$$

::: {.proof}
By step <1>2, monotone convergence gives a limit
$\ell\in[1,\alpha]$. Passing to the limit in
$x_{n+1}=T(x_n)$ gives
$$
\ell=\frac{3+2\ell}{3+\ell},
$$
so
$$
\ell^2+\ell-3=0.
$$
The two roots are $\alpha$ and $\beta$. Since
$\ell\in[1,\alpha]$, necessarily $\ell=\alpha$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 proves existence and computes the limit.
:::
:::
