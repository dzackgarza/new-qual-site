---
schema: qual/card@1
id: P-BKF13-9B
kind: problem
title: Number of irreducible sextics over $\mathbb F_3$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2013 solution packet: counting
    degree-six elements in the field of order 3^6 and dividing by Frobenius
    orbit size gives 116 monic irreducibles and 232 irreducibles in all.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the proper-subfield inclusion-exclusion, the six conjugates of
    every degree-six element, and the final factor from nonzero leading
    coefficients.
---

::: {.problem}
How many irreducible polynomials of degree exactly 6 are there over the finite field with 3 elements?
:::

::: {.solution}
Work inside $\FF_{3^6}$.

::: pf

::: {.pf-step #s1}

Exactly
$$
3^6-3^3-3^2+3=696
$$
elements of $\FF_{3^6}$ have degree exactly $6$ over $\FF_3$.

::: pf-proof

For an element $\alpha\in\FF_{3^6}$, the degree
$[\FF_3(\alpha):\FF_3]$ divides $6$. Hence an element whose degree is
less than $6$ has degree $1$, $2$, or $3$, and therefore lies in
$\FF_{3^2}$ or $\FF_{3^3}$. Conversely every element of either of these
proper subfields has degree less than $6$.

The two subfields satisfy
$$
\FF_{3^2}\cap\FF_{3^3}=\FF_3,
$$
because the degree of their intersection over $\FF_3$ divides both $2$
and $3$. Thus the number of elements lying in a proper subfield is
$$
3^2+3^3-3=9+27-3=33.
$$
Subtracting from $|\FF_{3^6}|=3^6=729$ gives
$$
729-33=696.
$$

:::

:::

::: {.pf-step #s2}

There are exactly
$$
\frac{696}{6}=116
$$
monic irreducible polynomials of degree $6$ over $\FF_3$.

::: pf-proof

Every element $\alpha$ counted in step [](#s1){.pf-ref} has a monic irreducible
minimal polynomial of degree $6$ over $\FF_3$. Such a polynomial has
six distinct roots in $\FF_{3^6}$,
$$
\alpha,\alpha^3,\alpha^{3^2},\ldots,\alpha^{3^5},
$$
and all six have the same minimal polynomial. Conversely every root of
a monic irreducible sextic has degree $6$ over $\FF_3$. Thus the $696$
degree-six elements are partitioned into sets of six roots, one set for
each monic irreducible sextic. Hence there are $696/6=116$ such monic
polynomials.

:::

:::

::: {.pf-step #s3}

The number of irreducible polynomials of degree exactly $6$ over
$\FF_3$ is
$$
\boxed{232}.
$$

::: pf-proof

Every irreducible polynomial is a unique nonzero scalar multiple of a
monic irreducible polynomial. Since $\FF_3^\times$ has two elements,
each of the $116$ monic irreducible sextics from step [](#s2){.pf-ref} has exactly
two nonzero scalar multiples. Therefore the total number is
$$
2\cdot116=232.
$$

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} gives the requested number.

:::

:::

:::
