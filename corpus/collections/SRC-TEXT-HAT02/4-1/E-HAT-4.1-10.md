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
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.1 Exercise 10, against §1.3 Exercise 7, and against Sam, §4.1 Exercise
    10, which is retained and does cover the exercise: it puts the image of $I^n$ in a region
    homeomorphic to an interval, or to two intervals with their midpoints identified, and concludes
    that $Y$ is weakly contractible. Two repairs. (1) The card said that no retained set covers the
    exercise and that the two facts it uses are proved in §1.3 Exercise 7; neither is true. That
    exercise states $\pi_1(Y)=0$ and asks only that $q$ fail to lift, and the preamble now names
    Sam's argument and says what the card supplies. (2) The step taking "every path has image in a
    finite tree" from §1.3 Exercise 7 was unsupported: "a path is compact, so its image misses a
    neighbourhood of the oscillation" does not prove it. It is replaced by the argument that no path
    passes between $V$ and $G$: if $\gamma(t_0)\in V$ and $\gamma(t_n)\in G$ with $t_n\to t_0$, then
    on the component of $\gamma^{-1}(G)$ through $t_n$ the coordinate $s\circ\gamma$ ranges over an
    interval from $0$ up to its maximum, so $\sin(1/s)$ takes both $1$ and $-1$ at times arbitrarily
    close to $t_0$, one of them at distance at least $1/2$ from $y(\gamma(t_0))$. Hence a path's
    trace in $G$ has a positive lower bound for $s$ and lies with $V$ and $A$ in a finite tree. The
    Peano-curve reduction, the vanishing of the homotopy groups, non-contractibility by homotopy
    lifting and the exclusion of a CW type stand, with step references updated.
---

::: {.problem}
Show the 'quasi-circle' described in Exercise 7 in §1.3 has trivial homotopy groups but is not contractible, hence does not have the homotopy type of a CW complex.
:::

