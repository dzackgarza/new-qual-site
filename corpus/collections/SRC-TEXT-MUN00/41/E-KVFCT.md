---
schema: qual/card@1
id: E-KVFCT
kind: problem
title: $\sigma$-compact regular spaces are paracompact
classification:
  areas:
  - topology
  topics:
  - Paracompactness
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    No complete published solution was located for this exercise, so the proof is checked line by line
    against the book and the search is recorded in the COMPLAINTS.md entry for §39--§42 of SRC-TEXT-MUN00.
    Searched: the sets listed in that entry --- Aleksey Zinger's MAT 530 sheets, the *Praying For Stockholm*
    posts, Moller's S38, the Riverside Math 205A solutions, Orellana, Doug's World, Whitman,
    "positron0802", "shenapse", "9beach", "kyp44", the seven further GitHub manuals, dbfin and Gardner's
    ETSU notes --- none of which solves this exercise.
    Checked against Munkres, Topology (2000), Section 41 Exercise 6, printed p. 260, with Theorem 41.5 (every regular Lindelof space is paracompact), which part (a) reproves from the shrinking $V_n\subset\overline{V_n}\subset U_n$, and the box topology of §20 for part (b). What was corrected: part (b) concluded the regularity of $\RR^\infty$ from the complete regularity of the box product $\RR^\omega$, which the card did not justify; it now proves regularity of $\RR^\infty$ directly, from boxes whose closures lie in a given box.
- event: source-corrected
  by: claude
  date: 2026-11-10
  note: >-
    Part (b) asserted that $K_{n,m}$ is compact without the two steps it needs; the card now describes the
    subspace topology: a basis element of the box topology meets $K_{n,m}$ in the product of its traces on
    the first $n$ coordinates, because the remaining coordinates of $K_{n,m}$ are fixed at $0$, so $K_{n,m}$
    is a finite product of compact intervals, compact by Theorem 27.1 and Theorem 26.7. The earlier repair
    of the regularity of $\RR^\infty$ stands. Checked against Theorem 27.1, Theorem 26.7 and the definition
    of the box topology of §19.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; the argument is the card's own and was re-read
    against the book. Pages added where the prose had none: paracompactness defined on
    printed p. 254, Theorem 41.5 on printed p. 257 with its own route through the
    shrinking lemma (Lemma 41.3, printed p. 256), the exercise on printed p. 260,
    Theorem 27.1 on printed p. 172 and Theorem 26.7 on printed p. 167. The step a reader
    can most easily garble is now pinned: the covering index is the least i with
    x in closure(V_i), which gives both x in U_i (through closure(V_i) inside U_i) and
    x outside closure(V_j) for every j < i; the least i with x in V_i would give the
    second but not the first. Repair of wording: the regularity paragraph for R^infinity
    ran two boxes together, so that "the finitely many constrained coordinates of a
    smaller box" had no antecedent; it now exhibits the given basic neighbourhood, the
    shrinking inside it, and a direct argument that a point off the closed box has a
    neighbourhood disjoint from the smaller one, which is the closure step. No repair to
    the statement.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Review repair of the regularity step. The step had taken a basic box neighbourhood of
    x to be of the form prod_{i<=N}(a_i,b_i) x R^{>N}, on the ground that a box-open set
    differs from R in only finitely many coordinates; that is true of the topology's
    definition only in the sense that no coordinate is privileged, and a basic box-open set
    may constrain infinitely many coordinates, so the finite-factor U_0 need not exist. The
    step now shrinks every coordinate: from the given basic set prod U_i (with each U_i an
    open subset of R containing x_i, possibly proper for infinitely many i) choose an
    interval (c_i,d_i) around x_i with closure in U_i, take V = R^infinity intersected with
    prod (c_i,d_i), and prove closure V inside prod [c_i,d_i] inside U by exhibiting, for a
    point y off prod [c_i,d_i], the box neighbourhood with i-th factor (y_i - 1, c_i) or
    (d_i, y_i + 1), which misses V. No other step of the card changed.
