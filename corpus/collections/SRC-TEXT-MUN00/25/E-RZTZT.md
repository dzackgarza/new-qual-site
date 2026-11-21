---
schema: qual/card@1
id: E-RZTZT
kind: problem
title: Components of R^omega in product, uniform, and box topologies
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §25 Exercise 2, printed p. 162, with Example 7 of
    §23, Exercise 23.8 and Exercise 19.8; the three parts and the two hints are stored as
    printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 25.2, PDF pp. 7-8. The product topology gives one
    component; in the uniform topology the bounded and unbounded sequences separate the
    space and the segment t -> t z joins the origin to a bounded sequence; in the box
    topology the coordinatewise affine homeomorphism of Exercise 19.8 sends the pair to a
    bounded and an unbounded sequence exactly when the difference is not eventually zero.
    The reference to the connectedness of R^omega is corrected to §23 Example 7.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with ten steps, each carrying a `pf-proof`; the three answers and the attribution are
    unchanged. One step is rewritten because the prose's construction was garbled: for part (c)
    the homeomorphism is now given explicitly, translation followed by the coordinate scaling
    $a_i=i/\abs{d_i}$ where $d_i\ne0$ and $a_i=1$ where $d_i=0$, which sends $\mathbf y$ to
    $\mathbf 0$ and $\mathbf x$ to the unbounded sequence $a_id_i$. Checked: that the uniform
    metric is translation invariant; that the bounded and unbounded sequences are both open in
    the uniform topology (the two ball estimates are written out); that $t\mapsto t\mathbf z$ is
    continuous for bounded $\mathbf z$; and that the uniform topology is coarser than the box
    topology, which is what carries the separation over. Cited by number only: Example 7 of §23,
    Exercise 24.8, Exercise 23.8 and Exercise 19.8.
---

::: {.exercise}

(a) What are the components and path components of $\RR^\omega$ (in the product topology)?

(b) Consider $\RR^\omega$ in the uniform topology.
Show that $\mathbf{x}$ and $\mathbf{y}$ lie in the same component of $\RR^\omega$ if and only if the sequence

$$
\mathbf{x} - \mathbf{y} = (x_1 - y_1, x_2 - y_2, \dots)
$$

is bounded.
[Hint: It suffices to consider the case where $\mathbf{y} = 0$.]

(c) Give $\RR^\omega$ the box topology.
Show that $\mathbf{x}$ and $\mathbf{y}$ lie in the same component of $\RR^\omega$ if and only if the sequence $\mathbf{x} - \mathbf{y}$ is "eventually zero."
[Hint: If $\mathbf{x} - \mathbf{y}$ is not eventually zero, show there is a homeomorphism $h$ of $\RR^\omega$ with itself such that $h(\mathbf{x})$ is bounded and $h(\mathbf{y})$ is unbounded.]
:::

::: {.solution}

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 25.2** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); all three parts are theirs, with one citation corrected: the connectedness of $\RR^{\omega}$ in the product topology is Example 7 of §23, not of §13.

::: pf

::: pf-step

(a) In the product topology $\RR^{\omega}$ is connected, so the whole space is its only component.

::: pf-proof

$\RR^\omega$ with the product topology is connected (Example 7 of §23, the product of connected spaces being connected). A connected space has exactly one component, namely itself.

:::

:::

::: pf-step

(a) It is path connected, so the whole space is also its only path component.

::: pf-proof

A product of path-connected spaces is path connected: given $\mathbf x,\mathbf y$, choose for each $n$ a path $\gamma_n$ in $\RR$ from $x_n$ to $y_n$, and set $\gamma(t)_n=\gamma_n(t)$; each coordinate function of $\gamma$ is continuous, so $\gamma$ is continuous by the universal property of the product, and $\gamma(0)=\mathbf x$, $\gamma(1)=\mathbf y$. Hence any two points are joined by a path, and the path components are the single set $\RR^\omega$ (Munkres, Exercise 24.8).

:::

:::

::: pf-step

(b) In the uniform topology, translation by $-\mathbf{x}$ is a homeomorphism, so it suffices to treat $\mathbf{y}=\mathbf{0}$.

::: pf-proof

The uniform metric is translation invariant: $\rho(\mathbf u-\mathbf w,\mathbf v-\mathbf w)=\sup_n\min(\abs{u_n-v_n},1)=\rho(\mathbf u,\mathbf v)$. So translation is an isometry, hence a homeomorphism, and it carries the pair $(\mathbf x,\mathbf y)$ to $(\mathbf 0,\mathbf x-\mathbf y)$; being in the same component is preserved by a homeomorphism.

:::

:::

::: pf-step

(b) If $\mathbf{z}$ is unbounded then $\mathbf{z}$ and $\mathbf{0}$ lie in different components, being separated by the open sets of bounded and of unbounded sequences.

::: pf-proof

