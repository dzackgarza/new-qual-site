---
schema: qual/card@1
id: P-GREPT-36
kind: problem
title: "Value $f(8)$ from $f(2n)=n^2+f(2(n-1))$ and $f(0)=0$"
classification:
  areas: [prelim]
  topics:
  - Recurrences
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 36 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Let $f(x)$ be a function whose graph passes through the origin. If $f(2n) = n^2 + f[2(n - 1)]$ for every integer $n$, what is the value of $f(8)$?

(A) $24$
(B) $30$
(C) $32$
(D) $36$
(E) Cannot be determined from the information given
:::

::: {.solution}

::: pf

::: pf-step

The condition that the graph passes through the origin gives
$$
f(0)=0.
$$


::: pf-proof

The origin is the point $(0,0)$, so membership of this point in the graph of
$f$ means exactly that $f(0)=0$.

:::

:::

::: {.pf-step #s1-2}

Successive use of the recursion gives
$$
f(2)=1,
\qquad
f(4)=5,
\qquad
f(6)=14.
$$


::: pf-proof

For $n=1,2,3$ respectively,
$$
\begin{aligned}
f(2)&=1^2+f(0)=1,\\
f(4)&=2^2+f(2)=4+1=5,\\
f(6)&=3^2+f(4)=9+5=14.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
f(8)=\boxed{30},
$$
so the answer is (B).


::: pf-proof

Applying the recursion with $n=4$ and using step [](#s1-2){.pf-ref} gives
$$
f(8)=4^2+f(6)=16+14=30.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value.

:::

:::

:::
