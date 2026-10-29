---
schema: qual/card@1
id: P-GRECH4-08
kind: problem
title: Fourth-order ODE initial-value problem
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
  note: Re-transcribed from Chapter 4 review Question 8 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch4-review/, replacing the earlier chapter-4.pdf transcription.
---

::: {.problem}
Let $y = f(x)$ be the solution of the equation

$$
\frac{d^4y}{dx^4} = \frac{d^2y}{dx^2}
$$

such that $f(0) = f'(0) = f''(0) = 0$ and $f'''(0) = -1$. What is $f(x)$?

(A) $x - \cosh x$
(B) $x - \sinh x$
(C) $x + \cosh x$
(D) $x + \sinh x$
(E) $\cosh x + \sinh x$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The general real solution is
$$
y=A+Bx+C\cosh x+D\sinh x.
$$


::: pf-proof

The differential equation is
$$
y^{(4)}-y''=0,
$$
whose characteristic polynomial factors as
$$
r^4-r^2=r^2(r-1)(r+1).
$$
Thus $0$ is a double root and $\pm1$ are simple roots, giving the displayed general solution.

:::

:::

::: {.pf-step #s1-2}

The conditions $f(0)=f''(0)=0$ imply
$$
A=0,\qquad C=0.
$$


::: pf-proof

From step [](#s1-1){.pf-ref},
$$
y(0)=A+C=0.
$$
Also
$$
y''=C\cosh x+D\sinh x,
$$
so $y''(0)=C=0$. Substituting this into $A+C=0$ gives $A=0$.

:::

:::

::: {.pf-step #s1-3}

The conditions $f'(0)=0$ and $f'''(0)=-1$ imply
$$
B=1,\qquad D=-1.
$$


::: pf-proof

Differentiating step [](#s1-1){.pf-ref} gives
$$
y'=B+C\sinh x+D\cosh x,
$$
so, using $C=0$ from step [](#s1-2){.pf-ref},
$$
y'(0)=B+D=0.
$$
Also
$$
y'''=C\sinh x+D\cosh x,
$$
hence
$$
y'''(0)=D=-1.
$$
Therefore $B=1$.

:::

:::

::: {.pf-step #s1-4}

Consequently
$$
\boxed{f(x)=x-\sinh x},
$$
so the answer is (B).


::: pf-proof

Substitute the constants from steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} into the general solution in step [](#s1-1){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested solution and corresponding choice.

:::

:::

:::
