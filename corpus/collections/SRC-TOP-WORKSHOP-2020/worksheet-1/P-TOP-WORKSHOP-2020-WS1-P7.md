---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS1-P7
kind: problem
title: Homeomorphic spaces have homeomorphic simply connected covering spaces
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Homeomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
(May 2016) Let $p\colon\widetilde X\to X$ and $q\colon\widetilde Y\to Y$ be covering spaces of path-connected, locally path-connected spaces $X$ and $Y$ with $\widetilde X$ and $\widetilde Y$ locally path-connected and simply connected.
Show that if $X$ and $Y$ are homeomorphic, then $\widetilde X$ and $\widetilde Y$ are homeomorphic.
:::

::: {.solution}
Let \(h:X\to Y\) be a homeomorphism. Choose \(\widetilde x_0\in\widetilde X\), put \(x_0=p(\widetilde x_0)\), choose \(\widetilde y_0\in q^{-1}(h(x_0))\), and consider
\[
h\circ p:\widetilde X\to Y.
\]
Since \(\widetilde X\) is simply connected, the lifting criterion gives a lift
\[
F:\widetilde X\to\widetilde Y
\]
of \(h\circ p\) with \(F(\widetilde x_0)=\widetilde y_0\):
\[
q\circ F=h\circ p.
\]

Similarly, since \(\widetilde Y\) is simply connected, \(h^{-1}\circ q\) has a lift
\[
G:\widetilde Y\to\widetilde X
\]
chosen so that \(G(\widetilde y_0)=\widetilde x_0\):
\[
p\circ G=h^{-1}\circ q.
\]
Then
\[
p\circ(GF)=h^{-1}qF=h^{-1}hp=p.
\]
Thus \(GF\) and the identity map of \(\widetilde X\) are two lifts of \(p:\widetilde X\to X\) that agree at \(\widetilde x_0\). Since \(\widetilde X\) is connected, uniqueness of lifts gives
\[
GF=\operatorname{id}_{\widetilde X}.
\]
Likewise \(FG=\operatorname{id}_{\widetilde Y}\). Hence \(F\) and \(G\) are inverse homeomorphisms, so
\[
\widetilde X\cong\widetilde Y.
\]
:::
