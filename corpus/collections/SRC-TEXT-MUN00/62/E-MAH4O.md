---
schema: qual/card@1
id: E-MAH4O
kind: problem
title: The inclusion of a curve in the punctured plane is trivial off its interior
classification:
  areas:
  - topology
  topics:
  - Invariance of Domain
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §62 Exercise 4, printed p. 384. No complete published solution located; the searches are listed in
    the COMPLAINTS.md entry for §61--§73 of SRC-TEXT-MUN00. The nontrivial direction is the contrapositive of
    Lemma 62.2 (the Borsuk lemma, printed p. 382) and needs nothing else. The trivial direction uses a polygonal
    ray from the puncture to infinity that avoids the curve and the fact that the complement of a polygonal ray
    in the plane is simply connected; that fact is not proved in the book at this point, and it is the one
    borrowed step on the card: the card states it as a lemma and proves it by straightening the ray with a
    piecewise-linear homeomorphism of the plane, whose construction is sketched. A reader who wants the
    statement closed against the book alone should treat that lemma as the gap. Checked against Lemma 62.2
    (printed p. 382), Theorem 61.3 (printed p. 379) and the definition of the unbounded component (printed
    p. 377).
---

::: {.exercise}

Let $C$ be a simple closed curve in $\RR^2 - 0$; let $j: C \to \RR^2 - 0$ be the inclusion mapping.
Show that $j_*$ is trivial if $0$ lies in the unbounded component of $\RR^2 - C$, and is nontrivial otherwise.
(In fact, $j_*$ is an isomorphism in the latter case, as we shall prove in §65.)
:::

::: {.solution}

Identify $\RR^2$ with $S^2-\theset{\infty}$, so that the two punctures of $S^2$ are $0$ and $\infty$, and $S^2-\theset{0,\infty}=\RR^2-\theset{0}$.

::: pf

::: pf-step

If $0$ lies in a bounded component of $\RR^2-C$, then $j_*$ is nontrivial.

::: pf-proof

Then $0$ and $\infty$ lie in different components of $S^2-C$. The inclusion $j:C\to\RR^2-\theset{0}=S^2-\theset{0,\infty}$ is continuous and injective with compact domain, so if it were nullhomotopic, Lemma 62.2 (the Borsuk lemma, printed p. 382) would put $0$ and $\infty$ in the same component of $S^2-C$. Hence $j$ is not nullhomotopic. Since $C$ is a simple closed curve, there is a homeomorphism $\gamma:S^1\to C$, and $j_*$ carries the class of $\gamma$ to the class of $j\circ\gamma$, the class of $j$; a loop is nullhomotopic exactly when its class is the identity, so that class is not the identity and $j_*$ is nontrivial.

:::

:::

::: pf-step

A polygonal ray in the plane from $0$ to infinity can be chosen disjoint from $C$.

::: pf-proof

Let $U$ be the unbounded component of $\RR^2-C$; it contains $0$ and it is open in $\RR^2$, hence locally path connected, and connected, hence path connected (Theorem 25.3, printed p. 160). Choose $R>0$ with $C\subseteq B_R(0)$ and, by path connectedness of $U$, points $0=p_0,p_1,\dots,p_k=q$ and paths in $U$ joining consecutive ones. In an open subset of $\RR^2$ any two points of a path can be joined by a polygonal path, by covering the path's image with finitely many balls contained in $U$ and joining successive centres by segments; so there is a polygonal path $L_0$ in $U$ from $0$ to a point $q$ with $\norm q>R$. Append the ray $\theset{tq: t\ge1}$ from $q$ radially outward: it stays outside $B_R$, hence meets no point of $C$. The result $L$ is a polygonal ray from $0$ to infinity, disjoint from $C$.

:::

:::

::: pf-step

The complement of a polygonal ray in the plane is simply connected.

::: pf-proof

Let $L$ be a polygonal ray, with vertices $p_0,\dots,p_k$ and last segment on the ray from $p_k$ in direction $u$. Straighten $L$ by a homeomorphism of the plane: for a segment from a point $p$ in direction $v$, the shear $x\mapsto x - \langle x-p, v^{\perp}\rangle v^{\perp}/c$ composed with a rotation and a translation is a homeomorphism of the plane carrying that segment to the corresponding piece of a fixed line while fixing the half plane beyond; performing one such move at each vertex in turn, from $p_k$ back to $p_0$, gives a homeomorphism $\Phi$ of $\RR^2$ with $\Phi(L)=\theset{(t,0):t\ge0}$. Then $\RR^2-L$ is homeomorphic to $\RR^2-\theset{(t,0):t\ge0}$, which is homeomorphic to $(0,\infty)\times(0,2\pi)$ by polar coordinates $x+iy\mapsto(\abs{x+iy},\arg(x+iy))$ with $\arg\in(0,2\pi)$; that product is convex, hence simply connected.

:::

:::

::: pf-step

If $0$ lies in the unbounded component of $\RR^2-C$, then $j_*$ is trivial.

::: pf-proof

By step 2 choose $L$ disjoint from $C$, and by step 3, $\RR^2-L$ is simply connected. Since $C\subseteq\RR^2-L\subseteq\RR^2-\theset{0}$, the inclusion $j$ factors as $C\hookrightarrow \RR^2-L\hookrightarrow\RR^2-\theset{0}$, and the first map's image space is simply connected; so $j_*$ is trivial.

:::

:::

::: pf-qed

Steps 1 and 4 prove the two assertions.

:::

:::
:::
