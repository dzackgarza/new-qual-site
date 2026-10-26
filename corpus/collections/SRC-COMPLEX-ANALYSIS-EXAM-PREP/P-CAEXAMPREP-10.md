---
schema: qual/card@1
id: P-CAEXAMPREP-10
kind: problem
title: Real Möbius transformations preserving the upper half-plane
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against the deterministic MinerU Flash extraction assets/attachments/Complex_Analysis_Exam_Prep_Solutions_extracted.md.
---

::: {.problem}
Suppose $a,b,c,d\in\mathbb R$ and $ad>bc$.
Show that
\[
T(z)=\frac{az+b}{cz+d}
\]
sends the upper half-plane to itself.
:::

::: pf

::: pf-step

The denominator \(cz+d\) does not vanish at any point of the upper half-plane.


::: pf-proof

If \(c=0\), then \(ad>bc=0\), so \(d\ne0\). If \(c\ne0\), the unique zero of \(cz+d\) is \(-d/c\in\mathbb R\). Thus in either case \(cz+d\ne0\) whenever \(\operatorname{Im}z>0\).

:::

:::

::: pf-step

For every \(z\) in the upper half-plane,
\[
\operatorname{Im}T(z)
=\frac{(ad-bc)\operatorname{Im}z}{|cz+d|^2}.
\]


::: pf-proof

Since \(a,b,c,d\) are real,
\[
\begin{aligned}
T(z)-\overline{T(z)}
&=\frac{az+b}{cz+d}-\frac{a\overline z+b}{c\overline z+d}\\
&=\frac{(az+b)(c\overline z+d)-(a\overline z+b)(cz+d)}{|cz+d|^2}\\
&=\frac{(ad-bc)(z-\overline z)}{|cz+d|^2}.
\end{aligned}
\]
Dividing by \(2i\) gives the stated formula for the imaginary part.

:::

:::

::: pf-step

One has
\[
\boxed{T(\{\operatorname{Im}z>0\})\subseteq\{\operatorname{Im}w>0\}}.
\]


::: pf-proof

If \(\operatorname{Im}z>0\), then step <1>1 makes the denominator in step <1>2 strictly positive. The hypothesis \(ad>bc\) says \(ad-bc>0\). Hence step <1>2 gives \(\operatorname{Im}T(z)>0\), as required.

:::

:::

::: pf-qed

Step <1>3 is the required invariance statement.

:::

:::
