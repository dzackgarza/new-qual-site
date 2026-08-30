---
schema: qual/card@1
id: P-V3DIZ
kind: problem
title: The torsion submodule of a module over an integral domain
classification:
  areas:
  - algebra
  topics:
  - Torsion
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $R$ be a commutative ring and let $M$ be an $R$-module.
An element $x \in M$ is a *torsion element* if there exists a non-zero $r \in R$ such that $rx = 0$ (or equivalently, $\operatorname{Ann}_R(x) \neq (0)$). Let $\operatorname{Tor}(M) = \{x \in M : \operatorname{Ann}_R(x) \neq (0)\}$ denote the set of torsion elements of $M$.

1. Prove that if $R$ is an integral domain, then $\operatorname{Tor}(M)$ is an $R$-submodule of $M$.

2. Prove that the quotient module $M / \operatorname{Tor}(M)$ is torsion-free.

3. Show by example that $\operatorname{Tor}(M)$ need not be a submodule if $R$ has zero divisors.
:::

::: {.solution}
<1>1. Prove that $\operatorname{Tor}(M)$ is a submodule when $R$ is an integral domain: <2>1. For $x = 0 \in M$, $1 \cdot 0 = 0$ with $1 \neq 0$ in $R$, so $0 \in \operatorname{Tor}(M)$.
Proof: $1 \in \operatorname{Ann}_R(0)$.
<2>2. Let $x, y \in \operatorname{Tor}(M)$.
There exist non-zero $r_1, r_2 \in R \setminus \{0\}$ such that $r_1 x = 0$ and $r_2 y = 0$.
Proof: definition of torsion elements.
<2>3. Since $R$ is an integral domain and $r_1 \neq 0, r_2 \neq 0$, the product $r_1 r_2 \neq 0$ in $R$.
Proof: integral domains have no zero divisors.
<2>4. Compute $(r_1 r_2)(x + y)$:
\[
(r_1 r_2)(x + y) = r_2(r_1 x) + r_1(r_2 y) = r_2(0) + r_1(0) = 0.
\]
Proof: commutativity of $R$ and module axioms.
<2>5. Since $r_1 r_2 \neq 0$, $x + y \in \operatorname{Tor}(M)$.
Proof: <2>3 and <2>4. <2>6. For any $c \in R$ and $x \in \operatorname{Tor}(M)$ with $r_1 x = 0$ ($r_1 \neq 0$):
\[
r_1(cx) = c(r_1 x) = c(0) = 0.
\]
Thus $cx \in \operatorname{Tor}(M)$.
Proof: commutativity of $R$.
<2>7. Therefore $\operatorname{Tor}(M)$ is closed under addition and scalar multiplication, hence an $R$-submodule of $M$.
Proof: subspace/submodule criterion.

<1>2. Prove that $M / \operatorname{Tor}(M)$ is torsion-free: <2>1. Let $\bar{x} = x + \operatorname{Tor}(M) \in M / \operatorname{Tor}(M)$ be a torsion element.
Proof: setup.
<2>2. Then there exists some non-zero $s \in R \setminus \{0\}$ such that $s \bar{x} = \bar{0}$ in $M / \operatorname{Tor}(M)$.
Proof: definition of torsion in quotient module.
<2>3. This means $sx \in \operatorname{Tor}(M)$.
Proof: definition of cosets in quotient module.
<2>4. Since $sx \in \operatorname{Tor}(M)$, there exists some non-zero $t \in R \setminus \{0\}$ such that $t(sx) = 0$.
Proof: definition of $\operatorname{Tor}(M)$.
<2>5. Rewrite $t(sx) = (ts)x = 0$.
Since $R$ is an integral domain and $t \neq 0, s \neq 0$, the product $ts \neq 0$.
Proof: integral domain property.
<2>6. Since $(ts)x = 0$ with $ts \neq 0$, $x \in \operatorname{Tor}(M)$.
Proof: definition of $\operatorname{Tor}(M)$.
<2>7. Thus $\bar{x} = x + \operatorname{Tor}(M) = \bar{0}$ in $M / \operatorname{Tor}(M)$.
Proof: $x \in \operatorname{Tor}(M) \implies x + \operatorname{Tor}(M) = \operatorname{Tor}(M)$.
<2>8. Hence $\operatorname{Tor}(M / \operatorname{Tor}(M)) = \{\bar{0}\}$, so $M / \operatorname{Tor}(M)$ is torsion-free.
Proof: <2>1 through <2>7.

<1>3. Counterexample when $R$ is not an integral domain: <2>1. Let $R = \mathbb{Z}/6\mathbb{Z}$ and $M = R = \mathbb{Z}/6\mathbb{Z}$ as a module over itself.
Proof: $R$ has zero divisors since $2 \cdot 3 = 0$.
<2>2. The element $x = [2]$ is torsion because $3 \cdot [2] = [0]$ with $[3] \neq [0]$ in $R$.
Proof: $3 \cdot 2 = 6 \equiv 0 \pmod 6$.
<2>3. The element $y = [3]$ is torsion because $2 \cdot [3] = [0]$ with $[2] \neq [0]$ in $R$.
Proof: $2 \cdot 3 = 6 \equiv 0 \pmod 6$.
<2>4. However, their sum $x + y = [5]$ satisfies $\operatorname{Ann}_R([5]) = \{[0]\}$ because $\gcd(5, 6) = 1$ ($[5]$ is a unit in $\mathbb{Z}/6\mathbb{Z}$). Thus $x + y = [5] \notin \operatorname{Tor}(M)$.
Proof: unit elements have trivial annihilators.
<2>5. Therefore $\operatorname{Tor}(M)$ is not closed under addition when $R$ has zero divisors.
Proof: <2>2, <2>3, and <2>4.

<1>4. Conclusion: $\operatorname{Tor}(M)$ is a submodule and $M/\operatorname{Tor}(M)$ is torsion-free over any integral domain, but closure under addition fails in the presence of zero divisors.
Q.E.D. Proof: <1>1, <1>2, and <1>3.
:::
