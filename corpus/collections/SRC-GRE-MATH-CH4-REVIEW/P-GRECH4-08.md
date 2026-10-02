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

\[
\frac{d^4y}{dx^4} = \frac{d^2y}{dx^2}
\]

such that $f(0) = f'(0) = f''(0) = 0$ and $f'''(0) = -1$. What is $f(x)$?

(A) $x - \cosh x$
(B) $x - \sinh x$
(C) $x + \cosh x$
(D) $x + \sinh x$
(E) $\cosh x + \sinh x$
:::

::: {.solution}
<1>1. The general real solution is
$$
y=A+Bx+C\cosh x+D\sinh x.
$$

::: {.proof}
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

<1>2. The conditions $f(0)=f''(0)=0$ imply
$$
A=0,\qquad C=0.
$$

::: {.proof}
From step <1>1,
$$
y(0)=A+C=0.
$$
Also
$$
y''=C\cosh x+D\sinh x,
$$
so $y''(0)=C=0$. Substituting this into $A+C=0$ gives $A=0$.
:::

<1>3. The conditions $f'(0)=0$ and $f'''(0)=-1$ imply
$$
B=1,\qquad D=-1.
$$

::: {.proof}
Differentiating step <1>1 gives
$$
y'=B+C\sinh x+D\cosh x,
$$
so, using $C=0$ from step <1>2,
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

<1>4. Consequently
$$
\boxed{f(x)=x-\sinh x},
$$
so the answer is (B).

::: {.proof}
Substitute the constants from steps <1>2 and <1>3 into the general solution in step <1>1.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested solution and corresponding choice.
:::
:::
