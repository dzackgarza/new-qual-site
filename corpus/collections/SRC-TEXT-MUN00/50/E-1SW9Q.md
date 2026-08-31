---
schema: qual/card@1
id: E-1SW9Q
kind: exercise
title: The Prufer manifold
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
---

::: {.exercise}

There is a space that is locally 2-euclidean and satisfies (v) but not (iv) of Exercise 2. It is constructed as follows.
Let $A$ be the following subspace of $\mathbb{R}^3$:

$$
A = \ts{(x, y, 0) \mid x > 0}.
$$

Given $c$ real, let $B_c$ be the following subspace of $\mathbb{R}^3$:

$$
B_c = \ts{(x, y, c) \mid x \leq 0}.
$$

Let $X$ be the set that is the union of $A$ and all the spaces $B_c$, for $c$ real.
Topologize $X$ by taking as a basis all sets of the following three types:

(i) $U$, where $U$ is open in $A$.

(ii) $V$, where $V$ is open in the subspace of $B_c$ consisting of points with $x < 0$.

(iii) For each open interval $I = (a, b)$ of $\mathbb{R}$, each real number $c$, and each $\epsilon > 0$, the set $A_c(I, \epsilon) \cup B_c(I, \epsilon)$, where

$$
A_c(I, \epsilon) = \ts{(x, y, 0) \mid 0 < x < \epsilon \text{ and } c + ax < y < c + bx},
$$

$$
B_c(I, \epsilon) = \ts{(x, y, c) \mid -\epsilon < x \leq 0 \text{ and } a < y < b}.
$$

The space $X$ is called the "Prüfer manifold."

(a) Sketch the sets $A_c(I, \epsilon)$ and $B_c(I, \epsilon)$.

(b) Show the sets of types (i)-(iii) form a basis for a topology on $X$.

(c) Show the map $f_c: \mathbb{R}^2 \to X$ given by

$$
f_c(x, y) =
\begin{cases}
(x, c + xy, 0) & \text{for } x > 0, \\
(x, y, c) & \text{for } x \leq 0
\end{cases}
$$

defines a homeomorphism of $\mathbb{R}^2$ with the subspace $A \cup B_c$ of $X$.

(d) Show that $A \cup B_c$ is open in $X$; conclude that $X$ is 2-euclidean.

(e) Show that $X$ is Hausdorff.

(f) Show that $X$ is not normal.
[Hint: The subspace

$$
L = \ts{(0, 0, c) \mid c \in \mathbb{R}}
$$

of $X$ is closed and discrete.
Compare Example 3 of §31.]
:::

::: solution
**Goal:** Prove the foundational geometric and topological properties of the Prüfer manifold $X$, showing it is a locally 2-euclidean Hausdorff space that fails to be normal.

<1>1. Part (a) & (b): Geometric description and basis verification.
    *Proof:*
    <2>1. Description: In the right half-plane $A$ ($z=0, x>0$), $A_c(I, \varepsilon)$ is an open wedge radiating from $(0, c, 0)$ bounded by rays of slopes $a, b$ and width $x < \varepsilon$. In the sheet $B_c$ ($z=c, x \le 0$), $B_c(I, \varepsilon)$ is an open rectangular strip $(-\varepsilon, 0] \times (a, b) \times \{c\}$.
    <2>2. Covering: Every point in $A$ is covered by (i); every point in $B_c$ with $x < 0$ is covered by (ii); every boundary point $(0, y_0, c) \in B_c$ is covered by (iii) with $I = (y_0 - 1, y_0 + 1)$ and $\varepsilon = 1$.
    <2>3. Intersections: Intersections of type (i) with (i) or (iii) are open in $A$ (type (i)). Intersections of type (ii) with (ii) or (iii) on the same sheet $B_c$ are open in $B_c$ ($x<0$) (type (ii)). For two type (iii) sets with the same $c$, their intersection is $A_c(I_1 \cap I_2, \min(\varepsilon_1, \varepsilon_2)) \cup B_c(I_1 \cap I_2, \min(\varepsilon_1, \varepsilon_2))$ (type (iii)). For distinct $c_1 \neq c_2$, $B_{c_1} \cap B_{c_2} = \emptyset$, and the intersection in $A$ is open in $A$ (type (i)).
    <2>4. Thus types (i)-(iii) form a basis.

