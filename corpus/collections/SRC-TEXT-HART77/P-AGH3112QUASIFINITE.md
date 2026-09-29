---
schema: qual/card@1
id: P-AGH3112QUASIFINITE
kind: problem
title: A projective quasi-finite morphism is finite
classification:
  areas:
  - algebraic-geometry
  topics:
  - Formal Functions
  - Finite Morphisms
  - Projective Morphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.11.2 in its Hartshorne source context together with
    Corollary III.11.2. The proof below follows the intended formal-functions
    route: zero-dimensional fibres kill R^1 of every coherent ideal, Serre's
    cohomological criterion makes the source affine over each affine base open,
    and coherence of projective pushforward then gives module finiteness. This
    was cross-checked against Stacks Project Tag 02OG rather than replaced by a
    circular citation to proper plus quasi-finite implies finite.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Show that a projective morphism with finite fibres, that is, a quasi-finite projective morphism (II, Ex.
3.5), is a finite morphism.
:::

::: {.solution}
We use the standing Noetherian hypotheses of Chapter III.

::: pf

::: pf-step

It is enough to prove the assertion after replacing the target by an arbitrary affine open subset.

::: pf-proof

Finiteness of a morphism is local on the target. If $V\subseteq Y$ is open,
then the base change
$$
f_V:f^{-1}(V)\longrightarrow V
$$
is again projective and has finite fibres. Thus it suffices to prove that
$f_V$ is finite for every affine open $V\subseteq Y$.

:::

:::

::: {.pf-step #s2}

Assume henceforth that $Y$ is affine. For every coherent ideal sheaf
$\mci\subseteq\mco_X$,
$$
R^1f_*\mci=0.
$$

::: pf-proof

Every fibre of $f$ is finite, hence has dimension $0$ when nonempty. Therefore
the maximum fibre dimension in [@Har10a, Corollary III.11.2] is
$$
r=0.
$$
That corollary says that for a projective morphism and every coherent sheaf
$\mcf$,
$$
R^if_*\mcf=0
\qquad
(i>r).
$$
Applying it to $\mcf=\mci$ and $i=1$ gives the claim.

:::

:::

::: {.pf-step #s3}

For every coherent ideal sheaf $\mci\subseteq\mco_X$,
$$
H^1(X,\mci)=0.
$$

::: pf-proof

The low-degree part of the [[T-COHLERAY|Leray spectral sequence]] gives
$$
0
\longrightarrow H^1(Y,f_*\mci)
\longrightarrow H^1(X,\mci)
\longrightarrow H^0(Y,R^1f_*\mci).
$$
Because $f$ is projective and $\mci$ is coherent, $f_*\mci$ is coherent by
the coherence theorem for projective direct images [@Har10a, Theorem III.8.8].
Since $Y$ is affine,
$$
H^1(Y,f_*\mci)=0
$$
by [[T-COHAFF|affine vanishing]]. Step [](#s2){.pf-ref} gives
$$
H^0(Y,R^1f_*\mci)=0.
$$
Hence the middle group is zero.

:::

:::

::: {.pf-step #s4}

The scheme $X$ is affine.

::: pf-proof

Step [](#s3){.pf-ref} proves
$$
H^1(X,\mci)=0
$$
for every coherent ideal sheaf $\mci$ on the Noetherian scheme $X$.
Therefore [[T-5IOUR|Serre's cohomological criterion for affineness]] gives
that $X$ is affine.

:::

:::

::: {.pf-step #s5}

Writing
$$
Y=\Spec A,
\qquad
X=\Spec B,
$$
the $A$-module $B$ is finite.

::: pf-proof

The structure sheaf $\mco_X$ is coherent. Since $f$ is projective, the
coherence theorem for projective direct images gives that
$$
f_*\mco_X
$$
is a coherent $\mco_Y$-module. On the affine scheme $Y=\Spec A$, its module
of global sections is therefore a finite $A$-module.

But
$$
\Gamma(Y,f_*\mco_X)
=
\Gamma(X,\mco_X)
=B.
$$
Thus $B$ is finite as an $A$-module.

:::

:::

::: pf-qed

By steps [](#s4){.pf-ref} and [](#s5){.pf-ref}, over every affine open $V=\Spec A\subseteq Y$ the
inverse image is affine,
$$
f^{-1}(V)=\Spec B,
$$
with $B$ a finite $A$-module. This is exactly the definition of a finite
morphism. Hence $f$ is finite.

:::

:::

:::
