---
schema: qual/card@1
id: P-GREPT-03
kind: problem
title: "Limit of $(\\sqrt{x+1}-1)/x$ at $0$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 3 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
$$\lim_{x \to 0} \frac{\sqrt{x + 1} - 1}{x} =$$

(A) $-\frac{1}{2}$
(B) $\frac{1}{2}$
(C) $1$
(D) $2$
(E) $\infty$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $x\ne0$,
$$
\frac{\sqrt{x+1}-1}{x}
=\frac1{\sqrt{x+1}+1}.
$$


::: pf-proof

Multiplying numerator and denominator by the conjugate $\sqrt{x+1}+1$ gives
$$
\frac{\sqrt{x+1}-1}{x}
\cdot
\frac{\sqrt{x+1}+1}{\sqrt{x+1}+1}
=\frac{(x+1)-1}{x(\sqrt{x+1}+1)}
=\frac1{\sqrt{x+1}+1}.
$$

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\lim_{x\to0}\frac{\sqrt{x+1}-1}{x}
=\boxed{\frac12},
$$
so the answer is (B).


::: pf-proof

By step [](#s1-1){.pf-ref}, the limit equals
$$
\lim_{x\to0}\frac1{\sqrt{x+1}+1}
=\frac1{1+1}=\frac12,
$$
because the simplified denominator is continuous at $x=0$ and nonzero there.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the required limit.

:::

:::

:::
