---
schema: qual/card@1
id: PR-L35O7
kind: proposition
title: $L^p$ spaces are Banach
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Completeness
  - Norms
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mathcal M,\mu)$ be a measure space and let $1\le p\le\infty$. Then $L^p(X,\mu)$, modulo equality almost everywhere and equipped with its usual $L^p$ norm, is a Banach space.
:::

::: {.proof}
First suppose $1\le p<\infty$, and let $(f_n)$ be Cauchy in $L^p$. Choose a subsequence $(f_{n_k})$ such that
\[
\|f_{n_{k+1}}-f_{n_k}\|_p\le 2^{-k}
\qquad(k\ge1).
\]
Set
\[
g_k=|f_{n_{k+1}}-f_{n_k}|,
\qquad
S_N=\sum_{k=1}^N g_k.
\]
Minkowski's inequality gives
\[
\|S_N\|_p\le\sum_{k=1}^N2^{-k}\le1.
\]
Since $S_N\uparrow S:=\sum_{k\ge1}g_k$, monotone convergence yields
\[
\int_X S^p\,d\mu
=\lim_{N\to\infty}\int_X S_N^p\,d\mu
\le1.
\]
Thus $S<\infty$ almost everywhere. Outside a null set, the numerical series
\[
\sum_{k\ge1}\bigl(f_{n_{k+1}}(x)-f_{n_k}(x)\bigr)
\]
is absolutely convergent; define its limit by $f(x)-f_{n_1}(x)$ there, and define $f$ arbitrarily on the exceptional null set.

For every $k$ and $N>k$,
\[
|f_{n_N}-f_{n_k}|
\le\sum_{j=k}^{N-1}g_j.
\]
Letting $N\to\infty$ pointwise and applying Fatou together with Minkowski gives
\[
\|f-f_{n_k}\|_p
\le\sum_{j=k}^{\infty}\|g_j\|_p
\le\sum_{j=k}^{\infty}2^{-j}
=2^{1-k}.
\]
Hence $f_{n_k}\to f$ in $L^p$. Because the original sequence is Cauchy, for every $\varepsilon>0$ choose $k$ large enough that $\|f_{n_k}-f\|_p<\varepsilon/2$ and then $N$ so large that $\|f_n-f_{n_k}\|_p<\varepsilon/2$ for all $n\ge N$. Therefore $f_n\to f$ in $L^p$.

Now let $p=\infty$. Again choose a subsequence satisfying
\[
\|f_{n_{k+1}}-f_{n_k}\|_\infty\le2^{-k}.
\]
For each $k$ there is a null set $N_k$ outside which
\[
|f_{n_{k+1}}-f_{n_k}|\le2^{-k}.
\]
Outside the null set $N=\bigcup_kN_k$, the series of successive differences converges uniformly by the Weierstrass $M$-test. Hence $(f_{n_k})$ converges uniformly on $X\setminus N$ to some bounded measurable function $f$, after defining $f$ arbitrarily on $N$, and
\[
\|f-f_{n_k}\|_\infty\le2^{1-k}.
\]
As above, Cauchyness of the full sequence then implies $f_n\to f$ in $L^\infty$.

Thus $L^p(X,\mu)$ is complete for every $1\le p\le\infty$.
:::
