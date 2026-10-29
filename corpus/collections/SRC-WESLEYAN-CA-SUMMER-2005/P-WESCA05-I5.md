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
$$
h(z)=\left(\frac{z^2-1}{e^z}\right)^{10}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Rewrite
$$
h(z)=(z^2-1)^{10}e^{-10z}.
$$


::: pf-proof

Since
$$
\left(\frac{z^2-1}{e^z}\right)^{10}
=(z^2-1)^{10}e^{-10z},
$$
the displayed expression is algebraically identical to the given function.

:::

:::

::: {.pf-step #s1-2}

Differentiating by the product and chain rules gives
$$
h'(z)
=
20z(z^2-1)^9e^{-10z}
-10(z^2-1)^{10}e^{-10z}.
$$


::: pf-proof

One has
$$
\frac{d}{dz}(z^2-1)^{10}
=
10(z^2-1)^9(2z)
=
20z(z^2-1)^9,
$$
and
$$
\frac{d}{dz}e^{-10z}=-10e^{-10z}.
$$
Apply the product rule to the expression in step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
h'(z)
=
10e^{-10z}(z^2-1)^9(-z^2+2z+1).}
$$


::: pf-proof

Factor the expression from step [](#s1-2){.pf-ref}:
$$
\begin{aligned}
h'(z)
&=
10e^{-10z}(z^2-1)^9
\bigl(2z-(z^2-1)\bigr)\\
&=
10e^{-10z}(z^2-1)^9(-z^2+2z+1).
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested derivative.

:::

:::

:::
