---
schema: qual/card@1
id: P-CC3DW
kind: problem
title: Let $M$ be a square matrix over a field $K$. Use a suitable canonical form...
classification:
  areas:
  - algebra
  topics:
  - linear-algebra
  - matrices
  - canonical-forms
relations: []
review: draft
---

::: problem
Let $M$ be a square matrix over a field $K$. Use a suitable canonical
form to show that $M$ is similar to its transpose $M^T$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

We use the **Rational Canonical Form** (Frobenius normal form), which exists for any square matrix over an arbitrary field $K$.

1. Over the field $K$, $M$ is similar to a direct sum of companion matrices of its invariant factors:
$$
M \sim C(p_1) \oplus C(p_2) \oplus \cdots \oplus C(p_k),
$$
where each $C(p_i)$ is the companion matrix of a monic polynomial $p_i(x) = x^d + a_{d-1}x^{d-1} + \cdots + a_1 x + a_0 \in K[x]$.

2. Since transposition distributes over direct sums and preserves similarity:
$$
M \sim M^T \iff C(p_i) \sim C(p_i)^T \text{ for each } i=1, \ldots, k.
$$
Thus, it suffices to prove that any companion matrix $C = C(p)$ is similar to its transpose $C^T$.

3. Let $C$ be the $d \times d$ companion matrix of $p(x)$:
$$
C = \begin{pmatrix}
0 & 0 & \cdots & 0 & -a_0 \\
1 & 0 & \cdots & 0 & -a_1 \\
0 & 1 & \cdots & 0 & -a_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \cdots & 1 & -a_{d-1}
\end{pmatrix}.
$$
The characteristic and minimal polynomials of both $C$ and $C^T$ are equal to $p(x)$.
Since $C^T$ has minimal polynomial $p(x)$ of degree equal to the dimension $d$, $C^T$ is also cyclic, and its single invariant factor is $p(x)$.

4. By the uniqueness of the Rational Canonical Form, any two matrices over $K$ with the same invariant factors are similar over $K$. Since $C$ and $C^T$ have the identical list of invariant factors (namely, the single polynomial $p(x)$), $C$ is similar to $C^T$ over $K$.

5. Taking the direct sum over all blocks gives $M \sim M^T$ over $K$.
:::
