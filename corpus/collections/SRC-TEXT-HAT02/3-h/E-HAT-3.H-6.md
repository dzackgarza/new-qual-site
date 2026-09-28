---
schema: qual/card@1
id: E-HAT-3.H-6
kind: problem
title: "Locally finite homology"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.H, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that homology groups $H_n^{lf}(X; G)$ can be defined using locally finite chains, which are formal sums $\sum_\sigma g_\sigma \sigma$ of singular simplices $\sigma: \Delta^n \to X$ with coefficients $g_\sigma \in G$, such that each $x \in X$ has a neighborhood meeting the images of only finitely many $\sigma$'s with $g_\sigma \neq 0$.
Develop this version of homology far enough to show that for a finite-dimensional locally compact CW complex $X$, $H_n^{lf}(X; G)$ can be computed using infinite cellular chains $\sum_\alpha g_\alpha e_\alpha^n$.
:::

::: {.solution}
A locally finite singular $n$-chain is a formal sum
\[
c=\sum_\sigma g_\sigma\sigma
\]
such that every point of $X$ has a neighborhood meeting the images of only finitely many simplices with nonzero coefficient. The usual singular boundary formula
\[
\partial\sigma=\sum_{i=0}^n(-1)^i\sigma|[v_0,\dots,\widehat v_i,\dots,v_n]
\]
extends termwise to locally finite sums. It remains locally finite, since any neighborhood meeting the image of a face also meets the image of its parent simplex, and each simplex has only finitely many faces. Thus the locally finite chains form a chain complex
\[
C_*^{lf}(X;G),
\]
and we define
\[
H_*^{lf}(X;G)=H_*(C_*^{lf}(X;G)).
\]
Ordinary finite chains embed as a subcomplex. Proper maps induce homomorphisms on locally finite chains, since the inverse image of a compact neighborhood is compact and therefore meets only finitely many simplices in a locally finite family.

Now suppose $X$ is a finite-dimensional locally compact CW complex. Such a CW complex is locally finite: every point has a neighborhood meeting only finitely many cells. Hence an arbitrary formal cellular chain
\[
\sum_\alpha g_\alpha e_\alpha^n
\]
is locally finite precisely in the geometric sense required above, and the cellular boundary is well-defined termwise. Indeed, near any point only finitely many cells occur, so only finitely many terms can contribute locally.

Filter $C_*^{lf}(X;G)$ by the skeleta. The relative locally finite homology of successive skeleta is concentrated in the cell dimension:
\[
H_k^{lf}(X^n,X^{n-1};G)=0\quad(k\ne n),
\]
while
\[
H_n^{lf}(X^n,X^{n-1};G)
\cong\prod_{e_\alpha^n}G,
\]
the product rather than the direct sum, since infinitely many $n$-cells may carry nonzero coefficients. The boundary maps in the exact couples of the skeletal filtration are exactly the usual cellular incidence-number boundary maps, extended to these infinite locally finite sums.

Because $X$ is finite-dimensional, the skeletal filtration is finite in each total degree, so the standard cellular-homology argument applies without convergence issues. It yields a chain equivalence between $C_*^{lf}(X;G)$ and the locally finite cellular complex
\[
C_n^{lf,cell}(X;G)=\left\{\sum_\alpha g_\alpha e_\alpha^n\right\},
\]
with the ordinary cellular boundary formula. Consequently
\[
\boxed{H_n^{lf}(X;G)
\cong H_n(C_*^{lf,cell}(X;G)).}
\]
Thus locally finite homology of a finite-dimensional locally compact CW complex is computed by infinite cellular chains.
:::
