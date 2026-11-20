---
schema: qual/card@1
id: P-APAS26F
kind: problem
title: Maximal commutative subalgebras equal their centralizers; classify those of $\operatorname{End}(V)$
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 6 of the Spring 2026 Applied Algebra Qualifying Exam (Math 202 A/B/C),
    printed p. 12, is the statement the card answers, and the head of the solution names it; the
    retained file assets/attachments/SP26_202_Applied_Algebra_Qual.pdf numbers every page including the
    blank versos, so Problem 6 stands on its page 12. Checked: the statement against the paper's text
    layer at the page named; both directions of the centralizer criterion and the classification of the
    maximal commutative subalgebras of $\operatorname{End}(V)$; `qualc.authoring check` on the card, and
    `tmp/lam.sh` for the numbering and the QED. Not checked: no retained solution set exists for this
    paper to compare the argument with, and no other card of the collection in this pass.
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Seven steps asserted their claim with no justification and each now carries one: the centralizer
    definition together with $\mathcal{B} \subseteq C_\mathcal{A}(\mathcal{B})$, both directions of the
    maximal-commutativity criterion, the spectral theorem for a commutative $*$-subalgebra (each element
    is normal because $T^* \in \mathcal{B}$ and $\mathcal{B}$ is commutative), the identification of the
    centralizer with the block-diagonal algebra, the dimension count forcing $\dim V_i = 1$, and both
    halves of the classification. Checked while writing: $\mathcal{D}_\mathcal{E}$ equals its own
    centralizer, since an operator commuting with every $E_{ii}$ is diagonal, which is what makes the
    diagonal algebras maximal rather than merely commutative. Two structural repairs: the two container
    steps carried labels instead of claims and now state the criterion and the classification as claims,
    and the closing pf-qed only restated them, which STYLE-08 does not admit, so it is gone and the
    classification step now carries the QED. The statement is unchanged. No retained solution set exists
    for this paper, so the argument is the card's own.
---

::: {.problem}
Let $\mathcal{B}$ be a commutative subalgebra of an algebra $\mathcal{A}$.
Prove that $\mathcal{B}$ is a maximal commutative subalgebra of $\mathcal{A}$ if and only if it is equal to its own centralizer.
Using this result, or otherwise, classify the maximal commutative subalgebras of $\operatorname{End}(V)$, where $V$ is a Hilbert space.

Note: On this exam, an algebra is a finite-dimensional complex vector space equipped with an associative, bilinear, unital multiplication and an antilinear, antimultiplicative, involutive conjugation; a Hilbert space is a finite-dimensional complex vector space equipped with a scalar product.
:::

::: {.solution}

The problem is Problem 6 of the Spring 2026 Applied Algebra Qualifying Exam (Math 202 A/B/C), printed p. 12 of the paper — the retained file `assets/attachments/SP26_202_Applied_Algebra_Qual.pdf` numbers the blank versos too, so the problems stand on its even pages.

::: pf

