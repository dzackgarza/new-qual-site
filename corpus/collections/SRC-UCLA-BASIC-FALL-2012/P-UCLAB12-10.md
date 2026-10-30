---
schema: qual/card@1
id: P-UCLAB12-10
kind: problem
title: Jordan form of $A$ with $A^4+2A^3-2A-I=0$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $A$ be a linear operator on a four dimensional complex vector space that satisfies the polynomial equation $P(A) = A^4 + 2A^3 - 2A - I = 0$, where $I$ is the identity operator.
Let $B = A + I$ and suppose $\dim(\operatorname{range}(B)) = 2$. Finally, suppose that $\abs{\Tr(A)} = 2$. Give a Jordan canonical form of $A$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The polynomial $P$ factors as
$$
P(t)
=
t^4+2t^3-2t-1
=
(t-1)(t+1)^3.
$$


::: pf-proof

One computes
$$
(t-1)(t+1)^3
=(t-1)(t^3+3t^2+3t+1)
=
t^4+2t^3-2t-1.
$$

:::

:::

::: pf-step

The only possible eigenvalues of $A$ are
$$
1
\qquad\text{and}\qquad
-1.
$$


::: pf-proof

If
$$
Av=\lambda v
$$
with $v\ne0$, then
$$
0=P(A)v=P(\lambda)v.
$$
Hence $P(\lambda)=0$. By step [](#s1-1){.pf-ref}, the only roots are $1$ and $-1$.

:::

:::

::: pf-step

Every Jordan block of $A$ for eigenvalue $1$ has size $1$, and every Jordan block for eigenvalue $-1$ has size at most $3$.


::: pf-proof

The minimal polynomial of $A$ divides
$$
P(t)=(t-1)(t+1)^3
$$
because $P(A)=0$.
For an eigenvalue $\lambda$, the largest Jordan-block size at $\lambda$ equals the exponent of $(t-\lambda)$ in the minimal polynomial.
Thus the exponent at $1$ is at most $1$, while the exponent at $-1$ is at most $3$.

:::

:::

::: {.pf-step #s1-4}

The nullspace of
$$
B=A+I
$$
has dimension $2$.


::: pf-proof

The underlying space has dimension $4$, and by hypothesis
$$
\dim\operatorname{range}B=2.
$$
Rank-nullity therefore gives
$$
\dim\ker B
=
4-2
=
2.
$$

:::

:::

::: {.pf-step #s1-5}

The Jordan form of $A$ contains exactly two Jordan blocks with eigenvalue $-1$.


::: pf-proof

Since
$$
B=A+I,
$$
one has
$$
\ker B=\ker(A+I),
$$
the eigenspace of $A$ for eigenvalue $-1$.
For a Jordan form, the dimension of the eigenspace for an eigenvalue equals the number of Jordan blocks carrying that eigenvalue.
By step [](#s1-4){.pf-ref},
$$
\dim\ker(A+I)=2,
$$
so there are exactly two $(-1)$-Jordan blocks.

:::

:::

::: {.pf-step #s1-6}

Let $m_-$ be the algebraic multiplicity of $-1$. Then
$$
m_-\in\{1,3\}.
$$


::: pf-proof

Let
$$
m_+=4-m_-
$$
be the algebraic multiplicity of $1$.
Since the trace is the sum of eigenvalues counted with algebraic multiplicity,
$$
\operatorname{Tr}(A)
=
m_+-m_-
=
4-2m_-.
$$
The hypothesis
$$
\abs{\operatorname{Tr}(A)}=2
$$
gives
$$
\abs{4-2m_-}=2.
$$
Therefore
$$
m_-=1
\quad\text{or}\quad
m_-=3.
$$

:::

:::

::: {.pf-step #s1-7}

In fact,
$$
\boxed{m_-=3}
\qquad\text{and}\qquad
\boxed{m_+=1}.
$$


::: pf-proof

By step [](#s1-5){.pf-ref}, there are two Jordan blocks for eigenvalue $-1$.
Thus its algebraic multiplicity is at least $2$.
Step [](#s1-6){.pf-ref} leaves only
$$
m_-=3.
$$
Hence
$$
m_+=4-3=1.
$$

:::

:::

::: {.pf-step #s1-8}

The two Jordan blocks for eigenvalue $-1$ have sizes $2$ and $1$.


::: pf-proof

By step [](#s1-7){.pf-ref}, their total size is the algebraic multiplicity
$$
3.
$$
By step [](#s1-5){.pf-ref}, there are exactly two such blocks.
The only partition of $3$ into two positive integers is
$$
2+1.
$$

:::

:::

::: {.pf-step #s1-9}

A Jordan canonical form of $A$ is
$$
\boxed{
\begin{pmatrix}
-1&1&0&0\\
0&-1&0&0\\
0&0&-1&0\\
0&0&0&1
\end{pmatrix}
}.
$$


::: pf-proof

Step [](#s1-8){.pf-ref} gives one Jordan block
$$
J_2(-1)
=
\begin{pmatrix}
-1&1\\
0&-1
\end{pmatrix},
$$
and one $1\times1$ block $[-1]$.
Step [](#s1-7){.pf-ref} gives one $1\times1$ block $[1]$.
Their direct sum is the displayed matrix.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the required Jordan canonical form.

:::

:::

:::
