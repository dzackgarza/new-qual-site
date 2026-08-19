---
order: 0
---

# Definitions

::: {.remark}
The main powerhouse: for $T:V\to V$ a linear transformation for $V\in\Vect_k$, map to $V\in \modsleft{k[x]}$ by letting polynomials act via $p(x)\cdot \vector v \da p(T)(\vector v)$.
Using that $k[x]$ is a PID iff $k$ is a field, and we can apply the FTFGMPID to get two decompositions:
\[
V &\cong \bigoplus_{i=1}^n k[x]/ \gens{ q_i(x) } && q_{i}(x) \divides q_{i+1}(x) \divides \cdots  \\
V &\cong \bigoplus _{j=1}^m k[x] / \gens{ p_i(x)^{e_i} } && \text{ with } p_i \text{ not necessarily distinct.} 
\]

- The $q_i$ are the **invariant factors** of $T$

  - $q_i$ is the minimal polynomial of $T$ restricted to $V_i \da k[x] / \gens{ q_i(x) }$.

  - The largest invariant factor $q_n$ is the **minimal polynomial** of $T$.

  - The product $\prod_{i=1}^n q_i(x)$ is the **characteristic polynomial** of $T$.

- The $p_i$ are the **elementary divisors** of $T$.

  - Grouping equal primes, the factors $p(x)^e$ are the cyclic summands in the primary decomposition.

  - Over an algebraically closed field (or after splitting), each $p_i(x)=x-\lambda$, and $(x-\lambda)^e$ is a Jordan block of size $e$ for eigenvalue $\lambda$.

  - The characteristic polynomial is the product of all elementary divisors.

  - The minimal polynomial is the lcm of the elementary divisors: for each distinct $p$, take the highest power $p^e$ that occurs.

  - The geometric multiplicity of $\lambda$ is the number of elementary divisors that are powers of $x-\lambda$ (the number of Jordan blocks).

  - The size of the largest Jordan block for $\lambda$ is the largest such exponent $e$.
:::

[[D-5BR4D]]

[[D-SSGKC]]

[[D-RG5FO]]

[[D-BSUV4]]

[[D-B4VTH]]

[[D-HGMOW]]

[[D-23FX7]]

[[PR-24CPI]]

[[PR-WDPF7]]

[[D-JIGMN]]

[[D-JRPTK]]

## Notation

::: {.remark}
Some definitions:

- $A^t$ is the usual transpose.

- $A^{\dagger}$ is the conjugate transpose.

- A matrix is $A^{\dagger}$ is **adjoint** to $A$ iff $\inner{A\vector x}{\vector y} = \inner{\vector x}{A^{\dagger} \vector y}$.

  - $A$ is **self-adjoint** iff $A$ is an adjoint for itself, so $\inner{A\vector x}{\vector y} = \inner{\vector x}{A \vector y}$.

- $A$ is **symmetric** iff $A = A^t$.

  - $A$ is **orthogonal** iff $A^tA = AA^t = I$

- $A$ is **Hermitian** iff $A^{\dagger} = A$.

  - $A$ is **normal** iff $AA^{\dagger} = A^{\dagger} A$.

  - $A$ is **unitary** iff $A^{\dagger}A = AA^{\dagger} = I$.
:::
