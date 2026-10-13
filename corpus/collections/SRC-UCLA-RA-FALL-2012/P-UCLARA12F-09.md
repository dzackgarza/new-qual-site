---
schema: qual/card@1
id: P-UCLARA12F-09
kind: problem
title: Repeated values accumulating at zero force constancy
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Suppose $f$ is holomorphic in the unit disc $\mathbb D$, and $(x_n)$ is a sequence of real numbers satisfying
\[
0<x_{n+1}<x_n<1
\]
for all $n$ and $x_n\to0$.
Show that if
\[
f(x_{2n+1})=f(x_{2n})
\]
for every $n$, then $f$ is constant.
:::

::: {.solution}
<1>1. Suppose, for contradiction, that $f$ is nonconstant. Then $f'$ is not identically zero, so there are an integer $k\ge0$ and a holomorphic function $h$ near $0$ such that
$$
f'(z)=z^k h(z),
\qquad
h(0)\ne0.
$$

::: {.proof}
Since $f'$ is holomorphic and not identically zero, its zero at $0$ has some finite order $k\ge0$. Factoring out that order gives the displayed representation with $h(0)\ne0$.
:::

<1>2. There are a real number $\theta$ and a number $\delta>0$ such that
$$
\operatorname{Re}\!\left(e^{-i\theta}h(x)\right)>0
$$
for every real $x\in[0,\delta)$.

::: {.proof}
Choose $\theta$ so that
$$
e^{-i\theta}h(0)=|h(0)|>0.
$$
By continuity of $h$, for all sufficiently small real $x\ge0$ the complex number $e^{-i\theta}h(x)$ remains in the open right half-plane. This gives the required $\delta$.
:::

<1>3. The real-valued function
$$
\phi(x)\coloneqq\operatorname{Re}\!\left(e^{-i\theta}f(x)\right)
$$
is strictly increasing on $(0,\delta)$.

::: {.proof}
For $0<x<\delta$, steps <1>1 and <1>2 give
$$
\begin{aligned}
\phi'(x)
&=\operatorname{Re}\!\left(e^{-i\theta}f'(x)\right)\\
&=x^k\operatorname{Re}\!\left(e^{-i\theta}h(x)\right)\\
&>0.
\end{aligned}
$$
Hence $\phi$ is strictly increasing on $(0,\delta)$.
:::

<1>4. For all sufficiently large $n$,
$$
f(x_{2n+1})\ne f(x_{2n}).
$$

::: {.proof}
Because $x_n\to0$, for all sufficiently large $n$ one has
$$
0<x_{2n+1}<x_{2n}<\delta.
$$
By step <1>3,
$$
\phi(x_{2n+1})<\phi(x_{2n}).
$$
If $f(x_{2n+1})=f(x_{2n})$, their rotated real parts would be equal, contradicting this strict inequality.
:::

<1>5. Therefore $f$ is constant.

::: {.proof}
Step <1>4 contradicts the hypothesis
$$
f(x_{2n+1})=f(x_{2n})
$$
for every $n$. Hence the assumption in step <1>1 that $f$ is nonconstant is false.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
