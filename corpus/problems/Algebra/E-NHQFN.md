---
schema: qual/card@1
id: E-NHQFN
kind: problem
title: Irreducible polynomial of every degree over $\mathbb{F}_{p}$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
  - Polynomials
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

::: {.problem}
20. Prove that for any positive integer $n$ there is an irreducible polynomial of degree $n$ over $\boldsymbol{F}_{p}$
:::

::: {.solution}
Fix a positive integer $n$, and work in an algebraic closure $\overline{\FF}_p$.

::: pf

::: pf-step
The set
\[
K=\{a\in\overline{\FF}_p:a^{p^n}=a\}
\]
is a field with exactly $p^n$ elements.

::: pf-proof
The polynomial
\[
f(x)=x^{p^n}-x
\]
has derivative $f'(x)=-1$, so it has no repeated roots. Since it splits in the algebraic closure and has degree $p^n$, it has exactly $p^n$ distinct roots; hence $|K|=p^n$.

If $a,b\in K$, then in characteristic $p$,
\[
(a+b)^{p^n}=a^{p^n}+b^{p^n}=a+b,
\]
and
\[
(ab)^{p^n}=a^{p^n}b^{p^n}=ab.
\]
Also $0,1\in K$, and if $0\neq a\in K$, then
\[
(a^{-1})^{p^n}=(a^{p^n})^{-1}=a^{-1}.
\]
Thus $K$ is a subfield of $\overline{\FF}_p$ with $p^n$ elements.
:::

:::

::: pf-step
The multiplicative group $K^\times$ is cyclic of order $p^n-1$.

::: pf-proof
The multiplicative group of every finite field is cyclic. Since $|K|=p^n$, its nonzero elements form a cyclic group of order $p^n-1$.
:::

:::

::: {.pf-step #alpha-generates-degree-n}
Let $\alpha$ generate $K^\times$. Then
\[
[\FF_p(\alpha):\FF_p]=n.
\]

::: pf-proof
Set
\[
d=[\FF_p(\alpha):\FF_p].
\]
Because $\FF_p(\alpha)\subseteq K$, it is a finite field with $p^d$ elements, so
\[
d\le n.
\]
Its multiplicative group has order $p^d-1$, and the order of $\alpha$ must divide this number. But $\alpha$ generates $K^\times$, so
\[
\operatorname{ord}(\alpha)=p^n-1.
\]
Hence
\[
p^n-1\mid p^d-1.
\]
If $d<n$, then $p^d-1<p^n-1$, impossible. Therefore $d=n$.
:::

:::

::: {.pf-step #min-poly-irreducible-degree-n}
The minimal polynomial of $\alpha$ over $\FF_p$ is irreducible of degree $n$.

::: pf-proof
By definition, the minimal polynomial $m_\alpha(x)\in\FF_p[x]$ is irreducible, and
\[
\deg m_\alpha=[\FF_p(\alpha):\FF_p].
\]
By step [](#alpha-generates-degree-n){.pf-ref}, this degree is $n$.
:::

:::

::: pf-step
Therefore for every positive integer $n$ there exists an irreducible polynomial of degree $n$ over $\FF_p$.

::: pf-proof
The polynomial $m_\alpha$ from step [](#min-poly-irreducible-degree-n){.pf-ref} is such a polynomial.
:::

:::

:::

:::
