---
schema: qual/card@1
id: P-ALGF09A
kind: problem
title: "Presentation of a semidirect product Z_m ⋊_φ Z_n"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $\phi: \mathbb{Z}_m \to \operatorname{Aut}(\mathbb{Z}_n)$ be a homomorphism, for some integers $m, n \geq 2$.
Let $G$ be the semidirect product $\mathbb{Z}_m \rtimes_\phi \mathbb{Z}_n$.
Find a presentation for $G$ by generators and relations and prove carefully that your presented group is isomorphic to $G$.
:::

::: {.solution}
<1>1. Setup of the semidirect product and candidate presentation:
<2>1. Let $G = \mathbb{Z}_n \rtimes_\phi \mathbb{Z}_m$, where the action $\phi: \mathbb{Z}_m \to \operatorname{Aut}(\mathbb{Z}_n) \cong (\mathbb{Z}/n\mathbb{Z})^\times$ is determined by an integer $k$ such that $\phi(1)(a) = a^k$, with $\gcd(k, n) = 1$ and $k^m \equiv 1 \pmod n$.
::: {.proof}
classification of automorphisms of cyclic groups.
:::
<2>2. We claim that $G$ has the presentation:
\[
\Gamma = \langle x, y \mid x^n = 1, \, y^m = 1, \, y x y^{-1} = x^k \rangle.
\]
::: {.proof}
candidate presentation for semidirect products of cyclic groups.
:::

<1>2. Existence of a surjective homomorphism $\Phi: \Gamma \to G$:
<2>1. In $G = \mathbb{Z}_n \rtimes_\phi \mathbb{Z}_m$, define the elements $\bar{x} = (1, 0)$ and $\bar{y} = (0, 1)$.
Compute the group relations in $G$:
\[
\bar{x}^n = (n \cdot 1, 0) = (0, 0) = e_G,
\]
\[
\bar{y}^m = (0, m \cdot 1) = (0, 0) = e_G,
\]
\[
\bar{y}\bar{x}\bar{y}^{-1} = (0, 1)(1, 0)(0, -1) = (\phi(1)(1), 1)(0, -1) = (k, 1)(0, -1) = (k, 0) = \bar{x}^k.
\]
::: {.proof}
definition of the semidirect product multiplication $(a_1, b_1)(a_2, b_2) = (a_1 + \phi(b_1)(a_2), b_1 + b_2)$.
:::
<2>2. By the universal property of group presentations, there exists a unique group homomorphism $\Phi: \Gamma \to G$ such that:
\[
\Phi(x) = \bar{x} = (1, 0) \quad \text{and} \quad \Phi(y) = \bar{y} = (0, 1).
\]
::: {.proof}
universal property of presentations.
:::
<2>3. Every element $(u, v) \in G$ satisfies $(u, v) = (u, 0)(0, v) = \bar{x}^u \bar{y}^v = \Phi(x^u y^v)$, so $\Phi$ is surjective.
Thus $|\Gamma| \ge |G| = mn$.
::: {.proof}
generation of $G$ by $\bar{x}$ and $\bar{y}$.
:::

<1>3. Upper bound on the order of $\Gamma$:
<2>1. The conjugation relation $y x y^{-1} = x^k$ can be written as the commutation relation $y x = x^k y$.
By induction, $y^j x^i = x^{i k^j} y^j$ for all $i, j \ge 0$.
::: {.proof}
induction on word length.
:::
<2>2. Using $y x = x^k y$ and the relations $x^n = 1$ and $y^m = 1$, every element of $\Gamma$ can be written in the normal form:
\[
x^i y^j \quad \text{for } 0 \le i < n \text{ and } 0 \le j < m.
\]
Thus $\Gamma = \{x^i y^j \mid 0 \le i < n, \, 0 \le j < m\}$.
::: {.proof}
moving all powers of $x$ to the left of powers of $y$.
:::
<2>3. Therefore $|\Gamma| \le mn$.
::: {.proof}
at most $mn$ distinct normal form words.
:::

<1>4. Bijectivity and Conclusion:
Since $|\Gamma| \le mn = |G|$ and $\Phi: \Gamma \to G$ is surjective, $\Phi$ is an isomorphism.
Thus $G \cong \langle x, y \mid x^n = 1, \, y^m = 1, \, y x y^{-1} = x^k \rangle$. Q.E.D.
::: {.proof}
<1>2 and <1>3.
:::
:::
