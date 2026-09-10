---
schema: qual/card@1
id: E-OD5RT
kind: problem
title: Countable products of compact metrizable spaces are compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
---

::: {.exercise}

If $X_n$ is metrizable with metric $d_n$, then

$$
D(\mathbf{x}, \mathbf{y}) = \sup\ts{\bar{d}_i(x_i, y_i)/i}
$$

is a metric for the product space $X = \prod X_n$.
Show that $X$ is totally bounded under $D$ if each $X_n$ is totally bounded under $d_n$.
Conclude without using the Tychonoff theorem that a countable product of compact metrizable spaces is compact.
:::

::: {.solution}
Fix $\varepsilon>0$. Choose $N$ so large that $1/(N+1)<\varepsilon$. For each $1\le i\le N$, total boundedness of $(X_i,d_i)$ (equivalently of $(X_i,\bar d_i)$) gives a finite $\varepsilon i$-net $F_i\subset X_i$ for $\bar d_i$ (if $\varepsilon i\ge1$, one point suffices). Choose arbitrary basepoints $a_i\in X_i$ for $i>N$. The finite set
\[
F=F_1\times\cdots\times F_N\times\prod_{i>N}\{a_i\}
\]
is an $\varepsilon$-net for $X$: given $x$, choose $y_i\in F_i$ with $\bar d_i(x_i,y_i)<\varepsilon i$ for $i\le N$ and put $y_i=a_i$ afterwards. Then for $i>N$,
\[
\bar d_i(x_i,y_i)/i\le1/i<\varepsilon,
\]
so $D(x,y)<\varepsilon$. Thus $(X,D)$ is totally bounded.

If every $X_i$ is compact, each is complete. A $D$-Cauchy sequence is Cauchy in every coordinate because $\bar d_i(x_i,y_i)\le iD(x,y)$; hence it converges coordinatewise to some $x\in X$. The same finite-head/tail estimate shows convergence in $D$, so $X$ is complete. A complete totally bounded metric space is compact. Hence the countable product of compact metrizable spaces is compact, without invoking Tychonoff.
:::
