---
schema: qual/card@1
id: P-GREPT-02
kind: problem
title: "Derivative of $1/x-1/\\log x$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 2 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
$$\frac{d}{dx}\left(\frac{1}{x} - \frac{1}{\log x}\right) =$$

(A) $\frac{x - (\log x)^2}{(x \log x)^2}$
(B) $\frac{x^2 - 2 \log x}{2x^2 \log x}$
(C) $\frac{x - 1}{(x \log x)^2}$
(D) $\frac{2x - 1}{2x^2 \log x}$
(E) $\frac{2x - 1}{(x \log x)^2}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Differentiating the two terms gives
$$
\frac{d}{dx}\left(\frac1x-\frac1{\log x}\right)
=-\frac1{x^2}+\frac1{x(\log x)^2}.
$$


::: pf-proof

The derivative of $x^{-1}$ is $-x^{-2}$. Also,
$$
\frac{d}{dx}\bigl[-(\log x)^{-1}\bigr]
=(\log x)^{-2}\frac1x
$$
by the chain rule. Adding the two derivatives proves the claim.

:::

:::

::: {.pf-step #s1-2}

The derivative simplifies to
$$
\boxed{\frac{x-(\log x)^2}{(x\log x)^2}},
$$
so the answer is (A).


::: pf-proof

Using the common denominator $x^2(\log x)^2$ in step [](#s1-1){.pf-ref} gives
$$
-\frac1{x^2}+\frac1{x(\log x)^2}
=\frac{-(\log x)^2+x}{x^2(\log x)^2}
=\frac{x-(\log x)^2}{(x\log x)^2}.
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the required derivative.

:::

:::

:::
