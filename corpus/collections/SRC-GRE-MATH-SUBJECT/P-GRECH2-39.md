---
schema: qual/card@1
id: P-GRECH2-39
kind: problem
title: Positive $a$ equating two integrals against $1/\sqrt{a^2-x^2}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 39 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Find the positive value of $a$ that satisfies the equation:

$$
\int_{0}^{a} \frac{dx}{\sqrt{a^2 - x^2}} = \int_{0}^{a} \frac{x \, dx}{\sqrt{a^2 - x^2}}
$$

(A) $\frac{2\sqrt{2}}{\pi}$
(B) $1$
(C) $\frac{\pi}{2\sqrt{2}}$
(D) $\sqrt{2}$
(E) $\frac{\pi}{2}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $a>0$,
$$
\int_0^a\frac{dx}{\sqrt{a^2-x^2}}=\frac{\pi}{2}.
$$


::: pf-proof

For $0<b<a$, set $x=a\sin\theta$. Since $a>0$, this gives
$$
\begin{aligned}
\int_0^b\frac{dx}{\sqrt{a^2-x^2}}
&=\int_0^{\arcsin(b/a)}
\frac{a\cos\theta\,d\theta}{a\cos\theta}\\
&=\arcsin(b/a).
\end{aligned}
$$
Taking $b\to a^-$ gives the claimed value $\arcsin(1)=\pi/2$.

:::

:::

::: {.pf-step #s1-2}

For every $a>0$,
$$
\int_0^a\frac{x\,dx}{\sqrt{a^2-x^2}}=a.
$$


::: pf-proof

For $0<b<a$,
$$
\begin{aligned}
\int_0^b\frac{x\,dx}{\sqrt{a^2-x^2}}
&=\left[-\sqrt{a^2-x^2}\right]_0^b\\
&=a-\sqrt{a^2-b^2},
\end{aligned}
$$
because $a>0$. Letting $b\to a^-$ gives the value $a$.

:::

:::

::: {.pf-step #s1-3}

The required positive value is
$$
\boxed{a=\frac{\pi}{2}},
$$
so the answer is (E).


::: pf-proof

By steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}, the displayed equation in the problem is equivalent to
$$
\frac{\pi}{2}=a.
$$
The resulting value is positive and therefore satisfies the stated requirement.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value and corresponding choice.

:::

:::

:::
