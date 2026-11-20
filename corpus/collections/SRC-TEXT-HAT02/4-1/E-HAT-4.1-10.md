---
schema: qual/card@1
id: E-HAT-4.1-10
kind: problem
title: "Quasi-circle has trivial homotopy but is not contractible"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 10; the stored statement matches.
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
    Read against the book (AT.txt:17861-17862 for the statement; the §1.3 exercise at 4069-4075). The
    argument is correct: the image of a map S^n -> Y is the image of a path of Y, which the §1.3 step
    confines to a finite truncation and hence to a contractible subspace, so the map is nullhomotopic;
    non-contractibility then follows because a nullhomotopy of the quotient map q: Y -> S^1 would lift
    through the covering R -> S^1, giving q a lift; and the CW conclusion is Whitehead. One citation was
    added, not a new argument: the step "S^n is a Peano continuum, therefore it is a continuous image of
    I" is the Hahn-Mazurkiewicz theorem and now names it. The dependence recorded in the card, that the
    path-confinement fact is proved in §1.3 Exercise 7, was checked to be true of that card's current
    solution (its step s1). Not checked: the fine structure of the quasi-circle's topology was not
    re-derived beyond what §1.3's card proves.

- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the quasi-circle, which is what Queue D asks for on this card. The two facts taken from §1.3 Exercise 7 are a step, the Peano-curve reduction of a map from a sphere to a path is a step, the vanishing of the homotopy groups is a step (with the basepoint inside the contracting tree made explicit), non-contractibility is a step, and the exclusion of CW homotopy type is the last. The lift argument is written as an application of the homotopy lifting property with the lift of the terminal constant map, which the prose abbreviated. No retained set covers this exercise; the card now says so. Locators checked: §1.3 Exercise 7 on printed p. 79, Whitehead's theorem (Theorem 4.5) on printed p. 346, the exercise on printed p. 358. No statement repair.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read step by step against Hatcher, Algebraic Topology (2002), §4.1 Exercise 10 and the two facts it
    takes from §1.3 Exercise 7, together with Theorem 4.5. The argument is correct as written: a path in
    the quasi-circle meeting only finitely many of the oscillating arcs lies in a finite tree and so is
    nullhomotopic through the basepoint placed inside that tree; the Peano-curve reduction handles a
    general map of a sphere by projecting a nullhomotopy to the quotient; and a lift of the essential
    map q to RR is forbidden by the lifting criterion, which is the non-contractibility. Contradiction
    with Whitehead then excludes a CW homotopy type. Four page locators removed from the body, in the
    opening paragraph, the step citing §1.3 Exercise 7, and the step invoking Theorem 4.5; no
    mathematics changed.
---

::: {.problem}
Show the 'quasi-circle' described in Exercise 7 in §1.3 has trivial homotopy groups but is not contractible, hence does not have the homotopy type of a CW complex.
:::

::: {.solution}
No retained solution set covers this exercise: the Hatcher sets in the checkout reach §4.1 in Proudfoot's Homework #6, which holds exercises 4, 11, 12, 14 and 15 of the section, and in the Proudfoot Homework #4 sheet, which holds none of exercise 10. The argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §4.1 Exercise 10, and it uses the two facts established in the exercise it cites, §1.3 Exercise 7.

Let $Y$ be the quasi-circle of §1.3 Exercise 7, and $q:Y\to S^1$ the quotient map collapsing its vertical segment.

::: pf

::: {.pf-step #quasi-circle-facts}
Every path in $Y$ has image in a finite tree contained in $Y$, and $q$ does not lift to $\RR\to S^1$.

::: pf-proof
Both are proved in §1.3 Exercise 7. The oscillating graph has the vertical segment as its only accumulation and a path is compact, so its image misses a neighbourhood of the oscillation in each direction and lies in a finite truncation together with the segment and the joining arc, which is a finite tree. And a lift of $q$ would give a path in $\RR$ joining the two heights that $q$ identifies on the vertical segment, which the lifting criterion forbids because $q$ is essential on that loop.
:::

:::

::: {.pf-step #image-in-tree}
Every map $f:S^n\to Y$, $n\ge0$, has image in a finite tree contained in $Y$.

::: pf-proof
For $n\ge1$ the sphere $S^n$ is a compact, connected, locally connected metric space, so by the Hahn--Mazurkiewicz theorem it is a continuous image of $I$: there is a surjection $r:I\to S^n$. Then $fr:I\to Y$ is a path, so by step [](#quasi-circle-facts){.pf-ref} its image lies in a finite tree $T\subset Y$, and that image is $f(S^n)$. For $n=0$ the sphere is a pair of points and the same conclusion holds with the path joining them; the argument below only needs $n\ge1$.
:::

:::

::: {.pf-step #trivial-groups}
$\pi_n(Y)=0$ for every $n\ge1$, and $\pi_0(Y)$ is a single point.

::: pf-proof
$Y$ is path connected, since any two of its points are joined by a path in the oscillating graph together with the segment, so $\pi_0(Y)$ is trivial. For $n\ge1$ and a based map $f:S^n\to Y$, step [](#image-in-tree){.pf-ref} puts $f(S^n)$ in a finite tree $T$, which is contractible and contains the basepoint; a contraction of $T$ to that basepoint, composed with the inclusion, is a homotopy from $f$ to the constant map, so $[f]=0$ in $\pi_n(Y)$.
:::

:::

::: {.pf-step #not-contractible}
$Y$ is not contractible.

::: pf-proof
If $Y$ were contractible then $q:Y\to S^1$ would be nullhomotopic, through a homotopy $H:Y\times I\to S^1$ with $H_0=q$ and $H_1$ constant at some $c$. Choose $\widetilde c\in\RR$ over $c$; the constant map at $\widetilde c$ is a lift of the constant homotopy at $c$, so the homotopy lifting property for the covering $\RR\to S^1$ gives a lift $\widetilde H:Y\times I\to\RR$ of $H$ with $\widetilde H(-,1)=\widetilde c$. Then $x\mapsto\widetilde H(x,0)$ is a lift of $q=H_0$ to $\RR$, contradicting step [](#quasi-circle-facts){.pf-ref}.
:::

:::

::: {.pf-step #no-cw-type}
$Y$ does not have the homotopy type of a CW complex.

::: pf-proof
Suppose $Y\simeq K$ with $K$ a CW complex. Then $K$ is weakly equivalent to a point, by step [](#trivial-groups){.pf-ref}: its homotopy groups vanish in all degrees and it is connected. Whitehead's theorem, Theorem 4.5, applies to CW complexes and makes the map $K\to\ast$ a homotopy equivalence, so $K$ is contractible and then $Y$ is too, contradicting step [](#not-contractible){.pf-ref}. Hence $Y$ has no CW homotopy type: it is weakly contractible but not contractible, which is what the exercise asks.
:::

:::

:::
:::
