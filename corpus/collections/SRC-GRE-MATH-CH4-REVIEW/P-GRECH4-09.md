---
schema: qual/card@1
id: P-GRECH4-09
kind: problem
title: General solution of a third-order forced ODE
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 4 review Question 9 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch4-review/, replacing the earlier chapter-4.pdf transcription.
---

::: {.problem}
What is the general solution of the differential equation

$$
2\frac{d^3x}{dt^3} + 7\frac{d^2x}{dt^2} + 3\frac{dx}{dt} = 6?
$$

(A) $x = 2t + c_1e^t + c_2e^{-t/2} + c_3e^{-3t}$
(B) $x = 2 + c_1e^t + c_2e^{-t/2} + c_3e^{-3t}$
(C) $x = t^2 + c_1 + c_2e^{-t/3} + c_3e^{-2t}$
(D) $x = 2t + c_1 + c_2e^{-t/3} + c_3e^{-2t}$
(E) $x = 2t + c_1 + c_2e^{-t/2} + c_3e^{-3t}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The general solution of the associated homogeneous equation is
$$
x_h(t)=c_1+c_2e^{-t/2}+c_3e^{-3t}.
$$


::: pf-proof

The homogeneous characteristic polynomial is
$$
2m^3+7m^2+3m
=m(2m^2+7m+3)
=m(2m+1)(m+3).
$$
Its distinct roots are
$$
0,\qquad -\frac12,\qquad -3,
$$
which gives the displayed homogeneous solution.

:::

:::

::: {.pf-step #s1-2}

A particular solution of the nonhomogeneous equation is
$$
x_p(t)=2t.
$$


::: pf-proof

Try $x_p(t)=At$. Then
$$
x_p'=A,\qquad x_p''=0,\qquad x_p'''=0.
$$
Substitution into
$$
2x'''+7x''+3x'=6
$$
gives $3A=6$, hence $A=2$.

:::

:::

::: {.pf-step #s1-3}

Therefore the general solution is
$$
\boxed{x(t)=2t+c_1+c_2e^{-t/2}+c_3e^{-3t}},
$$
so the answer is (E).


::: pf-proof

For a linear nonhomogeneous differential equation, adding any particular solution to the general homogeneous solution gives the full solution family. Combine steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested general solution and corresponding choice.

:::

:::

:::
