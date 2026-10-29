---
schema: qual/card@1
id: P-WESCA11-3
kind: problem
title: 'Conjugation preserves holomorphy in the reflected disk'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
If $f$ is holomorphic on the open unit disk, prove that
\[
g(z)=\overline{f(\overline z)}
\]
is holomorphic there as well.
:::

::: {.solution}

Let
\[
g(z)=\overline{f(\overline z)}
\]
for \(|z|<1\).

::: pf

::: pf-step

If
\[
|z|<1,
\]
then
\[
|\overline z|<1.
\]


::: pf-proof

Complex conjugation preserves modulus:
\[
|\overline z|=|z|.
\]
Thus \(f(\overline z)\) is defined on the whole unit disk.

:::

:::

::: pf-step

Fix
\[
z_0\in\DD
\]
and let
\[
h\ne0
\]
be sufficiently small.


::: pf-proof

Since the unit disk is open, \(z_0+h\in\DD\) for all sufficiently
small \(h\).

:::

:::

::: pf-step

The difference quotient is
\[
\frac{g(z_0+h)-g(z_0)}{h}
=
\frac{
\overline{
f(\overline{z_0}+\overline h)
-
f(\overline{z_0})
}
}{h}.
\]


::: pf-proof

Use
\[
\overline{z_0+h}
=
\overline{z_0}+\overline h
\]
and the definition of \(g\).

:::

:::

::: {.pf-step #s1-4}

Rewrite this quotient as
\[
\boxed{
\frac{g(z_0+h)-g(z_0)}{h}
=
\overline{
\frac{
f(\overline{z_0}+\overline h)-f(\overline{z_0})
}{
\overline h
}
}}.
\]


::: pf-proof

For \(h\ne0\),
\[
\overline{\frac{A}{\overline h}}
=
\frac{\overline A}{h},
\]
since
\[
\overline{\overline h}=h.
\]

:::

:::

::: {.pf-step #s1-5}

As
\[
h\to0,
\]
one has
\[
\overline h\to0.
\]


::: pf-proof

Again,
\[
|\overline h|=|h|.
\]

:::

:::

::: {.pf-step #s1-6}

Since \(f\) is holomorphic,
\[
\lim_{h\to0}
\frac{
f(\overline{z_0}+\overline h)-f(\overline{z_0})
}{
\overline h
}
=
f'(\overline{z_0}).
\]


::: pf-proof

Step [](#s1-5){.pf-ref} says the increment \(\overline h\) tends to \(0\), so this is the
ordinary complex derivative of \(f\) at \(\overline{z_0}\).

:::

:::

::: {.pf-step #s1-7}

Taking conjugates,
\[
\boxed{
g'(z_0)
=
\overline{f'(\overline{z_0})}}.
\]


::: pf-proof

Apply continuity of complex conjugation to the limit in step [](#s1-6){.pf-ref} and use
the difference quotient identity in step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Since \(z_0\in\DD\) was arbitrary,
\[
\boxed{
g\text{ is holomorphic on }\DD}.
\]


::: pf-proof

Step [](#s1-7){.pf-ref} proves existence of the complex derivative at every point of the
unit disk.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required conclusion.

:::

:::

:::
