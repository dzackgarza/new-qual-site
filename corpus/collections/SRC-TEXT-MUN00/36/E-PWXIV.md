---
schema: qual/card@1
id: E-PWXIV
kind: problem
title: Properties of eleven standard spaces
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Supplementary Exercises: Review of the
    Basics, Exercise 1, printed p. 228, and all 187 entries of the table now name the result that
    decides them. No published solution was located: dbFin's chapter-4 supplementary page
    (https://dbfin.com/topology/munkres/chapter-4/supplementary-exercises-review-of-the-basics/, read
    2026-11-11) carries the title and no solution, and its problem subpage directory for that section
    is empty; "Doug's World" covers the numbered exercises of 30-36 only, Moller's files are S31,
    S33, S34, S35 and S38, and Orellana's contents run 13-34 and 37. This exercise is in the
    COMPLAINTS.md entry. What the check confirmed against the book: S_Omega is limit point compact and
    not compact (Example 2 of Section 28), locally compact (Example 3 of Section 29), normal
    (Theorem 32.4), first countable only among the four countability axioms (Exercise 30.7) and
    locally metrizable (Exercise 42.2(a)); S_bar_Omega is compact (Exercise 29.7 with Theorem 29.1),
    hence Lindelof, and fails first countability, second countability, separability, local
    metrizability and metrizability as Example 3 of Section 28 and Exercise 30.7 say; the product in
    (c) is limit point compact by Exercise 28.4 and not normal by Example 2 of Section 32; the ordered
    square is connected (Theorem 24.1 with Example 1 of Section 24), not path connected (Example 6 of
    Section 24), locally connected and not locally path connected (Exercise 25.3), compact
    (Theorem 27.1), normal (Exercise 32.8), first countable (Exercise 21.4), not separable
    (Exercise 30.13) and not metrizable (Exercise 30.6); R_l is Lindelof, separable and first
    countable with no second countable (Example 3 of Section 30), normal (Example 2 of Section 31),
    and neither locally compact, locally metrizable nor metrizable (Exercise 34.8 with
    Exercise 30.6); R_l^2 is not Lindelof (Example 4 of Section 30), not normal (Example 3 of
    Section 31) and separable; R^omega has the metric properties in the product topology
    (Theorem 20.5, Example 1 of Section 30) and in the uniform topology (Example 2 of Section 30),
    is not locally compact in the product topology (Example 2 of Section 29) nor in the uniform one
    (Exercise 29.4, Corollary 29.3), is disconnected in the uniform topology (Exercise 23.8) and in
    the box topology (Example 6 of Section 23), is completely regular in the box topology
    (Exercise 33.9) and has box normality left open (the remark at Exercise 32.5); R^[0,1] has a
    countable dense subset (Exercise 30.16(a)) and is not normal (Exercise 32.9), hence not
    Lindelof (Exercise 32.4), nor first countable; and R_K is connected and not path connected
    (Exercise 27.3), Hausdorff but not regular (Example 1 of Section 31), second countable and
    locally metrizable. What was corrected: the page, which is 228 and not 228-229, since the
    properties and Exercises 1-5 are printed there and only Exercises 6 and 7 fall on p. 229; and the
    prose, which gave reasons for the eleven spaces in five groups without saying, entry by entry,
    which result decides it, and which asserted that the product in (c) is not normal because "the
    diagonal and the top edge give the standard nonseparable closed pair" without identifying the
    pair. The table itself is unchanged entry by entry.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof: each of the seventeen columns of the table is now a step
    whose proof is the argument for that column, and the table stands in the preamble. Reading
    for the restructure found one defect, in three places: columns 8, 9 and 10 cited Theorems
    31.2(a), 31.2(b) and 33.2 for (i), the box topology on R^omega, and all three theorems are
    stated for the product topology, which the box topology strictly refines. Column 8 now
    argues for (i) from the coarser topology being Hausdorff, and columns 9 and 10 from Exercise
    33.9 (the box product is completely regular, printed p. 213) together with the remark on
    printed p. 211 that a completely regular space is regular. The entries themselves are
    unchanged. Spot-checked against the book in this pass: R_l normal (Example 2 of Section 31),
    R_l^2 not normal (Example 3 of Section 31), and the ordered square locally connected but not
    locally path connected (Exercise 25.3); also Exercise 25.2(c) for the components in the box
    topology and Exercise 33.9 for complete regularity there.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    A review of this card reported four defects, all confirmed and all corrected. (i) Columns 8, 9
    and 10 listed (h), R^omega in the uniform topology, among the products in the product topology;
    the uniform topology is the metric topology of the uniform metric and is not a product
    topology, so (h) is now settled in those three columns as a metric space --- Hausdorff, and
    normal hence regular and completely regular by Theorem 32.2 and the Urysohn lemma. (ii) Column
    14 claimed (h) separable and Lindelof; the table and column 15 say otherwise, and the argument
    is now that {0,1}^omega is an uncountable closed discrete subspace (Example 2 of Section 30)
    and a Lindelof space has no such subspace. (iii) Column 12 excluded first countability for (c)
    by the slice S_Omega x {Omega}, which is homeomorphic to the first countable S_Omega and so
    proves nothing; the slice is now {alpha} x S-bar_Omega, homeomorphic to S-bar_Omega, which
    fails first countability at Omega. (iv) The table entries themselves are unchanged.
