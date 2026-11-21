---
schema: qual/card@1
id: E-AY5GK
kind: problem
title: Topologically complete spaces
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Parts (a) and (c) are transcribed from the located published solution: "Solutions to exercises for
    Mathematics 205A" (University of California, Riverside, Fall 2014), Part 3, section "III.2: Complete
    metric spaces", answers to Munkres §43 Exercise 6 (printed p. 270)(a) and 6(c) on the set's own printed p. 5 (in
    tmp/sources/munkres-solutions-ucr-math205-gentop.pdf, PDF p. 46; the file names no author, so the
    course and the file are the attribution). Part (a) is the set's: a Cauchy sequence of a closed
    subspace is Cauchy in the complete space and its limit lies in the closed subspace. Part (c) is the
    set's strategy from the book's hint: imbed U homeomorphically as the graph of phi(x) = 1/d(x, X - U)
    in X x R, which is complete, and show the graph closed by separating the three cases t < 0, t = 0 and
    t > 0 for a point (x,t) of its closure with x on the boundary of U; the card instead proves the graph
    closed by the single observation that d(x_k, F) -> 0 would force phi(x_k) -> infinity, which is the
    same three cases in one stroke. Parts (b) and (d) are the card's own, checked against the book: (b)
    with the metric sum 2^{-n} d-bar_n on the product, which induces the product topology by Theorem 20.5,
    coordinates of a Cauchy sequence being Cauchy and the product convergence following; (d) with the
    diagonal imbedding of A into the product of the open sets U_n, whose image is closed because it is the
    intersection of the closed conditions u_n = u_{n+1}, the space X being Hausdorff. Checked against
    Munkres, Topology (2000), §43 Exercise 6, printed p. 270, with Theorem 20.5, Theorem 43.5, Theorem
    43.2 and Exercise 17.13 (X Hausdorff iff the diagonal is closed), and the conclusion that the
    irrationals are topologically complete from the expression of the irrationals as a countable
    intersection of open sets.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Rewrote the solution's frame on 2026-11-19, leaving every argument as it was.
    The five steps carried run-in part labels and "Proof:" lines instead of
    claims, and the page cited no source. Each is now a labelled step (closed,
    product, open, g-delta, irrationals) whose first paragraph is its claim, and
    the preamble names the exercise (Section 43 Exercise 6, printed p. 270) and
    what is transcribed and what is the card's own: parts (a) and (c) follow the
    University of California, Riverside Mathematics 205A set, Part 3, answers to
    Exercise 6(a) and 6(c), printed p. 5 of that set, as the event of 2026-11-11
    records, and parts (b) and (d) are the card's own following the hints. No
    statement, argument or citation changes.

- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof. The card had 41 steps and 36 of them asserted their claim with no
    justification; each now carries one, and the five container steps keep their nested steps. Checked
    against Munkres, Topology (2000), section 43 Exercise 3, printed p. 271, with the facts the parts
    rest on: the restriction of a metric to a subset induces the subspace topology, the metric
    sum 2^{-n} min{1,d_n} induces the product topology, a positive continuous function has a continuous
    reciprocal, and the graph of x -> 1/d(x,F) is closed in X x R because the distance to F tends to 0 at
    the boundary while the second coordinate stays bounded. In part (d) the closedness of the coordinate
    equality sets uses that X, being metrizable, is Hausdorff. Nothing in the statement was changed.

---

::: {.exercise}

A space $X$ is said to be topologically complete if there exists a metric for the topology of $X$ relative to which $X$ is complete.

(a) Show that a closed subspace of a topologically complete space is topologically complete.

(b) Show that a countable product of topologically complete spaces is topologically complete (in the product topology).

(c) Show that an open subspace of a topologically complete space is topologically complete.
[Hint: If $U \subset X$ and $X$ is complete under the metric $d$, define $\phi: U \to \RR$ by the equation

$$
\phi(x) = 1/d(x, X - U).
$$

Imbed $U$ in $X \times \RR$ by setting $f(x) = x \times \phi(x)$.]

(d) Show that if $A$ is a $G_\delta$ set in a topologically complete space, then $A$ is topologically complete.
[Hint: Let $A$ be the intersection of the open sets $U_n$, for $n \in \ZZ_+$. Consider the diagonal imbedding $f(a) = (a, a, \ldots)$ of $A$ into $\prod U_n$.] Conclude that the irrationals are topologically complete.
:::

