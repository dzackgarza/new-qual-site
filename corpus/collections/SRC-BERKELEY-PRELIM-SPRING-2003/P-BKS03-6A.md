---
schema: qual/card@1
id: P-BKS03-6A
kind: problem
title: If $2x_{n+1}-x_n\to x$, then $x_n\to x$
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the boundedness induction, the half-sum identity, and
    the two limsup/liminf inequalities that force convergence. No retained solution set covers this
    exercise, so the argument is the card's own; the induction and both inequalities were re-read for this
    pass.
---

::: {.problem}
Suppose $(x_n)$ is a real sequence such that
$$
2x_{n+1}-x_n\longrightarrow x.
$$
Show that $x_n\to x$.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own. Write $b_{n}=2x_{n+1}-x_{n}$, so that $b_{n}\to x$ by hypothesis and $x_{n+1}=\tfrac12\bigl(x_{n}+b_{n}\bigr)$.

::: pf

::: {.pf-step #bounded}
The sequence $(x_{n})$ is bounded.

::: pf-proof
The convergent sequence $(b_{n})$ is bounded, so choose $M>0$ with $\abs{x_{1}}\le M$ and $\abs{b_{n}}\le M$ for all $n$. Then $\abs{x_{n}}\le M$ for all $n$: it holds for $n=1$ by the choice of $M$, and if $\abs{x_{n}}\le M$ then
$$
\abs{x_{n+1}}=\abs{\frac{x_{n}+b_{n}}{2}}\le\frac{\abs{x_{n}}+\abs{b_{n}}}{2}\le M,
$$
so the bound passes from $n$ to $n+1$ and holds throughout by induction.
:::

:::

::: {.pf-step #upper}
$\limsup x_{n}\le x$.

::: pf-proof
Since $x_{n+1}=\tfrac12(x_{n}+b_{n})$ and shifting a sequence does not change its limit superior, $\limsup x_{n}=\limsup x_{n+1}\le\tfrac12\bigl(\limsup x_{n}+\limsup b_{n}\bigr)=\tfrac12\bigl(\limsup x_{n}+x\bigr)$, using subadditivity of the limit superior for bounded sequences and $\limsup b_{n}=\lim b_{n}=x$. Writing $L=\limsup x_{n}$, which is a real number by step [](#bounded){.pf-ref}, the inequality $L\le\tfrac12(L+x)$ gives $L\le x$.
:::

:::

::: {.pf-step}
$\liminf x_{n}\ge x$, and hence $x_{n}\to x$.

::: pf-proof
The same computation with the limit inferior, $\liminf x_{n+1}\ge\tfrac12\bigl(\liminf x_{n}+\liminf b_{n}\bigr)$, gives $\liminf x_{n}\ge x$. Since $\liminf x_{n}\le\limsup x_{n}$ for every sequence, steps [](#upper){.pf-ref} and this inequality sandwich the two into $x\le\liminf x_{n}\le\limsup x_{n}\le x$, so both equal $x$; a real sequence whose limit inferior and limit superior coincide converges to that common value. Hence $x_{n}\to x$, as claimed.
:::

:::

:::
:::
