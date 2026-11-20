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
    Checked against Munkres, Topology (2000), Section 32 Exercise 7, with the
    answers of "Doug's World", "Munkres - Topology - Chapter 4 Solutions" (30 August 2017; the file
    names no author), Problem 32.7, (tmp/sources/munkres-solutions-dougsworld-ch4.pdf),
    which are Yes, No, Yes, Yes, No, Yes, Yes. Corrections: (b) is now the source's own example --
    S_Omega and S_bar_Omega are completely normal by Theorem 32.4, while S_Omega x S_bar_Omega is not
    normal by Example 2 of Section 32 -- instead of the Sorgenfrey plane, which
    would use part (g) of the same exercise; (c) was a citation to "linearly ordered topological
    spaces are hereditarily normal" with no argument, and now proves that a subspace of a
    well-ordered set carries the order topology of its induced well-order and applies Theorem 32.4; (e) was quoted from Stone's theorem on R^J for uncountable J, which needs
    Tychonoff for the compactness of [0,1]^J, and is now the book's own witness
    S_bar_Omega x S_bar_Omega, compact by Theorem 26.7 and Hausdorff by Theorem
    19.4, containing the non-normal subspace S_Omega x S_bar_Omega. The source's
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
    "Munkres - Topology - Chapter 4 Solutions", Problem 32.7, for the seven answers,
    which agree (Yes, No, Yes, Yes, No, Yes, Yes). Checked against Munkres, Topology (2000), Section
    32 Exercise 7, Theorem 32.4, Example 2 of Section 32, Theorems 26.7, 19.4 and 32.3. What was changed:
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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with twelve steps, one or more for each of the seven parts, each carrying a `pf-proof`; the
    seven answers are unchanged and every argument is the card's own. The page citations in the
    two earlier events are removed, the locators now being chapter, section and statement
    numbers only. Cited by number only: Theorem 32.4 (well-ordered sets are normal in the order
    topology), Exercise 32.6 (complete normality as separation of separated sets), Theorem
    26.7, Theorem 19.4, Theorem 32.3, Theorem 30.3, Exercise 32.4 (regular Lindelöf spaces are
    normal), and Example 2 of §32. Parts (d) and (g) are proved outright rather than cited:
    metrizable spaces are normal by the distance-function separation, written in step 8.
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

::: pf

::: pf-step

(a) Yes. A subspace of a completely normal space is completely normal.

::: pf-proof

If $Y$ is a subspace of $X$ and $Z\subseteq Y$, the topology $Z$ inherits from $Y$ is the topology it inherits from $X$, so $Z$ is a subspace of $X$. Complete normality of $X$ says that every subspace of $X$ is normal, so every subspace of $Y$ is normal, which is complete normality of $Y$.

:::

:::

::: pf-step

(b) No. The well-ordered sets $S_\Omega$ and $\overline{S}_\Omega$ are completely normal, but their product $S_\Omega\times\overline{S}_\Omega$ is not normal, as Example 2 of §32 shows; so the product of two completely normal spaces need not even be normal.

::: pf-proof

$S_\Omega$ and $\overline{S}_\Omega=[0,\Omega]$ are well-ordered sets in the order topology, so they are completely normal by part (c) below, and normal by Theorem 32.4. Their product $S_\Omega\times\overline{S}_\Omega$ is not normal by Example 2 of §32. A completely normal space has every subspace normal, so a product that is not even normal is certainly not completely normal.

:::

:::

::: pf-step

(c) Yes. Let $W$ be a well-ordered set in the order topology. Every interval $(x,y]$ of $W$ is open.

::: pf-proof

If $y$ is the largest element of $W$ then $(x,y]=\{z\in W:z>x\}$ is an open ray, hence a basis element. Otherwise $y$ has an immediate successor $y'$, the least element of the nonempty set $\{z:z>y\}$, and $(x,y]=(x,y')$, again an open ray; no element lies strictly between $y$ and $y'$ by the choice of $y'$. This is the observation used in the proof of Theorem 32.4.

:::

:::

::: pf-step

(c) For separated sets $A,B\subset W$ and $a\in A$ there is a neighbourhood $N_a$ of $a$ with $N_a\subset\{z:z\le a\}$ and $N_a\cap B=\varnothing$; for $b\in B$ there is $M_b$ with $M_b\subset\{z:z\le b\}$ and $M_b\cap A=\varnothing$.

::: pf-proof

Separated means $A\cap\overline B=\overline A\cap B=\varnothing$, so $a\notin\overline B$ and some neighbourhood of $a$ misses $B$. If $a$ is not the least element of $W$, the intervals $(x,a]$ form a basis at $a$ and the intersection of one of them with that neighbourhood is an $N_a\subseteq\{z:z\le a\}$ missing $B$; if $a$ is the least element then $\{a\}$ is open and itself serves, since every element is $\ge a$. The same construction at $b\in B$ gives $M_b$.

:::

:::

::: pf-step

(c) Then $U=\bigcup_{a\in A}N_a$ and $V=\bigcup_{b\in B}M_b$ are open and contain $A$ and $B$.