::: {.solution}
The exercise is Munkres, *Topology* (2000), Section 43, Exercise 6, printed p. 270. Parts (a) and (c) follow the published solution in "Solutions to exercises for Mathematics 205A" (University of California, Riverside, Fall 2014), Part 3, answers to Exercise 6(a) and 6(c), printed p. 5 of that set; parts (b) and (d) are the card's own, following the exercise's hints, and the last step applies (d) to $\RR\setminus\QQ=\bigcap_n(\RR\setminus\{q_n\})$.

::: pf

::: {.pf-step #closed}

A closed subspace of a topologically complete space is topologically complete.

::: pf-proof

::: pf-step

Let $X$ be topologically complete, so there is a metric $d$ on $X$ compatible with its topology such that $(X, d)$ is a complete metric space.


::: pf-proof
This is the definition: a metric compatible with the topology under which the space is complete.
:::

:::

::: pf-step

Let $A \subseteq X$ be a closed subspace, equipped with the subspace metric $d_A = d\restrict_{A \times A}$.


::: pf-proof
The restriction of a metric to a subset is a metric, and it induces the subspace topology.
:::

:::

::: pf-step

Let $(x_n)_{n=1}^\infty$ be a Cauchy sequence in $(A, d_A)$.


::: pf-proof
This is an arbitrary Cauchy sequence in the subspace, which is what completeness quantifies over.
:::

:::

::: pf-step

Since $d_A(x_n, x_m) = d(x_n, x_m)$, $(x_n)$ is a Cauchy sequence in the complete space $(X, d)$.


::: pf-proof
The two metrics agree on $A\times A$, so the Cauchy condition is literally the same.
:::

:::

::: pf-step

Therefore $(x_n)$ converges to some limit point $x \in X$.


::: pf-proof
Completeness of $(X,d)$ applied to this Cauchy sequence supplies the limit point in $X$.
:::

:::

::: pf-step

Since $A$ is closed in $X$, every limit of points in $A$ belongs to $A$, so $x \in A$.


::: pf-proof
A closed set contains the limit of every sequence in it that converges in the ambient space.
:::

:::

::: pf-step

Thus every Cauchy sequence in $(A, d_A)$ converges in $A$, so $(A, d_A)$ is complete.


::: pf-proof
Every Cauchy sequence of $A$ has a limit in $A$, which is the definition of completeness of $(A,d_A)$.
:::

:::

:::

:::

::: {.pf-step #product}

A countable product of topologically complete spaces is topologically complete in the product topology.

::: pf-proof

::: pf-step

Let $\{X_n\}_{n=1}^\infty$ be a countable family of topologically complete spaces, with each $(X_n, d_n)$ being a complete metric space.


::: pf-proof
This names the family and chooses, on each factor, a compatible metric under which it is complete.
:::

:::

::: pf-step

Define the bounded metrics $\bar{d}_n(x, y) = \min\{1, d_n(x, y)\}$ on each $X_n$.


::: pf-proof
Replacing $d_n$ by $\min\{1,d_n\}$ leaves the topology unchanged, because the two agree on distances below $1$, and the result is bounded.
:::

:::

::: pf-step

On the product space $X = \prod_{n=1}^\infty X_n$, define the metric
    $$D(x, y) = \sum_{n=1}^\infty \frac{1}{2^n} \bar{d}_n(x_n, y_n).$$


::: pf-proof
A summable weighted sum of metrics is a metric: the series converges because $\bar d_n\le1$, and the triangle inequality and symmetry hold termwise.
:::

:::

::: pf-step

The metric $D$ induces the product topology on $X$.


::: pf-proof
The balls of $D$ and the product topology generate the same neighbourhoods: $D(x,y)<\varepsilon$ forces the first finitely many coordinates to be close, and finitely many coordinate conditions bound $D$.
:::

:::

::: pf-step

Let $(x^{(k)})_{k=1}^\infty$ be a Cauchy sequence in $(X, D)$.


::: pf-proof
This is an arbitrary Cauchy sequence in the product, which is what completeness quantifies over.
:::

:::

::: pf-step

For each fixed coordinate $n$, $\bar{d}_n(x_n^{(k)}, x_n^{(m)}) \le 2^n D(x^{(k)}, x^{(m)}) \to 0$ as $k, m \to \infty$, so the coordinate sequence $(x_n^{(k)})_{k=1}^\infty$ is Cauchy in $(X_n, d_n)$.


::: pf-proof
$\bar d_n\le 2^nD$ since the sum is over non-negative terms, so the coordinate sequences inherit the Cauchy property.
:::

:::

::: pf-step

By completeness of each $(X_n, d_n)$, $x_n^{(k)} \to y_n \in X_n$ as $k \to \infty$.


::: pf-proof
Each factor is complete under $d_n$, so the coordinate sequence has a limit $y_n\in X_n$.
:::

:::

::: pf-step

Setting $y = (y_1, y_2, \dots) \in X$, $x^{(k)} \to y$ in the product topology, so $(X, D)$ is complete.


::: pf-proof
Convergence in $D$ is convergence in every coordinate, so the point $y$ is a limit of the sequence in the product topology.
:::

:::

:::

:::

::: {.pf-step #open}

An open subspace of a topologically complete space is topologically complete.

::: pf-proof

::: pf-step

Let $(X, d)$ be a complete metric space and let $U \subseteq X$ be an open subset.


::: pf-proof
This is the data of the part: a complete metric space and an open subset of it.
:::

:::

::: pf-step

If $U = X$, $U$ is already complete. If $U \subsetneq X$, the closed set $F = X \setminus U$ is non-empty.


::: pf-proof
The complement of an open set is closed, and it is non-empty exactly when $U$ is a proper subset.
:::

:::

::: pf-step

Define $\phi: U \to \RR$ by $\phi(x) = \frac{1}{d(x, F)}$. Since the distance function $x \mapsto d(x, F)$ is continuous and non-zero on $U$, $\phi$ is continuous.


::: pf-proof
The function $x\mapsto d(x,F)$ is continuous, and it is positive on $U$ because $F$ is closed and disjoint from the open set $U$; the reciprocal of a positive continuous function is continuous.
:::

:::

::: pf-step

Define the embedding $f: U \to X \times \RR$ by $f(x) = (x, \phi(x))$. The map $f$ is a homeomorphism of $U$ onto its image $f(U) \subset X \times \RR$ (with inverse being the first projection $\pi_1$).


::: pf-proof
The map is continuous into the product, injective, and its inverse is the first projection restricted to the graph, which is continuous.
:::

:::

::: pf-step

By parts (a) and (b), the product space $X \times \RR$ is complete under the metric $D((x_1, t_1), (x_2, t_2)) = d(x_1, x_2) + \abs{t_1 - t_2}$.


::: pf-proof
$\RR$ is topologically complete, and parts (a) and (b) give the completeness of the product of two, and hence of countably many, such spaces under the sum metric.
:::

:::

::: pf-step

We claim that the graph $f(U) = \{(x, \phi(x)) : x \in U\}$ is a closed subset of $X \times \RR$:
    Let $(x_k, \phi(x_k)) \to (x, t)$ in $X \times \RR$ as $k \to \infty$. Then $x_k \to x$ in $X$ and $\phi(x_k) \to t$ in $\RR$.
    If $x \in F$, then $d(x_k, F) \to d(x, F) = 0$, so $\phi(x_k) = \frac{1}{d(x_k, F)} \to \infty$, which contradicts $\phi(x_k) \to t \in \RR$.
    Thus $x \in U$, and by continuity of $\phi$, $t = \lim \phi(x_k) = \phi(x)$.


::: pf-proof
If a sequence of graph points converges to $(x,t)$ with $x\in F$, then $d(x_k,F)\to0$ and $\phi(x_k)\to\infty$, contradicting convergence to the real number $t$; hence $x\in U$, and continuity of $\phi$ gives $t=\phi(x)$.
:::

:::

::: pf-step

Hence $(x, t) = (x, \phi(x)) \in f(U)$, proving that $f(U)$ is closed in $X \times \RR$.


::: pf-proof
The limit point is then of the form $(x,\phi(x))$ with $x\in U$, that is, it lies in the graph, which is exactly closedness.
:::

:::

::: pf-step

By part (a), $f(U)$ is complete, so $U \cong f(U)$ is topologically complete.


::: pf-proof
The graph is a closed subspace of the complete space $X\times\RR$, hence complete by part (a), and $U$ is homeomorphic to it.
:::

:::

:::

:::

::: {.pf-step #s4}

A $G_\delta$ subset of a topologically complete space is topologically complete.

::: pf-proof

::: pf-step

Let $A \subseteq X$ be a $G_\delta$ subset in a topologically complete space $X$, so $A = \bigcap_{n=1}^\infty U_n$ for open sets $U_n \subseteq X$.


::: pf-proof
This is the definition of a $G_\delta$ set: a countable intersection of open sets.
:::

:::

::: pf-step

By part (c), each open set $U_n$ is topologically complete.


::: pf-proof
Each $U_n$ is an open subspace of the topologically complete space $X$, so part (c) applies to it.
:::

:::

::: pf-step

By part (b), the countable product $Y = \prod_{n=1}^\infty U_n$ is topologically complete.


::: pf-proof
The product of countably many topologically complete spaces is topologically complete by part (b).
:::

:::

::: pf-step

Define the diagonal map $\Delta: A \to Y$ by $\Delta(a) = (a, a, a, \dots)$.


::: pf-proof
The diagonal is well defined because $a\in A\subseteq U_n$ for every $n$.
:::

:::

::: pf-step

The map $\Delta$ is a homeomorphism of $A$ onto its image $\Delta(A) \subset Y$.


::: pf-proof
It is continuous and injective, and its inverse is the restriction of any coordinate projection to the image, which is continuous.
:::

:::

::: pf-step

The image is $\Delta(A) = \left\{(u_1, u_2, \dots) \in \prod_{n=1}^\infty U_n : u_1 = u_2 = u_3 = \cdots \right\} = \bigcap_{n=1}^\infty \{(u_k) \in Y : u_n = u_{n+1}\}$.


::: pf-proof
A tuple is a diagonal tuple exactly when all of its coordinates agree, and the displayed intersection expresses precisely that condition.
:::

:::

::: pf-step

Since each coordinate equality condition $\{ (u_k) \in Y : u_n = u_{n+1} \}$ is closed in the product topology (as $X$ is Hausdorff), $\Delta(A)$ is an intersection of closed sets, hence closed in $Y$.


::: pf-proof
The set where $u_n=u_{n+1}$ is the preimage of the diagonal of $X\times X$ under the continuous map $u\mapsto(u_n,u_{n+1})$, and the diagonal is closed because $X$ is Hausdorff, being metrizable.
:::

:::

::: pf-step

By part (a), the closed subspace $\Delta(A) \subseteq Y$ is topologically complete, so $A \cong \Delta(A)$ is topologically complete.


::: pf-proof
The image is a closed subspace of the topologically complete product, hence topologically complete by part (a), and $A$ is homeomorphic to it.
:::

:::

:::

:::

::: {.pf-step #irrationals}

$\RR\setminus\QQ$ is topologically complete.

::: pf-proof

::: pf-step

The real line $\RR$ with its standard metric is complete, hence topologically complete.


::: pf-proof
With its standard metric the real line is a complete metric space.
:::

:::

::: pf-step

The rationals $\QQ = \{q_1, q_2, q_3, \dots\}$ are countable, so $\QQ = \bigcup_{n=1}^\infty \{q_n\}$ is an $F_\sigma$ set.


::: pf-proof
The rationals are a countable union of singletons, each of which is closed.
:::

:::

::: pf-step

The irrational numbers are the complement $\RR \setminus \QQ = \bigcap_{n=1}^\infty (\RR \setminus \{q_n\})$.


::: pf-proof
De Morgan's law turns the complement of that union into the displayed intersection.
:::

:::

::: pf-step

Since each $\RR \setminus \{q_n\}$ is open in $\RR$, $\RR \setminus \QQ$ is a $G_\delta$ set in $\RR$.


::: pf-proof
The complement of the closed singleton $\{q_n\}$ is open in $\RR$.
:::

:::

::: pf-step

By step [](#s4){.pf-ref}, the irrational numbers $\RR \setminus \QQ$ are topologically complete.


::: pf-proof
Part (d) applies to the $G_\delta$ set $\RR\setminus\QQ$ of the topologically complete space $\RR$.
:::

:::

:::

:::

:::

:::
