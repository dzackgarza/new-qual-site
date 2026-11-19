---
schema: qual/card@1
id: E-HK-IF5V
kind: problem
title: Solutions to a homogeneous system over $\CC$
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the three containers state why their subclaims suffice, and the 12
    leaf steps that asserted a claim with no justification each carry a sentence deriving it. The Goal
    paragraph before the proof was removed and the solution vector is boxed in the concluding step. The
    mathematics is unchanged: det A = (1-i)^2 + 2i = 0, the first row multiplied by 1+i is the second, and
    the single equation gives x_2 = -(1+i)x_1, checked by substituting into the second equation. Checked
    against Hungerford, Algebra, section 1.3, the exercise as printed on the card. Nothing in the
    statement was changed.
---

::: {.exercise}
Find all solutions in $\CC^2$ to the homogeneous linear system:
$$
\begin{aligned}
(1 - i) x_1 - i x_2 &= 0 \\
2 x_1 + (1 - i) x_2 &= 0.
\end{aligned}
$$
:::

::: {.solution}

::: pf

::: pf-step
Matrix Form and Determinant Computation:

::: pf-proof
The subclaims assemble the coefficient matrix, compute its determinant, and record what singularity gives.

::: pf-step
The system can be written as $A x = 0$ where $x = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \in \CC^2$ and:
$$A = \begin{bmatrix} 1 - i & -i \\ 2 & 1 - i \end{bmatrix}.$$

::: pf-proof
Collecting the coefficients of $x_1$ and $x_2$ in the two equations produces the displayed matrix, and both right-hand sides are $0$.
:::

:::

::: pf-step
We compute the determinant of the coefficient matrix $A$:
$$\det(A) = (1 - i)(1 - i) - (-i)(2) = (1 - i)^2 + 2i.$$

::: pf-proof
The determinant of a $2\times2$ matrix is $ad-bc$, here $(1-i)(1-i)-(-i)\cdot2$.
:::

:::

::: pf-step
Expanding the complex square:
$$(1 - i)^2 = 1 - 2i + i^2 = 1 - 2i - 1 = -2i.$$

::: pf-proof
Multiply out $(1-i)(1-i)=1-2i+i^2$ and use $i^2=-1$.
:::

:::

::: pf-step
Substituting this into the determinant:
$$\det(A) = -2i + 2i = 0.$$

::: pf-proof
Substituting the value just computed for $(1-i)^2$ into the expression for the determinant.
:::

:::

::: pf-step
Since $\det(A) = 0$, the matrix $A$ is singular ($\operatorname{rank}(A) < 2$), so the system has non-trivial solutions.

::: pf-proof
A square matrix over a field is invertible exactly when its determinant is non-zero, so $A$ has rank less than $2$ and its kernel is non-trivial; any non-zero element of the kernel is a non-trivial solution.
:::

:::

:::

:::

::: pf-step
Row Reduction and Parametric Solution:

::: pf-proof
The subclaims show that the two equations coincide and solve the single equation that remains.

::: pf-step
Multiplying the first equation by $(1 + i)$:
$$(1 + i)(1 - i) x_1 - (1 + i) i x_2 = 0 \implies 2 x_1 - (i - 1) x_2 = 0 \implies 2 x_1 + (1 - i) x_2 = 0.$$

::: pf-proof
Multiplying an equation by the non-zero number $1+i$ gives an equivalent equation; $(1+i)(1-i)=1-i^2=2$ and $(1+i)i=i+i^2=i-1$, whose negative is $1-i$.
:::

:::

::: pf-step
This is identical to the second equation! Thus the second row is linearly dependent on the first.

::: pf-proof
The equation obtained is exactly the second equation of the system, so the second row of $A$ is the first row multiplied by $1+i$, a non-zero number.
:::

:::

::: pf-step
The single independent equation is:
$$(1 - i) x_1 - i x_2 = 0 \implies i x_2 = (1 - i) x_1.$$

::: pf-proof
The second row being a multiple of the first, the system is equivalent to the first equation alone, and moving $-ix_2$ to the right-hand side gives the displayed relation.
:::

:::

::: pf-step
Multiplying both sides by $-i$ (since $-i \cdot i = 1$):
$$x_2 = -i (1 - i) x_1 = (-i - 1) x_1 = -(1 + i) x_1.$$

::: pf-proof
$-i\cdot i=-i^2=1$ isolates $x_2$, and $-i(1-i)=-i+i^2=-i-1=-(1+i)$.
:::

:::

::: pf-step
Setting $x_1 = t \in \CC$ as the free parameter:
$$x_2 = -(1 + i) t.$$

::: pf-proof
Every complex value of $x_1$ determines $x_2$ by the preceding formula, and $t$ names that value.
:::

:::

:::

:::

::: pf-step
Solution Space:

::: pf-proof
The single subclaim collects the parametric description as a complex span.

::: pf-step
The complete solution set is the 1-dimensional complex subspace:
$$\operatorname{Sol} = \left\{ t \begin{bmatrix} 1 \\ -(1 + i) \end{bmatrix} \;\st\; t \in \CC \right\} = \operatorname{span}_\CC \left\{ \begin{bmatrix} 1 \\ -1 - i \end{bmatrix} \right\}.$$

::: pf-proof
The preceding container expresses every solution as the scalar multiple $t(1,-(1+i))$, and every such multiple satisfies the single equation; the set of those multiples is by definition the complex span of the displayed vector.
:::

:::

:::

:::

::: pf-step
Conclusion:
The solutions are all scalar multiples $x = \boxed{t \begin{bmatrix} 1 \\ -1 - i \end{bmatrix}}$ for $t \in \CC$.

::: pf-proof
The third container identifies the solution set with that span, and $-(1+i)=-1-i$ is the second coordinate of its spanning vector.
:::

:::

:::

:::
