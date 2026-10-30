---
schema: qual/card@1
id: P-BKS17-7B
kind: problem
title: Upper triangular solutions of $E^TR+R^TE=A$
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
  note: Restored spaces around inline math and normalized LaTeX against Sp17_Exam_0.pdf page 18 problem 7B.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: >-
    Independently reviewed the supplied Berkeley Spring 2017 triangular-splitting argument.
    The printed formula omits the final factor of $R$: multiplication gives
    $ER^{-1}=\operatorname{uph}(R^{-T}AR^{-1})$, hence
    $E=\operatorname{uph}(R^{-T}AR^{-1})R$. The solution below corrects this
    and gives the entries explicitly.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the transformed equation, symmetry of $R^{-T}AR^{-1}$, the unique upper-triangular splitting, and the resulting entry formula for $E$.
---

::: {.problem}
Suppose $R$ is an invertible upper triangular complex matrix and $A$ is symmetric. Find an explicit formula for the entries of the upper triangular matrix $E$ satisfying

$$
E^T R + R^T E = A
$$

and show that your solution is unique. Hint: Multiply by $R^{-1T}$ and $R^{-1}$.
:::

::: {.solution}

Set
$$
C\coloneqq R^{-T}AR^{-1}.
$$

::: pf

::: {.pf-step #s1-1}

If
$$
X\coloneqq ER^{-1},
$$
then $E$ is upper triangular exactly when $X$ is upper triangular, and the required equation is equivalent to
$$
X^T+X=C.
$$


::: pf-proof

Since $R$ is invertible upper triangular, both $R^{-1}$ and $R$ are upper triangular. Thus multiplication by $R^{-1}$ gives a bijection from upper triangular matrices $E$ to upper triangular matrices $X$, with inverse $E=XR$.

Multiplying
$$
E^TR+R^TE=A
$$
on the left by $R^{-T}$ and on the right by $R^{-1}$ gives
$$
R^{-T}E^T+ER^{-1}=R^{-T}AR^{-1}.
$$
Because
$$
R^{-T}E^T=(ER^{-1})^T=X^T,
$$
this is precisely $X^T+X=C$.

:::

:::

::: {.pf-step #s1-2}

The matrix $C$ is symmetric, and there is a unique upper triangular matrix $X$ satisfying $X^T+X=C$; its entries are
$$
X_{ij}
=
\begin{cases}
C_{ij}, & i<j,\\
\frac12 C_{ii}, & i=j,\\
0, & i>j.
\end{cases}
$$


::: pf-proof

Since $A^T=A$,
$$
C^T
=(R^{-T}AR^{-1})^T
=R^{-T}A^TR^{-1}
=C.
$$
Now let $X$ be upper triangular. If $i<j$, then $X_{ji}=0$, so the $(i,j)$ entry of $X^T+X=C$ forces $X_{ij}=C_{ij}$. If $i=j$, it forces $2X_{ii}=C_{ii}$. If $i>j$, upper triangularity already forces $X_{ij}=0$. Thus every entry of $X$ is forced by the displayed formula. Conversely, because $C$ is symmetric, that formula gives an upper triangular $X$ whose transpose plus itself is exactly $C$. Hence existence and uniqueness both hold.

:::

:::

::: {.pf-step #s1-3}

The unique required matrix is $E=XR$, where $X$ is given in step [](#s1-2){.pf-ref}. Equivalently, its entries are
$$
\boxed{
E_{ij}
=
\begin{cases}
\displaystyle
\frac12 C_{ii}R_{ij}
+\sum_{k=i+1}^{j}C_{ik}R_{kj}, & i\leq j,\\
0, & i>j,
\end{cases}
\qquad
C=R^{-T}AR^{-1}
}.
$$


::: pf-proof

Since $E=XR$ and both factors are upper triangular, $E_{ij}=0$ for $i>j$. For $i\leq j$,
$$
E_{ij}
=
\sum_{k=i}^{j}X_{ik}R_{kj}
=
\frac12 C_{ii}R_{ij}
+\sum_{k=i+1}^{j}C_{ik}R_{kj},
$$
using step [](#s1-2){.pf-ref}. Step [](#s1-1){.pf-ref} shows that this $E$ satisfies the original equation. Uniqueness of $X$ in step [](#s1-2){.pf-ref} and the bijection $E\leftrightarrow ER^{-1}$ in step [](#s1-1){.pf-ref} imply uniqueness of $E$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the explicit entries and proves existence and uniqueness.

:::

:::

:::
