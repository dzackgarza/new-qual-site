---
schema: qual/card@1
id: P-BERK85S-16
kind: problem
title: Uniform convergence of moving Riemann averages of a continuous function
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Identified the limit as F(x)=integral_0^1 f(x+t) dt. On a fixed
    interval [a,b], uniform continuity of f on [a,b+1] bounds the
    left-endpoint Riemann-sum error uniformly in x by the modulus of
    continuity at mesh size 1/n.
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be continuous and define
\[
f_n(x)=\frac1n\sum_{k=0}^{n-1}f\left(x+\frac{k}{n}\right).
\]
Prove that $(f_n)$ converges uniformly to a limit on every finite interval $[a,b]$.
:::

::: {.solution}
Fix a finite interval $[a,b]$, and define
$$
F(x)\coloneqq\int_0^1 f(x+t)\,dt.
$$

<1>1. The function $f$ is uniformly continuous on $[a,b+1]$.

::: {.proof}
The interval $[a,b+1]$ is compact and $f$ is continuous on
$\mathbb R$. Therefore the Heine--Cantor theorem applies.
:::

<1>2. Define the modulus
$$
\omega(\delta)
\coloneqq
\sup\left\{
\abs{f(u)-f(v)}:
u,v\in[a,b+1],
\abs{u-v}\leq\delta
\right\}.
$$
Then
$$
\omega(\delta)\longrightarrow0
\qquad(\delta\downarrow0).
$$

::: {.proof}
This is exactly the uniform continuity from step <1>1, written in
terms of the modulus of continuity.
:::

<1>3. For every $x\in[a,b]$,
$$
f_n(x)
=
\sum_{k=0}^{n-1}
\int_{k/n}^{(k+1)/n}
f\left(x+\frac{k}{n}\right)\,dt.
$$

::: {.proof}
Each interval of integration has length $1/n$, so its $k$th term is
$$
\frac1n f\left(x+\frac{k}{n}\right).
$$
Summing gives the definition of $f_n(x)$.
:::

<1>4. For every $x\in[a,b]$,
$$
\abs{f_n(x)-F(x)}
\leq
\omega\left(\frac1n\right).
$$

::: {.proof}
By step <1>3 and by splitting the integral defining $F$ over the same
partition,
$$
\begin{aligned}
\abs{f_n(x)-F(x)}
&=
\left|
\sum_{k=0}^{n-1}
\int_{k/n}^{(k+1)/n}
\left[
f\left(x+\frac{k}{n}\right)-f(x+t)
\right]dt
\right|\\
&\leq
\sum_{k=0}^{n-1}
\int_{k/n}^{(k+1)/n}
\left|
f\left(x+\frac{k}{n}\right)-f(x+t)
\right|dt.
\end{aligned}
$$
If $t\in[k/n,(k+1)/n]$, then
$$
\left|
\left(x+\frac{k}{n}\right)-(x+t)
\right|
\leq
\frac1n.
$$
Moreover both arguments lie in $[a,b+1]$. Thus every integrand is at
most $\omega(1/n)$, and the total length of all subintervals is $1$.
This yields the claimed bound.
:::

<1>5. The sequence $(f_n)$ converges uniformly to $F$ on $[a,b]$.

::: {.proof}
Taking the supremum in step <1>4 gives
$$
\sup_{x\in[a,b]}\abs{f_n(x)-F(x)}
\leq
\omega\left(\frac1n\right).
$$
By step <1>2, the right-hand side tends to $0$.
:::

<1>6. Therefore, on every finite interval,
$$
\boxed{
f_n(x)\longrightarrow
\int_0^1f(x+t)\,dt
}
$$
uniformly.

::: {.proof}
The interval $[a,b]$ was arbitrary, and step <1>5 proves uniform
convergence on it.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
