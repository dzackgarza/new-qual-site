---
schema: qual/card@1
id: E-HAT-3.3-9
kind: problem
title: Degree of covering space projections
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 9; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: the local sign of a covering projection is a locally constant function on a
    connected manifold, hence constant, so Exercise 8's formula gives $\pm p$.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    The card used $p$ both for the covering map and for the number of sheets, so $p^{-1}(B)$ and
    $\deg p$ were ambiguous; the map is now $q$, and the locally constant sign function $\epsilon$
    is defined rather than named, with the trivializing ball as the neighbourhood on which it is
    constant. The mathematics is the same as before: Exercise 8 applied to an evenly covered ball.
    Not checked: Exercise 8 itself is cited, and the case of a non-connected total space is excluded
    by the exercise's hypotheses.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Published solution located and compared: Math 538 homework solutions, HMW 4 handwritten page 2
    (PDF page 18), printed as #8 there, Hatcher 3.3 Ex.9. It reduces to Exercise 8 over an evenly
    covered ball exactly as the card does. Its last step, each local sign being +1 or -1 hence the
    sum being ±p, is a gap in the handout: the signs must be shown equal, which is what the card's
    locally constant sign function on the connected total space does. The card now records this.

- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Stanford Math 215C Solution Set 3, problem 9, printed p.1, supplies the full published argument:
    evenly covered balls, local sign locally constant on a connected total space, and degree the sum
    of the p signs. It confirms the correction previously supplied for the Math 538 sheet's jump to
    d=+-p and leaves no missing step in the card's display.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps and checked the statement against Hatcher, *Algebraic Topology* (2002), §3.3 Exercise 9, printed p. 258: "Show that a p sheeted covering space projection M to N has degree ±p, when M and N are connected closed orientable manifolds." The collection's provenance is the book, and no retained solution set covers this exercise; the argument is the card's own. Checked: the sign epsilon(x) is well defined because the covering map is a local homeomorphism; it is locally constant because over an evenly covered ball both local orientation systems are trivial; connectedness of M makes it constant; and the local-degree formula of Exercise 8 sums it over the p sheets. The card writes the covering map as q because the letter p counts the sheets.
---

::: {.problem}
Show that a $p$-sheeted covering space projection $M \to N$ has degree $\pm p$, when $M$ and $N$ are connected closed orientable manifolds.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §3.3 Exercise 9, printed p. 258. The covering map is written $q$ so that the letter $p$ can count the sheets.

::: pf

::: {.pf-step #setup}
Let $q:M\to N$ be a $p$-sheeted covering of connected closed orientable $n$-manifolds and $B\subset N$ an evenly covered open ball; then $q^{-1}(B)=B_1\amalg\cdots\amalg B_p$, each $B_i$ mapped homeomorphically onto $B$.

::: pf-proof
This is the definition of a $p$-sheeted covering: every point of $N$ has a neighbourhood whose inverse image is a disjoint union of $p$ open sets, each carried homeomorphically to the neighbourhood.
:::
:::

::: {.pf-step #sign}
There is a well-defined function $\epsilon:M\to\{+1,-1\}$ with $\epsilon(x)=+1$ when the local orientation of $M$ at $x$ maps to that of $N$ at $q(x)$ and $\epsilon(x)=-1$ otherwise.

::: pf-proof
$q$ is a local homeomorphism, so it induces an isomorphism $H_n(M\mid x)\to H_n(N\mid q(x))$; this isomorphism carries one of the two generators of $H_n(M\mid x)$ to plus or minus the chosen generator of $H_n(N\mid q(x))$, and the sign is that of the map, which is determined by $x$ alone.
:::
:::

::: {.pf-step #constant}
$\epsilon$ is locally constant, and since $M$ is connected it is constant, with a single value $\epsilon$.

::: pf-proof
Over an evenly covered ball both orientation systems are trivial: $H_n(M\mid x)$ is constant along $B_i$ and $H_n(N\mid q(x))$ along $B$, and $q$ is a homeomorphism $B_i\to B$; so the sign does not change within $B_i$. A locally constant function on a connected space is constant.
:::
:::

::: {.pf-step #degree}
$\deg q=\sum_{i=1}^{p}\epsilon_i$, where $\epsilon_i=\epsilon(x_i)$ for $x_i\in B_i$.

::: pf-proof
This is the local-degree formula of §3.3 Exercise 8: the degree of a map between closed orientable $n$-manifolds is the sum, over the preimages of a regular value, of the local degrees; here $q$ is a local homeomorphism, so a point $y\in B$ has exactly the $p$ preimages $q^{-1}(y)\cap B_i$ and the local degree at $x_i$ is $\epsilon_i$.
:::
:::

::: {.pf-step #conclusion}
$\deg q=\pm p$.

::: pf-proof
By step [](#constant){.pf-ref} all $\epsilon_i$ equal the single value $\epsilon\in\{+1,-1\}$, so the sum of step [](#degree){.pf-ref} is $p\epsilon=\pm p$.
:::
:::

:::
:::
