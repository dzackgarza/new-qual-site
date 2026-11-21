---
schema: qual/card@1
id: E-HAT-3.C-2
kind: problem
title: Retracts of H-spaces
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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Converted from prose to numbered steps under #2, four steps. No retained solution set covers
    §3.C Exercise 2 (Sam's §3.C has 5; Stanford 215C has §3.3 only; Kottke is 3.3.21; the Math 538
    sheets are §3.3), so the argument is the card's own and the card says so. What the prose left
    implicit is now a step: that $r(e)=e$ for the identity point of the retract, which is what makes
    the two unit homotopies based rather than unbased once they are pushed into $A$. Checked against
    the definition of an H-space in §3.C and the exercise as printed. Not checked: no certificate,
    and Hatcher's alternative convention with unbased unit homotopies is not discussed on the card.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.C, Exercise 2; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the proof: $\mu_A=r\circ\mu\circ(i\times i)$ with $i,r$ the retract pair, and the unit
    homotopies for $\mu_A$ are the composites of the given homotopies with $i$ and $r$, using
    $r\circ i=\mathrm{id}$. The identity element stays in $A$ by hypothesis, which is what makes
    $\mu_A(e,a)$ and $\mu_A(a,e)$ well formed.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 2 of §3.C, printed p. 291, and the definition of an H-space on
    printed p. 281. Correct. With $i\colon A\to X$, $r\colon X\to A$, $ri=\mathrm{id}_A$ and $e\in A$,
    the multiplication $\mu_A=r\circ\mu\circ(i\times i)$ satisfies $\mu_A(a,e)=r\mu(i(a),e)$ and
    $\mu_A(e,a)=r\mu(e,i(a))$, and composing the basepoint-preserving unit homotopies of the H-space
    structure with $i$ and $r$ gives $\mu_A(a,e)\simeq ri(a)=a$ and the same on the other side.
    These are basepoint-preserving because $r(e)=e$, which follows from $ri=\mathrm{id}_A$ and
    $e\in A$; that is why the hypothesis that the retract contains the identity is needed. Nothing
    changed. Not claimed: a published solution of this exercise, and no certificate.
---

::: {.problem}
Show that a retract of an H-space is an H-space if it contains the identity element.
:::

::: {.solution}
No retained solution set covers §3.C Exercise 2, so the argument is the card's own. It uses only the definition of an H-space in §3.C and the two unit homotopies that definition provides.

::: pf

::: {.pf-step #setup}
Let $X$ be an H-space with multiplication $\mu\colon X\times X\to X$ and identity $e$, let $A\subset X$ contain $e$, and let $i\colon A\to X$ and $r\colon X\to A$ satisfy $r\,i=\id_A$. Then $\mu_A\coloneqq r\circ\mu\circ(i\times i)\colon A\times A\to A$ is a continuous multiplication and $r(e)=e$.

::: pf-proof
$\mu_A$ is a composite of continuous maps, with target $A$ because $r$ has target $A$. Since $e\in A$ we may apply $r\,i=\id_A$ to $e$ and get $r(i(e))=e$, and $i(e)=e$ because $i$ is the inclusion; so $r(e)=e$.
:::

:::

::: {.pf-step #left-unit}
The map $a\mapsto\mu_A(a,e)$ is homotopic to $\id_A$ through maps and homotopies that fix $e$.

::: pf-proof
By the definition of an H-space the map $x\mapsto\mu(x,e)$ is homotopic to $\id_X$ through based maps, say by $H\colon X\times I\to X$ with $H(x,0)=\mu(x,e)$, $H(x,1)=x$ and $H(e,t)=e$. Then $(a,t)\mapsto r(H(i(a),t))$ is a homotopy with values in $A$, from $r(\mu(i(a),e))=\mu_A(a,e)$ to $r(i(a))=a$, and at $a=e$ it is $r(H(e,t))=r(e)=e$, so it is a based homotopy from $\mu_A(-,e)$ to $\id_A$.
:::

:::

::: {.pf-step #right-unit}
The map $a\mapsto\mu_A(e,a)$ is homotopic to $\id_A$ through maps and homotopies that fix $e$.

::: pf-proof
The same argument with the other unit homotopy of $X$, that $x\mapsto\mu(e,x)$ is homotopic to $\id_X$ through based maps: composing with $i$ and $r$ gives a based homotopy from $\mu_A(e,-)$ to $\id_A$.
:::

:::

::: {.pf-step}
$A$ is an H-space with identity $e$.

::: pf-proof
An H-space is a space with a continuous multiplication and a two-sided identity up to based homotopy; step [](#setup){.pf-ref} supplies the multiplication and the point $e$, and steps [](#left-unit){.pf-ref} and [](#right-unit){.pf-ref} the two unit homotopies.
:::

:::

:::

:::

