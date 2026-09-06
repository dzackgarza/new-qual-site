---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-13
kind: problem
title: Collapse the boundary of a Möbius band
classification:
  areas:
  - topology
  topics:
  - Surfaces
  - Quotient Spaces
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part Two, question 1 of the Topology Ph.D. Qualifying Exam dated January 17, 2009 in assets/attachments/F08phdtop.pdf.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Verified the quotient using a boundary collar. Collapsing the outer circle
    of a collar S^1 times [0,1] produces a disk, so the quotient is obtained by
    capping the boundary of a smaller Mobius band with a disk; this is RP^2.
---

::: {.problem}
Define what is meant by a Möbius band.
Identify the space obtained by identifying the boundary of a Möbius band to a point.
Give a brief explanation.
:::

::: {.solution}
<1>1. A Möbius band is the quotient
\[
M=([0,1]\times[-1,1])/{\sim},
\qquad
(0,t)\sim(1,-t).
\]
::: {.proof}
This is the standard rectangle model: the two vertical edges are glued with a half-twist.
:::

<1>2. The boundary $\partial M$ is a single circle.
::: {.proof}
The boundary is the image of
\[
[0,1]\times\{-1,1\}.
\]
Under the twisted edge identification,
\[
(0,1)\sim(1,-1),
\qquad
(0,-1)\sim(1,1),
\]
so the two horizontal edges join end-to-end to form one circle.
:::

<1>3. In the quotient $M/\partial M$, a collar of $\partial M$ becomes a disk.
::: {.proof}
Choose a closed collar
\[
N\cong S^1\times[0,1]
\]
of the boundary, with
\[
\partial M\cong S^1\times\{0\}.
\]
After collapsing $\partial M$ to one point, the image of $N$ is
\[
(S^1\times[0,1])/(S^1\times\{0\}),
\]
the cone on $S^1$.
The cone on $S^1$ is homeomorphic to the closed disk $D^2$ via
\[
[(e^{i\theta},r)]\longmapsto re^{i\theta}.
\]
Its boundary corresponds to $S^1\times\{1\}$.
:::

<1>4. The quotient $M/\partial M$ is obtained by attaching a disk to a Möbius band along its boundary.
::: {.proof}
Remove the interior of the collar $N$ from $M$.
The remaining surface
\[
M'=M\setminus\operatorname{int}(N)
\]
is again a Möbius band, with boundary $S^1\times\{1\}$.
By <1>3, the collapsed collar becomes a disk whose boundary is exactly this circle.
Thus
\[
M/\partial M\cong M'\cup_{\partial M'}D^2.
\]
:::

<1>5. Therefore
\[
\boxed{M/\partial M\cong\mathbb{RP}^2}.
\]
::: {.proof}
The real projective plane is obtained by attaching a $2$-disk to a Möbius band along its boundary.
Indeed, in the disk model
\[
\mathbb{RP}^2=D^2/(x\sim -x\text{ on }\partial D^2),
\]
an annular neighborhood of the boundary descends to a Möbius band, while the remaining central disk caps its boundary.
By <1>4, $M/\partial M$ has exactly this decomposition.
:::
:::
