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

::: {.problem}
Let $M$ be a finitely generated module over a PID $R$.

a. $M_t$ be the set of torsion elements of $M$, and show that $M_t$ is a submodule of $M$.

b. Show that $M/M_t$ is torsion free.

c. Prove that $M \cong M_t \oplus F$ where $F$ is a free module.
:::

::: {.solution}

::: pf

::: {.pf-step #part-a-submodule}
Part (a): Show that $M_t$ is a submodule of $M$:

::: pf-proof

::: {.pf-step #zero-in-mt}
$0 \in M_t$ because $1 \cdot 0 = 0$ with $1 \in R \setminus \{0\}$.

::: pf-proof
module identity axiom.
:::

:::

::: {.pf-step #mt-closed-subtraction}
Let $x, y \in M_t$. There exist non-zero $r, s \in R \setminus \{0\}$ such that $rx = 0$ and $sy = 0$.
Since $R$ is an integral domain, the product $rs \in R \setminus \{0\}$ is non-zero.
Compute:
\[
(rs)(x - y) = s(rx) - r(sy) = s(0) - r(0) = 0.
\]
Thus $x - y \in M_t$.

::: pf-proof
commutativity and zero-divisor freeness of $R$.
:::

:::

::: {.pf-step #mt-closed-scalar}
For any $a \in R$ and $x \in M_t$ with $rx = 0$ ($r \neq 0$):
\[
r(ax) = a(rx) = a(0) = 0.
\]
Thus $ax \in M_t$.

::: pf-proof
$R$-action on modules.
:::

:::

::: pf-step
Therefore $M_t$ is an $R$-submodule of $M$.

::: pf-proof
submodule criterion (step [](#zero-in-mt){.pf-ref} through step [](#mt-closed-scalar){.pf-ref}).
:::

:::

:::

:::

::: {.pf-step #part-b-torsion-free}
Part (b): Show that $M/M_t$ is torsion-free:

::: pf-proof

::: pf-step
Let $\bar{m} = m + M_t \in M/M_t$ and suppose $r \bar{m} = \bar{0}$ for some $r \in R \setminus \{0\}$.

::: pf-proof
setup for torsion in quotient.
:::

:::

::: pf-step
The condition $r \bar{m} = \bar{0}$ means $rm \in M_t$.

::: pf-proof
definition of cosets in quotient module.
:::

:::

::: pf-step
By definition of $M_t$, there exists a non-zero $s \in R \setminus \{0\}$ such that $s(rm) = 0$.

::: pf-proof
definition of torsion elements.
:::

:::

::: {.pf-step #m-in-mt-quotient-zero}
Since $R$ is an integral domain, $sr \in R \setminus \{0\}$.
Since $(sr)m = s(rm) = 0$, we have $m \in M_t$, which means $\bar{m} = \bar{0}$ in $M/M_t$.

::: pf-proof
$R$ has no non-zero zero divisors.
:::

:::

::: pf-step
Thus $M/M_t$ contains no non-zero torsion elements, so $M/M_t$ is torsion-free.

::: pf-proof
Step [](#m-in-mt-quotient-zero){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #part-c-splitting}
Part (c): Splitting of $M \cong M_t \oplus F$:

::: pf-proof

::: pf-step
Since $M$ is a finitely generated $R$-module, the quotient module $M/M_t$ is also finitely generated over $R$.

::: pf-proof
homomorphic image of a finitely generated module is finitely generated.
:::

:::

::: pf-step
Over a PID $R$, every finitely generated torsion-free module is free.
Since $M/M_t$ is finitely generated and torsion-free (by Part (b)), $F = M/M_t$ is a free $R$-module of finite rank.

::: pf-proof
Structure Theorem for finitely generated modules over a PID.
:::

:::

::: pf-step
Consider the canonical short exact sequence:
\[
0 \longrightarrow M_t \xrightarrow{i} M \xrightarrow{\pi} M/M_t \longrightarrow 0.
\]
Since $M/M_t \cong F$ is free (hence projective), the sequence splits: there exists an $R$-module homomorphism $\sigma: M/M_t \to M$ such that $\pi \circ \sigma = \operatorname{id}_{M/M_t}$.

::: pf-proof
projectivity of free modules.
:::

:::

::: pf-step
By the Splitting Lemma, $M = M_t \oplus \operatorname{im}(\sigma) \cong M_t \oplus F$, where $F \cong M/M_t$ is a free $R$-module.

::: pf-proof
Splitting Lemma for module exact sequences.
:::

:::

:::

:::

::: pf-step
Conclusion:
$M_t \le M$ is a submodule, $M/M_t$ is torsion-free, and $M \cong M_t \oplus F$ with $F$ free. Q.E.D.

::: pf-proof
Step [](#part-a-submodule){.pf-ref} through step [](#part-c-splitting){.pf-ref}.
:::

:::

:::

:::
