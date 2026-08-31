---
schema: qual/card@1
id: P-RZ2JV
kind: problem
title: Maximal submodules are those with simple quotient, and the roots of unity have
  no maximal submodule
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Maximal Ideals
  - Roots of Unity
relations: []
review: draft
---

::: problem
Let $R$ be a ring, and let $M$ be an $R$-module. An $R$-submodule $N \subset M$ is called **maximal** if $N \ne M$ and there is no $R$-submodule $P$ satisfying $N \subsetneq P \subsetneq M$.

(a) Show that an $R$-submodule $N$ of $M$ is maximal if and only if the quotient module $M/N$ is a **simple** $R$-module (that is, $M/N \ne \{0\}$ and $M/N$ has no submodules other than $\{0\}$ and $M/N$).

(b) Let $M$ be a $\mathbb{Z}$-module (an abelian group). Show that a submodule $N \subseteq M$ is maximal if and only if the quotient $|M/N| = p$ for some prime number $p$.

(c) Let $M = \mu_\infty = \{z \in \mathbb{C}^\times : z^n = 1 \text{ for some } n \in \mathbb{Z}^+\}$ be the multiplicative group of all complex roots of unity, viewed as a $\mathbb{Z}$-module. Show that $M$ has no maximal $\mathbb{Z}$-submodules.
:::

::: solution
**Goal:** Characterize maximal submodules via simplicity of quotients in (a), deduce prime-order quotients for abelian groups in (b), and prove that the divisible group of roots of unity has no maximal submodules in (c).

<1>1. Part (a): $N \subset M$ is maximal if and only if $M/N$ is simple.
::: {.proof}
    <2>1. By the Submodule Correspondence Theorem (Lattice Isomorphism Theorem for modules), the canonical quotient projection $\pi: M \to M/N$ induces an inclusion-preserving bijection between the set of submodules of $M$ containing $N$ and the set of submodules of $M/N$:
    $$P \longleftrightarrow P/N = \pi(P).$$
    <2>2. Under this correspondence, proper intermediate submodules $N \subsetneq P \subsetneq M$ correspond bijectively to non-zero proper submodules $\{0\} \subsetneq P/N \subsetneq M/N$.
    <2>3. $N$ is maximal if and only if $N \ne M$ and no such intermediate submodule $P$ exists.
    <2>4. This occurs if and only if $M/N \ne \{0\}$ and $M/N$ contains no submodules other than $\{0\}$ and $M/N$, which is the definition of $M/N$ being a simple $R$-module.

:::

<1>2. Part (b): A $\mathbb{Z}$-submodule $N \subseteq M$ is maximal if and only if $|M/N| = p$ is prime.
::: {.proof}
    <2>1. A $\mathbb{Z}$-module is an abelian group, and $\mathbb{Z}$-submodules are subgroups.
    <2>2. By Part (a), $N$ is maximal if and only if $A = M/N$ is a simple abelian group.
    <2>3. ($\impliedby$): If $|A| = p$ is prime, then by Lagrange's Theorem the only subgroups of $A$ are $\{0\}$ and $A$. Since $p \ge 2$, $A \ne \{0\}$, so $A$ is simple.
    <2>4. ($\implies$): Suppose $A$ is a simple abelian group. Since $A \ne \{0\}$, choose a non-zero element $x \in A \setminus \{0\}$.
    <2>5. The cyclic subgroup $\langle x \rangle \le A$ is a non-zero submodule of $A$. By simplicity, $\langle x \rangle = A$, so $A$ is cyclic.
    <2>6. If $A \cong \mathbb{Z}$, then the subgroup $\langle 2x \rangle \cong 2\mathbb{Z}$ is a non-zero proper subgroup of $A$, contradicting simplicity. Thus $A$ must be finite.
    <2>7. Since $A$ is finite cyclic, $A \cong \mathbb{Z}/n\mathbb{Z}$ for some integer $n \ge 2$.
    <2>8. If $n$ is composite, let $p$ be a prime divisor of $n$ with $1 < p < n$. The subgroup $\langle (n/p) x \rangle$ has order $p$, so $\{0\} \subsetneq \langle (n/p) x \rangle \subsetneq A$, contradicting simplicity.
    <2>9. Therefore $n = p$ must be prime, so $|M/N| = |A| = p$.

:::

<1>3. Part (c): $M = \mu_\infty$ has no maximal $\mathbb{Z}$-submodules.
::: {.proof}
    <2>1. Suppose for contradiction that $N \subset M$ is a maximal $\mathbb{Z}$-submodule (subgroup).
    <2>2. By Part (b), the quotient group $M/N$ has prime order $|M/N| = p$.
    <2>3. In any finite group of order $p$, every element raised to the power $p$ is the identity: for all $x \in M$, $(x N)^p = x^p N = N$, which implies $x^p \in N$.
    <2>4. We show that $M$ is $p$-divisible: let $x \in M$. By definition of $\mu_\infty$, $x^m = 1$ for some integer $m \ge 1$.
    <2>5. In $\mathbb{C}$, the polynomial $z^p - x = 0$ has $p$ solutions. Let $y \in \mathbb{C}^\times$ be any solution, so $y^p = x$.
    <2>6. Then $y^{p m} = (y^p)^m = x^m = 1$, which proves that $y \in \mu_\infty = M$.
    <2>7. Thus every element $x \in M$ can be written as $x = y^p$ for some $y \in M$.
    <2>8. Applying <2>3 to $y \in M$, we have $x = y^p \in N$.
    <2>9. This implies $M \subseteq N$, so $N = M$, which contradicts the definition of a maximal submodule ($N \subsetneq M$).
    <2>10. Thus no maximal $\mathbb{Z}$-submodule of $M$ exists.

:::

<1>4. Conclusion:
::: {.proof}
    Maximal submodules correspond to simple quotients, simple abelian groups are cyclic of prime order, and the divisible group of roots of unity possesses no maximal submodules.
:::
:::
