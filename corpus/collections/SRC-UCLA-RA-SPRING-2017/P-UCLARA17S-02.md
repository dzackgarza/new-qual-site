---
schema: qual/card@1
id: P-UCLARA17S-02
kind: problem
title: $L^1$-convergent subsequences of $L^2$-bounded monotone functions
classification:
  areas:
  - real-analysis
  topics:
  - Monotone Functions
  - Compactness
  - L¹
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $f_n:[0,1]\to[0,\infty)$ be a sequence of functions, each non-decreasing on $[0,1]$. Suppose the sequence is uniformly bounded in $L^2([0,1])$. Show that there exists a subsequence that converges in $L^1([0,1])$.
:::

::: {.solution}

Choose $C\ge0$ such that
$$
\norm{f_n}_{L^2([0,1])}\le C
$$
for every $n$.

::: pf

::: {.pf-step #s1-1}

For every $x\in[0,1)$ and every $n$,
$$
0\le f_n(x)\le\frac{C}{\sqrt{1-x}}.
$$


::: pf-proof

Since $f_n$ is nonnegative and non-decreasing,
$$
\int_x^1 f_n(t)^2\,dt
\ge (1-x)f_n(x)^2.
$$
The left-hand side is at most $C^2$. Dividing by $1-x>0$ and taking square roots gives the bound.

:::

:::

::: {.pf-step #s1-2}

There is a subsequence $(f_{n_k})$ and a non-decreasing function $f:[0,1)\to[0,\infty)$ such that
$$
f_{n_k}(x)\longrightarrow f(x)
$$
for almost every $x\in[0,1)$.


::: pf-proof

Enumerate $\QQ\cap[0,1)$ as $q_1,q_2,\ldots$. By step [](#s1-1){.pf-ref}, for each fixed $q_j$ the sequence $(f_n(q_j))_n$ is bounded. Successively extract subsequences converging at $q_1,q_2,\ldots$, and take the diagonal subsequence $(f_{n_k})$. Then
$$
g(q)\coloneqq\lim_{k\to\infty}f_{n_k}(q)
$$
exists for every rational $q\in[0,1)$, and $g$ is non-decreasing on the rationals.

For $x\in(0,1)$ define
$$
\alpha(x)\coloneqq\sup_{q<x,\ q\in\QQ}g(q),
\qquad
\beta(x)\coloneqq\inf_{r>x,\ r\in\QQ}g(r).
$$
For rationals $q<x<r$, monotonicity gives
$$
f_{n_k}(q)\le f_{n_k}(x)\le f_{n_k}(r).
$$
Hence
$$
\alpha(x)
\le\liminf_{k\to\infty}f_{n_k}(x)
\le\limsup_{k\to\infty}f_{n_k}(x)
\le\beta(x).
$$

The set
$$
E\coloneqq\{x\in(0,1):\alpha(x)<\beta(x)\}
$$
is countable. Indeed, if $x<y$, choose a rational $r$ with $x<r<y$; then
$$
\beta(x)\le g(r)\le\alpha(y),
$$
so the open intervals $(\alpha(x),\beta(x))$ for $x\in E$ are pairwise disjoint. Each contains a rational number, so there can be only countably many of them.

Define $f(x)=\alpha(x)$ for $0<x<1$ and set $f(0)=0$. The function $f$ is non-decreasing on $[0,1)$. For every $x\notin E$, one has $\alpha(x)=\beta(x)$, so the displayed squeeze gives $f_{n_k}(x)\to f(x)$. Thus convergence holds almost everywhere.

:::

:::

::: {.pf-step #s1-3}

The limit function satisfies
$$
f\in L^2([0,1])
\qquad\text{and}\qquad
\norm{f}_2\le C.
$$


::: pf-proof

Extend $f$ arbitrarily to the point $1$, which does not affect any integral. By step [](#s1-2){.pf-ref} and Fatou's lemma,
$$
\int_0^1 f(x)^2\,dx
\le\liminf_{k\to\infty}\int_0^1 f_{n_k}(x)^2\,dx
\le C^2.
$$

:::

:::

::: {.pf-step #s1-4}

For every $0<\delta<1$,
$$
\int_{1-\delta}^1\abs{f_{n_k}(x)-f(x)}\,dx
\le2C\sqrt\delta.
$$


::: pf-proof

By the triangle inequality and Cauchy--Schwarz,
$$
\begin{aligned}
\int_{1-\delta}^1\abs{f_{n_k}-f}
&\le\int_{1-\delta}^1 f_{n_k}+\int_{1-\delta}^1 f\\
&\le\sqrt\delta\,\norm{f_{n_k}}_2
+\sqrt\delta\,\norm{f}_2\\
&\le2C\sqrt\delta
\end{aligned}
$$
by the uniform bound and step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

For every fixed $0<\delta<1$,
$$
\int_0^{1-\delta}\abs{f_{n_k}(x)-f(x)}\,dx\longrightarrow0.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
0\le f_{n_k}(x)\le\frac C{\sqrt\delta}
$$
for $0\le x\le1-\delta$. The same bound holds for $f(x)$ at almost every point by step [](#s1-2){.pf-ref}. Hence
$$
\abs{f_{n_k}(x)-f(x)}\le\frac{2C}{\sqrt\delta}
$$
almost everywhere on this finite interval. Step [](#s1-2){.pf-ref} gives pointwise convergence almost everywhere, so the dominated convergence theorem gives the asserted $L^1$ convergence on $[0,1-\delta]$.

:::

:::

::: {.pf-step #s1-6}

The subsequence $(f_{n_k})$ converges to $f$ in $L^1([0,1])$.


::: pf-proof

Let $\varepsilon>0$. If $C=0$, every $f_n=0$ almost everywhere and the conclusion is immediate. Assume $C>0$ and choose $\delta>0$ so small that
$$
2C\sqrt\delta<\frac\varepsilon2.
$$
By step [](#s1-5){.pf-ref}, for all sufficiently large $k$,
$$
\int_0^{1-\delta}\abs{f_{n_k}-f}<\frac\varepsilon2.
$$
Step [](#s1-4){.pf-ref} then gives
$$
\norm{f_{n_k}-f}_1<\varepsilon.
$$

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} constructs the required $L^1$-convergent subsequence.

:::

:::

:::