Let $B$ be the set of bounded sequences and $U$ its complement, the unbounded ones. If $\mathbf z\in B$ with $\abs{z_n}\le M$ for all $n$, then any $\mathbf y$ with $\rho(\mathbf y,\mathbf z)<1$ has $\abs{y_n}<\abs{z_n}+1\le M+1$, so $\mathbf y\in B$ and $B$ is open. If $\mathbf z\in U$, then for any $M$ there is $n$ with $\abs{z_n}>M$; any $\mathbf y$ with $\rho(\mathbf y,\mathbf z)<\tfrac12$ has $\abs{y_n}>\abs{z_n}-\tfrac12>M-\tfrac12$, so $\mathbf y$ is unbounded as well once $M$ is taken large, and $U$ is open. Thus $B$ and $U$ are disjoint open sets covering $\RR^\omega$, a separation that puts $\mathbf z\in U$ and $\mathbf 0\in B$ on opposite sides (Munkres, Exercise 23.8).

:::

:::

::: pf-step

(b) If $\mathbf{z}$ is bounded, say $\abs{z_{n}}<M$, then $t\mapsto t\mathbf{z}$ is a path from $\mathbf{0}$ to $\mathbf{z}$.

::: pf-proof

The path is continuous into the uniform topology: for $\abs{t-t_0}<\varepsilon/M$ with $\varepsilon\le1$, $\rho(t\mathbf z,t_0\mathbf z)=\sup_n\min(\abs{t-t_0}\abs{z_n},1)\le\abs{t-t_0}M<\varepsilon$. It starts at $\mathbf 0$ and ends at $\mathbf z$, so $\mathbf z$ lies in the path component, hence the component, of $\mathbf 0$.

:::

:::

::: pf-step

(b) Hence $\mathbf{x}$ and $\mathbf{y}$ lie in the same component if and only if $\mathbf{x}-\mathbf{y}$ is bounded.

::: pf-proof

By step 3 it suffices to decide when $\mathbf z=\mathbf x-\mathbf y$ lies in the component of $\mathbf 0$: step 4 excludes every unbounded $\mathbf z$, and step 5 includes every bounded one. The same argument with $t\mapsto t\mathbf z$ shows the path components coincide with the components here.

:::

:::

::: pf-step

(c) In the box topology, if $\mathbf{x}-\mathbf{y}$ has finite support then $\mathbf{x}$ and $\mathbf{y}$ lie in the same component.

::: pf-proof

The map $t\mapsto\mathbf y+t(\mathbf x-\mathbf y)$ is a path in the box topology: on the finitely many coordinates where $x_i\ne y_i$ the coordinate function is affine in $t$ and hence continuous, and on all other coordinates it is constant. A path joins the two points, so they lie in the same path component and hence the same component.

:::

:::

::: pf-step

(c) If $\mathbf{x}-\mathbf{y}$ is not eventually zero, there is a homeomorphism $h$ of $\RR^{\omega}$ with the box topology such that $h(\mathbf{x})$ is bounded and $h(\mathbf{y})$ is unbounded.

::: pf-proof

Put $\mathbf d=\mathbf x-\mathbf y$, nonzero on infinitely many coordinates. Two coordinatewise affine maps, each a homeomorphism of the box topology by Exercise 19.8: first $T(\mathbf z)_i=z_i-y_i$, with $T(\mathbf x)=\mathbf d$ and $T(\mathbf y)=\mathbf 0$; then $S(\mathbf z)_i=a_iz_i$ with $a_i=i/\abs{d_i}$ where $d_i\ne0$ and $a_i=1$ where $d_i=0$, all $a_i$ positive. Then $h=S\circ T$ is a homeomorphism, $h(\mathbf y)=\mathbf 0$ is bounded, and $h(\mathbf x)_i=a_id_i=i\,\mathrm{sign}(d_i)$ at the infinitely many coordinates with $d_i\ne0$, so $h(\mathbf x)$ is unbounded.

:::

:::

::: pf-step

(c) In the box topology the bounded and the unbounded sequences are again open, so $\mathbf{x}$ and $\mathbf{y}$ with $\mathbf{x}-\mathbf{y}$ not eventually zero lie in different components.

::: pf-proof

The uniform topology is coarser than the box topology: a uniform ball of radius $\varepsilon<1$ about $\mathbf z$ is the product of the intervals $(z_n-\varepsilon,z_n+\varepsilon)$, a box basis element. So the sets $B$ and $U$ of step 4, open in the uniform topology, are open in the box topology, and they separate $h(\mathbf x)$ from $h(\mathbf y)$. A homeomorphism carries components to components, so $\mathbf x$ and $\mathbf y$ lie in different components.

:::

:::

::: pf-step

The three answers are: the whole space in the product topology; the class of $\mathbf{x}$ modulo bounded differences in the uniform topology; and the class of $\mathbf{x}$ modulo eventually-zero differences in the box topology.

::: pf-proof

Part (a) is steps 1--2; part (b) is steps 3--6, giving that the component of $\mathbf x$ consists of the $\mathbf y$ with $\mathbf x-\mathbf y$ bounded; part (c) is steps 7--9, giving that it consists of the $\mathbf y$ with $\mathbf x-\mathbf y$ eventually zero.

:::

:::

:::
:::
