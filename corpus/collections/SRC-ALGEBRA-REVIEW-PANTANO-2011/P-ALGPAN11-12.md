---
schema: qual/card@1
id: P-ALGPAN11-12
kind: problem
title: Which listed subsets of the reals are subrings
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the retained Pantano 2011 algebra-review source scan and verified from the stated algebraic criterion.
- event: source-checked
  by: claude-opus-5.5
  date: 2026-10-31
  note: Statement and choices transcribed from the ALGEBRA_REVIEW1.pdf page render; the machine extractions were garbled at this item.
---
::: {.problem}
Which of the following subsets are subrings of the ring of real numbers?

I. $\{a+b\sqrt2 \mid a\text{ and }b\text{ are rational}\}$

II. $\left\{\dfrac{n}{3^m} \st n\text{ is an integer and }m\text{ is a non-negative integer}\right\}$

III. $\{a+b\sqrt5 \mid a\text{ and }b\text{ are real numbers and }a^2+b^2\le1\}$

(A) I only (B) I and II only (C) I and III only (D) II and III only (E) I, II, and III
:::

::: {.solution}
Exactly I and II are subrings of $\RR$, choice (B).

::: pf

::: {.pf-step #s1}

I is a subring.

::: pf-proof

The set
$$
\QQ(\sqrt2)=\{a+b\sqrt2:a,b\in\QQ\}
$$
is closed under addition, additive inverses, and multiplication, and contains $1$; in fact it is a field.

:::

:::

::: {.pf-step #s2}

II is a subring.

::: pf-proof

The set
$$
\left\{\frac n{3^m}:n\in\ZZ,\ m\ge0\right\}=\ZZ[1/3]
$$
is closed under subtraction.
Also
$$
\frac n{3^m}\frac r{3^s}=\frac{nr}{3^{m+s}},
$$
so it is closed under multiplication and contains $1$.

:::

:::

::: {.pf-step #s3}

III is not a subring.

::: pf-proof

The element $1=1+0\sqrt5$ lies in III, but
$$
1+1=2
$$
does not, since its coefficients satisfy $2^2+0^2=4>1$.
Thus III is not closed under addition.

:::

:::

::: {.pf-step #s4}

Therefore exactly I and II are subrings of $\RR$.

::: pf-proof

Step [](#s1){.pf-ref} and step [](#s2){.pf-ref} prove that I and II are subrings, while step [](#s3){.pf-ref} rules out III.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives the requested classification.

:::

:::

:::
