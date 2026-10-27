---
schema: qual/card@1
id: P-GRECH2-26
kind: problem
title: Integral of the greatest-integer function over $[0,7/2]$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 26 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
If $[x]$ denotes the greatest integer $\le x$, then $\int_{0}^{\frac{7}{2}} [x] dx =$

(A) $\frac{5}{2}$
(B) $\frac{7}{2}$
(C) $\frac{9}{2}$
(D) $\frac{17}{2}$
(E) $\frac{37}{2}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

On the intervals $[0,1)$, $[1,2)$, $[2,3)$, and $[3,7/2]$, the function $[x]$ is respectively $0$, $1$, $2$, and $3$.


::: pf-proof

By definition, $[x]$ is the greatest integer not exceeding $x$. Hence it is constant with the stated values on each interval between consecutive integers.

:::

:::

::: {.pf-step #s1-2}

The integral equals
$$
0\cdot1+1\cdot1+2\cdot1+3\cdot\frac12=\frac92.
$$


::: pf-proof

Using step [](#s1-1){.pf-ref} and additivity of the integral,
$$
\begin{aligned}
\int_0^{7/2}[x]\,dx
&=\int_0^1 0\,dx+\int_1^2 1\,dx+\int_2^3 2\,dx+\int_3^{7/2}3\,dx\\
&=0+1+2+\frac32\\
&=\frac92.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{\frac92},
$$
so the answer is (C).


::: pf-proof

This is exactly the value obtained in step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested integral and corresponding choice.

:::

:::

:::
