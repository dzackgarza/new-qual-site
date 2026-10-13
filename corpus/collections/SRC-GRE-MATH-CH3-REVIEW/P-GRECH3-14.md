---
schema: qual/card@1
id: P-GRECH3-14
kind: problem
title: Mixed partial derivative at the origin
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
  note: "Checked against Chapter 3 review Question 14 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree."
---

::: {.problem}
Let $f$ be the function defined for all $(x,y)$ as follows:
\[
f(x,y)=\begin{cases}xy\,\dfrac{x^2-y^2}{x^2+y^2} & \text{if } (x,y)\ne(0,0)\\ 0 & \text{if } (x,y)=(0,0)\end{cases}
\]
What is the value of $f_{xy}$ at the point $(0,0)$?

(A) $-1$
(B) $0$
(C) $\frac{1}{2}$
(D) $1$
(E) Undefined
:::

::: {.solution}
<1>1. For every $y\ne0$,
$$
f_x(0,y)=-y.
$$

::: {.proof}
By the definition of the partial derivative with respect to $x$,
$$
f_x(0,y)
=\lim_{h\to0}\frac{f(h,y)-f(0,y)}{h}.
$$
For $y\ne0$, one has $f(0,y)=0$, and for sufficiently small nonzero $h$,
$$
\frac{f(h,y)}{h}
=y\,\frac{h^2-y^2}{h^2+y^2}.
$$
Therefore
$$
f_x(0,y)
=y\lim_{h\to0}\frac{h^2-y^2}{h^2+y^2}
=-y.
$$
:::

<1>2. One has
$$
f_x(0,0)=0.
$$

::: {.proof}
Again by definition,
$$
f_x(0,0)
=\lim_{h\to0}\frac{f(h,0)-f(0,0)}{h}.
$$
The defining formula gives $f(h,0)=0$ for every $h$ and $f(0,0)=0$, so the quotient is identically zero.
:::

<1>3. The mixed partial derivative at the origin is
$$
\boxed{f_{xy}(0,0)=-1},
$$
so the answer is (A).

::: {.proof}
By definition of differentiation of $f_x$ with respect to $y$,
$$
f_{xy}(0,0)
=\lim_{k\to0}\frac{f_x(0,k)-f_x(0,0)}{k}.
$$
For $k\ne0$, step <1>1 gives $f_x(0,k)=-k$, while step <1>2 gives $f_x(0,0)=0$. Hence
$$
f_{xy}(0,0)
=\lim_{k\to0}\frac{-k}{k}
=-1.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested mixed partial derivative and corresponding choice.
:::
:::
