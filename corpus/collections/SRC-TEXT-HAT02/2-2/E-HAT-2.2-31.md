---
schema: qual/card@1
id: E-HAT-2.2-31
kind: problem
title: Mayer–Vietoris gives $\tilde{H}_n(X \vee Y) \approx \tilde{H}_n(X) \oplus \tilde{H}_n(Y)$ under neighborhood condition
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
  - Wedge Sums
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 31; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete Mayer--Vietoris/algebraic proof checked.
---

::: {.problem}
Use the Mayer–Vietoris sequence to show there are isomorphisms $\tilde{H}_n(X \vee Y) \approx \tilde{H}_n(X) \oplus \tilde{H}_n(Y)$ if the basepoints of $X$ and $Y$ that are identified in $X \vee Y$ are deformation retracts of neighborhoods $U \subset X$ and $V \subset Y$.
:::

::: {.solution}
Let
\[
W=X\vee Y
\]
with common basepoint $*$. By hypothesis there are neighborhoods $U\subset X$ and $V\subset Y$ that deformation retract to $*$.

Choose subspaces of $W$
\[
A=X\cup V,
\qquad
B=U\cup Y,
\]
slightly thickened if necessary so that they form an excisive cover for Mayer--Vietoris.

<1>1. The inclusions induce homotopy equivalences
\[
A\simeq X,
\qquad
B\simeq Y,
\qquad
A\cap B=U\cup V\simeq *.
\]
::: {.proof}
Retract $V$ to the wedge point while fixing $X$, and similarly retract $U$ while fixing $Y$. Since both $U$ and $V$ retract to the common basepoint, their wedge $U\cup V$ is contractible.
:::

<1>2. The reduced Mayer--Vietoris sequence gives
\[
\widetilde H_n(W)\cong\widetilde H_n(A)\oplus\widetilde H_n(B)
\]
for every $n$.
::: {.proof}
The reduced Mayer--Vietoris sequence contains
\[
\widetilde H_n(A\cap B)
\longrightarrow
\widetilde H_n(A)\oplus\widetilde H_n(B)
\longrightarrow
\widetilde H_n(W)
\longrightarrow
\widetilde H_{n-1}(A\cap B).
\]
By <1>1 both outer groups vanish, so the middle arrow is an isomorphism. Replacing $A$ and $B$ by their deformation retracts yields
\[
\boxed{
\widetilde H_n(X\vee Y)\cong
\widetilde H_n(X)\oplus\widetilde H_n(Y).}
\]
:::
:::
