---
schema: qual/card@1
id: P-5EROX
kind: problem
title: $AB-BA=A$ implies $\det A=0$ in characteristic zero, but not in characteristic
  $2$
classification:
  areas:
  - algebra
  topics:
  - Trace
  - Determinants
  - Matrices
relations: []
review: draft
---

::: {.problem}
Let $k$ be a field of characteristic zero and $A, B \in M_n(k)$ be two square $n\times n$ matrices over $k$ such that $AB - BA = A$.
Prove that $\det A = 0$.

Moreover, when the characteristic of $k$ is 2, find a counterexample to this statement.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

In characteristic zero, $AB-BA=A$ forces
$$
\boxed{\det A=0}.
$$


::: pf-proof

Suppose $A$ were invertible. Right multiplication of $AB-BA=A$ by $A^{-1}$ gives $ABA^{-1}-B=I_n$. Taking traces yields
$$
0=\operatorname{tr}(ABA^{-1})-\operatorname{tr}(B)=\operatorname{tr}(I_n)=n,
$$
where the first equality uses invariance of trace under conjugation. Because $n>0$ and $\operatorname{char}k=0$, this is impossible. Hence $A$ is singular.

:::

:::

::: {.pf-step #s1-2}

In characteristic two, there are invertible matrices satisfying $AB-BA=A$; one example is
$$
\boxed{A=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
B=\begin{pmatrix}0&0\\0&1\end{pmatrix}}.
$$


::: pf-proof

Here $A^2=I_2$, so $A$ is invertible. Direct multiplication gives
$$
AB=\begin{pmatrix}0&1\\0&0\end{pmatrix},
\qquad BA=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
$$
In characteristic two, subtraction equals addition, so $AB-BA=A$. Nevertheless $\det A=-1=1\neq0$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves the characteristic-zero assertion, and step [](#s1-2){.pf-ref} supplies the required characteristic-two counterexample.

:::

:::

:::
