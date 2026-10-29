---
schema: qual/card@1
id: P-GRECH2-30
kind: problem
title: Evaluate $\exp\int_3^5 dx/(x^2-3x+2)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 30 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Simplify the following:

$$
\exp \int_{3}^{5} \frac{dx}{x^2 - 3x + 2}
$$

[Note: Recall that $\exp x$ is a standard, alternate notation for $e^x$.]

(A) $\frac{3}{8}$
(B) $\frac{2}{3}$
(C) $\frac{4}{3}$
(D) $\frac{3}{2}$
(E) $\frac{5}{3}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $x\ne1,2$,
$$
\frac1{x^2-3x+2}=-\frac1{x-1}+\frac1{x-2}.
$$


::: pf-proof

Since
$$
x^2-3x+2=(x-1)(x-2),
$$
one has
$$
-\frac1{x-1}+\frac1{x-2}
=\frac{-(x-2)+(x-1)}{(x-1)(x-2)}
=\frac1{(x-1)(x-2)}.
$$

:::

:::

::: {.pf-step #s1-2}

The definite integral is
$$
\int_3^5\frac{dx}{x^2-3x+2}=\log\frac32.
$$


::: pf-proof

On $[3,5]$, both $x-1$ and $x-2$ are positive, so step [](#s1-1){.pf-ref} gives the antiderivative
$$
-\log(x-1)+\log(x-2)
=\log\frac{x-2}{x-1}.
$$
Therefore
$$
\begin{aligned}
\int_3^5\frac{dx}{x^2-3x+2}
&=\left[\log\frac{x-2}{x-1}\right]_3^5\\
&=\log\frac34-\log\frac12\\
&=\log\frac32.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

Hence
$$
\boxed{\exp\int_3^5\frac{dx}{x^2-3x+2}=\frac32},
$$
so the answer is (D).


::: pf-proof

By step [](#s1-2){.pf-ref} and the inverse relation between the exponential and logarithm functions,
$$
\exp\left(\log\frac32\right)=\frac32.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested simplification and corresponding choice.

:::

:::

:::
