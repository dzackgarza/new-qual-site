---
schema: qual/card@1
id: P-GREPT-19
kind: problem
title: "Solve $y'=x-y$, $y(0)=1$ at $x=1$"
classification:
  areas: [prelim]
  topics: []
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
<1>1. The differential equation has general solution
$$
y=x-1+Ce^{-x}.
$$

::: {.proof}
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

<1>2. The initial condition $y(0)=1$ gives $C=2$.

::: {.proof}
Substituting $x=0$ into step <1>1 gives
$$
1=-1+C,
$$
so $C=2$.
:::

<1>3. Therefore
$$
y(1)=\boxed{\frac2e},
$$
so the answer is (C).

::: {.proof}
By steps <1>1--<1>2,
$$
y(1)=1-1+2e^{-1}=\frac2e.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested value.
:::
:::
