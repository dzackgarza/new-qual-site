---
schema: qual/card@1
id: P-YSR66
kind: problem
title: Riesz's lemma and noncompactness of the infinite-dimensional unit ball
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
  - Norms
  - Compactness
relations: []
review: draft
---

::: {.problem}
(a) Let $X$ be a normed vector space and $Y$ be a closed linear subspace of $X$.
Assume $Y$ is a proper subspace, that is, $Y\ne X$.
Show that, for arbitrary $\epsilon\in(0,1)$, there is an element $x\in X$ such that $\norm{x}=1$ and $\inf_{y\in Y}\norm{x-y}>1-\epsilon$.

(b) Use part (a) to prove that, if $X$ is an infinite dimensional normed vector space, then the unit ball of $X$ is not compact.
:::

::: {.solution}

The argument is the card's own, and its two gaps are filled: the distance from a point to a closed subspace is positive, and each finite-dimensional subspace used in (b) is closed. No retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $X$ be a normed vector space over $\RR$ or $\CC$ and $Y\le X$ a linear subspace; write $\operatorname{dist}(x,Y)=\inf_{y\in Y}\norm{x-y}$.

::: pf

::: {.pf-step #distance}
If $Y$ is closed and $x\notin Y$, then $d=\operatorname{dist}(x,Y)>0$.

::: pf-proof
The infimum $d\ge0$ is finite. If $d=0$ there are $y_{n}\in Y$ with $\norm{x-y_{n}}<1/n$, so $y_{n}\to x$; a closed subspace contains the limit of every convergent sequence of its points, so $x\in Y$, contrary to the hypothesis. Hence $d>0$.
:::

:::

::: {.pf-step #riesz}
(a) For every $\varepsilon\in(0,1)$ there is $u\in X$ with $\norm{u}=1$ and $\operatorname{dist}(u,Y)>1-\varepsilon$.

::: pf-proof

::: {.pf-step #choice}
Choose $\delta>0$ with $\dfrac{d}{d+\delta}>1-\varepsilon$ and $y_{0}\in Y$ with $\norm{x-y_{0}}<d+\delta$.

::: pf-proof
Since $1-\varepsilon<1$ and $d>0$ by step [](#distance){.pf-ref}, the inequality $\frac{d}{d+\delta}>1-\varepsilon$ holds for all small enough $\delta>0$, because $\frac{d}{d+\delta}\to1$ as $\delta\to0^{+}$. As $d=\inf_{y\in Y}\norm{x-y}$, some $y_{0}\in Y$ has $\norm{x-y_{0}}<d+\delta$, the infimum being approached within $\delta$.
:::

:::

::: {.pf-step #unit}
$u=\dfrac{x-y_{0}}{\norm{x-y_{0}}}$ has $\norm{u}=1$ and $\operatorname{dist}(u,Y)=\dfrac{d}{\norm{x-y_{0}}}>1-\varepsilon$.

::: pf-proof
$x-y_{0}\ne0$ because $x\notin Y$ and $y_{0}\in Y$, so $\norm{x-y_{0}}>0$ and $\norm{u}=1$. For $y\in Y$,
$$
\norm{u-y}=\frac{1}{\norm{x-y_{0}}}\norm{x-y_{0}-\norm{x-y_{0}}\,y},
$$
and $y\mapsto\norm{x-y_{0}}\,y$ is a bijection of $Y$ onto $Y$, so the infimum over $y\in Y$ of the right side is $\operatorname{dist}(x,Y)/\norm{x-y_{0}}$. By step [](#choice){.pf-ref} the denominator is less than $d+\delta$, so the quotient exceeds $\frac{d}{d+\delta}>1-\varepsilon$.
:::

:::

:::

:::

::: {.pf-step #separated}
(b) If $X$ is infinite dimensional there are $x_{n}$ of norm $1$ with $\norm{x_{n}-x_{m}}>\tfrac12$ for $n\ne m$.

::: pf-proof
Define $x_{1}$ as any element of norm $1$. Suppose $x_{1},\ldots,x_{n-1}$ are defined and let $Y_{n}=\operatorname{span}\{x_{1},\ldots,x_{n-1}\}$, a finite-dimensional linear subspace; it is closed, since every finite-dimensional subspace of a normed space is closed, and it is a proper subspace because $X$ is infinite dimensional. Apply step [](#riesz){.pf-ref} with $\varepsilon=\tfrac12$ to get $x_{n}\in X$ with $\norm{x_{n}}=1$ and $\operatorname{dist}(x_{n},Y_{n})>\tfrac12$. For $m<n$ one has $x_{m}\in Y_{n}$, so $\norm{x_{n}-x_{m}}\ge\operatorname{dist}(x_{n},Y_{n})>\tfrac12$. The recursion gives the sequence.
:::

:::

::: {.pf-step #not-compact}
(b) The closed unit ball of an infinite-dimensional normed space is not compact.

::: pf-proof
Let $B=\{x:\norm{x}\le1\}$. The sequence of step [](#separated){.pf-ref} lies in $B$ and satisfies $\norm{x_{n}-x_{m}}>\tfrac12$ for all $n\ne m$, so it has no Cauchy subsequence and hence no convergent subsequence: a subsequence converging to some $x$ would be Cauchy, so its terms would satisfy $\norm{x_{n}-x_{m}}<\tfrac12$ for all large $m,n$ in its index set, which the separation forbids. But $X$ is a metric space, and a compact metric space is sequentially compact (Theorem 28.2), so if $B$ were compact the sequence would have a convergent subsequence. Therefore $B$ is not compact.
:::

:::

:::
:::
