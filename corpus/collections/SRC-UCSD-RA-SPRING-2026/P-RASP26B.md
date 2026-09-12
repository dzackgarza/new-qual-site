---
schema: qual/card@1
id: P-RASP26B
kind: problem
title: "Metric on L^1 via antiderivatives and compactness via Arzela-Ascoli"
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
  date: 2026-09-09
  note: Checked against Problem 2 of the official UCSD Spring 2026 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Consider the function
$$
d(f, g) := \sup_{0 \leq x \leq 1} \left|\int_0^x (f(t) - g(t))\,dt\right|, \qquad f, g \in L^1([0,1]).
$$
Let $C := \{f \in L^1([0,1]) : |f(t)| \leq 1 \text{ for a.e. } t \in [0,1]\}$.

(1) Prove that $d$ is a metric on $L^1([0,1])$.

(2) Prove that $C$ is compact in $(L^1([0,1]), d)$.

Hint: Let $\tilde{C} = \{F(x) := \int_0^x f : f \in C\}$ and use Arzelà-Ascoli.
:::

::: solution
<1>1. Prove that $d$ is a metric.
::: proof
Nonnegativity and symmetry are immediate. For the triangle inequality, if $f,g,h\in L^1([0,1])$, then for every $x\in[0,1]$,
\[
\left|\int_0^x(f-h)\right|
\le
\left|\int_0^x(f-g)\right|
+
\left|\int_0^x(g-h)\right|.
\]
Taking the supremum over $x$ gives
\[
d(f,h)\le d(f,g)+d(g,h).
\]

It remains to prove definiteness. Suppose $d(f,g)=0$. Then
\[
F(x):=\int_0^x(f(t)-g(t))\,dt=0
\]
for every $x\in[0,1]$. The function $F$ is absolutely continuous, and the Lebesgue Fundamental Theorem of Calculus gives
\[
F'(x)=f(x)-g(x)
\]
for almost every $x$. Since $F\equiv0$, we have $F'=0$ almost everywhere, hence
\[
f=g
\]
almost everywhere. Thus $f$ and $g$ are the same element of $L^1([0,1])$.

Therefore $d$ is a metric on $L^1([0,1])$.
:::

<1>2. Identify the image of $C$ under the primitive map.
::: proof
Define
\[
T:C\to C([0,1]),
\qquad
T(f)(x)=\int_0^x f(t)\,dt.
\]
If $f\in C$, then for $0\le x<y\le1$,
\[
|T(f)(y)-T(f)(x)|
=\left|\int_x^y f(t)\,dt\right|
\le y-x.
\]
Thus every $T(f)$ is $1$-Lipschitz and vanishes at $0$.

Conversely, suppose $F\in C([0,1])$ is $1$-Lipschitz and $F(0)=0$. A Lipschitz function is absolutely continuous and differentiable almost everywhere, with
\[
|F'(t)|\le1
\]
almost everywhere. Put $f=F'$. Then $f\in C$ and the Fundamental Theorem of Calculus gives
\[
F(x)=F(0)+\int_0^x f(t)\,dt=T(f)(x).
\]
Hence
\[
T(C)
=\{F\in C([0,1]):F(0)=0,\ |F(x)-F(y)|\le|x-y|\}.
\]
:::

<1>3. Observe that $T$ is an isometry.
::: proof
For $f,g\in C$,
\[
\begin{aligned}
\|T(f)-T(g)\|_\infty
&=\sup_{0\le x\le1}
\left|\int_0^x(f(t)-g(t))\,dt\right|\\
&=d(f,g).
\end{aligned}
\]
Thus $T$ is an isometry from $(C,d)$ onto $T(C)$ equipped with the uniform norm.
:::

<1>4. Prove compactness by Arzelà--Ascoli.
::: proof
Every $F\in T(C)$ satisfies
\[
|F(x)|=|F(x)-F(0)|\le x\le1,
\]
so $T(C)$ is uniformly bounded. It is also equicontinuous because every element is $1$-Lipschitz.

By Arzelà--Ascoli, $T(C)$ is relatively compact in the uniform norm. It is also uniformly closed: if $F_n\in T(C)$ and $F_n\to F$ uniformly, then
\[
F(0)=0
\]
and, for every $x,y$,
\[
|F(x)-F(y)|
=\lim_{n\to\infty}|F_n(x)-F_n(y)|
\le|x-y|.
\]
Hence $F\in T(C)$ by Step 2.

Therefore $T(C)$ is compact in $C([0,1])$. Since $T$ is an isometry onto $T(C)$,
\[
\boxed{C\text{ is compact in }(L^1([0,1]),d).}
\]
:::
:::
