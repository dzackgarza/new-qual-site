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

---

::: {.problem}
Show that a $p$-sheeted covering space projection $M \to N$ has degree $\pm p$, when $M$ and $N$ are connected closed orientable manifolds.
:::

::: {.solution}
Let $q:M\to N$ be a $p$-sheeted covering between connected closed orientable $n$-manifolds, so that the letter $p$ is free to count sheets. Choose an evenly covered ball $B\subset N$. Its inverse image is a disjoint union of $p$ balls
$$
q^{-1}(B)=B_1\amalg\cdots\amalg B_p,
$$
each mapped homeomorphically to $B$.

For a point $x\in M$ put $\epsilon(x)=+1$ if the local orientation of $M$ at $x$ maps to the local orientation of $N$ at $q(x)$ under the isomorphism $H_n(M\mid x)\to H_n(N\mid q(x))$ induced by $q$, and $\epsilon(x)=-1$ otherwise; this is well defined because $q$ is a local homeomorphism. The map $\epsilon$ is locally constant: on a ball over which $q$ is trivial, both local orientation systems are constant, so $\epsilon$ is constant there. Since $M$ is connected, $\epsilon$ is constant, say with value $\epsilon$, and in particular all the signs $\epsilon_i=\epsilon(x_i)$ of the homeomorphisms $q\restrict_{B_i}$ coincide.

By Exercise 8's local-degree formula,
$$
\deg q=\sum_{i=1}^p\epsilon_i=p\epsilon.
$$
Hence
$$
\boxed{\deg q=\pm p.}
$$

The degree computation is also printed in **Stanford Math 215C, Solution Set 3**, problem 9, printed p. 1 of `tmp/sources/stanford-math215c-spring2009-solution3.pdf` ([course PDF](https://math.stanford.edu/~ralph/math215c/solution3.pdf)): it gives an evenly covered neighborhood with homeomorphic sheets, then explicitly states that local degree is locally constant on a connected total space, and sums the local degrees to get $\deg f=\sum_i\epsilon_i=\pm p$. That is exactly the proof above, including the step the Math 538 sheet omits.
:::
