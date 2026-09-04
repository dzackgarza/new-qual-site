---
schema: qual/card@1
id: P-VZVZA
kind: problem
title: Surfaces covered by a closed surface of genus $2$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Surfaces
  - Euler Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Checked the statement against problem 5 of the official UGA Spring 2014 topology exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Retained the classification Sigma_2 and N_3, and repaired the proof to establish connectedness and finite covering degree before using multiplicativity of Euler characteristic.
---

::: problem
Find *all* surfaces, orientable and non-orientable, which can be covered by a closed surface (i.e. compact with empty boundary) of genus 2. Prove that your answer is correct.
:::

::: {.solution}
<1>1. If $p:\Sigma_2\to S$ is a covering map, then $S$ is a connected closed surface and $p$ has a finite positive degree $d$.
::: {.proof}
By definition a covering map is surjective.
Since $\Sigma_2$ is connected and $p$ is continuous, its image $S$ is connected.
Since $\Sigma_2$ is compact, $S$ is compact.

A covering map is a local homeomorphism.
Every point of $\Sigma_2$ is an interior point of a surface without boundary, so no point of $S$ can be a boundary point: a boundary point has a neighborhood locally homeomorphic to a half-disk rather than an open disk, and this local type is preserved by a local homeomorphism.
Thus $S$ has empty boundary and is closed.

Fix $s\in S$.
The fiber
\[
p^{-1}(s)
\]
is closed in the compact Hausdorff space $\Sigma_2$, hence compact.
It is also discrete: an evenly covered neighborhood of $s$ meets each sheet in exactly one point of the fiber.
A compact discrete space is finite, so the fiber is finite.
Because $S$ is connected, the cardinality of the fiber is locally constant and therefore constant; denote it by
\[
d\ge1.
\]
Thus $p$ is a finite $d$-sheeted covering.
:::

<1>2. The Euler characteristics satisfy
\[
\chi(\Sigma_2)=d\,\chi(S).
\]
::: {.proof}
For a finite $d$-sheeted covering of compact surfaces, lift a finite triangulation of $S$.
Every vertex, edge, and face has exactly $d$ lifts, so if the triangulation of $S$ has $v,e,f$ cells in dimensions $0,1,2$, the lifted triangulation has $dv,de,df$.
Hence
\[
\chi(\Sigma_2)=dv-de+df=d(v-e+f)=d\chi(S).
\]
:::

<1>3. Consequently
\[
d\chi(S)=-2,
\]
so either
\[
(d,\chi(S))=(1,-2)
\qquad\text{or}\qquad
(d,\chi(S))=(2,-1).
\]
::: {.proof}
For a closed orientable surface of genus $g$,
\[
\chi(\Sigma_g)=2-2g.
\]
Thus
\[
\chi(\Sigma_2)=2-4=-2.
\]
Combining this with <1>2 gives
\[
-2=d\chi(S).
\]
Since $d$ is a positive integer and $\chi(S)$ is an integer, $d$ is a positive divisor of $2$, yielding exactly the two displayed possibilities.
:::

<1>4. The classification theorem for closed connected surfaces reduces the possible targets to
\[
\Sigma_2,
\qquad
N_4,
\qquad
N_3,
\]
where $N_k$ denotes the closed nonorientable surface of nonorientable genus $k$.
::: {.proof}
If $S$ is orientable, then
\[
\chi(S)=2-2g.
\]
The value $-1$ cannot occur, while $2-2g=-2$ gives $g=2$.
Thus the only orientable candidate is $\Sigma_2$.

If $S$ is nonorientable, then
\[
\chi(S)=2-k.
\]
The equations
\[
2-k=-2
\qquad\text{and}\qquad
2-k=-1
\]
give respectively
\[
k=4
\qquad\text{and}\qquad
k=3.
\]
Hence the only nonorientable candidates are $N_4$ and $N_3$.
:::

<1>5. The candidate $N_4$ cannot be covered by $\Sigma_2$.
::: {.proof}
Since
\[
\chi(N_4)=-2,
\]
<1>3 forces any covering
\[
\Sigma_2\to N_4
\]
to have degree $1$.
A one-sheeted covering is a homeomorphism.
But $\Sigma_2$ is orientable and $N_4$ is nonorientable, contradicting invariance of orientability under homeomorphism.
:::

<1>6. Both $\Sigma_2$ and $N_3$ do occur as targets.
::: {.proof}
The identity map shows that $\Sigma_2$ covers itself.

For $N_3$, take its orientation double cover
\[
q:\widetilde N_3\to N_3.
\]
Because $N_3$ is connected and nonorientable, this double cover is connected and orientable.
By multiplicativity of Euler characteristic,
\[
\chi(\widetilde N_3)=2\chi(N_3)=2(-1)=-2.
\]
The classification of closed connected orientable surfaces therefore gives
\[
\widetilde N_3\cong\Sigma_2.
\]
Hence $\Sigma_2$ is a two-sheeted cover of $N_3$.
:::

<1>7. Therefore the complete list is
\[
\boxed{\Sigma_2\text{ and }N_3}.
\]
::: {.proof}
By <1>4 and <1>5 there are no other candidates, and <1>6 realizes both remaining candidates.
:::
:::
