---
schema: qual/card@1
id: E-HAT-3.1-5
kind: problem
title: 1-cocycles as functions on paths and $H^1(X;G)\to\operatorname{Hom}(\pi_1(X),G)$
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.1, Exercise 5; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read all four parts: the cocycle condition on the triangle with edges $f$, $g$ and $f\cdot g$
    gives additivity; $c\cdot c=c$ gives vanishing on constant paths without a degenerate simplex;
    the triangulated homotopy square gives invariance once the constant endpoint paths vanish; and
    $\varphi=\delta\psi$ says $\varphi(f)=\psi(v_1)-\psi(v_0)$, with the converse by joining each
    point to one basepoint per component.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 5 (p.205) including the bracketed parenthetical and the printed iff in (d). Rechecked (a) on the triangle, (b) from c.c = c, (c) by the boundary computation now written out, and both directions of (d) with the explicit psi(x) = phi(f_x) and the chain phi(f_{x_0} . f) = phi(f_{x_0}) + phi(f) that makes delta psi = phi. The terse proofs "definition of cocycle" and "definition of coboundary" replaced by the p.191 identification delta = partial*. Not covered: the bracket's appeal to Theorem 3.2 (p.195) is cited, not re-proved.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 5 of §3.1, printed p. 205, and against the definition of
    $\delta=\partial^*$ on printed p. 191. Repaired the proof structure. Four steps had proofs
    that were bare back-references ('Step s1', 'Step s2', ...), two further steps merely restated
    the preceding one ('Hence $\varphi(f\cdot g)=\varphi(f)+\varphi(g)$', 'Hence
    $\varphi(f)=\varphi(g)$'), and the card closed with a $\mathtt{pf-qed}$ block listing five
    labels and nothing else; STYLE-08 forbids a step that only back-references. The solution is now
    six steps that each carry their own argument: additivity from the boundary
    $\partial\sigma=g-(f\cdot g)+f$ of the triangle, vanishing on constant paths from $c\cdot
    c=c$, homotopy invariance from the two-triangle chain whose boundary is
    $f+c_{x_1}-g-c_{x_0}$, both directions of (d), the second by transporting along $f_{x_0}\cdot
    f$ as the card already had it, and the map $H^1(X;G)\to\operatorname{Hom}(\pi_1(X,x_0),G)$
    that the printed bracket asserts, with Theorem 3.2 (printed p. 195) cited rather than
    re-proved. Not claimed: a certificate.
---

::: {.problem}
Regarding a cochain $\varphi \in C^1(X; G)$ as a function from paths in $X$ to $G$, show that if $\varphi$ is a cocycle, then

(a) $\varphi(f \cdot g) = \varphi(f) + \varphi(g)$,

(b) $\varphi$ takes the value 0 on constant paths,

(c) $\varphi(f) = \varphi(g)$ if $f \simeq g$,

(d) $\varphi$ is a coboundary iff $\varphi(f)$ depends only on the endpoints of $f$, for all $f$.

[In particular, (a) and (c) give a map $H^1(X; G) \to \operatorname{Hom}(\pi_1(X), G)$, which the universal coefficient theorem says is an isomorphism if $X$ is path-connected.]
:::

::: {.solution}
Hatcher defines $C^n(X;G)=\operatorname{Hom}(C_n(X),G)$ with $\delta=\partial^*$ on printed p.~191. So a $1$-cochain $\varphi$ is a function from paths in $X$ to $G$, and it is a cocycle exactly when $\varphi(\partial\sigma)=0$ for every singular $2$-simplex $\sigma$. The exercise is Exercise 5 of §3.1, printed p.~205.

::: pf

::: {.pf-step #s1}

**(a)** If $f(1)=g(0)$ then $\varphi(f\cdot g)=\varphi(f)+\varphi(g)$.

::: pf-proof

Let $\sigma\colon\Delta^2\to X$ carry the edge $[v_0,v_1]$ to $f$, the edge $[v_1,v_2]$ to $g$ and the edge $[v_0,v_2]$ to $f\cdot g$; this is the singular $2$-simplex whose image is the triangle bounded by the three paths. Its boundary is $\partial\sigma=g-(f\cdot g)+f$, so the cocycle condition gives $0=\varphi(\partial\sigma)=\varphi(g)-\varphi(f\cdot g)+\varphi(f)$.

:::

:::

::: {.pf-step #s2}

**(b)** $\varphi$ takes the value $0$ on constant paths.

::: pf-proof

A constant path $c$ satisfies $c\cdot c=c$, so part (a) gives $\varphi(c)=\varphi(c)+\varphi(c)$ in $G$, whence $\varphi(c)=0$.

:::

:::

::: {.pf-step #s3}

**(c)** $\varphi(f)=\varphi(g)$ if $f\simeq g$.

::: pf-proof

Let $H\colon I\times I\to X$ be a homotopy from $f$ to $g$ fixed on the endpoints $x_0=f(0)=g(0)$ and $x_1=f(1)=g(1)$. Split the square along the diagonal from $(0,0)$ to $(1,1)$ into the triangles with vertices $(0,0),(1,0),(1,1)$ and $(0,0),(1,1),(0,1)$, and compose the two affine maps $\Delta^2\to I\times I$ with $H$. The two diagonal edges cancel in the boundary of the sum $T$ of the resulting singular $2$-simplices, so
$$
\partial T=f+c_{x_1}-g-c_{x_0},
$$
where $c_{x}$ is the constant path at $x$ (the four outer edges are the bottom $f$, the right and left constant paths and the top edge $g$ traversed backwards). Hence $0=\varphi(\partial T)=\varphi(f)-\varphi(g)$ by part (b).

:::

:::

::: {.pf-step #s4}

**(d)** If $\varphi=\delta\psi$ is a coboundary then $\varphi(f)$ depends only on the endpoints of $f$.

::: pf-proof

A $0$-cochain is a function $\psi$ on the vertices, and $\delta\psi(f)=\psi(\partial f)=\psi(f(1))-\psi(f(0))$ by the definition on printed p.~191, which involves the endpoints only.

:::

:::

::: {.pf-step #s5}

**(d)** Conversely, if $\varphi(f)$ depends only on the endpoints, then $\varphi$ is a coboundary.

::: pf-proof

Choose a basepoint $b(x)$ in the path component of each point $x$, and a path $f_x$ from $b(x)$ to $x$. Set $\psi(x)=\varphi(f_x)$; the endpoint hypothesis makes this independent of the choice of $f_x$. For a path $f$ from $x_0$ to $x_1$, the concatenation $f_{x_0}\cdot f$ runs from $b(x_0)$ to $x_1$, so it has the same endpoints as $f_{x_1}$ and $\psi(x_1)=\varphi(f_{x_0}\cdot f)=\varphi(f_{x_0})+\varphi(f)=\psi(x_0)+\varphi(f)$ by part (a). Thus $\varphi(f)=\delta\psi(f)$ for every path $f$.

:::

:::

::: {.pf-step #s6}

Consequently a cocycle restricts to a homomorphism $\pi_1(X,x_0)\to G$ and a coboundary restricts to zero, so there is a map $H^1(X;G)\to\operatorname{Hom}(\pi_1(X,x_0),G)$, which the universal coefficient theorem identifies as an isomorphism when $X$ is path-connected.

::: pf-proof

By (a) and (c) a cocycle $\varphi$ gives a well-defined homomorphism on homotopy classes of loops at $x_0$, additive by (a) and independent of the representative by (c). A coboundary vanishes on such loops by (d), since both endpoints equal $x_0$. The identification with $\operatorname{Hom}(\pi_1(X,x_0),G)$ is the statement of Theorem 3.2 (printed p.~195) that $h$ in the universal coefficient sequence is an isomorphism for path-connected $X$, which is cited here and not re-proved.

:::

:::

:::

:::
