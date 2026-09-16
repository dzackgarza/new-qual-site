---
schema: qual/card@1
id: L-CD6QT
kind: lemma
title: Jordan form data from the minimal and characteristic polynomials
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Minimal and Characteristic Polynomials
  - Eigenvalues and Eigenvectors
relations: []
review: draft
---

::: {.lemma}
Let $k$ be a field and let $A\in\Mat_n(k)$ have characteristic polynomial $\chi_A(x)=\det(xI-A)$ that splits over $k$, with distinct eigenvalues $\lambda_1,\ldots,\lambda_r$.
Write
$$
\chi_A(x)=\prod_{i=1}^r(x-\lambda_i)^{m_i},\qquad\min_A(x)=\prod_{i=1}^r(x-\lambda_i)^{\ell_i},
$$
where $\min_A$ is the [[D-GK5SF|minimal polynomial]], and let $E_{\lambda_i}=\ker(A-\lambda_iI)$ be the eigenspace and $V^{\lambda_i}=\ker(A-\lambda_iI)^{m_i}$ the generalized eigenspace of $\lambda_i$.
The exponent $m_i$ is the algebraic multiplicity and $\dim E_{\lambda_i}$ the geometric multiplicity of $\lambda_i$.
In the Jordan canonical form $\JCF(A)$:

1. The roots of $\chi_A$ and of $\min_A$ are exactly the eigenvalues $\lambda_i$, and $1\le\ell_i\le m_i$.

2. $\ell_i$ is the size of the largest Jordan block with eigenvalue $\lambda_i$, and it is the least $j\ge1$ with $\ker(A-\lambda_iI)^j=\ker(A-\lambda_iI)^{j+1}$.

3. $m_i$ is the sum of the sizes of the Jordan blocks with eigenvalue $\lambda_i$, which is the number of times $\lambda_i$ appears on the diagonal of $\JCF(A)$, and $m_i=\dim V^{\lambda_i}$.

4. $\dim E_{\lambda_i}$ is the number of Jordan blocks with eigenvalue $\lambda_i$.

5. $A$ is diagonalizable over $k$ if and only if $\dim E_{\lambda_i}=m_i$ for every $i$, if and only if $\ell_i=1$ for every $i$.
:::

::: {.proof}
Choose a basis in which $A$ is the block diagonal matrix $\JCF(A)$, and let $J=J_s(\lambda)$ be one of its Jordan blocks, of size $s$.
Then $J-\lambda I$ sends the $j$th basis vector of the block to the $(j-1)$st and the first to $0$, so $\dim\ker(J-\lambda I)^j=\min(j,s)$, while $J-\mu I$ is invertible for $\mu\ne\lambda$.
In particular $\chi_J(x)=(x-\lambda)^s$, and $(x-\lambda)^j$ kills $J$ exactly when $j\ge s$, so $\min_J(x)=(x-\lambda)^s$.

The characteristic polynomial of a block diagonal matrix is the product of those of the blocks, which gives 3 and the first part of 1; the minimal polynomial is their least common multiple, which gives the first part of 2.
The inequality $\ell_i\le m_i$ is Cayley--Hamilton: $\min_A$ divides $\chi_A$.
Summing $\dim\ker(J-\lambda_iI)^j=\min(j,s)$ over the blocks with eigenvalue $\lambda_i$ shows that $\dim\ker(A-\lambda_iI)^j$ increases strictly for $j<\ell_i$ and is constant for $j\ge\ell_i$, and that $\dim V^{\lambda_i}=m_i$; taking $j=1$ gives 4, since the first basis vectors of the blocks with eigenvalue $\lambda_i$ form a basis of $E_{\lambda_i}$.
Finally, $A$ is diagonalizable if and only if every Jordan block has size $1$, which by 2, 3, and 4 is each of the two conditions in 5.
:::
