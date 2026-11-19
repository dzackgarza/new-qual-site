---
schema: qual/card@1
id: P-WESCA06-I5
kind: problem
title: "State Cauchy's Integral Formula"
classification:
  areas: [complex-analysis]
  topics:
  - Cauchy Integral Formula
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Theorems and Definitions, item 5 (August 9, 2006) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read the item on 2026-11-19 in the retained scan
    assets/attachments/analysis_2003-2007.pdf, PDF p. 15: the Complex Analysis
    Preliminary Examination of August 9, 2006, Section 1 item 5. The page had cited
    only the extraction; it now names the examination, its item and the page of
    the scan. The statement is unchanged.

- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The proof ended with a pf-qed that only announced that earlier steps had answered
    the question, which STYLE-08 forbids; it is dropped, and the last step that carries
    content is now the QED step. No argument or statement changes.

---

::: {.problem}
State Cauchy's Integral Formula.
:::

::: {.solution}
The item is Section 1 item 5 of the Complex Analysis Preliminary Examination of August 9, 2006
(State Cauchy's Integral Formula), on the first page of that paper, PDF p. 15 of the retained scan
assets/attachments/analysis_2003-2007.pdf.


::: pf

::: {.pf-step #s1-1}

**Cauchy's Integral Formula.**

Let $f$ be holomorphic on a domain containing a positively oriented simple
closed contour
$$
\gamma
$$
and its interior. Let
$$
z_0
$$
lie inside $\gamma$. Then
$$
\boxed{
f(z_0)
=
\frac1{2\pi i}
\int_\gamma
\frac{f(\zeta)}
{\zeta-z_0}
\,d\zeta.
}
$$


::: pf-proof

Equivalently, if
$$
\overline{B(z_0,r)}
$$
lies in the domain of holomorphy of $f$, then
$$
f(z_0)
=
\frac1{2\pi i}
\int_{\abs{\zeta-z_0}=r}
\frac{f(\zeta)}
{\zeta-z_0}
\,d\zeta.
$$
This is the standard circle form of Cauchy's formula.

:::

:::

::: {.pf-step #s1-2}

More generally, for every integer
$$
m\ge0,
$$
$$
f^{(m)}(z_0)
=
\frac{m!}{2\pi i}
\int_\gamma
\frac{f(\zeta)}
{(\zeta-z_0)^{m+1}}
\,d\zeta.
$$


::: pf-proof

Differentiate the formula in step [](#s1-1){.pf-ref} under the integral sign.
This is Cauchy's integral formula for derivatives.

:::

:::


:::

:::
