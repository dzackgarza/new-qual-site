---
schema: qual/card@1
id: P-APAF04D
kind: problem
title: Twisting irreducible characters by a linear character; pointwise similarity of representations
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
(a) Prove that if $G$ is finite group and $\lambda(x)$ is a linear character of $G$, then for any irreducible character $\chi$ of $G$, the function $\chi^*$ defined by $\chi^*(\sigma)=\lambda(\sigma)\chi(\sigma)$ for all $\sigma\in G$ is also an irreducible character of $G$.

(b) Let $A:G\to GL_n(\mathbb{C})$ and $B:G\to GL_n(\mathbb{C})$ be two representations of a finite group $G$.
Show that if for all $\sigma\in G$, there exists a matrix $P(\sigma)$ such that
\[
\bigl(P(\sigma)\bigr)^{-1}A(\sigma)P(\sigma)=B(\sigma),
\]
then there exist a nonsingular matrix $T$ such that for all $\sigma$,
\[
T^{-1}A(\sigma)T=B(\sigma).
\]
:::

::: {.solution}
**(a).**

<1>1. $\chi^*$ is the character of a representation of $G$.
<2>1. Let $\rho: G \to \operatorname{GL}(V)$ be an irreducible representation affording the character $\chi$.
Proof: $\chi$ is an irreducible character.
<2>2. Since $\lambda$ is a linear character, $\lambda: G \to \mathbb{C}^\times$ is a 1-dimensional representation.
Proof: definition of a linear character.
<2>3. The 1-dimensional representation $\lambda$ and representation $\rho$ give a tensor product representation $\lambda \otimes \rho: G \to \operatorname{GL}(V)$ defined by $(\lambda \otimes \rho)(\sigma) = \lambda(\sigma) \rho(\sigma)$.
Proof: standard tensor product of representations (specifically with a 1-dimensional factor).
<2>4. The character of $\lambda \otimes \rho$ is $\operatorname{Tr}(\lambda(\sigma)\rho(\sigma)) = \lambda(\sigma)\operatorname{Tr}(\rho(\sigma)) = \lambda(\sigma)\chi(\sigma) = \chi^*(\sigma)$.
Proof: linearity of trace.
<2>5. Hence $\chi^*$ is the character of $\lambda \otimes \rho$.
Proof: <2>4.

<1>2. The character $\chi^*$ is irreducible.
<2>1. A character $\psi$ of a finite group over $\mathbb{C}$ is irreducible if and only if $\langle \psi, \psi \rangle = 1$.
Proof: character theory of finite groups over $\mathbb{C}$.
<2>2. Since $G$ is finite, for each $\sigma \in G$, $\sigma^{|G|} = e$, so $\lambda(\sigma)^{|G|} = \lambda(e) = 1$.
Proof: group homomorphism from a finite group.
<2>3. Thus $\lambda(\sigma)$ is a root of unity in $\mathbb{C}$, so $|\lambda(\sigma)| = 1$ and $|\lambda(\sigma)|^2 = \lambda(\sigma)\overline{\lambda(\sigma)} = 1$.
Proof: roots of unity have absolute value $1$.
<2>4. Compute the inner product:
\[
\langle \chi^*, \chi^* \rangle = \frac{1}{|G|} \sum_{\sigma \in G} \chi^*(\sigma)\overline{\chi^*(\sigma)} = \frac{1}{|G|} \sum_{\sigma \in G} \lambda(\sigma)\chi(\sigma)\overline{\lambda(\sigma)\chi(\sigma)} = \frac{1}{|G|} \sum_{\sigma \in G} |\lambda(\sigma)|^2 |\chi(\sigma)|^2.
\]
Proof: definition of the inner product of class functions.
<2>5. Substituting $|\lambda(\sigma)|^2 = 1$ gives:
\[
\langle \chi^*, \chi^* \rangle = \frac{1}{|G|} \sum_{\sigma \in G} |\chi(\sigma)|^2 = \langle \chi, \chi \rangle.
\]
Proof: <2>3 and <2>4.
<2>6. Since $\chi$ is irreducible, $\langle \chi, \chi \rangle = 1$, so $\langle \chi^*, \chi^* \rangle = 1$.
Proof: <2>5 and irreducibility of $\chi$.
<2>7. Therefore $\chi^*$ is an irreducible character of $G$.
Proof: <1>1, <2>1, and <2>6.

**(b).**

<1>1. Pointwise similarity implies equality of characters $\chi_A = \chi_B$.
<2>1. The characters of $A$ and $B$ are given by $\chi_A(\sigma) = \operatorname{Tr}(A(\sigma))$ and $\chi_B(\sigma) = \operatorname{Tr}(B(\sigma))$.
Proof: definition of the character of a matrix representation.
<2>2. For each $\sigma \in G$, $B(\sigma) = P(\sigma)^{-1}A(\sigma)P(\sigma)$.
Proof: hypothesis.
<2>3. Since the trace is invariant under cyclic permutations and similarity transformations:
\[
\operatorname{Tr}(B(\sigma)) = \operatorname{Tr}\bigl(P(\sigma)^{-1}A(\sigma)P(\sigma)\bigr) = \operatorname{Tr}(A(\sigma)).
\]
Proof: cyclic property of trace: $\operatorname{Tr}(XY) = \operatorname{Tr}(YX)$ with $X = P(\sigma)^{-1}A(\sigma)$, $Y = P(\sigma)$.
<2>4. Hence $\chi_A(\sigma) = \chi_B(\sigma)$ for all $\sigma \in G$.
Proof: <2>1 and <2>3.

<1>2. Two complex representations of a finite group are isomorphic if and only if their characters are identical.
<2>1. By Maschke's theorem, every complex representation of a finite group is completely reducible (a direct sum of irreducible representations).
Proof: Maschke's theorem for finite groups over $\mathbb{C}$.
<2>2. The multiplicity of an irreducible representation $V_i$ in $V$ is uniquely determined by the character via $m_i = \langle \chi_V, \chi_i \rangle$.
Proof: orthogonality of irreducible characters.
<2>3. Since $\chi_A = \chi_B$, $A$ and $B$ have the same irreducible constituents with the same multiplicities.
Proof: <1>1 and <2>2.
<2>4. Thus $A \cong B$ as $\mathbb{C}[G]$-modules.
Proof: <2>1 and <2>3.
<2>5. Consequently, there exists an invertible matrix $T \in \operatorname{GL}_n(\mathbb{C})$ such that $T^{-1}A(\sigma)T = B(\sigma)$ for all $\sigma \in G$.
Proof: isomorphism of matrix representations.

<1>3. Q.E.D.
Proof: <1>2 (a) and <1>2 (b).
:::
