---
schema: qual/card@1
id: P-PRACT20-W4-26
kind: problem
title: Invertibility and inverse of $I_n+\sigma J_n$
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Matrices
  - Invertibility
relations: []
review: draft
---

::: {.problem}
Let $I _ { n }$ by the $n \times n$ identity matrix and let $J _ { n }$ be the $n \times n$ matrix with all entries equal to 1. Determine the values of $\sigma \in \mathbb { R }$ so that $I _ { n } + \sigma J _ { n }$ is invertible.
Find $( I _ { n } + \sigma J _ { n } ) ^ { - 1 }$ for such σ.
:::

::: {.solution}
<1>1. The all-ones matrix satisfies
$$
J_n^2=nJ_n.
$$
::: {.proof}
Every entry of $J_n^2$ is the sum of $n$ products $1\cdot1$, hence equals $n$.
:::

<1>2. If $\sigma=-1/n$, then $I_n+\sigma J_n$ is not invertible.
::: {.proof}
Let
$$
\mathbf 1=(1,\dots,1)^T.
$$
Since
$$
J_n\mathbf1=n\mathbf1,
$$
we have
$$
\left(I_n-\frac1nJ_n\right)\mathbf1=0.
$$
Thus the matrix has a nonzero kernel vector.
:::

<1>3. If $\sigma\ne-1/n$, then
$$
\boxed{
(I_n+\sigma J_n)^{-1}
=I_n-\frac{\sigma}{1+n\sigma}J_n.
}
$$
::: {.proof}
For any scalar $\tau$, step <1>1 gives
$$
\begin{aligned}
(I_n+\sigma J_n)(I_n+\tau J_n)
&=I_n+(\sigma+\tau)J_n+\sigma\tau J_n^2\\
&=I_n+(\sigma+\tau+n\sigma\tau)J_n.
\end{aligned}
$$
If $1+n\sigma\ne0$, take
$$
\tau=-\frac{\sigma}{1+n\sigma}.
$$
Then $\sigma+\tau+n\sigma\tau=0$, so the product is $I_n$. The two factors commute because both are polynomials in $J_n$, hence the displayed matrix is a two-sided inverse.
:::

<1>4. Therefore $I_n+\sigma J_n$ is invertible exactly when
$$
\boxed{\sigma\ne-\frac1n}.
$$
::: {.proof}
Step <1>2 gives noninvertibility at $-1/n$, while step <1>3 gives an explicit inverse for every other $\sigma$.
:::

<1>5. Q.E.D.
::: {.proof}
Steps <1>3--<1>4 give both requested answers.
:::
:::
