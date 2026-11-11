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
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §45 Exercise 1 (printed p. 280) was located; the sets searched are listed in
    the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against the book, with
    Exercise 20.3(b) for the metric D on the product, Theorem 45.1 (compact iff complete and totally
    bounded), Theorem 28.2 for sequential compactness and the definition of total boundedness in §45. The
    argument: for eps > 0 take N with 1/(N+1) < eps, choose finite eps*i-nets in the first N factors and
    arbitrary basepoints beyond, and the resulting finite set is an eps-net for D, because a coordinate
    beyond N contributes at most 1/i <= 1/(N+1) and a coordinate up to N contributes less than eps;
    then a D-Cauchy sequence is Cauchy in each coordinate, converges coordinatewise by compactness of the
    factors, and converges in D since all but finitely many coordinates contribute less than eps uniformly;
    so the product is complete and totally bounded, hence compact. The card's opening sentence covers the
    case of an empty factor, which makes the product empty and both claims vacuous.
---
::: {.exercise}

If $X_n$ is metrizable with metric $d_n$, then

$$
D(\mathbf{x}, \mathbf{y}) = \sup\theset{\bar{d}_i(x_i, y_i)/i}
$$

is a metric for the product space $X = \prod X_n$.
Show that $X$ is totally bounded under $D$ if each $X_n$ is totally bounded under $d_n$.
Conclude without using the Tychonoff theorem that a countable product of compact metrizable spaces is compact.
:::

::: {.solution}
If some $X_i$ is empty, the product is empty and both claims follow. Assume every factor is nonempty.

Fix $\varepsilon>0$. Choose $N$ so large that $1/(N+1)<\varepsilon$. For each $1\le i\le N$, total boundedness of $(X_i,d_i)$ (equivalently of $(X_i,\bar d_i)$) gives a finite $\varepsilon i$-net $F_i\subset X_i$ for $\bar d_i$. Choose arbitrary basepoints $a_i\in X_i$ for $i>N$. The finite set
$$
F=F_1\times\cdots\times F_N\times\prod_{i>N}\{a_i\}
$$
is an $\varepsilon$-net for $X$: given $x$, choose $y_i\in F_i$ with $\bar d_i(x_i,y_i)<\varepsilon i$ for $i\le N$ and put $y_i=a_i$ afterwards. Then for $i>N$,
$$
\bar d_i(x_i,y_i)/i\le1/i<\varepsilon,
$$
so $D(x,y)<\varepsilon$. Thus $(X,D)$ is totally bounded.

If every $X_i$ is compact, each is complete. A $D$-Cauchy sequence is Cauchy in every coordinate because $\bar d_i(x_i,y_i)\le iD(x,y)$; hence it converges coordinatewise to some $x\in X$. Given $\varepsilon>0$, choose $N$ with $1/(N+1)<\varepsilon$; the terms with $i>N$ in $D(x^{(k)},x)$ are at most $1/(N+1)$, and the finitely many terms with $i\le N$ are less than $\varepsilon$ for large $k$. So $x^{(k)}\to x$ in $D$, and $X$ is complete. A complete totally bounded metric space is compact. Hence the countable product of compact metrizable spaces is compact, without invoking Tychonoff.
:::
