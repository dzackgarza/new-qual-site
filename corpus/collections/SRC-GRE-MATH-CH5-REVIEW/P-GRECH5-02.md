---
schema: qual/card@1
id: P-GRECH5-02
kind: problem
title: Parameter in a three-equation linear system
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 5 review Question 2 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
The solution of the system

$$
\begin{aligned}
ax + ay - z &= 1 \\
x - ay - az &= -1 \\
ax - y + az &= 1
\end{aligned}
$$

is $(x, y, z) = (a, b, a)$. If $a$ is NOT an integer, what is the numerical value of $a + b$?

(A) $-\frac{3}{2}$
(B) $-1$
(C) $0$
(D) $\frac{1}{2}$
(E) $1$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Substituting $(x,y,z)=(a,b,a)$ into the third equation gives
$$
b=2a^2-1.
$$


::: pf-proof

The third equation becomes
$$
a(a)-b+a(a)=1,
$$
so
$$
2a^2-b=1.
$$
Solving for $b$ gives the displayed formula.

:::

:::

::: {.pf-step #s1-2}

The parameter $a$ satisfies
$$
(a^2-1)(2a+1)=0.
$$


::: pf-proof

The first equation after substitution is
$$
a^2+ab-a=1.
$$
Using step [](#s1-1){.pf-ref},
$$
a^2+a(2a^2-1)-a=1,
$$
so
$$
2a^3+a^2-2a-1=0.
$$
Factoring gives
$$
2a^3+a^2-2a-1
=(a^2-1)(2a+1).
$$

:::

:::

::: {.pf-step #s1-3}

Since $a$ is not an integer,
$$
a=-\frac12
\qquad\text{and}\qquad
b=-\frac12.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives
$$
a\in\left\{1,-1,-\frac12\right\}.
$$
The first two values are integers, so the hypothesis forces $a=-1/2$. Step [](#s1-1){.pf-ref} then gives
$$
b=2\left(\frac14\right)-1=-\frac12.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{a+b=-1},
$$
so the answer is (B).


::: pf-proof

Add the two values in step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested numerical value and corresponding choice.

:::

:::

:::
