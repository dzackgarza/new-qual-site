---
schema: qual/card@1
id: P-EPDRU
kind: problem
title: The torsion submodule of a finitely generated module over a PID splits as a
  direct summand
classification:
  areas:
  - algebra
  topics:
  - Torsion
  - Free Modules
  - Structure Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $M$ be a finitely generated module over a PID $R$.

a. $M_t$ be the set of torsion elements of $M$, and show that $M_t$ is a submodule of $M$.

b. Show that $M/M_t$ is torsion free.

c. Prove that $M \cong M_t \oplus F$ where $F$ is a free module.
:::

::: {.solution}
<1>1. Part (a): Show that $M_t$ is a submodule of $M$:
<2>1. $0 \in M_t$ because $1 \cdot 0 = 0$ with $1 \in R \setminus \{0\}$.
::: {.proof}
module identity axiom.
:::
<2>2. Let $x, y \in M_t$. There exist non-zero $r, s \in R \setminus \{0\}$ such that $rx = 0$ and $sy = 0$.
Since $R$ is an integral domain, the product $rs \in R \setminus \{0\}$ is non-zero.
Compute:
\[
(rs)(x - y) = s(rx) - r(sy) = s(0) - r(0) = 0.
\]
Thus $x - y \in M_t$.
::: {.proof}
commutativity and zero-divisor freeness of $R$.
:::
<2>3. For any $a \in R$ and $x \in M_t$ with $rx = 0$ ($r \neq 0$):
\[
r(ax) = a(rx) = a(0) = 0.
\]
Thus $ax \in M_t$.
::: {.proof}
$R$-action on modules.
:::
<2>4. Therefore $M_t$ is an $R$-submodule of $M$.
::: {.proof}
submodule criterion (<2>1 through <2>3).
:::

<1>2. Part (b): Show that $M/M_t$ is torsion-free:
<2>1. Let $\bar{m} = m + M_t \in M/M_t$ and suppose $r \bar{m} = \bar{0}$ for some $r \in R \setminus \{0\}$.
::: {.proof}
setup for torsion in quotient.
:::
<2>2. The condition $r \bar{m} = \bar{0}$ means $rm \in M_t$.
::: {.proof}
definition of cosets in quotient module.
:::
<2>3. By definition of $M_t$, there exists a non-zero $s \in R \setminus \{0\}$ such that $s(rm) = 0$.
::: {.proof}
definition of torsion elements.
:::
<2>4. Since $R$ is an integral domain, $sr \in R \setminus \{0\}$.
Since $(sr)m = s(rm) = 0$, we have $m \in M_t$, which means $\bar{m} = \bar{0}$ in $M/M_t$.
::: {.proof}
$R$ has no non-zero zero divisors.
:::
<2>5. Thus $M/M_t$ contains no non-zero torsion elements, so $M/M_t$ is torsion-free.
::: {.proof}
<2>4.
:::

<1>3. Part (c): Splitting of $M \cong M_t \oplus F$:
<2>1. Since $M$ is a finitely generated $R$-module, the quotient module $M/M_t$ is also finitely generated over $R$.
::: {.proof}
homomorphic image of a finitely generated module is finitely generated.
:::
<2>2. Over a PID $R$, every finitely generated torsion-free module is free.
Since $M/M_t$ is finitely generated and torsion-free (by Part (b)), $F = M/M_t$ is a free $R$-module of finite rank.
::: {.proof}
Structure Theorem for finitely generated modules over a PID.
:::
<2>3. Consider the canonical short exact sequence:
\[
0 \longrightarrow M_t \xrightarrow{i} M \xrightarrow{\pi} M/M_t \longrightarrow 0.
\]
Since $M/M_t \cong F$ is free (hence projective), the sequence splits: there exists an $R$-module homomorphism $\sigma: M/M_t \to M$ such that $\pi \circ \sigma = \operatorname{id}_{M/M_t}$.
::: {.proof}
projectivity of free modules.
:::
<2>4. By the Splitting Lemma, $M = M_t \oplus \operatorname{im}(\sigma) \cong M_t \oplus F$, where $F \cong M/M_t$ is a free $R$-module.
::: {.proof}
Splitting Lemma for module exact sequences.
:::

<1>4. Conclusion:
$M_t \le M$ is a submodule, $M/M_t$ is torsion-free, and $M \cong M_t \oplus F$ with $F$ free. Q.E.D.
::: {.proof}
<1>1 through <1>3.
:::
:::
