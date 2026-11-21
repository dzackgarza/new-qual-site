---
schema: qual/card@1
id: E-HAT-3.D-2
kind: problem
title: "Fundamental group of $SO(n)$"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Converted from prose to numbered steps under #2, six of them, each with its proof. No retained
    solution set covers §3.D Exercise 2 (Sam has no §3.D, Kottke is 3.3.21, Stanford 215C's sets are
    §3.2 and §3.3), so the card says the argument is its own and follows Hatcher's §3.D, citing
    Proposition 3D.1 for the cell structure. Two things the prose compressed are steps: the count of
    the cells of dimension at most $2$ from the decreasing sequences, and the reason the higher cells
    do not change $\pi_1$, namely that their attaching maps are nullhomotopic in the $2$-skeleton.
    The exercise's second half is a step of its own, with the characteristic disk of $e^2$ named as
    the nullhomotopy of the doubled loop. Citation by numbered statement only; nothing paginated is
    written, and the earlier events' locators stand as history. Not checked: no certificate, and the
    cell structure of Proposition 3D.1 was used as stated rather than re-derived.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.D, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.D Exercise 2, printed page
    302. The statement matches the book word for word. Checked: the cells of SO(n)
    are indexed by admissible sequences n > i_1 > ... > i_r > 0 with dimension
    i_1 + ... + i_r (Proposition 3D.1, p. 294), so the 2-skeleton has exactly e^0,
    e^1, e^2; the cellular boundary is de^i = 2e^{i-1} for even i and 0 for odd i
    (§3.D, p. 299), so the 2-cell is attached by a degree 2 map and
    π₁ = ⟨a | a²⟩ = Z_2; cells of dimension at least 3 do not change π₁. The
    generator is the rotation loop in a fixed 2-plane, and the characteristic disk of
    e^2 is the explicit nullhomotopy of its double. No defect.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170's continuation, outside the sections already closed. Read against Hatcher, Exercise 2
    of §3.D, printed p. 302 — the §3.D exercises 1--3 are on that page, checked at PDF page 311 of
    the held book. Checked: the cells of $SO(n)$ are indexed by admissible sequences
    $n>i_1>\cdots>i_r>0$ of dimension $i_1+\cdots+i_r$ (Proposition 3D.1, printed p. 294), so in
    dimensions at most two there are exactly $e^0,e^1,e^2$; those two cells are the images of the
    cells of $\RP^{n-1}$ under $\rho(v)=r(v)r(e_1)$, and the characteristic map of the $2$-cell
    restricts to the double cover $S^1\to\RP^1$, so the $2$-cell attaches by a degree-two map; hence
    $\pi_1$ of the $2$-skeleton is $\langle a\mid a^2\rangle=\ZZ_2$, and cells of dimension at least
    three do not change it. Checked the two requested exhibits as well: the rotation loop in a fixed
    $2$-plane is the $1$-cell's loop, and the characteristic disk of $e^2$ is the explicit
    nullhomotopy of its double. No defect.
---

::: {.problem}
Using the CW structure on $SO(n)$, show that $\pi_1 SO(n) \approx \ZZ_2$ for $n \geq 3$.
Find a loop representing a generator, and describe how twice this loop is nullhomotopic.
:::

::: {.solution}
No retained solution set covers §3.D Exercise 2, so the argument is the card's own, following Hatcher's §3.D: the CW structure of Proposition 3D.1, the identification of its low cells with those of $\RP^{n-1}$, and the degree of the attaching map read off there.

::: pf

::: {.pf-step #cells}
$SO(n)$ has a CW structure whose cells are indexed by the strictly decreasing sequences $n>i_1>\cdots>i_r>0$, the cell indexed by such a sequence having dimension $i_1+\cdots+i_r$, together with a single $0$-cell.

::: pf-proof
This is Proposition 3D.1. Everything below reads only the cells of dimension at most $2$.
:::

:::

::: {.pf-step #lowcells}
For $n\ge3$ the cells of dimension at most $2$ are exactly $e^0$, $e^1$ and $e^2$, and $e^1$ and $e^2$ are the images of the standard cells of $\RP^{n-1}\subset SO(n)$ under the map $\rho(v)=r(v)r(e_1)$.

::: pf-proof
A decreasing sequence of positive integers below $n$ with sum at most $2$ is one of the empty sequence, $(1)$ or $(2)$, so there are exactly three cells, of dimensions $0$, $1$ and $2$. The map $\rho$ carries the cell decomposition of $\RP^{n-1}$ to that of $SO(n)$, sending the $1$-cell and the $2$-cell of $\RP^{n-1}$ to $e^1$ and $e^2$, since the sequences $(1)$ and $(2)$ index those two cells.
:::

:::

::: {.pf-step #attach}
The $2$-cell of $SO(n)$ is attached to the $1$-skeleton by a map of degree $2$.

::: pf-proof
The characteristic map of the $2$-cell of $\RP^{n-1}$ restricts on its boundary circle to the double cover $S^1\to\RP^1\cong S^1$, which has degree $2$; the identification of step [](#lowcells){.pf-ref} carries the attaching map of that cell to the attaching map of $e^2$ and the $1$-cell to $e^1$, and degree is preserved.
:::

:::

::: {.pf-step #pi1}
$\pi_1SO(n)\cong\ZZ_2$ for $n\ge3$.

::: pf-proof
The $2$-skeleton is the circle $e^1$ with a $2$-cell attached along a degree-two map of its boundary, so its fundamental group is $\langle a\mid a^2=1\rangle\cong\ZZ_2$ by the description of the fundamental group of a CW complex in §1.2. The inclusion of the $2$-skeleton into $SO(n)$ induces a surjection on $\pi_1$ whose kernel is generated by the attaching maps of the higher cells, each of which is a map $S^k\to SO(n)^{(2)}$ with $k\ge2$ and so is nullhomotopic there; hence the higher cells change nothing and $\pi_1SO(n)\cong\ZZ_2$.
:::

:::

::: {.pf-step #generator}
The loop that rotates a fixed oriented $2$-plane of $\RR^n$ through angle $2\pi$ and fixes its orthogonal complement pointwise represents the nonzero class.

::: pf-proof
This is a loop in $SO(n)$, continuous in the angle and returning to the identity at $2\pi$. Its image lies in the copy of $SO(2)$ spanned by the plane and fixed complement, which is the circle of the $1$-cell $e^1$ of step [](#lowcells){.pf-ref}; the loop runs once around it, so it represents the class $a$, the generator of step [](#pi1){.pf-ref}.
:::

:::

::: {.pf-step #double}
Twice this loop is nullhomotopic, and the characteristic disk of $e^2$ is an explicit nullhomotopy.

::: pf-proof
Traversing the loop twice is the rotation through $4\pi$ on the plane and the identity on the complement. The attaching map of $e^2$ traverses $e^1$ twice, by step [](#attach){.pf-ref}, so the characteristic map of the $2$-cell is a map of the disk whose boundary is that doubled loop; a map of the disk restricts to a nullhomotopy of its boundary circle. Hence the doubled loop is nullhomotopic and the generator has order exactly $2$.
:::

:::

:::

:::

