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

::: pf

::: {.pf-step #s1}

A $1$-cochain $\varphi$ assigns to each path $f$ a value $\varphi(f) \in G$, and $\delta\varphi = 0$ (cocycle condition) means $\varphi(\partial\sigma) = 0$ for every $2$-simplex $\sigma$.

::: pf-proof

Hatcher p.191: $\delta = \partial^*$, so a cocycle is a cochain with $\varphi(\partial\sigma) = 0$ for every singular $2$-simplex $\sigma$.

:::

:::

::: {.pf-step #s2}

**(a)** For paths $f, g$ with $f(1) = g(0)$, the concatenation $f \cdot g$ bounds a $2$-simplex (the triangle with edges $f$, $g$, and $f \cdot g$), so $\varphi(f \cdot g) - \varphi(f) - \varphi(g) = \varphi(\partial\sigma) = 0$.

::: pf-proof

Step [](#s1){.pf-ref} (the cocycle vanishes on the boundary of the triangle).

:::

:::

::: {.pf-step #s3}

Hence $\varphi(f \cdot g) = \varphi(f) + \varphi(g)$.

::: pf-proof

Step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

**(b)** A constant path $c$ satisfies $c \cdot c = c$, so $\varphi(c) = \varphi(c \cdot c) = \varphi(c) + \varphi(c)$, forcing $\varphi(c) = 0$.

::: pf-proof

Step [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

**(c)** If $f \simeq g$ rel endpoints, triangulate the homotopy square. The boundary of its image as a singular $2$-chain is $g-f$ plus two constant endpoint paths. By step [](#s4){.pf-ref} the cocycle vanishes on those constant paths, so $\varphi(f)=\varphi(g)$.

::: pf-proof

Step [](#s1){.pf-ref} and step [](#s4){.pf-ref}, applied to the following chain. Split $[0,1]\times[0,1]$ into the triangles with vertices $(0,0),(1,0),(1,1)$ and $(0,0),(1,1),(0,1)$ and compose both affine maps with a homotopy $H$ from $f$ to $g$ fixing the ends. Their sum $T$ is a singular $2$-chain whose boundary is $g - f + c_{f(1)} - c_{f(0)}$ up to the degenerate edges, where $c_x$ is the constant path at $x$. Since $\varphi$ is a homomorphism on chains and vanishes on constant paths by step [](#s4){.pf-ref}, $0 = \varphi(\partial T) = \varphi(g) - \varphi(f)$.

:::

:::

::: {.pf-step #s6}

Hence $\varphi(f) = \varphi(g)$.

::: pf-proof

Step [](#s5){.pf-ref}.

:::

:::

::: {.pf-step #s7}

**(d)** ($\Rightarrow$) If $\varphi = \delta\psi$ is a coboundary, then $\varphi(f) = \psi(f(1)) - \psi(f(0))$ depends only on the endpoints.

::: pf-proof

Hatcher p.191: $\delta\psi(f) = \psi(\partial f) = \psi(f(1)) - \psi(f(0))$, a $0$-chain being a formal sum of points.

:::

:::

::: {.pf-step #s8}

($\Leftarrow$) Choose one basepoint in each path component. If $\varphi(f)$ depends only on endpoints, define $\psi(x)=\varphi(f_x)$ using any path $f_x$ from the chosen basepoint of $x$'s component to $x$. This is well-defined. By part (a), $\varphi(f)=\psi(f(1))-\psi(f(0))=\delta\psi(f)$ for every path $f$, so $\varphi$ is a coboundary.

::: pf-proof

The endpoint hypothesis makes the choice of $f_x$ immaterial. For a path $f$ from $x_0 = f(0)$ to $x_1 = f(1)$, part (a) gives $\varphi(f_{x_0} \cdot f) = \varphi(f_{x_0}) + \varphi(f)$, and $f_{x_0} \cdot f$ has the same endpoints as $f_{x_1}$, so the hypothesis gives $\psi(x_1) - \psi(x_0) = \varphi(f)$.

:::

:::

::: pf-qed

Steps [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref}.

:::

:::

:::