::: {.solution}
The argument follows **Steven V. Sam, *Solutions to Algebraic Topology* (2008), §4.1 Exercise 10** (`tmp/sources/hatcher-solutions-sam-2008.pdf`), which puts the image of a map $I^n\to Y$ inside a region homeomorphic to an interval, or to two intervals with their midpoints identified, and concludes that $Y$ is weakly contractible. Sam asserts rather than proves that a path cannot run through the oscillation; that proof is supplied in step [](#paths){.pf-ref} and is the card's, as is the argument that $q$ does not lift. Hatcher's §1.3 Exercise 7 states $\pi_1(Y)=0$ and asks only for the failure of the lift, so it is cited for neither.

Let $Y$ be the quasi-circle of §1.3 Exercise 7, $G$ the part of it in the graph of $y=\sin(1/x)$, $V$ the segment $\{0\}\times[-1,1]$ in the $y$-axis, $A$ the arc joining $G$ to $V$, and $q:Y\to S^1$ the quotient map that collapses $V$ to a point.

::: pf

::: {.pf-step #paths}
No path in $Y$ passes from $V$ into $G$, and every path in $Y$ has image in a finite tree contained in $Y$.

::: pf-proof
Identify $G$ with $(0,a]$ through the $x$-coordinate, so that the points of $G$ are $s\mapsto(s,\sin(1/s))$ for $s\in(0,a]$, and write $s(z)=x(z)$ for $z\in Y$; the set where $s=0$ is exactly $V$.

First, no path passes between $V$ and $G$. Let $\gamma:I\to Y$ be a path and $t_0\in I$ with $\gamma(t_0)\in V$, and suppose $\gamma(t_n)\in G$ for some $t_n\to t_0$. For each $n$ let $J_n$ be the component of the open set $\gamma^{-1}(G)$ containing $t_n$. If $t_0$ lies in the closure of some $J_n$, then $t_0$ is an endpoint of $J_n$, and $s\circ\gamma$ is positive and continuous on $J_n$ with limit $0$ at that endpoint; hence on $J_n$ the function $s\circ\gamma$ assumes every value in some interval $(0,\delta)$, which contains a full period of $\sin(1/s)$, so $y(\gamma(t))=\sin(1/s(\gamma(t)))$ takes both values $1$ and $-1$ at times arbitrarily close to $t_0$. One of these two values is at distance at least $1/2$ from $y(\gamma(t_0))$, which contradicts $\gamma(t)\to\gamma(t_0)$. If no $J_n$ has $t_0$ in its closure, then $J_n=(a_n,b_n)$ with $a_n,b_n\to t_0$; by continuity of $s$ on $Y$ the limits of $s\circ\gamma$ at both ends of $J_n$ are $s(\gamma(t_0))=0$, so the same argument applies on $J_n$ and gives the same contradiction for large $n$.

Second, let $\gamma:I\to Y$ be a path and suppose $\gamma(t_n)\in G$ with $s(\gamma(t_n))\to0$. A subsequence converges to some $t_0$, and $s(\gamma(t_0))=0$, so $\gamma(t_0)\in V$, contradicting the first part. Hence $c=\inf\{s(\gamma(t)):\gamma(t)\in G\}>0$ when the set is nonempty, and then $\gamma(I)\subset V\cup A\cup\{s\ge c\}$. That last set is a finite tree: $V$ is an arc, $A$ is an arc meeting $V$ in one endpoint and $G$ in the point $s=a$, and $\{s\ge c\}$ is an arc in $G$ having that point as an endpoint.
:::

:::

::: {.pf-step #no-lift}
$q$ does not lift to the covering $\RR\to S^1$.

::: pf-proof
Suppose $r:Y\to\RR$ satisfies $p\circ r=q$ for the covering $p:\RR\to S^1$. On $V$ the map $q$ is constant, so $r(V)$ lies in the fibre $p^{-1}(q(V))=\ZZ$, and $V$ is connected, so $r$ is constant on $V$, say $\restrictionof{r}{V}=n$. The arc $A\cup G$ has one endpoint on $V$ and its other end accumulates at points of $V$: as $s\to0$ in $G$ the points $(s,\sin(1/s))$ tend to $V$. The map $q$ is injective on $A\cup G$ and its image is $S^1$ minus the collapsed point, so $q$ winds once around the circle on $A\cup G$, starting and ending at that point. Hence $r$ restricted to $A\cup G$ is a path in $\RR$ whose two ends differ by $1$, as a lift of a loop of degree one; but each end of $A\cup G$ accumulates at points of $V$, and $r$ is continuous on $V$ with the constant value $n$, so $r$ tends to $n$ at both ends. A path in $\RR$ cannot have ends differing by $1$ and equal limits at once, so no such $r$ exists.
:::

:::

::: {.pf-step #image-in-tree}
Every map $f:S^n\to Y$, $n\ge0$, has image in a finite tree contained in $Y$.

::: pf-proof
For $n\ge1$ the sphere $S^n$ is a compact, connected, locally connected metric space, so by the Hahn--Mazurkiewicz theorem it is a continuous image of $I$: there is a surjection $r:I\to S^n$. Then $fr:I\to Y$ is a path, so by step [](#paths){.pf-ref} its image lies in a finite tree $T\subset Y$, and that image is $f(S^n)$. For $n=0$ the sphere is a pair of points and the same conclusion holds with the path joining them; the argument below only needs $n\ge1$.
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
If $Y$ were contractible then $q:Y\to S^1$ would be nullhomotopic, through a homotopy $H:Y\times I\to S^1$ with $H_0=q$ and $H_1$ constant at some $c$. Choose $\widetilde c\in\RR$ over $c$; the constant map at $\widetilde c$ is a lift of the constant homotopy at $c$, so the homotopy lifting property for the covering $\RR\to S^1$ gives a lift $\widetilde H:Y\times I\to\RR$ of $H$ with $\widetilde H(-,1)=\widetilde c$. Then $x\mapsto\widetilde H(x,0)$ is a lift of $q=H_0$ to $\RR$, contradicting step [](#no-lift){.pf-ref}.
:::

:::

::: {.pf-step #no-cw-type}
$Y$ does not have the homotopy type of a CW complex.

::: pf-proof
Suppose $Y\simeq K$ with $K$ a CW complex. Then the homotopy groups of $K$ vanish in all degrees and $K$ is connected, by step [](#trivial-groups){.pf-ref}, so the map $K\to\ast$ is a weak homotopy equivalence; Whitehead's theorem, Theorem 4.5, applied to that map of CW complexes makes it a homotopy equivalence, so $K$ is contractible and then $Y$ is too, contradicting step [](#not-contractible){.pf-ref}. Hence $Y$ has no CW homotopy type: it is weakly contractible but not contractible, which is what the exercise asks.
:::

:::

:::
:::
