---
schema: qual/card@1
id: P-GREPT-31
kind: problem
title: "Evaluate $\\int_0^\\infty e^{-x}/\\sqrt{x}\\,dx$ from the Gaussian integral"
classification:
  areas: [prelim]
  topics:
  - Gamma Function
  - Gaussian Integral
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 31 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Given that $\int_{0}^{\infty} e^{-x^2} \, dx = \frac{1}{2}\sqrt{\pi}$, what's the value of the following integral?

$$\int_{0}^{\infty} \frac{e^{-x}}{\sqrt{x}} \, dx$$

(A) $\frac{1}{4}\sqrt{\pi}$
(B) $\frac{1}{2}\sqrt{\pi}$
(C) $\sqrt{\pi}$
(D) $2\sqrt{\pi}$
(E) $\frac{1}{4}\pi$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Under the substitution
$$
x=u^2,
$$
the integral becomes
$$
\int_0^\infty\frac{e^{-x}}{\sqrt{x}}\,dx
=2\int_0^\infty e^{-u^2}\,du.
$$


::: pf-proof

For $u\ge0$, the substitution $x=u^2$ gives
$dx=2u\,du$ and $\sqrt{x}=u$. Therefore
$$
\frac{e^{-x}}{\sqrt{x}}\,dx
=\frac{e^{-u^2}}{u}(2u\,du)
=2e^{-u^2}\,du.
$$
The endpoints $x=0$ and $x\to\infty$ correspond to $u=0$ and
$u\to\infty$.

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\int_0^\infty\frac{e^{-x}}{\sqrt{x}}\,dx
=\boxed{\sqrt\pi},
$$
so the answer is (C).


::: pf-proof

Using the given Gaussian integral in step [](#s1-1){.pf-ref},
$$
2\int_0^\infty e^{-u^2}\,du
=2\left(\frac12\sqrt\pi\right)
=\sqrt\pi.
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the required value.

:::

:::

:::