---

::: {.exercise}

Consider the following properties a space may satisfy:

(1) connected, (2) path connected, (3) locally connected, (4) locally path connected, (5) compact, (6) limit point compact, (7) locally compact Hausdorff, (8) Hausdorff, (9) regular, (10) completely regular, (11) normal, (12) first-countable, (13) second-countable, (14) Lindelöf, (15) has a countable dense subset, (16) locally metrizable, (17) metrizable.

For each of the following spaces, determine (if you can) which of these properties it satisfies.
(Assume the Tychonoff theorem if you need it.)

(a) $S_\Omega$

(b) $\overline{S}_\Omega$

(c) $S_\Omega \times \overline{S}_\Omega$

(d) The ordered square

(e) $\RR_\ell$

(f) $\RR_\ell^2$

(g) $\RR^\omega$ in the product topology

(h) $\RR^\omega$ in the uniform topology

(i) $\RR^\omega$ in the box topology

(j) $\RR^I$ in the product topology, where $I = [0, 1]$

(k) $\RR_K$
:::

::: {.solution}


Write **Y** for “yes,” **N** for “no,” and **?** for the box-product normality question not decided by the results used here. The columns are the properties (1)–(17) in the problem statement.

| space |1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| (a) $S_\Omega$ |N|N|N|N|N|Y|Y|Y|Y|Y|Y|Y|N|N|N|Y|N|
| (b) $\overline S_\Omega$ |N|N|N|N|Y|Y|Y|Y|Y|Y|Y|N|N|Y|N|N|N|
| (c) $S_\Omega\times\overline S_\Omega$ |N|N|N|N|N|Y|Y|Y|Y|Y|N|N|N|N|N|N|N|
| (d) ordered square |Y|N|Y|N|Y|Y|Y|Y|Y|Y|Y|Y|N|Y|N|N|N|
| (e) $\RR_\ell$ |N|N|N|N|N|N|N|Y|Y|Y|Y|Y|N|Y|Y|N|N|
| (f) $\RR_\ell^2$ |N|N|N|N|N|N|N|Y|Y|Y|N|Y|N|N|Y|N|N|
| (g) $\RR^\omega$, product |Y|Y|Y|Y|N|N|N|Y|Y|Y|Y|Y|Y|Y|Y|Y|Y|
| (h) $\RR^\omega$, uniform |N|N|Y|Y|N|N|N|Y|Y|Y|Y|Y|N|N|N|Y|Y|
| (i) $\RR^\omega$, box |N|N|N|N|N|N|N|Y|Y|Y|?|N|N|N|N|N|N|
| (j) $\RR^I$, product |Y|Y|Y|Y|N|N|N|Y|Y|Y|N|N|N|N|Y|N|N|
| (k) $\RR_K$ |Y|N|N|N|N|N|N|Y|N|N|N|Y|Y|Y|Y|Y|N|

Each entry is decided by a numbered result of the book or by an explicit witness; the entries are taken property by property below. Two facts are used repeatedly: a property strictly stronger than another fails whenever the weaker one does — a path connected space is connected, a compact space is limit point compact (Theorem 28.1) and Lindelöf, a second countable space is first countable and Lindelöf and has a countable dense subset (Theorem 30.3), a metrizable space is normal (Theorem 32.2) hence regular hence completely regular, and a locally metrizable space is first countable — and a product or subspace inherits a property from its factors or its ambient space in the cases the cited theorem states.

