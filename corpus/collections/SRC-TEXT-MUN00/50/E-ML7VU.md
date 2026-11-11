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
---

::: {.exercise}

Show that the topologist's sine curve has dimension 1.
:::

::: {.solution}
Let
$$
S=\{(x,\sin(1/x)):0<x\le1\},\qquad V=\{0\}\times[-1,1],\qquad \bar S=S\cup V
$$
be the topologist's sine curve, as in Example 7 of §24. Give $\RR^2$ the square metric $\rho$, which induces the usual topology (Theorem 20.3), and give $\bar S$ the subspace metric.

**Step 1: what has to be produced.** By the definition of topological dimension (printed p. 305), $\dim\bar S\le1$ means that every open covering $\mathcal A$ of $\bar S$ has an open covering refining $\mathcal A$ in which no point lies in more than two members. So let $\mathcal A$ be an open covering of $\bar S$. The space $\bar S$ lies in $[0,1]\times[-1,1]$ and is closed in $\RR^2$, so it is compact (Theorem 27.3); let $\delta>0$ be a Lebesgue number for $\mathcal A$ (Lemma 27.5). It is enough to cover $\bar S$ by open subsets of $\bar S$, each of diameter less than $\delta$, no point lying in more than two of them: by the Lebesgue number lemma each of those sets is contained in a member of $\mathcal A$, so the family refines $\mathcal A$.

**Step 2: constants.** Choose real numbers with
$$
0<\eta\le\tfrac12,\quad \eta<\frac{\delta}{8},\qquad \rho_0=\frac{\delta}{16},\qquad \sigma=\frac{\delta}{64},\qquad 0<\ell<\min\Bigl\{\frac{\delta}{8},\ \frac{\delta\eta^2}{16}\Bigr\},\qquad \nu=\min\Bigl\{\frac{\delta}{32},\ \frac{\ell}{4},\ \frac{\eta}{2}\Bigr\}.
$$
Note $\eta<\delta$, $2\nu\le\ell/2<\delta$, $2\sigma<\delta$, and $\ell/\eta^2<\delta/16$. (The symbol $\rho_0$ is used for the radius to avoid a clash with the square metric $\rho$.)

**Step 3: the cover near the vertical segment.** Let $y_0=\sin(1/\eta)$. Choose open intervals $I_1,\dots,I_p$ of $\RR$ covering $[-1,1]$ such that

- no point of $[-1,1]$ lies in more than two of the $I_i$;
- one of them, call it $I_0$, is $(y_0-2\sigma,\,y_0+2\sigma)$, and every other $I_i$ is contained either in $(-\infty,\,y_0-\sigma)$ or in $(y_0+\sigma,\,\infty)$, so that a point of $\bar S$ whose second coordinate satisfies $\abs{y-y_0}<\sigma$ lies in exactly one of the $I_i$;
- $\abs{I_i}<\delta/2$ for every $i$.

Such intervals exist. Suppose first that $L=y_0-2\sigma+1>0$, and take a partition $-1=b_0<b_1<\dots<b_q=y_0-2\sigma$ whose mesh $m$ satisfies $\frac{\delta}{64}<m<\frac{\delta}{16}$: if $L\ge\frac{\delta}{16}$ take $q$ with $\frac{16L}{\delta}<q<\frac{32L}{\delta}$, which exists because that interval of integers has length $\frac{16L}{\delta}\ge1$, and put $b_k=-1+k\frac{L}{q}$ so that $m=\frac{L}{q}\in(\frac{\delta}{32},\frac{\delta}{16})$; if $L<\frac{\delta}{16}$ take $q=1$, so that $m=L<\frac{\delta}{16}$ and there is only one interval. Put $J_k=(b_{k-1}-\frac{\delta}{128},\,b_k+\frac{\delta}{128})$. Then $J_k\cap J_l=\emptyset$ when $\abs{k-l}\ge2$, because $b_{k+1}-b_k=m>\frac{\delta}{64}=\frac{2\delta}{128}$ forces $b_{k+1}-\frac{\delta}{128}>b_k+\frac{\delta}{128}$; each $J_k$ has length less than $\frac{\delta}{16}+\frac{\delta}{64}<\frac{\delta}{8}$; and each $J_k$ is contained in $(-\infty,y_0-\sigma)$, because its right end is at most $(y_0-2\sigma)+\frac{\delta}{128}=y_0-2\sigma+\frac{\sigma}{2}<y_0-\sigma$. Cover $[y_0+2\sigma,1]$ the same way when that interval is nonempty, with the roles of $y_0-\sigma$ and $y_0+\sigma$ exchanged, and add $I_0$; the points of $[-1,1]$ outside $(y_0-2\sigma,y_0+2\sigma)$ are covered by the $J$'s.