---

::: {.exercise}

(a) Let $X$ be a regular space.
If $X$ is a countable union of compact subspaces of $X$, then $X$ is paracompact.

(b) Show that $\RR^\infty$ is paracompact as a subspace of $\RR^\omega$ in the box topology.
:::

::: {.solution}
The argument is the card's own: no retained set solves this exercise, as the searches recorded in the audit and in the COMPLAINTS.md entry for §39--§42 show. Part (a) is a direct proof of Munkres' Theorem 41.5 (printed p. 257), whose own route is the countably locally finite subcover together with the shrinking lemma of his Lemma 41.3; the direct route below is kept because every step of it is checked here.

Throughout, $X$ is regular, $X=\bigcup_{n\in\ZZ_+}K_n$ with each $K_n$ compact, an open cover $\mathcal{U}$ of $X$ is given, and paracompact means that every open cover has an open locally finite refinement (§41, printed p. 254). In part (b), $\RR^\infty$ is the subspace of eventually zero sequences of $\RR^\omega$ with the box topology, and $K_{n,m}=[-m,m]^n\times\{0\}\times\{0\}\times\cdots$.

::: pf

::: {.pf-step #lindelof}
(a) $X$ is Lindelöf, so every open cover of $X$ has a countable subcover.

::: pf-proof
For each $n$ the compact space $K_n$ is covered by $\mathcal{U}$, so finitely many members of $\mathcal{U}$ cover $K_n$ (§26). The union over $n$ of these finite subfamilies is countable, and it covers $\bigcup_n K_n=X$.
:::

:::

::: {.pf-step #shrinking}
There is a countable family $V_1,V_2,\ldots$ of open sets covering $X$ and, for each $n$, a member $U_n\in\mathcal{U}$ with $V_n\subset\closure{V_n}\subset U_n$.

::: pf-proof
For $x\in X$ choose $U_x\in\mathcal{U}$ with $x\in U_x$; regularity of $X$ gives an open neighbourhood $V_x$ of $x$ with $\closure{V_x}\subset U_x$, so $x\in V_x\subset\closure{V_x}\subset U_x$. The family $\{V_x\}_{x\in X}$ is an open cover, and by step [](#lindelof){.pf-ref} it has a countable subcover $V_1,V_2,\ldots$, each $V_n$ being $V_x$ for some $x$ whose $U_x$ we call $U_n$.
:::

:::

::: {.pf-step #refinement}
The sets $W_n=U_n-\bigcup_{i<n}\closure{V_i}$ form an open family refining $\mathcal{U}$ that covers $X$ and is locally finite; hence $X$ is paracompact.

::: pf-proof

::: {.pf-step #open}
Each $W_n$ is open and $W_n\subset U_n\in\mathcal{U}$.

::: pf-proof
$U_n$ is open and $\bigcup_{i<n}\closure{V_i}$ is a finite union of closed sets, hence closed; the difference of an open set and a closed set is open. The containment $W_n\subset U_n$ is immediate.
:::

:::

::: {.pf-step #cover}
The family $\{W_n\}$ covers $X$.

::: pf-proof
Let $x\in X$. Since $V_n\subset\closure{V_n}$ and the $V_n$ cover $X$, the set of indices $i$ with $x\in\closure{V_i}$ is nonempty, so it has a least element $i$; then $x\notin\closure{V_j}$ for every $j<i$, so $x\notin\bigcup_{j<i}\closure{V_j}$, while $x\in\closure{V_i}\subset U_i$. Hence $x\in U_i-\bigcup_{j<i}\closure{V_j}=W_i$.
:::

:::

::: {.pf-step #locally-finite}
$\{W_n\}$ is locally finite.

::: pf-proof
Let $x\in X$; by step [](#shrinking){.pf-ref} there is $m$ with $x\in V_m$, and $V_m$ is a neighbourhood of $x$. For $n>m$ the set $\closure{V_m}$ is among the sets subtracted in the definition of $W_n$, so $W_n\subset X-\closure{V_m}$ and therefore $V_m\cap W_n=\emptyset$ because $V_m\subset\closure{V_m}$. Thus the neighbourhood $V_m$ of $x$ meets only $W_1,\ldots,W_m$.
:::

:::

:::

:::

::: {.pf-step #b-compact}
(b) Each $K_{n,m}$ is compact.

::: pf-proof
A basic open set of the box topology on $\RR^\omega$ is a product $\prod_i G_i$ of open subsets of $\RR$; its trace on $K_{n,m}$ is $\big(\prod_{i\le n}(G_i\cap[-m,m])\big)\times\prod_{i>n}(G_i\cap\{0\})$, and the second factor is either $\{0\}$ or empty, because every coordinate of $K_{n,m}$ after the $n$-th is the fixed point $0$. So the subspace topology on $K_{n,m}$ is the finite product topology on $\prod_{i\le n}[-m,m]$, and $[-m,m]$ is compact (Theorem 27.1, printed p. 172). A finite product of compact spaces is compact (Theorem 26.7, printed p. 167), so $K_{n,m}$ is compact.
:::

:::

::: {.pf-step #b-union}
$\RR^\infty=\bigcup_{n,m\ge1}K_{n,m}$.

::: pf-proof
A point of $\RR^\infty$ is a sequence that is zero from some index $n$ on, and its first $n$ coordinates are bounded in absolute value by some integer $m$; hence the point lies in $K_{n,m}$. Conversely every point of every $K_{n,m}$ is eventually zero, so it lies in $\RR^\infty$.
:::

:::

::: {.pf-step #b-regular}
$\RR^\infty$ is regular.

::: pf-proof
Let $x\in\RR^\infty$ and let $U$ be a neighbourhood of $x$ in $\RR^\infty$. Then $U$ contains a basic neighbourhood $\RR^\infty\cap\prod_iU_i$, where each $U_i$ is an open subset of $\RR$ containing $x_i$: a basic open set of the box topology is such a product, and infinitely many of its factors may be proper subsets of $\RR$, so every coordinate is treated below and no factor is assumed to be $\RR$. For each $i$ choose an open interval $(c_i,d_i)$ with $x_i\in(c_i,d_i)$ and $\closure{(c_i,d_i)}\subset U_i$, which is possible because $U_i$ is a neighbourhood of $x_i$ in $\RR$; put $V=\RR^\infty\cap\prod_i(c_i,d_i)$, which is open in $\RR^\infty$ and contains $x$. Then $\closure{V}\subset U$, by the chain $\closure{V}\subset\RR^\infty\cap\prod_i[c_i,d_i]\subset\RR^\infty\cap\prod_iU_i\subset U$: for the first inclusion, if $y\in\RR^\infty$ has $y_i\notin[c_i,d_i]$, say $y_i<c_i$ (the case $y_i>d_i$ is symmetric), then $\RR^\infty\cap\big(G\times\prod_{j\ne i}\RR\big)$ with $G=(y_i-1,c_i)$ is a neighbourhood of $y$ disjoint from $V$, because its $i$-th factor misses $(c_i,d_i)$. Hence every neighbourhood of every point of $\RR^\infty$ contains a closed neighbourhood, and $\RR^\infty$ is regular.
:::

:::

::: {.pf-step}
$\RR^\infty$ is paracompact.

::: pf-proof
By step [](#b-union){.pf-ref} $\RR^\infty$ is the union of the countably many compact subspaces $K_{n,m}$ of step [](#b-compact){.pf-ref}, and it is regular by step [](#b-regular){.pf-ref}; so part (a), step [](#refinement){.pf-ref}, applies to it and gives that every open cover of $\RR^\infty$ has an open locally finite refinement.
:::

:::

:::
:::
