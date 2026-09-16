---
schema: qual/card@1
id: PR-L35O7
kind: proposition
title: $L^p$ spaces are Banach spaces
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
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure space]] and let $1\leq p\leq\infty$.
Then $L^p(X,\mu)$, whose elements are classes of functions modulo equality $\mu$-almost everywhere, with the norm $\norm{\cdot}_p$, is a [[D-BG455|Banach space]].
:::

::: {.proof}
First let $1\leq p<\infty$, and let $(f_n)$ be Cauchy in $L^p$.
Choose a subsequence $(f_{n_k})$ such that
$$
\norm{f_{n_{k+1}}-f_{n_k}}_p\leq 2^{-k}
\qquad(k\geq1).
$$
Set
$$
g_k\coloneqq\abs{f_{n_{k+1}}-f_{n_k}},
\qquad
S_N\coloneqq\sum_{k=1}^N g_k.
$$
Minkowski's inequality gives
$$
\norm{S_N}_p\leq\sum_{k=1}^N2^{-k}\leq1.
$$
Since $S_N\uparrow S\coloneqq\sum_{k\geq1}g_k$, the monotone convergence theorem yields
$$
\int_X S^p\dmu
=\lim_{N\to\infty}\int_X S_N^p\dmu
\leq1.
$$
Thus $S<\infty$ almost everywhere.
Outside a null set, the series
$$
\sum_{k\geq1}\big(f_{n_{k+1}}(x)-f_{n_k}(x)\big)
$$
converges absolutely; there, define $f(x)$ so that this sum equals $f(x)-f_{n_1}(x)$, and put $f\coloneqq0$ on the exceptional null set.

For every $k$ and $N>k$,
$$
\abs{f_{n_N}-f_{n_k}}
\leq\sum_{j=k}^{N-1}g_j.
$$
Letting $N\to\infty$ and applying Fatou's lemma together with Minkowski's inequality gives
$$
\norm{f-f_{n_k}}_p
\leq\sum_{j=k}^{\infty}\norm{g_j}_p
\leq\sum_{j=k}^{\infty}2^{-j}
=2^{1-k}.
$$
Hence $f_{n_k}\to f$ in $L^p$.
Given $\varepsilon>0$, choose $k$ with $\norm{f_{n_k}-f}_p<\varepsilon/2$ and $n_k\geq N$, where $N$ is such that $\norm{f_n-f_m}_p<\varepsilon/2$ for all $m,n\geq N$.
Then $\norm{f_n-f}_p<\varepsilon$ for all $n\geq N$, so $f_n\to f$ in $L^p$.

Now let $p=\infty$, and again choose a subsequence with
$$
\norm{f_{n_{k+1}}-f_{n_k}}_\infty\leq2^{-k}.
$$
For each $k$ there is a null set $Z_k$ outside which
$$
\abs{f_{n_{k+1}}-f_{n_k}}\leq2^{-k}.
$$
Outside the null set $Z\coloneqq\bigcup_kZ_k$, the series of successive differences converges uniformly by the Weierstrass $M$-test.
Hence $(f_{n_k})$ converges uniformly on $X\setminus Z$ to a bounded measurable function $f$, extended by $0$ on $Z$, and
$$
\norm{f-f_{n_k}}_\infty\leq2^{1-k}.
$$
As in the case $p<\infty$, since $(f_n)$ is Cauchy, $f_n\to f$ in $L^\infty$.
:::
