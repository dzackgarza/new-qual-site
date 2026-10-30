---
schema: qual/card@1
id: P-BKS06-7A
kind: problem
title: Elements of $\operatorname{SL}(2,\RR)$ without real eigenvalues are conjugate to rotations
classification:
  areas: [prelim]
  topics:
  - Linear Algebra
relations: []
review: draft
---

::: {.problem}
Recall that $\SL(2, \RR)$ denotes the group of real $2 \times 2$ matrices of determinant $1$. Suppose that $A \in \SL(2, \RR)$ does not have a real eigenvalue.
Show that there exists $B \in \SL(2, \RR)$ such that $B A B^{-1}$ equals a rotation matrix $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ for some $\theta \in \RR$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The eigenvalues of $A$ are $e^{\pm i\theta}$ for some $\theta\in\RR$ with $\sin\theta\ne0$.

::: pf-proof

The characteristic polynomial of $A$ is real, so its roots are $\lambda$ and $\bar\lambda$, and $\lambda\notin\RR$ by hypothesis. Then $\abs{\lambda}^2=\lambda\bar\lambda=\det A=1$, so $\lambda=e^{i\theta}$ with $\sin\theta\ne0$.

:::

:::

::: {.pf-step #s2}

Let $v=a+ib$, with $a,b\in\RR^2$, be an eigenvector of $A$ for $e^{i\theta}$, and let $C$ be the matrix with columns $b$ and $a$. Then $C$ is invertible and $AC=CR_\theta$, where $R_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$.

::: pf-proof

Comparing real and imaginary parts of $A(a+ib)=(\cos\theta+i\sin\theta)(a+ib)$ gives
$$
Ab=(\cos\theta)\,b+(\sin\theta)\,a,\qquad Aa=(-\sin\theta)\,b+(\cos\theta)\,a,
$$
which is $AC=CR_\theta$ column by column. If $a$ and $b$ were linearly dependent over $\RR$, then $v=cw$ for some $c\in\CC$ and a real vector $w\ne0$, and $Aw=e^{i\theta}w$ with $Aw$ real would force $e^{i\theta}\in\RR$, contradicting step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

We may take $d=\det C>0$.

::: pf-proof

If $d<0$, replace $\theta$ by $-\theta$ and $v$ by $\bar v=a-ib$, which is an eigenvector for $e^{-i\theta}$. The columns become $-b$ and $a$, and the determinant becomes $-d>0$.

:::

:::

::: pf-qed

Put $B=\sqrt d\,C^{-1}$. Then $\det B=d\cdot d^{-1}=1$, so $B\in\SL(2,\RR)$, and by step [](#s2){.pf-ref}, $BAB^{-1}=C^{-1}AC=R_\theta$.

:::

:::

:::
