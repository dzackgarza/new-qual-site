---
schema: qual/card@1
id: P-GRECH7-30
kind: problem
title: Polar form of $(i-\sqrt3)^6$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 30 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. Choice (D) is partly garbled in both extractions.
---

::: {.problem}
What is the polar form of a complex number equal to $(i - \sqrt{3})^6$?

(A) $-2^6$
(B) $2^6(-1 + i)$
(C) $2^6(1 - i)$
(D) $2^6\left(\frac{1}{2} - \sqrt{\frac{3}{2}}\,i\right)$
(E) $2^6$
:::

::: {.remark}
The source prints a stray empty "$2^6(\ )$" after choice (D).
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The complex number $i-\sqrt3$ has modulus $2$ and argument $5\pi/6$.


::: pf-proof

Its real and imaginary parts are $-\sqrt3$ and $1$, so its modulus is
$$
\sqrt{(-\sqrt3)^2+1^2}=2.
$$
It lies in the second quadrant, and
$$
\tan\theta=\frac{1}{-\sqrt3}=-\frac1{\sqrt3},
$$
so the principal argument is $\theta=5\pi/6$. Thus
$$
i-\sqrt3=2e^{5\pi i/6}.
$$

:::

:::

::: {.pf-step #s1-2}

Its sixth power is
$$
(i-\sqrt3)^6=2^6e^{5\pi i}.
$$


::: pf-proof

Apply De Moivre's formula to the polar form in step [](#s1-1){.pf-ref}:
$$
\left(2e^{5\pi i/6}\right)^6
=2^6e^{5\pi i}.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
(i-\sqrt3)^6
=2^6(\cos5\pi+i\sin5\pi)
=\boxed{-2^6},
$$
so the answer is (A).


::: pf-proof

Since $\cos5\pi=-1$ and $\sin5\pi=0$, the expression from step [](#s1-2){.pf-ref} is the negative real number $-2^6$. Equivalently, its polar form may be written $2^6e^{i\pi}$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value in polar form and the matching choice.

:::

:::

:::
