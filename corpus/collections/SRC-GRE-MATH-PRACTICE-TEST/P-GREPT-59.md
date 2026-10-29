---
schema: qual/card@1
id: P-GREPT-59
kind: problem
title: "Evaluate $z^2+z$ at $z=\\omega+\\omega^{-1}$ for a primitive fifth root of unity"
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 59 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Let $\omega = e^{2\pi i/5}$ be a fifth root of $1$. What is the value of the function $f(z) = z^2 + z$ at $z = \omega + \omega^{-1}$?

(A) $-2$
(B) $-1$
(C) $0$
(D) $1$
(E) $2$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

$1+\omega+\omega^2+\omega^3+\omega^4=0$.


::: pf-proof

Since $\omega=e^{2\pi i/5}$, one has $\omega^5=1$ and $\omega\neq 1$. Thus
$$
0=\omega^5-1=(\omega-1)(\omega^4+\omega^3+\omega^2+\omega+1).
$$
Because $\omega-1\neq 0$, the second factor must vanish.

:::

:::

::: {.pf-step #s1-2}

$\omega^2+\omega+1+\omega^{-1}+\omega^{-2}=0$.


::: pf-proof

Divide the identity in step [](#s1-1){.pf-ref} by the nonzero number $\omega^2$.

:::

:::

::: {.pf-step #s1-3}

$f(\omega+\omega^{-1})=\boxed{1}$.


::: pf-proof

Expanding and then applying step [](#s1-2){.pf-ref} gives
$$
\begin{aligned}
f(\omega+\omega^{-1})
&=(\omega+\omega^{-1})^2+(\omega+\omega^{-1})\\
&=\omega^2+2+\omega^{-2}+\omega+\omega^{-1}\\
&=(\omega^2+\omega+1+\omega^{-1}+\omega^{-2})+1\\
&=1.
\end{aligned}
$$
Hence the correct choice is (D).

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value.

:::

:::

:::
