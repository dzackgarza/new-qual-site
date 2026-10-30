---
schema: qual/card@1
id: P-B2P3P
kind: problem
title: Jordan and rational forms from characteristic and minimal polynomials;
  nilpotents with a unique two-dimensional invariant subspace
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Rational Canonical Form
  - Nilpotence
relations: []
review: draft
---

::: {.problem}
Let $V$ be a 5-dimensional vector space over a field $F$.

(a) Let $T: V \to V$ be a linear transformation with characteristic polynomial $(x-1)^3(x-2)^2$ and minimal polynomial $(x-1)^2(x-2)$.

(i) Write down a matrix which represents $T$ in Jordan normal form.

(ii) Write down the matrix which represents $T$ in rational normal form.

(b) Instead, let $T: V \to V$ be a *nilpotent* linear transformation which has exactly one 2-dimensional invariant subspace.

(i) How many similarity classes of such linear maps $T$ are there?

(ii) Assuming finally that $F$ is the finite field $\FF_q$ with $q$ elements, find an explicit formula for the number of such linear maps $T$.
:::

::: {.solution}

::: pf

::: {.pf-step #a1}
(a)(i) The Jordan normal form of $T$ is
$$
\begin{pmatrix} 1&1&0&0&0\\ 0&1&0&0&0\\ 0&0&1&0&0\\ 0&0&0&2&0\\ 0&0&0&0&2 \end{pmatrix}.
$$

::: pf-proof
The exponent of $x-1$ in the minimal polynomial is the size of the largest Jordan block for the eigenvalue $1$, and its exponent in the characteristic polynomial is the total size of those blocks. So the blocks for $1$ have sizes $2,1$. In the same way, the blocks for $2$ have sizes $1,1$.
:::

:::

::: {.pf-step #a2}
(a)(ii) The rational normal form of $T$ is
$$
\begin{pmatrix} 0&-2&0&0&0\\ 1&3&0&0&0\\ 0&0&0&0&2\\ 0&0&1&0&-5\\ 0&0&0&1&4 \end{pmatrix}.
$$

::: pf-proof
By step [](#a1){.pf-ref}, the $F[x]$-module $V$ is
$$
\frac{F[x]}{(x-1)} \oplus \frac{F[x]}{(x-1)^2} \oplus \frac{F[x]}{(x-2)} \oplus \frac{F[x]}{(x-2)}
\cong \frac{F[x]}{(x-1)(x-2)} \oplus \frac{F[x]}{(x-1)^2(x-2)}
$$
by the Chinese remainder theorem. The invariant factors are $x^2-3x+2$ and $x^3-4x^2+5x-2$, and the displayed matrix is the block sum of their companion matrices.
:::

:::

::: {.pf-step #b1}
(b)(i) There is exactly one similarity class: the single nilpotent Jordan block of size $5$.

::: pf-proof
A nilpotent $T$ is similar to a sum of Jordan blocks with eigenvalue $0$, one for each part of a partition of $5$, and the number of blocks is $\dim\ker T$.

For the single block, with $Te_1=0$ and $Te_i=e_{i-1}$, every invariant subspace $W\neq0$ contains $e_1$, and induction on $\dim W$ applied to $W/\langle e_1\rangle$ under the single block of size $4$ shows $W=\ker T^{\dim W}$. So $\ker T^2$ is the only $2$-dimensional invariant subspace.

Every other partition has at least two blocks, and gives at least two $2$-dimensional invariant subspaces:

- With at least three blocks, $\dim\ker T\ge3$, and every $2$-dimensional subspace of $\ker T$ is invariant.
- For the partition $4+1$, with blocks $e_1,\ldots,e_4$ and $f$, both $\ker T=\langle e_1,f\rangle$ and $\langle e_1,e_2\rangle$ are invariant.
- For the partition $3+2$, with blocks $e_1,e_2,e_3$ and $f_1,f_2$, both $\langle e_1,e_2\rangle$ and $\langle f_1,f_2\rangle$ are invariant.
:::

:::

::: {.pf-step #b2}
(b)(ii) Over $\FF_q$ the number of such maps $T$ is
$$
\boxed{q^6(q^5-1)(q^4-1)(q^3-1)(q^2-1)}.
$$

::: pf-proof
By step [](#b1){.pf-ref}, these maps form one conjugacy class under $GL_5(\FF_q)$, the class of the single Jordan block $N$. Its size is the index of the centralizer of $N$. The centralizer of $N$ consists of the invertible matrices of the form
$$
\begin{pmatrix} a&b&c&d&e\\ &a&b&c&d\\ &&a&b&c\\ &&&a&b\\ &&&&a \end{pmatrix},
$$
which has order $(q-1)q^4$. Since $\cardinality{GL_5(\FF_q)} = q^{10}(q^5-1)(q^4-1)(q^3-1)(q^2-1)(q-1)$, the index is the displayed number.
:::

:::

::: pf-qed
Steps [](#a1){.pf-ref} and [](#a2){.pf-ref} answer (a), and steps [](#b1){.pf-ref} and [](#b2){.pf-ref} answer (b).
:::

:::

:::
