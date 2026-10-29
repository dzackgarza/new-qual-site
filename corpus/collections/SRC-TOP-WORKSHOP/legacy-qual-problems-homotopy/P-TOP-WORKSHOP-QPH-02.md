---
schema: qual/card@1
id: P-TOP-WORKSHOP-QPH-02
kind: problem
title: The boundary torus is not a retract of the solid torus
classification:
  areas: [topology]
  topics: [Retractions, Fundamental Group]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2, labeled Michigan Jan 2010, in assets/attachments/QualProblemsHomotopy_extracted.md.
---

::: {.problem}
Let $D^2$ be the closed $2$-disk and $S^1=\partial D^2$.
Is
$$
X=S^1\times S^1
$$
a retract of
$$
Y=D^2\times S^1?
$$
That is, does there exist a continuous map $r:Y\to X$ whose restriction to $X\subset Y$ is the identity?
:::

::: {.solution}

Let
$$
i:X=S^1\times S^1\hookrightarrow Y=D^2\times S^1
$$
be the inclusion.

::: pf

::: pf-step

One has
$$
\boxed{
\pi_1(X)\cong\ZZ\oplus\ZZ}.
$$


::: pf-proof

The fundamental group of a product is the product of the fundamental groups:
$$
\pi_1(S^1\times S^1)
\cong
\pi_1(S^1)\times\pi_1(S^1)
\cong
\ZZ\oplus\ZZ.
$$

:::

:::

::: pf-step

One has
$$
\boxed{
\pi_1(Y)\cong\ZZ}.
$$


::: pf-proof

The disk $D^2$ is contractible, so
$$
D^2\times S^1
\simeq
S^1.
$$
Hence its fundamental group is $\ZZ$.

:::

:::

::: pf-step

Let
$$
m(t)=(e^{2\pi it},1)
$$
be the meridian loop in $X$.


::: pf-proof

This loop travels once around the boundary circle of the disk factor while remaining fixed in the second $S^1$-factor.

:::

:::

::: {.pf-step #s1-4}

The class
$$
[m]
$$
is nontrivial in $\pi_1(X)$.


::: pf-proof

Under the identification
$$
\pi_1(X)\cong\ZZ\oplus\ZZ,
$$
the loop $m$ represents
$$
(1,0)\ne(0,0).
$$

:::

:::

::: {.pf-step #s1-5}

The same loop becomes nullhomotopic in $Y$.


::: pf-proof

Inside
$$
D^2\times S^1,
$$
the loop
$$
t\longmapsto(e^{2\pi it},1)
$$
bounds the disk
$$
D^2\times\{1\}.
$$
Thus its image under the inclusion is nullhomotopic.

:::

:::

::: pf-step

Hence the induced map
$$
i_*:\pi_1(X)\to\pi_1(Y)
$$
has nontrivial kernel.


::: pf-proof

The nontrivial class $[m]$ from step [](#s1-4){.pf-ref} is sent to the identity by step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{i_*\text{ is not injective}}.
$$


::: pf-proof

A homomorphism with nontrivial kernel cannot be injective.

:::

:::

::: pf-step

Since $r$ is a retraction,
$$
\boxed{
r\circ i=\operatorname{id}_X}.
$$


::: pf-proof

A retraction restricts to the identity on the subspace onto which it retracts.

:::

:::

::: pf-step

Passing to fundamental groups,
$$
\boxed{
r_*\circ i_*=\operatorname{id}_{\pi_1(X)}}.
$$


::: pf-proof

Fundamental groups are functorial under composition.

:::

:::

::: {.pf-step #s1-10}

The existence of a left inverse $r_*$ forces $i_*$ to be injective.


::: pf-proof

If
$$
i_*(\gamma)=1,
$$
then
$$
\gamma
=
(r_*\circ i_*)(\gamma)
=
r_*(1)
=
1.
$$
Hence the kernel of $i_*$ is trivial.

:::

:::

::: {.pf-step #s1-11}

This contradicts step [](#s1-7){.pf-ref}.


::: pf-proof

Step [](#s1-7){.pf-ref} says $i_*$ is not injective, while step [](#s1-10){.pf-ref} says a retraction would make it injective.

:::

:::

::: {.pf-step #s1-12}

Therefore
$$
\boxed{
S^1\times S^1
\text{ is not a retract of }
D^2\times S^1}.
$$


::: pf-proof

The assumption of a retraction led to the contradiction in step [](#s1-11){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-12){.pf-ref} answers the question.

:::

:::

:::
