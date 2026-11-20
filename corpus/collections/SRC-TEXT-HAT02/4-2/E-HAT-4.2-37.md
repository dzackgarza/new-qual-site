---
schema: qual/card@1
id: E-HAT-4.2-37
kind: problem
title: "Whitehead products vanish in H-spaces"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 37; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Structured the argument into numbered steps and made the logical role of the product explicit:
    the Whitehead product [f,g] is the class of (f v g) composed with the attaching map w of the top
    cell of S^p x S^q, so it vanishes exactly when f v g extends over the product. Supplied the two
    facts the prose used without statement: that w is null-homotopic inside S^p x S^q, since it bounds
    the top cell, and that the restriction of the H-space map F(x,y) = mu(f(x),g(y)) to each axis is
    homotopic to f respectively g through the unit homotopies, hence F restricted to the wedge is
    homotopic to f v g. That homotopy, not an exact equality, is what the argument needs, and the card
    now says so instead of invoking the homotopy extension property to force equality. Every macro
    used is one the preamble defines. Not checked this session: the printed page of the exercise.

---

::: {.problem}
Show that all Whitehead products in a path-connected H-space are trivial.
:::

::: {.solution}

The argument is the card's own; no retained solution set in `tmp/sources` covers Section 4.2 Exercise 37. The statement was checked against Hatcher, *Algebraic Topology* (2002), §4.2 Exercise 37, and the definition of the Whitehead product and the cell structure of $S^{p}\times S^{q}$ are those of that section.

Let $X$ be a path-connected H-space with multiplication $\mu$ and identity $e$, let $f\colon S^{p}\to X$ and $g\colon S^{q}\to X$ be based maps, and write $f\vee g\colon S^{p}\vee S^{q}\to X$ for the map agreeing with $f$ and with $g$ on the two spheres.

::: pf

::: {.pf-step #cells}
$S^{p}\times S^{q}=(S^{p}\vee S^{q})\cup e^{p+q}$: the product has the cell structure with the two spheres as its subcomplex plus one cell of dimension $p+q$, attached by a map $w\colon S^{p+q-1}\to S^{p}\vee S^{q}$.

::: pf-proof
$S^{p}$ has one $0$-cell and one $p$-cell, and $S^{q}$ one $0$-cell and one $q$-cell; the product CW structure therefore has one $0$-cell (the basepoint), one $p$-cell, one $q$-cell and one $(p+q)$-cell. The union of the first three is $S^{p}\vee S^{q}$ and the remaining cell is attached to it, its attaching map being $w$. This is the cell structure Hatcher describes in §4.2 when defining the Whitehead product.
:::

:::

::: {.pf-step #w-null}
The attaching map $w$ is null-homotopic as a map into $S^{p}\times S^{q}$.

::: pf-proof
$w$ is the attaching map of a cell of $S^{p}\times S^{q}$, so it extends over the closed ball $D^{p+q}$ to the characteristic map of that cell; a map on $S^{p+q-1}$ that extends over the ball is null-homotopic in the target. The null-homotopy takes place inside $S^{p}\times S^{q}$ and in fact inside its $(p+q)$-skeleton, which is all of it.
:::

:::

::: {.pf-step #definition}
The Whitehead product $[f,g]\in\pi_{p+q-1}(X)$ is the class of $(f\vee g)\circ w$; consequently $[f,g]=0$ if and only if $f\vee g$ extends to a map $S^{p}\times S^{q}\to X$.

::: pf-proof
By definition $[f,g]=(f\vee g)_{*}[w]$, the class represented by the composite $(f\vee g)\circ w$. For the second claim: if $F\colon S^{p}\times S^{q}\to X$ extends $f\vee g$, then $(f\vee g)\circ w=F\circ w\simeq\ast$ by step [](#w-null){.pf-ref}, so $[f,g]=0$. Conversely, if $[f,g]=0$ then $(f\vee g)\circ w$ is null-homotopic, and the criterion for extending a map defined on the subcomplex $S^{p}\vee S^{q}$ over the single attached cell is exactly the null-homotopy of its restriction to the attaching sphere.
:::

:::

::: {.pf-step #F-axis}
The map $F(x,y)=\mu\bigl(f(x),g(y)\bigr)$ satisfies $F(x,e)\simeq f(x)$ and $F(e,y)\simeq g(y)$.

::: pf-proof
$F(x,e)=\mu\bigl(f(x),g(e)\bigr)=\mu\bigl(f(x),e\bigr)$, and by the H-space axioms of §3.C the map $u\mapsto\mu(u,e)$ is homotopic to the identity through maps $(X,e)\to(X,e)$; composing with $f$ gives $F(-,e)\simeq f$. The other axis is the same with the roles of the two variables exchanged.
:::

:::

::: {.pf-step #F-wedge}
The restriction $\restrictionof{F}{S^{p}\vee S^{q}}$ is homotopic to $f\vee g$.

::: pf-proof
$S^{p}\vee S^{q}$ is the union of $S^{p}\times\{e\}$ and $\{e\}\times S^{q}$, which meet in the basepoint. On the first, $F$ is homotopic to $f$ by step [](#F-axis){.pf-ref}, and the homotopy rel the basepoint exists because the unit homotopy is through based maps; on the second, similarly for $g$. Gluing the two homotopies along the common basepoint, where both are constant, gives a homotopy of restrictions.
:::

:::

::: {.pf-step #product-zero}
$[f,g]=0$.

::: pf-proof
$F\colon S^{p}\times S^{q}\to X$ is continuous, being a composite of $\mu$ with $(f\circ\pi_{1},g\circ\pi_{2})$, so $F\circ w$ is null-homotopic by step [](#w-null){.pf-ref}. By step [](#F-wedge){.pf-ref} the composite $(f\vee g)\circ w$ is homotopic to $\restrictionof{F}{S^{p}\vee S^{q}}\circ w=F\circ w$, hence also null-homotopic, that is $[f,g]=0$ by step [](#definition){.pf-ref}.
:::

:::

::: {.pf-step}
Every Whitehead product in a path-connected H-space is trivial.

::: pf-proof
$f$ and $g$ were arbitrary based maps of spheres into $X$, and step [](#product-zero){.pf-ref} shows their Whitehead product vanishes; the Whitehead product of arbitrary elements of the homotopy groups is the product of representative maps, so all products vanish.
:::

:::

:::

:::
