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
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read step by step against Hatcher, Algebraic Topology (2002), §4.1 Exercise 20, and the obstruction theory of §4.3. Two repairs, both in the proofs rather
    than in the statements. (1) Step `postnikov` justified the vanishing of the obstructions with "the
    coefficients vanish for i >= d+1", which is false: above degree d the fibre of Y -> Y^d has the
    homotopy of Y, and the statement assumes nothing there. The step now separates the two ranges:
    pi_i of the fibre vanishes for i <= d because Y -> Y^d is an isomorphism there, and the
    cohomology vanishes for i >= d+1 because X is d-dimensional. (2) Step `percell` stated its count
    for the whole k-skeleton, where the number of extensions is the product over the k-cells, not
    |pi_k|; its own sub-step `independent` and step `induction` both read it per cell. The statement
    is now about a single k-cell, which is what the argument proves. Steps `obstruction`, `choices`,
    `independent`, `components` and `induction` are unchanged and correct: the obstruction per cell is
    the class of the composite with the attaching map, extensions over a disc up to homotopy rel
    boundary form a pi_k-torsor, and homotopies glue cell by cell. Not checked: no sharper bound, and
    nothing about infinite X.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.1 Exercise 20, and against Sam, §4.1 Exercise 20, which is retained and
    does solve the exercise in sketch: finitely many homotopy classes on a cell, because a map of a
    cell is its attaching map followed by a map of the skeleton, and finitely many maps in total
    because the homotopies are relative to the cell boundaries. The card's sentence that no retained
    set solves it is therefore false, and is replaced: the preamble now names Sam's sketch and says
    that the induction through the Postnikov stage is the card's. Two repairs in the proofs. (1) Step
    `induction` began the induction with "exactly one map of the one-point space $X^0$"; $X^0$ is a
    finite discrete set with one point per $0$-cell, and a finite connected CW complex can have many
    $0$-cells. What is true, and what the induction uses, is that there is exactly one homotopy class
    of maps $X^0\to C$, since $C$ is path-connected and $X^0$ is finite. (2) Step `percell`
    described the extensions for $k=1$ as a quotient of $\pi_1(C)$; the homotopy classes of paths
    between two fixed points form a torsor under $\pi_1(C)$, not a quotient. The count and every
    other step are unchanged; `postnikov`, `components`, `obstruction`, `choices`, `independent` and
    the conclusion were re-read and stand.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    One further repair, in step `induction`. Its conclusion passed from "finitely many extensions of a
    fixed map on $X^{k-1}$" to "finitely many classes in $[X^k,C]$" without saying how the latter is
    assembled from the former: $[X^k,C]$ is the union over the classes $[\varphi]\in[X^{k-1},C]$ of
    the classes restricting to $[\varphi]$, and each fibre is a quotient of the extensions of
    $\varphi$ up to homotopy relative to $X^{k-1}$, because two homotopic extensions can be replaced
    by extensions agreeing on $X^{k-1}$ using the homotopy extension property of the CW pair
    $(X^k,X^{k-1})$ (Proposition 0.16). The step now runs that passage; the induction is unchanged
    otherwise.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    The preamble cited Sam's sketch without saying what it leaves out. It now records that the sketch
    never uses the finiteness of $\pi_i(Y)$ — its sentences would make $[X,Y]$ finite for an arbitrary
    target, so they prove nothing about this exercise — and that the count in which the hypothesis
    enters is the card's. Step `induction` carries the same marking at the point where $\pi_k(C)$ is
    counted. No mathematics changed.
---

::: {.problem}
Show that $[X, Y]$ is finite if $X$ is a finite connected CW complex and $\pi_i(Y)$ is finite for $i \leq \dim X$.
:::

::: {.solution}
The argument follows the retained sketch of **Steven V. Sam, *Solutions to Algebraic Topology* (2008), §4.1 Exercise 20** (`tmp/sources/hatcher-solutions-sam-2008.pdf`), where a map is fixed on the $(k-1)$-skeleton and shown to have finitely many extensions over each cell. Sam's sketch never uses the finiteness of $\pi_i(Y)$: the same sentences would make $[X,Y]$ finite for an arbitrary target, so the count in which the hypothesis does its work is the card's, and the step carrying it is marked as the card's below. It is checked against Hatcher, §4.1 Exercise 20, and against the obstruction theory of §4.3.

