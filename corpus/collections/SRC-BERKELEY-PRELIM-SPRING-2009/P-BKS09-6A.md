---
schema: qual/card@1
id: P-BKS09-6A
kind: problem
title: Dimension of the centralizer of a $2\times 2$ complex matrix
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with the Spring 2009 solution-packet extraction and independently reviewed the Jordan-form classification despite OCR damage in its displayed matrices.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently proved that the centralizer of every non-scalar 2-by-2 complex matrix is exactly span{I,A}.
---

::: {.problem}
Let $M _ { 2 } ( \mathbb { C } )$ be the set of $2 \times 2$ matrices over the complex numbers.
Given $A \in M _ { 2 } ( \mathbb { C } )$ , define $C ( A ) = \{ B \in M _ { 2 } ( \mathbb { C } ) : A B = B A \}$

(a) Prove that $C ( A )$ is a linear subspace of $M _ { 2 } ( \mathbb { C } )$ , for every A.

(b) Determine, with proof, all possible values of the dimension dim $C ( A )$

(c) Formulate a simple and explicit rule to find dim $C ( A )$ , given A. "Simple" means the rule should yield the answer with hardly any computational effort.
:::

::: {.solution}
<1>1. For every $A\in M_2(\CC)$, the set $C(A)$ is a complex linear
subspace of $M_2(\CC)$.

::: {.proof}
The zero matrix commutes with $A$. If $B,D\in C(A)$ and
$\lambda,\mu\in\CC$, then
$$
\begin{aligned}
A(\lambda B+\mu D)
&=\lambda AB+\mu AD\\
&=\lambda BA+\mu DA\\
&=(\lambda B+\mu D)A.
\end{aligned}
$$
Thus $C(A)$ is closed under linear combinations.
:::

<1>2. If $A$ is not a scalar matrix, there exists $v\in\CC^2$ such that
$v$ and $Av$ are linearly independent.

::: {.proof}
Suppose instead that $Av\in\CC v$ for every $v\in\CC^2$. Choose a basis
$e_1,e_2$. Then
$$
Ae_1=\lambda_1e_1,
\qquad
Ae_2=\lambda_2e_2
$$
for some scalars $\lambda_1,\lambda_2$. Since $A(e_1+e_2)$ must also be
a scalar multiple of $e_1+e_2$, one has $\lambda_1=\lambda_2$. Hence
$A=\lambda_1I$, contrary to the hypothesis. Therefore such a vector $v$
exists.
:::

<1>3. If $A$ is not scalar, then
$$
C(A)=\operatorname{span}_{\CC}\{I,A\}.
$$

::: {.proof}
Choose $v$ as in step <1>2. Then $(v,Av)$ is a basis of $\CC^2$. Let
$B\in C(A)$. There are unique $\alpha,\beta\in\CC$ such that
$$
Bv=\alpha v+\beta Av.
$$
Because $AB=BA$,
$$
B(Av)=A(Bv)=\alpha Av+\beta A^2v.
$$
The matrix $\alpha I+\beta A$ has exactly the same values on the basis
vectors:
$$
(\alpha I+\beta A)v=\alpha v+\beta Av
$$
and
$$
(\alpha I+\beta A)(Av)=\alpha Av+\beta A^2v.
$$
Thus $B=\alpha I+\beta A$. This proves
$C(A)\subseteq\operatorname{span}\{I,A\}$, while the reverse inclusion is
immediate because both $I$ and $A$ commute with $A$.
:::

<1>4. If $A$ is not scalar, then
$$
\dim_{\CC}C(A)=2.
$$

::: {.proof}
By step <1>3, $C(A)$ is spanned by $I$ and $A$. These two matrices are
linearly independent: a relation $\alpha I+\beta A=0$ with $\beta\neq0$
would make $A$ scalar, while $\beta=0$ then forces $\alpha=0$.
:::

<1>5. If $A$ is scalar, then
$$
\dim_{\CC}C(A)=4.
$$

::: {.proof}
If $A=\lambda I$, then every matrix commutes with $A$, so
$$
C(A)=M_2(\CC).
$$
The four matrix units form a basis of $M_2(\CC)$, hence its complex
dimension is $4$.
:::

<1>6. The possible dimensions and the requested rule are
$$
\boxed{
\dim_{\CC}C(A)=
\begin{cases}
4,&A\text{ is a scalar matrix},\\
2,&A\text{ is not a scalar matrix}.
\end{cases}
}
$$

::: {.proof}
Steps <1>4 and <1>5 give all possibilities. Thus determining whether the
off-diagonal entries of $A$ vanish and its two diagonal entries are equal
immediately determines the dimension.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>1 proves part (a), and step <1>6 proves parts (b) and (c).
:::
:::
