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
---

::: {.exercise}

(a) Let $X$ be a regular space.
If $X$ is a countable union of compact subspaces of $X$, then $X$ is paracompact.

(b) Show that $\RR^\infty$ is paracompact as a subspace of $\RR^\omega$ in the box topology.
:::

::: {.solution}
(a) Suppose
$$
X=\bigcup_{n=1}^{\infty}K_n
$$
with each $K_n$ compact. Then $X$ is Lindelöf: if $\mathcal U$ is an open cover, each $K_n$ has a finite subcover, and the union of these finite subcovers over $n$ is countable and covers $X$.

We now prove directly that a regular Lindelöf space is paracompact. Let $\mathcal U$ be an open cover. For every $x\in X$, regularity gives open sets $V_x$ and $U_x\in\mathcal U$ such that
$$
x\in V_x\subset\overline{V_x}\subset U_x.
$$
By Lindelöfness choose $V_1,V_2,\ldots$ covering $X$, with corresponding $U_n\in\mathcal U$. Define
$$
W_n=U_n-\bigcup_{i<n}\overline{V_i}.
$$
Each $W_n$ is open and refines $\mathcal U$. The family covers $X$: for $x$, choose the least $i$ such that $x\in\overline{V_i}$; then $x\in U_i$ and $x\notin\overline{V_j}$ for $j<i$, hence $x\in W_i$. It is locally finite: if $x\in V_m$, then $V_m\cap W_n=\varnothing$ for every $n>m$, since $W_n$ omits $\overline{V_m}$. Thus $V_m$ meets only $W_1,\ldots,W_m$. Hence $X$ is paracompact.

(b) Let $\RR^\infty$ be the eventually-zero sequences, with the topology inherited from the box topology on $\RR^\omega$. For $n,m\ge1$, put
$$
K_{n,m}=[-m,m]^n\times\{0\}\times\{0\}\times\cdots.
$$
On $K_{n,m}$, the box-subspace topology is just the usual finite product topology, so $K_{n,m}$ is compact. Moreover
$$
\RR^\infty=\bigcup_{n,m\ge1}K_{n,m}.
$$
The space $\RR^\infty$ is regular: a basic neighbourhood of $x\in\RR^\infty$ in the box topology has all but finitely many factors equal to $\RR$, so it contains a box $\prod_{i\le N}(c_i,d_i)\times\RR^{>N}$ with $c_i<x_i<d_i$ and $a_i<c_i$, $d_i<b_i$ for the finitely many constrained coordinates of a smaller box $\prod_{i\le N}(a_i,b_i)\times\RR^{>N}$ around $x$; the closure in $\RR^\infty$ of the smaller box is contained in $\prod_{i\le N}[a_i,b_i]\times\RR^{>N}$, which the given neighbourhood contains. Therefore part (a) applies with the countably many compact sets $K_{n,m}$, and $\RR^\infty$ is paracompact.
:::
