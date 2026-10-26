---
schema: qual/card@1
id: P-GREPT-25
kind: problem
title: "Evaluate $\\int_{-1/2}^{1/2}dx/(1-x^2)$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 25 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
$\int_{-1/2}^{1/2} \frac{dx}{1 - x^2} =$

(A) $\log 2$
(B) $\log 3$
(C) $3 \log 2$
(D) $2 \log 3$
(E) $3 \log 3$
:::

::: pf

::: pf-step

On $[-1/2,1/2]$,
$$
\frac1{1-x^2}
=\frac12\left(\frac1{1+x}+\frac1{1-x}\right).
$$


::: pf-proof

Combining the two fractions on the right gives
$$
\frac12\frac{(1-x)+(1+x)}{(1+x)(1-x)}
=\frac1{1-x^2}.
$$

:::

:::

::: pf-step

An antiderivative on this interval is
$$
\frac12\log\frac{1+x}{1-x}.
$$


::: pf-proof

Integrating the decomposition from step <1>1 gives
$$
\frac12\log(1+x)-\frac12\log(1-x)
=\frac12\log\frac{1+x}{1-x}.
$$
Both $1+x$ and $1-x$ are positive on the interval.

:::

:::

::: pf-step

Therefore
$$
\int_{-1/2}^{1/2}\frac{dx}{1-x^2}
=\boxed{\log3},
$$
so the answer is (B).


::: pf-proof

By step <1>2,
$$
\begin{aligned}
\int_{-1/2}^{1/2}\frac{dx}{1-x^2}
&=\frac12\left[
\log\frac{1+x}{1-x}
\right]_{-1/2}^{1/2}\\
&=\frac12\left(\log3-\log\frac13\right)
=\log3.
\end{aligned}
$$

:::

:::

::: pf-qed

Step <1>3 gives the required integral.

:::

:::
