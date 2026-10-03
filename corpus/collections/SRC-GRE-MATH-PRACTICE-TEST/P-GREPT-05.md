---
schema: qual/card@1
id: P-GREPT-05
kind: problem
title: "Upper limits $a$ with $\\int_0^a(12x^2+8x+1)\\,dx=0$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 5 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR). The extraction prints the upper limit of integration as infinity; the question asks about values of a, and the book's Chapter 10 solution integrates from 0 to a."
---

::: {.problem}
For how many values of $a$ is the integral $\int_0^a (12x^2 + 8x + 1) \, dx$ equal to zero?

(A) $0$
(B) $1$
(C) $2$
(D) $3$
(E) $4$
:::

::: {.solution}
<1>1. The integral equals
$$
4a^3+4a^2+a.
$$

::: {.proof}
An antiderivative of $12x^2+8x+1$ is
$$
4x^3+4x^2+x.
$$
Therefore
$$
\int_0^a(12x^2+8x+1)\,dx
=\left[4x^3+4x^2+x\right]_0^a
=4a^3+4a^2+a.
$$
:::

<1>2. The integral vanishes exactly when
$$
a=0
\qquad\text{or}\qquad
a=-\frac12.
$$

::: {.proof}
By step <1>1,
$$
4a^3+4a^2+a
=a(4a^2+4a+1)
=a(2a+1)^2.
$$
This product is zero exactly for $a=0$ or $2a+1=0$, the latter giving
$a=-1/2$.
:::

<1>3. Hence the number of values of $a$ is
$$
\boxed{2},
$$
so the answer is (C).

::: {.proof}
Step <1>2 lists exactly two distinct values.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested count.
:::
:::
