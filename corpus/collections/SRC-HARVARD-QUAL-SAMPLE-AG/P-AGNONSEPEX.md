---
schema: qual/card@1
id: P-AGNONSEPEX
kind: problem
title: A non-separated morphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Separated Morphisms
  - Gluing
  - Examples
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; the source asks for an example of a non-separated morphism.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Give an example of a non-separated morphism.
:::

::: {.solution}
Let $k$ be a field.  Take two copies
\[
U_1=\operatorname{Spec}k[t],
\qquad
U_2=\operatorname{Spec}k[t],
\]
and glue them along the common open subset
\[
D(t)=\operatorname{Spec}k[t,t^{-1}]
\]
by the identity.  Denote the resulting scheme by $X$.

::: pf

::: pf-step
The scheme $X$ is the affine line with doubled origin.

::: pf-proof
Away from $t=0$, the two copies are identified, so every nonzero point occurs once.  The origins
\[
0_1\in U_1,
\qquad
0_2\in U_2
\]
are not in the gluing locus and remain distinct.  Thus the underlying scheme has one copy of every nonzero point and two origins.
:::

:::

::: {.pf-step #not-separated}
The structure morphism
\[
\boxed{X\longrightarrow\operatorname{Spec}k}
\]
is not separated.

::: pf-proof
Consider the diagonal
\[
\Delta:X\longrightarrow X\times_kX.
\]
If $X$ were separated, its image would be closed.

Look at the affine open
\[
U_1\times_kU_2
\cong
\operatorname{Spec}k[x,y]
\subseteq X\times_kX.
\]
The intersection of the diagonal image with this open consists of the pairs
\[
(a,a)
\]
with $a\ne0$, because the two charts represent the same point of $X$ precisely on the gluing locus $\mathbb G_m$.  Hence
\[
\Delta(X)\cap(U_1\times U_2)
=V(x-y)\cap D(x)
\]
inside $\mathbb A^2$.

Its closure in $U_1\times U_2$ is the whole line
\[
V(x-y),
\]
which contains the point
\[
(0_1,0_2).
\]
But $0_1\ne0_2$ in $X$, so this point is not on the diagonal.  Therefore the diagonal is not closed in $X\times_kX$.

Thus
\[
X\to\operatorname{Spec}k
\]
is not separated.
:::

:::

::: pf-step
In $X$, every open neighborhood of $0_1$ meets every open neighborhood of $0_2$.

::: pf-proof
An open neighborhood of $0_i$ meets the common copy of $\mathbb G_m$ in a nonempty open subset.  Two nonempty open subsets of the irreducible curve $\mathbb G_m$ intersect.  The point $(0_1,0_2)$ in the closure of the diagonal in step [](#not-separated){.pf-ref} is the scheme-theoretic form of this statement.
:::

:::

::: pf-qed
Step [](#not-separated){.pf-ref} supplies the requested non-separated morphism.
:::

:::
:::
