---
schema: qual/card@1
id: P-AGXVARNORMALR1
kind: problem
title: Normal varieties are smooth in codimension one
classification:
  areas:
  - algebraic-geometry
  topics:
  - Normality
  - Smoothness
  - Codimension
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Proposition 8.3 in the recorded source. It states that for
    a normal projective variety every irreducible component of the singular
    locus has codimension at least 2.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Replaced the context-free phrase "normal implies smooth in codimension 1"
    by the source's projective statement over C, while retaining the equivalent
    regular-in-codimension-one interpretation in the solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    At a codimension-one generic point, checked that normality gives a
    one-dimensional Noetherian normal local domain, hence a DVR and a regular
    local ring. Over C this is a smooth point, excluding codimension-one
    components of the singular locus.
---

::: {.problem}
Let $X$ be a normal projective variety over $\CC$. Show that every
irreducible component of
$$
\operatorname{Sing}(X)
$$
has codimension at least $2$ in $X$. Equivalently, $X$ is smooth in
codimension one.
:::

::: {.solution}
<1>1. Let $Z\subseteq X$ be an irreducible closed subset of codimension one,
and let $\eta$ be its generic point. Then
$$
\dim\mco_{X,\eta}=1.
$$

::: {.proof}
The point $\eta$ corresponds to a height-one prime in any affine
neighborhood of $\eta$. The Krull dimension of the local ring at a prime is
the height of that prime. Hence
$$
\dim\mco_{X,\eta}
=
\height(\eta)
=
1.
$$
:::

<1>2. The local ring $\mco_{X,\eta}$ is a discrete valuation ring and hence
regular.

::: {.proof}
Because $X$ is normal, every local ring of $X$ is a normal domain. Projective
varieties are Noetherian, so
$$
\mco_{X,\eta}
$$
is a one-dimensional Noetherian normal local domain by step <1>1.

The one-dimensional normality criterion
[[D-QJ5M9|says]] that such a ring is a discrete valuation ring. A DVR is
regular.
:::

<1>3. The variety $X$ is smooth at every codimension-one point.

::: {.proof}
The ground field $\CC$ is perfect. For a variety of finite type over a
perfect field, regularity of the local ring is equivalent to smoothness at
the corresponding point. Step <1>2 therefore makes every codimension-one
point smooth.
:::

<1>4. No irreducible component of $\operatorname{Sing}(X)$ has codimension
one.

::: {.proof}
Suppose that
$$
Z\subseteq\operatorname{Sing}(X)
$$
were an irreducible component of codimension one, with generic point
$\eta$. Since the singular locus is closed, it contains $\eta$.

But step <1>3 says that $X$ is smooth at every codimension-one point,
including $\eta$. Thus
$$
\eta\notin\operatorname{Sing}(X),
$$
a contradiction.
:::

<1>5. Therefore every irreducible component $Z$ of the singular locus
satisfies
$$
\boxed{\codim(Z,X)\geq2.}
$$

::: {.proof}
The singular locus is a proper closed subset of the projective variety $X$,
so every irreducible component has positive codimension. Step <1>4 excludes
codimension one. Therefore every component has codimension at least two.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 establish regularity and smoothness at every
codimension-one point, and steps <1>4--<1>5 convert this into the source's
codimension statement for the singular locus.
:::
:::
