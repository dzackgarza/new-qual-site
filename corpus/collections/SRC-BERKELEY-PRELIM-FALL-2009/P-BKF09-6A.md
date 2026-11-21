---
schema: qual/card@1
id: P-BKF09-6A
kind: problem
title: Finite continued fractions as ratios of determinants
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the omitted definition of Delta_n as a tridiagonal determinant, completing the truncated statement, against f09solutions.pdf page 3 problem 6A.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the tridiagonal recurrence, the cross-multiplied form of
    the continued fraction $C_{n}$, and the induction. The card's own division by $\Delta_{n-1}$ is replaced
    by an identity that holds whether or not $\Delta_{n-1}$ vanishes; the displayed quotient then follows
    whenever the denominator is nonzero. No retained solution set covers this exercise, so the argument is
    the card's own.
---

::: {.problem}
For $n \geq 1$, prove that

$$
a_n + \cfrac{1}{a_{n-1} + \cfrac{1}{\cdots + \cfrac{1}{a_1 + \cfrac{1}{a_0}}}} = \frac{\Delta_n}{\Delta_{n-1}},
$$

where

$$
\Delta_n = \begin{vmatrix}
a_0 & 1 & 0 & \cdots & 0 \\
-1 & a_1 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \ddots & \vdots \\
0 & \cdots & -1 & a_{n-1} & 1 \\
0 & \cdots & 0 & -1 & a_n
\end{vmatrix}.
$$
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own. Write $C_{n}$ for the continued fraction of the statement, $C_{0}=a_{0}$ and $C_{n}=a_{n}+1/C_{n-1}$, and $\Delta_{n}$ for the displayed tridiagonal determinant, with $\Delta_{0}=a_{0}$. The identity proved below is $\Delta_{n}=C_{n}\Delta_{n-1}$ for $n\ge1$; dividing by $\Delta_{n-1}$ when that is nonzero gives the displayed quotient.

::: pf

::: {.pf-step #recurrence}
$\Delta_{n}=a_{n}\Delta_{n-1}+\Delta_{n-2}$ for $n\ge2$.

::: pf-proof
Expand $\Delta_{n}$ along its last row, which is $(0,\dots,0,-1,a_{n})$. The entry $a_{n}$ in position $(n,n)$ contributes $a_{n}$ times the minor obtained by deleting the last row and column, which is exactly $\Delta_{n-1}$. The entry $-1$ in position $(n,n-1)$ contributes $(-1)^{n+(n-1)}(-1)$ times its minor, and $(-1)^{2n-1}=-1$ so the sign in front makes the contribution $+1$ times that minor, which is the determinant of the tridiagonal matrix built from $a_{0},\dots,a_{n-2}$, that is $\Delta_{n-2}$. All other entries of the last row vanish, so the two contributions are the whole expansion.
:::

:::

::: {.pf-step #base}
$\Delta_{1}=C_{1}\Delta_{0}$.

::: pf-proof
$\Delta_{0}=a_{0}$ and $\Delta_{1}=a_{0}a_{1}-(1)(-1)=a_{0}a_{1}+1$. And $C_{1}=a_{1}+1/a_{0}$, so $C_{1}\Delta_{0}=a_{0}a_{1}+1$ after multiplying out; the identity $C_{n}C_{n-1}=a_{n}C_{n-1}+1$ used here is the definition of $C_{n}$ cleared of fractions.
:::

:::

::: {.pf-step #step}
If $\Delta_{k}=C_{k}\Delta_{k-1}$ holds for all $1\le k<n$, then $\Delta_{n}=C_{n}\Delta_{n-1}$.

::: pf-proof
Clear the definition of $C_{n}$ of fractions: $C_{n}C_{n-1}=a_{n}C_{n-1}+1$. Multiplying by $\Delta_{n-2}$,
$$
C_{n}\bigl(C_{n-1}\Delta_{n-2}\bigr)=a_{n}\bigl(C_{n-1}\Delta_{n-2}\bigr)+\Delta_{n-2}.
$$
By the induction hypothesis the parentheses are $\Delta_{n-1}$, so the right side is $a_{n}\Delta_{n-1}+\Delta_{n-2}=\Delta_{n}$ by step [](#recurrence){.pf-ref}, and the left side is $C_{n}\Delta_{n-1}$. Hence $\Delta_{n}=C_{n}\Delta_{n-1}$.
:::

:::

::: {.pf-step}
Therefore $a_{n}+\dfrac{1}{a_{n-1}+\dfrac{1}{\cdots+\dfrac{1}{a_{0}}}}=\dfrac{\Delta_{n}}{\Delta_{n-1}}$ for every $n\ge1$ with $\Delta_{n-1}\ne0$.

::: pf-proof
By steps [](#base){.pf-ref} and [](#step){.pf-ref} induction gives $\Delta_{n}=C_{n}\Delta_{n-1}$ for every $n\ge1$, where $C_{n}$ is the continued fraction displayed on the left. When $\Delta_{n-1}\ne0$ this may be divided through, giving $C_{n}=\Delta_{n}/\Delta_{n-1}$, which is the assertion; and the cross-multiplied form $\Delta_{n}=C_{n}\Delta_{n-1}$ holds in all cases, including those where $\Delta_{n-1}=0$ and the quotient is undefined.
:::

:::

:::
:::
