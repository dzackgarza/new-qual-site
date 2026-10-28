---
schema: qual/card@1
id: P-GREPT-37
kind: problem
title: "Parameter values making a $3\\times3$ linear system inconsistent"
classification:
  areas: [applied-algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 37 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
For how many values of the parameter, $k$, will the following system have no solutions?

$$\begin{aligned} kx + y + z &= 1 \\ x + ky + z &= k \\ x + y + kz &= k^2 \end{aligned}$$

(A) $0$
(B) $1$
(C) $2$
(D) $4$
(E) Infinitely many
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The determinant of the coefficient matrix is
$$
\det
\begin{pmatrix}
k&1&1\\
1&k&1\\
1&1&k
\end{pmatrix}
=(k-1)^2(k+2).
$$


::: pf-proof

The vector $(1,1,1)^T$ is an eigenvector with eigenvalue $k+2$. Every vector
whose coordinates sum to $0$ is an eigenvector with eigenvalue $k-1$, and
that subspace has dimension $2$. Hence the determinant, the product of the
three eigenvalues with multiplicity, is $(k+2)(k-1)^2$.

:::

:::

::: {.pf-step #s1-2}

If $k\ne1,-2$, the system has a unique solution.


::: pf-proof

By step [](#s1-1){.pf-ref} the coefficient matrix is invertible for these values of $k$.
An invertible coefficient matrix gives a unique solution for every right-hand
side, so such $k$ cannot yield an inconsistent system.

:::

:::

::: {.pf-step #s1-3}

For $k=1$, the system is consistent.


::: pf-proof

All three equations become
$$
x+y+z=1,
$$
because the right-hand sides are $1$, $k=1$, and $k^2=1$. Thus there are
infinitely many solutions, not zero solutions.

:::

:::

::: {.pf-step #s1-4}

For $k=-2$, the system is inconsistent.


::: pf-proof

Adding the three equations gives $0$ on the left, because the total
coefficient of each of $x,y,z$ is $-2+1+1=0$. The right side sums to
$$
1+(-2)+(-2)^2=3.
$$
Thus the system would require $0=3$, a contradiction.

:::

:::

::: {.pf-step #s1-5}

Therefore there is exactly
$$
\boxed{1}
$$
value of $k$ for which the system has no solutions, so the answer is (B).


::: pf-proof

Steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref} exhaust the singular and nonsingular cases identified in
step [](#s1-1){.pf-ref}. Only $k=-2$ is inconsistent.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the requested count.

:::

:::

:::
