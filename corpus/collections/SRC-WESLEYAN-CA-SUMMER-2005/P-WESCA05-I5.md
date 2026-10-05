---
schema: qual/card@1
id: P-WESCA05-I5
kind: problem
title: "Differentiate a tenth power involving an exponential"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1, item 5 (Summer 2005) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Calculate $h'(z)$ for
\[
h(z)=\left(\frac{z^2-1}{e^z}\right)^{10}.
\]
:::

::: {.solution}
<1>1. Rewrite
\[
h(z)=(z^2-1)^{10}e^{-10z}.
\]

::: {.proof}
Since
\[
\left(\frac{z^2-1}{e^z}\right)^{10}
=(z^2-1)^{10}e^{-10z},
\]
the displayed expression is algebraically identical to the given function.
:::

<1>2. Differentiating by the product and chain rules gives
\[
h'(z)
=
20z(z^2-1)^9e^{-10z}
-10(z^2-1)^{10}e^{-10z}.
\]

::: {.proof}
One has
\[
\frac{d}{dz}(z^2-1)^{10}
=
10(z^2-1)^9(2z)
=
20z(z^2-1)^9,
\]
and
\[
\frac{d}{dz}e^{-10z}=-10e^{-10z}.
\]
Apply the product rule to the expression in step <1>1.
:::

<1>3. Therefore
\[
\boxed{
h'(z)
=
10e^{-10z}(z^2-1)^9(-z^2+2z+1).}
\]

::: {.proof}
Factor the expression from step <1>2:
\[
\begin{aligned}
h'(z)
&=
10e^{-10z}(z^2-1)^9
\bigl(2z-(z^2-1)\bigr)\\
&=
10e^{-10z}(z^2-1)^9(-z^2+2z+1).
\end{aligned}
\]
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested derivative.
:::
:::
