---
schema: qual/card@1
id: E-HAT-3.C-6
kind: problem
title: Spheres as H-spaces via $J_2(S^n)$
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 6; repaired the local statement to restore the source's “if and only if”.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.C, Exercise 6; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the proof. A multiplication with strict two-sided identity is exactly an extension of the
    fold $\nabla:S^n\vee S^n\to S^n$ over $S^n\times S^n$, which exists iff $\nabla\circ\omega$ is
    nullhomotopic, and $J_2(S^n)$ is defined so that its single $2n$-cell is attached by exactly
    that composite. The converse uses Exercise 1 to homotope an H-space multiplication to one with
    strict unit. The step that is asserted rather than expanded is that the $n$-skeleton of
    $J_2(S^n)$ is the fold quotient of the wedge, which is the definition's content.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 6 of §3.C, printed p. 291, and the definition of $J_2(X)$ on
    printed p. 224. The equivalence is correct: $S^n\times S^n$ is $S^n\vee S^n$ with one $2n$-cell
    attached by $\omega$, a multiplication with strict two-sided identity is exactly an extension
    of the fold $\nabla$ over that cell, such an extension exists exactly when $\nabla\circ\omega$
    is nullhomotopic, and $J_2(S^n)$ is the quotient in which the wedge is collapsed, so its
    $2n$-cell is attached by $\nabla\circ\omega$; Exercise 1 of the same page supplies the passage
    from an arbitrary multiplication to one with a strict identity. Added to the text: the
    hypothesis $n\ge1$, which the cell description needs, together with the reason the case $n=0$
    is outside the exercise's phrasing but not in doubt, $S^0=\{\pm1\}$ being a topological group.
    Nothing else changed. Not claimed: a published solution, and no certificate.
---

::: {.problem}
Show that $S^n$ is an H-space if and only if the attaching map of the $2n$-cell of $J_2(S^n)$ is homotopically trivial.
:::

::: {.solution}

The argument is the card's own: a multiplication with a strict identity is exactly an extension of the fold map over the top cell of $S^{n}\times S^{n}$, and the second James stage is built so that its $2n$-cell is attached by the same composite.

The CW structure used below needs $n\ge1$, which is the range the exercise is about: at $n=0$ the product $S^0\times S^0$ is four points and has no $2n$-cell attached in this sense. The conclusion is not in doubt there, since $S^0=\{\pm1\}$ is a topological group and hence an H-space; what fails is only the cell description.

Let $S^{n}\vee S^{n}\hookrightarrow S^{n}\times S^{n}$ be the standard inclusion, let $\omega:S^{2n-1}\to S^{n}\vee S^{n}$ be the attaching map of the top cell of the product, and let $\nabla:S^{n}\vee S^{n}\to S^{n}$ be the fold map, the identity on each summand.

::: pf

::: {.pf-step #cw}
$S^{n}\times S^{n}$ is the wedge $S^{n}\vee S^{n}$ with a single $2n$-cell attached, and a map $\mu:S^{n}\times S^{n}\to S^{n}$ with $\mu(x,e)=x=\mu(e,x)$ for all $x$ is the same thing as an extension of $\nabla$ over that cell.

::: pf-proof
The product of two $n$-spheres has a CW structure with one $0$-cell, two $n$-cells and one $2n$-cell, whose $(n)$-skeleton is the wedge; the remaining cell has dimension $2n$ and attaching map $\omega$. If $\mu$ satisfies $\mu(x,e)=x=\mu(e,x)$, then on the wedge $\mu$ restricts to the identity on each copy of $S^{n}$, that is to $\nabla$; conversely a map extending $\nabla$ satisfies those two identities because the points $(x,e)$ and $(e,x)$ lie in the wedge, where the restriction is $\nabla$.
:::

:::

::: {.pf-step #extension}
Such an extension exists if and only if $\nabla\circ\omega$ is nullhomotopic.

::: pf-proof
By the CW extension criterion, a map defined on the $(n)$-skeleton extends over the $2n$-cell if and only if its composite with the attaching map of that cell is nullhomotopic: the extension over $D^{2n}$ exists exactly when the map on $\partial D^{2n}=S^{2n-1}$ is null, since a map from a disc is determined by its boundary value up to homotopy relative to the boundary. Here the map on the skeleton is $\nabla$ and the attaching map is $\omega$, so the condition is that $\nabla\circ\omega$ be nullhomotopic.
:::

:::

::: {.pf-step #james}
$J_{2}(S^{n})=S^{n}\times S^{n}/\big((x,e)\sim x\sim(e,x)\big)$ has $n$-skeleton $S^{n}$ and its single $2n$-cell is attached by $\nabla\circ\omega$.

::: pf-proof
Collapsing the wedge $S^{n}\vee S^{n}\subset S^{n}\times S^{n}$ is the same as imposing $(x,e)\sim(e,x)\sim e$, and the quotient of the $(n)$-skeleton is a single copy of $S^{n}$ — the map identifying the two summands is the fold $\nabla$. The top cell survives the collapse because its interior is disjoint from the wedge, so $J_{2}(S^{n})$ has one $2n$-cell, and its attaching map is the composite of $\omega$ with the collapse of the wedge, which is $\nabla$.
:::

:::

::: {.pf-step #equivalence}
$S^{n}$ is an H-space if and only if the attaching map of the $2n$-cell of $J_{2}(S^{n})$ is nullhomotopic.

::: pf-proof
Suppose $\nabla\circ\omega$ is nullhomotopic. By step [](#extension){.pf-ref} $\nabla$ extends to $\mu:S^{n}\times S^{n}\to S^{n}$, and by step [](#cw){.pf-ref} $\mu(x,e)=x=\mu(e,x)$, so $\mu$ is a multiplication with a strict two-sided identity and $S^{n}$ is an H-space. Conversely, if $S^{n}$ is an H-space, Exercise 1 of this section lets its multiplication be homotoped to one, again denoted $\mu$, with $\mu(x,e)=x=\mu(e,x)$; then $\mu$ extends $\nabla$, so $\nabla\circ\omega$ is nullhomotopic by step [](#extension){.pf-ref}. By step [](#james){.pf-ref} the composite $\nabla\circ\omega$ is exactly the attaching map of the $2n$-cell of $J_{2}(S^{n})$, so
$$
\boxed{S^{n}\text{ is an H-space}\iff\text{the }2n\text{-cell of }J_{2}(S^{n})\text{ is attached trivially}.}
$$
:::

:::

:::
:::
