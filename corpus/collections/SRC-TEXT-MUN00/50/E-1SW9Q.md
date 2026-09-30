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
---

::: {.exercise}

There is a space that is locally 2-euclidean and satisfies (v) but not (iv) of Exercise 2. It is constructed as follows.
Let $A$ be the following subspace of $\mathbb{R}^3$:

$$
A = \theset{(x, y, 0) \mid x > 0}.
$$

Given $c$ real, let $B_c$ be the following subspace of $\mathbb{R}^3$:

$$
B_c = \theset{(x, y, c) \mid x \leq 0}.
$$

Let $X$ be the set that is the union of $A$ and all the spaces $B_c$, for $c$ real.
Topologize $X$ by taking as a basis all sets of the following three types:

(i) $U$, where $U$ is open in $A$.

(ii) $V$, where $V$ is open in the subspace of $B_c$ consisting of points with $x < 0$.

(iii) For each open interval $I = (a, b)$ of $\mathbb{R}$, each real number $c$, and each $\epsilon > 0$, the set $A_c(I, \epsilon) \cup B_c(I, \epsilon)$, where

$$
A_c(I, \epsilon) = \theset{(x, y, 0) \mid 0 < x < \epsilon \text{ and } c + ax < y < c + bx},
$$

$$
B_c(I, \epsilon) = \theset{(x, y, c) \mid -\epsilon < x \leq 0 \text{ and } a < y < b}.
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
L = \theset{(0, 0, c) \mid c \in \mathbb{R}}
$$

of $X$ is closed and discrete.
Compare Example 3 of §31.]
:::

::: {.solution}

::: pf

::: pf-step

Part (a) & (b): Geometric description and basis verification.
    *Proof:*

::: pf-proof

::: pf-step

Description: In the right half-plane $A$ ($z=0, x>0$), $A_c(I, \varepsilon)$ is an open wedge radiating from $(0, c, 0)$ bounded by rays of slopes $a, b$ and width $x < \varepsilon$. In the sheet $B_c$ ($z=c, x \le 0$), $B_c(I, \varepsilon)$ is an open rectangular strip $(-\varepsilon, 0] \times (a, b) \times \{c\}$.

:::

::: pf-step

Covering: Every point in $A$ is covered by (i); every point in $B_c$ with $x < 0$ is covered by (ii); every boundary point $(0, y_0, c) \in B_c$ is covered by (iii) with $I = (y_0 - 1, y_0 + 1)$ and $\varepsilon = 1$.

:::

::: pf-step

Intersections: Intersections of type (i) with (i) or (iii) are open in $A$ (type (i)). Intersections of type (ii) with (ii) or (iii) on the same sheet $B_c$ are open in $B_c$ ($x<0$) (type (ii)). For two type (iii) sets with the same $c$, their intersection is $A_c(I_1 \cap I_2, \min(\varepsilon_1, \varepsilon_2)) \cup B_c(I_1 \cap I_2, \min(\varepsilon_1, \varepsilon_2))$ (type (iii)). For distinct $c_1 \neq c_2$, $B_{c_1} \cap B_{c_2} = \emptyset$, and the intersection in $A$ is open in $A$ (type (i)).

:::

::: pf-step

Thus types (i)-(iii) form a basis.

:::

:::

:::

::: pf-step

Part (c) & (d): Homeomorphism $f_c: \mathbb{R}^2 \to A \cup B_c$ and local 2-euclidean structure.
    *Proof:*

::: pf-proof

::: pf-step

