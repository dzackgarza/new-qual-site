---
schema: qual/card@1
id: P-APAS04E
kind: problem
title: Induced trivial and Kronecker products of Specht modules in $S_6$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-31
  note: 'Solution parts (b) and (c) corrected: the old decompositions had dimensions 60 and
    45 instead of 45 and 80.'
---

::: {.problem}
If $\lambda=(\lambda_1\ge\lambda_2\ge\dots\ge\lambda_k)$ is a partition of $n$, let $A^\lambda$ denote the irreducible representation of the symmetric group $S_n$ such that the Frobenius image of $\chi^{A^\lambda}$ is the Schur function $S_\lambda(x_1,\ldots,x_N)$ where $N>n$.

(a) Let $T$ be the trivial representation.
Decompose $T\uparrow_{S_3\times S_3}^{S_6}$ as a sum of irreducible representations of $S_6$ where $S_3\times S_3$ is the Young subgroup of $S_6$ consisting of all permuations $\sigma\in S_6$ such that
$$
\sigma(1),\sigma(2),\sigma(3)\in\{1,2,3\},\qquad \sigma(4),\sigma(5),\sigma(6)\in\{4,5,6\}.
$$

(b) Decompose $A^{(2,4)}\otimes A^{(1,5)}$ as a sum of irreducible representations of $S_6$ where $\otimes$ represents the Kronecker product of the representations.

(c) Decompose $A^{(1,2)}\times A^{(1,2)}\uparrow_{S_3\times S_3}^{S_6}$ as a sum of irreducible representations of $S_6$.
(Here $S_3\times S_3$ is group described in part (a).)
:::

::: {.solution}

**(a).**

::: pf

::: pf-step
$T \uparrow_{S_3 \times S_3}^{S_6}$ is the permutation representation on the cosets of $S_3 \times S_3$, i.e. on the $\binom{6}{3} = 20$ three-element subsets of $\{1, \ldots, 6\}$.

::: pf-proof
the cosets of the Young subgroup $S_3 \times S_3$ correspond to $3$-subsets.
:::

:::

::: {.pf-step #a-decomposition}
By the Pieri rule (or the Littlewood–Richardson rule), the induced trivial representation decomposes as
$$T \uparrow_{S_3 \times S_3}^{S_6} = A^{(6)} \oplus A^{(5,1)} \oplus A^{(4,2)} \oplus A^{(3,3)}.$$

::: pf-proof
the permutation representation on $3$-subsets decomposes into the Specht modules indexed by partitions of $6$ with at most $2$ parts; these are exactly $(6), (5,1), (4,2), (3,3)$.
:::

:::

:::

**(b).**

::: pf

::: pf-step
$A^{(2,4)} = A^{(4,2)}$ and $A^{(1,5)} = A^{(5,1)}$.

::: pf-proof
$(2,4)$ and $(4,2)$ are the same partition (written in nonincreasing order), and similarly $(1,5) = (5,1)$.
:::

:::

::: {.pf-step #kronecker-product-decomposition}
The Kronecker product $A^{(4,2)} \otimes A^{(5,1)}$ decomposes (by the Kronecker coefficients) as
$$A^{(4,2)} \otimes A^{(5,1)} = A^{(5,1)} \oplus A^{(4,2)} \oplus A^{(4,1,1)} \oplus A^{(3,3)} \oplus A^{(3,2,1)}.$$

::: pf-proof
The permutation representation $P=\CC^6$ of $S_6$ is $A^{(6)}\oplus A^{(5,1)}$ and equals $T\uparrow_{S_5}^{S_6}$. For any representation $V$, $V\otimes T\uparrow_{S_5}^{S_6}\cong (V\downarrow_{S_5})\uparrow^{S_6}$, so
$$A^{(4,2)}\otimes A^{(5,1)}\cong \bigl(A^{(4,2)}\downarrow_{S_5}\bigr)\uparrow^{S_6}\ominus A^{(4,2)}.$$
By the branching rule, $A^{(4,2)}\downarrow_{S_5}=A^{(4,1)}\oplus A^{(3,2)}$. Inducing by the branching rule again,
$$A^{(4,1)}\uparrow^{S_6}=A^{(5,1)}\oplus A^{(4,2)}\oplus A^{(4,1,1)},\qquad A^{(3,2)}\uparrow^{S_6}=A^{(4,2)}\oplus A^{(3,3)}\oplus A^{(3,2,1)}.$$
Removing one copy of $A^{(4,2)}$ gives the stated sum. As a check, the dimensions are $9\cdot 5=45=5+9+10+5+16$.
:::

:::

:::

**(c).**

::: pf

::: pf-step
$A^{(1,2)} = A^{(2,1)}$ is the standard $2$-dimensional representation of $S_3$.

::: pf-proof
$(1,2) = (2,1)$ is the partition of $3$ with two parts.
:::

:::

::: {.pf-step #outer-product-decomposition}
$A^{(2,1)} \times A^{(2,1)}$ is the outer (tensor) product, which by the Pieri rule is
$$A^{(2,1)} \times A^{(2,1)}\uparrow_{S_3\times S_3}^{S_6} = A^{(4,2)} \oplus A^{(4,1,1)} \oplus A^{(3,3)} \oplus 2A^{(3,2,1)} \oplus A^{(3,1,1,1)} \oplus A^{(2,2,2)} \oplus A^{(2,2,1,1)}.$$

::: pf-proof
The Littlewood–Richardson coefficients $c^{\nu}_{(2,1),(2,1)}$ are $1$ for $\nu=(4,2),(4,1,1),(3,3),(3,1,1,1),(2,2,2),(2,2,1,1)$ and $2$ for $\nu=(3,2,1)$. As a check, the dimensions are $\binom63\cdot2\cdot2=80=9+10+5+2\cdot16+10+5+9$.
:::

:::

::: {.pf-step #induction-equals-outer-product}
Inducing from $S_3 \times S_3$ to $S_6$ (which is the same as the outer product, since induction from a Young subgroup is the outer product), the decomposition is exactly the one in step [](#outer-product-decomposition){.pf-ref}.

::: pf-proof
induction from $S_3 \times S_3$ to $S_6$ of an outer product is the outer product itself.
:::

:::

::: pf-qed
Step [](#a-decomposition){.pf-ref} (a), step [](#kronecker-product-decomposition){.pf-ref} (b), steps [](#outer-product-decomposition){.pf-ref} and [](#induction-equals-outer-product){.pf-ref} (c).
:::

:::

:::
