---
schema: qual/card@1
id: E-HAT-2.2-18
kind: problem
title: Relative cellular chain complex for CW pair
classification:
  areas:
  - topology
  topics:
  - Homology
  - CW Complexes
  - Relative Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 18; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete cellular-chain proof checked.
---

For a CW pair $(X, A)$ show there is a relative cellular chain complex formed by the groups $H_i(X^i, X^{i-1} \cup A^i)$, having homology groups isomorphic to $H_n(X, A)$.

::: {.solution}
Let $(X,A)$ be a CW pair, so $A$ is a subcomplex of $X$. Define
\[
C_n^{CW}(X,A)
=
H_n(X^n,X^{n-1}\cup A^n),
\qquad A^n=A\cap X^n.
\]

<1>1. These groups are naturally the cellular chain groups of the quotient CW complex $X/A$.
::: {.proof}
The quotient $X/A$ inherits a CW structure whose non-basepoint cells are exactly the cells of $X$ not contained in $A$. Its $n$-skeleton is
\[
(X/A)^n=X^n/A^n.
\]
Therefore
\[
C_n^{CW}(X/A)
=H_n(X^n/A^n,\,X^{n-1}/A^{n-1}).
\]
By the quotient theorem for relative homology, this is naturally isomorphic to
\[
H_n(X^n,X^{n-1}\cup A^n)=C_n^{CW}(X,A).
\]
:::

<1>2. Under these identifications, the cellular boundary on $X/A$ gives boundary maps
\[
d_n:C_n^{CW}(X,A)\to C_{n-1}^{CW}(X,A).
\]
::: {.proof}
The cellular boundary of $X/A$ is defined using the connecting homomorphisms for its skeletal pairs. Transport these maps through the natural isomorphisms of <1>1. Equivalently, they are the connecting maps obtained from the triples
\[
(X^n,\,X^{n-1}\cup A^n,\,X^{n-2}\cup A^{n-1}).
\]
Since they come from an ordinary cellular chain complex, they satisfy $d_{n-1}d_n=0$.
:::

<1>3. The homology of this relative cellular chain complex is $H_n(X,A)$.
::: {.proof}
By <1>1--<1>2, the relative cellular complex is canonically the cellular chain complex of $X/A$. Hence its homology is
\[
H_n^{CW}(X/A)\cong\widetilde H_n(X/A).
\]
For a CW pair, collapsing $A$ gives the standard relative-homology isomorphism
\[
\widetilde H_n(X/A)\cong H_n(X,A)
\]
(with the usual unreduced interpretation in degree $0$). Therefore
\[
\boxed{H_n(C_*^{CW}(X,A))\cong H_n(X,A).}
\]
:::

Thus the groups specified in the problem form the desired relative cellular chain complex.
:::
