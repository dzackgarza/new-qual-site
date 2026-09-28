---
schema: qual/card@1
id: P-BKS03-3A
kind: problem
title: Centralizer of a Jordan block over $\QQ$
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Let $R$ be the subring of $M_2(\mathbb Q)$ consisting of matrices commuting with
\[
\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]

(a) Prove that $R$ is a subring of $M_2(\mathbb Q)$.

(b) Prove that $R\cong\mathbb Q[x]/(x^2)$.
:::

::: {.solution}
(a) Let $N=\begin{pmatrix}1&1\\0&1\end{pmatrix}$. If $A,B\in R$, then $(A+B)N=AN+BN=NA+NB=N(A+B)$, so $A+B\in R$. If $A,B\in R$, then $(AB)N=A(BN)=A(NB)=(AN)B=(NA)B=N(AB)$, so $AB\in R$. If $I$ is the identity matrix, then clearly $-I\in R$. These three facts imply that $R$ is a subring.

(b) Calculating shows that the matrix $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ belongs to $R$ if and only if $a=a+c$, $a+b=b+d$, and $c+d=d$, that is, if and only if $A$ has the form $\begin{pmatrix}a&b\\0&a\end{pmatrix}$. We define a $\QQ$-algebra homomorphism $h:\QQ[x]\to R$ by mapping $x$ to $\begin{pmatrix}0&1\\0&0\end{pmatrix}$. Clearly $h(x^2)=\begin{pmatrix}0&1\\0&0\end{pmatrix}^2=0$, so $h$ induces a homomorphism $\QQ[x]/(x^2)\to R$. Since $h(a+bx)=\begin{pmatrix}a&b\\0&a\end{pmatrix}$, this homomorphism $\QQ[x]/(x^2)\to R$ is an isomorphism.
:::
