---
schema: qual/card@1
id: P-QMPVS
kind: problem
title: Hölder's inequality, Minkowski's inequality, $L^\infty[0,1]$, and $\lim_{p\to\infty}\int_{[0,1]}f^p$
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Norms
  - L∞
relations: []
review: draft
---

::: {.problem}
a. Prove Holder's inequality:
  let $f\in L^p, g\in L^q$ with $p, q$ conjugate, and show that
\[
\pnorm{fg}p \leq \pnorm{f}p \cdot \pnorm{g}q
.\]

b. Prove Minkowski's Inequality:
\[
1\leq p < \infty \implies \pnorm{f+g}{p} \leq \pnorm{f}{p}+ \pnorm{g}{p}
.\]
Conclude that if $f, g\in L^p(\RR^n)$ then so is $f+g$.

c. Let $X = [0, 1] \subset \RR$.

    1. Give a definition of the Banach space $L^\infty(X)$ of essentially bounded functions of $X$.

    2. Let $f$ be non-negative and measurable on $X$, prove that
    \[
    \int_X f(x)^p \,dx \converges{p\to\infty}\to
    \begin{dcases}
    \infty \quad\text{or} \\
    m\qty{\theset{f\inv(1)}}
    \end{dcases}
    ,\]
    and characterize the functions of each type
:::

::: {.solution}
Part (c)2. Let $f \ge 0$ be measurable on $X = [0,1]$.

<1>1. $\int_X f^p = \int_{\theset{f < 1}} f^p + m\theset{f = 1} + \int_{\theset{f > 1}} f^p$.

::: {.proof}
$X$ is the disjoint union of $\theset{f < 1}$, $\theset{f = 1}$ and $\theset{f > 1}$, and $f^p = 1$ on $\theset{f = 1}$.
:::

<1>2. $\int_{\theset{f < 1}} f^p \to 0$ as $p \to \infty$.

::: {.proof}
On $\theset{f < 1}$, $f^p \to 0$ pointwise and $0 \le f^p \le 1$, and $m(X) = 1$, so dominated convergence applies.
:::

<1>3. $\int_{\theset{f > 1}} f^p \to \infty$ if $m\theset{f > 1} > 0$, and it is $0$ if $m\theset{f > 1} = 0$.

::: {.proof}
If $m\theset{f > 1} > 0$, then $m\theset{f > 1 + 1/k} > 0$ for some $k$, and $\int_{\theset{f > 1}} f^p \ge (1 + 1/k)^p\, m\theset{f > 1 + 1/k} \to \infty$.
:::

<1>4. Q.E.D.

::: {.proof}
By steps <1>1--<1>3, $\int_X f^p \to m\theset{f = 1} = m(f^{-1}(1))$ when $f \le 1$ a.e., and $\int_X f^p \to \infty$ when $m\theset{f > 1} > 0$.
:::
:::
