---
schema: qual/card@1
id: P-GREPT-17
kind: problem
title: "Evaluate $1+\\cot^2(\\arcsin\\frac{\\pi}{4})$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 17 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
$1 + \cot^2 \left(\arcsin \frac{\pi}{4}\right) =$

(A) $\frac{3}{2} \pi$
(B) $2\pi$
(C) $3\pi$
(D) $5\pi$
(E) $\frac{16}{\pi^2}$
:::

::: {.solution}
<1>1. Let
$$
\theta=\arcsin\frac\pi4.
$$
Then
$$
\sin\theta=\frac\pi4.
$$

::: {.proof}
This is the defining property of the inverse sine. Since
$0<\pi/4<1$, the expression is well-defined.
:::

<1>2. One has
$$
1+\cot^2\theta=\csc^2\theta.
$$

::: {.proof}
This is the Pythagorean identity relating cotangent and cosecant.
:::

<1>3. Therefore
$$
1+\cot^2\left(\arcsin\frac\pi4\right)
=\boxed{\frac{16}{\pi^2}},
$$
so the answer is (E).

::: {.proof}
By steps <1>1--<1>2,
$$
1+\cot^2\theta
=\csc^2\theta
=\frac1{\sin^2\theta}
=\frac1{(\pi/4)^2}
=\frac{16}{\pi^2}.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested value.
:::
:::
