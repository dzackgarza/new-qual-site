---
schema: qual/card@1
id: P-WESRA04-P6
kind: problem
title: Completeness of $L^\infty$
classification:
  areas: [real-analysis]
  topics: [Function Spaces, Banach Spaces]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis section 2.3, problem 6 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Prove that $L^\infty(X,\mathcal B,\mu)$ is complete in the $L^\infty$ norm.
:::

::: solution
Let $(f_n)$ be Cauchy in $L^\infty$.
Choose a subsequence $(f_{n_k})$ such that
\[
\|f_{n_{k+1}}-f_{n_k}\|_\infty<2^{-k}
\qquad(k\ge1).
\]
For each $k$, there is a null set $N_k$ outside which
\[
|f_{n_{k+1}}(x)-f_{n_k}(x)|\le2^{-k}.
\]
Let
\[
N=\bigcup_{k=1}^\infty N_k.
\]
Then $\mu(N)=0$.
For $x\notin N$ and $m>k$,
\[
|f_{n_m}(x)-f_{n_k}(x)|
\le\sum_{j=k}^{m-1}2^{-j}
\le2^{1-k}.
\]
Thus $(f_{n_k})$ is uniformly Cauchy on $X\setminus N$.
Define
\[
f(x)=\lim_{k\to\infty}f_{n_k}(x)
\quad(x\notin N),
\qquad
f(x)=0
\quad(x\in N).
\]
Then $f$ is measurable.
Moreover, for $x\notin N$,
\[
|f(x)-f_{n_k}(x)|\le2^{1-k},
\]
so
\[
\|f-f_{n_k}\|_\infty\le2^{1-k}\longrightarrow0.
\]
In particular $f\in L^\infty$.

Finally, since the original sequence $(f_n)$ is Cauchy, given $\varepsilon>0$ choose $N_0$ such that
\[
m,n\ge N_0\quad\Longrightarrow\quad
\|f_m-f_n\|_\infty<\varepsilon/2.
\]
Choose $k$ with $n_k\ge N_0$ and
\[
\|f_{n_k}-f\|_\infty<\varepsilon/2.
\]
Then for every $n\ge N_0$,
\[
\|f_n-f\|_\infty
\le\|f_n-f_{n_k}\|_\infty+\|f_{n_k}-f\|_\infty
<\varepsilon.
\]
Hence $f_n\to f$ in $L^\infty$, and therefore
\[
\boxed{L^\infty(X,\mathcal B,\mu)\text{ is Banach}.}
\]
:::
