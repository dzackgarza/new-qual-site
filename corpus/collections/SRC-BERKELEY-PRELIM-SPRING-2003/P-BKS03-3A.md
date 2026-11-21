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
Let $R$ be the subring of $M_2(\QQ)$ consisting of matrices commuting with
$$
\begin{pmatrix}1&1\\0&1\end{pmatrix}.
$$

(a) Prove that $R$ is a subring of $M_2(\QQ)$.

(b) Prove that $R\cong\QQ[x]/(x^2)$.
:::

::: {.solution}

The argument is the card's own: $R$ is the centraliser of $N=\begin{pmatrix}1&1\\0&1\end{pmatrix}$, hence a subring, and its explicit shape is $\QQ[x]/(x^{2})$.

::: pf

::: {.pf-step #subring}

(a) $R=\{A\in M_{2}(\QQ):AN=NA\}$ is a subring of $M_{2}(\QQ)$.

::: pf-proof

$0$ and $I$ commute with $N$, so $I\in R$; in particular $R$ is nonempty. If $A,B\in R$ and $c\in\QQ$ then $(A+cB)N=AN+cBN=NA+cNB=N(A+cB)$, so $R$ is a $\QQ$-subspace of $M_{2}(\QQ)$. If $A,B\in R$ then $(AB)N=A(BN)=A(NB)=(AN)B=(NA)B=N(AB)$, so $R$ is closed under multiplication. A subset containing $1$ that is closed under subtraction and multiplication is a subring.

:::

:::

::: {.pf-step #shape}

$A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in R$ exactly when $A=\begin{pmatrix}a&b\\0&a\end{pmatrix}$.

::: pf-proof

Multiplying out, $AN=\begin{pmatrix}a&a+b\\c&c+d\end{pmatrix}$ and $NA=\begin{pmatrix}a+c&b+d\\c&d\end{pmatrix}$. Equality of the two matrices is the system $a=a+c$, $a+b=b+d$, $c=c$, $c+d=d$, which is $c=0$ and $d=a$. So $R$ consists exactly of the matrices $\begin{pmatrix}a&b\\0&a\end{pmatrix}$ with $a,b\in\QQ$.

:::

:::

::: {.pf-step #map}

The $\QQ$-algebra map $h:\QQ[x]\to M_{2}(\QQ)$ with $h(x)=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ has image $R$ and kernel $(x^{2})$.

::: pf-proof

$h$ is the unique $\QQ$-algebra map sending $x$ to the given matrix, and $h\bigl(\sum a_{i}x^{i}\bigr)=\sum a_{i}\begin{pmatrix}0&1\\0&0\end{pmatrix}^{i}$. Since $\begin{pmatrix}0&1\\0&0\end{pmatrix}^{2}=0$, the image consists of $a_{0}I+a_{1}\begin{pmatrix}0&1\\0&0\end{pmatrix}=\begin{pmatrix}a_{0}&a_{1}\\0&a_{0}\end{pmatrix}$, which is exactly $R$ by step [](#shape){.pf-ref}. The kernel contains $x^{2}$; conversely if $h(f)=0$ then $f$'s constant and linear coefficients vanish and, since $x^{2}\mapsto0$, also $f\in(x^{2})$.

:::

:::

::: {.pf-step #isomorphism}

(b) $R\cong\QQ[x]/(x^{2})$.

::: pf-proof

By the first isomorphism theorem for rings, $\QQ[x]/\ker h\cong\operatorname{im}h$. Step [](#map){.pf-ref} identifies the kernel as $(x^{2})$ and the image as $R$, so
$$
\boxed{R=\Bigl\{\begin{pmatrix}a&b\\0&a\end{pmatrix}:a,b\in\QQ\Bigr\}\cong\QQ[x]/(x^{2}).}
$$

:::

:::

:::
:::
