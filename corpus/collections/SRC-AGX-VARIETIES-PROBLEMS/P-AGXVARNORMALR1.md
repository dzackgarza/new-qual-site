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

::: pf

::: {.pf-step #local-ring-dim-one}
Let $Z\subseteq X$ be an irreducible closed subset of codimension one,
and let $\eta$ be its generic point. Then
$$
\dim\mco_{X,\eta}=1.
$$

::: pf-proof
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

:::

::: {.pf-step #local-ring-regular}
The local ring $\mco_{X,\eta}$ is a discrete valuation ring and hence
regular.

::: pf-proof
Because $X$ is normal, every local ring of $X$ is a normal domain. Projective
varieties are Noetherian, so
$$
\mco_{X,\eta}
$$
is a one-dimensional Noetherian normal local domain by step [](#local-ring-dim-one){.pf-ref}.

By the one-dimensional normality criterion
[[D-QJ5M9]], such a ring is a discrete valuation ring. A DVR is
regular.
:::

:::

::: {.pf-step #smooth-codim-one-points}
The variety $X$ is smooth at every codimension-one point.

::: pf-proof
The ground field $\CC$ is perfect. For a variety of finite type over a
perfect field, regularity of the local ring is equivalent to smoothness at
the corresponding point. Step [](#local-ring-regular){.pf-ref} therefore makes every codimension-one
point smooth.
:::

:::

::: {.pf-step #no-codim-one-singular-component}
No irreducible component of $\operatorname{Sing}(X)$ has codimension
one.

::: pf-proof
Suppose that
$$
Z\subseteq\operatorname{Sing}(X)
$$
were an irreducible component of codimension one, with generic point
$\eta$. Since the singular locus is closed, it contains $\eta$.

But step [](#smooth-codim-one-points){.pf-ref} says that $X$ is smooth at every codimension-one point,
including $\eta$. Thus
$$
\eta\notin\operatorname{Sing}(X),
$$
a contradiction.
:::

:::

::: {.pf-step #codim-bound}
Therefore every irreducible component $Z$ of the singular locus
satisfies
$$
\boxed{\codim(Z,X)\geq2.}
$$

::: pf-proof
The singular locus is a proper closed subset of the projective variety $X$,
so every irreducible component has positive codimension. Step [](#no-codim-one-singular-component){.pf-ref} excludes
codimension one. Therefore every component has codimension at least two.
:::

:::

::: pf-qed
Steps [](#local-ring-dim-one){.pf-ref}, [](#local-ring-regular){.pf-ref} and [](#smooth-codim-one-points){.pf-ref} establish regularity and smoothness at every
codimension-one point, and steps [](#no-codim-one-singular-component){.pf-ref} and [](#codim-bound){.pf-ref} convert this into the
codimension bound for the singular locus.
:::

:::

:::
