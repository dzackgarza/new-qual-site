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
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $\mathcal{B}$ be a commutative subalgebra of an algebra $\mathcal{A}$.
Prove that $\mathcal{B}$ is a maximal commutative subalgebra of $\mathcal{A}$ if and only if it is equal to its own centralizer.
Using this result, or otherwise, classify the maximal commutative subalgebras of $\operatorname{End}(V)$, where $V$ is a Hilbert space.

Note: On this exam, an algebra is a finite-dimensional complex vector space equipped with an associative, bilinear, unital multiplication and an antilinear, antimultiplicative, involutive conjugation; a Hilbert space is a finite-dimensional complex vector space equipped with a scalar product.
:::

::: {.solution}
<1>1. Equivalence of maximal commutativity and self-centralization:
<2>1. Let $\mathcal{B} \subseteq \mathcal{A}$ be a commutative subalgebra.
The centralizer is $C_\mathcal{A}(\mathcal{B}) = \{x \in \mathcal{A} \mid xb = bx \text{ for all } b \in \mathcal{B}\}$.
Because $\mathcal{B}$ is commutative, $\mathcal{B} \subseteq C_\mathcal{A}(\mathcal{B})$.
<2>2. **Direction ($\Leftarrow$):** Suppose $\mathcal{B} = C_\mathcal{A}(\mathcal{B})$.
Let $\mathcal{B}' \subseteq \mathcal{A}$ be any commutative subalgebra containing $\mathcal{B}$.
For each $y \in \mathcal{B}'$, since $\mathcal{B}'$ is commutative, $y$ commutes with every element of $\mathcal{B}'$, and in particular with every element of $\mathcal{B}$.
Thus $y \in C_\mathcal{A}(\mathcal{B}) = \mathcal{B}$, so $\mathcal{B}' = \mathcal{B}$.
Hence $\mathcal{B}$ is maximal commutative.
<2>3. **Direction ($\Rightarrow$):** Suppose $\mathcal{B}$ is a maximal commutative subalgebra.
Suppose for contradiction that there exists $x \in C_\mathcal{A}(\mathcal{B}) \setminus \mathcal{B}$.
Consider the subalgebra $\mathcal{B}[x] = \{ \sum_{k=0}^m b_k x^k \mid b_k \in \mathcal{B}, \, m \in \mathbb{N} \}$.
Because $x$ commutes with all elements of $\mathcal{B}$ and powers of $x$ commute with each other, any two elements of $\mathcal{B}[x]$ commute:
\[
\left(\sum_{k} b_k x^k\right) \left(\sum_{j} c_j x^j\right) = \sum_{k, j} b_k c_j x^{k+j} = \left(\sum_{j} c_j x^j\right) \left(\sum_{k} b_k x^k\right).
\]
Thus $\mathcal{B}[x]$ is a commutative subalgebra of $\mathcal{A}$ strictly containing $\mathcal{B}$, contradicting the maximality of $\mathcal{B}$.
Therefore $\mathcal{B} = C_\mathcal{A}(\mathcal{B})$.

<1>2. Classification of maximal commutative $*$-subalgebras of $\operatorname{End}(V)$:
<2>1. Let $V$ be an $n$-dimensional Hilbert space ($n = \dim V$).
By the Spectral Theorem, any commutative $*$-subalgebra $\mathcal{B} \subset \operatorname{End}(V)$ is simultaneously diagonalizable: there exists an orthogonal decomposition:
\[
V = V_1 \oplus V_2 \oplus \cdots \oplus V_k
\]
such that every $T \in \mathcal{B}$ acts as a scalar multiple $\lambda_i(T) \operatorname{id}_{V_i}$ on each eigenspace $V_i$.
<2>2. The centralizer of $\mathcal{B}$ in $\operatorname{End}(V)$ consists of all operators preserving this decomposition:
\[
C_{\operatorname{End}(V)}(\mathcal{B}) \cong \bigoplus_{i=1}^k \operatorname{End}(V_i).
\]
<2>3. By <1>1, $\mathcal{B}$ is maximal commutative if and only if $\mathcal{B} = C_{\operatorname{End}(V)}(\mathcal{B}) \cong \bigoplus_{i=1}^k \operatorname{End}(V_i)$.
Since $\mathcal{B}$ is commutative, each block algebra $\operatorname{End}(V_i)$ must be commutative, which occurs if and only if $\dim V_i = 1$ for each $i \in \{1, \dots, k\}$.
Thus $k = n$, and $V = \mathbb{C} e_1 \oplus \cdots \oplus \mathbb{C} e_n$ for an orthonormal basis $\mathcal{E} = \{e_1, \dots, e_n\}$.
<2>4. Therefore the maximal commutative $*$-subalgebras of $\operatorname{End}(V)$ are precisely the algebras of operators diagonalized by an orthonormal basis of $V$:
\[
\mathcal{D}_\mathcal{E} = \{ T \in \operatorname{End}(V) \mid [T]_\mathcal{E} \text{ is diagonal} \} \cong \mathbb{C}^n.
\]

<1>3. Conclusion:
$\mathcal{B}$ is maximal commutative iff $\mathcal{B} = C_\mathcal{A}(\mathcal{B})$, and the maximal commutative $*$-subalgebras of $\operatorname{End}(V)$ are the $n$-dimensional subalgebras of operators diagonal with respect to some orthonormal basis of $V$. Q.E.D.
:::
