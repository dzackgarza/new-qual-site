---
schema: qual/card@1
id: P-ALGS13C
kind: problem
title: Elementary divisor $p^k$ yields a submodule isomorphic to $A/(p)$
classification:
  areas:
  - algebra
  topics:
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Let $A$ be a PID and let $M$ be a torsion finitely generated $A$-module.
Suppose that $p \in A \setminus \{0\}$ is a prime element such that $p^k$ is one of the elementary divisors of $M$ for some $k \geq 1$.
Show that $M$ has a submodule which is isomorphic to $A/(p)$ as an $A$-module.
:::

::: {.solution}
<1>1. By the elementary-divisor decomposition, $M$ has a direct summand isomorphic to $A/(p^k)$.
::: {.proof}
Since $p^k$ is an elementary divisor of the finitely generated torsion $A$-module $M$, the structure theorem over a PID gives a decomposition
\[
M\cong A/(p^k)\oplus M'
\]
for some $A$-module $M'$.
:::

<1>2. Inside $A/(p^k)$, let $x$ be the class of $p^{k-1}$.
::: {.proof}
The class $x=p^{k-1}+(p^k)$ is well-defined.
Since $p^k\nmid p^{k-1}$ in the domain $A$, we have $x\neq 0$.
:::

<1>3. The annihilator of $x$ is exactly the ideal $(p)$.
::: {.proof}
For $a\in A$,
\[
ax=0\text{ in }A/(p^k)
\iff p^k\mid ap^{k-1}.
\]
Because $A$ is a domain and $p$ is prime, this is equivalent to $p\mid a$.
Hence
\[
\operatorname{Ann}_A(x)=(p).
\]
:::

<1>4. Therefore the cyclic submodule $Ax$ is isomorphic to $A/(p)$.
::: {.proof}
The map
\[
A\longrightarrow Ax,\qquad a\longmapsto ax
\]
is surjective and has kernel $\operatorname{Ann}_A(x)=(p)$ by <1>3. The first isomorphism theorem gives
\[
Ax\cong A/(p).
\]
:::

<1>5. Viewing $A/(p^k)$ as a direct summand of $M$, the submodule $Ax$ is a submodule of $M$ isomorphic to $A/(p)$.
::: {.proof}
This follows from <1>1 and <1>4.
:::
:::
