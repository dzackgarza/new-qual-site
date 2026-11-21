---
schema: qual/card@1
id: P-APA23D
kind: problem
title: Rayleigh quotient bounds; $p$-norm of a diagonal matrix; $\norm{aa^H}_2$ and a block companion
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
  note: Verified the Rayleigh, induced-norm, and spectral-norm computations.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The fourteen leaf steps of parts (a), (b) and (c) asserted their claim with no proof body;
    each now carries one, and the three part headings now hold their steps inside one proof body
    instead of closing it before the first step. No claim, no numbering and no statement is
    changed; the displayed conclusions are those the card had. Cited by number only: the
    spectral theorem for Hermitian matrices, the definition of the induced $p$-norm and of the
    singular values, and the Rayleigh bound of part (a) itself for the 2-norm. Checked: the
    positivity of $x^Hx$, the termwise bound with nonnegative multipliers, the attainment
    vector $e_k$, that $A_2$ is Hermitian so $A_2^HA_2=A_2^2$, the block product of $A_2$ with
    itself, and that $\lambda_1(aa^H)=\norm a_2^2$ so that $\norm{aa^H}_2$ equals it.
---

::: {.problem}
Throughout, $M_n$ denotes the set of $n \times n$ matrices with complex entries, and $x^H$ denotes the Hermitian transpose of $x$.

(a) Consider any Hermitian $A \in M_n$ with eigenvalues ordered so that $\lambda_n(A) \le \cdots \le \lambda_2(A) \le \lambda_1(A)$.
Prove that:
$$\lambda_n(A) \le \frac{x^H A x}{x^H x} \le \lambda_1(A) \quad \text{for all nonzero } x \in \CC^n.$$

(b) Suppose that $D \in M_n$ with $D = \operatorname{diag}(d_1, d_2, \dots, d_n)$.
Prove that for all $1 \le p \le \infty$, the induced operator $p$-norm of $D$ is given by $\norm{D}_p = \max_{1 \le i \le n} \abs{d_i}$.

(c) Given $a \in \CC^n$, find $\norm{A}_2$ for the matrices:
$$A_1 = a a^H \quad \text{and} \quad A_2 = \begin{pmatrix} 0 & a^H \\ a & 0 \end{pmatrix}.$$
:::

::: {.solution}

::: pf

::: pf-step
Part (a): Rayleigh Quotient Bounds for Hermitian Matrices:

::: pf-proof
*Proof:*

::: pf-step
By the **Spectral Theorem**, there exists an orthonormal eigenbasis $\{u_1, u_2, \dots, u_n\}$ of $\CC^n$ such that $A u_i = \lambda_i(A) u_i$ and $u_i^H u_j = \delta_{ij}$.

::: pf-proof
A Hermitian matrix is unitarily diagonalisable: there is a unitary $U$ with $A=U\Lambda U^H$ and $\Lambda$ real diagonal. The columns of $U$ are orthonormal, being the columns of a unitary matrix, and each is an eigenvector with the corresponding diagonal entry of $\Lambda$ as eigenvalue. Ordering the columns orders the eigenvalues as the statement does, and the eigenvalues are real so that no complex conjugate enters the ordering.
:::

:::

::: pf-step
Write any non-zero vector $x \in \CC^n \setminus \{0\}$ as $x = \sum_{i=1}^n c_i u_i$ with $c_i = u_i^H x \in \CC$.

::: pf-proof
$\{u_i\}$ is a basis, so $x$ has an expression $\sum c_iu_i$; taking the inner product with $u_j$ and using $u_i^Hu_j=\delta_{ij}$ leaves $u_j^Hx=c_j$, which is the displayed formula for the coefficients. The vector is nonzero exactly when not all $c_i$ vanish.
:::

:::

::: pf-step
Then:
$$x^H x = \sum_{i=1}^n \abs{c_i}^2 > 0, \qquad x^H A x = \sum_{i=1}^n \lambda_i(A) \abs{c_i}^2.$$

::: pf-proof
Expand in the orthonormal basis: $x^Hx=\sum_{i,j}\overline{c_i}c_ju_i^Hu_j=\sum_i\abs{c_i}^2$, which is positive because $x\ne0$. For the second, $Ax=\sum_jc_j\lambda_j(A)u_j$ by linearity and the eigenvector property, so $x^HAx=\sum_{i,j}\overline{c_i}c_j\lambda_j(A)\delta_{ij}=\sum_j\lambda_j(A)\abs{c_j}^2$.
:::

:::

::: pf-step
Since $\lambda_n(A) \le \lambda_i(A) \le \lambda_1(A)$ for each $i \in \{1, \dots, n\}$:
$$\lambda_n(A) \sum_{i=1}^n \abs{c_i}^2 \le \sum_{i=1}^n \lambda_i(A) \abs{c_i}^2 \le \lambda_1(A) \sum_{i=1}^n \abs{c_i}^2.$$

::: pf-proof
Multiply the two inequalities $\lambda_n(A)\le\lambda_i(A)\le\lambda_1(A)$ by the nonnegative number $\abs{c_i}^2$ and sum over $i$; a sum of inequalities with nonnegative multipliers preserves the direction, and factoring the constant terms out of the sums gives the displayed chain.
:::