For each of these intervals let
$$
W(I)=\bar S\cap\bigl\{(x,y):y\in I\bigr\}\cap\bigl\{(x,y):x<\eta\bigr\}.
$$
This is open in $\bar S$, being the trace on $\bar S$ of the open set $\{y\in I\}\cap\{x<\eta\}$ of $\RR^2$. Its first coordinates lie in $[0,\eta]$ and its second in $I$, so its diameter under the square metric is $\max\{\eta,\abs{I}\}<\delta$. The family $\{W(I)\}$ covers every point of $\bar S$ whose first coordinate is less than $\eta$, since the $I$'s cover $[-1,1]$; no point of $\bar S$ lies in more than two members, since its second coordinate lies in at most two of the $I$'s; and a point of $\bar S$ with $x<\eta$ and $\abs{y-y_0}<\sigma$ lies in exactly one member.

**Step 4: the cover of the part away from the segment.** Put $s_k=\eta+k\ell$ and take $N\ge1$ with $s_N\ge1$. For $k=0,\dots,N-1$ and $j=0,\dots,N$ let
$$
C_k=\bar S\cap\{s_k<x<s_{k+1}\}\cap\{\abs{y-\sin(1/x)}<\rho_0\},\qquad
D_j=\bar S\cap\{\abs{x-s_j}<\nu\}\cap\{\abs{y-\sin(1/s_j)}<\sigma\},
$$
and delete any of these sets that is empty. Each is open in $\bar S$: the map $(x,y)\mapsto\sin(1/x)$ is continuous on the open set $\{x>\eta/2\}$, which contains all the sets displayed ($\sin$ is continuous by the familiar properties quoted in Example 3 of §18, and $x\mapsto1/x$ is continuous where $x\ne0$), and each of the sets is $\bar S$ meet an open subset of $\RR^2$ contained in that half-plane.

Their diameters are less than $\delta$. For $C_k$: two of its points $(x,y)$, $(x',y')$ have $s_k<x,x'<s_{k+1}$, so $\abs{x-x'}<\ell$, and then, with $x,x'\ge\eta$,
$$
\abs{y-y'}\le\abs{y-\sin(1/x)}+\abs{\sin(1/x)-\sin(1/x')}+\abs{\sin(1/x')-y'}<\rho_0+\frac{\abs{x-x'}}{xx'}+\rho_0\le 2\rho_0+\frac{\ell}{\eta^2}<\frac{\delta}{8}+\frac{\delta}{16},
$$
where $\abs{\sin a-\sin a'}\le\abs{a-a'}$ (mean value theorem) and $\abs{1/x-1/x'}=\abs{x-x'}/xx'\le\ell/\eta^2$ are used; hence $\operatorname{diam}C_k\le\max\{\ell,3\delta/16\}<\delta$. For $D_j$: the first coordinates span less than $2\nu\le\ell/2<\delta$ and the second less than $2\sigma<\delta$.

These sets cover every point of $\bar S$ whose first coordinate is at least $\eta$: such a point with $0<x\le1$ satisfies $y=\sin(1/x)$, so it lies in $C_k$ if $s_k<x<s_{k+1}$, and it lies in $D_j$ if $x=s_j$; there are no other points of $\bar S$ with first coordinate at least $\eta$.

**Step 5: no point lies in more than two sets.** Let $q=(x,y)\in\bar S$.

- If $x<\eta$: then $q$ lies in at most two of the $W(I)$, and in no $C_k$; it lies in a $D_j$ only if $\abs{x-s_j}<\nu$. For $j\ge1$ this needs $x>s_j-\nu\ge\eta+\ell-\nu>\eta$ because $\nu\le\ell/4$; so only $j=0$ can occur, and then $\abs{y-y_0}<\sigma$, so $q$ lies in exactly one $W(I)$. Hence $q$ lies in at most two members.
- If $x=s_j$ for some $j$: then $q\in D_j$ and $q$ lies in no $C_k$ and in no $W(I)$ (since $x\ge\eta$); so $q$ lies in exactly one member.
- If $s_k<x<s_{k+1}$ for some $k$: then $q\in C_k$ and $q$ lies in no $W(I)$; it lies in $D_j$ only if $\abs{x-s_j}<\nu$, which for $\nu\le\ell/4$ happens for at most one $j$, namely $j=k$ or $j=k+1$. So $q$ lies in at most two members.

So the family consisting of the sets $W(I)$, $C_k$ and $D_j$ is an open cover of $\bar S$, every member of which has diameter less than $\delta$ and no point of which lies in more than two members; by Step 1 it refines $\mathcal A$. As $\mathcal A$ was arbitrary, $\dim\bar S\le1$.

**Step 6: the lower bound.** By Example 7 of §24 the space $\bar S$ is connected, it is metrizable hence $T_1$, and it has more than one point; by [[E-KWBI9]] every connected $T_1$ space with more than one point has dimension at least $1$. Hence
$$
\dim\bar S=1 .
$$
:::