::: pf

::: {.pf-step #p1}

Column 1 of the table, *Connected*: Y for (d) ordered square, (g) $\RR^\omega$, product, (j) $\RR^I$, product, (k) $\RR_K$, N for the remaining 7.

::: pf-proof

Y for (d) — a linear continuum is connected, Theorem 24.1, and the ordered square is one, Example 1 of §24 — for (g) by Example 7 of §23, for (j) by Exercise 23.10, and for (k) by Exercise 27.3(b). N for the other seven: in (a) and (b) every successor $\alpha+1$ is isolated, $\{\alpha+1\}=(\alpha,\alpha+2)$ being a basis element; in (c) the slice $S_\Omega\times\{\Omega\}$ is both open and closed, since $\{\Omega\}$ is; in (e) and (f) the basis elements $[a,b)$, resp. $[a,b)\times[c,d)$, are also closed, so both spaces are totally disconnected; in (h) the bounded sequences form a nonempty proper set that is open and closed, a ball of radius less than $1$ about a bounded sequence consisting of bounded sequences and the same ball about an unbounded one of unbounded ones, which is the argument of Example 6 of §23 with the uniform ball in place of the box; (i) is exactly Example 6 of §23.

:::

:::

::: {.pf-step #p2}

Column 2 of the table, *Path connected*: Y for (g) $\RR^\omega$, product, (j) $\RR^I$, product, N for the remaining 9.

::: pf-proof

Y only for (g) and (j): coordinatewise straight-line paths are continuous by Theorem 19.6, whatever the index set. N for the other nine: (d) is Example 6 of §24, connected and not path connected; (k) is Exercise 27.3(c); and in (a), (b), (c), (e), (f), (h), (i) a path connected space would be connected, which entry 1 denies.

:::

:::

::: {.pf-step #p3}

Column 3 of the table, *Locally connected*: Y for (d) ordered square, (g) $\RR^\omega$, product, (h) $\RR^\omega$, uniform, (j) $\RR^I$, product, N for the remaining 7.

::: pf-proof

Y for (d) — Exercise 25.3, the ordered square is locally connected and not locally path connected — for (g) and (j) — a basic neighbourhood is a product of finitely many open intervals with copies of the whole factor, homeomorphic to $\RR^n$, resp. to $\RR^I$, which is connected by Theorem 23.6, resp. Exercise 23.10 — and for (h), where a ball of radius less than $1$ in the uniform metric is convex, a convex combination of two points of it staying in it, so that straight-line paths show it is path connected. N for the other seven: (a), (b), (c), (e), (f) are totally disconnected, so a connected neighbourhood of a point would be the point itself and Theorem 25.3 would make every point isolated, which is false; in (i) the components are the classes of sequences differing in finitely many coordinates, Exercise 25.2(c), and none is open, a basic neighbourhood with radii tending to $0$ containing points outside the class, so Theorem 25.3 applies; in (k) the component of $0$ in the open set $(-1,1)-K$ is $(-1,0]$, which is connected in the usual topology and is not open in $(-1,1)-K$, so Theorem 25.3 applies again.

:::

:::

::: {.pf-step #p4}

Column 4 of the table, *Locally path connected*: Y for (g) $\RR^\omega$, product, (h) $\RR^\omega$, uniform, (j) $\RR^I$, product, N for the remaining 8.

::: pf-proof

Y for (g), (h), (j) for the reasons just given, the neighbourhoods there being path connected. N for the other eight: (d) is Exercise 25.3, and in the rest a locally path connected space would be locally connected, which entry 3 denies.

:::

:::

::: {.pf-step #p5}

Column 5 of the table, *Compact*: Y for (b) $\overline S_\Omega$, (d) ordered square, N for the remaining 9.

::: pf-proof

Y for (b) — Exercise 29.7, $\overline S_\Omega$ is the one-point compactification of $S_\Omega$, so it is compact by Theorem 29.1 — and for (d) — Theorem 27.1, a closed interval in a simply ordered set with the least upper bound property is compact, and the ordered square is such a set with a least and a greatest element. N for the other nine: in (a) the covering by the initial segments $[0,\alpha)$, $\alpha<\omega_1$, has no finite subcover, which is why Example 2 of §28 says $S_\Omega$ is not compact; (c) contains the closed subspace $S_\Omega\times\{\Omega\}$ and is not compact by Theorem 26.2; (e) the covering by the half-open intervals $[n,n+1)$, $n\in\ZZ$, has no finite subcover; (f) contains the closed subspace $\RR_\ell\times\{0\}$; (g) and (j) contain the infinite closed discrete subspaces $\ZZ_+^\omega$ and $(\ZZ_+)^I$, which have no limit point, so these spaces are not compact by Theorem 28.1; (h) contains the closed discrete subspace $\{0,1\}^\omega$ of Example 2 of §30, so it is not compact by Theorem 28.1; (i) the box-open covering by the products $\prod_n(-m,m)$, $m\in\ZZ_+$, has no finite subcover; (k) $[0,1]$ is a closed subspace that is not compact, Exercise 27.3(a), so $\RR_K$ is not compact by Theorem 26.2.

:::

:::

::: {.pf-step #p6}

Column 6 of the table, *Limit point compact*: Y for (a) $S_\Omega$, (b) $\overline S_\Omega$, (c) $S_\Omega\times\overline S_\Omega$, (d) ordered square, N for the remaining 7.

::: pf-proof

Y for (a) by Example 2 of §28, for (b) and (d) because both are compact, entry 5, and compactness implies limit point compactness, Theorem 28.1, and for (c): every countable subset of $S_\Omega$ is bounded below $\omega_1$, hence lies in a compact rectangle $[0,\alpha]\times[0,\beta]$, so the product is countably compact, and a countably compact $T_1$ space is limit point compact, Exercise 28.4. N for the other seven: in (e) the set $\{-1/n\}$ is infinite and has no limit point in $\RR_\ell$; (f) contains the closed subspace $\RR_\ell\times\{0\}$, and closed subspaces of a limit point compact space are limit point compact, Exercise 28.3(b); (g), (h), (i), (j) each contain one of the infinite closed discrete subspaces named in entry 5, and such a subspace has no limit point at all; in (k) the set $K$ is infinite, closed and discrete.

:::

:::

::: {.pf-step #p7}

Column 7 of the table, *Locally compact Hausdorff*: Y for (a) $S_\Omega$, (b) $\overline S_\Omega$, (c) $S_\Omega\times\overline S_\Omega$, (d) ordered square, N for the remaining 7.

::: pf-proof

Y for (a) and (d) — Example 3 of §29, a simply ordered set with the least upper bound property is locally compact, and both spaces are Hausdorff because every order topology is regular, Exercise 31.3 — for (b) because it is compact Hausdorff, entries 5 and 8, and for (c) by Exercise 29.2(b) applied to (a) and (b), with Theorem 31.2(a). N for the other seven: in (e) no half-open interval $[x,x+\epsilon)$ lies in a compact set, the increasing sequence $x+\epsilon-\epsilon/n$ in it having no limit point in $\RR_\ell$, so Theorem 28.1 applies; (f) contains the closed subspace $\RR_\ell\times\{0\}$ and a closed subspace of a locally compact space is locally compact, Corollary 29.3; (g) is Example 2 of §29; (h) is Exercise 29.4 together with Corollary 29.3, $[0,1]^\omega$ being a closed subspace of $\RR^\omega$ in the uniform topology; in (i) a compact set containing a basic neighbourhood would contain the closed discrete set $\prod_n\{a_n,b_n\}$ with $a_n\neq b_n$ in the $n$-th factor, contradicting Theorem 28.1; in (j), as in (g), a basic neighbourhood contains a closed copy of $\RR^I$, so local compactness would make $\RR^I$ compact, which entry 5 denies; (k) a locally compact Hausdorff space is regular, Exercise 32.3, and $\RR_K$ is not, Example 1 of §31.

:::

:::

::: {.pf-step #p8}

Column 8 of the table, *Hausdorff*: Y for (a) $S_\Omega$, (b) $\overline S_\Omega$, (c) $S_\Omega\times\overline S_\Omega$, (d) ordered square, (e) $\RR_\ell$, (f) $\RR_\ell^2$, (g) $\RR^\omega$, product, (h) $\RR^\omega$, uniform, (i) $\RR^\omega$, box, (j) $\RR^I$, product, (k) $\RR_K$.

::: pf-proof

Y for all eleven. For (a), (b), (c), (d) this is Exercise 31.3, every order topology being regular. For the products in the product topology, (c), (f), (g) and (j), it is Theorem 31.2(a), a product of Hausdorff spaces being Hausdorff; for (h) the uniform topology on $\RR^\omega$ is the metric topology of the uniform metric, so it is Hausdorff as every metric space is; for (i), $\RR^\omega$ in the box topology, the same theorem applies to the product topology on the same set, and the box topology contains it, so sets separating two points in the coarser topology separate them in the finer one as well --- Theorem 31.2(a) is stated for the product topology and is not itself a statement about the box topology. For (e) it is Example 2 of §31, $\RR_\ell$ being normal, hence regular. For (k) it is Example 1 of §31, which records that $\RR_K$ is Hausdorff.

:::

:::

::: {.pf-step #p9}

Column 9 of the table, *Regular*: Y for (a) $S_\Omega$, (b) $\overline S_\Omega$, (c) $S_\Omega\times\overline S_\Omega$, (d) ordered square, (e) $\RR_\ell$, (f) $\RR_\ell^2$, (g) $\RR^\omega$, product, (h) $\RR^\omega$, uniform, (i) $\RR^\omega$, box, (j) $\RR^I$, product, N for the remaining one.

::: pf-proof

Y for all but (k): (a) and (b) are normal, Theorem 32.4, and a normal space is regular; (d) is Exercise 31.3; (e) is Example 2 of §31; and (c), (f), (g), (j) are products of regular spaces in the product topology, Theorem 31.2(b); (h) is metrizable, so normal by Theorem 32.2 and hence regular. For (i) the theorem does not apply, the box topology being strictly finer than the product topology; the entry rests instead on Exercise 33.9, which shows that $\RR^J$ in the box topology is completely regular, together with the remark on printed p. 211 that a completely regular space is regular, the preimages of $[0,\frac{1}{2})$ and $(\frac{1}{2},1]$ under a separating function being disjoint open sets. N for (k) by Example 1 of §31.

:::

:::

::: {.pf-step #p10}

Column 10 of the table, *Completely regular*: Y for (a) $S_\Omega$, (b) $\overline S_\Omega$, (c) $S_\Omega\times\overline S_\Omega$, (d) ordered square, (e) $\RR_\ell$, (f) $\RR_\ell^2$, (g) $\RR^\omega$, product, (h) $\RR^\omega$, uniform, (i) $\RR^\omega$, box, (j) $\RR^I$, product, N for the remaining one.

::: pf-proof

Y for all but (k). A normal space is completely regular by the Urysohn lemma, Theorem 33.1, which settles (a), (b), (d), (e) through their normality, entry 11; and a product of completely regular spaces is completely regular, Theorem 33.2, which settles (c), (f), (g) and (j) in the product topology; (h) is metrizable, so normal by Theorem 32.2 and hence completely regular by the Urysohn lemma. That theorem's product clause is again about the product topology, so (i) is settled by Exercise 33.9, the result that $\RR^J$ in the box topology is completely regular. N for (k): a completely regular space is regular, the preimages of $[0,\frac{1}{2})$ and $(\frac{1}{2},1]$ under a separating function being disjoint open sets, and (k) is not regular.

:::

:::

::: {.pf-step #p11}

Column 11 of the table, *Normal*: Y for (a) $S_\Omega$, (b) $\overline S_\Omega$, (d) ordered square, (e) $\RR_\ell$, (g) $\RR^\omega$, product, (h) $\RR^\omega$, uniform, N for the remaining 4, and left ? for (i) $\RR^\omega$, box.

::: pf-proof

Y for (a) by Theorem 32.4, a well-ordered set being normal in the order topology; for (b) by Theorem 32.3, a compact Hausdorff space being normal; for (d) by Exercise 32.8, every linear continuum being normal; for (e) by Example 2 of §31; and for (g) and (h) by Theorem 32.2, both being metrizable, Theorem 20.5 for the product topology and the uniform metric for the other. N for (c) by Example 2 of §32, for (f) by Example 3 of §31, for (j) by Exercise 32.9, an uncountable product of copies of $\RR$ being nonnormal, and for (k) because it is not even regular. The entry for (i) is left **?**: the book records the box-product question as open, in the remark attached to Exercise 32.5, together with Mary-Ellen Rudin's proof of normality, indeed of paracompactness, under the continuum hypothesis.

:::

:::

::: {.pf-step #p12}

Column 12 of the table, *First countable*: Y for (a) $S_\Omega$, (d) ordered square, (e) $\RR_\ell$, (f) $\RR_\ell^2$, (g) $\RR^\omega$, product, (h) $\RR^\omega$, uniform, (k) $\RR_K$, N for the remaining 4.

::: pf-proof

Y for (a) by Exercise 30.7, which asks which of the four countability axioms $S_\Omega$ satisfies and whose answer is the first alone; for (d) and (e) by Exercise 21.4; for (f) and (g) by Theorem 30.2, a countable product of first countable spaces being first countable, and Example 1 of §30 for the countable basis of (g); for (h) because the uniform metric is a metric and a metrizable space is first countable, §21; and for (k) because it is second countable, entry 13. N for (b) at the point $\Omega$; for (c) because the slice $\{\alpha\}\times\overline S_\Omega$, for any fixed $\alpha\in S_\Omega$, is homeomorphic to $\overline S_\Omega$, which is not first countable at $\Omega$, and first countability passes to subspaces, Theorem 30.2 --- the slice $S_\Omega\times\{\Omega\}$ would not serve, being homeomorphic to the first countable $S_\Omega$; and for (i) and (j) by the diagonal argument — countably many basic neighbourhoods of a point involve countably many coordinates in all, and a coordinate outside that countable set carries a cylinder containing none of them.

:::

:::

::: {.pf-step #p13}

Column 13 of the table, *Second countable*: Y for (g) $\RR^\omega$, product, (k) $\RR_K$, N for the remaining 9.

::: pf-proof

Y for (g) by Example 1 of §30 and for (k) by the countable basis consisting of the intervals $(a,b)$ and the sets $(a,b)-K$ with rational end points. N for the other nine: (a), (b), (c) by Exercise 30.7; (d) because it has no countable dense subset, entry 15, and a second countable space has one, Theorem 30.3(b); (e) by Example 3 of §30; and (f), (h), (i), (j) because each fails first countability, entry 12, and second countability implies it.

:::

:::

::: {.pf-step #p14}

Column 14 of the table, *Lindelöf*: Y for (b) $\overline S_\Omega$, (d) ordered square, (e) $\RR_\ell$, (g) $\RR^\omega$, product, (k) $\RR_K$, N for the remaining 6.

::: pf-proof

Y for (b) and (d) because both are compact, entry 5, and a compact space is Lindelöf, as Example 5 of §30 notes in passing; for (e) by Example 3 of §30; for (g) because it is metrizable and separable, hence second countable by Exercise 30.5(a), hence Lindelöf by Theorem 30.3(a); for (k) by Theorem 30.3(a) and entry 13. N for (a) by Exercise 30.7; for (c) because it is regular, entry 9, and not normal, entry 11, whereas a regular Lindelöf space is normal, Exercise 32.4; for (f) by Example 4 of §30; for (i) because the uncountable closed discrete subspace $\{0,1\}^\omega$ forces the failure — the cover by $X-A$ together with a neighbourhood of each point of $A$ meeting $A$ only there has no countable subcover; for (j) by Exercise 32.4 again, (j) being regular and not normal; for (h) because $\{0,1\}^\omega$ is an uncountable closed discrete subspace of $\RR^\omega$ in the uniform topology (Example 2 of §30), and a Lindelöf space has no uncountable closed discrete subspace: the cover by the complement of that subspace together with one open set about each of its points, meeting it only there, has no countable subcover.

:::

:::

::: {.pf-step #p15}

Column 15 of the table, *Countable dense subset*: Y for (e) $\RR_\ell$, (f) $\RR_\ell^2$, (g) $\RR^\omega$, product, (j) $\RR^I$, product, (k) $\RR_K$, N for the remaining 6.

::: pf-proof

Y for (e) by Example 3 of §30, the rationals being dense in $\RR_\ell$; for (f) because $\QQ^2$ is countable and dense in $\RR_\ell^2$ by Theorem 19.5; for (g) by Example 1 of §30 or by Exercise 30.10; for (j) by Exercise 30.16(a); for (k) by Theorem 30.3(b) and entry 13. N for (a) and (b) by Exercise 30.7, a countable set of ordinals being bounded and so not dense; for (c) because the projection of a countable dense set into $S_\Omega$ would be bounded by some $\gamma<\omega_1$, and then $(\gamma,\omega_1]\times\overline S_\Omega$ would miss it; for (d) because the sets $\{x\}\times(0,1)$, $x\in I$, are uncountably many pairwise disjoint open sets of the ordered square, which Exercise 30.13 forbids in a space with a countable dense subset; for (h) because the uncountable discrete subspace $\{0,1\}^\omega$ of Example 2 of §30 shows that no countable set is dense there, a discrete subspace of a second countable space being countable (Example 2 of §30) and (h) being metrizable, so Exercise 30.5(a) applies; for (i) by the diagonal argument, the point $x$ with $x_n=d^n_n+1$ having the box neighbourhood $\prod_n(x_n-\frac{1}{4},x_n+\frac{1}{4})$ free of the countably many points $d^k$.

:::

:::

::: {.pf-step #p16}

Column 16 of the table, *Locally metrizable*: Y for (a) $S_\Omega$, (g) $\RR^\omega$, product, (h) $\RR^\omega$, uniform, (k) $\RR_K$, N for the remaining 7.

::: pf-proof

Y for (a) by Exercise 42.2(a), each section $[0,\alpha]$ of $S_\Omega$ having a countable basis and hence, by Theorem 34.1, a metric; for (g) and (h) because both are metrizable; and for (k), where the point is that a small interval about a point off $K\cup\{0\}$ misses $K$, an interval about $1/n$ meets $K$ only in $1/n$ and the extra open sets $(c,d)-K$ are then unions of usual open intervals, and a basis element $(a,b)-K$ about $0$ carries the usual topology as a subspace because $(c,d)-K$ meets it in the usual open set $((a,b)\cap(c,d))-K$. N for the other seven: (b) because a neighbourhood of $\Omega$ contains a final segment $(\alpha,\omega_1]$, which is not first countable at $\omega_1$, a countable family of final segments being beaten by $(\sup_n\alpha_n,\omega_1]$, while a metrizable space is first countable; (c) because locally metrizable implies first countable and entry 12 is N; (d) because it is compact Hausdorff and would then be metrizable, Exercise 34.7, which Exercise 30.6 denies; (e) because it is regular and Lindelöf by Examples 2 of §31 and 3 of §30, so Exercise 34.8 would make it metrizable, which Exercise 30.6 denies; (f) because a basis element $[a,b)\times[c,d)$ is homeomorphic to $\RR_\ell^2$, which has the closed subspace $\RR_\ell\times\{0\}$ and is therefore not metrizable either, by Exercise 21.1 and Exercise 30.6; (i) because a basic neighbourhood is homeomorphic to $\RR^\omega$ in the box topology, which is not first countable; (j) because locally metrizable implies first countable and entry 12 is N.

:::

:::

::: {.pf-step #p17}

Column 17 of the table, *Metrizable*: Y for (g) $\RR^\omega$, product, (h) $\RR^\omega$, uniform, N for the remaining 9.

::: pf-proof

Y only for (g) by Theorem 20.5 and for (h), whose topology is given by the uniform metric. N for the other nine: (a) is limit point compact and not compact, so it is not metrizable by Theorem 28.2, which is the argument of Example 3 of §28; (b) is Example 3 of §28, where the sequence lemma fails at $\Omega$; (c) has the closed subspace $S_\Omega\times\{\Omega\}$ and metrizability passes to subspaces, Exercise 21.1; (d) and (e) are Exercise 30.6; (f) as in entry 16; (i) is Example 1 of §21, the box topology on $\RR^\omega$ being nonmetrizable; (j) is Example 2 of §21; (k) would be regular by Theorem 32.2, and it is not.

:::

:::

::: pf-step

Every entry of the table is as recorded: each column is settled by the result named for it above, and the eleven rows carry those verdicts.

::: pf-proof

Steps [](#p1){.pf-ref} to [](#p17){.pf-ref} dispose of the seventeen properties one column at a time, each entry of a column being settled by the argument given in that column's step; the entries are therefore exactly those of the table, with the single exception of the box-product normality question, which the table marks ? and which step [](#p11){.pf-ref} leaves open by design.

:::

:::

:::

:::

