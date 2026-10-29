---
schema: qual/card@1
id: P-GREPT-29
kind: problem
title: "Evaluate $\\int_0^1 x\\log x\\,dx$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 29 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
$\int_0^1 (x \log x) \, dx =$

(A) $-1$
(B) $-\frac{1}{2}$
(C) $-\frac{1}{4}$
(D) $1$
(E) does not exist
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $0<\varepsilon<1$,
$$
\int_\varepsilon^1x\log x\,dx
=\left[\frac12x^2\log x-\frac14x^2\right]_\varepsilon^1.
$$


::: pf-proof

Integration by parts with $u=\log x$ and $dv=x\,dx$ gives
$$
\int x\log x\,dx
=\frac12x^2\log x-\frac12\int x\,dx
=\frac12x^2\log x-\frac14x^2.
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
\lim_{x\to0^+}x^2\log x=0.
$$


::: pf-proof

Rewrite the expression as
$$
\frac{\log x}{x^{-2}}.
$$
As $x\to0^+$ this is of type $-\infty/\infty$, so L'Hopital's rule gives
$$
\lim_{x\to0^+}\frac{\log x}{x^{-2}}
=\lim_{x\to0^+}\frac{x^{-1}}{-2x^{-3}}
=\lim_{x\to0^+}-\frac{x^2}{2}=0.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\int_0^1x\log x\,dx=\boxed{-\frac14},
$$
so the answer is (C).


::: pf-proof

By the definition of the improper integral and steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref},
$$
\begin{aligned}
\int_0^1x\log x\,dx
&=\lim_{\varepsilon\to0^+}
\left[\frac12x^2\log x-\frac14x^2\right]_\varepsilon^1\\
&=-\frac14.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required integral.

:::

:::

:::
