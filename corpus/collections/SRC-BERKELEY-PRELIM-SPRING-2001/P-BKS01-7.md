---
schema: qual/card@1
id: P-BKS01-7
kind: problem
title: Maps $[0,1]\to[0,1]$ that are $1$-Lipschitz at scales $\ge1/n$ have a uniformly convergent subsequence
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Derived the global asymptotic Lipschitz estimate
    |f_n(x)-f_n(y)| <= |x-y|+2/n for n>=3. A diagonal subsequence
    converges on Q intersect [0,1], and the estimate plus a finite
    rational net makes that subsequence uniformly Cauchy.
---

::: {.problem}
Let $f_n:[0,1]\to[0,1]$ satisfy
\[
|f_n(x)-f_n(y)|\le |x-y|
\]
whenever $|x-y|\ge1/n$.
Prove that $(f_n)$ has a uniformly convergent subsequence.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every $n\geq3$ and all $x,y\in[0,1]$,
$$
\abs{f_n(x)-f_n(y)}
\leq
\abs{x-y}+\frac2n.
$$

::: pf-proof

It is enough to assume $x\leq y$. If
$$
y-x\geq\frac1n,
$$
the hypothesis gives the stronger estimate
$$
\abs{f_n(x)-f_n(y)}\leq y-x.
$$

Now suppose
$$
0\leq y-x<\frac1n.
$$
If $x\geq1/n$, set
$$
z=x-\frac1n.
$$
Then
$$
x-z=\frac1n,
\qquad
y-z=y-x+\frac1n\geq\frac1n.
$$
Applying the hypothesis to $(x,z)$ and $(y,z)$,
$$
\begin{aligned}
\abs{f_n(x)-f_n(y)}
&\leq
\abs{f_n(x)-f_n(z)}
+
\abs{f_n(z)-f_n(y)}\\
&\leq
\frac1n+
\left(y-x+\frac1n\right)\\
&=
y-x+\frac2n.
\end{aligned}
$$

If $x<1/n$, then
$$
y<x+\frac1n<\frac2n.
$$
Since $n\geq3$, the point
$$
z=y+\frac1n
$$
lies in $[0,1]$. Moreover,
$$
z-y=\frac1n,
\qquad
z-x=y-x+\frac1n\geq\frac1n.
$$
The same triangle-inequality argument gives
$$
\abs{f_n(x)-f_n(y)}
\leq
y-x+\frac2n.
$$

:::

:::

::: {.pf-step #s2}

There is a subsequence
$$
(f_{n_k})_{k\geq1}
$$
that converges at every rational point of $[0,1]$.

::: pf-proof

Enumerate
$$
\QQ\cap[0,1]
=
\{q_1,q_2,\ldots\}.
$$
The sequence $(f_n(q_1))_n$ lies in the compact interval $[0,1]$, so
it has a convergent subsequence. From that subsequence choose one on
which the values at $q_2$ converge, and continue inductively. The
diagonal subsequence converges at every $q_j$.

:::

:::

::: {.pf-step #s3}

The subsequence from step [](#s2){.pf-ref} is uniformly Cauchy on $[0,1]$.

::: pf-proof

Let $\varepsilon>0$. Choose finitely many rational points
$$
q_1',\ldots,q_m'\in\QQ\cap[0,1]
$$
such that every $x\in[0,1]$ satisfies
$$
\abs{x-q_j'}<\frac{\varepsilon}{6}
$$
for some $j$.

Since $n_k\to\infty$, there exists $K_1$ such that for $k\geq K_1$,
$$
n_k\geq3,
\qquad
\frac{2}{n_k}<\frac{\varepsilon}{6}.
$$
Since the subsequence converges at each of the finitely many points
$q_j'$, there exists $K_2$ such that for all $k,\ell\geq K_2$ and
every $j$,
$$
\abs{f_{n_k}(q_j')-f_{n_\ell}(q_j')}
<
\frac{\varepsilon}{3}.
$$

Let $k,\ell\geq\max\{K_1,K_2\}$ and $x\in[0,1]$. Choose $q_j'$
within $\varepsilon/6$ of $x$. Step [](#s1){.pf-ref} gives
$$
\abs{f_{n_k}(x)-f_{n_k}(q_j')}
<
\frac{\varepsilon}{3}
$$
and
$$
\abs{f_{n_\ell}(x)-f_{n_\ell}(q_j')}
<
\frac{\varepsilon}{3}.
$$
Therefore
$$
\begin{aligned}
\abs{f_{n_k}(x)-f_{n_\ell}(x)}
&\leq
\abs{f_{n_k}(x)-f_{n_k}(q_j')}
+
\abs{f_{n_k}(q_j')-f_{n_\ell}(q_j')}\\
&\qquad+
\abs{f_{n_\ell}(q_j')-f_{n_\ell}(x)}\\
&<
\varepsilon.
\end{aligned}
$$
The bound is independent of $x$, so the subsequence is uniformly
Cauchy.

:::

:::

::: {.pf-step #s4}

The subsequence $(f_{n_k})$ converges uniformly on $[0,1]$.

::: pf-proof

For each $x\in[0,1]$, step [](#s3){.pf-ref} makes the real sequence
$(f_{n_k}(x))_k$ Cauchy, hence convergent; denote its limit by $f(x)$.
The uniform Cauchy estimate in step [](#s3){.pf-ref} remains valid after letting
$\ell\to\infty$, so for every $\varepsilon>0$ and all sufficiently
large $k$,
$$
\sup_{x\in[0,1]}
\abs{f_{n_k}(x)-f(x)}
\leq
\varepsilon.
$$
Thus $f_{n_k}\to f$ uniformly.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives the required uniformly convergent subsequence.

:::

:::

:::
