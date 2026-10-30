---
schema: qual/card@1
id: P-GREPT-21
kind: problem
title: "Integral of the fractional part over $[-\\frac12,1]$"
classification:
  areas: [prelim]
  topics:
  - Integration
  - Fractional Part
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 21 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
For any real number $x$, let $[x]$ denote the unique integer, $n$, such that $n \le x < n + 1$. Evaluate the integral

$$\int_{-b}^{2b} (x - [x]) \, dx$$

for $b = \frac{1}{2}$.

(A) $\frac{3}{4}$
(B) $\frac{7}{8}$
(C) $\frac{5}{4}$
(D) $\frac{9}{8}$
(E) does not exist
:::

::: {.solution}

::: pf

::: pf-step

For $b=\frac12$, the integral is
$$
\int_{-1/2}^{1}(x-[x])\,dx.
$$


::: pf-proof

Substituting $b=1/2$ into the limits $-b$ and $2b$ gives $-1/2$ and $1$.

:::

:::

::: pf-step

On the relevant subintervals,
$$
x-[x]=
\begin{cases}
x+1, & -\frac12\le x<0,\\
x, & 0\le x<1.
\end{cases}
$$


::: pf-proof

For $-1\le x<0$, the defining integer is $[x]=-1$, while for
$0\le x<1$ it is $[x]=0$. The values at the single endpoints do not affect
the integral.

:::

:::

::: {.pf-step #s1-3}

The two pieces have integrals
$$
\int_{-1/2}^{0}(x+1)\,dx=\frac38
\qquad\text{and}\qquad
\int_0^1x\,dx=\frac12.
$$


::: pf-proof

Direct calculation gives
$$
\left[\frac{x^2}{2}+x\right]_{-1/2}^{0}=\frac38
$$
and
$$
\left[\frac{x^2}{2}\right]_0^1=\frac12.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\int_{-1/2}^{1}(x-[x])\,dx
=\boxed{\frac78},
$$
so the answer is (B).


::: pf-proof

Adding the two values from step [](#s1-3){.pf-ref} gives
$$
\frac38+\frac12=\frac78.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required integral.

:::

:::

:::
