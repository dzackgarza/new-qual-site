---
schema: qual/card@1
id: P-BLAR-04
kind: problem
title: Solve three matrix equations
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Review Problem 4 in the deterministic MinerU Flash extraction assets/attachments/Basic_Linear_Algebra_Review_extracted.md.
---

::: {.problem}
Find the solution or solutions, if they exist, for each system \(Ax=b\):

\[
\text{(a)}\quad
\begin{bmatrix}
3&3&4\\
3&5&9\\
5&9&17
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}1\\2\\4\end{bmatrix},
\]

\[
\text{(b)}\quad
\begin{bmatrix}3&1&2\\6&2&4\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}5\\2\end{bmatrix},
\]

\[
\text{(c)}\quad
\begin{bmatrix}3&1&2\\6&2&4\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\end{bmatrix}.
\]
:::

::: {.solution}

::: pf

::: pf-step
In part (a), the unique solution is
\[
\boxed{(x_1,x_2,x_3)=(1,-2,1)}.
\]

::: pf-proof
Subtracting the first equation from the second gives
\[
2x_2+5x_3=1.
\]
Multiplying the third equation by \(3\) and the first by \(5\), then subtracting, gives
\[
12x_2+31x_3=7.
\]
Subtracting six times the first of these two equations from the second gives \(x_3=1\). Hence \(x_2=-2\), and the original first equation then gives \(x_1=1\). Each elimination step is reversible, so this is the unique solution.
:::

:::

::: pf-step
In part (b), the solution set is \(\boxed{\varnothing}\).

::: pf-proof
The left side of the second equation is twice the left side of the first, whereas its right side is \(2\) rather than \(2\cdot5=10\). Thus the two equations are inconsistent.
:::

:::

::: pf-step
In part (c), the solution set is
\[
\boxed{\left\{s(1,-3,0)+t(0,-2,1):s,t\in\RR\right\}}.
\]

::: pf-proof
The second equation is twice the first, so the system is equivalent to
\[
3x_1+x_2+2x_3=0.
\]
Taking \(x_1=s\) and \(x_3=t\) gives \(x_2=-3s-2t\), and every pair \((s,t)\in\RR^2\) produces a solution. This is exactly the displayed set.
:::

:::

:::

:::
