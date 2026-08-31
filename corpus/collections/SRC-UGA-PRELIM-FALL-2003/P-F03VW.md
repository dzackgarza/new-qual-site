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

::: problem
Let $M$ be an $m \times n$ matrix, and let $V = \{v \in \mathbb{R}^n : Mv = 0\}$ and $W = \{M^t y : y \in \mathbb{R}^m\}$.

a) Prove that $V$ and $W$ are vector subspaces of $\mathbb{R}^n$.

b) Prove that $V = \{x \in \mathbb{R}^n : x \cdot w = 0 \text{ for all } w \in W\}$.
:::

::: {.solution}
**Part (a).**

<1>1. $V = \{v \in \mathbb{R}^n : Mv = 0\} = \ker(M)$ is a vector subspace of $\mathbb{R}^n$.
<2>1. $M(0_{\mathbb{R}^n}) = 0_{\mathbb{R}^m}$, so $0_{\mathbb{R}^n} \in V$.
::: {.proof}
linear maps preserve the zero vector.
:::
<2>2. If $u, v \in V$, then $M(u + v) = Mu + Mv = 0 + 0 = 0$, so $u + v \in V$.
::: {.proof}
linearity of matrix multiplication: $M(u+v) = Mu + Mv$.
:::
<2>3. If $v \in V$ and $c \in \mathbb{R}$, then $M(cv) = c(Mv) = c \cdot 0 = 0$, so $cv \in V$.
::: {.proof}
scalar compatibility of matrix multiplication: $M(cv) = c(Mv)$.
:::
<2>4. Hence $V$ is a subspace of $\mathbb{R}^n$.
::: {.proof}
subspace criterion.
:::

<1>2. $W = \{M^t y : y \in \mathbb{R}^m\} = \operatorname{im}(M^t)$ is a vector subspace of $\mathbb{R}^n$.
<2>1. For $y = 0_{\mathbb{R}^m}$, $M^t(0_{\mathbb{R}^m}) = 0_{\mathbb{R}^n} \in W$.
::: {.proof}
$M^t$ is linear.
:::
<2>2. If $w_1, w_2 \in W$, then $w_1 = M^t y_1$ and $w_2 = M^t y_2$ for some $y_1, y_2 \in \mathbb{R}^m$.
Then $w_1 + w_2 = M^t(y_1 + y_2) \in W$ since $y_1 + y_2 \in \mathbb{R}^m$.
::: {.proof}
linearity of $M^t$.
:::
<2>3. If $w = M^t y \in W$ and $c \in \mathbb{R}$, then $cw = c(M^t y) = M^t(cy) \in W$ since $cy \in \mathbb{R}^m$.
::: {.proof}
linearity of $M^t$.
:::
<2>4. Hence $W$ is a subspace of $\mathbb{R}^n$.
::: {.proof}
subspace criterion.
:::

**Part (b).**

<1>3. Prove $V \subseteq W^\perp = \{x \in \mathbb{R}^n : x \cdot w = 0 \text{ for all } w \in W\}$.
<2>1. Let $x \in V$, so $Mx = 0$.
::: {.proof}
definition of $V$.
:::
<2>2. Let $w \in W$ be arbitrary, so $w = M^t y$ for some $y \in \mathbb{R}^m$.
::: {.proof}
definition of $W$.
:::
<2>3. Express the dot product as matrix multiplication:
\[
x \cdot w = x^t w = x^t (M^t y) = (Mx)^t y.
\]
::: {.proof}
transpose identity $(AB)^t = B^t A^t$ and associativity of matrix multiplication.
:::
<2>4. Since $Mx = 0$, $(Mx)^t y = 0^t y = 0$.
::: {.proof}
<2>1. <2>5. Thus $x \cdot w = 0$ for all $w \in W$, so $x \in W^\perp$.
:::
::: {.proof}
<2>3 and <2>4.
:::

<1>4. Prove $W^\perp \subseteq V$.
<2>1. Let $x \in W^\perp$, so $x \cdot w = 0$ for all $w \in W$.
::: {.proof}
setup.
:::
<2>2. For every $y \in \mathbb{R}^m$, the vector $M^t y \in W$, so $x \cdot (M^t y) = 0$.
::: {.proof}
definition of $W$.
:::
<2>3. $0 = x \cdot (M^t y) = x^t M^t y = (Mx)^t y = (Mx) \cdot y$ for all $y \in \mathbb{R}^m$.
::: {.proof}
<2>2 and transpose properties.
:::
<2>4. Choose $y = Mx \in \mathbb{R}^m$.
Then $(Mx) \cdot (Mx) = \|Mx\|^2 = 0$.
::: {.proof}
setting $y = Mx$ in <2>3. <2>5. By positive definiteness of the Euclidean norm, $\|Mx\|^2 = 0 \implies Mx = 0$.
:::
::: {.proof}
standard property of inner products.
:::
<2>6. Hence $x \in V$.
::: {.proof}
definition of $V$.
:::

<1>5. Conclusion: $V = W^\perp = \{x \in \mathbb{R}^n : x \cdot w = 0 \text{ for all } w \in W\}$.
::: {.proof}
<1>3 and <1>4.
:::
Q.E.D.
:::
