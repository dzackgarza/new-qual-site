---
schema: qual/card@1
id: P-3AKX2
kind: problem
title: $p^{-1}(U)$ is connected iff $i_*:\pi_1(U)\to\pi_1(S)$ is surjective
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Connectedness
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 7 of the official UGA Spring 2007 topology exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Replaced the compressed coset-orbit sketch with an explicit path-lifting
    argument. The endpoint bijection between pi_1(S) and a fiber of the
    universal cover identifies points lying in the same component of p^{-1}(U)
    with im(i_*); surjectivity then connects every lifted point back to the
    chosen fiber point. Compare Hatcher, Algebraic Topology, Section 1.3.
---

::: problem
Let $S$ be a connected surface, and let $U$ be a connected open subset of $S$.
Let $p : \tilde S \to  S$ be the universal cover of $S$.
Show that $p\inv (U )$ is connected if and only if the homomorphism $i_\ast : \pi_1 (U ) \to \pi_1 (S)$ induced by the inclusion $i : U \to S$ is onto.
:::

::: {.solution}
Fix $x_0\in U$ and $\widetilde x_0\in p^{-1}(x_0)$.

<1>1. The set $U$ is path-connected, and $p^{-1}(U)$ is locally path-connected.
::: {.proof}
Every surface is locally path-connected.
Since $U$ is an open subset of a surface, it is locally path-connected as well.
In a locally path-connected space, path components are open.
Because $U$ is connected, it therefore has only one path component.

The set $p^{-1}(U)$ is open in the surface $\widetilde S$, hence is locally path-connected by the same argument.
:::

<1>2. Lifting loops from $x_0$ gives a bijection
\[
\Phi:\pi_1(S,x_0)\longrightarrow p^{-1}(x_0),
\qquad
[\gamma]\longmapsto \widetilde\gamma(1),
\]
where $\widetilde\gamma$ is the lift of $\gamma$ beginning at $\widetilde x_0$.
::: {.proof}
The endpoint depends only on the homotopy class of $\gamma$ by homotopy lifting.

For surjectivity, let $\widetilde y\in p^{-1}(x_0)$.
Since the universal cover $\widetilde S$ is path-connected, choose a path $\widetilde\alpha$ from $\widetilde x_0$ to $\widetilde y$.
Its projection $\alpha=p\circ\widetilde\alpha$ is a loop at $x_0$, and $\widetilde\alpha$ is its lift from $\widetilde x_0$.
Hence
\[
\Phi([\alpha])=\widetilde y.
\]

For injectivity, suppose the lifts of loops $\gamma$ and $\delta$ from $\widetilde x_0$ have the same endpoint.
Concatenating the lift of $\gamma$ with the reverse of the lift of $\delta$ gives a loop in the simply-connected space $\widetilde S$.
It is nullhomotopic, so its projection $\gamma\delta^{-1}$ is nullhomotopic in $S$.
Thus
\[
[\gamma]=[\delta]
\]
in $\pi_1(S,x_0)$.
:::

<1>3. For $g\in\pi_1(S,x_0)$, the fiber point $\Phi(g)$ lies in the same path component of $p^{-1}(U)$ as $\widetilde x_0$ if and only if
\[
g\in\operatorname{im} i_*.
\]
::: {.proof}
Suppose first that $g=i_*([\alpha])$ for a loop $\alpha$ in $U$ based at $x_0$.
The lift of $\alpha$ from $\widetilde x_0$ stays in $p^{-1}(U)$ and ends at $\Phi(g)$.
Hence $\Phi(g)$ and $\widetilde x_0$ lie in the same path component.

Conversely, suppose there is a path $\widetilde\alpha$ in $p^{-1}(U)$ from $\widetilde x_0$ to $\Phi(g)$.
Its projection $\alpha=p\circ\widetilde\alpha$ is a loop in $U$ based at $x_0$.
By construction,
\[
\Phi(i_*[\alpha])=\Phi(g).
\]
The injectivity in <1>2 gives
\[
i_*[\alpha]=g.
\]
Thus $g\in\operatorname{im}i_*$.
:::

<1>4. If $p^{-1}(U)$ is connected, then $i_*$ is surjective.
::: {.proof}
By <1>1, the locally path-connected space $p^{-1}(U)$ is path-connected whenever it is connected.
Hence every point of the fiber $p^{-1}(x_0)$ lies in the same path component as $\widetilde x_0$.

Let $g\in\pi_1(S,x_0)$.
By <1>2, $\Phi(g)$ is a point of this fiber, so <1>3 gives
\[
g\in\operatorname{im}i_*.
\]
Thus every element of $\pi_1(S,x_0)$ lies in the image of $i_*$.
:::

<1>5. If $i_*$ is surjective, then $p^{-1}(U)$ is path-connected, hence connected.
::: {.proof}
Let $\widetilde y\in p^{-1}(U)$ and set $y=p(\widetilde y)$.
By <1>1, choose a path
\[
\alpha:[0,1]\to U
\]
from $y$ to $x_0$.
Lift $\alpha$ starting at $\widetilde y$.
Its endpoint is some
\[
\widetilde z\in p^{-1}(x_0).
\]
By <1>2 there is a unique $g\in\pi_1(S,x_0)$ with $\Phi(g)=\widetilde z$.
Surjectivity of $i_*$ gives a loop $\beta$ in $U$ based at $x_0$ such that
\[
i_*[\beta]=g.
\]
By <1>3, the lift of $\beta$ from $\widetilde x_0$ is a path in $p^{-1}(U)$ from $\widetilde x_0$ to $\widetilde z$.

The reverse of the lifted path $\alpha$ joins $\widetilde z$ to $\widetilde y$ inside $p^{-1}(U)$.
Concatenating these two paths gives a path from $\widetilde x_0$ to $\widetilde y$.
Since $\widetilde y$ was arbitrary, $p^{-1}(U)$ is path-connected.
:::

Combining <1>4 and <1>5 proves
\[
\boxed{p^{-1}(U)\text{ is connected}\iff i_*:\pi_1(U,x_0)\to\pi_1(S,x_0)\text{ is surjective}.}
\]
:::
