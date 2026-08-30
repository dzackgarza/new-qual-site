---
title: Modules over a PID
order: 10
problems:
  topics:
  - Modules over PIDs
  - Structure Theorem
  - Torsion
---

# Modules over a PID

## Definitions

[[D-NQZUY]]

[[PR-TAPZF]]

[[FF-UYMWY]]

[[D-JUYFQ]]

[[PR-JBDUI]]

[[D-CRWZ7]]

[[FD-BVM37]]

[[D-4HEUB]]

[[FD-2EUYX]]

[[FD-GNRTS]]

[[D-HY7UU]]

[[FD-S2W5E]]

## The structure theorem

[[PR-DJZLY]]

[[PR-RIJSC]]

[[PR-UVUS6]]

[[FD-LHLDU]]

:::{.remark title="Free plus torsion"}
Every finitely generated module decomposes as $M \cong F_M \oplus M_t$ with $F_M$ free and $M_t$ torsion, and moreover $F_M \cong M/M_t$.

$M/M_t$ is torsion-free: if $r(m + M_t) = M_t$ then $rm$ is torsion, so $r'(rm) = 0$ for some $r'$, making $m$ torsion and $m + M_t$ the zero coset.

$F_M \cong M/M_t$: the sequence $0\to M_t\to M \to F\to 0$ gives $F \cong M/M_t$, and it splits because $F$ is free hence projective.

:::

## Ideals, and when they are free

[[PR-ASW5L]]

:::{.proof}
$\implies$:
Suppose $I$ is free with basis $B = \ts{\vector m_j}_{j\in J}$, and suppose $\abs B \geq 2$, so there are distinct $\vector m_1, \vector m_2 \in B$.
Since $R$ is commutative,
$$
\vector m_1 \vector m_2 - \vector m_2 \vector m_1 = \vector 0
,$$
which is a nontrivial dependence with coefficients $\alpha_1 = -m_2$ and $\alpha_2 = m_1$, both nonzero.
This contradicts $B$ being a basis, so $\abs B = 1$ and $I = \gens{\vector m}$ is principal.

$\impliedby$:
Suppose $I = \gens{\vector m}$ with $\vector m \neq 0$.
Every $x\in I$ is $\alpha\vector m$, and $\alpha \vector m = 0$ with $R$ a domain and $m \neq 0$ forces $\alpha = 0$.
So $\ts{\vector m}$ is independent and is a basis.

:::

## Algebraic properties

[[D-B5X33]]

[[PR-O5YUI]]
[[PR-BHUO6]]
[[PR-TGFTL]]

[[PR-LPJLD]]

[[PR-5PDNQ]]

[[PR-GXII2]]

[[PR-KX7L7]]
