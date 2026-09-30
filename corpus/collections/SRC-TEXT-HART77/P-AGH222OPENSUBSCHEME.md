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
Show that $\qty{U, \restrictionof{\OO_X}{U}}$ is a scheme.
We call this the **induced scheme structure** on the open set $U$, and we refer to $\qty{U, \restrictionof{\OO_X}{U}}$ as an **open subscheme** of $X$.
:::

::: {.solution}

::: pf

::: {.pf-step #restricted-space-locally-ringed}
The restricted ringed space
\[
(U,\mathcal O_X|_U)
\]
is a locally ringed space.

::: pf-proof
For a point $P\in U$, the stalk of the restricted sheaf is naturally
\[
(\mathcal O_X|_U)_P\cong\mathcal O_{X,P}.
\]
Since $X$ is a scheme, $\mathcal O_{X,P}$ is a local ring.  Hence every stalk of the restricted sheaf is local.
:::

:::

::: {.pf-step #affine-neighborhood-exists}
Fix $P\in U$.  Choose an affine open neighborhood
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

::: pf-proof
The affine neighborhoods form a cover of the scheme $X$, so such a $V$ exists.  Since both $U$ and $V$ are open in $X$, their intersection is open, and it contains $P$.
:::

:::

::: {.pf-step #distinguished-open-in-intersection}
There exists
\[
f\in A
\]
such that
\[
P\in D_V(f)\subseteq U\cap V.
\]

::: pf-proof
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

:::

::: {.pf-step #dvf-affine-scheme}
With its induced structure sheaf,
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

::: pf-proof
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

:::

::: {.pf-step #distinguished-opens-cover-u}
The distinguished affine opens obtained in steps [](#distinguished-open-in-intersection){.pf-ref} and [](#dvf-affine-scheme){.pf-ref} cover $U$.

::: pf-proof
For every point $P\in U$, steps [](#affine-neighborhood-exists){.pf-ref}, [](#distinguished-open-in-intersection){.pf-ref} and [](#dvf-affine-scheme){.pf-ref} construct an affine open neighborhood
\[
P\in D_V(f)\subseteq U.
\]
Taking all such neighborhoods gives an open affine cover of $U$.
:::

:::

::: {.pf-step #u-is-scheme}
Therefore
\[
\boxed{(U,\mathcal O_X|_U)\text{ is a scheme}.}
\]

::: pf-proof
By step [](#restricted-space-locally-ringed){.pf-ref} it is a locally ringed space, and by step [](#distinguished-opens-cover-u){.pf-ref} it admits an open cover by affine schemes.  This is exactly the definition of a scheme.
:::

:::

::: pf-qed
Step [](#u-is-scheme){.pf-ref} proves that every open subset of a scheme carries the induced open-subscheme structure.
:::

:::

:::
