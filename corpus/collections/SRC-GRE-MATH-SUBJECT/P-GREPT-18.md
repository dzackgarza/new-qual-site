---
schema: qual/card@1
id: P-GREPT-18
kind: problem
title: "Limit of $(x+e^{3x})^{1/x}$ at $0$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 18 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
$\lim_{x \to 0} (x + e^{3x})^{1/x} =$

(A) $0$
(B) $1$
(C) $e^3$
(D) $1 + e^3$
(E) $e^4$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $x$ sufficiently close to $0$ with $x\ne0$, set
$$
y(x)=(x+e^{3x})^{1/x}.
$$
Then
$$
\log y(x)=\frac{\log(x+e^{3x})}{x}.
$$


::: pf-proof

Since $x+e^{3x}\to1$ as $x\to0$, the base is positive for all sufficiently
small $\abs{x}$. Taking the natural logarithm of the positive quantity $y(x)$
gives the displayed identity.

:::

:::

::: {.pf-step #s1-2}

One has
$$
\lim_{x\to0}\log y(x)=4.
$$


::: pf-proof

Both numerator and denominator in step [](#s1-1){.pf-ref} tend to $0$. By L'Hopital's rule,
$$
\lim_{x\to0}\frac{\log(x+e^{3x})}{x}
=\lim_{x\to0}\frac{1+3e^{3x}}{x+e^{3x}}
=\frac{1+3}{1}=4.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\lim_{x\to0}(x+e^{3x})^{1/x}=\boxed{e^4},
$$
so the answer is (E).


::: pf-proof

By step [](#s1-2){.pf-ref} and continuity of the exponential function,
$$
y(x)=\exp(\log y(x))\longrightarrow e^4.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required limit.

:::

:::

:::