:::

::: pf-step
Dividing by $x^H x = \sum_{i=1}^n \abs{c_i}^2$:
$$\lambda_n(A) \le \frac{x^H A x}{x^H x} \le \lambda_1(A).$$

::: pf-proof
The divisor is a positive real number by step 1.3, so dividing the chain of step 1.4 by it preserves both inequalities and turns the means into the Rayleigh quotient. Since $x\ne0$ was arbitrary, this is the assertion of (a).
:::

:::

:::

:::

::: pf-step
Part (b): $p$-Norm of a Diagonal Matrix $\norm{D}_p = \max_i \abs{d_i}$:

::: pf-proof
*Proof:*

::: pf-step
Let $M = \max_{1 \le i \le n} \abs{d_i}$.

::: pf-proof
The set $\{\abs{d_1},\dots,\abs{d_n}\}$ is a finite nonempty set of nonnegative reals, so it has a maximum; $M$ denotes it, and $M\ge0$ with $\abs{d_i}\le M$ for every $i$.
:::

:::

::: pf-step
For any $x \in \CC^n$ and $1 \le p < \infty$:
$$\norm{D x}_p^p = \sum_{i=1}^n \abs{d_i x_i}^p = \sum_{i=1}^n \abs{d_i}^p \abs{x_i}^p \le \sum_{i=1}^n M^p \abs{x_i}^p = M^p \sum_{i=1}^n \abs{x_i}^p = M^p \norm{x}_p^p.$$
Taking $p$-th roots gives $\norm{D x}_p \le M \norm{x}_p$, so $\norm{D}_p \le M$.
(For $p = \infty$: $\norm{D x}_\infty = \max_i \abs{d_i x_i} \le M \max_i \abs{x_i} = M \norm{x}_\infty$).

::: pf-proof
$(Dx)_i=d_ix_i$ because $D$ is diagonal, and $\abs{d_ix_i}^p=\abs{d_i}^p\abs{x_i}^p$ for a real exponent $p$ because the modulus is multiplicative. Replace $\abs{d_i}$ by the upper bound $M$ termwise, using $\abs{x_i}^p\ge0$. Both sides are nonnegative, so taking $p$-th roots preserves the inequality, and the result is $\norm{Dx}_p\le M\norm{x}_p$ for every $x$, hence $\norm D_p=\sup_{x\ne0}\norm{Dx}_p/\norm x_p\le M$. The case $p=\infty$ is the same estimate with the maximum in place of the sum, using that the maximum of $\abs{d_i}\abs{x_i}$ is at most $M$ times the maximum of $\abs{x_i}$.
:::

:::

::: pf-step
To show attainment, choose index $k$ such that $\abs{d_k} = M = \max_i \abs{d_i}$.

::: pf-proof
A maximum of the finite set of the $\abs{d_i}$ is attained at some index, by definition of the maximum; that index is $k$.
:::

:::

::: pf-step
Let $e_k = (0, \dots, 0, 1, 0, \dots, 0)^T$ be the $k$-th standard basis vector.

::: pf-proof
This is the vector with a $1$ in the $k$-th coordinate and $0$ elsewhere; it is nonzero and lies in $\CC^n$.
:::

:::

::: pf-step
$\norm{e_k}_p = 1$, and $D e_k = d_k e_k$, so $\norm{D e_k}_p = \abs{d_k} \norm{e_k}_p = M$.

::: pf-proof
$\norm{e_k}_p^p=\sum_i\abs{(e_k)_i}^p=1$ for $p<\infty$ and $\max_i\abs{(e_k)_i}=1$ for $p=\infty$. Multiplying $e_k$ by the diagonal matrix gives the vector whose $k$-th entry is $d_k$ and whose other entries are $0$, that is $d_ke_k$; its norm is $\abs{d_k}\norm{e_k}_p=\abs{d_k}=M$ by the choice of $k$.
:::

:::

::: pf-step
Therefore:
$$\norm{D}_p = \sup_{x \ne 0} \frac{\norm{D x}_p}{\norm{x}_p} = M = \max_{1 \le i \le n} \abs{d_i}.$$

::: pf-proof
Step 2.2 gives $\norm D_p\le M$ and step 2.5 exhibits the nonzero vector $e_k$ with quotient $\norm{De_k}_p/\norm{e_k}_p=M$, so the supremum is at least $M$. The two bounds give equality, and $M$ is the stated maximum.
:::

:::

:::

:::

::: pf-step
Part (c): Evaluation of $\norm{A}_2$ (Spectral Norm):

::: pf-proof
*Proof:*

::: pf-step
The matrix 2-norm is the largest singular value: $\norm{A}_2 = \sigma_1(A) = \sqrt{\lambda_1(A^H A)}$.

