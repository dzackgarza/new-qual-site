---
schema: qual/card@1
id: P-6JCW5
kind: problem
title: $\GF(p^n)$ is the splitting field of $x^{p^n}-x$ over $\FF_p$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Splitting Fields
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
- Show that  $\GF(p^n)$ is the splitting field of $x^{p^n} - x \in \FF_p[x]$.
:::

::: {.solution}
Let
\[
f(x)=x^{p^n}-x\in\FF_p[x],
\]
and let $L$ be its splitting field over $\FF_p$.

::: pf

::: {.pf-step #s1}

The polynomial $f$ has exactly $p^n$ distinct roots in $L$.

::: pf-proof

Its derivative is
\[
f'(x)=p^n x^{p^n-1}-1=-1
\]
in characteristic $p$. Thus $\gcd(f,f')=1$, so $f$ is separable. Since $\deg f=p^n$ and $L$ is a splitting field, $f$ has exactly $p^n$ distinct roots in $L$.

:::

:::

::: {.pf-step #s2}

The root set
\[
S=\{a\in L:a^{p^n}=a\}
\]
is a subfield of $L$.

::: pf-proof

Clearly $0,1\in S$. If $a,b\in S$, then the Frobenius identity in characteristic $p$ gives
\[
(a-b)^{p^n}=a^{p^n}-b^{p^n}=a-b,
\]
so $a-b\in S$, and
\[
(ab)^{p^n}=a^{p^n}b^{p^n}=ab,
\]
so $ab\in S$. If $0\ne b\in S$, then
\[
(b^{-1})^{p^n}=(b^{p^n})^{-1}=b^{-1},
\]
so $b^{-1}\in S$. Hence $S$ is a field.

:::

:::

::: {.pf-step #s3}

The field $S$ has exactly $p^n$ elements and contains $\FF_p$.

::: pf-proof

By step [](#s1){.pf-ref}, $S$ is exactly the set of the $p^n$ distinct roots of $f$, so $|S|=p^n$. For $c\in\FF_p$, one has $c^p=c$, and iterating Frobenius gives $c^{p^n}=c$. Thus $\FF_p\subseteq S$.

:::

:::

::: {.pf-step #s4}

The splitting field $L$ equals $S$.

::: pf-proof

The splitting field $L$ is generated over $\FF_p$ by all roots of $f$. Those roots form the field $S$ by step [](#s2){.pf-ref} and already contain $\FF_p$ by step [](#s3){.pf-ref}. Hence adjoining them produces nothing larger than $S$, so $L=S$.

:::

:::

::: pf-step

Therefore $L\cong\GF(p^n)$, and $\GF(p^n)$ is the splitting field of $x^{p^n}-x$ over $\FF_p$.

::: pf-proof

By steps [](#s3){.pf-ref} and [](#s4){.pf-ref}, $L$ is a finite field with $p^n$ elements. Up to unique isomorphism over $\FF_p$, there is exactly one finite field of order $p^n$, denoted $\GF(p^n)$. Thus the splitting field is $\GF(p^n)$.

:::

:::

:::

:::
