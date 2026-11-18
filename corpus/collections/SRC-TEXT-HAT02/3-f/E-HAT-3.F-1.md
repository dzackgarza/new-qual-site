---
schema: qual/card@1
id: E-HAT-3.F-1
kind: problem
title: "Reverse and double mapping telescopes"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.F, Exercise 1; the stored statement matches.
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
    Read against Hatcher, Algebraic Topology (2002), §3.F Exercise 1, printed page
    320; the statement matches word for word. Checked: each mapping cylinder
    deformation retracts onto its top copy of X_{i+1} by sliding along the interval
    direction, and these retractions are compatible with the gluing in the reverse
    telescope (indices i < 0), so the whole retracts onto X_0; in the double
    telescope the same slides retract it onto the sub-telescope over indices i > n.
    No defect.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps and checked the statement against Hatcher, *Algebraic Topology* (2002), §3.F Exercise 1, printed p. 320, both halves of the printed text matching the card. The collection's provenance is the book, and no retained solution set covers the exercise; the argument is the card's own. Checked: the strip retractions and their compatibility under gluing; the shrinking-interval schedule and the compactness argument that makes the homotopy continuous; and that the left-hand part of the double telescope is a reverse telescope ending at $X_n$, so the same retraction extends by the identity on the right-hand tail.
---

::: {.problem}
Given maps $f_i: X_i \to X_{i+1}$ for integers $i < 0$, show that the "reverse mapping telescope" obtained by gluing together the mapping cylinders of the $f_i$'s in the obvious way deformation retracts onto $X_0$.
Similarly, if maps $f_i: X_i \to X_{i+1}$ are given for all $i \in \ZZ$, show that the resulting "double mapping telescope" deformation retracts onto any of the ordinary mapping telescopes contained in it, the union of the mapping cylinders of the $f_i$'s for $i$ greater than a given number $n$.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §3.F Exercise 1, printed p. 320. Both retractions are explicit homotopies: the strips are collapsed one after another in shrinking time intervals, so that only finitely many strips move at any time before $1$ and every compact set meets only finitely many of them.

::: pf

::: {.pf-step #setup}
For $i<0$ let $M_i$ be the mapping cylinder of $f_i:X_i\to X_{i+1}$ and let $T^-=\cdots\cup M_{-2}\cup M_{-1}$ be the reverse telescope, with the top copy of $X_{i+1}$ in $M_i$ identified with the bottom copy in $M_{i+1}$.

::: pf-proof
This is the definition of the reverse mapping telescope of the exercise: the mapping cylinders of the maps $f_i$ for $i<0$, glued along the copies of $X_{i+1}$.
:::
:::

::: {.pf-step #strip}
Each $M_i$ deformation retracts onto its top copy of $X_{i+1}$, fixing that copy, by sliding along the interval coordinate.

::: pf-proof
The mapping cylinder of $f_i$ is the quotient of $X_i\times I\amalg X_{i+1}$ that identifies $(x,1)$ with $f_i(x)$; the homotopy that replaces the interval coordinate $t$ by $(1-s)t+s$ retracts it onto $X_{i+1}\times\{1\}$ and is the identity on the top copy for every $s$.
:::
:::

::: {.pf-step #homotopy}
The strip retractions combine into a homotopy $H:T^-\times I\to T^-$ with $H_0=\mathrm{id}$, image in $X_0$ at time $1$, and $H_s$ the identity on $X_0$ for every $s$.

::: pf-proof
Perform the retraction of $M_{-1}$ during the time interval $[0,\tfrac12]$, of $M_{-2}$ during $[\tfrac12,\tfrac34]$, of $M_{-3}$ during $[\tfrac34,\tfrac78]$, and so on, each strip being collapsed onto the copy of $X_0$ below it. A point of $M_{-j}$ moves only during its own interval and afterwards stays where it was carried; at time $1$ every point of $M_{-j}$ has reached $X_0$. The homotopy is continuous because a compact subset of $T^-$ meets only finitely many strips, hence only finitely many of the intervals are relevant there, and on each strip the formula is continuous.
:::
:::

::: {.pf-step #reverse}
$T^-$ deformation retracts onto $X_0$.

::: pf-proof
By step [](#homotopy){.pf-ref} the homotopy starts at the identity of $T^-$, ends in $X_0$, and fixes $X_0$ throughout; that is a deformation retraction of $T^-$ onto $X_0$.
:::
:::

::: {.pf-step #left-part}
For the double telescope $T=\bigcup_{i\in\ZZ}M_i$ and a fixed $n$, the union $L=\cdots\cup M_{n-2}\cup M_{n-1}$ is a reverse telescope ending at $X_n$ and deformation retracts onto $X_n$.

::: pf-proof
$L$ is exactly the reverse telescope of the maps $f_i$ for $i<n$, whose top is the copy of $X_n$; step [](#reverse){.pf-ref} applies with $X_n$ in place of $X_0$.
:::
:::

::: {.pf-step #double}
$T$ deformation retracts onto the ordinary telescope $T_{\ge n}=\bigcup_{i\ge n}M_i$ for every $n$.

::: pf-proof
Extend the deformation retraction of step [](#left-part){.pf-ref} by the identity on $T_{\ge n}$: the two agree on the common copy of $X_n$, so the extension is continuous, it starts at the identity of $T$, ends in $T_{\ge n}$ and fixes $T_{\ge n}$ throughout.
:::
:::

::: {.pf-step}
The reverse telescope deformation retracts onto $X_0$, and the double telescope onto each of its ordinary tails $T_{\ge n}$.

::: pf-proof
Steps [](#reverse){.pf-ref} and [](#double){.pf-ref} are the two assertions.
:::
:::

:::
:::
