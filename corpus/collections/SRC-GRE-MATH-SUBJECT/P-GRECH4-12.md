---
schema: qual/card@1
id: P-GRECH4-12
kind: problem
title: General solution of a homogeneous first-order ODE
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
  note: Re-transcribed from Chapter 4 review Question 12 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch4-review/, replacing the earlier chapter-4.pdf transcription.
---

::: {.problem}
Find the general solution of the differential equation:

$$
\frac{dy}{dx} = \frac{x + y}{x}
$$

(A) $e^{y/x} = cx$
(B) $e^{y/x} = cy$
(C) $e^{x/y} = cx$
(D) $e^{x/y} = cy$
(E) $e^{-x/y} = cx$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

With the substitution
$$
v=\frac{y}{x},
\qquad
y=xv,
$$
the differential equation becomes
$$
x\frac{dv}{dx}=1.
$$


::: pf-proof

On any interval where the equation is defined, $x\ne0$. Since
$$
y=xv,
$$
differentiation gives
$$
\frac{dy}{dx}=v+x\frac{dv}{dx}.
$$
The right-hand side of the given equation is
$$
\frac{x+y}{x}=1+\frac{y}{x}=1+v.
$$
Equating these expressions and cancelling $v$ gives the displayed equation.

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\frac{y}{x}=\log\abs{x}+C.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives
$$
\frac{dv}{dx}=\frac1x.
$$
Integrating on an interval not containing $0$ yields
$$
v=\log\abs{x}+C.
$$
Substitute $v=y/x$.

:::

:::

::: {.pf-step #s1-3}

The general solution may be written
$$
\boxed{e^{y/x}=cx},
$$
so the answer is (A).


::: pf-proof

Exponentiating step [](#s1-2){.pf-ref} gives
$$
e^{y/x}=e^C\abs{x}.
$$
On any connected solution interval, the sign of $x$ is fixed. Absorbing that fixed sign together with $e^C$ into a nonzero constant $c$ gives $e^{y/x}=cx$; necessarily $cx>0$ on that interval.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested general solution and corresponding choice.

:::

:::

:::
