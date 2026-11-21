---
schema: qual/card@1
id: E-QJXDP
kind: problem
title: Weak local connectedness at a point without local connectedness
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §25 Exercise 7, printed p. 162, with the figure
    and the hint; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 25.7, PDF pp. 9-10. A connected neighbourhood of p
    would have to contain every a_i, by spreading along the segments crossing a small ball;
    the sub-broom over the tail of the a_i is a path-connected set containing a
    neighbourhood of p. (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: source-checked
  by: claude
  date: 2026-11-18
  note: >-
    Two defects located, neither repaired in this pass, which is why the solution section
    still carries the retained set's argument. (1) The printed statement cannot hold. The
    definition in Exercise 6 of the same page, read at 600 dpi from the retained PDF
    (printed p. 162), is "for every neighborhood U of x, there is a connected subspace of X
    contained in U that contains a neighborhood of x"; the connected subspace then contains
    a neighbourhood of x, so it is itself a connected neighbourhood of x contained in U, and
    a space weakly locally connected at x is locally connected at x. The exercise asks for a
    space that is not locally connected at p and is weakly locally connected at p, so the
    printed conclusion is impossible under the printed definition, whatever the space.
    (2) The description of the space in the solution section, taken from the retained
    positron0802 solution, does not have the property the exercise asserts: with bristles
    running from (a_i,0) to (a_{i+1},r_j), choose epsilon with a_{N+1} < epsilon < a_N and
    delta no larger than a_{N+1}; every bristle meeting B(p,delta) has its foot of the form
    (a_i,0) with a_i <= a_{N+1} < epsilon, hence inside B(p,epsilon), so the component of p
    in the trace of B(p,epsilon) contains the whole trace of B(p,delta) and is a
    neighbourhood of p: that space is locally connected at p. The book draws Figure 25.1 and
    states no formula for the bristles, no retained set in the checkout describes them in
    words (the Whitman, 9beach and shenapse manuals have no occurrence of the broom), and
    the figure does not determine what the bristles attach to. The card is therefore left as
    it stands pending a description of the space that the figure settles; rewriting the
    proof alone would not repair it.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    The card rewritten as a structured proof, after the two defects recorded above. (1) The
    space: the book gives Figure 25.1 and no formula; the retained description (branches from
    (a_i,0) to (a_{i+1},r_j)) is discarded because it makes X locally connected at p, as the
    note above shows. The description now on the card is the one the figure shows, with the
    properties the proof uses stated: branches from (a_i,0) to (a_{i+j},r_j) with
    r_j decreasing to 0, branches meeting the axis only at their feet and having pairwise
    disjoint relative interiors, which is what lets a point of a branch have a ball meeting X
    only in that branch. (2) Part (b): the printed definition of weak local connectivity makes
    part (b) impossible for any space, so the proof is given for the standard notion, "for
    every neighbourhood U of p a connected subspace containing p and contained in U", and the
    card says so on its face. What was searched for a description and did not supply one:
    Wikipedia's "infinite broom" is a different space (segments from the origin to (1,1/n)
    with an interval on the axis); the Math StackExchange threads 2439096 and 4145547 discuss
    this exercise without stating the figure's geometry, and 4145547 records the same
    difficulty with the printed definition; the retained manuals (Whitman, 9beach, shenapse)
    contain no occurrence of the broom. The proof of (a): for epsilon in (0,a_1), delta in
    (0,epsilon) and j large, the point (a_{1+j},r_j) lies in B(p,delta) and is an endpoint of
    the branch from (a_1,0), whose foot is outside B(p,epsilon); so in any open neighbourhood
    V of p inside B(p,epsilon) the set V intersected with that branch is nonempty, open and
    closed in V and misses p, and V is disconnected. Part (b) is then the axis piece.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The two notes above of this date are withdrawn: the printed statement is not defective
    and the retained description of the space is not wrong. The error was mine, in the
    reading of "neighbourhood". Munkres fixes the term on printed p. 97: "U is a
    neighborhood of x" is short for "U is an open set containing x", and he explicitly
    rejects the other usage, under which a neighbourhood is any set containing an open set
    containing the point. Since a connected subspace containing an open set about x need not
    itself be open, weak local connectivity at x does not imply local connectivity at x, and
    Exercise 25.7 is consistent as printed. The card now uses the printed notions (p. 161 for
    local connectedness, p. 162 for weak local connectivity), restores the retained
    description of the broom and the retained tail sub-broom C = X intersect B(p,a_N) for
    part (b), which is connected because no branch straddles the radius a_N and contains the
    open set X intersect B(p,a_{N+1}), and proves part (a) through Theorem 25.3: for
    epsilon between consecutive a's the component of p in X intersect B(p,epsilon) is not
    open, since a point y of the axis with a_{N+1} < y_x < epsilon has, in every ball about
    it, points of the branch that straddles y_x + eta, whose foot lies outside the ball of
    radius epsilon, so those points lie in another component. What is not claimed: the
    retained source's own step for part (a), that a connected set meeting a connected
    neighbourhood lies in it, which is not valid as stated and is not used here.
---

::: {.exercise}

Consider the "infinite broom" $X$ pictured in Figure 25.1 of the text.
Show that $X$ is not locally connected at $p$, but is weakly locally connected at $p$.
[Hint: Any connected neighborhood of $p$ must contain all the points $a_i$.]
:::

::: {.solution}
The argument is the retained published solution, **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 25.7, PDF pp. 9--10** (`tmp/sources/munkres-solutions-positron-ch3.pdf`), with its description of the broom and its tail sub-broom for part (b); part (a) is proved here through Theorem 25.3 instead of the source's step about connected sets meeting a neighbourhood, and the earlier note on this card calling the printed statement defective is withdrawn.

