---
schema: qual/card@1
id: P-GRECH4-05
kind: problem
title: Zeros of a third-order linear ODE solution
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
  note: Re-transcribed from Chapter 4 review Question 5 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch4-review/, replacing the earlier chapter-4.pdf transcription.
---

::: {.problem}
If $a$ is a positive constant, let $y = f(x)$ be the solution of the equation

$$
y''' - ay'' + a^2y' - a^3y = 0
$$

such that $f(0) = 1$, $f'(0) = 0$, and $f''(0) = a^2$. How many positive values of $x$ satisfy the equation $f(x) = 0$?

(A) $0$
(B) $1$
(C) $2$
(D) $3$
(E) more than $3$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The general real solution of the differential equation is
$$
y=c_1e^{ax}+c_2\cos(ax)+c_3\sin(ax).
$$


::: pf-proof

The characteristic polynomial factors as
$$
r^3-ar^2+a^2r-a^3
=(r-a)(r^2+a^2).
$$
Its roots are $a,ia,-ia$, so the displayed expression is the general real solution.

:::

:::

::: {.pf-step #s1-2}

The initial conditions give
$$
c_1=1,\qquad c_2=0,\qquad c_3=-1.
$$


::: pf-proof

From step [](#s1-1){.pf-ref},
$$
y(0)=c_1+c_2=1.
$$
Differentiating gives
$$
y'
=ac_1e^{ax}-ac_2\sin(ax)+ac_3\cos(ax),
$$
so
$$
y'(0)=a(c_1+c_3)=0.
$$
Also,
$$
y''
=a^2c_1e^{ax}-a^2c_2\cos(ax)-a^2c_3\sin(ax),
$$
so
$$
y''(0)=a^2(c_1-c_2)=a^2.
$$
Because $a>0$, these equations reduce to
$$
c_1+c_2=1,\qquad c_1+c_3=0,\qquad c_1-c_2=1,
$$
whose solution is the displayed triple.

:::

:::

::: {.pf-step #s1-3}

Thus
$$
f(x)=e^{ax}-\sin(ax).
$$


::: pf-proof

Substitute the constants from step [](#s1-2){.pf-ref} into the general solution in step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

There are
$$
\boxed{0}
$$
positive values of $x$ satisfying $f(x)=0$, so the answer is (A).


::: pf-proof

If $x>0$, then $a>0$ implies $e^{ax}>1$. On the other hand, $\sin(ax)\le1$. Hence step [](#s1-3){.pf-ref} gives
$$
f(x)=e^{ax}-\sin(ax)>0
$$
for every positive $x$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested number of positive zeros and corresponding choice.

:::

:::

:::
