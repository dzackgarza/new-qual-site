---
schema: qual/card@1
id: P-AGH3111PUNCTAFFINE
kind: problem
title: Higher direct images on punctured affine space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Formal Functions
  - Higher Direct Images
  - Local Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Checked Exercise III.11.1 against the retained Hartshorne source context.
    Independently computed the cohomology of punctured affine space with the
    standard distinguished-open Cech cover, and checked the passage from
    cohomology to higher direct image against Stacks Project Tags 01XD, 01XJ,
    and 01XK. No source solution was used.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Show that the result of (11.2) is false without the projective hypothesis. For example, let $X = \AA_k^n$, let $P = (0, \ldots, 0)$, let $U = X - P$, and let $f: U \to X$ be the inclusion. Then the fibres of $f$ all have dimension $0$, but
\[
R^{n-1} f_* \mco_U \neq 0
.\]
:::

::: {.solution}
Write
$$
A=k[x_1,\ldots,x_n],
\qquad
X=\Spec A,
\qquad
P=V(x_1,\ldots,x_n).
$$

::: pf

::: {.pf-step #s1}

Every nonempty fibre of $f$ is a single point, and the fibre over $P$ is empty.

::: pf-proof

The map $f:U\hookrightarrow X$ is an open immersion. Hence for $x\in U$,
$$
U\times_X\Spec\kappa(x)\cong\Spec\kappa(x),
$$
whereas
$$
U\times_X\Spec\kappa(P)=\varnothing.
$$
Thus every fibre has dimension at most $0$; in particular the morphism has the
fibre-dimension bound appearing in the result whose projective hypothesis is
being tested.

:::

:::

::: {.pf-step #s2}

For every $q\ge0$,
$$
H^q(U,\mco_U)
\cong
\Gamma\bigl(X,R^qf_*\mco_U\bigr).
$$

::: pf-proof

We have the finite affine cover
$$
U=D(x_1)\cup\cdots\cup D(x_n),
$$
so the open immersion $f$ is quasi-compact; every open immersion is
quasi-separated. Since $X$ is affine and $\mco_U$ is quasicoherent, the
[affine-base higher-direct-image formula](https://stacks.math.columbia.edu/tag/01XK)
gives the displayed isomorphism. Equivalently, this is the collapse of the
Leray spectral sequence after using
[quasi-coherence of higher direct images](https://stacks.math.columbia.edu/tag/01XJ).

:::

:::

::: {.pf-step #s3}

If $n=1$, then
$$
R^0f_*\mco_U\ne0.
$$

::: pf-proof

In this case
$$
U=D(x_1)=\Spec k[x_1,x_1^{-1}],
$$
so
$$
H^0(U,\mco_U)=k[x_1,x_1^{-1}]\ne0.
$$
Step [](#s2){.pf-ref} with $q=0$ gives
$$
\Gamma(X,R^0f_*\mco_U)\ne0,
$$
hence the sheaf $R^0f_*\mco_U$ is nonzero.

:::

:::

::: {.pf-step #s4}

Assume $n\ge2$. The cover
$$
\mathcal U=\{D(x_i)\}_{i=1}^n
$$
computes $H^\bullet(U,\mco_U)$ by its alternating Cech complex.

::: pf-proof

Every nonempty finite intersection is a distinguished affine open:
$$
D(x_{i_0})\cap\cdots\cap D(x_{i_p})
=
D(x_{i_0}\cdots x_{i_p}).
$$
Therefore the Cech-to-derived-cohomology map is an isomorphism for the
quasicoherent sheaf $\mco_U$; see the
[affine-intersection Cech comparison](https://stacks.math.columbia.edu/tag/01XD).

:::

:::

::: {.pf-step #s5}

The top nonzero Cech cohomology group is
$$
H^{n-1}(U,\mco_U)
\cong
\frac{A_{x_1\cdots x_n}}
{\displaystyle\sum_{i=1}^n
 A_{x_1\cdots\widehat{x_i}\cdots x_n}}.
$$

::: pf-proof

The degree-$n-1$ term of the alternating Cech complex is the single
localization
$$
A_{x_1\cdots x_n}.
$$
There is no outgoing differential. The image of the degree-$n-2$ differential
is the sum of the images of the $n$ localizations obtained by omitting one
$x_i$, with signs that do not affect the generated submodule. Taking the
cokernel gives the displayed quotient.

:::

:::

::: {.pf-step #s6}

The class
$$
\left[\frac1{x_1\cdots x_n}\right]
\in H^{n-1}(U,\mco_U)
$$
is nonzero.

::: pf-proof

The ring
$$
A_{x_1\cdots x_n}
=
k[x_1^{\pm1},\ldots,x_n^{\pm1}]
$$
has the Laurent monomials
$$
x_1^{a_1}\cdots x_n^{a_n},
\qquad
(a_1,\ldots,a_n)\in\ZZ^n,
$$
as a $k$-basis.

For fixed $i$, every Laurent monomial occurring in
$$
A_{x_1\cdots\widehat{x_i}\cdots x_n}
$$
has exponent of $x_i$ at least $0$. Consequently the sum in the denominator of
step [](#s5){.pf-ref} is spanned by Laurent monomials having at least one nonnegative
exponent.

The monomial
$$
x_1^{-1}\cdots x_n^{-1}
$$
has every exponent equal to $-1$, so it does not lie in that sum. Its class is
therefore nonzero.

:::

:::

::: {.pf-step #s7}

For $n\ge2$,
$$
R^{n-1}f_*\mco_U\ne0.
$$

::: pf-proof

By step [](#s6){.pf-ref},
$$
H^{n-1}(U,\mco_U)\ne0.
$$
Step [](#s2){.pf-ref} identifies this group with
$$
\Gamma\bigl(X,R^{n-1}f_*\mco_U\bigr).
$$
A sheaf with a nonzero global section is nonzero, proving the claim.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} gives the required fibre-dimension bound. Step [](#s3){.pf-ref} proves the
assertion when $n=1$, and steps [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} prove it when $n\ge2$. Thus the
projective hypothesis in (11.2) cannot be omitted.

:::

:::

:::
