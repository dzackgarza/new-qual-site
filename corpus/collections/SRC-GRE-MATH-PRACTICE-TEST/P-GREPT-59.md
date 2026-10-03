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
<1>1. $1+\omega+\omega^2+\omega^3+\omega^4=0$.

::: {.proof}
Since $\omega=e^{2\pi i/5}$, one has $\omega^5=1$ and $\omega\neq 1$. Thus
\[
0=\omega^5-1=(\omega-1)(\omega^4+\omega^3+\omega^2+\omega+1).
\]
Because $\omega-1\neq 0$, the second factor must vanish.
:::

<1>2. $\omega^2+\omega+1+\omega^{-1}+\omega^{-2}=0$.

::: {.proof}
Divide the identity in step <1>1 by the nonzero number $\omega^2$.
:::

<1>3. $f(\omega+\omega^{-1})=\boxed{1}$.

::: {.proof}
Expanding and then applying step <1>2 gives
\[
\begin{aligned}
f(\omega+\omega^{-1})
&=(\omega+\omega^{-1})^2+(\omega+\omega^{-1})\\
&=\omega^2+2+\omega^{-2}+\omega+\omega^{-1}\\
&=(\omega^2+\omega+1+\omega^{-1}+\omega^{-2})+1\\
&=1.
\end{aligned}
\]
Hence the correct choice is (D).
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested value.
:::
:::
