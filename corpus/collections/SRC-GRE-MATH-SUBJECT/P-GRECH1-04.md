---
schema: qual/card@1
id: P-GRECH1-04
kind: problem
title: Second iterate of a nonlinear recurrence
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 1 review Question 4 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription.
---

::: {.problem}
Let $f$ be a function such that $f(n+1) = 1 - [f(n)]^2$ for all nonnegative integers $n$. Which of the following correctly expresses $f(n+2)$ in terms of $f(n)$?

(A) $2[f(n)]^2$
(B) $2f(n) - 2[f(n)]^2$
(C) $2f(n) + 2[f(n)]^2$
(D) $2[f(n)]^2 - [f(n)]^4$
(E) $2[f(n)]^2 + [f(n)]^4$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Applying the recurrence at $n+1$ gives
$$
f(n+2)=1-[f(n+1)]^2.
$$


::: pf-proof

Since $n$ is nonnegative, so is $n+1$, and the given recurrence therefore applies with $n+1$ in place of $n$.

:::

:::

::: {.pf-step #s1-2}

Substituting the recurrence for $f(n+1)$ gives
$$
f(n+2)=\boxed{2[f(n)]^2-[f(n)]^4},
$$
so the answer is (D).


::: pf-proof

By step [](#s1-1){.pf-ref} and the given recurrence,
$$
\begin{aligned}
f(n+2)
&=1-\left(1-[f(n)]^2\right)^2\\
&=1-\left(1-2[f(n)]^2+[f(n)]^4\right)\\
&=2[f(n)]^2-[f(n)]^4.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the requested expression and identifies the corresponding choice.

:::

:::

:::
