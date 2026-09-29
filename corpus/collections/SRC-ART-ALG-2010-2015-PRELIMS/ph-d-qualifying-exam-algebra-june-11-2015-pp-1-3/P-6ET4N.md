---
schema: qual/card@1
id: P-6ET4N
kind: problem
title: Rational and Jordan canonical forms of a $3\times 3$ real matrix; abelian groups
  of order $360$
classification:
  areas:
  - prelim
  topics:
  - Jordan Canonical Form
  - Rational Canonical Form
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.problem}
(a) Find a **Rational Canonical Form** and a **Jordan Canonical Form** for the following $3 \times 3$ matrix with real entries:
$$A = \begin{pmatrix} 0 & -1 & 2 \\ 3 & -4 & 6 \\ 2 & -2 & 3 \end{pmatrix}.$$

(b) Describe all distinct isomorphism classes of **Abelian groups of order 360**.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The characteristic polynomial of $A$ is $p_A(\lambda)=(\lambda-1)(\lambda+1)^2$.

::: pf-proof

Expanding $\det(\lambda I-A)$ along the first row of
$$
\lambda I-A=\begin{pmatrix}\lambda&1&-2\\-3&\lambda+4&-6\\-2&2&\lambda-3\end{pmatrix}
$$
gives
$$
\lambda(\lambda^2+\lambda)-(-3\lambda-3)-2(2\lambda+2)=\lambda^3+\lambda^2-\lambda-1=(\lambda-1)(\lambda+1)^2.
$$

:::

:::

::: {.pf-step #s2}

The matrix $A$ is diagonalizable, with minimal polynomial $m_A(\lambda)=\lambda^2-1$.

::: pf-proof

The matrix
$$
-I-A=\begin{pmatrix}-1&1&-2\\-3&3&-6\\-2&2&-4\end{pmatrix}
$$
has rank $1$, since every row is a multiple of $(1,-1,2)$. So the eigenspace for $-1$ has dimension $2$, equal to the algebraic multiplicity from step [](#s1){.pf-ref}, and the eigenvalue $1$ has multiplicity $1$.
Hence $A$ is diagonalizable, and its minimal polynomial is the product of the distinct factors $(\lambda-1)(\lambda+1)$.

:::

:::

::: {.pf-step #s3}

In part (a), the Jordan canonical form is $J=\operatorname{diag}(1,-1,-1)$, and the rational canonical form is
$$
R=\begin{pmatrix}-1&0&0\\0&0&1\\0&1&0\end{pmatrix},
$$
with invariant factors $\lambda+1\mid\lambda^2-1$.

::: pf-proof

By step [](#s2){.pf-ref}, $A$ is similar to the diagonal matrix of its eigenvalues.
The invariant factors $d_1\mid d_2$ satisfy $d_2=m_A=\lambda^2-1$ and $d_1d_2=p_A$, so $d_1=\lambda+1$.
Their companion matrices are $(-1)$ and $\begin{pmatrix}0&1\\1&0\end{pmatrix}$, and $R$ is their block sum [@DF04].

:::

:::

::: {.pf-step #s4}

In part (b), there are six abelian groups of order $360$:
$$
\ZZ_{360},\quad \ZZ_3\times\ZZ_{120},\quad \ZZ_2\times\ZZ_{180},\quad \ZZ_6\times\ZZ_{60},\quad \ZZ_2\times\ZZ_2\times\ZZ_{90},\quad \ZZ_2\times\ZZ_6\times\ZZ_{30}.
$$

::: pf-proof

Since $360=2^3\cdot3^2\cdot5$, an abelian group of order $360$ is $P_2\times P_3\times P_5$ with $\abs{P_2}=8$, $\abs{P_3}=9$, $\abs{P_5}=5$, and its isomorphism type is determined by a partition of each exponent [@DF04].
The partitions $3$, $2+1$, $1+1+1$ give $P_2=\ZZ_8$, $\ZZ_4\times\ZZ_2$, $\ZZ_2^3$; the partitions $2$, $1+1$ give $P_3=\ZZ_9$, $\ZZ_3^2$; and $P_5=\ZZ_5$.
The $3\cdot2\cdot1=6$ combinations, rewritten in invariant-factor form by the Chinese remainder theorem, are the listed groups.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} answers part (a) and step [](#s4){.pf-ref} answers part (b).

:::

:::

:::
