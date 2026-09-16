---
schema: qual/card@1
id: E-HAT-2.1-20
kind: problem
title: Reduced homology of suspension is shift of reduced homology
classification:
  areas:
  - topology
  topics:
  - Homology
  - Suspension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 20; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Applied reduced Mayer--Vietoris for the suspension and identified a union of r cones with a wedge of r-1 suspensions after collapsing one contractible cone.
---

::: {.problem}
Show that $\tilde{H}_n(X) \approx \tilde{H}_{n+1}(SX)$ for all $n$, where $SX$ is the suspension of $X$.
More generally, thinking of $SX$ as the union of two cones $CX$ with their bases identified, compute the reduced homology groups of the union of any finite number of cones $CX$ with their bases identified.
:::

::: {.solution}
Write the suspension as
\[
SX=C_+X\cup C_-X,
\qquad
C_+X\cap C_-X=X,
\]
where both cones are contractible.

<1>1. For every $n$,
\[
\boxed{\widetilde H_{n+1}(SX)\cong\widetilde H_n(X).}
\]
::: {.proof}
The reduced Mayer--Vietoris sequence contains
\[
\widetilde H_{n+1}(C_+X)\oplus\widetilde H_{n+1}(C_-X)
\to\widetilde H_{n+1}(SX)
\to\widetilde H_n(X)
\to\widetilde H_n(C_+X)\oplus\widetilde H_n(C_-X).
\]
Both outer groups vanish because cones are contractible, so the middle map is an isomorphism.
:::

Now let $Y_r$ be the union of $r\ge1$ cones on $X$, all with their bases identified.

<1>2. For $r\ge2$,
\[
Y_r\simeq\bigvee^{r-1}SX.
\]
::: {.proof}
Choose one cone $C_1X\subset Y_r$. It is a contractible subcomplex, so collapsing it to a point is a homotopy equivalence:
\[
Y_r\simeq Y_r/C_1X.
\]
For each remaining cone $C_iX$, its common base $X$ has been collapsed to that point. The quotient
\[
C_iX/X
\]
is the suspension $SX$. Different cones meet only in the collapsed base, so
\[
Y_r/C_1X\cong\bigvee_{i=2}^r(C_iX/X)
\cong\bigvee^{r-1}SX.
\]
:::

<1>3. Hence for every $k$,
\[
\boxed{
\widetilde H_k(Y_r)
\cong
\bigoplus^{r-1}\widetilde H_{k-1}(X).
}
\]
::: {.proof}
Reduced homology sends a finite wedge to the direct sum of reduced homology groups. Apply <1>2 and then <1>1 to each suspension summand.
:::
:::
