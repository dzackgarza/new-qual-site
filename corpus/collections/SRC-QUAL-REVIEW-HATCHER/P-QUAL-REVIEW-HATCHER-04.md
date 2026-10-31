---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-04
kind: problem
title: Degree of the coordinate-squaring map of the sphere
classification:
  areas: [topology]
  topics:
  - Degree of a Map
  - Spheres
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against practice problem 4 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md (Mistral OCR), which agrees with the earlier MinerU Flash text.
---

::: {.problem}
Let $f\colon S^4\to S^4$ be defined by
$$
f(x,y,z,w)=\frac{1}{\sqrt{x^4+y^4+z^4+w^4}}\,(x^2,y^2,z^2,w^2).
$$
Compute the degree of $f$.
:::

::: {.remark}
The source prints $S^4$, but the formula has four coordinates, so it defines a self-map of the unit sphere $S^3\subset\RR^4$.
:::

::: {.solution}

The printed formula has four coordinates, so it defines the map
$$
f:S^3\to S^3
$$
recorded in the remark on the card. Its degree is
$$
\boxed{0}.
$$

::: pf

::: {.pf-step #s1-1}

For every
$$
(x,y,z,w)\in S^3,
$$
all four coordinates of $f(x,y,z,w)$ are nonnegative.


::: pf-proof

The numerator is
$$
(x^2,y^2,z^2,w^2),
$$
whose coordinates are all nonnegative, and the normalizing denominator is positive.

:::

:::

::: {.pf-step #s1-2}

Hence
$$
\boxed{
f(S^3)
\subseteq
\{(u_1,u_2,u_3,u_4)\in S^3:u_i\ge0\text{ for all }i\}}.
$$


::: pf-proof

This is exactly step [](#s1-1){.pf-ref} written as a statement about the image.

:::

:::

::: {.pf-step #s1-3}

In particular,
$$
\boxed{
(-1,0,0,0)\notin f(S^3)}.
$$


::: pf-proof

The first coordinate of every image point is nonnegative by step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Therefore $f$ factors through
$$
S^3\setminus\{(-1,0,0,0)\}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} says the image avoids that point.

:::

:::

::: {.pf-step #s1-5}

The punctured sphere
$$
S^3\setminus\{(-1,0,0,0)\}
$$
is contractible.


::: pf-proof

Stereographic projection from the omitted point gives a homeomorphism
$$
S^3\setminus\{(-1,0,0,0)\}
\cong
\RR^3,
$$
and $\RR^3$ is contractible.

:::

:::

::: pf-step

Hence $f$ is null-homotopic as a map
$$
S^3\to S^3.
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, $f$ factors through the contractible space in step [](#s1-5){.pf-ref}. Any map factoring through a contractible space is null-homotopic.

:::

:::

::: {.pf-step #s1-7}

A null-homotopic self-map of $S^3$ induces the zero homomorphism on
$$
H_3(S^3;\ZZ)\cong\ZZ.
$$


::: pf-proof

Homotopic maps induce the same map on homology. A null-homotopic map is homotopic to a constant map, and a constant map induces the zero map in positive-dimensional reduced homology.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{\deg f=0}.
$$


::: pf-proof

By definition, the degree is the integer by which
$$
f_*:H_3(S^3;\ZZ)\to H_3(S^3;\ZZ)
$$
multiplies a fundamental class. Step [](#s1-7){.pf-ref} says this map is zero.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the requested degree for the self-map actually defined by the printed formula.

:::

:::

:::
