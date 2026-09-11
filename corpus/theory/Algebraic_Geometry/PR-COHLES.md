---
schema: qual/card@1
id: PR-COHLES
kind: proposition
title: The long exact sequence, and the ideal sequence as a computational device
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Long Exact Sequences
  - Ideal Sheaves
relations:
- kind: uses
  target: D-COHDER
- kind: uses
  target: T-IJW1K
review: draft
prompts:
- What is the long exact sequence in sheaf cohomology?
- How do you compute the cohomology of a hypersurface in $\PP^n$?
---

::: {.proposition}
A short exact sequence $0 \to \mcf' \to \mcf \to \mcf'' \to 0$ of sheaves of abelian groups gives a long exact sequence
\[
0 \to H^0(\mcf') \to H^0(\mcf) \to H^0(\mcf'') \mapsvia{\delta} H^1(\mcf') \to \cdots ,
\]
natural in morphisms of short exact sequences.
:::

::: {.remark title="What the connecting map is"}
$\delta$ sends a global section of $\mcf''$ to the obstruction to lifting it: lift locally on a cover, take the differences of the lifts on overlaps, and read the result as a class in $H^1(\mcf')$.
So $H^1(\mcf') = 0$ is precisely the statement that every global section of the quotient lifts.
:::

::: {.remark title="How every computation actually goes"}
For $Y \subseteq \PP^n$ closed with ideal sheaf $\mci_Y$, twist the ideal sequence:
\[
0 \to \mci_Y(d) \to \OO_{\PP^n}(d) \to \OO_Y(d) \to 0 .
\]
Known cohomology of the middle term plus known cohomology of the left term determines the right, which is the unknown.
For a smooth hypersurface of degree $e$, $\mci_Y = \OO(-e)$ and everything is a binomial coefficient; this is how one gets $h^0(\OO_Y(d))$, the Hilbert polynomial of $Y$, and the genus of a plane curve as $\binom{e-1}{2}$.

The other constant use is the skyscraper sequence $0 \to \OO(D-p) \to \OO(D) \to k(p) \to 0$ on a curve, which is how $\ell(D)$ moves by at most one when a point is added, and hence how Riemann--Roch is proved by induction.
:::
