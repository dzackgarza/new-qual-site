---
schema: qual/card@1
id: P-BERK90S-03
kind: problem
title: A coefficient-norm bound for the roots of a monic polynomial
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-22
  note: Compared Problem 3 with the retained MinerU Flash extraction of Spring90.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
---

::: {.problem}
Let $c_0,\ldots,c_{n-1}\in\CC$. Prove that every zero of
$$
z^n+c_{n-1}z^{n-1}+\cdots+c_1z+c_0
$$
lies in the open disk centered at $0$ of radius
$$
\sqrt{1+\abs{c_{n-1}}^2+\cdots+\abs{c_1}^2+\abs{c_0}^2}.
$$
:::

::: {.solution}
Put $C\coloneqq\sum_{j=0}^{n-1}\abs{c_j}^2$. Let $\zeta\in\CC$ be a
zero of the polynomial, and put $r\coloneqq\abs{\zeta}$.

<1>1. If $C=0$, then $r<\sqrt{1+C}$.

::: {.proof}
Every summand defining $C$ is nonnegative. Thus $C=0$ forces every
coefficient $c_j$ to vanish. The polynomial is then $z^n$, so $\zeta=0$
and $r=0<1=\sqrt{1+C}$.
:::

<1>2. If $C>0$ and $r\leq1$, then $r<\sqrt{1+C}$.

::: {.proof}
The assumption $C>0$ gives $r\leq1<\sqrt{1+C}$.
:::

<1>3. If $C>0$ and $r>1$, then $r<\sqrt{1+C}$.

::: {.proof}
The equation defining $\zeta$ gives
$$
\zeta^n=-\sum_{j=0}^{n-1}c_j\zeta^j.
$$
The triangle inequality and the
[[PR-X5D4Z|Cauchy--Schwarz inequality]] applied to the vectors
$(\abs{c_j})_{j=0}^{n-1}$ and $(r^j)_{j=0}^{n-1}$ give
$$
\begin{aligned}
r^{2n}
&=\abs{\sum_{j=0}^{n-1}c_j\zeta^j}^2\\
&\leq\left(\sum_{j=0}^{n-1}\abs{c_j}r^j\right)^2\\
&\leq C\sum_{j=0}^{n-1}r^{2j}
=C\frac{r^{2n}-1}{r^2-1}.
\end{aligned}
$$
Since $r>1$, multiplying by $r^2-1$ and dividing by $r^{2n}$ yields
$$
r^2-1\leq C(1-r^{-2n})<C.
$$
The last inequality is strict because $C>0$ and $r^{-2n}>0$.
Consequently $r^2<1+C$, and taking nonnegative square roots proves the claim.
:::

<1>4. Q.E.D.

::: {.proof}
Since $C\geq0$ and $r\geq0$, steps <1>1--<1>3 cover every case and show
that $\abs{\zeta}<\sqrt{1+C}$. The zero $\zeta$ was arbitrary, so every
zero lies in the stated open disk.
:::
:::
