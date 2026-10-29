---
schema: qual/card@1
id: P-GRECH7-48
kind: problem
title: Recovering $v$ from the real part $5x-3y$ of an analytic function
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 48 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Let $f(z)$ be a complex analytic function such that $f(z) = (5x - 3y) + i v(x, y)$, where $v(x, y)$ is a real-valued function and $x, y, \in \RR$. If $v(4, 1) = 7$, what is $v(3, 2)$?

(A) $-10$
(B) $-9$
(C) $1$
(D) $9$
(E) $14$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The Cauchy--Riemann equations give
$$
v_y=5
\qquad\text{and}\qquad
v_x=3.
$$


::: pf-proof

Write $f=u+iv$ with $u(x,y)=5x-3y$. Since $f$ is analytic, the Cauchy--Riemann equations are $u_x=v_y$ and $u_y=-v_x$. Here $u_x=5$ and $u_y=-3$, so $v_y=5$ and $v_x=3$.

:::

:::

::: {.pf-step #s1-2}

There is a real constant $C$ such that
$$
v(x,y)=3x+5y+C.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, integrating $v_y=5$ with respect to $y$ gives $v(x,y)=5y+h(x)$ for some differentiable function $h$. Differentiating with respect to $x$ and using $v_x=3$ from step [](#s1-1){.pf-ref} gives $h'(x)=3$, hence $h(x)=3x+C$ for a constant $C$.

:::

:::

::: {.pf-step #s1-3}

The initial value $v(4,1)=7$ gives $C=-10$.


::: pf-proof

Substituting $(x,y)=(4,1)$ into the formula from step [](#s1-2){.pf-ref} gives
$$
7=3(4)+5(1)+C=17+C,
$$
so $C=-10$.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
v(3,2)=\boxed{9},
$$
so the answer is (D).


::: pf-proof

By steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref},
$$
v(3,2)=3(3)+5(2)-10=9.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested value.

:::

:::

:::
