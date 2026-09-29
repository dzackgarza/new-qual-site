---
schema: qual/card@1
id: P-APAF11F
kind: problem
title: Ordered commutative ring is an integral domain; positive cone
classification:
  areas:
  - applied-algebra
  topics:
  - Integral Domains
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $\langle A,+,\cdot\rangle$ be a commutative ring with identity $1$ and let $<$ be a linear order on $A$ such that for all $a,b,x$ in $A$
\begin{align*}
\text{(I)}\quad &a<b\Rightarrow a+x<b+x,\\
\text{(II)}\quad &a<b,\ 0<x\Rightarrow a\cdot x<b\cdot x.
\end{align*}

(a) Prove that $\langle A,+,\cdot\rangle$ is an integral domain.

(b) Let $A^+=\{a\in A:0<a\}$.
Prove the following:

(i) $A^+$ is closed under multiplication and addition.

(ii) If $a\in A$, then exactly one of the following holds: $a\in A^+$, $-a\in A^+$, $a=0$.

(iii) $1\in A^+$.
:::

::: {.solution}
We use the standard convention implicit in the problem that the identity is nonzero, $1\ne0$.

::: pf

::: {.pf-step #s1}

For every $a\in A$, exactly one of
\[
a>0,\qquad a=0,\qquad -a>0
\]
holds.

::: pf-proof

By linearity of the order, exactly one of $a>0$, $a=0$, or $a<0$ holds. If $a<0$, adding $-a$ to both sides by (I) gives
\[
0<-a.
\]
Conversely, if $-a>0$, adding $a$ gives $a<0$. Hence the three alternatives above are exactly the trichotomy alternatives, so precisely one holds. This proves part (b)(ii).

:::

:::

::: {.pf-step #s2}

The set
\[
A^+=\{a\in A:0<a\}
\]
is closed under addition.

::: pf-proof

Let $a,b\in A^+$. From $0<a$, condition (I) with $x=b$ gives
\[
b<a+b.
\]
Since $0<b$, transitivity yields
\[
0<a+b.
\]
Thus $a+b\in A^+$.

:::

:::

::: {.pf-step #s3}

The set $A^+$ is closed under multiplication.

::: pf-proof

If $a,b\in A^+$, then $0<a$ and $0<b$. Apply (II) to $0<a$ with the positive multiplier $b$:
\[
0\cdot b<a\cdot b.
\]
Hence $0<ab$, so $ab\in A^+$. Together with step [](#s2){.pf-ref} this proves part (b)(i).

:::

:::

::: {.pf-step #s4}

The ring $A$ has no zero divisors.

::: pf-proof

Suppose $ab=0$ and $b\ne0$. By step [](#s1){.pf-ref}, either $b>0$ or $-b>0$; replacing $b$ by $-b$ if necessary, we may assume $b>0$.
If $a\ne0$, then again by step [](#s1){.pf-ref} either $a>0$ or $-a>0$.
If $a>0$, step [](#s3){.pf-ref} gives
\[
0<ab=0,
\]
a contradiction. If $-a>0$, then step [](#s3){.pf-ref} gives
\[
0<(-a)b=-(ab)=0,
\]
again a contradiction. Therefore $a=0$.
Thus $ab=0$ implies $a=0$ or $b=0$, so $A$ has no zero divisors.

:::

:::

::: pf-step

Therefore $A$ is an integral domain.

::: pf-proof

By hypothesis $A$ is a commutative ring with nonzero identity, and step [](#s4){.pf-ref} shows that it has no zero divisors. This is exactly the definition of an integral domain. This proves part (a).

:::

:::

::: pf-step

One has
\[
1\in A^+.
\]

::: pf-proof

Since $1\ne0$, step [](#s1){.pf-ref} says that either $1>0$ or $-1>0$. Suppose $-1>0$. By multiplicative closure from step [](#s3){.pf-ref},
\[
(-1)(-1)=1>0.
\]
Then both $1$ and $-1$ lie in $A^+$, contradicting the exclusivity in step [](#s1){.pf-ref} applied to $a=1$. Hence $-1$ cannot be positive, so $1>0$. This proves part (b)(iii).

:::

:::

:::

:::
