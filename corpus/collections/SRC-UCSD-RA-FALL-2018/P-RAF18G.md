---
schema: qual/card@1
id: P-RAF18G
kind: problem
title: "Derivative of an integral involving min(x,y)"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 7 of the official UCSD Fall 2018 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $g \in L^1([0,1], m)$ and $h : [0,1] \to \mathbb{R}$ be a continuous function.

1. If $f : [0,1] \to \mathbb{R}$ is absolutely continuous and satisfies $f'(x) = h(x)$ for a.e. $x$, show $f'(x) = h(x)$ for all $x \in (0,1)$.

2. Now suppose that
$$
f(x) := \int_0^1 \min(x,y)\,g(y)\,dy.
$$
Show $f'(x) = \int_x^1 g(y)\,dy$ for all $x \in (0,1)$.
:::

::: solution
<1>1. Upgrade the a.e. derivative identity to an everywhere identity.
::: proof
Since $f$ is absolutely continuous,
\[
f(x)=f(0)+\int_0^x f'(t)\,dt
\]
for every $x\in[0,1]$. Because $f'=h$ almost everywhere,
\[
f(x)=f(0)+\int_0^x h(t)\,dt.
\]
The function $h$ is continuous, so the ordinary Fundamental Theorem of Calculus gives
\[
\frac{d}{dx}\int_0^x h(t)\,dt=h(x)
\]
for every $x\in(0,1)$. Hence
\[
\boxed{f'(x)=h(x)\quad\text{for every }x\in(0,1).}
\]
:::

<1>2. Rewrite the integral involving $\min(x,y)$.
::: proof
For $x\in[0,1]$,
\[
\min(x,y)=
\begin{cases}
y,&0\le y\le x,\\
x,&x<y\le1.
\end{cases}
\]
Therefore
\[
f(x)=\int_0^x y g(y)\,dy+x\int_x^1 g(y)\,dy.
\]
Both terms are absolutely continuous functions of $x$ because $g\in L^1([0,1])$. Differentiating almost everywhere gives
\[
\begin{aligned}
f'(x)
&=xg(x)+\int_x^1g(y)\,dy-xg(x)\\
&=\int_x^1g(y)\,dy
\end{aligned}
\]
for almost every $x$.
:::

<1>3. Upgrade the formula to every interior point.
::: proof
Define
\[
h(x):=\int_x^1g(y)\,dy.
\]
Since $g\in L^1([0,1])$, the function $h$ is absolutely continuous, hence continuous, on $[0,1]$. Step 2 shows that $f$ is absolutely continuous and $f'=h$ almost everywhere. Applying part 1 gives
\[
\boxed{f'(x)=\int_x^1g(y)\,dy\quad\text{for every }x\in(0,1).}
\]
:::
:::
