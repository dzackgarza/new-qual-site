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
    No complete published solution of Munkres §45 Exercise 1 was located; the sets searched are listed in
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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with seven steps, each carrying a `pf-proof`: the empty-product case, the choice of $N$ and
    the finite nets, the $\varepsilon$-net and total boundedness, the coordinatewise convergence
    of a $D$-Cauchy sequence, the convergence in $D$, and the appeal to Theorem 45.1. The
    arguments are the card's own and the statement is unchanged. Cited by number only:
    Exercise 20.3(b) for the metric $D$ and the product topology, Theorem 28.2 for sequential
    compactness of a compact metric space, Theorem 45.1 (complete and totally bounded implies
    compact), and the definition of total boundedness in §45. One page citation in the earliest
    event is removed under the citation rule now in force.
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

::: pf

::: pf-step

If some $X_i$ is empty, the product is empty and both claims follow; assume every factor is nonempty.

::: pf-proof

A product with an empty factor is empty, and the empty metric space is totally bounded (the empty set is an $\varepsilon$-net for every $\varepsilon$) and compact (every open cover has the empty subcover). So the two assertions are trivial in that case, and the arguments below may choose basepoints in each factor.

:::

:::

::: pf-step

Fix $\varepsilon>0$ and choose $N$ with $1/(N+1)<\varepsilon$. For each $1\le i\le N$, total boundedness of $(X_i,d_i)$, equivalently of $(X_i,\bar d_i)$, gives a finite $\varepsilon i$-net $F_i\subset X_i$ for $\bar d_i$.

::: pf-proof

Such an $N$ exists because $1/(N+1)\to0$. On $X_i$ the metrics $d_i$ and $\bar d_i=\min(d_i,1)$ have the same Cauchy sequences and the same totally boundedness: a set is $\delta$-dense for $d_i$ if and only if it is $\delta$-dense for $\bar d_i$ whenever $\delta\le1$, and for $\delta>1$ the whole space is $\delta$-dense for $\bar d_i$. So total boundedness of $(X_i,d_i)$ supplies a finite $F_i$ with every point of $X_i$ within $\varepsilon i$ of it in $\bar d_i$.

:::

:::

::: pf-step

Choose basepoints $a_i\in X_i$ for $i>N$; then
$$
F=F_1\times\cdots\times F_N\times\prod_{i>N}\{a_i\}
$$
is finite, and for every $x\in X$ there is $y\in F$ with $D(x,y)<\varepsilon$.

::: pf-proof

$F$ is a product of finitely many finite sets and singleton factors, hence finite, and nonempty because every factor is nonempty. Given $x$, choose $y_i\in F_i$ with $\bar d_i(x_i,y_i)<\varepsilon i$ for $i\le N$, possible by step 2, and put $y_i=a_i$ for $i>N$; then $y\in F$. For $i\le N$ the $i$-th term of the supremum is below $\varepsilon$, and for $i>N$ it is $\bar d_i(x_i,y_i)/i\le1/i\le1/(N+1)<\varepsilon$; hence $D(x,y)\le\varepsilon$, and the bound is strict because all terms are.

:::

:::

::: pf-step

Thus $(X,D)$ is totally bounded.

::: pf-proof

Step 3 produces, for every $\varepsilon>0$, a finite $\varepsilon$-net $F$; that is the definition of total boundedness for the metric $D$ of Exercise 20.3(b).

:::

:::

::: pf-step

If every $X_i$ is compact then each is complete, and a $D$-Cauchy sequence is Cauchy in every coordinate because $\bar d_i(x_i,y_i)\le i\,D(x,y)$; hence it converges coordinatewise to some $x\in X$.

::: pf-proof

A compact metric space is complete: a Cauchy sequence has a convergent subsequence by compactness of the completion-free sequential compactness of metric spaces (Theorem 28.2), and a Cauchy sequence with a convergent subsequence converges. For the coordinate claim, $\bar d_i(x_i,y_i)/i\le D(x,y)$ gives $\bar d_i(x_i,y_i)\le iD(x,y)$, so a $D$-Cauchy sequence is $\bar d_i$-Cauchy for each $i$, hence $d_i$-Cauchy, hence convergent in $X_i$; the coordinatewise limits define a point $x$ of the product.

:::

:::

::: pf-step

Given $\varepsilon>0$ choose $N$ with $1/(N+1)<\varepsilon$; the terms with $i>N$ in $D(x^{(k)},x)$ are at most $1/(N+1)$, and the finitely many terms with $i\le N$ are below $\varepsilon$ for large $k$. So $x^{(k)}\to x$ in $D$, and $X$ is complete.

::: pf-proof

For $i>N$ every term satisfies $\bar d_i(x^{(k)}_i,x_i)/i\le1/i\le1/(N+1)$. For each of the finitely many $i\le N$ the coordinate sequence converges, so there is $k_i$ with $\bar d_i(x^{(k)}_i,x_i)<\varepsilon i$ for $k\ge k_i$; taking $k$ at least the maximum of the $k_i$ makes all $i\le N$ terms below $\varepsilon$ and hence $D(x^{(k)},x)<\varepsilon$. A Cauchy sequence with a limit is convergent, so every Cauchy sequence converges.

:::

:::

::: pf-step

A complete totally bounded metric space is compact, so the countable product of compact metrizable spaces is compact without invoking Tychonoff.

::: pf-proof

That is Theorem 45.1. Steps 4 and 6 give total boundedness and completeness of $(X,D)$, and $D$ induces the product topology by Exercise 20.3(b), so $X$ is compact in the product topology.

:::

:::

:::
:::
