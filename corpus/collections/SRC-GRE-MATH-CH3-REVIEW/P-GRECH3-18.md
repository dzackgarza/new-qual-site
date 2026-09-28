---
schema: qual/card@1
id: P-GRECH3-18
kind: problem
title: Multivariable chain rule from tabulated derivatives
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
  note: "Checked against Chapter 3 review Question 18 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree."
---

::: {.problem}
Let $f$, $g$, and $h$ be functions of two variables that are differentiable everywhere such that $z=f(x,y)$, where $x=g(u,v)$ and $y=h(u,v)$. When $u=0$ and $v=1$, the values of $x$ and $y$ are $2$ and $1$, respectively. Let $P_0$ denote the point $(u,v)=(0,1)$, and let $Q_0$ denote the point $(x,y)=(2,1)$. Given the following data,
\[
\left.\frac{\partial f}{\partial x}\right|_{Q_0}=11,\quad
\left.\frac{\partial f}{\partial y}\right|_{Q_0}=-3,\quad
\left.\frac{\partial g}{\partial u}\right|_{P_0}=1,\quad
\left.\frac{\partial h}{\partial u}\right|_{P_0}=-3,\quad
\left.\frac{\partial g}{\partial v}\right|_{P_0}=\left.\frac{\partial h}{\partial v}\right|_{P_0}=2,
\]
what's the value of $\frac{\partial z}{\partial v}$ at $P_0$?

(A) $-21$
(B) $16$
(C) $15$
(D) $12$
(E) $-10$
:::
