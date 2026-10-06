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

<1>1. If
\[
|z|<1,
\]
then
\[
|\overline z|<1.
\]

::: {.proof}
Complex conjugation preserves modulus:
\[
|\overline z|=|z|.
\]
Thus \(f(\overline z)\) is defined on the whole unit disk.
:::

<1>2. Fix
\[
z_0\in\mathbb D
\]
and let
\[
h\ne0
\]
be sufficiently small.

::: {.proof}
Since the unit disk is open, \(z_0+h\in\mathbb D\) for all sufficiently
small \(h\).
:::

<1>3. The difference quotient is
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

::: {.proof}
Use
\[
\overline{z_0+h}
=
\overline{z_0}+\overline h
\]
and the definition of \(g\).
:::

<1>4. Rewrite this quotient as
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

::: {.proof}
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

<1>5. As
\[
h\to0,
\]
one has
\[
\overline h\to0.
\]

::: {.proof}
Again,
\[
|\overline h|=|h|.
\]
:::

<1>6. Since \(f\) is holomorphic,
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

::: {.proof}
Step <1>5 says the increment \(\overline h\) tends to \(0\), so this is the
ordinary complex derivative of \(f\) at \(\overline{z_0}\).
:::

<1>7. Taking conjugates,
\[
\boxed{
g'(z_0)
=
\overline{f'(\overline{z_0})}}.
\]

::: {.proof}
Apply continuity of complex conjugation to the limit in step <1>6 and use
the difference quotient identity in step <1>4.
:::

<1>8. Since \(z_0\in\mathbb D\) was arbitrary,
\[
\boxed{
g\text{ is holomorphic on }\mathbb D}.
\]

::: {.proof}
Step <1>7 proves existence of the complex derivative at every point of the
unit disk.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the required conclusion.
:::
:::