The notions are the printed ones. *Weakly locally connected at $x$*: for every neighbourhood $U$ of $x$ there is a connected subspace of $X$ contained in $U$ that contains a neighbourhood of $x$ (§25 Exercise 6, printed p. 162). *Locally connected at $x$*: for every neighbourhood $U$ of $x$ there is a connected neighbourhood of $x$ contained in $U$ (§25, printed p. 161). And a neighbourhood is an open set containing the point: Munkres records the convention and rejects the other one, under which a neighbourhood is any set containing an open set containing the point (§17, printed p. 97). It follows that a connected subspace containing a neighbourhood of $x$ need not itself be a neighbourhood of $x$, so weak local connectivity at $x$ does not give local connectivity at $x$; that is why the exercise is not vacuous.

The space is the retained description of Figure 25.1: $p=(0,0)$; points $(a_i,0)$ on the axis with $a_1=1$ and $a_i$ strictly decreasing to $p$; the segment $L$ from $p$ to $(a_1,0)$; for each $i,j\ge1$ the segment $L_{i,j}$ from $(a_i,0)$ to $(a_{i+1},r_j)$, with $r_j>0$ and $r_j\downarrow0$; branches meet the axis only at their feet and have pairwise disjoint relative interiors; $X=L\cup\bigcup_{i,j}L_{i,j}$ as a subspace of $\RR^2$. The exercise is §25 Exercise 7 (printed p. 162).

::: pf

::: {.pf-step #not-locally}
(a) $X$ is not locally connected at $p$.

::: pf-proof
Suppose it were. By Theorem 25.3 (printed p. 161) a space is locally connected exactly when every component of every open set is open in it; so for the open set $U=X\cap B(p,\varepsilon)$, with $0<\varepsilon<1$ chosen so that no $a_i$ equals $\varepsilon$, the component $P$ of $p$ in $U$ would be open in $X$. It is not, and the point that witnesses this is any $y=(y_x,0)$ on the axis with $a_{N+1}<y_x<\varepsilon$, where $N$ is the index with $a_{N+1}<\varepsilon<a_N$: every ball about $y$ contains a point of $U$ outside $P$.

::: {.pf-step #straddling}
For $0<\eta<\varepsilon-y_x$ let $i$ be the index with $a_{i+1}<y_x+\eta\le a_i$. Then $a_i\ge a_N>\varepsilon$, and for $r_j$ small the branch $L_{i,j}$ meets the ball $B(y,\eta)$ in a point of $U$.

::: pf-proof
Since $y_x+\eta<\varepsilon<a_N\le a_i$ whenever $i\le N$, and $a_{i+1}<y_x+\eta\le a_i$ forces $a_i>a_{N+1}$, we get $i\le N$ and hence $a_i\ge a_N>\varepsilon$. The branch $L_{i,j}$ runs from $(a_i,0)$ to $(a_{i+1},r_j)$; the point of the branch whose first coordinate is $y_x$ lies between its endpoints because $a_{i+1}<y_x$ and $y_x<y_x+\eta\le a_i$, and its height there is $r_j\,(a_i-y_x)/(a_i-a_{i+1})$, which is less than $\eta$ for $r_j$ small. That point is in $B(y,\eta)$, and it lies in $U$ because its distance to $p$ is at most $y_x+\eta<\varepsilon$.
:::

:::

::: {.pf-step #outside}
Such a point lies outside $P$.

::: pf-proof
The branch $L_{i,j}$ meets the axis only at $(a_i,0)$, which is not in $U$ because $a_i>\varepsilon$, and its other endpoint $(a_{i+1},r_j)$ is not on the axis; dually every other branch meets $L_{i,j}$ only possibly at a foot, and all feet of $L_{i,j}$ lie outside $U$. So the set of points of $L_{i,j}$ lying in $U$ is both open and closed in $U$ — open because each of its points is an interior point of the branch, where a ball meets $X$ only in that branch, and closed because its closure in the branch is met by $U$ only in itself — and it does not contain $p$. Hence it is a union of components of $U$ different from $P$.
:::

:::

:::

:::

::: {.pf-step #weakly}
(b) $X$ is weakly locally connected at $p$.

::: pf-proof
Let $U$ be a neighbourhood of $p$; since $U$ is open and the balls about $p$ form a local base, $X\cap B(p,\varepsilon)\subset U$ for some $0<\varepsilon<1$. Choose $N$ with $a_N<\varepsilon$ and put
$$
C=X\cap B(p,a_N),
$$
the tail sub-broom. First $C$ is a neighbourhood of $p$ in the sense required: it contains $X\cap B(p,a_{N+1})$, an open set containing $p$. Next $C$ is connected: it is the union of the connected set $[0,a_N)\times\{0\}=L\cap C$ with the pieces $L_{i,j}\cap C$ for those branches that meet $C$, and each such piece meets $L\cap C$: for a branch with $a_i<a_N$ that is its foot $(a_i,0)$; for a branch with $a_i\ge a_N$ there is no piece at all, because every point of it has first coordinate at least $a_{i+1}$, and $a_{i+1}\ge a_N$ when $i\le N-1$ while for $i\ge N$ we have $a_i\le a_N$ and the branch lies in the case already treated — so no branch straddles the radius $a_N$. Hence $C$ is connected, $p\in C$, and $C\subset U$ because $a_N<\varepsilon$.
:::

:::

:::

:::
