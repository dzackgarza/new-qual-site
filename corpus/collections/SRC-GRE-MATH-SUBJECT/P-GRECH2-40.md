---
schema: qual/card@1
id: P-GRECH2-40
kind: problem
title: Convergence of three improper integrals
classification:
  areas: [prelim]
  topics:
  - Improper Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 40 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Which of the following improper integrals converge?

I. $\int_{-\infty}^{\infty} \frac{dx}{(x^2 + 1)^2}$

II. $\int_{1}^{\infty} x e^{-x} dx$

III. $\int_{0}^{2} \frac{dx}{(2 - x)^2}$

(A) I only
(B) I and II only
(C) II only
(D) I and III only
(E) II and III only
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Integral I converges.


::: pf-proof

The integrand is continuous on every bounded interval. For $\abs{x}\ge1$,
$$
0<\frac1{(x^2+1)^2}\le\frac1{x^4}.
$$
Since
$$
\int_1^\infty \frac{dx}{x^4}<\infty
\qquad\text{and}\qquad
\int_{-\infty}^{-1}\frac{dx}{x^4}<\infty,
$$
the comparison test shows that both tails of integral I converge. Hence
$\int_{-\infty}^{\infty}dx/(x^2+1)^2$ converges.

:::

:::

::: {.pf-step #s1-2}

Integral II converges.


::: pf-proof

Integration by parts gives
$$
\int xe^{-x}\,dx=-(x+1)e^{-x}.
$$
Thus
$$
\begin{aligned}
\int_1^\infty xe^{-x}\,dx
&=\lim_{b\to\infty}
\left[-(x+1)e^{-x}\right]_1^b\\
&=\lim_{b\to\infty}
\left(\frac2e-(b+1)e^{-b}\right)\\
&=\frac2e,
\end{aligned}
$$
because $(b+1)e^{-b}\to0$.

:::

:::

::: {.pf-step #s1-3}

Integral III diverges.


::: pf-proof

For $0<b<2$,
$$
\int_0^b\frac{dx}{(2-x)^2}
=\left[\frac1{2-x}\right]_0^b
=\frac1{2-b}-\frac12.
$$
As $b\to2^-$, the right-hand side tends to $+\infty$. Hence integral III diverges.

:::

:::

::: {.pf-step #s1-4}

Exactly I and II converge, so the answer is
$$
\boxed{\text{(B) I and II only}}.
$$


::: pf-proof

This follows directly from steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested choice.

:::

:::

:::
