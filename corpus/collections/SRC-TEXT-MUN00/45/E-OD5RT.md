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
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Math StackExchange 1287635, "countable product of
    totally bounded space is totally bounded" (2015-05-18), has Brian M. Scott's answer 1288761
    proving the first part of this exercise for the metric d(x,y) = sum_k 2^{-k} \bar d_k(x_k,y_k)
    rather than the D = sup_i \bar d_i(x_i,y_i)/i that Munkres uses here: the first finitely many
    coordinates are covered by finite eps/2-nets and the tail is pinned at one point, which in
    Munkres' D needs the factor 1/i and the choice of m with 1/m < eps/2 in place of Scott's
    choice of m with 2^{-m} < eps/4. The answer says nothing of the exercise's second part, the
    compactness of a countable product of compact metrizable spaces; so the page is a model for
    the first part and not a solution of the exercise, and it is not transcribed. dbFin has no
    chapter-7 page (404, checked 2026-11-15), and no GitHub Munkres repository named in the
    COMPLAINTS.md entry for §30--§36 reaches Chapter 7. The card keeps its own proof, which this
    pass did not re-read; the search is recorded in the COMPLAINTS.md entry for §43--§50 with
    every query.

- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    The AoPS blog post by cinnamon_e, "Topology by Munkres Chapter 7 | Day 16" (2025-09-09, listed
    on the blog's topology tag page
    https://artofproblemsolving.com/community/c3401823t440f3401823_topology, text at
    tmp/sources/aops-shooting-star-munkres-ch7-day16.md), also answers this exercise, at its item 1
    of §45. The text is held, but the formulas are not: the extraction drops every inline formula,
    so the answer reads as the words between blanks and cannot be transcribed or checked. It is
    recorded here and in the COMPLAINTS.md entry for §43--§50 as located with its formulas
    unreadable, the site answering an automated request with a Cloudflare human check, which is not
    worked around.

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
