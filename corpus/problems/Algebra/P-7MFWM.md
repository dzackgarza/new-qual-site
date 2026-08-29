---
schema: qual/card@1
id: P-7MFWM
kind: problem
title: If $\exp(A)=B\in\SL_n(\RR)$, must $A\in\SL_n(\RR)$?
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Determinants
  - Trace
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Say we can find a matrix $A \in M_n(\mathbb{R})$ such that $\exp(A) = B$ for $B \in \operatorname{SL}_n(\mathbb{R})$.
Does $A$ also have to be in $\operatorname{SL}_n(\mathbb{R})$?
Does $A$ have to satisfy $\operatorname{tr}(A) = 0$ (i.e. $A \in \mathfrak{sl}_n(\mathbb{R})$)?
:::

::: solution
**Goal:** Analyze the relationship between $\exp(A) = B \in \operatorname{SL}_n(\mathbb{R})$ and the conditions $A \in \operatorname{SL}_n(\mathbb{R})$ vs. $\operatorname{tr}(A) = 0$ ($A \in \mathfrak{sl}_n(\mathbb{R})$).

<1>1. Determinant of the matrix exponential (Jacobi's formula):
    *Proof:*
    <2>1. For any matrix $A \in M_n(\mathbb{R})$:
        $$\det(\exp(A)) = e^{\operatorname{tr}(A)}.$$
    <2>2. Since $B = \exp(A) \in \operatorname{SL}_n(\mathbb{R})$, we have $\det(B) = 1$.
    <2>3. Therefore:
        $$e^{\operatorname{tr}(A)} = 1.$$
    <2>4. Because $A$ is a real matrix, its trace $\operatorname{tr}(A) \in \mathbb{R}$ is a real number.
    <2>5. The only real number $x \in \mathbb{R}$ satisfying $e^x = 1$ is $x = 0$.
    <2>6. Thus $\operatorname{tr}(A) = 0$, which means $A \in \mathfrak{sl}_n(\mathbb{R})$ (the Lie algebra of $\operatorname{SL}_n(\mathbb{R})$).

<1>2. Does $A$ have to be in the group $\operatorname{SL}_n(\mathbb{R})$?
    *Proof:*
    <2>1. For $A$ to be in $\operatorname{SL}_n(\mathbb{R})$, we would need $\det(A) = 1$.
    <2>2. Having $\operatorname{tr}(A) = 0$ does **not** imply $\det(A) = 1$.
    <2>3. **Counterexample:**
        - Consider $n = 2$ and the traceless matrix $A = \begin{pmatrix} 0 & \pi \\ -\pi & 0 \end{pmatrix} \in \mathfrak{sl}_2(\mathbb{R})$.
        - $\operatorname{tr}(A) = 0 + 0 = 0$.
        - $\det(A) = 0 - (-\pi^2) = \pi^2 \ne 1$, so $A \notin \operatorname{SL}_2(\mathbb{R})$.
        - Computing $\exp(A)$: since $A = \pi \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, $\exp(A) = \begin{pmatrix} \cos\pi & \sin\pi \\ -\sin\pi & \cos\pi \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -I_2$.
        - $\det(\exp(A)) = \det(-I_2) = (-1)^2 = 1$, so $\exp(A) \in \operatorname{SL}_2(\mathbb{R})$.
        - Another counterexample: $A = 0 \in M_n(\mathbb{R})$ gives $\exp(0) = I_n \in \operatorname{SL}_n(\mathbb{R})$, but $\det(0) = 0 \ne 1$ for $n \ge 1$.

<1>3. Conclusion:
    $A$ must be in the Lie algebra $\mathfrak{sl}_n(\mathbb{R})$ (i.e. $\operatorname{tr}(A) = 0$), but $A$ does **not** have to be in the Lie group $\operatorname{SL}_n(\mathbb{R})$ (its determinant need not be 1). Q.E.D.
:::
