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

::: {.problem}
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

::: pf

::: {.pf-step #p1-s1}
$\chi^*$ is the character of a representation of $G$.

::: pf-proof

::: pf-step
Let $\rho: G \to \operatorname{GL}(V)$ be an irreducible representation affording the character $\chi$.

::: pf-proof
$\chi$ is an irreducible character.
:::

:::

::: pf-step
Since $\lambda$ is a linear character, $\lambda: G \to \mathbb{C}^\times$ is a 1-dimensional representation.

::: pf-proof
definition of a linear character.
:::

:::

::: pf-step
The 1-dimensional representation $\lambda$ and representation $\rho$ give a tensor product representation $\lambda \otimes \rho: G \to \operatorname{GL}(V)$ defined by $(\lambda \otimes \rho)(\sigma) = \lambda(\sigma) \rho(\sigma)$.

::: pf-proof
standard tensor product of representations (specifically with a 1-dimensional factor).
:::

:::

::: {.pf-step #p1-s1-4}
The character of $\lambda \otimes \rho$ is $\operatorname{Tr}(\lambda(\sigma)\rho(\sigma)) = \lambda(\sigma)\operatorname{Tr}(\rho(\sigma)) = \lambda(\sigma)\chi(\sigma) = \chi^*(\sigma)$.

::: pf-proof
linearity of trace.
:::

:::

::: pf-step
Hence $\chi^*$ is the character of $\lambda \otimes \rho$.

::: pf-proof
step [](#p1-s1-4){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #p1-s2}
The character $\chi^*$ is irreducible.

::: pf-proof

::: {.pf-step #p1-s2-1}
A character $\psi$ of a finite group over $\mathbb{C}$ is irreducible if and only if $\langle \psi, \psi \rangle = 1$.

::: pf-proof
character theory of finite groups over $\mathbb{C}$.
:::

:::

::: pf-step
Since $G$ is finite, for each $\sigma \in G$, $\sigma^{|G|} = e$, so $\lambda(\sigma)^{|G|} = \lambda(e) = 1$.

::: pf-proof
group homomorphism from a finite group.
:::

:::

::: {.pf-step #p1-s2-3}
Thus $\lambda(\sigma)$ is a root of unity in $\mathbb{C}$, so $|\lambda(\sigma)| = 1$ and $|\lambda(\sigma)|^2 = \lambda(\sigma)\overline{\lambda(\sigma)} = 1$.

::: pf-proof
roots of unity have absolute value $1$.
:::

:::

::: {.pf-step #p1-s2-4}
Compute the inner product:
\[
\langle \chi^*, \chi^* \rangle = \frac{1}{|G|} \sum_{\sigma \in G} \chi^*(\sigma)\overline{\chi^*(\sigma)} = \frac{1}{|G|} \sum_{\sigma \in G} \lambda(\sigma)\chi(\sigma)\overline{\lambda(\sigma)\chi(\sigma)} = \frac{1}{|G|} \sum_{\sigma \in G} |\lambda(\sigma)|^2 |\chi(\sigma)|^2.
\]

::: pf-proof
definition of the inner product of class functions.
:::

:::

::: {.pf-step #p1-s2-5}
Substituting $|\lambda(\sigma)|^2 = 1$ gives:
\[
\langle \chi^*, \chi^* \rangle = \frac{1}{|G|} \sum_{\sigma \in G} |\chi(\sigma)|^2 = \langle \chi, \chi \rangle.
\]

::: pf-proof
step [](#p1-s2-3){.pf-ref} and step [](#p1-s2-4){.pf-ref}.
:::

:::

::: {.pf-step #p1-s2-6}
Since $\chi$ is irreducible, $\langle \chi, \chi \rangle = 1$, so $\langle \chi^*, \chi^* \rangle = 1$.

::: pf-proof
step [](#p1-s2-5){.pf-ref} and irreducibility of $\chi$.
:::

:::

::: pf-step
Therefore $\chi^*$ is an irreducible character of $G$.

::: pf-proof
step [](#p1-s1){.pf-ref}, step [](#p1-s2-1){.pf-ref}, and step [](#p1-s2-6){.pf-ref}.
:::

:::

:::

:::

:::

**(b).**

::: pf

::: {.pf-step #p2-s1}
Pointwise similarity implies equality of characters $\chi_A = \chi_B$.

::: pf-proof

::: {.pf-step #p2-s1-1}
The characters of $A$ and $B$ are given by $\chi_A(\sigma) = \operatorname{Tr}(A(\sigma))$ and $\chi_B(\sigma) = \operatorname{Tr}(B(\sigma))$.

::: pf-proof
definition of the character of a matrix representation.
:::

:::

::: pf-step
For each $\sigma \in G$, $B(\sigma) = P(\sigma)^{-1}A(\sigma)P(\sigma)$.

::: pf-proof
hypothesis.
:::

:::

::: {.pf-step #p2-s1-3}
Since the trace is invariant under cyclic permutations and similarity transformations:
\[
\operatorname{Tr}(B(\sigma)) = \operatorname{Tr}\bigl(P(\sigma)^{-1}A(\sigma)P(\sigma)\bigr) = \operatorname{Tr}(A(\sigma)).
\]

::: pf-proof
cyclic property of trace: $\operatorname{Tr}(XY) = \operatorname{Tr}(YX)$ with $X = P(\sigma)^{-1}A(\sigma)$, $Y = P(\sigma)$.
:::

:::

::: pf-step
Hence $\chi_A(\sigma) = \chi_B(\sigma)$ for all $\sigma \in G$.

::: pf-proof
step [](#p2-s1-1){.pf-ref} and step [](#p2-s1-3){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #p2-s2}
Two complex representations of a finite group are isomorphic if and only if their characters are identical.

::: pf-proof

::: {.pf-step #p2-s2-1}
By Maschke's theorem, every complex representation of a finite group is completely reducible (a direct sum of irreducible representations).

::: pf-proof
Maschke's theorem for finite groups over $\mathbb{C}$.
:::

:::

::: {.pf-step #p2-s2-2}
The multiplicity of an irreducible representation $V_i$ in $V$ is uniquely determined by the character via $m_i = \langle \chi_V, \chi_i \rangle$.

::: pf-proof
orthogonality of irreducible characters.
:::

:::

::: {.pf-step #p2-s2-3}
Since $\chi_A = \chi_B$, $A$ and $B$ have the same irreducible constituents with the same multiplicities.

::: pf-proof
step [](#p2-s1){.pf-ref} and step [](#p2-s2-2){.pf-ref}.
:::

:::

::: pf-step
Thus $A \cong B$ as $\mathbb{C}[G]$-modules.

::: pf-proof
step [](#p2-s2-1){.pf-ref} and step [](#p2-s2-3){.pf-ref}.
:::

:::

::: pf-step
Consequently, there exists an invertible matrix $T \in \operatorname{GL}_n(\mathbb{C})$ such that $T^{-1}A(\sigma)T = B(\sigma)$ for all $\sigma \in G$.

::: pf-proof
isomorphism of matrix representations.
:::

:::

:::

:::

::: pf-qed
step [](#p1-s2){.pf-ref} (a) and step [](#p2-s2){.pf-ref} (b).
:::

:::
:::
