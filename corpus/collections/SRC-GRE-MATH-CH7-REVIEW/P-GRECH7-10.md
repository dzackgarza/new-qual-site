---
schema: qual/card@1
id: P-GRECH7-10
kind: problem
title: Newton's method iteration formula
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 10 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Let $g(x)$ be a polynomial function whose derivative is continuous and nonzero on the interval $[a,b]$. Suppose there exists a $y$ on this same interval such that $g(y)=0$. Let $x_0$ be an arbitrary $x$-value in the interval. Then $x_1$ is the $x$-intercept of the line tangent to $g(x)$ at $x_0$. For each subsequent $n$, $x_n$ is the $x$-intercept of the line tangent to $g(x)$ at $x_{n-1}$. Which formula best approximates the root of $g(x)$ using the method described above?

(A) $x_{n+1}=x_n-\dfrac{g(x)}{g^{n}(x)}$
(B) $x_{n+1}=x_n-\dfrac{g'(x)}{g''(x)}$
(C) $x_{n+1}=x_n+\dfrac{g(x)}{g'(x)}$
(D) $x_{n+1}=x_n-\dfrac{g(x)}{g'(x)}$
(E) $x_{n+1}=x_n-\dfrac{g'(x)}{g(x)}$
:::
