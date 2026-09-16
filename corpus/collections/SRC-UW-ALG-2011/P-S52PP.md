---
schema: qual/card@1
id: P-S52PP
kind: problem
title: A commutative integral domain is a field if and only if it is semisimple if
  and only if every module is projective
classification:
  areas:
  - algebra
  topics:
  - Integral Domains
  - Semisimplicity
  - Projective Modules
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $R$ be a commutative integral domain.
Show that the following are equivalent:

- $R$ is a field;

- $R$ is a semi-simple ring;

- Any $R$-module is projective.
:::


::: {.solution}
<1>1. If $R$ is a field, then $R$ is semisimple.
::: {.proof}
Viewed as a left module over itself, a field $R$ has only the submodules $0$ and $R$, because its left ideals are precisely its ideals. Thus ${}_RR$ is simple. A simple module is semisimple, so $R$ is a semisimple ring.
:::

<1>2. If $R$ is semisimple, then every $R$-module is projective.
::: {.proof}
Let $M$ be an $R$-module. Choose a surjection
\[
\pi:F\twoheadrightarrow M
\]
from a free module $F$. Since $R$ is semisimple, the regular module ${}_RR$ is semisimple. Therefore every direct sum of copies of $R$, in particular the free module $F$, is semisimple. Hence every submodule of $F$ is a direct summand; in particular,
\[
F=\ker\pi\oplus C
\]
for some submodule $C$.

The restriction
\[
\pi|_C:C\longrightarrow M
\]
is an isomorphism: it is injective because $C\cap\ker\pi=0$, and it is surjective because every $f\in F$ can be written $f=k+c$ with $k\in\ker\pi$, so $\pi(f)=\pi(c)$. Thus the surjection $F\twoheadrightarrow M$ splits. Since every surjection from a free module onto $M$ splits, $M$ is projective.
:::

<1>3. If every $R$-module is projective, then $R$ is a field.
::: {.proof}
Let $0\ne a\in R$. The module $R/(a)$ is projective by hypothesis, so the short exact sequence
\[
0\longrightarrow (a)\longrightarrow R\longrightarrow R/(a)\longrightarrow0
\]
splits. Hence
\[
R=(a)\oplus I
\]
for some ideal $I$.

Let $e\in(a)$ be the component of $1$ under this direct-sum decomposition, so
\[
1=e+f,
\qquad e\in(a),\ f\in I.
\]
Because $(a)$ and $I$ are ideals,
\[
ef\in(a)\cap I=0.
\]
Therefore
\[
e=e(e+f)=e^2.
\]
Thus $e$ is an idempotent. Since $(a)\ne0$, its direct-summand projection is nonzero, so $e\ne0$. In an integral domain the only idempotents are $0$ and $1$, because
\[
e^2=e\implies e(e-1)=0.
\]
Hence $e=1$. Since $e\in(a)$, we have $1\in(a)$, so $(a)=R$ and $a$ is a unit.

Every nonzero element of $R$ is therefore invertible, so $R$ is a field.
:::

<1>4. Consequently the three conditions are equivalent.
::: {.proof}
Steps <1>1, <1>2, and <1>3 give the cycle
\[
R\text{ field}\Longrightarrow R\text{ semisimple}
\Longrightarrow\text{every }R\text{-module projective}
\Longrightarrow R\text{ field}.
\]
:::
:::
