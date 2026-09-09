---
schema: qual/card@1
id: P-IAW24
kind: problem
title: Constructible numbers
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Geometry
  - Galois Theory
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
Which numbers are constructible?
Give an example of a non-constructible number whose degree is nevertheless a power of 2.
:::


::: {.solution}
A real algebraic number $\alpha$ is **constructible** by straightedge and compass iff there is a tower of fields
\[
\QQ=K_0\subset K_1\subset\cdots\subset K_r
\]
with
\[
[K_i:K_{i-1}]=2
\]
for every $i$, such that $\alpha\in K_r\subseteq\RR$.

Equivalently, $\alpha$ lies in the smallest subfield of $\RR$ obtained from $\QQ$ by repeatedly adjoining square roots of positive elements.

<1>1. Every constructible algebraic number has degree a power of $2$ over $\QQ$.
::: {.proof}
If $\alpha\in K_r$, then
\[
[\QQ(\alpha):\QQ]\mid[K_r:\QQ]=2^r
\]
by the tower law. Hence its degree is a power of $2$.
:::

<1>2. The converse is false.
::: {.proof}
Let $\alpha$ be a real root of
\[
f(x)=x^4-x-1.
\]
The polynomial is irreducible over $\QQ$: modulo $2$ it becomes
\[
x^4+x+1,
\]
which has no root in $\FF_2$ and is not divisible by the only irreducible quadratic $x^2+x+1$, so it is irreducible over $\FF_2$, hence over $\QQ$.
Thus
\[
[\QQ(\alpha):\QQ]=4.
\]

The discriminant of $f$ is
\[
-283,
\]
which is not a square. Its cubic resolvent is
\[
y^3+4y-1,
\]
which is irreducible over $\QQ$ by the rational-root test. For an irreducible quartic, irreducibility of the cubic resolvent implies that the Galois group is $A_4$ or $S_4$; the nonsquare discriminant excludes $A_4$. Hence the Galois closure has Galois group $S_4$.

If $\alpha$ were constructible, it would lie in an iterated quadratic extension; the normal closure of such an extension has degree a power of $2$, so the Galois group of the normal closure of $\QQ(\alpha)$ would be a $2$-group. But $S_4$ has order $24$, not a power of $2$. Contradiction.
:::

Thus degree a power of $2$ is necessary, but not sufficient, for constructibility.
:::