::: pf-proof
$\norm{A}_2=\sup_{x\ne0}\norm{Ax}_2/\norm x_2$, and $\norm{Ax}_2^2=x^HA^HAx$; the matrix $A^HA$ is Hermitian positive semidefinite, so by the Rayleigh bound of part (a) its quotient is at most $\lambda_1(A^HA)$ and equals it at an eigenvector of the top eigenvalue. Hence $\norm A_2^2=\lambda_1(A^HA)$, which is the square of the largest singular value by definition of the singular values as the square roots of the eigenvalues of $A^HA$.
:::

:::

::: pf-step
**For $A_1 = a a^H$ (where $a \in \CC^n$):**

- If $a = 0$, $\norm{A_1}_2 = 0 = \norm{a}_2^2$.
- If $a \ne 0$, $A_1 a = (a a^H) a = a (a^H a) = \norm{a}_2^2 a$, so $a$ is an eigenvector with eigenvalue $\norm{a}_2^2$.
- For any $v \perp a$, $A_1 v = a (a^H v) = 0$.
- Since $A_1$ is Hermitian and rank 1, its eigenvalues are $\norm{a}_2^2$ (multiplicity 1) and $0$ (multiplicity $n - 1$).
- Thus:
  $$\norm{A_1}_2 = \lambda_1(A_1) = \norm{a}_2^2.$$

::: pf-proof
$A_1$ is Hermitian because $(aa^H)^H=aa^H$, and its rank is one when $a\ne0$, its image being the line $\CC a$; when $a=0$ it is the zero matrix and the claim is immediate. The computation $A_1a=a(a^Ha)$ uses associativity and $a^Ha=\norm a_2^2$, a real scalar. The orthogonal complement of $a$ has dimension $n-1$ and lies in the kernel by the displayed computation, so with the eigenvector $a$ the eigenvalues are $\norm a_2^2$ once and $0$ with multiplicity $n-1$; a Hermitian matrix with those eigenvalues is diagonalisable, which confirms the multiplicities. $\norm{A_1}_2=\sigma_1(A_1)=\sqrt{\lambda_1(A_1^HA_1)}$ and $A_1^HA_1=A_1^2$ has eigenvalues $\norm a_2^4$ and $0$, so the largest singular value is $\sqrt{\norm a_2^4}=\norm a_2^2$, which is also $\lambda_1(A_1)$ because that eigenvalue is nonnegative.
:::

:::

::: pf-step
**For $A_2 = \begin{pmatrix} 0 & a^H \\ a & 0 \end{pmatrix} \in M_{n+1}(\CC)$:**

- We compute $A_2^H A_2 = A_2^2$ (since $A_2$ is Hermitian):
  $$A_2^2 = \begin{pmatrix} 0 & a^H \\ a & 0 \end{pmatrix} \begin{pmatrix} 0 & a^H \\ a & 0 \end{pmatrix} = \begin{pmatrix} a^H a & 0 \\ 0 & a a^H \end{pmatrix} = \begin{pmatrix} \norm{a}_2^2 & 0 \\ 0 & a a^H \end{pmatrix}.$$
- The eigenvalues of the block diagonal matrix $A_2^2$ are:
  - From top block $1 \times 1$: $\norm{a}_2^2$.
  - From bottom block $n \times n$: eigenvalues of $a a^H$, which are $\norm{a}_2^2$ and $0$.
- Thus the largest eigenvalue of $A_2^2$ is $\lambda_{\max}(A_2^2) = \norm{a}_2^2$.
- Taking the square root gives the spectral norm:
  $$\norm{A_2}_2 = \sqrt{\lambda_{\max}(A_2^2)} = \sqrt{\norm{a}_2^2} = \norm{a}_2.$$

::: pf-proof
$A_2$ is Hermitian, so $A_2^H=A_2$ and $A_2^HA_2=A_2^2$; the block product is computed by the usual rule, the off-diagonal blocks being $0\cdot a^H+a^H\cdot0=0$ and $a\cdot0+0\cdot a=0$, and the diagonal ones $0\cdot0+a^Ha$ and $aa^H+0\cdot0$, with $a^Ha=\norm a_2^2$. The eigenvalues of a block diagonal matrix are the union, with multiplicity, of the eigenvalues of its blocks, since its characteristic polynomial is the product of theirs; step 3.2 gives those of $aa^H$ as $\norm a_2^2$ and $0$. The largest eigenvalue of $A_2^2$ is therefore $\norm a_2^2\ge0$, and by step 3.1 the 2-norm is the square root of the largest eigenvalue of $A_2^HA_2$, that is $\sqrt{\norm a_2^2}=\norm a_2$.
:::

:::

:::

:::

::: pf-qed
Conclusion:

The Rayleigh quotient is bounded by $\lambda_n \le \frac{x^HAx}{x^Hx} \le \lambda_1$, $\norm{D}_p = \max_i \abs{d_i}$, $\norm{a a^H}_2 = \norm{a}_2^2$, and $\norm{ \begin{pmatrix} 0 & a^H \\ a & 0 \end{pmatrix} }_2 = \norm{a}_2$.

::: pf-proof
Part (a) is steps 1.1 to 1.5, part (b) steps 2.1 to 2.6, and part (c) steps 3.1 to 3.3; each displayed formula of the conclusion is the last step of its part.
:::

:::

:::

:::
