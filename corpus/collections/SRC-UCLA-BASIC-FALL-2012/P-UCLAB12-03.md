---
schema: qual/card@1
id: P-UCLAB12-03
kind: problem
title: Dini's theorem
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $\{f_n(x)\}$ be a sequence of non-negative continuous functions on a compact metric space $X$. Assume $f_n(x) \geq f_{n+1}(x)$ for all $n$ and $x$, so that $\lim_{n\to\infty} f_n(x) = f(x)$ exists for every $x \in X$. Prove $f$ is continuous if and only if $f_n$ converges to $f$ uniformly on $X$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $f_n\to f$ uniformly on $X$, then $f$ is continuous.


::: pf-proof

Let $x_0\in X$ and $\varepsilon>0$.
Choose $N$ such that
$$
\abs{f_N(x)-f(x)}<\frac{\varepsilon}{3}
$$
for every $x\in X$.
Since $f_N$ is continuous at $x_0$, there exists $\delta>0$ such that
$$
d(x,x_0)<\delta
$$
implies
$$
\abs{f_N(x)-f_N(x_0)}<\frac{\varepsilon}{3}.
$$
Then
$$
\begin{aligned}
\abs{f(x)-f(x_0)}
&\le
\abs{f(x)-f_N(x)}
+
\abs{f_N(x)-f_N(x_0)}
+
\abs{f_N(x_0)-f(x_0)}\\
&<
\varepsilon.
\end{aligned}
$$
Thus $f$ is continuous at $x_0$, and hence on $X$.

:::

:::

::: {.pf-step #s1-2}

Assume conversely that $f$ is continuous, and fix $\varepsilon>0$.
For each $n$, define
$$
U_n=\{x\in X:f_n(x)-f(x)<\varepsilon\}.
$$
Then $U_n$ is open.


::: pf-proof

The function
$$
x\longmapsto f_n(x)-f(x)
$$
is continuous because both $f_n$ and $f$ are continuous. Therefore
$$
U_n=(f_n-f)^{-1}((-\infty,\varepsilon))
$$
is open.

:::

:::

::: {.pf-step #s1-3}

The sets $U_n$ are increasing:
$$
U_n\subseteq U_{n+1}.
$$


::: pf-proof

Since
$$
f_{n+1}(x)\le f_n(x)
$$
for every $x$,
$$
f_{n+1}(x)-f(x)
\le
f_n(x)-f(x).
$$
Thus membership in $U_n$ implies membership in $U_{n+1}$.

:::

:::

::: {.pf-step #s1-4}

The sets $U_n$ cover $X$.


::: pf-proof

Fix $x\in X$. By pointwise convergence,
$$
f_n(x)\to f(x).
$$
Also
$$
f_n(x)\ge f(x)
$$
because the sequence is decreasing to its limit. Hence for sufficiently large $n$,
$$
0\le f_n(x)-f(x)<\varepsilon,
$$
so $x\in U_n$.

:::

:::

::: {.pf-step #s1-5}

There exists $N$ such that
$$
U_N=X.
$$


::: pf-proof

By steps [](#s1-2){.pf-ref} and [](#s1-4){.pf-ref}, the sets $U_n$ form an open cover of the compact space $X$. Hence finitely many
$$
U_{n_1},\ldots,U_{n_r}
$$
cover $X$. Let
$$
N=\max\{n_1,\ldots,n_r\}.
$$
By step [](#s1-3){.pf-ref},
$$
U_{n_j}\subseteq U_N
$$
for every $j$, so
$$
X\subseteq U_N\subseteq X.
$$
Thus $U_N=X$.

:::

:::

::: {.pf-step #s1-6}

For every $n\ge N$ and every $x\in X$,
$$
0\le f_n(x)-f(x)<\varepsilon.
$$


::: pf-proof

Because $U_N=X$,
$$
f_N(x)-f(x)<\varepsilon
$$
for all $x$.
For $n\ge N$,
$$
f(x)\le f_n(x)\le f_N(x),
$$
so
$$
0\le f_n(x)-f(x)\le f_N(x)-f(x)<\varepsilon.
$$

:::

:::

::: {.pf-step #s1-7}

Therefore $f_n\to f$ uniformly on $X$.


::: pf-proof

Step [](#s1-6){.pf-ref} gives
$$
\sup_{x\in X}\abs{f_n(x)-f(x)}<\varepsilon
$$
for every $n\ge N$. This is uniform convergence.

:::

:::

::: {.pf-step #s1-8}

Hence
$$
\boxed{
f\text{ is continuous}
\iff
f_n\to f\text{ uniformly on }X
}.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} proves the forward implication from uniform convergence to continuity, and steps [](#s1-2){.pf-ref} through [](#s1-7){.pf-ref} prove the converse under the monotone hypotheses.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required equivalence.

:::

:::

:::
