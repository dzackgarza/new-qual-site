---
schema: qual/card@1
id: E-RIGIX
kind: problem
title: Complete normality of standard spaces and constructions
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Checked against Munkres, Topology (2000), Section 32 Exercise 7, printed pp. 205-206, with the
    answers of "Doug's World", "Munkres - Topology - Chapter 4 Solutions" (30 August 2017; the file
    names no author), Problem 32.7, printed p. 7 (tmp/sources/munkres-solutions-dougsworld-ch4.pdf),
    which are Yes, No, Yes, Yes, No, Yes, Yes. Corrections: (b) is now the source's own example --
    S_Omega and S_bar_Omega are completely normal by Theorem 32.4, while S_Omega x S_bar_Omega is not
    normal by Example 2 of Section 32 (printed p. 203) -- instead of the Sorgenfrey plane, which
    would use part (g) of the same exercise; (c) was a citation to "linearly ordered topological
    spaces are hereditarily normal" with no argument, and now proves that a subspace of a
    well-ordered set carries the order topology of its induced well-order and applies Theorem 32.4
    (printed p. 202); (e) was quoted from Stone's theorem on R^J for uncountable J, which needs
    Tychonoff for the compactness of [0,1]^J, and is now the book's own witness
    S_bar_Omega x S_bar_Omega, compact by Theorem 26.7 (printed p. 167) and Hausdorff by Theorem
    19.4 (printed p. 116), containing the non-normal subspace S_Omega x S_bar_Omega. The source's
    own answers to (c) and (e) are the bare sentences "Remember that in fact every set in the order
    topology is completely normal!" and "No, but I haven't been able to find a counterexample I
    understand", so no complete published argument exists for those two parts; the search is
    recorded in the COMPLAINTS.md entry for this batch.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Rebuilt on the located published solution for all seven parts: dbFin, "Section 32: Problem 7
    Solution", https://dbfin.com/topology/munkres/chapter-4/section-32-normal-spaces/problem-7-solution/
    (read 2026-11-10; kept at
    tmp/sources/dbfin/section-32-normal-spaces/problem-7-solution.txt), together with "Doug's World",
    "Munkres - Topology - Chapter 4 Solutions", Problem 32.7, printed p. 7, for the seven answers,
    which agree (Yes, No, Yes, Yes, No, Yes, Yes). Checked against Munkres, Topology (2000), Section
    32 Exercise 7, printed pp. 205-206, Theorem 32.4 (printed p. 202), Example 2 of Section 32
    (printed p. 203), Theorems 26.7 (p. 167), 19.4 (p. 116) and 32.3 (p. 202). What was changed:
    (c) is now dbFin's argument -- every interval (a,b] is open in a well-ordered set, as in the
    proof of Theorem 32.4, and the sets {(x,a]} and {(y,b]} chosen to miss the other of a separated
    pair are automatically disjoint, by the ordering, which the source asserts ("Moreover, the
    neighbourhoods belonging to one set do not intersect the neighbourhoods belonging to the other")
    and the card now proves -- instead of the previous reduction to Theorem 32.4 through the induced
    order on a subspace. (g) is the same argument with the basis [x,x+eps) of R_l, which dbFin
    gives; the previous proof of (g) by hereditary Lindelofness is superseded. (c) and (g) are
    applied through the characterization of Exercise 32.6, which is on E-TZ1IN. (b) and (e) are
    dbFin's answers -- R_l is completely normal while R_l^2 is not, and "No. See Example 2" for the
    compact Hausdorff space -- and the card keeps the book's own witness S_Omega x S_bar_Omega,
    whose non-normality is Example 2 and whose compact Hausdorff container S_bar_Omega^2 needs only
    Theorem 26.7, not Tychonoff. This supersedes the previous note, which recorded (c) and (e) as
    having no complete published argument.
---

::: {.exercise}

Which of the following spaces are completely normal?
Justify your answers.

(a) A subspace of a completely normal space.

(b) The product of two completely normal spaces.

(c) A well-ordered set in the order topology.

(d) A metrizable space.

(e) A compact Hausdorff space.

(f) A regular space with a countable basis.

(g) The space $\RR_\ell$.
:::

::: {.solution}
(a) Yes. Every subspace of a subspace of a completely normal space is a subspace of the original space, hence normal.

(b) No. The well-ordered sets $S_\Omega$ and $\overline{S}_\Omega$ are completely normal by part (c) below, and by Theorem 32.4; but their product $S_\Omega\times\overline{S}_\Omega$ is not normal, as Example 2 of §32 shows. The same example shows that the product of two normal spaces need not be normal.

(c) Yes. Let $W$ be well-ordered in the order topology. Every interval $(x,y]$ of $W$ is open, by the argument of the proof of Theorem 32.4: if $y$ is the largest element of $W$ then $(x,y]$ is a basis element, and otherwise $(x,y]=(x,y')$ for the immediate successor $y'$ of $y$. By Exercise 32.6 it is enough to separate a pair $A,B$ of separated subsets of $W$ by disjoint open sets. For $a\in A$ the point $a$ is not in $\overline{B}$, so there is a neighbourhood $N_a$ of $a$ disjoint from $B$, taken of the form $(x_a,a]$ when $a$ is not the least element of $W$ and equal to $\{a\}=[a,b)$ when it is; in either case $N_a\subseteq\{z:z\le a\}$. For $b\in B$ choose $M_b$ likewise, with $M_b\subseteq\{z:z\le b\}$ and $M_b\cap A=\varnothing$. Then $U=\bigcup_{a\in A}N_a$ and $V=\bigcup_{b\in B}M_b$ are open and contain $A$ and $B$. They are disjoint: if $z\in N_a\cap M_b$ with $a\le b$, then $z\le a\le b$ and $z\in M_b$ force $a\in M_b$ (if $z=a$, or if $M_b=(y_b,b]$ and $z>y_b$, then $y_b<z\le a\le b$), contradicting $M_b\cap A=\varnothing$. Hence every pair of separated sets in $W$ has disjoint neighbourhoods, and by Exercise 32.6 the well-ordered set is completely normal.

(d) Yes. Every subspace of a metrizable space is metrizable, hence normal.

(e) No. The space $\overline{S}_\Omega\times\overline{S}_\Omega$ is compact (Theorem 26.7) and Hausdorff (Theorem 19.4), hence normal (Theorem 32.3); but it contains the subspace $S_\Omega\times\overline{S}_\Omega$, which is not normal by Example 2 of §32. Complete normality of the product would make that subspace normal, so the product is not completely normal.

(f) Yes. Every subspace of a regular second-countable space is regular and second countable. Second-countable spaces are Lindelöf, so every subspace is regular Lindelöf and hence normal by the preceding exercise. Thus the original space is completely normal.

(g) Yes. In $\RR_\ell$ the sets $[x,x+\epsilon)$ form a basis at $x$. Let $A,B$ be separated subsets and for $a\in A$ choose $\epsilon_a>0$ with $[a,a+\epsilon_a)$ disjoint from $B$, and for $b\in B$ choose $\delta_b>0$ with $[b,b+\delta_b)$ disjoint from $A$; these exist because $a\notin\overline B$ and $b\notin\overline A$. Then $U=\bigcup_{a\in A}[a,a+\epsilon_a)$ and $V=\bigcup_{b\in B}[b,b+\delta_b)$ are open and contain $A$ and $B$. If $z$ lay in $[a,a+\epsilon_a)\cap[b,b+\delta_b)$ with $a\le b$, then $b\le z<a+\epsilon_a$, so $b\in[a,a+\epsilon_a)$, contradicting that this interval misses $B$. Hence the sets are disjoint, and by Exercise 32.6 the Sorgenfrey line is completely normal.

:::
