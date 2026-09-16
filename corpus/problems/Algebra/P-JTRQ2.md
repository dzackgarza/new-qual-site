---
schema: qual/card@1
id: P-JTRQ2
kind: problem
title: Injective module
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Homological Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
What is an injective module over a ring $R$?
State Baer's Criterion and the characterization of injective modules over PIDs (divisible modules).
:::

::: {.solution}
A left $R$-module $Q$ is **injective** if every homomorphism into $Q$ defined on a submodule extends across the containing module: whenever $A\hookrightarrow B$ is injective and $f:A\to Q$ is $R$-linear, there exists $g:B\to Q$ with $g|_A=f$. Equivalently, the contravariant functor
\[
\operatorname{Hom}_R(-,Q)
\]
is exact.

**Baer's criterion.** A left $R$-module $Q$ is injective if and only if every $R$-linear map
\[
f:I\to Q
\]
from a left ideal $I\subseteq R$ extends to an $R$-linear map $R\to Q$.

Now let $R$ be a commutative PID. An $R$-module $Q$ is **divisible** if, for every $0\ne r\in R$ and $q\in Q$, there exists $y\in Q$ with
\[
ry=q.
\]
Over a PID,
\[
Q\text{ is injective}\iff Q\text{ is divisible}.
\]
Indeed, every ideal is $(r)$. A homomorphism $f:(r)\to Q$ is determined by $q=f(r)$. Extending $f$ to $R$ is equivalent to finding $y=g(1)$ with $ry=q$, exactly the divisibility condition.

Thus over $\mathbb Z$ the injective modules are precisely the divisible abelian groups; examples include $\mathbb Q$, $\mathbb Q/\mathbb Z$, and the Prüfer $p$-groups. More generally, if $R$ is a PID, its fraction field $\operatorname{Frac}(R)$ is divisible and therefore injective as an $R$-module.
:::
