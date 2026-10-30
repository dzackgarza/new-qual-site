---
schema: qual/card@1
id: P-GREPT-27
kind: problem
title: "General solution of $y^{(4)}+2y'''+5y''=0$"
classification:
  areas: [prelim]
  topics:
  - Linear ODEs
  - Constant Coefficients
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 27 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Find the general solution of the equation

$$\frac{d^4y}{dx^4} + 2\frac{d^3y}{dx^3} + 5\frac{d^2y}{dx^2} = 0$$

(A) $y = c_1 + c_2x + e^{2x}(c_3 \cos x + c_4 \sin x)$
(B) $y = c_1 + c_2x + e^{-2x}(c_3 \cos x + c_4 \sin x)$
(C) $y = c_1 + c_2x + e^x(c_3 \cos 2x + c_4 \sin 2x)$
(D) $y = c_1 + c_2x + e^{-x}(c_3 \cos 2x + c_4 \sin 2x)$
(E) $y = c_1 + e^x(c_2 \cos 2x + c_3 \sin 2x)$
:::

::: {.solution}

::: pf

::: pf-step

The characteristic polynomial is
$$
r^4+2r^3+5r^2
=r^2(r^2+2r+5).
$$


::: pf-proof

Substituting a trial solution $y=e^{rx}$ into the constant-coefficient
differential equation produces
$$
(r^4+2r^3+5r^2)e^{rx}=0.
$$
Since $e^{rx}$ is nonzero, the displayed polynomial is the characteristic
polynomial, and factoring out $r^2$ gives the stated form.

:::

:::

::: pf-step

Its roots are
$$
r=0\quad\text{with multiplicity }2,
\qquad
r=-1\pm2i.
$$


::: pf-proof

The factor $r^2$ gives the double root $0$. Completing the square in the
remaining factor gives
$$
r^2+2r+5=(r+1)^2+4,
$$
whose roots are $-1\pm2i$.

:::

:::

::: {.pf-step #s1-3}

Therefore the general real solution is
$$
\boxed{y=c_1+c_2x+e^{-x}(c_3\cos2x+c_4\sin2x)},
$$
so the answer is (D).


::: pf-proof

The double root $0$ contributes the independent solutions $1$ and $x$.
The conjugate roots $-1\pm2i$ contribute the real independent solutions
$e^{-x}\cos2x$ and $e^{-x}\sin2x$. Combining these four solutions with
arbitrary real coefficients gives the displayed general solution.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the complete four-parameter solution of the fourth-order
equation.

:::

:::

:::