::: pf-proof

A union of open sets is open, and $a\in N_a\subseteq U$, $b\in M_b\subseteq V$ for each $a\in A$ and $b\in B$.

:::

:::

::: pf-step

(c) $U\cap V=\varnothing$.

::: pf-proof

Suppose $z\in N_a\cap M_b$ for some $a\in A$, $b\in B$. From $z\in N_a\subseteq\{z':z'\le a\}$ and $z\in M_b\subseteq\{z':z'\le b\}$ we get $z\le a$ and $z\le b$; exchanging the names $A$ and $B$ if necessary, assume $a\le b$. If $z=a$ then $a\in M_b$, contradicting $M_b\cap A=\varnothing$. If $z<a$, then $M_b$ is either $\{b\}$ — which forces $z=b\le a\le b$, so $z=a$, excluded — or an interval $(y_b,b]$ with $y_b<z$, and then $y_b<z<a\le b$ gives $a\in(y_b,b]=M_b$, again contradicting $M_b\cap A=\varnothing$.

:::

:::

::: pf-step

(c) By Exercise 32.6, $W$ is completely normal.

::: pf-proof

Exercise 32.6 characterizes complete normality as the separation of every pair of separated sets by disjoint open sets; steps 4--6 do that for an arbitrary separated pair $A,B$ of $W$.

:::

:::

::: pf-step

(d) Yes. Every subspace of a metrizable space is metrizable, hence normal.

::: pf-proof

A subspace of a metrizable space is metrizable, the restriction of the metric inducing its topology. A metrizable space is normal: for disjoint closed sets $A,B$ the functions $x\mapsto d(x,A)$ and $x\mapsto d(x,B)$ are continuous, so $U=\{x:d(x,A)<d(x,B)\}$ and $V=\{x:d(x,B)<d(x,A)\}$ are open, disjoint, and contain $A$ and $B$ respectively, because $d(x,A)=0<d(x,B)$ for $x\in A$ and symmetrically for $B$. So every subspace is normal and the space is completely normal.

:::

:::

::: pf-step

(e) No. The space $\overline{S}_\Omega\times\overline{S}_\Omega$ is compact (Theorem 26.7) and Hausdorff (Theorem 19.4), hence normal (Theorem 32.3); but it contains the subspace $S_\Omega\times\overline{S}_\Omega$, which is not normal by Example 2 of §32.

::: pf-proof

A product of two compact spaces is compact (Theorem 26.7) and a product of two Hausdorff spaces is Hausdorff (Theorem 19.4); a compact Hausdorff space is normal (Theorem 32.3). Complete normality of the product would make each of its subspaces normal, and $S_\Omega\times\overline{S}_\Omega$ is not normal by Example 2 of §32, so the product is not completely normal.

:::

:::

::: pf-step

(f) Yes. Every subspace of a regular second-countable space is regular and second countable; second-countable spaces are Lindelöf, so every subspace is regular Lindelöf and hence normal by Exercise 32.4. Thus the original space is completely normal.

::: pf-proof

A subspace of a second-countable space is second countable, the traces of a countable basis being a countable basis, and a subspace of a regular space is regular. A second-countable space is Lindelöf (Theorem 30.3), so each subspace is second countable, hence Lindelöf, and regular; a regular Lindelöf space is normal (Exercise 32.4). Every subspace is therefore normal, which is complete normality.

:::

:::

::: pf-step

(g) Yes. In $\RR_\ell$ the sets $[x,x+\epsilon)$ form a basis at $x$. For separated $A,B$ choose $\epsilon_a>0$ with $[a,a+\epsilon_a)$ disjoint from $B$ and $\delta_b>0$ with $[b,b+\delta_b)$ disjoint from $A$; then $U=\bigcup_{a\in A}[a,a+\epsilon_a)$ and $V=\bigcup_{b\in B}[b,b+\delta_b)$ are disjoint open sets containing $A$ and $B$, so $\RR_\ell$ is completely normal by Exercise 32.6.

::: pf-proof

$a\notin\overline B$ gives a basic neighbourhood $[a,a+\epsilon_a)$ of $a$ missing $B$, and likewise $[b,b+\delta_b)$ for $b\in B$. The two unions are open and contain $A$ and $B$. If $z$ lay in $[a,a+\epsilon_a)\cap[b,b+\delta_b)$ with $a\le b$ (the other case is symmetric), then $b\le z<a+\epsilon_a$, so $b\in[a,a+\epsilon_a)$, contradicting that this interval misses $B$. Hence the unions are disjoint, and Exercise 32.6 gives complete normality.

:::

:::

::: pf-step

The seven answers are: (a) Yes, (b) No, (c) Yes, (d) Yes, (e) No, (f) Yes, (g) Yes.

::: pf-proof

Parts (a), (c), (d), (f) and (g) are steps 1, 3--7, 8, 10 and 11, and the counterexamples of (b) and (e) are steps 2 and 9.

:::

:::

:::
:::
