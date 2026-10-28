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

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The tangent line to $g$ at $x_n$ is
$$
L_n(t)=g(x_n)+g'(x_n)(t-x_n).
$$


::: pf-proof

The tangent line through $(x_n,g(x_n))$ has slope $g'(x_n)$, so its point-slope equation is exactly the displayed formula.

:::

:::

::: {.pf-step #s1-2}

Its $x$-intercept is
$$
x_{n+1}=x_n-\frac{g(x_n)}{g'(x_n)}.
$$


::: pf-proof

By definition of $x_{n+1}$, one has $L_n(x_{n+1})=0$. Using step [](#s1-1){.pf-ref},
$$
0=g(x_n)+g'(x_n)(x_{n+1}-x_n).
$$
Since $g'(x_n)\ne0$ by hypothesis, solving for $x_{n+1}$ gives the displayed recurrence.

:::

:::

::: {.pf-step #s1-3}

Therefore Newton's iteration is
$$
\boxed{x_{n+1}=x_n-\frac{g(x_n)}{g'(x_n)}},
$$
which is choice (D), with the $x$ in its displayed quotient evaluated at $x_n$.


::: pf-proof

Step [](#s1-2){.pf-ref} derives the recurrence directly from the tangent-intercept construction in the problem.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested approximation formula.

:::

:::

:::
