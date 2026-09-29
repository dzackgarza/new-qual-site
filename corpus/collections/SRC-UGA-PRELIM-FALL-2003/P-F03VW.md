---
schema: qual/card@1
id: P-F03VW
kind: problem
title: Nullspace of $M$ is the orthogonal complement of the column space of $M^t$
classification:
  areas:
  - prelim
  topics:
  - Vector Spaces
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $M$ be an $m \times n$ matrix, and let $V = \{v \in \mathbb{R}^n : Mv = 0\}$ and $W = \{M^t y : y \in \mathbb{R}^m\}$.

a) Prove that $V$ and $W$ are vector subspaces of $\mathbb{R}^n$.

b) Prove that $V = \{x \in \mathbb{R}^n : x \cdot w = 0 \text{ for all } w \in W\}$.
:::

::: {.solution}
**Part (a).**

::: pf

::: pf-step
$V = \{v \in \mathbb{R}^n : Mv = 0\} = \ker(M)$ is a vector subspace of $\mathbb{R}^n$.

::: pf-proof

::: pf-step
$M(0_{\mathbb{R}^n}) = 0_{\mathbb{R}^m}$, so $0_{\mathbb{R}^n} \in V$.

::: pf-proof
linear maps preserve the zero vector.
:::

:::

::: pf-step
If $u, v \in V$, then $M(u + v) = Mu + Mv = 0 + 0 = 0$, so $u + v \in V$.

::: pf-proof
linearity of matrix multiplication: $M(u+v) = Mu + Mv$.
:::

:::

::: pf-step
If $v \in V$ and $c \in \mathbb{R}$, then $M(cv) = c(Mv) = c \cdot 0 = 0$, so $cv \in V$.

::: pf-proof
scalar compatibility of matrix multiplication: $M(cv) = c(Mv)$.
:::

:::

::: pf-step
Hence $V$ is a subspace of $\mathbb{R}^n$.

::: pf-proof
subspace criterion.
:::

:::

:::

:::

::: pf-step
$W = \{M^t y : y \in \mathbb{R}^m\} = \operatorname{im}(M^t)$ is a vector subspace of $\mathbb{R}^n$.

::: pf-proof

::: pf-step
For $y = 0_{\mathbb{R}^m}$, $M^t(0_{\mathbb{R}^m}) = 0_{\mathbb{R}^n} \in W$.

::: pf-proof
$M^t$ is linear.
:::

:::

::: pf-step
If $w_1, w_2 \in W$, then $w_1 = M^t y_1$ and $w_2 = M^t y_2$ for some $y_1, y_2 \in \mathbb{R}^m$.
Then $w_1 + w_2 = M^t(y_1 + y_2) \in W$ since $y_1 + y_2 \in \mathbb{R}^m$.

::: pf-proof
linearity of $M^t$.
:::

:::

::: pf-step
If $w = M^t y \in W$ and $c \in \mathbb{R}$, then $cw = c(M^t y) = M^t(cy) \in W$ since $cy \in \mathbb{R}^m$.

::: pf-proof
linearity of $M^t$.
:::

:::

::: pf-step
Hence $W$ is a subspace of $\mathbb{R}^n$.

::: pf-proof
subspace criterion.
:::

:::

:::

:::

:::

**Part (b).**

::: pf

::: {.pf-step #s3}
Prove $V \subseteq W^\perp = \{x \in \mathbb{R}^n : x \cdot w = 0 \text{ for all } w \in W\}$.

::: pf-proof

::: {.pf-step #s3-1}
Let $x \in V$, so $Mx = 0$.

::: pf-proof
definition of $V$.
:::

:::

::: pf-step
Let $w \in W$ be arbitrary, so $w = M^t y$ for some $y \in \mathbb{R}^m$.

::: pf-proof
definition of $W$.
:::

:::

::: {.pf-step #s3-3}
Express the dot product as matrix multiplication:
\[
x \cdot w = x^t w = x^t (M^t y) = (Mx)^t y.
\]

::: pf-proof
transpose identity $(AB)^t = B^t A^t$ and associativity of matrix multiplication.
:::

:::

::: {.pf-step #s3-4}
Since $Mx = 0$, $(Mx)^t y = 0^t y = 0$.

::: pf-proof
Step [](#s3-1){.pf-ref}.
:::

:::

::: pf-step
Thus $x \cdot w = 0$ for all $w \in W$, so $x \in W^\perp$.

::: pf-proof
Steps [](#s3-3){.pf-ref} and [](#s3-4){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s4}
Prove $W^\perp \subseteq V$.

::: pf-proof

::: pf-step
Let $x \in W^\perp$, so $x \cdot w = 0$ for all $w \in W$.

::: pf-proof
setup.
:::

:::

::: {.pf-step #s4-2}
For every $y \in \mathbb{R}^m$, the vector $M^t y \in W$, so $x \cdot (M^t y) = 0$.

::: pf-proof
definition of $W$.
:::

:::

::: {.pf-step #s4-3}
$0 = x \cdot (M^t y) = x^t M^t y = (Mx)^t y = (Mx) \cdot y$ for all $y \in \mathbb{R}^m$.

::: pf-proof
Step [](#s4-2){.pf-ref} and transpose properties.
:::

:::

::: pf-step
Choose $y = Mx \in \mathbb{R}^m$.
Then $(Mx) \cdot (Mx) = \|Mx\|^2 = 0$.

::: pf-proof
setting $y = Mx$ in step [](#s4-3){.pf-ref}.
:::

:::

::: pf-step
By positive definiteness of the Euclidean norm, $\|Mx\|^2 = 0 \implies Mx = 0$.

::: pf-proof
standard property of inner products.
:::

:::

::: pf-step
Hence $x \in V$.

::: pf-proof
definition of $V$.
:::

:::

:::

:::

::: pf-step
Conclusion: $V = W^\perp = \{x \in \mathbb{R}^n : x \cdot w = 0 \text{ for all } w \in W\}$.

::: pf-proof
Steps [](#s3){.pf-ref} and [](#s4){.pf-ref}.
:::

:::

:::
:::
