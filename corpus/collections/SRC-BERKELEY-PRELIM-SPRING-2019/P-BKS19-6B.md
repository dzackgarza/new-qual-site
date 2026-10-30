---
schema: qual/card@1
id: P-BKS19-6B
kind: problem
title: Moore determinant over $\ZZ/2$
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
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2019 Graduate Preliminary Examination.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2019 Moore-determinant argument. The divisibility and degree comparison are correct; the solution below also verifies explicitly that the determinant is nonzero, so the degree comparison is legitimate.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the Frobenius identity, column-operation divisibility by every nonzero linear form, pairwise nonassociateness of the factors, nonvanishing of the determinant, and equality by degree in the UFD $\ZZ_2[x_1,\ldots,x_n]$.
---

::: {.problem}
Let $\ZZ_2$ be the ring of integers modulo $2$.
Prove the identity in $\ZZ_2[x_1,\ldots,x_n]$
$$
\det\!\begin{pmatrix}
x_1&\cdots&x_n\\
x_1^2&\cdots&x_n^2\\
\vdots&&\vdots\\
x_1^{2^{n-1}}&\cdots&x_n^{2^{n-1}}
\end{pmatrix}
=
\prod_{(a_1,\ldots,a_n)\ne(0,\ldots,0)}(a_1x_1+\cdots+a_nx_n),
$$
where $(a_1,\ldots,a_n)$ runs over all nonzero elements of $\ZZ_2^n$.
:::

::: {.solution}

Let
$$
D(x_1,\ldots,x_n)
\coloneqq
\det\!\begin{pmatrix}
x_1&\cdots&x_n\\
x_1^2&\cdots&x_n^2\\
\vdots&&\vdots\\
x_1^{2^{n-1}}&\cdots&x_n^{2^{n-1}}
\end{pmatrix},
$$
and for $a=(a_1,\ldots,a_n)\in\ZZ_2^n$ put
$$
L_a\coloneqq a_1x_1+\cdots+a_nx_n.
$$

::: pf

::: {.pf-step #s1-1}

For every $k\geq0$ and every $a\in\ZZ_2^n$,
$$
L_a^{\,2^k}
=
\sum_{j=1}^n a_jx_j^{2^k}.
$$


::: pf-proof

In characteristic $2$, Frobenius is a ring homomorphism:
$$
(u+v)^2=u^2+v^2.
$$
Iterating gives
$$
\left(\sum_j a_jx_j\right)^{2^k}
=
\sum_j a_j^{2^k}x_j^{2^k}.
$$
Since each $a_j\in\ZZ_2$ satisfies $a_j^{2^k}=a_j$, the displayed identity follows.

:::

:::

::: {.pf-step #s1-2}

For every nonzero $a\in\ZZ_2^n$, the linear polynomial $L_a$ divides $D$.


::: pf-proof

Choose $i$ with $a_i=1$. Replace the $i$-th column of the determinant by the sum
$$
\sum_{j=1}^n a_j\,(\text{$j$-th column}).
$$
Because $a_i=1$, this is obtained from the original $i$-th column by adding a linear combination of the other columns, so the determinant is unchanged. By step [](#s1-1){.pf-ref}, the new $i$-th column is
$$
\begin{pmatrix}
L_a\\
L_a^2\\
\vdots\\
L_a^{2^{n-1}}
\end{pmatrix}.
$$
Every entry in that column is divisible by $L_a$, hence the determinant is divisible by $L_a$.

:::

:::

::: {.pf-step #s1-3}

The product
$$
P\coloneqq\prod_{a\in\ZZ_2^n\setminus\{0\}}L_a
$$
divides $D$.


::: pf-proof

Each $L_a$ is a nonzero linear polynomial, hence irreducible in the polynomial UFD
$$
\ZZ_2[x_1,\ldots,x_n].
$$
If $a\neq b$, then $L_a\neq L_b$. Since the only nonzero unit of $\ZZ_2$ is $1$, distinct $L_a$ are nonassociate. Step [](#s1-2){.pf-ref} shows that every one of these pairwise nonassociate irreducibles divides $D$, so their product divides $D$.

:::

:::

::: {.pf-step #s1-4}

The determinant $D$ is nonzero and homogeneous of degree
$$
1+2+\cdots+2^{n-1}=2^n-1.
$$


::: pf-proof

Every term in the determinant expansion chooses one entry from each row, so every term has total degree
$$
\sum_{k=0}^{n-1}2^k=2^n-1.
$$
Moreover, the identity permutation contributes the monomial
$$
x_1x_2^2x_3^{2^2}\cdots x_n^{2^{n-1}}.
$$
No other permutation contributes this monomial, because the exponents
$$
1,2,2^2,\ldots,2^{n-1}
$$
are pairwise distinct and therefore determine which variable was chosen in each row. Hence this monomial cannot cancel, so $D\neq0$ and has the stated degree.

:::

:::

::: {.pf-step #s1-5}

The product $P$ is homogeneous of degree $2^n-1$.


::: pf-proof

There are exactly $2^n-1$ nonzero vectors in $\ZZ_2^n$, and every factor $L_a$ has degree $1$.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
D
=
\prod_{a\in\ZZ_2^n\setminus\{0\}}
(a_1x_1+\cdots+a_nx_n)
}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, write $D=PQ$. Steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} show
$$
\deg D=\deg P=2^n-1.
$$
Since $D$ and $P$ are nonzero, $Q$ has degree $0$, hence is a nonzero constant. The only nonzero constant unit in $\ZZ_2$ is $1$, so $Q=1$ and $D=P$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required identity.

:::

:::

:::
