---
schema: qual/card@1
id: P-GREPT-19
kind: problem
title: "Solve $y'=x-y$, $y(0)=1$ at $x=1$"
classification:
  areas: [prelim]
  topics:
  - First-Order Linear ODEs
  - Initial Value Problems
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 19 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
If $y' = x - y$ and $y(0) = 1$, then $y(1) =$

(A) $\frac{1}{e}$
(B) $\left(\frac{1}{e}\right) + 1$
(C) $\frac{2}{e}$
(D) $\left(\frac{2}{e}\right) - 1$
(E) $e$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The differential equation has general solution
$$
y=x-1+Ce^{-x}.
$$


::: pf-proof

Rewrite the equation as
$$
y'+y=x.
$$
Multiplying by the integrating factor $e^x$ gives
$$
(e^xy)'=xe^x.
$$
Since
$$
\int xe^x\,dx=e^x(x-1)+C,
$$
we obtain
$$
e^xy=e^x(x-1)+C,
$$
and hence the stated formula.

:::

:::

::: {.pf-step #s1-2}

The initial condition $y(0)=1$ gives $C=2$.


::: pf-proof

Substituting $x=0$ into step [](#s1-1){.pf-ref} gives
$$
1=-1+C,
$$
so $C=2$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
y(1)=\boxed{\frac2e},
$$
so the answer is (C).


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref},
$$
y(1)=1-1+2e^{-1}=\frac2e.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value.

:::

:::

:::
