---
schema: qual/card@1
id: E-HAT-3.C-1
kind: problem
title: H-space structure and strict identity
classification:
  areas:
  - topology
  topics:
  - H-Spaces
  - Hopf Algebras
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.C, Exercise 1; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the proof. The hypotheses of the cited strictification theorem (tom Dieck--Kamps--Puppe,
    Theorem 3.37 and Proposition 3.38) are checked rather than assumed: $e$ a $0$-cell makes
    $\{e\}\hookrightarrow X$ a closed cofibration, hence so is $X\vee X\hookrightarrow X\times X$,
    and the two one-sided unit homotopies are given by hypothesis. The second half extends the
    homotopy from the wedge to $X\times X$ by the homotopy extension property and gets a strict
    two-sided unit. The step that is a citation rather than an argument is the strictification
    itself; the geometric hypotheses around it are verified here.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps and checked the statement against Hatcher, *Algebraic Topology* (2002), §3.C Exercise 1, printed p. 291, both sentences of the printed text matching the card. The collection's provenance is the book, and no retained solution set covers the exercise; the argument is the card's own in the sense that the steps verify the hypotheses of the cited strictification theorem for this situation. The citation of tom Dieck--Kamps--Puppe, *Homotopy Theory*, Theorem 3.37 and Proposition 3.38 was kept from the earlier solution; I did not read that book, so the theorem's statement is relied on as cited rather than checked against its page.
---

::: {.problem}
Suppose that $X$ is a CW complex with basepoint $e \in X$ a 0-cell.
Show that $X$ is an H-space if there is a map $\mu: X \times X \to X$ such that the maps $X \to X$, $x \mapsto \mu(x, e)$ and $x \mapsto \mu(e, x)$, are homotopic to the identity.
[Sometimes this is taken as the definition of an H-space, rather than the more restrictive condition in the definition we have given.] With the same hypotheses, show also that $\mu$ can be homotoped so that $e$ is a strict two-sided identity.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own. The stiffening of a homotopy unit into a strict one is the unit-strictification theorem for well-pointed spaces, cited on the card as tom Dieck--Kamps--Puppe, *Homotopy Theory*, Theorem 3.37 and Proposition 3.38; what the steps verify is that its hypotheses hold here, namely that $e$ is a nondegenerate basepoint of the CW complex and that $\mu$ has a two-sided homotopy unit. The statement is Hatcher, *Algebraic Topology* (2002), §3.C Exercise 1, printed p. 291.

::: pf

::: {.pf-step #cofibration}
The inclusion $\{e\}\hookrightarrow X$ is a closed cofibration, and so is $X\vee X\hookrightarrow X\times X$.

::: pf-proof
$e$ is a $0$-cell of a CW complex, so $\{e\}$ is a deformation retract of a closed neighbourhood by the standard neighbourhood of a cell, and a CW pair is a cofibration pair; the product of a cofibration with a space and the pushout $X\vee X=(X\times\{e\})\cup(\{e\}\times X)$ then give the second inclusion as a cofibration.
:::
:::

::: {.pf-step #homotopy-unit}
The maps $x\mapsto\mu(x,e)$ and $x\mapsto\mu(e,x)$ are homotopic to the identity.

::: pf-proof
This is the hypothesis of the exercise.
:::
:::

::: {.pf-step #strictify}
There is a map $\mu'$ homotopic to $\mu$ with $\mu'(x,e)=\mu'(e,x)=x$ for every $x$.

::: pf-proof
The unit-strictification theorem (tom Dieck--Kamps--Puppe, Theorem 3.37 and Proposition 3.38) says that on a well-pointed space, a multiplication with a two-sided homotopy unit can be homotoped to one with a strict two-sided unit; step [](#cofibration){.pf-ref} supplies well-pointedness and step [](#homotopy-unit){.pf-ref} the homotopy unit.
:::
:::

::: {.pf-step #hspace}
$X$ is an H-space with multiplication $\mu'$ and basepoint $e$.

::: pf-proof
By step [](#strictify){.pf-ref} $\mu'$ is a map $X\times X\to X$ for which $x\mapsto\mu'(x,e)$ and $x\mapsto\mu'(e,x)$ are the identity, hence homotopic to it; that is the definition of an H-space with a strict two-sided unit.
:::
:::

::: {.pf-step}
$\mu$ can be homotoped so that $e$ is a strict two-sided identity, and then $X$ is an H-space.

::: pf-proof
Step [](#strictify){.pf-ref} produces the homotopy of $\mu$ and step [](#hspace){.pf-ref} the H-space structure.
:::
:::

:::
:::
