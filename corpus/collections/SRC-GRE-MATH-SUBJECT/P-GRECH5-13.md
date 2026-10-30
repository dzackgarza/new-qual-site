---
schema: qual/card@1
id: P-GRECH5-13
kind: problem
title: Locus defined by a $3\times3$ determinant
classification:
  areas:
  - applied-algebra
  topics:
  - Determinants
  - Analytic Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 5 review Question 13 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
The set of all points $(x, y)$ in $\RR^2$ that satisfy the equation

$$
\begin{vmatrix} x & y & 1 \\ 0 & y_1 & 1 \\ 1 & y_2 & 1 \end{vmatrix} = 0
$$

forms

(A) an ellipse centered at the origin
(B) a line with slope $\frac{y_2}{y_1}$
(C) a circle with center $(0, y_1)$ and radius $1$
(D) a line with slope $y_2 - y_1$
(E) a parabola with vertex $(1, y_2)$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The determinant equation is equivalent to
$$
x(y_1-y_2)+y-y_1=0.
$$


::: pf-proof

Expanding the determinant along the first row gives
$$
x\begin{vmatrix}y_1&1\\ y_2&1\end{vmatrix}
-y\begin{vmatrix}0&1\\ 1&1\end{vmatrix}
+\begin{vmatrix}0&y_1\\ 1&y_2\end{vmatrix}.
$$
The three $2\times2$ determinants are $y_1-y_2$, $-1$, and $-y_1$, respectively. Hence the displayed determinant equals $x(y_1-y_2)+y-y_1$.

:::

:::

::: {.pf-step #s1-2}

The locus is the line
$$
y=(y_2-y_1)x+y_1,
$$
whose slope is
$$
\boxed{y_2-y_1}.
$$
Thus the answer is (D).


::: pf-proof

Solving the equation in step [](#s1-1){.pf-ref} for $y$ gives
$$
y=y_1-x(y_1-y_2)=(y_2-y_1)x+y_1.
$$
This is the slope-intercept equation of a line with slope $y_2-y_1$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} identifies the locus and its slope.

:::

:::

:::
