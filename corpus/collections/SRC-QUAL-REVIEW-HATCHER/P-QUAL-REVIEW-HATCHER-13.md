---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-13
kind: problem
title: The figure-eight is not a retract of the torus
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against practice problem 13 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md.
---

::: {.problem}
Prove that
\[
S^1\vee S^1
\]
is not a retract of
\[
S^1\times S^1.
\]
:::

::: {.solution}

Let
\[
A=S^1\vee S^1
\]
and
\[
X=S^1\times S^1.
\]

Suppose, toward a contradiction, that \(A\) is a retract of \(X\). Let
\[
i:A\hookrightarrow X
\]
be the inclusion and
\[
r:X\to A
\]
a retraction.

::: pf

::: pf-step

Since \(r\) is a retraction,
\[
\boxed{
r\circ i=\operatorname{id}_A}.
\]


::: pf-proof

A retraction restricts to the identity on the retract.

:::

:::

::: pf-step

Passing to fundamental groups,
\[
\boxed{
r_*\circ i_*=\operatorname{id}_{\pi_1(A)}}.
\]


::: pf-proof

Fundamental group is functorial with respect to composition.

:::

:::

::: {.pf-step #s1-3}

Therefore
\[
\boxed{
i_*:\pi_1(A)\to\pi_1(X)
\text{ is injective}}.
\]


::: pf-proof

If
\[
i_*(g)=1,
\]
then
\[
g
=
(r_*\circ i_*)(g)
=
r_*(1)
=
1.
\]
Thus the kernel is trivial.

:::

:::

::: {.pf-step #s1-4}

One has
\[
\boxed{
\pi_1(A)\cong F_2},
\]
the free group on two generators.


::: pf-proof

The fundamental group of a wedge of two circles is the free product
\[
\ZZ*\ZZ
\cong
F_2.
\]

:::

:::

::: {.pf-step #s1-5}

One has
\[
\boxed{
\pi_1(X)
\cong
\ZZ^2}.
\]


::: pf-proof

For the torus,
\[
\pi_1(S^1\times S^1)
\cong
\pi_1(S^1)\times\pi_1(S^1)
\cong
\ZZ^2.
\]

:::

:::

::: {.pf-step #s1-6}

Every subgroup of \(\ZZ^2\) is abelian.


::: pf-proof

Every subgroup of an abelian group is abelian.

:::

:::

::: {.pf-step #s1-7}

The group \(F_2\) is nonabelian.


::: pf-proof

If \(a,b\) are its free generators, then the reduced words
\[
ab
\qquad\text{and}\qquad
ba
\]
are distinct. Hence
\[
ab\ne ba.
\]

:::

:::

::: {.pf-step #s1-8}

Therefore there is no injective homomorphism
\[
F_2\hookrightarrow\ZZ^2.
\]


::: pf-proof

The image of such an injection would be a subgroup of \(\ZZ^2\), hence abelian by step [](#s1-6){.pf-ref}. Then \(F_2\) itself would be abelian, contradicting step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

This contradicts the injectivity of \(i_*\) from step [](#s1-3){.pf-ref}.


::: pf-proof

Combine steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} with step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

Hence
\[
\boxed{
S^1\vee S^1
\text{ is not a retract of }
S^1\times S^1}.
\]


::: pf-proof

The assumption of a retraction led to the contradiction in step [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required conclusion.

:::

:::

:::
