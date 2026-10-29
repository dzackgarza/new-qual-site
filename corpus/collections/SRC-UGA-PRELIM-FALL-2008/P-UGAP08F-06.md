---
schema: qual/card@1
id: P-UGAP08F-06
kind: problem
title: A continuous nonnegative function positive at one point has positive integral
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Suppose $f:[0,1]\to\RR$ is continuous, $f(x)\ge0$ for all $x\in[0,1]$, and
\[
f(1/2)>0.
\]
Prove that
\[
\int_0^1 f(x)\,dx>0.
\]
Give an example showing that the conclusion need not hold when $f$ is not continuous.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

There are constants $c>0$ and $\delta>0$ such that
$$
f(x)\ge c
$$
whenever $x\in[0,1]$ and $|x-1/2|<\delta$.


::: pf-proof

Set
$$
c\coloneqq\frac12 f(1/2)>0.
$$
By continuity of $f$ at $1/2$, there is a $\delta>0$ such that
$$
|x-1/2|<\delta
\quad\Longrightarrow\quad
|f(x)-f(1/2)|<c.
$$
For such $x$,
$$
f(x)>f(1/2)-c=c.
$$
Replacing $\delta$ by $\min(\delta,1/2)$ if necessary keeps the relevant interval inside $[0,1]$.

:::

:::

::: {.pf-step #s1-2}

One has
$$
\boxed{\int_0^1 f(x)\,dx>0}.
$$


::: pf-proof

Using step [](#s1-1){.pf-ref} and the hypothesis $f\ge0$ on $[0,1]$,
$$
\begin{aligned}
\int_0^1 f(x)\,dx
&\ge
\int_{1/2-\delta}^{1/2+\delta}f(x)\,dx\\
&\ge
\int_{1/2-\delta}^{1/2+\delta}c\,dx\\
&=2c\delta>0.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

Continuity is necessary: define
$$
g(x)=
\begin{cases}
1,&x=1/2,\\
0,&x\ne1/2.
\end{cases}
$$
Then $g\ge0$ and $g(1/2)>0$, but
$$
\boxed{\int_0^1 g(x)\,dx=0}.
$$


::: pf-proof

The function $g$ is discontinuous at $1/2$. It differs from the zero function at only one point. Equivalently, for every partition of $[0,1]$ every lower sum is $0$, while upper sums can be made arbitrarily small by placing $1/2$ in an interval of arbitrarily small length. Hence $g$ is Riemann integrable with integral $0$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves the assertion under continuity, and step [](#s1-3){.pf-ref} supplies the requested counterexample without continuity.

:::

:::

:::
