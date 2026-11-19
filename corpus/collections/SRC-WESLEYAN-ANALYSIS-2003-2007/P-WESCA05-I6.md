---
schema: qual/card@1
id: P-WESCA05-I6
kind: problem
title: "Winding number of a circle about a distant point"
classification:
  areas: [complex-analysis]
  topics:
  - Winding Number
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1, item 6 (Summer 2005) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read the item on 2026-11-19 in the retained scan
    assets/attachments/analysis_2003-2007.pdf at PDF p. 25: the Complex Analysis Section of
    the Analysis Qualifier, Wesleyan University, Summer 2005, Section 1 item 6. The page had cited
    only the extraction; it now names the examination, its item and the page of the
    scan. The statement is unchanged.

- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The proof ended with a pf-qed that only announced that an earlier step had
    answered the question, which STYLE-08 forbids; it is dropped, and the step that
    carries the result is now the QED step. No argument or statement changes.

---

::: {.problem}
Find the winding number of
$$
\gamma(t)=4e^{it}+2i,\qquad 0\le t\le2\pi,
$$
about the point $10+10i$.
:::

::: {.solution}
The item is Section 1 item 6 of the Complex Analysis Section of the Analysis Qualifier, Wesleyan
University, Summer 2005 (winding number of 4e^{it}+2i about 10+10i), on PDF p. 25 of the retained scan
assets/attachments/analysis_2003-2007.pdf.


::: pf

::: pf-step

The curve $\gamma$ is the positively oriented circle of radius $4$ centered at $2i$.


::: pf-proof

The parametrization
$$
\gamma(t)=2i+4e^{it},
\qquad 0\le t\le2\pi,
$$
is the standard counterclockwise parametrization of that circle.

:::

:::

::: {.pf-step #s1-2}

The point $w=10+10i$ lies outside this circle.


::: pf-proof

Its distance from the center $2i$ is
$$
\abs{w-2i}
=\abs{10+8i}
=\sqrt{10^2+8^2}
=\sqrt{164}
>4.
$$

:::

:::

::: {.pf-step #s1-3}

The winding number is
$$
\boxed{\operatorname{Ind}(\gamma,10+10i)=0}.
$$


::: pf-proof

The function
$$
z\longmapsto\frac1{z-w}
$$
is holomorphic on and inside the circle because $w$ lies outside it by step [](#s1-2){.pf-ref}. By Cauchy's theorem,
$$
\int_\gamma\frac{dz}{z-w}=0.
$$
Hence
$$
\operatorname{Ind}(\gamma,w)
=\frac1{2\pi i}\int_\gamma\frac{dz}{z-w}
=0.
$$

:::

:::


:::

:::
