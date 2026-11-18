---
schema: qual/card@1
id: E-HAT-4.1-20
kind: problem
title: "Finiteness of $[X, Y]$ for finite CW complexes"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 20; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Read against the book (AT.txt:17898-17899 for the statement). The obstruction induction is written at
    sketch level but is sound: replacing Y by its d-th Postnikov stage is legitimate because Y -> Y^d is an
    isomorphism on pi_i for i <= d and X is d-dimensional; a map is then built cell by cell, with
    obstructions in pi_{k-1}(Y) and the set of extensions up to homotopy rel boundary a torsor under
    pi_k(Y); both finite for k <= d, and only finitely many cells occur. The free-homotopy bookkeeping is
    covered by the card's use of the hypothesis at i = 0: a map lands in one component of Y and pi_0(Y) is
    finite, which the statement's "for i <= dim X" supplies, and without it the claim fails (a point and a
    space with infinitely many components). Not checked: no re-derivation of the Postnikov-stage reduction
    beyond the argument given.

- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained solution set is cited on the card and none was
    located among the retained Hatcher sets, so the argument is the card's own. Checked against
    Hatcher, Section 4.1 Exercise 20, printed p. 359, and the obstruction theory of Section 4.3
    (pp. 412-419). Each step re-read: Y -> Y^d is an isomorphism on pi_i for i <= d with
    pi_i(Y^d) = 0 above, so a map of the d-dimensional X factors through it up to homotopy and so
    do homotopies; X connected means a map lands in one path component and pi_0(Y) is finite; for
    a single k-cell the obstruction is the class in pi_{k-1} of the composite with the attaching
    map, and the extensions up to homotopy rel boundary are as many as pi_k, with the k = 1 case
    stated separately because pi_1 is not abelian; and the choices over the finitely many cells
    are independent because a homotopy is determined cell by cell. Not claimed: any bound sharper
    than finiteness, or anything about X infinite, where the induction gives no finiteness.
---

::: {.problem}
Show that $[X, Y]$ is finite if $X$ is a finite connected CW complex and $\pi_i(Y)$ is finite for $i \leq \dim X$.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and none of the retained Hatcher sets solves Section 4.1 Exercise 20. It is checked against Hatcher, Algebraic Topology, Section 4.1 Exercise 20, printed p. 359, and against the obstruction theory of Section 4.3 (pp. 412--419), in particular the compression of maps of a $d$-dimensional complex into the $d$-th Postnikov stage.

::: pf

