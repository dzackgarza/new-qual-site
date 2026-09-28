---
schema: qual/card@1
id: P-AGXVARSMOOTHNORMAL
kind: problem
title: Smoothness against normality
classification:
  areas:
  - algebraic-geometry
  topics:
  - Smoothness
  - Normality
  - Singularities
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Definitions 5.2 and 6.1 together with Exercises 6.5 in the
    recorded source. The source supplies both comparison facts used here:
    normal affine curves are smooth, while the Veronese quotient cone
    A^2/mu_n for n>1 is a normal affine surface with a singular point.
    The standalone comparison question is synthesized from that material.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Made the algebraically closed characteristic-zero ground field explicit and
    stated the converse failure with its dimension-one exception.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Used smooth over a perfect field implies regular local rings, regular local
    rings are normal, and the completed cyclic quotient surface as an explicit
    normal singular counterexample. The completed normal-curve card records
    the dimension-one converse.
---

::: {.problem}
Let $X$ be a variety over an algebraically closed field $k$ of
characteristic zero.

(a) Does smoothness imply normality?

(b) Does normality imply smoothness? If not, what happens for curves?
:::

::: {.solution}
<1>1. If $X$ is smooth, then every local ring
$$
\mco_{X,p}
$$
is regular.

::: {.proof}
The field $k$ is perfect because it is algebraically closed. For schemes
locally of finite type over a perfect field, smoothness implies regularity;
indeed smoothness and regularity are equivalent in this setting by
[[T-MORSMREG]].

Therefore, if $X$ is smooth, then for every point $p\in X$ the local ring
$\mco_{X,p}$ is regular.
:::

<1>2. Every smooth variety $X$ is normal.

::: {.proof}
By step <1>1, every local ring $\mco_{X,p}$ is a regular local ring. Every
regular local ring is a normal domain by [[D-QJ5M9]]. Hence every local ring
of $X$ is normal.

By definition, a variety whose local rings are all normal is normal.
Therefore
$$
\boxed{X\text{ smooth }\Longrightarrow X\text{ normal}.}
$$
This proves (a).
:::

<1>3. Normality does not imply smoothness in dimension at least $2$.

::: {.proof}
Let $n>1$ and let
$$
\mu_n
=
\{\zeta\in\CC^\times:\zeta^n=1\}
$$
act on $\AA^2_\CC$ by scalar multiplication. The quotient
$$
V_n
=
\AA^2_\CC/\mu_n
$$
is the Veronese cyclic quotient surface from
[[P-AGXVAREXQUOTSING|the cyclic quotient singularity calculation]].

That card proves that $V_n$ is a normal affine surface and that the image of
the origin is singular. Thus
$$
V_n\text{ is normal but not smooth}.
$$
Therefore the converse to step <1>2 fails already in dimension $2$.
:::

<1>4. For curves, normality does imply smoothness.

::: {.proof}
Let $C$ be a normal curve over $k$. At every closed point $p\in C$, the
local ring $\mco_{C,p}$ is a one-dimensional Noetherian normal local domain.
Such a ring is a discrete valuation ring, hence regular, by [[D-QJ5M9]].
Because $k$ is perfect, regularity is equivalent to smoothness by
[[T-MORSMREG]].

For affine curves this argument is carried out in
[[P-AGXVARNORMALCURVE|normal affine curves are smooth]], and the projective
case is [[P-AGXVARNORMALPROJCURVE|normal projective curves are smooth]].
Thus
$$
\boxed{
\dim C=1,\ C\text{ normal}
\Longrightarrow
C\text{ smooth}.
}
$$
:::

<1>5. The precise comparison is:
$$
\boxed{
\text{smooth}\Longrightarrow\text{normal},
}
$$
the converse fails in dimension $\geq2$, and it holds for curves.

::: {.proof}
Step <1>2 proves smooth implies normal. Step <1>3 gives a normal singular
surface, so the converse fails in dimension at least two. Step <1>4 proves
the dimension-one converse.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 answers both parts of the problem.
:::
:::
