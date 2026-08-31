---
schema: qual/card@1
id: P-TLBS5
kind: problem
title: A non-normal subgroup, and whether $\mathrm{SO}(2)\normal\mathrm{SL}_2(\RR)$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Matrix Groups
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(1) Give an interesting example of a non-normal subgroup in a familiar group.
(2) Is the rotation subgroup $\operatorname{SO}(2)$ normal inside the special linear group $\operatorname{SL}_2(\mathbb{R})$? Prove your assertion with an explicit calculation.
:::

::: solution
**Goal:** Provide an explicit non-normal subgroup example and prove that $\operatorname{SO}(2)$ is **not** normal in $\operatorname{SL}_2(\mathbb{R})$.

<1>1. Part 1: Familiar Examples of Non-Normal Subgroups:
::: {.proof}
<2>1. **Example 1 ($S_3$):** In the symmetric group $S_3 = \{e, (1\,2), (1\,3), (2\,3), (1\,2\,3), (1\,3\,2)\}$, the subgroup $H = \langle (1\,2) \rangle = \{e, (1\,2)\}$ has order 2 and index 3. Conjugating $(1\,2)$ by $(1\,2\,3)$ gives:
$$(1\,2\,3)(1\,2)(1\,2\,3)^{-1} = (1\,2\,3)(1\,2)(1\,3\,2) = (2\,3) \notin H.$$
Thus $H$ is not normal in $S_3$.
<2>2. **Example 2 (Matrix groups):** The group of diagonal matrices $D \subset \operatorname{GL}_2(\mathbb{R})$ is not normal, as conjugating by an upper triangular shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ produces off-diagonal entries.
:::

<1>2. Part 2: $\operatorname{SO}(2)$ is NOT Normal in $\operatorname{SL}_2(\mathbb{R})$:
::: {.proof}
<2>1. Recall the definition of the special orthogonal group:
$$\operatorname{SO}(2) = \left\{ R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \;\middle|\; \theta \in \mathbb{R} \right\} \subset \operatorname{SL}_2(\mathbb{R}).$$
<2>2. We test whether $g R_\theta g^{-1} \in \operatorname{SO}(2)$ for all $g \in \operatorname{SL}_2(\mathbb{R})$ and $R_\theta \in \operatorname{SO}(2)$.
<2>3. Choose the rotation by $\pi/2$:
$$J = R_{\pi/2} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \in \operatorname{SO}(2).$$
<2>4. Choose the diagonal scaling matrix $g \in \operatorname{SL}_2(\mathbb{R})$:
$$g = \begin{pmatrix} 2 & 0 \\ 0 & 1/2 \end{pmatrix} \in \operatorname{SL}_2(\mathbb{R}) \quad (\det(g) = 2 \cdot (1/2) = 1).$$
<2>5. Its inverse is:
$$g^{-1} = \begin{pmatrix} 1/2 & 0 \\ 0 & 2 \end{pmatrix}.$$
<2>6. Compute the conjugate $g J g^{-1}$:
$$g J g^{-1} = \begin{pmatrix} 2 & 0 \\ 0 & 1/2 \end{pmatrix} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1/2 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 0 & -2 \\ 1/2 & 0 \end{pmatrix} \begin{pmatrix} 1/2 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 0 & -4 \\ 1/4 & 0 \end{pmatrix}.$$
<2>7. We check if $M \coloneqq \begin{pmatrix} 0 & -4 \\ 1/4 & 0 \end{pmatrix}$ belongs to $\operatorname{SO}(2)$:
- A matrix in $\operatorname{SO}(2)$ must satisfy $M^T M = I_2$ (orthogonality), so its columns must have Euclidean norm 1.
- The first column of $M$ is $\begin{pmatrix} 0 \\ 1/4 \end{pmatrix}$, with norm $\|(0, 1/4)\|_2 = 1/4 \ne 1$.
- The second column has norm $\|(-4, 0)\|_2 = 4 \ne 1$.
<2>8. Thus $g J g^{-1} \notin \operatorname{SO}(2)$.
:::

<1>3. Geometric / Lie-Theoretic Rationale:
::: {.proof}
<2>1. $\operatorname{SO}(2)$ is a maximal compact subgroup of the non-compact simple Lie group $\operatorname{SL}_2(\mathbb{R})$.
<2>2. The only normal subgroups of $\operatorname{SL}_2(\mathbb{R})$ are its center $Z(\operatorname{SL}_2(\mathbb{R})) = \{\pm I_2\}$ and the whole group itself (since $\operatorname{PSL}_2(\mathbb{R})$ is a simple group).
<2>3. Because $\operatorname{SO}(2)$ has dimension 1 while $Z$ has dimension 0, $\operatorname{SO}(2)$ cannot be normal.
:::

<1>4. Conclusion:
::: {.proof}
$\operatorname{SO}(2)$ is not normal in $\operatorname{SL}_2(\mathbb{R})$ as shown by the explicit counterexample $g J g^{-1} = \begin{pmatrix} 0 & -4 \\ 1/4 & 0 \end{pmatrix} \notin \operatorname{SO}(2)$.
:::
:::
