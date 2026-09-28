---
schema: qual/card@1
id: P-AGH2219DISCONNIDEM
kind: problem
title: A spectrum is disconnected exactly when the ring splits as a product
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Connectedness
  - Idempotents
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.2.19 statement; the standard equivalence agrees with the Stacks Project's idempotent/clopen correspondence.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $A$ be a ring.
Show that the following conditions are equivalent:

1. $\Spec A$ is disconnected;

2. there exist nonzero elements $e_1, e_2 \in A$ such that $e_1 e_2 = 0$, $e_1^2 = e_1$, $e_2^2 = e_2$, and $e_1 + e_2 = 1$ (these are called **orthogonal idempotents**);

3. $A$ is isomorphic to a direct product $A_1 \times A_2$ of two nonzero rings.
:::

::: {.solution}
<1>1. If $\Spec A$ is disconnected, then $A$ has nonzero orthogonal idempotents $e_1,e_2$ with $e_1+e_2=1$.
::: {.proof}
Write
\[
\Spec A=U\amalg V
\]
with $U,V$ nonempty disjoint open subsets.  Since they are complements of one another, both are also closed.

The sheaf axiom for the disjoint open cover $\{U,V\}$ gives an isomorphism of rings
\[
A=\Gamma(\Spec A,\mathcal O)
\xrightarrow{\sim}
\Gamma(U,\mathcal O)\times\Gamma(V,\mathcal O).
\]
Let $e_1,e_2\in A$ be the preimages of
\[
(1,0),\qquad(0,1).
\]
Then
\[
e_1^2=e_1,
\qquad
e_2^2=e_2,
\qquad
e_1e_2=0,
\qquad
e_1+e_2=1.
\]
Both are nonzero: if, for example, $e_1=0$, then its restriction to the nonempty open $U$ would be the zero section, contradicting that it restricts to $1$ there.  Thus condition (2) holds.
:::

<1>2. Suppose condition (2) holds.  Then
\[
\boxed{A\cong Ae_1\times Ae_2.}
\]
::: {.proof}
Define
\[
\Phi:A\longrightarrow Ae_1\times Ae_2,
\qquad
a\longmapsto(ae_1,ae_2).
\]
The rings $Ae_i$ have identities $e_i$.

Define
\[
\Psi:Ae_1\times Ae_2\longrightarrow A,
\qquad
(x,y)\longmapsto x+y.
\]
If $x\in Ae_1$ and $y\in Ae_2$, then
\[
xe_1=x,
\quad xe_2=0,
\quad ye_1=0,
\quad ye_2=y.
\]
Therefore
\[
\Phi(\Psi(x,y))=(x,y),
\]
while
\[
\Psi(\Phi(a))=a(e_1+e_2)=a.
\]
Thus $\Phi$ is an isomorphism.  Since $e_1,e_2$ are nonzero, both factor rings are nonzero.  Hence condition (3) holds.
:::

<1>3. Suppose
\[
A\cong A_1\times A_2
\]
with $A_1,A_2\ne0$.  Then $\Spec A$ is disconnected.
::: {.proof}
Let
\[
e_1=(1,0),
\qquad
e_2=(0,1).
\]
These are complementary orthogonal idempotents.  For every prime ideal $\mathfrak p\subset A$, the relation
\[
e_1e_2=0
\]
forces $e_1\in\mathfrak p$ or $e_2\in\mathfrak p$, while $e_1+e_2=1$ prevents both from lying in $\mathfrak p$.

Hence
\[
\Spec A=D(e_1)\amalg D(e_2).
\]
Each $D(e_i)$ is open, and it is also closed because
\[
D(e_1)=V(e_2),
\qquad
D(e_2)=V(e_1).
\]
They are nonempty because
\[
D(e_1)\cong\Spec A_1,
\qquad
D(e_2)\cong\Spec A_2,
\]
and a nonzero ring has a prime ideal.  Thus $\Spec A$ is a disjoint union of two nonempty open subsets and is disconnected.
:::

<1>4. Therefore the three conditions are equivalent.
::: {.proof}
Step <1>1 proves $(1)\Rightarrow(2)$, step <1>2 proves $(2)\Rightarrow(3)$, and step <1>3 proves $(3)\Rightarrow(1)$.
:::

<1>5. Equivalently,
\[
\boxed{
\Spec A\text{ is connected}
\iff
A\text{ has no idempotents other than }0,1.
}
\]
::: {.proof}
A nontrivial idempotent $e$ gives the complementary pair $e,1-e$, and every pair in condition (2) has this form.
:::

<1>6. Q.E.D.
::: {.proof}
Step <1>4 is the required equivalence.
:::
:::