::: {.pf-step #postnikov}
With $d=\dim X$ and $Y^{d}$ the $d$-th Postnikov stage of $Y$, the map $Y\to Y^{d}$ induces a bijection $[X,Y]\to[X,Y^{d}]$.

::: pf-proof
$Y\to Y^{d}$ is by construction an isomorphism on $\pi_i$ for $i\le d$ and $\pi_i(Y^{d})=0$ for $i>d$. Since $X$ is $d$-dimensional, obstruction theory gives that every map $X\to Y^{d}$ lifts to $Y$ up to homotopy, that every homotopy between such maps does as well, and that the resulting map on homotopy classes is a bijection — the obstructions lie in $H^{i+1}(X;\pi_i)$ for $i\ge d+1$, where the coefficients vanish.
:::

:::

::: {.pf-step #components}
A map $X\to Y^{d}$ has image in a single path component of $Y^{d}$, and there are only finitely many components.

::: pf-proof
$X$ is connected, so its image is connected and lies in one component. The components of $Y^{d}$ are those of $Y$, and $\pi_0(Y)$, hence $\pi_0(Y^{d})$, is finite by hypothesis. So the set of maps is the finite union, over the finitely many components $C$, of the maps into $C$.
:::

:::

::: {.pf-step #percell}
Fix a component $C$ of $Y^{d}$, a $k\ge1$ and a map $\varphi:X^{k-1}\to C$. The extensions of $\varphi$ over $X^{k}$ up to homotopy relative to $X^{k-1}$ are either none, or in bijection with a quotient of the finite group $\pi_k(C)$ by the action of $\pi_1$ in the case $k=1$; in either case there are at most $\cardinality{\pi_k(C)}$ of them.

:::: pf-proof

::: {.pf-step #obstruction}
For a $k$-cell $e$ with attaching map $\alpha:S^{k-1}\to X^{k-1}$, the composite $\varphi\circ\alpha$ is a map $S^{k-1}\to C$ whose class in $\pi_{k-1}(C)$ is the obstruction to extending over $e$.

::: pf-proof
An extension of $\varphi$ over $e$ is precisely a nullhomotopy of $\varphi\circ\alpha$, since $e$ is a $k$-disc attached along $\alpha$; a nullhomotopy of that composite exists exactly when its class in $\pi_{k-1}(C)$ vanishes, and then the extension is the cone on the nullhomotopy.
:::

:::

::: {.pf-step #choices}
If $\varphi\circ\alpha$ is null, the extensions over $e$ up to homotopy rel $\partial e$ form a set in bijection with $\pi_k(C)$ for $k\ge2$, and with the set of elements of $\pi_1(C)$ for $k=1$.

::: pf-proof
Two extensions are maps $D^{k}\to C$ agreeing on $\partial D^{k}=S^{k-1}$; gluing one with the reverse of the other along the boundary gives a map $S^{k}\to C$, i.e. an element of $\pi_k(C)$, and this assignment is a bijection once one extension is fixed. For $k=1$ this is the description of $\pi_1(C)$ as the set of homotopy classes of paths between two fixed points, basepoint-free, and the set carries a free transitive action of $\pi_1(C)$ on either side, so its cardinality is that of $\pi_1(C)$.
:::

:::

::: {.pf-step #independent}
The choices over the finitely many $k$-cells are independent, so the number of extensions over $X^{k}$ is at most the product of $\cardinality{\pi_k(C)}$ over the $k$-cells.

::: pf-proof
A homotopy rel $X^{k-1}$ between two extensions restricts to a homotopy rel $\partial e$ on each closed $k$-cell, and conversely a family of such homotopies, one for each $k$-cell, glues to a homotopy rel $X^{k-1}$ because the cells meet $X^{k-1}$ exactly in their boundaries and have disjoint interiors. Since $X$ is a finite CW complex there are finitely many $k$-cells.
:::

:::

:::

:::

::: {.pf-step #induction}
For each $k\le d$ the set of homotopy classes of maps $X^{k}\to C$ extending a fixed map on $X^{k-1}$ is finite, and consequently $[X,C]$ is finite.

::: pf-proof
Induction on $k$ from $k=0$, where there is exactly one map of the one-point space $X^{0}$ into the path-connected $C$. At the step, step [](#percell){.pf-ref} gives at most $\cardinality{\pi_k(C)}$ extensions over each $k$-cell and step [](#independent){.pf-ref} bounds their number by a finite product, with $\pi_k(C)$ finite for $k\le d$ by hypothesis. Since $X$ is $d$-dimensional, $X^{d}=X$, and the induction terminates at $[X,C]$.
:::

:::

::: {.pf-step}
$[X,Y]$ is finite.

::: pf-proof
Step [](#postnikov){.pf-ref} identifies $[X,Y]$ with $[X,Y^{d}]$, step [](#components){.pf-ref} writes the latter as a finite union over the finitely many path components, and step [](#induction){.pf-ref} makes each of those finite. A finite union of finite sets is finite, so
$$
\boxed{[X,Y]\text{ is finite}.}
$$
The finiteness of $\pi_i(Y)$ for $i\le d$ is used at every stage of the induction, and $\pi_0(Y)$ in step [](#components){.pf-ref}; nothing is assumed about $\pi_i(Y)$ for $i>d$, where the Postnikov stage already has trivial homotopy groups.
:::

:::

:::
:::