<1>2. Part (c) & (d): Homeomorphism $f_c: \mathbb{R}^2 \to A \cup B_c$ and local 2-euclidean structure.
    *Proof:*
    <2>1. $f_c$ is bijective from $\mathbb{R}^2$ onto $A \cup B_c$: on $x > 0$ it is the diffeomorphism onto $A$ of <2>2, on $x < 0$ it is the Cartesian identification onto $B_c$ of <2>3, and the two pieces meet only at $x = 0$, where $f_c(0, y) = (0, c, 0)$ is the single point of $A \cap B_c$; hence $f_c$ is injective and surjective onto $A \cup B_c$.
    <2>2. On $x > 0$, $f_c(x, y) = (x, c + xy, 0)$ is a smooth diffeomorphism onto $A$ with continuous inverse $(u, v, 0) \mapsto (u, \frac{v-c}{u})$.
    <2>3. On $x < 0$, $f_c(x, y) = (x, y, c)$ is the standard Cartesian identification.
    <2>4. At $x = 0$, the image of the basic product neighborhood $(-\varepsilon, \varepsilon) \times (a, b) \subset \mathbb{R}^2$ under $f_c$ is precisely $A_c((a, b), \varepsilon) \cup B_c((a, b), \varepsilon)$, which is the type (iii) basis element of $X$.
    <2>5. Thus $f_c$ is a homeomorphism of $\mathbb{R}^2$ onto $A \cup B_c$.
    <2>6. For any $p \in A \cup B_c$, $p$ possesses a basis neighborhood contained in $A \cup B_c$, so $A \cup B_c$ is open in $X$. Since $\{A \cup B_c : c \in \mathbb{R}\}$ is an open cover of $X$ by Euclidean planes $\mathbb{R}^2$, $X$ is locally 2-euclidean.

<1>3. Part (e): $X$ is Hausdorff.
    *Proof:*
    <2>1. Distinct points in the same sheet $A \cup B_c$ are separated because $A \cup B_c \cong \mathbb{R}^2$ is Hausdorff.
    <2>2. Points $p \in B_{c_1}$ and $q \in B_{c_2}$ with $c_1 \neq c_2$:
        - If $x(p) < 0$ or $x(q) < 0$, disjoint type (ii) neighborhoods separate them.
        - If $p = (0, y_1, c_1)$ and $q = (0, y_2, c_2)$, choose open intervals $I_1 = (y_1 - 1, y_1 + 1) = (a_1, b_1)$ and $I_2 = (y_2 - 1, y_2 + 1) = (a_2, b_2)$.
        - Without loss of generality, assume $c_1 < c_2$. Choose $\varepsilon > 0$ such that $\varepsilon < \frac{c_2 - c_1}{b_1 - a_2}$ (if $b_1 > a_2$, or any $\varepsilon > 0$ otherwise).
        - Then for all $0 < x < \varepsilon$, $c_1 + b_1 x < c_2 + a_2 x$, which guarantees that the wedges $A_{c_1}(I_1, \varepsilon)$ and $A_{c_2}(I_2, \varepsilon)$ are disjoint.
        - Since $B_{c_1} \cap B_{c_2} = \emptyset$, the type (iii) neighborhoods of $p$ and $q$ are completely disjoint.
    <2>3. Thus $X$ is Hausdorff.

<1>4. Part (f): $X$ is not normal.
    *Proof:*
    <2>1. The subspace $L = \{(0, 0, c) : c \in \mathbb{R}\} \subset X$ is closed and discrete, since each basic neighborhood $A_c((-1, 1), 1) \cup B_c((-1, 1), 1)$ contains only the point $(0, 0, c)$ of $L$.
    <2>2. The cardinality of $L$ is $|L| = |\mathbb{R}| = 2^{\aleph_0} = \mathfrak{c}$.
    <2>3. The countable set $D = (\mathbb{Q}_+ \times \mathbb{Q}) \times \{0\} \subset A$ is dense in $X$, because every open set of type (i) and type (iii) intersects $A$ in a non-empty open subset containing points of $D$. Thus $X$ is separable.
    <2>4. By Jones' Lemma, a separable space containing a closed discrete subspace of cardinality $2^{\aleph_0}$ cannot be normal.
    <2>5. Therefore $X$ is not normal. Q.E.D.
:::
