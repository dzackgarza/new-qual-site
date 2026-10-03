---
schema: qual/card@1
id: P-GREPT-40
kind: problem
title: "Tangent line to $y=x^{(e^x)}$ at $(1,1)$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 40 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR). The extraction prints the exponent as e^+; the book's Chapter 10 solution differentiates x^(e^x)."
---

::: {.problem}
The tangent line to the curve $y = x^{(e^x)}$ at the point $(1, 1)$ passes through the point $(2, y_0)$, where $y_0 =$

(A) $e - 1$
(B) $e$
(C) $2e - 1$
(D) $e + 1$
(E) $2e$
:::

::: {.solution}
<1>1. For $x>0$, the derivative of
$$
y=x^{e^x}
$$
is
$$
y'=x^{e^x}e^x\left(\log x+\frac1x\right).
$$

::: {.proof}
Taking logarithms gives
$$
\log y=e^x\log x.
$$
Differentiating yields
$$
\frac{y'}y=e^x\log x+\frac{e^x}{x},
$$
and multiplying by $y=x^{e^x}$ gives the formula.
:::

<1>2. The slope at $(1,1)$ is
$$
y'(1)=e.
$$

::: {.proof}
Substituting $x=1$ into step <1>1 gives
$$
y'(1)=1^e e\left(\log1+1\right)=e.
$$
:::

<1>3. The tangent line is
$$
y-1=e(x-1).
$$

::: {.proof}
The tangent line through $(1,1)$ with slope $e$ from step <1>2 has the
displayed point-slope equation.
:::

<1>4. At $x=2$, this line has
$$
y_0=\boxed{e+1},
$$
so the answer is (D).

::: {.proof}
Substituting $x=2$ into step <1>3 gives $y-1=e$, hence $y=e+1$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested value.
:::
:::
