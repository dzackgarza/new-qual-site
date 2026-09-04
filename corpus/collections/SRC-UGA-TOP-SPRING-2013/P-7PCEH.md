---
schema: qual/card@1
id: P-7PCEH
kind: problem
title: Definition of deformation retract; isomorphic $\pi_1$ of the figure-eight and
  the theta space; $\pi_1$ of the theta space free on two generators
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Fundamental Group
  - Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Restored the braces in {0} x [-1,1] and checked all three parts against the official Spring 2013 exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Corrected the deformation-retract definition so the retract is fixed pointwise throughout; retained the valid maximal-tree collapse computation.
---

::: problem
a. Let $A$ be a subspace of a topological space $X$.
Define what it means for $A$ to be a **deformation retract** of $X$.

b. Consider $X_1$ the "planar figure eight" and $$X_2 = S^1 \cup (\{0\} \times [-1, 1])$$ (the "theta space"). Show that $X_1$ and $X_2$ have isomorphic fundamental groups.

c. Prove that the fundamental group of $X_2$ is a free group on two generators.
:::

::: {.solution}
<1>1. A subspace \(A\subseteq X\) is a deformation retract of \(X\) if there is a continuous map
\[
H:X\times[0,1]\to X
\]
such that
\[
H(x,0)=x
\qquad(x\in X),
\]
\[
H(x,1)\in A
\qquad(x\in X),
\]
and
\[
H(a,t)=a
\qquad(a\in A,\ 0\le t\le1).
\]
::: {.proof}
At time \(1\), the map
\[
r(x)=H(x,1)
\]
has image in \(A\) and satisfies \(r(a)=a\) for \(a\in A\), so it is a retraction onto \(A\). The last displayed condition says that the homotopy from \(\operatorname{id}_X\) to \(r\) is relative to \(A\); this is the standard deformation-retraction condition.
:::

<1>2. Regard
\[
X_2=S^1\cup(\{0\}\times[-1,1])
\]
as a graph with two vertices
\[
v_+=(0,1),
\qquad
v_-=(0,-1)
\]
and three edges: the left semicircle, the right semicircle, and the vertical diameter
\[
T=\{0\}\times[-1,1].
\]
Then
\[
X_2/T\cong S^1\vee S^1=X_1.
\]
::: {.proof}
The subgraph \(T\) is a single edge joining the two vertices, hence is a maximal tree in \(X_2\). Collapsing \(T\) identifies \(v_+\) and \(v_-\) to one point.
Each of the two semicircular edges then becomes a loop based at this point, so the quotient is a wedge of two circles, i.e. the planar figure eight \(X_1\).
:::

<1>3. The quotient map
\[
q:X_2\to X_2/T
\]
is a homotopy equivalence.
::: {.proof}
The pair \((X_2,T)\) is a CW pair and \(T\) is contractible.
For a CW pair, collapsing a contractible subcomplex to a point yields a homotopy-equivalent quotient (Hatcher, *Algebraic Topology*, Proposition 0.17). Therefore \(q\) is a homotopy equivalence.
:::

<1>4. Consequently,
\[
\boxed{\pi_1(X_1)\cong\pi_1(X_2)}.
\]
::: {.proof}
By <1>2,
\[
X_2/T\cong X_1.
\]
By <1>3, \(q\) is a homotopy equivalence, so it induces an isomorphism on fundamental groups.
Hence
\[
\pi_1(X_2)\cong\pi_1(X_2/T)\cong\pi_1(X_1).
\]
:::

<1>5. The fundamental group of \(X_2\) is the free group on two generators:
\[
\boxed{\pi_1(X_2)\cong F_2}.
\]
::: {.proof}
By <1>2--<1>4,
\[
\pi_1(X_2)
\cong
\pi_1(S^1\vee S^1).
\]
Applying Seifert--van Kampen to the wedge of two circles gives
\[
\pi_1(S^1\vee S^1)
\cong
\pi_1(S^1)*\pi_1(S^1)
\cong
\mathbb Z*\mathbb Z
=F_2.
\]
:::
:::
