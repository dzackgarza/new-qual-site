---
schema: qual/card@1
id: P-AGH383PROJFORMULA
kind: problem
title: The projection formula for higher direct images
classification:
  areas:
  - algebraic-geometry
  topics:
  - Higher Direct Images
  - Locally Free Sheaves
  - Ringed Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise III.8.3 and its reference to the ordinary projection formula II.5.1. The proof tensors an injective resolution by the finite locally free pullback f^*E, which preserves injectives because tensoring by a finite locally free sheaf is an exact autoequivalence up to dual, applies the ordinary projection formula termwise, and then takes cohomology.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $f: X \to Y$ be a morphism of ringed spaces, let $\mcf$ be an $\mco_X\dash$module, and let $\mce$ be a locally free $\mco_Y\dash$module of finite rank. Prove the projection formula (cf. (II, Ex. 5.1)):
\[
R^i f_*(\mcf \tensor f^* \mce) \cong R^i f_*(\mcf) \tensor \mce
.\]
:::

::: {.solution}
Let
$$
0\longrightarrow\mcf\longrightarrow\mci^0\longrightarrow\mci^1\longrightarrow\cdots
$$
be an injective resolution of $\mcf$ as an $\mco_X$-module.

::: pf

::: {.pf-step #s1}

Tensoring by $f^*\mce$ is exact and sends injective $\mco_X$-modules to injective $\mco_X$-modules.

::: pf-proof

Because $\mce$ is locally free of finite rank on $Y$, its pullback $f^*\mce$ is locally free of finite rank on $X$.
Let
$$
(f^*\mce)^\vee=\mathcal Hom_{\mco_X}(f^*\mce,\mco_X).
$$
There are natural adjunction isomorphisms
$$
\operatorname{Hom}_{\mco_X}(\mca,\mcb\tensor f^*\mce)
\cong
\operatorname{Hom}_{\mco_X}(\mca\tensor(f^*\mce)^\vee,\mcb).
$$
Both tensor functors with $f^*\mce$ and with its dual are exact, because these sheaves are locally free.
Hence tensoring by $f^*\mce$ has an exact left adjoint and therefore preserves injective objects.
It is itself exact as well.

:::

:::

::: {.pf-step #s2}

The complex
$$
0\longrightarrow\mcf\tensor f^*\mce
\longrightarrow\mci^0\tensor f^*\mce
\longrightarrow\mci^1\tensor f^*\mce
\longrightarrow\cdots
$$
is an injective resolution of $\mcf\tensor f^*\mce$.

::: pf-proof

Exactness follows from exactness of tensoring by $f^*\mce$, established in step [](#s1){.pf-ref}.
Each term $\mci^q\tensor f^*\mce$ is injective by the same step.
Thus the displayed complex is an injective resolution.

:::

:::

::: {.pf-step #s3}

For every $q\ge0$, the ordinary projection formula gives a natural isomorphism
$$
f_*(\mci^q\tensor f^*\mce)
\cong
f_*\mci^q\tensor\mce.
$$

::: pf-proof

This is the projection formula for ordinary direct images, Hartshorne II, Exercise 5.1, applied to the $\mco_X$-module $\mci^q$ and the finite locally free $\mco_Y$-module $\mce$.
The isomorphisms are functorial in $\mci^q$, so they commute with the differentials of the resolution and identify the two cochain complexes
$$
f_*(\mci^\bullet\tensor f^*\mce)
\cong
f_*\mci^\bullet\tensor\mce.
$$

:::

:::

::: {.pf-step #s4}

Taking cohomology of the right-hand complex gives
$$
H^i(f_*\mci^\bullet\tensor\mce)
\cong
H^i(f_*\mci^\bullet)\tensor\mce.
$$

::: pf-proof

Tensoring by the locally free sheaf $\mce$ is exact.
For an exact functor $T$ and any cochain complex $C^\bullet$, kernels, images, and quotients are preserved, so
$$
H^i(TC^\bullet)\cong T(H^i(C^\bullet)).
$$
Apply this to
$$
T=(-)\tensor\mce,
\qquad
C^\bullet=f_*\mci^\bullet.
$$

:::

:::

::: {.pf-step #s5}

For every $i\ge0$ there is a natural isomorphism
$$
\boxed{
R^if_*(\mcf\tensor f^*\mce)
\cong
R^if_*(\mcf)\tensor\mce}.
$$

::: pf-proof

By step [](#s2){.pf-ref},
$$
R^if_*(\mcf\tensor f^*\mce)
=H^i\bigl(f_*(\mci^\bullet\tensor f^*\mce)\bigr).
$$
Step [](#s3){.pf-ref} identifies this with
$$
H^i(f_*\mci^\bullet\tensor\mce),
$$
which step [](#s4){.pf-ref} identifies with
$$
H^i(f_*\mci^\bullet)\tensor\mce
=R^if_*(\mcf)\tensor\mce.
$$
Every map used is natural in $\mcf$ and $\mce$, so the resulting isomorphism is natural.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required projection formula in every degree.

:::

:::

:::
