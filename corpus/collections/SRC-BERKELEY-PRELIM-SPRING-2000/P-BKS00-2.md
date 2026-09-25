---
schema: qual/card@1
id: P-BKS00-2
kind: problem
title: Uniform convergence of successive maxima of an equicontinuous bounded sequence
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
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Let g be the pointwise supremum of the f_n. Compactness upgrades
    equicontinuity to one uniform modulus shared by all f_n, hence by g
    and the finite maxima g_n. A finite delta-net then upgrades pointwise
    convergence at its centers to uniform convergence on X.
---

::: {.problem}
Let $\{f_n\}_{n=1}^\infty$ be a uniformly bounded equicontinuous sequence of real-valued functions on a compact metric space $(X,d)$. Define
\[
g_n(x)=\max\{f_1(x),\ldots,f_n(x)\}.
\]
Prove that $\{g_n\}$ converges uniformly on $X$.
:::

::: {.solution}
If $X=\varnothing$, the conclusion is immediate. Assume henceforth that
$X\ne\varnothing$, and define
$$
g(x)=\sup_{k\geq 1} f_k(x).
$$

<1>1. For every $x\in X$,
$$
g_n(x)\uparrow g(x).
$$

::: {.proof}
Uniform boundedness gives $M>0$ such that
$$
\abs{f_k(x)}\leq M
$$
for every $k\geq 1$ and every $x\in X$. Thus $g(x)$ is finite. Moreover,
$$
g_n(x)
=
\max_{1\leq k\leq n} f_k(x)
$$
is nondecreasing in $n$, and its supremum over $n$ is exactly
$\sup_{k\geq 1}f_k(x)=g(x)$.
:::

<1>2. For every $\eta>0$ there exists $\delta>0$ such that, for every
$k\geq 1$,
$$
d(x,y)<\delta
\quad\Longrightarrow\quad
\abs{f_k(x)-f_k(y)}<\eta.
$$

::: {.proof}
For each $a\in X$, equicontinuity at $a$ gives $r_a>0$ such that
$$
d(a,z)<r_a
\quad\Longrightarrow\quad
\abs{f_k(a)-f_k(z)}<\frac{\eta}{2}
$$
for every $k\geq 1$. The balls
$$
B\left(a,\frac{r_a}{2}\right),
\qquad
a\in X,
$$
cover $X$. By compactness, finitely many of them,
$$
B\left(a_j,\frac{r_{a_j}}{2}\right),
\qquad
1\leq j\leq m,
$$
cover $X$. Set
$$
\delta
=
\min_{1\leq j\leq m}\frac{r_{a_j}}{2}
>0.
$$
If $d(x,y)<\delta$, choose $j$ with
$d(x,a_j)<r_{a_j}/2$. Then
$$
d(y,a_j)
<
\delta+\frac{r_{a_j}}{2}
\leq
r_{a_j}.
$$
Therefore, for every $k$,
$$
\abs{f_k(x)-f_k(y)}
\leq
\abs{f_k(x)-f_k(a_j)}
+
\abs{f_k(a_j)-f_k(y)}
<
\eta.
$$
:::

<1>3. For the same $\delta$ as in step <1>2,
$$
d(x,y)<\delta
\quad\Longrightarrow\quad
\abs{g_n(x)-g_n(y)}<\eta
$$
for every $n$, and also
$$
d(x,y)<\delta
\quad\Longrightarrow\quad
\abs{g(x)-g(y)}\leq\eta.
$$

::: {.proof}
If $d(x,y)<\delta$, step <1>2 gives
$$
f_k(x)<f_k(y)+\eta
$$
for every $k$. Taking the maximum over $1\leq k\leq n$ gives
$$
g_n(x)<g_n(y)+\eta.
$$
Interchanging $x$ and $y$ yields
$\abs{g_n(x)-g_n(y)}<\eta$.

Taking the supremum over all $k$ instead gives
$$
g(x)\leq g(y)+\eta,
$$
and interchanging $x$ and $y$ gives
$\abs{g(x)-g(y)}\leq\eta$.
:::

<1>4. For every $\varepsilon>0$ there exists $N$ such that, for all
$n\geq N$ and all $x\in X$,
$$
0\leq g(x)-g_n(x)<\varepsilon.
$$

::: {.proof}
Apply step <1>2 with
$$
\eta=\frac{\varepsilon}{3}
$$
and let $\delta>0$ be the resulting number. By compactness, choose
$x_1,\ldots,x_m\in X$ such that
$$
X
\subseteq
\bigcup_{j=1}^m B\left(x_j,\frac{\delta}{2}\right).
$$
By step <1>1, for each $j$ there exists $N_j$ such that
$$
n\geq N_j
\quad\Longrightarrow\quad
0\leq g(x_j)-g_n(x_j)<\frac{\varepsilon}{3}.
$$
Set
$$
N=\max_{1\leq j\leq m}N_j.
$$

Let $n\geq N$ and $x\in X$. Choose $j$ with
$d(x,x_j)<\delta/2$. Step <1>3 then gives
$$
\abs{g(x)-g(x_j)}\leq\frac{\varepsilon}{3},
\qquad
\abs{g_n(x)-g_n(x_j)}<\frac{\varepsilon}{3}.
$$
Since $g_n\leq g$ pointwise,
$$
\begin{aligned}
0
&\leq
g(x)-g_n(x)\\
&\leq
\abs{g(x)-g(x_j)}
+
\bigl(g(x_j)-g_n(x_j)\bigr)
+
\abs{g_n(x_j)-g_n(x)}\\
&<
\varepsilon.
\end{aligned}
$$
:::

<1>5. The sequence $\{g_n\}$ converges uniformly on $X$ to $g$.

::: {.proof}
Step <1>4 is exactly the definition of uniform convergence of $g_n$ to
$g$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 proves the required uniform convergence.
:::
:::
