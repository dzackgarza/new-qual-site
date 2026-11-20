---
schema: qual/card@1
id: E-ML7VU
kind: problem
title: The topologist's sine curve has dimension one
classification:
  areas:
  - topology
  topics:
  - Dimension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution was located; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00.
    Checked against Munkres, Topology (2000), §50 Exercise 3, printed p. 315, with Example 2 (the interval has
    dimension 1), Corollary 50.3 and Theorem 50.1 for the pieces, and the card of Exercise 50.2 for the lower
    bound. What the card cannot do with the book alone: the decomposition of the sine curve into the closed arcs
    A_n and the closed vertical interval is countable, and the book proves only the finite closed-sum theorem
    (Theorem 50.2); the passage to countably many closed pieces is the countable closed-sum theorem of dimension
    theory, which the card states, cites by author and title (Engelking, Theory of Dimensions Finite and
    Infinite, Theorem 1.5.3; Hurewicz and Wallman, Dimension Theory) and does not prove. Neither book is in the
    checkout and no page of either has been read here, so the citation is by theorem number only, and the card is
    listed in COMPLAINTS.md as the one card of this batch whose proof rested on a borrowed theorem rather than on
    the book; both that citation and the entry for it are withdrawn later on the same day, and the event that
    follows records the direct proof from the book.
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    The earlier note on this card cited the countable closed-sum theorem of dimension theory by author and
    theorem number (Engelking, Theory of Dimensions Finite and Infinite, Theorem 1.5.3; Hurewicz and
    Wallman, Dimension Theory) without a page, because neither book is in the checkout and the archive.org
    copies of the second are access-restricted. A citation that was not read on its page certifies nothing,
    so it is withdrawn and the bound dim S-bar <= 1 is now proved directly from the book: the definition of
    order, refinement and topological dimension on printed p. 305, Theorem 20.3 (the square metric gives the
    usual topology of R^2), Theorem 27.3 (S-bar is a closed bounded subset of R^2, hence compact), the
    Lebesgue number lemma (Lemma 27.5), and the continuity of x -> sin(1/x) used by the book itself in
    Example 3 of §18 and Example 7 of §24. The construction, for an arbitrary open cover and a Lebesgue
    number delta: near the segment take the sets W(I) = S-bar meet {y in I} meet {x < eta}, where the
    intervals I cover [-1,1] with multiplicity at most two, exactly one of them meeting any point whose
    second coordinate is within sigma of y_0 = sin(1/eta); away from the segment take the spiral slabs C_k = S-bar meet {s_k < x < s_{k+1}} meet
    {|y - sin(1/x)| < delta/16} and the seam pieces D_j = S-bar meet {|x - s_j| < nu} meet
    {|y - sin(1/s_j)| < delta/64}; every member has diameter below delta under the square metric (for the
    slabs by the mean value theorem, |sin a - sin a'| <= |a - a'|, and |1/x - 1/x'| <= l/eta^2) and no point
    lies in more than two members, the three cases x < eta, x = s_j and s_k < x < s_{k+1} being checked
    separately. The lower bound dim S-bar >= 1 is the card of Exercise 50.2, with connectedness from
    Example 7 of §24. The construction was also checked numerically for several values of delta: the
    parameters used give no uncovered sampled point, maximum multiplicity 2, and a largest sampled
    coordinate spread below delta.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Math StackExchange 2480896, "Topological dimension of
    topologist's sine curve and general question about topological dimension" (2017-10-20), is this exercise,
    and its only answer, by Alex Ravsky (2017-10-31), kept at tmp/sources/mse-2480896-munkres-50-3.md, does not
    give a proof at the level of the book: it points to the sum theorem for closed subspaces in Engelking's
    *Dimension Theory* (1.5.3) as a way to get the dimension, and says of the asker's construction only that a
    refinement problem can occur at points of the curve that lie in the closure of two squares of the cover of
    the vertical segment. Engelking's theorem is not in Munkres, so nothing of that answer is transcribed; the
    card's construction is its own, made from the Lebesgue number of the cover, a cover of the vertical segment
    of order 2 and a mesh small enough that the curve crosses the vertical strip in disjoint pieces. The AoPS
    post *Topology by Munkres Chapter 8 | Day 18* (https://artofproblemsolving.com/community/c3401823h3647630)
    answers §50 as well, with its formulas lost; Murayama, dbFin and the ten GitHub repositories listed in
    COMPLAINTS.md have no Chapter 8. Nothing on the card needed correction.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Re-read on issue #144. Step 3 branched on $L\ge\delta/16$ and asked for an integer $q$ strictly between
    $16L/\delta$ and $32L/\delta$; at $L=\delta/16$ that is the interval $(1,2)$, which contains no integer,
    and the justification offered, that the interval has length at least 1, is not enough for an open interval.
    The branch is now taken only for $L>\delta/16$, where the interval has length greater than 1 and does
    contain an integer, and the case $L\le\delta/16$ is the single interval $q=1$. The mesh bound is stated as
    $m\le\delta/16$, the length of $J_k$ as $m+\delta/64\le5\delta/64<\delta/8$, and the disjointness of
    $J_k$, $J_l$ for $\abs{k-l}\ge2$ is drawn from $m>\delta/64$, which holds only when $q\ge2$ and can fail at
    $q=1$, where no two such indices exist. Nothing else on the card changed.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    A reader of this card reported that the construction of the cover of [-1, 1] fails at L = 0, where
    y_0 - 2 sigma = -1: the point -1 then lies outside I_0 = (y_0 - 2 sigma, y_0 + 2 sigma), which is open,
    and no J_k is built, the card having branched on L > 0. Step 3 now writes L = y_0 - 2 sigma + 1,
    observes that for L < 0 no point of [-1, 1] lies below y_0 - 2 sigma and -1 lies in I_0, and takes the
    partition for L >= 0, with the single interval of the case L <= delta/16 degenerate at L = 0, where
    b_0 = b_1 = -1 and J_1 contains -1. The upper side is covered "the same way", which now includes its
    own degenerate case. Nothing else on the card changed.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose in six headed steps with no `pf` structure. It
    is now a `pf` with nine steps, the interval construction carried as a sub-step of the near-cover
    step, and every step carrying a `pf-proof`. Cited by numbered statement only: Munkres, Topology,
    §50 Exercise 3, the definition of topological dimension in §50, Lemma 27.5 (the Lebesgue number
    lemma), Theorem 27.3 (Heine--Borel), Theorem 20.3 (the square metric induces the usual topology),
    Example 3 of §18 and Example 7 of §24, with §50 Exercise 2 on [[E-KWBI9]] for the lower bound. No
    retained published set answers this exercise, and the card says so in its preamble: the sets
    searched are the ones recorded in the COMPLAINTS.md entry for §43--§50, and the Chapter 7
    self-study notes state the exercise without answering it. Checked: that the Lebesgue number
    applies to a cover of the compact space, the four consequences listed for the constants, the
    disjointness and the length bound of the $J_k$ in the interval sub-step including the case
    $L=0$, the two diameter estimates with the mean value theorem and $\abs{1/x-1/x'}\le\ell/\eta^2$,
    and the three cases of the order-two count.
---

::: {.exercise}

Show that the topologist's sine curve has dimension 1.
:::

::: {.solution}

No retained published solution of Munkres, *Topology*, §50 Exercise 3 was located: the sets searched are listed in the `COMPLAINTS.md` entry for §43--§50 of `SRC-TEXT-MUN00`, and the self-study notes that reach Chapter 7 state this exercise without answering it. The proof is the card's own, checked against the numbered statements it cites: the definition of topological dimension in §50, Lemma 27.5 (the Lebesgue number lemma), Theorem 27.3 (Heine--Borel), Theorem 20.3 (the square metric induces the usual topology) and Example 7 of §24.

::: pf

::: {.pf-step #setup}
Let $S=\{(x,\sin(1/x)):0<x\le1\}$, $V=\{0\}\times[-1,1]$ and $\bar S=S\cup V$, the topologist's sine curve of Munkres, Example 7 of §24, with the metric $\rho$ it inherits from the square metric of $\RR^2$, which induces the usual topology.

::: pf-proof
Example 7 of §24 defines the space as this union, so the set is as displayed. The square metric induces the usual topology of $\RR^2$ by Munkres, Theorem 20.3, so the subspace metric $\rho$ induces the subspace topology and the diameters computed below are diameters for the topology of $\bar S$.
:::

:::

::: {.pf-step #criterion}
It is enough to produce, for an arbitrary open cover $\mathcal A$ of $\bar S$, an open cover of $\bar S$ refining it in which no point lies in more than two members.

::: pf-proof
Munkres, §50 defines $\dim X\le n$ to mean that every open cover of $X$ has an open refinement of order at most $n+1$, that is, one in which no point lies in more than $n+1$ members. With $n=1$ this is exactly the requirement stated, and $\dim\bar S\le1$ follows once it holds for every $\mathcal A$.
:::

:::

::: {.pf-step #compact-lebesgue}
$\bar S$ is compact and, for the given cover $\mathcal A$, there is $\delta>0$ such that every subset of $\bar S$ of diameter less than $\delta$ lies in a member of $\mathcal A$.

::: pf-proof
$\bar S\subseteq[0,1]\times[-1,1]$ is bounded and closed in $\RR^2$, so it is compact by Munkres, Theorem 27.3 (Heine--Borel); note that a cover of $\bar S$ by sets open in $\bar S$ is a cover of the compact space $\bar S$. The number $\delta$ is then supplied by Munkres, Lemma 27.5 (the Lebesgue number lemma, which is stated for a compact metric space and an open cover of it).
:::

:::

::: {.pf-step #constants}
Choose reals
$$
0<\eta\le\tfrac12,\quad \eta<\frac{\delta}{8},\qquad \rho_0=\frac{\delta}{16},\qquad \sigma=\frac{\delta}{64},\qquad 0<\ell<\min\Bigl\{\frac{\delta}{8},\ \frac{\delta\eta^2}{16}\Bigr\},\qquad \nu=\min\Bigl\{\frac{\delta}{32},\ \frac{\ell}{4},\ \frac{\eta}{2}\Bigr\}.
$$
Then $\eta<\delta$, $2\nu\le\ell/2<\delta$, $2\sigma<\delta$, $4\nu\le\ell$ and $\ell/\eta^2<\delta/16$.

::: pf-proof
Each of $\eta,\ell,\nu$ is required only to be a positive number below finitely many positive bounds, so the choices are possible. The listed consequences follow by the displayed definitions: $\eta<\delta/8<\delta$; $2\nu\le2\cdot\ell/4=\ell/2<\delta/2$; $2\sigma=2\delta/64=\delta/32<\delta$; $4\nu\le4\cdot\ell/4=\ell$; and $\ell<\delta\eta^2/16$ says $\ell/\eta^2<\delta/16$.
:::

:::

::: {.pf-step #near-cover}
Let $y_0=\sin(1/\eta)$. There are open intervals $I_1,\dots,I_p$ of $\RR$ covering $[-1,1]$, of order at most two, with $\abs{I_i}<\delta/2$, one of them $I_0=(y_0-2\sigma,y_0+2\sigma)$ and every other contained in $(-\infty,y_0-\sigma)$ or in $(y_0+\sigma,\infty)$; and then
$$
W(I)=\bar S\cap\{(x,y):y\in I\}\cap\{(x,y):x<\eta\}
$$
is open in $\bar S$, the family $\{W(I)\}$ covers every point of $\bar S$ with first coordinate below $\eta$, has diameter less than $\delta$, and no point of $\bar S$ lies in more than two of its members.

::: pf-proof

::: {.pf-step #intervals}
The intervals $I_i$ with those four properties exist.

::: pf-proof
Write $L=y_0-2\sigma+1$, so that $y_0-2\sigma=-1+L$. If $L<0$ no point of $[-1,1]$ lies below $y_0-2\sigma$ and nothing is needed on that side. If $L\ge0$ take $-1=b_0\le b_1\le\cdots\le b_q=y_0-2\sigma$ with consecutive points at distance $m\le\delta/16$, equal only when $L=0$: if $L>\delta/16$ choose an integer $q$ with $16L/\delta<q<32L/\delta$, possible because that interval has length $16L/\delta>1$, and put $b_k=-1+kL/q$, so that $m=L/q\in(\delta/32,\delta/16)$; if $0\le L\le\delta/16$ take $q=1$, so that $m=L\le\delta/16$, the interval being degenerate when $L=0$. Put $J_k=(b_{k-1}-\delta/128,\ b_k+\delta/128)$; then $J_1$ contains $-1$ and $y_0-2\sigma$, and $J_k\cap J_l=\varnothing$ when $\abs{k-l}\ge2$, because for $q\ge2$ one has $m>\delta/64=2\delta/128$, so $b_{k+1}-\delta/128>b_k+\delta/128$, while for $q=1$ there is no pair of such indices. Each $J_k$ has length $m+\delta/64\le5\delta/64<\delta/8$, and each lies in $(-\infty,y_0-\sigma)$, its right end being at most $y_0-2\sigma+\delta/128=y_0-2\sigma+\sigma/2<y_0-\sigma$. Covering $[y_0+2\sigma,1]$ the same way when it is nonempty, with the roles of $y_0-\sigma$ and $y_0+\sigma$ exchanged, and adding $I_0=(y_0-2\sigma,y_0+2\sigma)$ gives the family: the $J$'s cover $[-1,1]$ outside $(y_0-2\sigma,y_0+2\sigma)$, they are pairwise disjoint except for consecutive ones, so no point lies in more than two, and every one of them misses $(y_0-\sigma,y_0+\sigma)$ while $I_0$ lies inside it, so a point with $\abs{y-y_0}<\sigma$ lies in $I_0$ alone.
:::

:::

::: {.pf-step #near-properties}
Each $W(I)$ is open in $\bar S$, the family covers the points of $\bar S$ with $x<\eta$, each has diameter less than $\delta$ in the square metric, and no point of $\bar S$ lies in more than two of them.

::: pf-proof
$W(I)$ is the trace on $\bar S$ of $\{y\in I\}\cap\{x<\eta\}$, an open subset of $\RR^2$, so it is open in $\bar S$. A point of $\bar S$ with $x<\eta$ has its second coordinate in $[-1,1]$, hence in some $I$ by step [#intervals]{.pf-ref}, so it lies in that $W(I)$. A member's first coordinates lie in $[0,\eta]$ and its second coordinates in $I$, so its diameter in the square metric $\rho$ is $\max\{\eta,\abs{I}\}<\delta$, since $\eta<\delta/8$ and $\abs{I}<\delta/2$. A point of $\bar S$ lies in $W(I)$ only if its second coordinate lies in $I$, and that coordinate lies in at most two of the $I$'s; so it lies in at most two of the $W(I)$.
:::

:::

:::

:::

::: {.pf-step #far-cover}
Put $s_k=\eta+k\ell$ and take $N\ge1$ with $s_N\ge1$. For $k=0,\dots,N-1$ and $j=0,\dots,N$ let
$$
C_k=\bar S\cap\{s_k<x<s_{k+1}\}\cap\{\abs{y-\sin(1/x)}<\rho_0\},\qquad
D_j=\bar S\cap\{\abs{x-s_j}<\nu\}\cap\{\abs{y-\sin(1/s_j)}<\sigma\},
$$
deleting empty members. Each is open in $\bar S$, each has diameter less than $\delta$, and together they cover every point of $\bar S$ whose first coordinate is at least $\eta$.

::: pf-proof
The map $x\mapsto\sin(1/x)$ is continuous on $\{x>\eta/2\}\supseteq[0,1]\cap\{x\ge\eta\}$, since $x\mapsto1/x$ is continuous where $x\ne0$ and $\sin$ is continuous (Munkres, Example 3 of §18), and each displayed set is $\bar S$ meet an open subset of $\RR^2$ contained in that half-plane; so each is open in $\bar S$. For $C_k$ take two of its points $(x,y),(x',y')$; then $s_k<x,x'<s_{k+1}$ gives $\abs{x-x'}<\ell$, and with $x,x'\ge\eta$,
$$
\abs{y-y'}\le\abs{y-\sin(1/x)}+\abs{\sin(1/x)-\sin(1/x')}+\abs{\sin(1/x')-y'}<\rho_0+\frac{\abs{x-x'}}{xx'}+\rho_0\le2\rho_0+\frac{\ell}{\eta^2}<\frac{\delta}{8}+\frac{\delta}{16},
$$
using the mean value theorem for $\abs{\sin a-\sin a'}\le\abs{a-a'}$ and $\abs{1/x-1/x'}=\abs{x-x'}/xx'\le\ell/\eta^2$; so $\operatorname{diam}C_k\le\max\{\ell,3\delta/16\}<\delta$. For $D_j$ the first coordinates span less than $2\nu\le\ell/2<\delta$ and the second less than $2\sigma<\delta$, so its diameter is below $\delta$. For the cover, a point of $\bar S$ with $0<x\le1$ has $y=\sin(1/x)$, so it lies in $C_k$ when $s_k<x<s_{k+1}$ and in $D_j$ when $x=s_j$; there are no points of $\bar S$ with first coordinate at least $\eta$ other than these, since $\bar S$'s vertical part has first coordinate $0$.
:::

:::

::: {.pf-step #order-two}
No point of $\bar S$ lies in more than two members of the family consisting of the $W(I)$, the $C_k$ and the $D_j$.

::: pf-proof
Let $q=(x,y)\in\bar S$. If $x<\eta$ then $q$ lies in at most two of the $W(I)$ and in no $C_k$, and it lies in $D_j$ only if $\abs{x-s_j}<\nu$; for $j\ge1$ that needs $x>s_j-\nu\ge\eta+\ell-\nu>\eta$ because $\nu\le\ell/4$, so only $j=0$ can occur, and then $\abs{y-y_0}<\sigma$ puts $q$ in exactly one $W(I)$; so at most two members contain $q$. If $x=s_j$ for some $j$ then $q\in D_j$ and $q$ lies in no $C_k$ and in no $W(I)$, since $x\ge\eta$; exactly one member. If $s_k<x<s_{k+1}$ then $q\in C_k$, $q$ lies in no $W(I)$, and $q$ lies in $D_j$ only if $\abs{x-s_j}<\nu$, which for $4\nu\le\ell$ happens for at most one $j$; so at most two members.
:::

:::

::: {.pf-step #upper-bound}
$\dim\bar S\le1$.

::: pf-proof
The family of steps [#near-cover]{.pf-ref} and [#far-cover]{.pf-ref} is an open cover of $\bar S$ refining $\mathcal A$, since every member has diameter less than $\delta$ and therefore lies in a member of $\mathcal A$ by step [#compact-lebesgue]{.pf-ref}, and no point lies in more than two members by step [#order-two]{.pf-ref}. As $\mathcal A$ was arbitrary, the criterion of step [#criterion]{.pf-ref} gives $\dim\bar S\le1$.
:::

:::

::: {.pf-step #lower-bound}
$\dim\bar S\ge1$, and hence $\dim\bar S=1$.

::: pf-proof
$\bar S$ is connected by Munkres, Example 7 of §24, it is metrizable and hence $T_1$, and it has more than one point. A connected $T_1$ space with more than one point has dimension at least $1$, which is proved on [[E-KWBI9]] (Munkres §50 Exercise 2). With step [#upper-bound]{.pf-ref} this gives $\dim\bar S=1$.
:::

:::

:::

:::
