---
schema: qual/card@1
id: E-HAT-3.H-4
kind: problem
title: "Proper homotopy equivalence of universal covers"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.H, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that if finite connected CW complexes $X$ and $Y$ are homotopy equivalent, then their universal covers $\tilde{X}$ and $\tilde{Y}$ are proper homotopy equivalent.

::: {.solution}
Let
\[
f:X\to Y,
\qquad
g:Y\to X
\]
be homotopy inverse maps between finite connected CW complexes. Choose basepoints and lifts
\[
\widetilde f:\widetilde X\to\widetilde Y,
\qquad
\widetilde g:\widetilde Y\to\widetilde X.
\]
Since $f_*$ is an isomorphism on fundamental groups, after identifying the deck groups through $f_*$ the lift $\widetilde f$ is equivariant:
\[
\widetilde f(\gamma x)=f_*(\gamma)\widetilde f(x).
\]
Similarly for $\widetilde g$.

We first show these lifts are proper. Let $K_X\subset\widetilde X$ and $K_Y\subset\widetilde Y$ be finite unions of lifted closed cells mapping onto $X$ and $Y$. Every compact subset of a universal cover of a finite CW complex meets only finitely many deck translates of such a fundamental finite subcomplex. By equivariance, the inverse image under $\widetilde f$ of a finite union of translates of $K_Y$ lies in a finite union of translates of $K_X$. Hence inverse images of compact sets are compact, so $\widetilde f$ is proper; likewise $\widetilde g$.

Choose homotopies
\[
gf\simeq\operatorname{id}_X,
\qquad
fg\simeq\operatorname{id}_Y.
\]
They lift to homotopies
\[
\widetilde g\widetilde f\simeq\operatorname{id}_{\widetilde X},
\qquad
\widetilde f\widetilde g\simeq\operatorname{id}_{\widetilde Y}
\]
after the endpoint lifts are chosen compatibly. These lifted homotopies are proper: they are equivariant lifts of homotopies on the compact finite CW quotients $X\times I$ and $Y\times I$, so the same finite-fundamental-domain argument applies uniformly in the parameter.

Thus $\widetilde f$ and $\widetilde g$ are proper maps and proper homotopy inverses. Therefore
\[
\boxed{\widetilde X\simeq_{\mathrm{proper}}\widetilde Y.}
\]
:::
