---
schema: qual/card@1
id: P-GRECH3-11
kind: problem
title: Continuity at the origin of three functions
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
  note: "Checked against Chapter 3 review Question 11 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree."
---

::: {.problem}
Consider the following three functions, each of which is defined for all $(x,y)$ in the plane:
$$
f_1(x,y)=\begin{cases}\dfrac{x-y}{x+y} & \text{if } x+y\ne0\\ 1 & \text{if } x+y=0\end{cases}
$$
$$
f_2(x,y)=\begin{cases}\dfrac{xy}{x^2+y^2} & \text{if } (x,y)\ne(0,0)\\ 0 & \text{if } (x,y)=(0,0)\end{cases}
$$
$$
f_3(x,y)=\begin{cases}\dfrac{x^3-y^3}{x^2+y^2} & \text{if } (x,y)\ne(0,0)\\ 0 & \text{if } (x,y)=(0,0)\end{cases}
$$
Which of these functions is/are continuous at the origin?

(A) None
(B) $f_1$ only
(C) $f_2$ only
(D) $f_3$ only
(E) All three
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The function $f_1$ is not continuous at $(0,0)$.


::: pf-proof

At the origin, $x+y=0$, so
$$
f_1(0,0)=1.
$$
Along the line $y=2x$, for $x\ne0$,
$$
f_1(x,2x)
=\frac{x-2x}{x+2x}
=-\frac13.
$$
Hence
$$
\lim_{x\to0}f_1(x,2x)=-\frac13\ne1=f_1(0,0),
$$
so $f_1$ is not continuous at the origin.

:::

:::

::: {.pf-step #s1-2}

The function $f_2$ is not continuous at $(0,0)$.


::: pf-proof

By definition, $f_2(0,0)=0$. Along the line $y=x$, for $x\ne0$,
$$
f_2(x,x)
=\frac{x^2}{x^2+x^2}
=\frac12.
$$
Thus
$$
\lim_{x\to0}f_2(x,x)=\frac12\ne0=f_2(0,0),
$$
so $f_2$ is not continuous at the origin.

:::

:::

::: {.pf-step #s1-3}

The function $f_3$ is continuous at $(0,0)$.


::: pf-proof

For $(x,y)\ne(0,0)$, set
$$
\rho=\sqrt{x^2+y^2}.
$$
Then $|x|\le\rho$ and $|y|\le\rho$, so
$$
|x|^3\le \rho x^2,
\qquad
|y|^3\le \rho y^2.
$$
Therefore
$$
\left|f_3(x,y)\right|
=\frac{|x^3-y^3|}{x^2+y^2}
\le
\frac{|x|^3+|y|^3}{x^2+y^2}
\le
\frac{\rho(x^2+y^2)}{x^2+y^2}
=\rho.
$$
As $(x,y)\to(0,0)$, one has $\rho\to0$, so the squeeze theorem gives
$$
\lim_{(x,y)\to(0,0)}f_3(x,y)=0=f_3(0,0).
$$
Hence $f_3$ is continuous at the origin.

:::

:::

::: {.pf-step #s1-4}

Exactly $f_3$ is continuous at the origin, so the answer is
$$
\boxed{\text{(D)}}.
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} exclude $f_1$ and $f_2$, while step [](#s1-3){.pf-ref} proves continuity of $f_3$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} identifies precisely which of the three functions is continuous at the origin.

:::

:::

:::