::: pf

::: {.pf-step #postnikov}
With $d=\dim X$ and $Y^{d}$ the $d$-th Postnikov stage of $Y$, the map $Y\to Y^{d}$ induces a bijection $[X,Y]\to[X,Y^{d}]$.

::: pf-proof
$Y\to Y^{d}$ is by construction an isomorphism on $\pi_i$ for $i\le d$ and $\pi_i(Y^{d})=0$ for $i>d$. Since $X$ is $d$-dimensional, obstruction theory gives that every map $X\to Y^{d}$ lifts to $Y$ up to homotopy, that every homotopy between such maps does as well, and that the resulting map on homotopy classes is a bijection — with $F$ the homotopy fibre of $Y\to Y^{d}$, the obstructions are classes in $H^{i+1}(X;\pi_i(F))$, and these vanish in the two ranges for two different reasons: $\pi_i(F)=0$ for $i\le d$, because $Y\to Y^{d}$ is an isomorphism on $\pi_i$ there, and $H^{i+1}(X;\cdot)=0$ for $i\ge d+1$, because $X$ has no cohomology above its dimension. Nothing is assumed about $\pi_i(F)$ for $i\ge d+1$, where it equals $\pi_i(Y)$.
:::

:::

::: {.pf-step #components}
A map $X\to Y^{d}$ has image in a single path component of $Y^{d}$, and there are only finitely many components.

::: pf-proof
$X$ is connected, so its image is connected and lies in one component. The components of $Y^{d}$ are those of $Y$, and $\pi_0(Y)$, hence $\pi_0(Y^{d})$, is finite by hypothesis. So the set of maps is the finite union, over the finitely many components $C$, of the maps into $C$.
:::

:::

::: {.pf-step #percell}
Fix a component $C$ of $Y^{d}$, a $k\ge1$, a map $\varphi:X^{k-1}\to C$ and a $k$-cell $e$ of $X$. The extensions of $\varphi$ over $e$, up to homotopy relative to $\partial e$, are either none, or in bijection with $\pi_k(C)$ for $k\ge2$ and with the set of homotopy classes of paths in $C$ between two fixed points for $k=1$, a set on which $\pi_1(C)$ acts freely and transitively; in either case there are at most $\cardinality{\pi_k(C)}$ of them.

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
Induction on $k$ from $k=0$, where the set of homotopy classes of maps $X^{0}\to C$ is a single point: $X^{0}$ is a finite discrete set and $C$ is path-connected, so any two maps of $X^{0}$ into $C$ are homotopic, a homotopy moving each of the finitely many image points along a path in $C$. At the step, step [](#percell){.pf-ref} gives at most $\cardinality{\pi_k(C)}$ extensions over each $k$-cell and step [](#independent){.pf-ref} bounds their number by a finite product, with $\pi_k(C)$ finite for $k\le d$ by hypothesis. This count is the card's: it is where the finiteness of $\pi_k(Y)$ is used, and Sam's sketch, which never uses it, does not supply it. For the passage from a fixed map to all maps, $[X^{k},C]$ is the union over the classes $[\varphi]\in[X^{k-1},C]$, finitely many by the induction hypothesis, of the classes restricting to $[\varphi]$; each of those fibres is a quotient of the set of extensions of $\varphi$ over $X^{k}$ up to homotopy relative to $X^{k-1}$ used above, because two extensions homotopic relative to $X^{k-1}$ are homotopic, and two homotopic extensions of $\varphi$ can be replaced by extensions agreeing on $X^{k-1}$ using the homotopy extension property of the CW pair $(X^{k},X^{k-1})$ (Proposition 0.16). So $[X^{k},C]$ is finite for each $k$, and since $X$ is $d$-dimensional, $X^{d}=X$ and the induction terminates at $[X,C]$.
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
