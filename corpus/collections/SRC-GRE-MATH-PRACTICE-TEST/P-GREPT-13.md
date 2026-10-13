---
schema: qual/card@1
id: P-GREPT-13
kind: problem
title: "Maximum of $\\log x/x^a$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 13 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
If $a$ is a positive constant, what is the maximum value of the following function?

$$f(x) = \frac{\log x}{x^a}$$

(A) $\frac{1}{ae}$
(B) $a^{a-1}$
(C) $a^e$
(D) $e^a$
(E) $\frac{e^{a^2}}{a}$
:::

::: {.solution}
<1>1. On its domain $x>0$,
$$
f'(x)=\frac{1-a\log x}{x^{a+1}}.
$$

::: {.proof}
Writing $f(x)=(\log x)x^{-a}$ and applying the product rule gives
$$
f'(x)=\frac1x x^{-a}+(\log x)(-a)x^{-a-1}
=x^{-a-1}(1-a\log x).
$$
:::

<1>2. The function increases on $(0,e^{1/a})$ and decreases on
$(e^{1/a},\infty)$.

::: {.proof}
Because $a>0$ and $x^{a+1}>0$, the sign of $f'(x)$ in step <1>1 is the sign
of $1-a\log x$. This quantity is positive exactly when
$x<e^{1/a}$, vanishes at $x=e^{1/a}$, and is negative exactly when
$x>e^{1/a}$.
:::

<1>3. Hence the maximum value is
$$
\boxed{\frac1{ae}},
$$
so the answer is (A).

::: {.proof}
By step <1>2, the unique global maximum occurs at $x=e^{1/a}$. At that point,
$$
f(e^{1/a})
=\frac{\log(e^{1/a})}{(e^{1/a})^a}
=\frac{1/a}{e}
=\frac1{ae}.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested maximum value.
:::
:::
