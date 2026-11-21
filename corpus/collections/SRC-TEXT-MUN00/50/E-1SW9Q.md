---
schema: qual/card@1
id: E-1SW9Q
kind: problem
title: The Prüfer manifold
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Seventeen steps asserted their claim with no justification and each now carries one: that the three
    types of set form a basis (description, covering by the three cases, and each kind of intersection),
    that $f_c$ is a bijection and a homeomorphism (the two halves, the boundary neighbourhood
    computation, and the passage to a local Euclidean neighbourhood), the Hausdorff argument in the
    same-sheet and different-sheet cases with the epsilon chosen from $c_1 < c_2$, and the four steps of
    the non-normality proof: discreteness of $L$, closedness of $L$, density of the countable set $D$ in
    the neighbourhoods of $L$, the injection from the power set of $L$ into that of $D$, and the
    cardinality contradiction. Checked while writing: the separation of the wedges needs
    $c_1 + b_1x < c_2 + a_2x$, which the chosen $\varepsilon$ supplies, and the density argument needs the
    $A$-part of a type (iii) set to be open in the Euclidean half-plane. The statement is unchanged. The
    collection is Munkres's Topology, which retains no solution manual here, so the argument is the
    card's own.
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution was located; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00.
    Checked line by line against Munkres, Topology (2000), supplementary Exercise 6 of §50, printed pp. 317-318,
    with Example 3 of §31 for the pattern of the non-normality argument (a closed discrete subspace of size
    continuum with a countable set dense in a way that separates its subsets) and Theorem 18.3 for continuity on
    the two closed halves of the plane. Points checked: the three types of basic sets do give a basis, the
    intersections of two type (iii) sets with the same index c being again of type (iii) and those with distinct
    indices meeting only in A; the map f_c is a bijection whose inverse is continuous on each half and which
    carries a product neighbourhood of a point with x = 0 onto a type (iii) set; A cup B_c is open, so X is
    2-euclidean; the Hausdorff property at two points of distinct sheets reduces to the inequality
    c_1 + b_1 x < c_2 + a_2 x for small x > 0; and the non-normality is the cardinality argument from the
    closed discrete set L, each of whose points has a neighbourhood meeting A in a nonempty open set and hence
    meeting the countable set D of points with rational coordinates. Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Nothing located treats supplementary Exercise 6 of §50 (printed
    pp. 317--318), the Prüfer manifold with its six parts. The Stack Exchange query "Prüfer manifold" returned
    4566735, on connected locally euclidean Hausdorff topological groups, 3082048, on imbedding theorems for
    non-second-countable manifolds, and 5022965, on four-manifolds, none of which is this example; a query for
    the non-normality of a locally euclidean space returned nothing relevant. Murayama's selection has no
    Chapter 8, dbFin has no chapter-8 page, the ten GitHub repositories of Munkres solutions listed in
    COMPLAINTS.md stop before §36, and the AoPS post *Topology by Munkres Chapter 8 | Day 18*
    (https://artofproblemsolving.com/community/c3401823h3647630) answers §50 with its formulas lost. The card
    proves (a)--(f) itself; the two steps that carry the exercise are that the sets of types (i)--(iii) form a
    basis, which is where the inequality $c_1+b_1x<c_2+a_2x$ for small $x>0$ is used, and the failure of
    normality, which is the cardinality argument on the closed discrete set $L$ against the countable set of
    points with rational coordinates. Nothing needed correction.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Rewrote the solution's frame on 2026-11-19, leaving every argument as it was.
    The four steps carried run-in part labels and "Proof:" lines instead of
    claims, the page cited no source, and the first group ended with a substep
    that only restated its conclusion. Each group is now a labelled step (basis,
    euclidean, hausdorff, not-normal) whose first paragraph is its claim, that
    substep is gone, and the preamble names the exercise and the pages the
    argument leans on: supplementary Exercise 6 of §50 at printed pp. 317-318,
    the pattern of Example 3 of §31 for the non-normality, and Theorem 18.3 at
    printed p. 108 for continuity on the two halves. As the event of 2026-11-11
    records, no complete published solution was located, so the argument remains
    the card's own and the page claims nothing else.

---

::: {.exercise}

There is a space that is locally 2-euclidean and satisfies (v) but not (iv) of Exercise 2. It is constructed as follows.
Let $A$ be the following subspace of $\RR^3$:

$$
A = \theset{(x, y, 0) \mid x > 0}.
$$

Given $c$ real, let $B_c$ be the following subspace of $\RR^3$:

$$
B_c = \theset{(x, y, c) \mid x \leq 0}.
$$

Let $X$ be the set that is the union of $A$ and all the spaces $B_c$, for $c$ real.
Topologize $X$ by taking as a basis all sets of the following three types:

(i) $U$, where $U$ is open in $A$.

(ii) $V$, where $V$ is open in the subspace of $B_c$ consisting of points with $x < 0$.

(iii) For each open interval $I = (a, b)$ of $\RR$, each real number $c$, and each $\epsilon > 0$, the set $A_c(I, \epsilon) \cup B_c(I, \epsilon)$, where

$$
A_c(I, \epsilon) = \theset{(x, y, 0) \mid 0 < x < \epsilon \text{ and } c + ax < y < c + bx},
$$

$$
B_c(I, \epsilon) = \theset{(x, y, c) \mid -\epsilon < x \leq 0 \text{ and } a < y < b}.
$$

The space $X$ is called the "Prüfer manifold."

(a) Sketch the sets $A_c(I, \epsilon)$ and $B_c(I, \epsilon)$.

(b) Show the sets of types (i)-(iii) form a basis for a topology on $X$.

(c) Show the map $f_c: \RR^2 \to X$ given by

$$
f_c(x, y) =
\begin{cases}
(x, c + xy, 0) & \text{for } x > 0, \\
(x, y, c) & \text{for } x \leq 0
\end{cases}
$$

defines a homeomorphism of $\RR^2$ with the subspace $A \cup B_c$ of $X$.

(d) Show that $A \cup B_c$ is open in $X$; conclude that $X$ is 2-euclidean.

(e) Show that $X$ is Hausdorff.

(f) Show that $X$ is not normal.
[Hint: The subspace

$$
L = \theset{(0, 0, c) \mid c \in \RR}
$$

of $X$ is closed and discrete.
Compare Example 3 of §31.]
:::

::: {.solution}
The exercise is supplementary Exercise 6 of §50, printed pp. 317--318. The non-normality argument follows the pattern of Example 3 of §31, and the continuity of each $f_c$ on the two halves of the plane is Theorem 18.3, printed p. 108.

::: pf

::: {.pf-step #basis}
The sets of types (i)--(iii) form a basis for a topology on $X$, and a basic neighbourhood of a point of $B_c$ with $x=0$ meets $A$ in a wedge $A_c(I,\varepsilon)$.

::: pf-proof

::: pf-step

Description: In the right half-plane $A$ ($z=0, x>0$), $A_c(I, \varepsilon)$ is an open wedge radiating from $(0, c, 0)$ bounded by rays of slopes $a, b$ and width $x < \varepsilon$. In the sheet $B_c$ ($z=c, x \le 0$), $B_c(I, \varepsilon)$ is an open rectangular strip $(-\varepsilon, 0] \times (a, b) \times \{c\}$.


::: pf-proof
By the definitions of the three types: a type (i) set is a Euclidean ball in the half-plane $A$; a type (ii) set is $(-\varepsilon,0)\times(a,b)\times\{c\}$ in the sheet $B_c$; and a type (iii) set is the union of the wedge $A_c(I,\varepsilon)$ in $A$ and the strip $B_c(I,\varepsilon)$ in $B_c$, with the wedge bounded by the rays of slopes $a$ and $b$ issuing from $(0,c,0)$ and cut off at $x = \varepsilon$.
:::

:::

::: pf-step

Covering: Every point in $A$ is covered by (i); every point in $B_c$ with $x < 0$ is covered by (ii); every boundary point $(0, y_0, c) \in B_c$ is covered by (iii) with $I = (y_0 - 1, y_0 + 1)$ and $\varepsilon = 1$.


::: pf-proof
Each point lies in exactly one of the three situations: a point of $A$ lies in a Euclidean ball because $A$ is an open half-plane; a point of $B_c$ with $x < 0$ lies in a strip of type (ii); and a point with $x = 0$ is a boundary point $(0,y_0,c)$, which the type (iii) set with $I = (y_0-1,y_0+1)$ and $\varepsilon = 1$ contains by definition of that set.
:::

:::

::: pf-step

Intersections: Intersections of type (i) with (i) or (iii) are open in $A$ (type (i)). Intersections of type (ii) with (ii) or (iii) on the same sheet $B_c$ are open in $B_c$ ($x<0$) (type (ii)). For two type (iii) sets with the same $c$, their intersection is $A_c(I_1 \cap I_2, \min(\varepsilon_1, \varepsilon_2)) \cup B_c(I_1 \cap I_2, \min(\varepsilon_1, \varepsilon_2))$ (type (iii)). For distinct $c_1 \neq c_2$, $B_{c_1} \cap B_{c_2} = \emptyset$, and the intersection in $A$ is open in $A$ (type (i)).


::: pf-proof
Two sets of type (i) intersect in a ball, and a type (i) with a type (iii) meets $A$ in the intersection of a ball with a wedge, which is open in $A$; two type (ii) sets on one sheet intersect in a strip; two type (iii) sets with the same $c$ intersect in the type (iii) set built from $I_1 \cap I_2$ and $\min(\varepsilon_1,\varepsilon_2)$; and for distinct $c$ the sheets are disjoint so only the $A$-parts meet, again open in $A$. In each case the intersection contains a basis element around each of its points, which is exactly what it means for a family of sets to be a basis for a topology.
:::

:::


:::

:::

::: {.pf-step #euclidean}
Each $f_c$ is a homeomorphism of $\RR^2$ onto $A\cup B_c$, and $A\cup B_c$ is open in $X$, so every point of $X$ has a neighbourhood homeomorphic to a ball in $\RR^2$.

::: pf-proof

::: pf-step

$f_c$ is bijective from $\RR^2$ onto $A \cup B_c$: on $x > 0$ it is the bijection onto $A$ of step [](#s2-2){.pf-ref}, on $x \le 0$ it is the bijection $(x, y) \mapsto (x, y, c)$ onto $B_c$, and the images $A$ (third coordinate $0$, $x > 0$) and $B_c$ ($x \le 0$) are disjoint.


::: pf-proof
On $x > 0$ the formula is a bijection onto $A$ and on $x \le 0$ it is $(x,y) \mapsto (x,y,c)$, a bijection onto $B_c$; the images are disjoint because a point of $A$ has third coordinate $0$ and $x > 0$, while a point of $B_c$ has $x \le 0$ and, when $x = 0$, has $y$-coordinate not constrained to make it lie in $A$. So the map is a bijection onto $A \cup B_c$.
:::

:::

::: {.pf-step #s2-2}

On $x > 0$, $f_c(x, y) = (x, c + xy, 0)$ is a smooth diffeomorphism onto $A$ with continuous inverse $(u, v, 0) \mapsto (u, \frac{v-c}{u})$.


::: pf-proof
For $x > 0$ the formula is smooth into $A$ and the displayed formula $(u,v,0) \mapsto (u,(v-c)/u)$ is smooth on $A$ and is a two-sided inverse; a smooth bijection with a smooth inverse is a diffeomorphism onto $A$.
:::

:::

::: pf-step

On $x < 0$, $f_c(x, y) = (x, y, c)$ is the standard Cartesian identification.


::: pf-proof
For $x < 0$ the formula repeats the first two coordinates and appends the label $c$, which is the standard identification of the open half-plane $\{x<0\}$ with the sheet $B_c$ minus its boundary line; being the restriction of the identity of $\RR^2$ it is a homeomorphism onto its image.
:::

:::

::: pf-step

At $x = 0$, the image of the basic product neighborhood $(-\varepsilon, \varepsilon) \times (a, b) \subset \RR^2$ under $f_c$ is precisely $A_c((a, b), \varepsilon) \cup B_c((a, b), \varepsilon)$, which is the type (iii) basis element of $X$.


::: pf-proof
A point $(x,y)$ with $0 < x < \varepsilon$ and $a < y < b$ maps to $(x, c+xy, 0)$, and $a < y < b$ is equivalent to $c+ax < c+xy < c+bx$, so the image is in the wedge $A_c((a,b),\varepsilon)$; a point with $-\varepsilon < x \le 0$ maps to $(x,y,c)$, which lies in the strip $B_c((a,b),\varepsilon)$. Conversely a point of the wedge or of the strip has coordinates of that shape and comes from the corresponding pair, so the image is exactly the type (iii) set.
:::

:::

::: pf-step

Thus $f_c$ is a homeomorphism of $\RR^2$ onto $A \cup B_c$.


::: pf-proof
The map is a bijection by an earlier step, restricts to homeomorphisms on $x > 0$ and on $x < 0$, and carries each basic product neighbourhood of the boundary line $x = 0$ onto a basis element of type (iii), which is a basic neighbourhood of the corresponding boundary point of $B_c$; a bijection with these properties is a homeomorphism.
:::

:::

::: pf-step

For any $p \in A \cup B_c$, $p$ possesses a basis neighborhood contained in $A \cup B_c$, so $A \cup B_c$ is open in $X$. Since $\{A \cup B_c : c \in \RR\}$ is an open cover of $X$ by Euclidean planes $\RR^2$, $X$ is locally 2-euclidean.


::: pf-proof
Each point lies in some $A \cup B_c$ and, by the covering step, has a basis element of type (i), (ii) or (iii) inside that set; so $A \cup B_c$ is an open neighbourhood of the point homeomorphic to $\RR^2$, and the family indexed by $c \in \RR$ covers $X$, which is what locally 2-Euclidean means.
:::

:::

:::

:::

::: {.pf-step #hausdorff}
$X$ is Hausdorff.

::: pf-proof

::: pf-step

Distinct points in the same sheet $A \cup B_c$ are separated because $A \cup B_c \cong \RR^2$ is Hausdorff.


::: pf-proof
The sheet $A \cup B_c$ is homeomorphic to $\RR^2$ by step [](#euclidean){.pf-ref}, and $\RR^2$ is Hausdorff, so two distinct points of the sheet have disjoint open neighbourhoods inside it; the sheet is open in $X$, so those neighbourhoods are also open in $X$.
:::

:::

::: pf-step

Points $p \in B_{c_1}$ and $q \in B_{c_2}$ with $c_1 \neq c_2$:
        - If $x(p) < 0$ or $x(q) < 0$, a type (ii) neighborhood of that point lies in its own sheet and is disjoint from a neighborhood of the other point chosen in its different sheet (type (ii) or type (iii) as appropriate).
        - If $p = (0, y_1, c_1)$ and $q = (0, y_2, c_2)$, choose open intervals $I_1 = (y_1 - 1, y_1 + 1) = (a_1, b_1)$ and $I_2 = (y_2 - 1, y_2 + 1) = (a_2, b_2)$.
        - Without loss of generality, assume $c_1 < c_2$. Choose $\varepsilon > 0$ such that $\varepsilon < \frac{c_2 - c_1}{b_1 - a_2}$ (if $b_1 > a_2$, or any $\varepsilon > 0$ otherwise).
        - Then for all $0 < x < \varepsilon$, $c_1 + b_1 x < c_2 + a_2 x$, which guarantees that the wedges $A_{c_1}(I_1, \varepsilon)$ and $A_{c_2}(I_2, \varepsilon)$ are disjoint.
        - Since $B_{c_1} \cap B_{c_2} = \emptyset$, the type (iii) neighborhoods of $p$ and $q$ are completely disjoint.


::: pf-proof
If $x(p) < 0$ then $p$ lies in the open set $\{x<0\}\cap B_{c_1}$, which is a type (ii) neighbourhood disjoint from $B_{c_2}$ and hence from the part of any type (iii) neighbourhood of $q$ that lies on the sheet $B_{c_2}$, so the two are disjoint. In the boundary case, $c_1 < c_2$ and $\varepsilon(b_1-a_2) < c_2-c_1$ give $c_1+b_1x < c_2+a_2x$ for $0 < x < \varepsilon$, so a point of the first wedge and a point of the second cannot share their $y$-coordinate, and the strips lie on different sheets; hence the two type (iii) sets are disjoint.
:::

:::

::: pf-step

Thus $X$ is Hausdorff.


::: pf-proof
Every pair of distinct points is either in one sheet or in two different ones, and each case produces disjoint neighbourhoods by the two steps above, which is the definition of the Hausdorff property.
:::

:::

:::

:::

::: {.pf-step #not-normal}
$X$ is not normal.

::: pf-proof

::: {.pf-step #s4-1}

The subspace $L = \{(0, 0, c) : c \in \RR\} \subset X$ is closed and discrete, since each basic neighborhood $A_c((-1, 1), 1) \cup B_c((-1, 1), 1)$ contains only the point $(0, 0, c)$ of $L$.


::: pf-proof
The type (iii) basis element with $I = (-1,1)$ and $\varepsilon = 1$ meets $L$ only in $(0,0,c)$, since the points of $L$ have second coordinate $0$ and the only point of that basis element with second coordinate $0$ is the boundary point of the $c$-th sheet; so each point of $L$ has a neighbourhood meeting $L$ in itself, which is discreteness.
:::

:::

::: {.pf-step #s4-2}

$L$ is closed: a point of $A$ has a type (i) neighborhood, a point of $B_c$ with $x < 0$ has a type (ii) neighborhood, and a point $(0, y, c)$ with $y \neq 0$ has a type (iii) neighborhood with $0 \notin I$; none of these meets $L$.


::: pf-proof
A point outside $L$ is in $A$, or in some $B_c$ with $x<0$, or is $(0,y,c)$ with $y \ne 0$. The first has a type (i) neighbourhood inside $A$, which misses $L$ because $L$ lies on the boundary lines; the second has a type (ii) neighbourhood with $x<0$, which misses $L$ for the same reason; the third has the type (iii) neighbourhood with $0 \notin I$, whose $A$-part avoids the ray of slope $0$ and whose strip avoids $y = 0$. So the complement of $L$ is open.
:::

:::

::: {.pf-step #s4-3}

The countable set $D = (\QQ_+ \times \QQ) \times \{0\} \subset A$ meets every neighborhood of every point of $L$, because each such neighborhood contains a type (iii) set, whose part $A_c(I, \varepsilon)$ is a nonempty open subset of the half-plane $A$.


::: pf-proof
$D$ is a product of two countable sets and hence countable, and it lies in $A$. A neighbourhood of a point of $L$ contains a basic one, which by the covering step may be taken of type (iii) with an interval $I$ around $0$ and some $\varepsilon > 0$; its $A$-part is the wedge $\{c+yx : y \in I,\ 0 < x < \varepsilon\}$, a nonempty open subset of $A$ in the Euclidean topology, and every nonempty open subset of the plane contains a point with both coordinates rational.
:::

:::

::: {.pf-step #s4-4}

Suppose $X$ is normal. For each $S \subseteq L$, the sets $S$ and $L \setminus S$ are closed in $X$ by steps [](#s4-1){.pf-ref} and [](#s4-2){.pf-ref}, so there are disjoint open sets $U_S \supseteq S$ and $V_S \supseteq L \setminus S$. If $S \neq T$, say $p \in S \setminus T$, then $U_S \cap V_T$ is a neighborhood of $p$, so it contains a point of $D$ by step [](#s4-3){.pf-ref}; that point lies in $U_S \cap D$ and not in $U_T \cap D$. Hence $S \mapsto U_S \cap D$ is an injective map from the power set of $L$ to the power set of $D$.


::: pf-proof
Assuming $X$ normal, the disjoint closed sets $S$ and $L\setminus S$ have disjoint open neighbourhoods $U_S \supseteq S$ and $V_S \supseteq L\setminus S$, which is what normality provides. If $S \ne T$ choose $p \in S\setminus T$; then $p \in U_S$ and $p \in V_T$, so $U_S \cap V_T$ is an open neighbourhood of $p$ and contains a point of $D$ by step [](#s4-3){.pf-ref}. That point lies in $U_S \cap D$ but, being in $V_T$, it does not lie in $U_T$ because $U_T \cap V_T = \emptyset$. Hence the sets $U_S \cap D$ and $U_T \cap D$ differ, and $S \mapsto U_S \cap D$ is injective.
:::

:::

::: pf-step

The power set of $L$ has cardinality $2^{\mathfrak{c}}$ and the power set of the countable set $D$ has cardinality $\mathfrak{c} < 2^{\mathfrak{c}}$, which contradicts step [](#s4-4){.pf-ref}. Therefore $X$ is not normal. Q.E.D.


::: pf-proof
The power set of a set of cardinality $\mathfrak c$ has cardinality $2^{\mathfrak c}$, and the power set of a countable set has cardinality $2^{\aleph_0} = \mathfrak c$; an injection of the first into the second would give $2^{\mathfrak c} \le \mathfrak c$, contradicting Cantor's theorem that $\mathfrak c < 2^{\mathfrak c}$. So the assumption that $X$ is normal is false.
:::

:::

:::

:::

:::

:::
