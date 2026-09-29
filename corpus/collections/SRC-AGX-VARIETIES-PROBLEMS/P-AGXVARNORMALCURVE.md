---
schema: qual/card@1
id: P-AGXVARNORMALCURVE
kind: problem
title: Normal affine curves are smooth
classification:
  areas:
  - algebraic-geometry
  topics:
  - Normality
  - Curves
  - Smoothness
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the normality definitions in Zaidenberg section 5 and the corresponding
    clause of Exercises 6.5 in the recorded source. Over the standing field
    k=C it asks that every normal affine curve be smooth.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Made the source's standing field k=C explicit on the standalone card.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Localized the normal coordinate domain at an arbitrary point, used that a
    one-dimensional Noetherian normal local domain is a DVR and therefore
    regular, and then used regular equals smooth over the perfect field C.
---

::: {.problem}
Show that every normal affine curve over $\CC$ is smooth.
:::

::: {.solution}
Let
$$
X=\mspec A
$$
be a normal affine curve over $\CC$.
Thus $A$ is a finitely generated integral $\CC$-algebra of dimension $1$ and is integrally closed in its fraction field.

::: pf

::: {.pf-step #local-ring-normal-1dim}
For every point $p\in X$, the local ring
$$
\mco_{X,p}=A_{\mathfrak m_p}
$$
is a one-dimensional Noetherian normal local domain.

::: pf-proof
Because $A$ is finitely generated over a field, it is Noetherian.
Localization preserves the Noetherian property and the domain property.

Normality also localizes.
Indeed, if
$$
\frac ab\in\Frac(A)
$$
is integral over $A_{\mathfrak m_p}$, then after clearing the finitely many denominators occurring in a monic integral equation, there is some
$$
s\in A\setminus\mathfrak m_p
$$
such that
$$
s\frac ab
$$
is integral over $A$.
Since $A$ is integrally closed,
$$
s\frac ab\in A,
$$
and hence
$$
\frac ab\in A_{\mathfrak m_p}.
$$
Thus $A_{\mathfrak m_p}$ is normal.

Finally, $p$ is a closed point of the affine curve and
$$
\dim X=1.
$$
The affine dimension theorem gives
$$
\dim A_{\mathfrak m_p}=1.
$$
:::

:::

::: {.pf-step #local-ring-dvr-regular}
Every local ring $\mco_{X,p}$ is a discrete valuation ring and hence regular.

::: pf-proof
By step [](#local-ring-normal-1dim){.pf-ref}, $\mco_{X,p}$ is a one-dimensional Noetherian normal local domain.
By the one-dimensional normality criterion [[D-QJ5M9]], such a ring is a discrete valuation ring.
A DVR is a regular local ring of dimension $1$.
:::

:::

::: {.pf-step #every-point-smooth}
Every point $p\in X$ is smooth.

::: pf-proof
The field $\CC$ is perfect.
For a variety of finite type over a perfect field, a point is smooth exactly when its local ring is regular.
Step [](#local-ring-dvr-regular){.pf-ref} shows that
$$
\mco_{X,p}
$$
is regular for every $p\in X$.
Hence every point is smooth.
:::

:::

::: {.pf-step #x-smooth}
Therefore
$$
\boxed{X\text{ is smooth}.}
$$

::: pf-proof
A variety is smooth when it is smooth at every point.
This is step [](#every-point-smooth){.pf-ref}.
:::

:::

::: pf-qed
Steps [](#local-ring-normal-1dim){.pf-ref}, [](#local-ring-dvr-regular){.pf-ref}, [](#every-point-smooth){.pf-ref} and [](#x-smooth){.pf-ref} prove that normality of an affine curve over $\CC$ forces smoothness.
:::

:::

:::
