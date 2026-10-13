---
schema: qual/card@1
id: P-GRECH2-33
kind: problem
title: Solid of revolution with volume independent of the parameters
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 33 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Let $a$ and $b$ be positive numbers. The region in the second quadrant bounded by the graphs of $y = ax^2$ and $y = -bx$ is revolved around the $x$-axis. Which of the following relationships between $a$ and $b$ would imply that the volume of this solid of revolution is a constant, independent of $a$ and $b$?

(A) $b^4 = 2a^5$
(B) $b^3 = 2a^5$
(C) $b^5 = 2a^3$
(D) $b^4 = 2a^2$
(E) $b^2 = 2a^3$
:::

::: {.solution}
<1>1. The two boundary curves meet at
$$
x=-\frac{b}{a}
\quad\text{and}\quad
x=0.
$$

::: {.proof}
Their intersections satisfy
$$
ax^2=-bx,
$$
so
$$
x(ax+b)=0.
$$
Since $a,b>0$, the two solutions are $x=0$ and $x=-b/a$.
:::

<1>2. The volume of revolution is
$$
V=\frac{2\pi}{15}\frac{b^5}{a^3}.
$$

::: {.proof}
For $-b/a\le x\le0$, the line $y=-bx$ is above the parabola $y=ax^2$. Rotating about the $x$-axis gives washers with outer radius $-bx$ and inner radius $ax^2$. Hence
$$
\begin{aligned}
V
&=\pi\int_{-b/a}^{0}\left[b^2x^2-a^2x^4\right]dx\\
&=\pi\left[\frac{b^2x^3}{3}-\frac{a^2x^5}{5}\right]_{-b/a}^{0}\\
&=\frac{2\pi b^5}{15a^3}.
\end{aligned}
$$
:::

<1>3. The relation
$$
\boxed{b^5=2a^3}
$$
makes $V$ independent of $a$ and $b$, so the answer is (C).

::: {.proof}
Under the displayed relation,
$$
\frac{b^5}{a^3}=2,
$$
so step <1>2 gives the constant volume
$$
V=\frac{4\pi}{15}.
$$
Thus choice (C) has the required property.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 verifies the stated parameter relation produces a constant volume.
:::
:::
