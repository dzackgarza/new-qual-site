---
schema: qual/card@1
id: P-GREPT-45
kind: problem
title: "Line integral of $e^x(\\sin y\\,dx+\\cos y\\,dy)$ along a parametrized curve"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 45 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Let $C$ be the curve in the $xy$-plane given parametrically by the equations $x = te^{1-t}$ and $y = \arcsin t$, as the parameter $t$ increases from $0$ to $1$. Evaluate the integral

$$\int_C e^x (\sin y \, dx + \cos y \, dy)$$

(A) $1$
(B) $e$
(C) $\frac{\pi e}{2}$
(D) $2e$
(E) $\pi e$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The differential form
$$
e^x\sin y\,dx+e^x\cos y\,dy
$$
is exact, with potential
$$
F(x,y)=e^x\sin y.
$$


::: pf-proof

Direct differentiation gives
$$
F_x=e^x\sin y
\qquad\text{and}\qquad
F_y=e^x\cos y,
$$
which are exactly the coefficients of $dx$ and $dy$ in the integrand.

:::

:::

::: {.pf-step #s1-2}

The curve $C$ starts at $(0,0)$ and ends at $(1,\pi/2)$.


::: pf-proof

At $t=0$,
$$
x=0e^1=0,
\qquad
y=\arcsin0=0.
$$
At $t=1$,
$$
x=1e^0=1,
\qquad
y=\arcsin1=\frac\pi2.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\int_C e^x(\sin y\,dx+\cos y\,dy)=\boxed{e},
$$
so the answer is (B).


::: pf-proof

By the fundamental theorem for line integrals and steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref},
$$
\begin{aligned}
\int_C dF
&=F(1,\pi/2)-F(0,0)\\
&=e\sin(\pi/2)-1\sin0\\
&=e.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required integral.

:::

:::

:::
