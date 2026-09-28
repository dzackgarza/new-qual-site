---
schema: qual/card@1
id: P-BERK87S-05
kind: problem
title: Periodization of a decaying continuous function and integration against periodic functions
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
    Used the quadratic decay to obtain locally uniform absolute convergence
    of the periodization. Uniform convergence on [0,1] permits termwise
    integration, and a unit-interval change of variables plus periodicity of
    G converts the resulting sum into the integral over R.
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be continuous and satisfy
\[
|f(x)|\le\frac{C}{1+x^2}
\]
for some $C>0$. Define
\[
F(x)=\sum_{n=-\infty}^{\infty}f(x+n).
\]

1. Prove that $F$ is continuous and $1$-periodic.
2. If $G$ is continuous and $1$-periodic, prove that
   \[
   \int_0^1F(x)G(x)\,dx
   =\int_{-\infty}^{\infty}f(x)G(x)\,dx.
   \]
:::

::: {.solution}
<1>1. The series
$$
\sum_{n\in\ZZ}f(x+n)
$$
converges absolutely and uniformly on every compact interval.

::: {.proof}
Fix a compact interval $K=[a,b]$ and set
$$
R\coloneqq\max\{\abs{a},\abs{b}\}.
$$
If $x\in K$ and
$$
\abs{n}\geq2R+1,
$$
then
$$
\abs{x+n}
\geq
\abs{n}-\abs{x}
\geq
\abs{n}-R
\geq
\frac{\abs{n}}{2}.
$$
Hence
$$
\abs{f(x+n)}
\leq
\frac{C}{1+(x+n)^2}
\leq
\frac{4C}{n^2}.
$$
The series
$$
\sum_{n\in\ZZ\setminus\{0\}}\frac1{n^2}
$$
converges. The finitely many remaining values of $n$ cause no problem,
so the Weierstrass M-test gives uniform absolute convergence on $K$.
:::

<1>2. The function
$$
F(x)=\sum_{n\in\ZZ}f(x+n)
$$
is continuous on $\RR$.

::: {.proof}
Each function
$$
x\longmapsto f(x+n)
$$
is continuous. By step <1>1, their series converges uniformly on every
compact interval. Therefore its sum is continuous on every compact
interval, hence on all of $\RR$.
:::

<1>3. The function $F$ is $1$-periodic.

::: {.proof}
Absolute convergence from step <1>1 permits reindexing:
$$
\begin{aligned}
F(x+1)
&=
\sum_{n\in\ZZ}f(x+1+n)\\
&=
\sum_{m\in\ZZ}f(x+m)\\
&=
F(x),
\end{aligned}
$$
where $m=n+1$.
:::

<1>4. If $G$ is continuous and $1$-periodic, then $G$ is bounded on
$\RR$.

::: {.proof}
Continuity on the compact interval $[0,1]$ gives a number $M_G$ such
that
$$
\abs{G(x)}\leq M_G
$$
for $x\in[0,1]$. For arbitrary $y\in\RR$, choose $k\in\ZZ$ with
$y-k\in[0,1]$. Periodicity gives
$$
G(y)=G(y-k),
$$
so the same bound holds on all of $\RR$.
:::

<1>5. One may integrate the defining series for $F$ term by term against
$G$ on $[0,1]$:
$$
\int_0^1F(x)G(x)\,dx
=
\sum_{n\in\ZZ}
\int_0^1 f(x+n)G(x)\,dx.
$$

::: {.proof}
By step <1>1, the series defining $F$ converges uniformly on $[0,1]$.
By step <1>4, $G$ is bounded there. Hence
$$
\sum_{n\in\ZZ}f(x+n)G(x)
$$
also converges uniformly on $[0,1]$. Termwise integration of a uniformly
convergent series of continuous functions is therefore valid.
:::

<1>6. For each $n\in\ZZ$,
$$
\int_0^1 f(x+n)G(x)\,dx
=
\int_n^{n+1}f(y)G(y)\,dy.
$$

::: {.proof}
Use the substitution
$$
y=x+n.
$$
Then
$$
\begin{aligned}
\int_0^1 f(x+n)G(x)\,dx
&=
\int_n^{n+1}f(y)G(y-n)\,dy\\
&=
\int_n^{n+1}f(y)G(y)\,dy,
\end{aligned}
$$
because $G$ has period $1$ and $n\in\ZZ$.
:::

<1>7. The function $fG$ is absolutely integrable on $\RR$.

::: {.proof}
By step <1>4,
$$
\abs{f(x)G(x)}
\leq
\frac{CM_G}{1+x^2}.
$$
The majorant is integrable on $\RR$, so
$$
\int_{-\infty}^{\infty}\abs{f(x)G(x)}\,dx<\infty.
$$
:::

<1>8. Therefore
$$
\boxed{
\int_0^1F(x)G(x)\,dx
=
\int_{-\infty}^{\infty}f(x)G(x)\,dx
}.
$$

::: {.proof}
By steps <1>5 and <1>6,
$$
\int_0^1F(x)G(x)\,dx
=
\sum_{n\in\ZZ}
\int_n^{n+1}f(y)G(y)\,dy.
$$
Absolute integrability from step <1>7 allows the unit intervals
$[n,n+1]$ to be summed over all $n\in\ZZ$, giving exactly the improper
integral over $\RR$.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>2 and <1>3 prove part 1, and step <1>8 proves part 2.
:::
:::
