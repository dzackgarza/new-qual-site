---
schema: qual/card@1
id: P-CAEXAMPREP-11
kind: problem
title: A bounded region conformally equivalent to an unbounded region
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
Find a bijective conformal map that takes a bounded region of $\CC$ to an unbounded region.
:::

::: {.solution}

Let
$$
\DD=\{z:|z|<1\},
\qquad
H=\{w:\operatorname{Re}w>0\},
$$
and define
$$
F(z)=\frac{1+z}{1-z}.
$$

::: pf

::: {.pf-step #s1-1}

The map $F$ sends $\DD$ into $H$.


::: pf-proof

For $|z|<1$,
$$
\begin{aligned}
\operatorname{Re}F(z)
&=\frac12\left(\frac{1+z}{1-z}+\frac{1+\overline z}{1-\overline z}\right)\\
&=\frac{1-|z|^2}{|1-z|^2}>0.
\end{aligned}
$$
Thus $F(z)\in H$.

:::

:::

::: {.pf-step #s1-2}

The inverse formula
$$
F^{-1}(w)=\frac{w-1}{w+1}
$$
maps $H$ into $\DD$.


::: pf-proof

If $\operatorname{Re}w>0$, then
$$
|w+1|^2-|w-1|^2=4\operatorname{Re}w>0.
$$
Hence $|w-1|<|w+1|$, so
$$
\left|\frac{w-1}{w+1}\right|<1.
$$
Also $w+1\ne0$ in $H$, so the formula is well defined there.

:::

:::

::: {.pf-step #s1-3}

The map
$$
\boxed{F(z)=\frac{1+z}{1-z}}
$$
is a bijective conformal map from the bounded region $\DD$ onto the unbounded region $H$.


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} show that the displayed formulas for $F$ and $F^{-1}$ map between $\DD$ and $H$, and direct substitution shows they are mutual inverses. Moreover,
$$
F'(z)=\frac{2}{(1-z)^2}\ne0
$$
on $\DD$, so $F$ is conformal. The unit disc is bounded, whereas the right half-plane is unbounded.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} supplies the requested example.

:::

:::

:::
