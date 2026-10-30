---
schema: qual/card@1
id: P-GREPT-63
kind: problem
title: "Radius of convergence of $\\sum (n!)^3x^{2n}/(3n)!$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 63 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Find the largest number $a$ that makes the following statement true:

"The series $\sum_{n=0}^{\infty} \frac{(n!)^3}{(3n)!} x^{2n}$ converges for all $x$ with $\abs{x} < a$."

(A) $3$
(B) $3\sqrt{3}$
(C) $6$
(D) $6\sqrt{3}$
(E) $9$
:::

::: {.solution}

For fixed $x$, write
$$
u_n=\frac{(n!)^3}{(3n)!}x^{2n}.
$$

::: pf

::: {.pf-step #s1-1}

If $x\neq 0$, the ratio of successive absolute values satisfies
$$
\lim_{n\to\infty}\abs{\frac{u_{n+1}}{u_n}}
=\frac{x^2}{27}.
$$


::: pf-proof

For $x\neq 0$,
$$
\abs{\frac{u_{n+1}}{u_n}}
=\frac{(n+1)^3x^2}{(3n+3)(3n+2)(3n+1)}.
$$
Dividing numerator and denominator by $n^3$ and taking the limit gives
$x^2/(3\cdot3\cdot3)=x^2/27$.

:::

:::

::: {.pf-step #s1-2}

The series converges for every $x$ with $\abs{x}<3\sqrt3$.


::: pf-proof

If $x=0$, the series is $1$ and therefore converges. If
$0<\abs{x}<3\sqrt3$, then $x^2/27<1$, so step [](#s1-1){.pf-ref} and the ratio test imply
absolute convergence.

:::

:::

::: {.pf-step #s1-3}

For every $x$ with $\abs{x}>3\sqrt3$, the series diverges.


::: pf-proof

If $\abs{x}>3\sqrt3$, then the limit in step [](#s1-1){.pf-ref} is greater than $1$.
Hence $\abs{u_{n+1}/u_n}>1$ for all sufficiently large $n$, so in particular
$u_n$ does not tend to $0$. Therefore the series diverges.

:::

:::

::: {.pf-step #s1-4}

The largest admissible number is $\boxed{3\sqrt3}$.


::: pf-proof

Step [](#s1-2){.pf-ref} shows that $a=3\sqrt3$ has the required property. If
$a>3\sqrt3$, choose $x$ with $3\sqrt3<\abs{x}<a$. Step [](#s1-3){.pf-ref} then shows that
the series diverges at this $x$, so such an $a$ cannot have the required
property. Thus the correct choice is (B).

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} establishes the largest possible value of $a$.

:::

:::

:::
