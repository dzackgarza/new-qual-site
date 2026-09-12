---
schema: qual/card@1
id: P-EAGXS
kind: problem
title: The structure theorem for modules over a PID and conjugacy classes in $\mathrm{GL}(V)$
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Canonical Forms
  - Conjugacy
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
What is the connection between the structure theorem for modules over a PID and conjugacy classes in the general linear group over a field?
:::


::: {.solution}
Let $V$ be a finite-dimensional vector space over a field $F$, and let $T\in\operatorname{End}_F(V)$.

<1>1. The operator $T$ makes $V$ into an $F[t]$-module by
\[
f(t)\cdot v=f(T)v.
\]
::: {.proof}
Polynomial evaluation at $T$ is a ring homomorphism $F[t]\to\operatorname{End}_F(V)$, so this defines an $F[t]$-module structure. Conversely, an $F[t]$-module structure extending the given $F$-vector-space structure is determined by the action of $t$, hence by one linear operator.
:::

<1>2. Two operators $S,T\in\operatorname{End}_F(V)$ are conjugate in $\operatorname{GL}(V)$ iff the corresponding $F[t]$-modules are isomorphic.
::: {.proof}
An $F$-linear isomorphism $P:V\to V$ is $F[t]$-linear exactly when
\[
P(Tv)=S(Pv)
\]
for every $v$, i.e.
\[
PT=SP.
\]
Since $P$ is invertible, this is equivalent to $S=PTP^{-1}$.
:::

<1>3. Since $F[t]$ is a PID and $V$ is finitely generated and torsion as an $F[t]$-module, the structure theorem classifies $T$ up to conjugacy.
::: {.proof}
Finite-dimensionality over $F$ makes $V$ finitely generated over $F[t]$. Cayley-Hamilton gives a nonzero polynomial annihilating all of $V$, so the module is torsion. Hence
\[
V\cong\bigoplus_i F[t]/(f_i(t))
\]
with invariant factors
\[
f_1\mid f_2\mid\cdots\mid f_r.
\]
These invariant factors determine and are determined by the conjugacy class of $T$.
:::

<1>4. The companion matrices of the invariant factors give the rational canonical form of $T$.
::: {.proof}
On the cyclic module $F[t]/(f)$, multiplication by $t$ is represented in the standard cyclic basis by the companion matrix of $f$. Taking the direct sum over the invariant factors produces a canonical matrix representative of the conjugacy class.
:::

Thus conjugacy classes of linear operators are precisely isomorphism classes of the associated finite torsion $F[t]$-modules, and the PID structure theorem is the module-theoretic source of rational canonical form.
:::
