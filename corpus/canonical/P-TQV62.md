---
schema: qual/card@1
id: P-TQV62
kind: problem
title: Let $A$ be an $n \times n$ matrix. Suppose that $v$ is a column vector such...
classification:
  areas:
  - algebra
  topics:
  - minimal-and-characteristic-polynomials
  - rational-canonical-form
  - linear-algebra
relations: []
review: draft
---

::: problem
Let $A$ be an $n \times n$ matrix.

(a) Suppose that $v$ is a column vector such that the set $\{v, Av, . . . , A^{n-1} v\}$ is linearly independent.
Show that any matrix $B$ that commutes with $A$ is a polynomial in $A$.

(b) Show that there exists a column vector $v$ such that the set $\{v, Av, . . . , A^{n-1} v\}$ is linearly independent $\iff$ the characteristic polynomial of A equals the minimal polynomial of A.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**(a) Any matrix $B$ commuting with $A$ is a polynomial in $A$:** Since $\{v, Av, \ldots, A^{n-1}v\}$ is a set of $n$ linearly independent vectors in an $n$-dimensional vector space $V = K^n$, it forms a basis for $V$.
Because $Bv \in V$, we can express $Bv$ as a linear combination of this basis:
$$
Bv = c_0 v + c_1 Av + \cdots + c_{n-1} A^{n-1}v = p(A)v,
$$
where $p(x) = c_0 + c_1 x + \cdots + c_{n-1} x^{n-1} \in K[x]$.

Now, let $w \in V$ be any vector.
Since $\{v, Av, \ldots, A^{n-1}v\}$ is a basis, $w = q(A)v$ for some polynomial $q(x) \in K[x]$.
Since $B$ commutes with $A$, $B$ commutes with every polynomial in $A$, so $B q(A) = q(A) B$.
Therefore:
$$
Bw = B(q(A)v) = q(A)(Bv) = q(A)(p(A)v) = p(A)(q(A)v) = p(A)w.
$$
Since $Bw = p(A)w$ for all $w \in V$, the linear transformations are identical:
$$
B = p(A),
$$
which is a polynomial in $A$.

**(b) Existence of a cyclic vector $\iff \operatorname{char}_A(x) = m_A(x)$:**

- **$(\Longrightarrow)$:** Suppose such a vector $v$ exists.
  If $m_A(x)$ had degree $d < n$, then $m_A(A)v = 0$ would give a non-trivial linear combination $A^d v + \sum_{i=0}^{d-1} a_i A^i v = 0$ among $\{v, Av, \ldots, A^{n-1}v\}$, contradicting linear independence.
  Thus $\deg(m_A) \geq n$.
  By the Cayley-Hamilton theorem, $m_A(x) \mid \operatorname{char}_A(x)$, so $\deg(m_A) \leq \deg(\operatorname{char}_A) = n$.
  Hence $\deg(m_A) = n = \deg(\operatorname{char}_A)$.
  Since both polynomials are monic and $m_A \mid \operatorname{char}_A$, they must be equal: $m_A(x) = \operatorname{char}_A(x)$.

- **$(\Longleftarrow)$:** Suppose $\operatorname{char}_A(x) = m_A(x)$.
  By the Rational Canonical Form theorem (structure theorem for finitely generated modules over the PID $K[x]$), $V$ decomposes into cyclic $K[x]$-submodules:
  $$
  V \cong K[x]/(d_1(x)) \oplus K[x]/(d_2(x)) \oplus \cdots \oplus K[x]/(d_k(x)),
  $$
  where the invariant factors satisfy $d_1(x) \mid d_2(x) \mid \cdots \mid d_k(x)$, and the minimal polynomial is $m_A(x) = d_k(x)$, while the characteristic polynomial is $\operatorname{char}_A(x) = d_1(x) d_2(x) \cdots d_k(x)$.
  Since $\operatorname{char}_A(x) = m_A(x)$, we have $d_1(x) d_2(x) \cdots d_k(x) = d_k(x)$, which forces $k = 1$ and $d_1(x) = m_A(x)$ of degree $n$.
  Thus $V \cong K[x]/(m_A(x))$ is a cyclic $K[x]$-module.
  This means there exists a vector $v \in V$ such that $V = K[x]v = \operatorname{span}\{v, Av, A^2v, \ldots, A^{n-1}v\}$.
  Since $\dim(V) = n$, the spanning set $\{v, Av, \ldots, A^{n-1}v\}$ of size $n$ is linearly independent.
:::
