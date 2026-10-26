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
\[
X=S^1\times S^1
\]
a retract of
\[
Y=D^2\times S^1?
\]
That is, does there exist a continuous map $r:Y\to X$ whose restriction to $X\subset Y$ is the identity?
:::

Let
\[
i:X=S^1\times S^1\hookrightarrow Y=D^2\times S^1
\]
be the inclusion.

::: pf

::: pf-step

One has
\[
\boxed{
\pi_1(X)\cong\mathbb Z\oplus\mathbb Z}.
\]


::: pf-proof

The fundamental group of a product is the product of the fundamental groups:
\[
\pi_1(S^1\times S^1)
\cong
\pi_1(S^1)\times\pi_1(S^1)
\cong
\mathbb Z\oplus\mathbb Z.
\]

:::

:::

::: pf-step

One has
\[
\boxed{
\pi_1(Y)\cong\mathbb Z}.
\]


::: pf-proof

The disk \(D^2\) is contractible, so
\[
D^2\times S^1
\simeq
S^1.
\]
Hence its fundamental group is \(\mathbb Z\).

:::

:::

::: pf-step

Let
\[
m(t)=(e^{2\pi it},1)
\]
be the meridian loop in \(X\).


::: pf-proof

This loop travels once around the boundary circle of the disk factor while remaining fixed in the second \(S^1\)-factor.

:::

:::

::: pf-step

The class
\[
[m]
\]
is nontrivial in \(\pi_1(X)\).


::: pf-proof

Under the identification
\[
\pi_1(X)\cong\mathbb Z\oplus\mathbb Z,
\]
the loop \(m\) represents
\[
(1,0)\ne(0,0).
\]

:::

:::

::: pf-step

The same loop becomes nullhomotopic in \(Y\).


::: pf-proof

Inside
\[
D^2\times S^1,
\]
the loop
\[
t\longmapsto(e^{2\pi it},1)
\]
bounds the disk
\[
D^2\times\{1\}.
\]
Thus its image under the inclusion is nullhomotopic.

:::

:::

::: pf-step

Hence the induced map
\[
i_*:\pi_1(X)\to\pi_1(Y)
\]
has nontrivial kernel.


::: pf-proof

The nontrivial class \([m]\) from step <1>4 is sent to the identity by step <1>5.

:::

:::

::: pf-step

Therefore
\[
\boxed{i_*\text{ is not injective}}.
\]


::: pf-proof

A homomorphism with nontrivial kernel cannot be injective.

:::

:::

::: pf-step

Since \(r\) is a retraction,
\[
\boxed{
r\circ i=\operatorname{id}_X}.
\]


::: pf-proof

A retraction restricts to the identity on the subspace onto which it retracts.

:::

:::

::: pf-step

Passing to fundamental groups,
\[
\boxed{
r_*\circ i_*=\operatorname{id}_{\pi_1(X)}}.
\]


::: pf-proof

Fundamental groups are functorial under composition.

:::

:::

::: pf-step

The existence of a left inverse \(r_*\) forces \(i_*\) to be injective.


::: pf-proof

If
\[
i_*(\gamma)=1,
\]
then
\[
\gamma
=
(r_*\circ i_*)(\gamma)
=
r_*(1)
=
1.
\]
Hence the kernel of \(i_*\) is trivial.

:::

:::

::: pf-step

This contradicts step <1>7.


::: pf-proof

Step <1>7 says \(i_*\) is not injective, while step <1>10 says a retraction would make it injective.

:::

:::

::: pf-step

Therefore
\[
\boxed{
S^1\times S^1
\text{ is not a retract of }
D^2\times S^1}.
\]


::: pf-proof

The assumption of a retraction led to the contradiction in step <1>11.

:::

:::

::: pf-qed

Step <1>12 answers the question.

:::

:::