$f_c$ is bijective from $\mathbb{R}^2$ onto $A \cup B_c$: on $x > 0$ it is the bijection onto $A$ of step [](#s2-2){.pf-ref}, on $x \le 0$ it is the bijection $(x, y) \mapsto (x, y, c)$ onto $B_c$, and the images $A$ (third coordinate $0$, $x > 0$) and $B_c$ ($x \le 0$) are disjoint.

:::

::: {.pf-step #s2-2}

On $x > 0$, $f_c(x, y) = (x, c + xy, 0)$ is a smooth diffeomorphism onto $A$ with continuous inverse $(u, v, 0) \mapsto (u, \frac{v-c}{u})$.

:::

::: pf-step

On $x < 0$, $f_c(x, y) = (x, y, c)$ is the standard Cartesian identification.

:::

::: pf-step

At $x = 0$, the image of the basic product neighborhood $(-\varepsilon, \varepsilon) \times (a, b) \subset \mathbb{R}^2$ under $f_c$ is precisely $A_c((a, b), \varepsilon) \cup B_c((a, b), \varepsilon)$, which is the type (iii) basis element of $X$.

:::

::: pf-step

Thus $f_c$ is a homeomorphism of $\mathbb{R}^2$ onto $A \cup B_c$.

:::

::: pf-step

For any $p \in A \cup B_c$, $p$ possesses a basis neighborhood contained in $A \cup B_c$, so $A \cup B_c$ is open in $X$. Since $\{A \cup B_c : c \in \mathbb{R}\}$ is an open cover of $X$ by Euclidean planes $\mathbb{R}^2$, $X$ is locally 2-euclidean.

:::

:::

:::

::: pf-step

Part (e): $X$ is Hausdorff.
    *Proof:*

::: pf-proof

::: pf-step

Distinct points in the same sheet $A \cup B_c$ are separated because $A \cup B_c \cong \mathbb{R}^2$ is Hausdorff.

:::

::: pf-step

Points $p \in B_{c_1}$ and $q \in B_{c_2}$ with $c_1 \neq c_2$:
        - If $x(p) < 0$ or $x(q) < 0$, disjoint type (ii) neighborhoods separate them.
        - If $p = (0, y_1, c_1)$ and $q = (0, y_2, c_2)$, choose open intervals $I_1 = (y_1 - 1, y_1 + 1) = (a_1, b_1)$ and $I_2 = (y_2 - 1, y_2 + 1) = (a_2, b_2)$.
        - Without loss of generality, assume $c_1 < c_2$. Choose $\varepsilon > 0$ such that $\varepsilon < \frac{c_2 - c_1}{b_1 - a_2}$ (if $b_1 > a_2$, or any $\varepsilon > 0$ otherwise).
        - Then for all $0 < x < \varepsilon$, $c_1 + b_1 x < c_2 + a_2 x$, which guarantees that the wedges $A_{c_1}(I_1, \varepsilon)$ and $A_{c_2}(I_2, \varepsilon)$ are disjoint.
        - Since $B_{c_1} \cap B_{c_2} = \emptyset$, the type (iii) neighborhoods of $p$ and $q$ are completely disjoint.

:::

::: pf-step

Thus $X$ is Hausdorff.

:::

:::

:::

::: pf-step

Part (f): $X$ is not normal.
    *Proof:*

::: pf-proof

::: {.pf-step #s4-1}

The subspace $L = \{(0, 0, c) : c \in \mathbb{R}\} \subset X$ is closed and discrete, since each basic neighborhood $A_c((-1, 1), 1) \cup B_c((-1, 1), 1)$ contains only the point $(0, 0, c)$ of $L$.

:::

::: {.pf-step #s4-2}

$L$ is closed: a point of $A$ has a type (i) neighborhood, a point of $B_c$ with $x < 0$ has a type (ii) neighborhood, and a point $(0, y, c)$ with $y \neq 0$ has a type (iii) neighborhood with $0 \notin I$; none of these meets $L$.

:::

::: {.pf-step #s4-3}

The countable set $D = (\mathbb{Q}_+ \times \mathbb{Q}) \times \{0\} \subset A$ meets every neighborhood of every point of $L$, because each such neighborhood contains a type (iii) set, whose part $A_c(I, \varepsilon)$ is a nonempty open subset of the half-plane $A$.

:::

::: {.pf-step #s4-4}

Suppose $X$ is normal. For each $S \subseteq L$, the sets $S$ and $L \setminus S$ are closed in $X$ by steps [](#s4-1){.pf-ref} and [](#s4-2){.pf-ref}, so there are disjoint open sets $U_S \supseteq S$ and $V_S \supseteq L \setminus S$. If $S \neq T$, say $p \in S \setminus T$, then $U_S \cap V_T$ is a neighborhood of $p$, so it contains a point of $D$ by step [](#s4-3){.pf-ref}; that point lies in $U_S \cap D$ and not in $U_T \cap D$. Hence $S \mapsto U_S \cap D$ is an injective map from the power set of $L$ to the power set of $D$.

:::

::: pf-step

The power set of $L$ has cardinality $2^{\mathfrak{c}}$ and the power set of the countable set $D$ has cardinality $\mathfrak{c} < 2^{\mathfrak{c}}$, which contradicts step [](#s4-4){.pf-ref}. Therefore $X$ is not normal. Q.E.D.

:::

:::

:::

:::

:::
