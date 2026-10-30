---
schema: qual/card@1
id: P-GRECH2-35
kind: problem
title: Arc length of the astroid $x^{2/3}+y^{2/3}=1$
classification:
  areas: [prelim]
  topics:
  - Arc Length
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 35 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Calculate the length of the portion of the hypocycloid $x^{2/3} + y^{2/3} = 1$ in the first quadrant from the point $\left(\frac{1}{8}, \frac{3\sqrt{3}}{8}\right)$, to the point $(1, 0)$.

(A) $\frac{9}{8}$
(B) $\frac{3\sqrt{2}}{4}$
(C) $1$
(D) $\frac{5\sqrt{2}}{8}$
(E) $\frac{\sqrt{3}}{2}$
:::

::: {.solution}

On the first-quadrant branch,
$$
y=(1-x^{2/3})^{3/2}.
$$

::: pf

::: {.pf-step #s1-1}

For $0<x<1$,
$$
y'=-x^{-1/3}(1-x^{2/3})^{1/2}.
$$


::: pf-proof

Differentiate the displayed expression by the chain rule:
$$
\begin{aligned}
y'
&=\frac32(1-x^{2/3})^{1/2}\left(-\frac23x^{-1/3}\right)\\
&=-x^{-1/3}(1-x^{2/3})^{1/2}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

The arc-length integrand simplifies to
$$
\sqrt{1+(y')^2}=x^{-1/3}.
$$


::: pf-proof

Using step [](#s1-1){.pf-ref},
$$
\begin{aligned}
1+(y')^2
&=1+x^{-2/3}(1-x^{2/3})\\
&=x^{-2/3}.
\end{aligned}
$$
Since $x>0$, its positive square root is $x^{-1/3}$.

:::

:::

::: {.pf-step #s1-3}

The required length is
$$
\boxed{\frac98},
$$
so the answer is (A).


::: pf-proof

The endpoint abscissas are $1/8$ and $1$. Therefore, by step [](#s1-2){.pf-ref},
$$
\begin{aligned}
L
&=\int_{1/8}^{1}x^{-1/3}\,dx\\
&=\left[\frac32x^{2/3}\right]_{1/8}^{1}\\
&=\frac32\left(1-\frac14\right)\\
&=\frac98.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested arc length and corresponding choice.

:::

:::

:::
