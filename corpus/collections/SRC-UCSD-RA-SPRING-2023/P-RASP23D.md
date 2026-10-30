---
schema: qual/card@1
id: P-RASP23D
kind: problem
title: "Radon measure on a non-standard metric space"
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
  note: Checked against Problem 4 of the official UCSD Spring 2023 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Define the distance function between $(x_1, y_1)$ and $(x_2, y_2)$ in the plane to be
$$
d = \begin{cases} \abs{y_1 - y_2} & \text{if } x_1 = x_2, \\ 1 + \abs{y_1 - y_2} & \text{if } x_1 \neq x_2. \end{cases}
$$

(i) Prove that this is indeed a metric.

(ii) The corresponding metric space $(X, d)$ is locally compact.

(iii) For any $f \in C_c(X)$, let $F$ be the set of $x$ such that there exists $y$ with $f(x,y) \neq 0$.
Prove that $F$ is a finite set $\{x_1, x_2, \ldots, x_n\}$.

(iv) For $f$ in (iii) define $I(f) = \sum_{i=1}^{n} \int_{-\infty}^{\infty} f(x_i, y)\,dy$.
Then $I(f)$ induces a Radon measure $\mu$ on $X$.
Is $\mu$ inner regular for all Borel sets?
If yes, prove it.
If no, find a Borel set which is not inner regular.
:::

::: {.solution}

::: pf

::: pf-step

Verify the metric axioms.

::: pf-proof

Write a point as $(x,y)$. Then the proposed distance is
$$
d((x_1,y_1),(x_2,y_2))
=d_{\mathrm{disc}}(x_1,x_2)+\abs{y_1-y_2},
$$
where
$$
d_{\mathrm{disc}}(x_1,x_2)=
\begin{cases}
0,&x_1=x_2,\\
1,&x_1\ne x_2.
\end{cases}
$$
The discrete distance and the Euclidean distance are metrics, and the sum of two metrics is a metric. Thus positivity, symmetry, definiteness, and the triangle inequality all hold.

:::

:::

::: pf-step

Prove local compactness.

::: pf-proof

Fix $(x_0,y_0)\in X$ and choose $0<r<1$. If
$$
d((x,y),(x_0,y_0))\le r,
$$
then necessarily $x=x_0$, because distinct $x$-coordinates already contribute $1$ to the distance. Hence
$$
\overline B((x_0,y_0),r)
=\{x_0\}\times[y_0-r,y_0+r].
$$
With the induced metric this is isometric to the compact interval $[y_0-r,y_0+r]$. Thus every point has a neighborhood with compact closure, so $X$ is locally compact.

:::

:::

::: {.pf-step #finite-lines}

Show that a compactly supported continuous function uses only finitely many vertical lines.

::: pf-proof

Let $K=\operatorname{supp}f$, which is compact. The balls
$$
B((x,y),1/3),\qquad (x,y)\in K,
$$
form an open cover of $K$. Each such ball lies entirely in one vertical line $\{x\}\times\RR$. By compactness, finitely many of these balls cover $K$. Therefore $K$, and hence the set
$$
F=\{x:\exists y,\ f(x,y)\ne0\},
$$
meets only finitely many vertical lines. Thus
$$
F=\{x_1,\dots,x_n\}.
$$

:::

:::

::: {.pf-step #open-sets}

For every open $V\subseteq X$, $\mu(V)=\sum_{x\in\RR}m(V_x)$, where $V_x\coloneqq\{y:(x,y)\in V\}$ and an uncountable sum of nonnegative numbers means the supremum of its finite partial sums.

::: pf-proof

By the Riesz representation theorem (Rudin, *Real and Complex Analysis*, Theorem 2.14), $\mu(V)=\sup\{I(f):f\prec V\}$ for open $V$, and $\mu(E)=\inf\{\mu(V):E\subseteq V,\ V\text{ open}\}$ for every Borel $E$.
Each section $V_x$ is open in $\RR$, because a ball of radius less than $1$ lies in one vertical line and is a Euclidean interval there.

If $f\prec V$, step [](#finite-lines){.pf-ref} gives finitely many lines $x_1,\ldots,x_n$ that carry the support of $f$, and $0\le f\le 1$, so $I(f)\le\sum_{i=1}^n m(V_{x_i})\le\sum_x m(V_x)$.
Conversely, given finitely many $x_1,\ldots,x_n$ and compact sets $K_i\subseteq V_{x_i}$, Urysohn's lemma on each line gives $f\prec V$ with $f=1$ on $\bigcup_i\{x_i\}\times K_i$, so $I(f)\ge\sum_i m(K_i)$.
Inner regularity of Lebesgue measure on the open sets $V_{x_i}$ makes $\sum_i m(K_i)$ approach $\sum_i m(V_{x_i})$, and the supremum of these finite sums is $\sum_x m(V_x)$.

:::

:::

::: {.pf-step #line-measure}

The set $E\coloneqq\RR\times\{0\}$ is closed and $\mu(E)=\infty$.

::: pf-proof

A point $(x,y)$ with $y\neq0$ has the ball of radius $\min(\abs{y},1)/2$ about it inside $\{x\}\times(\RR\setminus\{0\})$, so $E$ is closed, hence Borel.
Let $V\supseteq E$ be open. For every $x\in\RR$ the open set $V_x$ contains $0$, so $m(V_x)>0$.
Uncountably many positive numbers include, for some $k\ge1$, infinitely many greater than $1/k$, so $\sum_x m(V_x)=\infty$.
By step [](#open-sets){.pf-ref}, $\mu(V)=\infty$ for every open $V\supseteq E$, so $\mu(E)=\infty$ by outer regularity.

:::

:::

::: pf-step

The answer is $\boxed{\text{No}}$: the Borel set $E=\RR\times\{0\}$ is not inner regular.

::: pf-proof

Let $K\subseteq E$ be compact. As in step [](#finite-lines){.pf-ref}, finitely many balls of radius $1/3$, each inside one vertical line, cover $K$, so $K$ meets finitely many lines. Each line meets $E$ in one point, so $K=\{(x_1,0),\ldots,(x_n,0)\}$ is finite.
For $\varepsilon>0$ the open set $V=\bigcup_{i=1}^n\{x_i\}\times(-\varepsilon,\varepsilon)$ contains $K$, and $\mu(V)=2n\varepsilon$ by step [](#open-sets){.pf-ref}. Hence $\mu(K)=0$.
Thus $\sup\{\mu(K):K\subseteq E,\ K\text{ compact}\}=0<\infty=\mu(E)$ by step [](#line-measure){.pf-ref}.

:::

:::

:::

:::
