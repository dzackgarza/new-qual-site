---
schema: qual/card@1
id: P-AGH381DEGENLERAY
kind: problem
title: Vanishing higher direct images give isomorphic cohomology
classification:
  areas:
  - algebraic-geometry
  topics:
  - Higher Direct Images
  - Leray Spectral Sequence
  - Sheaf Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: "Read Exercise III.8.1 and the definition of the higher direct images as the right derived functors of f_* in Hartshorne III.8. The proof uses an injective resolution: f_* preserves injectives because it is right adjoint to the exact inverse-image functor, and the assumed vanishing makes the pushed-forward complex an injective resolution of f_*F."
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $f: X \to Y$ be a continuous map of topological spaces. Let $\mcf$ be a sheaf of abelian groups on $X$, and assume that $R^i f_*(\mcf) = 0$ for all $i > 0$. Show that there are natural isomorphisms, for each $i \geq 0$,
\[
H^i(X, \mcf) \cong H^i(Y, f_* \mcf)
.\]

This is a degenerate case of the Leray spectral sequence; see Godement [1, II, 4.17.1].
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The direct-image functor $f_*$ sends injective sheaves on $X$ to injective sheaves on $Y$.

::: pf-proof

The inverse-image functor
$$
f^{-1}:\operatorname{Ab}(Y)\longrightarrow\operatorname{Ab}(X)
$$
is exact for sheaves of abelian groups, and it is left adjoint to $f_*$:
$$
\operatorname{Hom}_X(f^{-1}\mcg,\mci)
\cong
\operatorname{Hom}_Y(\mcg,f_*\mci).
$$
Let $\mci$ be injective on $X$.
Given a monomorphism $\mcg'\hookrightarrow\mcg$ on $Y$, exactness of $f^{-1}$ makes
$$
f^{-1}\mcg'\hookrightarrow f^{-1}\mcg
$$
a monomorphism.
Injectivity of $\mci$ therefore makes
$$
\operatorname{Hom}_X(f^{-1}\mcg,\mci)
\longrightarrow
\operatorname{Hom}_X(f^{-1}\mcg',\mci)
$$
surjective.
By adjunction, the same is true for
$$
\operatorname{Hom}_Y(\mcg,f_*\mci)
\longrightarrow
\operatorname{Hom}_Y(\mcg',f_*\mci),
$$
so $f_*\mci$ is injective.

:::

:::

::: {.pf-step #s2}

If
$$
0\longrightarrow\mcf\longrightarrow\mci^0\longrightarrow\mci^1\longrightarrow\cdots
$$
is an injective resolution on $X$, then under the hypothesis $R^if_*\mcf=0$ for $i>0$,
$$
0\longrightarrow f_*\mcf\longrightarrow f_*\mci^0\longrightarrow f_*\mci^1\longrightarrow\cdots
$$
is an injective resolution on $Y$.

::: pf-proof

By step [](#s1){.pf-ref} every $f_*\mci^q$ is injective.
By definition, the cohomology sheaves of the complex
$$
f_*\mci^0\longrightarrow f_*\mci^1\longrightarrow\cdots
$$
are the derived functors
$$
R^if_*\mcf.
$$
The degree-zero cohomology is $f_*\mcf$, because $f_*$ is left exact, and all positive-degree cohomology sheaves vanish by hypothesis.
Thus adjoining $f_*\mcf$ in degree zero makes the displayed complex exact.
It is therefore an injective resolution of $f_*\mcf$.

:::

:::

::: {.pf-step #s3}

Applying global sections to the two resolutions gives the same cochain complex.

::: pf-proof

For every sheaf $\mci$ on $X$, the definition of direct image gives
$$
\Gamma(Y,f_*\mci)
=(f_*\mci)(Y)
=\mci(f^{-1}Y)
=\mci(X)
=\Gamma(X,\mci).
$$
Hence term by term,
$$
\Gamma(Y,f_*\mci^q)=\Gamma(X,\mci^q),
$$
and these equalities commute with the differentials.
So the global-section complexes calculating the two cohomologies are identical.

:::

:::

::: {.pf-step #s4}

For every $i\ge0$ there is a natural isomorphism
$$
\boxed{H^i(X,\mcf)\cong H^i(Y,f_*\mcf)}.
$$

::: pf-proof

The injective resolution $\mci^\bullet$ computes
$$
H^i(X,\mcf)
=H^i\bigl(\Gamma(X,\mci^\bullet)\bigr).
$$
By step [](#s2){.pf-ref}, $f_*\mci^\bullet$ is an injective resolution of $f_*\mcf$, so it computes
$$
H^i(Y,f_*\mcf)
=H^i\bigl(\Gamma(Y,f_*\mci^\bullet)\bigr).
$$
Step [](#s3){.pf-ref} identifies these cochain complexes canonically, hence identifies their cohomology groups.
The construction is natural in $\mcf$ because comparison morphisms between injective resolutions are unique up to homotopy and the identification $\Gamma(Y,f_*(-))=\Gamma(X,-)$ is functorial.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives the required natural isomorphisms in every degree.

:::

:::

:::