::: {.pf-step #s1}
A commutative subalgebra $\mathcal{B} \subseteq \mathcal{A}$ is maximal commutative if and only if $\mathcal{B} = C_\mathcal{A}(\mathcal{B})$.

::: pf-proof

::: {.pf-step #centralizer}
Let $\mathcal{B} \subseteq \mathcal{A}$ be a commutative subalgebra.
The centralizer is $C_\mathcal{A}(\mathcal{B}) = \{x \in \mathcal{A} \mid xb = bx \text{ for all } b \in \mathcal{B}\}$.
Because $\mathcal{B}$ is commutative, $\mathcal{B} \subseteq C_\mathcal{A}(\mathcal{B})$.

::: pf-proof
The displayed set is the definition of the centralizer, the elements of $\mathcal{A}$ commuting with every element of $\mathcal{B}$. It contains $\mathcal{B}$ because $\mathcal{B}$ is commutative, so each of its elements commutes with every element of $\mathcal{B}$.
:::

:::

::: {.pf-step #converse}
**Direction ($\Leftarrow$):** Suppose $\mathcal{B} = C_\mathcal{A}(\mathcal{B})$.
Let $\mathcal{B}' \subseteq \mathcal{A}$ be any commutative subalgebra containing $\mathcal{B}$.
For each $y \in \mathcal{B}'$, since $\mathcal{B}'$ is commutative, $y$ commutes with every element of $\mathcal{B}'$, and in particular with every element of $\mathcal{B}$.
Thus $y \in C_\mathcal{A}(\mathcal{B}) = \mathcal{B}$, so $\mathcal{B}' = \mathcal{B}$.
Hence $\mathcal{B}$ is maximal commutative.

::: pf-proof
Let $\mathcal{B}' \supseteq \mathcal{B}$ be a commutative subalgebra and $y \in \mathcal{B}'$; since $\mathcal{B}'$ is commutative, $y$ commutes with every element of $\mathcal{B}'$, hence with every element of the subset $\mathcal{B}$, so $y \in C_\mathcal{A}(\mathcal{B}) = \mathcal{B}$. Therefore $\mathcal{B}' \subseteq \mathcal{B}$, and with the opposite inclusion the two are equal; no commutative subalgebra contains $\mathcal{B}$ properly, which is maximality.
:::

:::

::: {.pf-step #forward}
**Direction ($\Rightarrow$):** Suppose $\mathcal{B}$ is a maximal commutative subalgebra.
Suppose for contradiction that there exists $x \in C_\mathcal{A}(\mathcal{B}) \setminus \mathcal{B}$.
Consider the subalgebra $\mathcal{B}[x] = \{ \sum_{k=0}^m b_k x^k \mid b_k \in \mathcal{B}, \, m \in \NN \}$.
Because $x$ commutes with all elements of $\mathcal{B}$ and powers of $x$ commute with each other, any two elements of $\mathcal{B}[x]$ commute:
$$
\left(\sum_{k} b_k x^k\right) \left(\sum_{j} c_j x^j\right) = \sum_{k, j} b_k c_j x^{k+j} = \left(\sum_{j} c_j x^j\right) \left(\sum_{k} b_k x^k\right).
$$
Thus $\mathcal{B}[x]$ is a commutative subalgebra of $\mathcal{A}$ strictly containing $\mathcal{B}$, contradicting the maximality of $\mathcal{B}$.
Therefore $\mathcal{B} = C_\mathcal{A}(\mathcal{B})$.

::: pf-proof
The set $\mathcal{B}[x]$ is closed under sums and scalar multiples because the coefficients lie in the vector space $\mathcal{B}$, and it is closed under products because $x^k x^j = x^{k+j}$; it contains $\mathcal{B}$ by taking $m = 0$ and it contains $x$ by taking $b_1 = 1$ and the other coefficients $0$. The displayed computation is valid because $x$ commutes with each $b_k$, which lets the coefficient of $x^{k+j}$ in a product be written as $b_k c_j$, and because $\mathcal{B}$ is commutative, so $b_k c_j = c_j b_k$ and the two orders agree. As $x \notin \mathcal{B}$, the algebra $\mathcal{B}[x]$ strictly contains $\mathcal{B}$, contradicting maximality; hence $C_\mathcal{A}(\mathcal{B}) \subseteq \mathcal{B}$, and with step [](#centralizer){.pf-ref} the two are equal.
:::

:::

:::

:::

::: pf-step
The maximal commutative $*$-subalgebras of $\operatorname{End}(V)$ are exactly the algebras $\mathcal{D}_\mathcal{E}$ of operators diagonal with respect to some orthonormal basis $\mathcal{E}$ of $V$.

::: pf-proof

::: {.pf-step #spectral}
Let $V$ be an $n$-dimensional Hilbert space ($n = \dim V$).
By the Spectral Theorem, any commutative $*$-subalgebra $\mathcal{B} \subset \operatorname{End}(V)$ is simultaneously diagonalizable: there exists an orthogonal decomposition:
$$
V = V_1 \oplus V_2 \oplus \cdots \oplus V_k
$$
such that every $T \in \mathcal{B}$ acts as a scalar multiple $\lambda_i(T) \operatorname{id}_{V_i}$ on each eigenspace $V_i$.

::: pf-proof
Since $\mathcal{B}$ is a $*$-subalgebra, $T^* \in \mathcal{B}$ for $T \in \mathcal{B}$, and $\mathcal{B}$ is commutative, so $TT^* = T^*T$ and $T$ is normal. A commuting family of normal operators on a finite-dimensional Hilbert space has a common orthonormal eigenbasis, and grouping the basis vectors by the character $\lambda(T)$ that $T$ induces on them gives the orthogonal decomposition; the pieces are the common eigenspaces, so distinct pieces carry distinct characters and each $T$ acts as the scalar $\lambda_i(T)$ on $V_i$.
:::

:::

::: {.pf-step #block-centralizer}
The centralizer of $\mathcal{B}$ in $\operatorname{End}(V)$ consists of all operators preserving this decomposition:
$$
C_{\operatorname{End}(V)}(\mathcal{B}) \cong \bigoplus_{i=1}^k \operatorname{End}(V_i).
$$

::: pf-proof
An operator $S$ commutes with every $T \in \mathcal{B}$ if and only if it preserves each $V_i$: it must preserve each common eigenspace, because on $V_i$ the operator $T$ has the eigenvalue $\lambda_i(T)$ and distinct pieces carry distinct characters, and conversely an operator preserving every $V_i$ agrees with $T$ on each piece, so the two commute. The operators acting blockwise on the decomposition form the algebra $\bigoplus_i \operatorname{End}(V_i)$, with the direct sum of the actions on the pieces and no mixing between them.
:::

:::

::: {.pf-step #dimension-count}
By step [](#s1){.pf-ref}, $\mathcal{B}$ is maximal commutative if and only if $\mathcal{B} = C_{\operatorname{End}(V)}(\mathcal{B}) \cong \bigoplus_{i=1}^k \operatorname{End}(V_i)$.
Since $\mathcal{B}$ is commutative, each block algebra $\operatorname{End}(V_i)$ must be commutative, which occurs if and only if $\dim V_i = 1$ for each $i \in \{1, \dots, k\}$.
Thus $k = n$, and $V = \CC e_1 \oplus \cdots \oplus \CC e_n$ for an orthonormal basis $\mathcal{E} = \{e_1, \dots, e_n\}$.

::: pf-proof
By step [](#s1){.pf-ref} the algebra $\mathcal{B}$ is maximal commutative exactly when it equals its centralizer, which by step [](#block-centralizer){.pf-ref} is $\bigoplus_i \operatorname{End}(V_i)$. If $\mathcal{B}$ equals that direct sum, the projection onto the $i$-th summand is a surjective algebra homomorphism from the commutative algebra $\mathcal{B}$, so $\operatorname{End}(V_i)$ is commutative; the matrix units $E_{12}$ and $E_{21}$ in a subspace of dimension at least $2$ do not commute, so $\dim V_i = 1$. Conversely, if every $\dim V_i = 1$ then the centralizer is $\CC^k$, which is commutative and contains $\mathcal{B}$, so maximality of $\mathcal{B}$ forces equality with it.
:::

:::

::: {.pf-step #diagonal}
Therefore the maximal commutative $*$-subalgebras of $\operatorname{End}(V)$ are precisely the algebras of operators diagonalized by an orthonormal basis of $V$:
$$
\mathcal{D}_\mathcal{E} = \{ T \in \operatorname{End}(V) \mid [T]_\mathcal{E} \text{ is diagonal} \} \cong \CC^n.
$$

::: pf-proof
With $\dim V_i = 1$ for every $i$, let $e_i$ span $V_i$; the $e_i$ form an orthonormal basis because the pieces are pairwise orthogonal and each is spanned by a unit vector, and every $T \in \mathcal{B}$ acts as $\lambda_i(T)$ on $V_i$, so its matrix in $\mathcal{E}$ is diagonal and $\mathcal{B} \subseteq \mathcal{D}_\mathcal{E}$. Conversely, an operator whose matrix in an orthonormal basis is diagonal commutes with every such operator, the algebra $\mathcal{D}_\mathcal{E}$ is commutative, and it equals its own centralizer because an operator commuting with every diagonal matrix unit $E_{ii}$ is diagonal; by step [](#s1){.pf-ref} each $\mathcal{D}_\mathcal{E}$ is therefore maximal commutative, and it is isomorphic to $\CC^n$.
:::

:::

:::

:::

:::
:::
