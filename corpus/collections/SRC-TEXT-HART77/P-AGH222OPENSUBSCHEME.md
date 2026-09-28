---
schema: qual/card@1
id: P-AGH222OPENSUBSCHEME
kind: problem
title: Open subsets of a scheme carry an induced scheme structure
classification:
  areas:
  - algebraic-geometry
  topics:
  - Schemes
  - Open Subschemes
  - Locally Ringed Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.2.2 statement and source-order placement after II.2.1.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $(X, \OO_X)$ be a scheme and let $U \subseteq X$ be any open subset.
Show that $\qty{U, \ro{\OO_X}{U}}$ is a scheme.
We call this the **induced scheme structure** on the open set $U$, and we refer to $\qty{U, \ro{\OO_X}{U}}$ as an **open subscheme** of $X$.
:::

::: {.solution}
<1>1. The restricted ringed space
\[
(U,\mathcal O_X|_U)
\]
is a locally ringed space.
::: {.proof}
For a point $P\in U$, the stalk of the restricted sheaf is naturally
\[
(\mathcal O_X|_U)_P\cong\mathcal O_{X,P}.
\]
Since $X$ is a scheme, $\mathcal O_{X,P}$ is a local ring.  Hence every stalk of the restricted sheaf is local.
:::

<1>2. Fix $P\in U$.  Choose an affine open neighborhood
\[
P\in V\subseteq X,
\qquad
V\cong\operatorname{Spec}A.
\]
Then
\[
U\cap V
\]
is an open neighborhood of $P$ in $V$.
::: {.proof}
The affine neighborhoods form a cover of the scheme $X$, so such a $V$ exists.  Since both $U$ and $V$ are open in $X$, their intersection is open, and it contains $P$.
:::

<1>3. There exists
\[
f\in A
\]
such that
\[
P\in D_V(f)\subseteq U\cap V.
\]
::: {.proof}
The distinguished opens
\[
D_V(f),
\qquad f\in A,
\]
form a basis for the Zariski topology on
\[
V=\operatorname{Spec}A.
\]
Since $U\cap V$ is an open neighborhood of $P$, some distinguished basic neighborhood of $P$ is contained in it.
:::

<1>4. With its induced structure sheaf,
\[
D_V(f)
\]
is an affine scheme:
\[
\boxed{
\left(D_V(f),\mathcal O_X|_{D_V(f)}\right)
\cong
\operatorname{Spec}A_f.
}
\]
::: {.proof}
On the affine open $V$, the restricted structure sheaf is its usual affine structure sheaf.  Hartshorne II.2.1 identifies every distinguished open of an affine scheme with the spectrum of the corresponding localization:
\[
\left(D_V(f),\mathcal O_V|_{D_V(f)}\right)
\cong
\operatorname{Spec}A_f.
\]
Since
\[
\mathcal O_V=\mathcal O_X|_V,
\]
this is the displayed isomorphism.
:::

<1>5. The distinguished affine opens obtained in <1>3--<1>4 cover $U$.
::: {.proof}
For every point $P\in U$, steps <1>2--<1>4 construct an affine open neighborhood
\[
P\in D_V(f)\subseteq U.
\]
Taking all such neighborhoods gives an open affine cover of $U$.
:::

<1>6. Therefore
\[
\boxed{(U,\mathcal O_X|_U)\text{ is a scheme}.}
\]
::: {.proof}
By <1>1 it is a locally ringed space, and by <1>5 it admits an open cover by affine schemes.  This is exactly the definition of a scheme.
:::

<1>7. Q.E.D.
::: {.proof}
Step <1>6 proves that every open subset of a scheme carries the induced open-subscheme structure.
:::
:::
