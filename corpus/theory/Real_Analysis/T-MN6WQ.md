---
schema: qual/card@1
id: T-MN6WQ
kind: theorem
title: Interchanging sums and integrals for absolutely summable series
slogan: 'Absolute $L^1$ summability gives almost-everywhere convergence and lets summation commute with integration.'
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Series of Functions
  - L¹
relations: []
review: draft
---

::: {.theorem}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space and let $f_n\colon X\to\CC$ for $n\geq1$ be [[D-DHFN4|measurable]].

(a) The two quantities
$$
\sum_{n=1}^\infty \int_X \abs{f_n}\dmu \quad\text{and}\quad \int_X\sum_{n=1}^\infty \abs{f_n}\dmu
$$
are equal in $[0,\infty]$.
More generally, $\int_X\sum_n g_n\dmu=\sum_n\int_X g_n\dmu$ in $[0,\infty]$ for any $g_n\in$ [[D-BF5L2|$L^+$]] [@Fol13].

(b) If $\sum_{n}\norm{f_n}_1<\infty$, then $\sum_{n}f_n(x)$ converges absolutely for almost every $x$, its sum $F$, defined almost everywhere, lies in $L^1(X,\mu)$, and
$$
\norm{F-\sum_{n=1}^N f_n}_1 \convergesto{N\to\infty} 0,
\qquad
\int_X F\dmu = \sum_{n=1}^\infty \int_X f_n\dmu .
$$
:::

::: {.proof}
The partial sums $\sum_{n=1}^N g_n$ are nonnegative, measurable, and increase pointwise to $\sum_n g_n$, so the monotone convergence theorem gives (a); take $g_n=\abs{f_n}$ for the first statement.

For (b), let $S\coloneqq\sum_n\abs{f_n}$.
By (a), $\int_X S\dmu=\sum_n\norm{f_n}_1<\infty$.
The set $A\coloneqq\theset{S=\infty}$ is measurable, and $S\geq t\,\one_A$ for every $t>0$, so $t\,\mu(A)\le\int_X S\dmu$; letting $t\to\infty$ gives $\mu(A)=0$.
Off $A$ the series $\sum_n f_n(x)$ converges absolutely, and $\abs{F}\le S$, so $F\in L^1$.
The remainders satisfy $\abs{F-\sum_{n\le N}f_n}\le\sum_{n>N}\abs{f_n}\le S$ and tend to $0$ off $A$, so the [[T-IJQQG|dominated convergence theorem]] gives $\norm{F-\sum_{n\le N}f_n}_1\to0$.
Since $\abs{\int_X F\dmu-\sum_{n\le N}\int_X f_n\dmu}\le\norm{F-\sum_{n\le N}f_n}_1$, the integrals converge as well.
:::

::: {.remark title="Proof by Fubini--Tonelli on $X\times\NN$"}
Let $\nu$ be counting measure on $\NN$ and $F(x,n)\coloneqq f_n(x)$, which is measurable for the product $\sigma$-algebra since $F^{-1}(B)=\bigcup_n f_n^{-1}(B)\times\theset{n}$.
The two sides of (b) are the two iterated integrals of $F$.
For each $n$ and $k\geq1$, $\mu\qty{\theset{\abs{f_n}>1/k}}\le k\norm{f_n}_1<\infty$, so every $f_n$ vanishes outside $A\coloneqq\bigcup_n\theset{f_n\neq0}$, on which $\mu$ is $\sigma$-finite; replacing $X$ by $A$ changes neither side.
By Tonelli's theorem, $\int_{A\times\NN}\abs{F}\,d(\mu\times\nu)=\sum_n\norm{f_n}_1<\infty$, so $F\in L^1(A\times\NN)$, and Fubini's theorem gives that $\sum_n\abs{f_n(x)}<\infty$ for almost every $x$ and that the iterated integrals agree.

With counting measure on $\NN\times\NN$, the same argument shows that $\sum_{m,n} \int_X \abs{f_{m,n}}\dmu < \infty$ justifies interchanging a double sum with the integral.
:::
