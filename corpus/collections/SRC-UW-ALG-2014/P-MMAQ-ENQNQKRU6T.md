---
schema: qual/card@1
id: P-MMAQ-ENQNQKRU6T
kind: problem
title: 'Rings with $a^2=a$: Jacobson radical, characteristic, commutativity, and finite
  rings isomorphic to $(\ZZ/2\ZZ)^d$'
classification:
  areas:
  - algebra
  topics:
  - Jacobson Radical
  - Characteristic
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $R$ be a ring with the property that $a^2=a$ for all $a\in R$.

- Compute the Jacobson radical of $R$.

- What is the characteristic of $R$?

- Prove that $R$ is commutative.

- Prove that if $R$ is finite, then $R$ is isomorphic (as a ring) to $(\mathbb Z/2\mathbb Z)^d$ for some $d$.
:::


::: {.solution}
<1>1. The Jacobson radical of \(R\) is zero.
::: {.proof}
Let \(x\in J(R)\). Since every element is idempotent,
\[
x^2=x,
\]
so
\[
x(1-x)=0.
\]
Because \(x\in J(R)\), the element \(1-x\) is a unit. Multiplying by its inverse gives \(x=0\). Hence
\[
J(R)=0.
\]
:::

<1>2. The characteristic of \(R\) is \(2\) (unless \(R=0\), in which case the usual convention gives characteristic \(1\)).
::: {.proof}
Applying the identity \(a^2=a\) to \(a=1+1\) gives
\[
(1+1)^2=1+1.
\]
Thus
\[
4\cdot1=2\cdot1,
\]
so \(2\cdot1=0\). For a nonzero unital ring this means \(\operatorname{char}R=2\).
:::

<1>3. The ring \(R\) is commutative.
::: {.proof}
For arbitrary \(a,b\in R\),
\[
(a+b)^2=a+b.
\]
Expanding and using \(a^2=a\), \(b^2=b\), we obtain
\[
ab+ba=0.
\]
By <1>2, \(-ba=ba\), so \(ab=ba\). Hence \(R\) is commutative.
:::

<1>4. If \(R\) is finite, then
\[
R\cong (\mathbb Z/2\mathbb Z)^d
\]
for some \(d\ge0\).
::: {.proof}
Because \(R\) is finite, it has only finitely many maximal ideals, say
\[
\mathfrak m_1,\dots,\mathfrak m_d.
\]
In any commutative ring,
\[
J(R)=\bigcap_{i=1}^d \mathfrak m_i.
\]
By <1>1 this intersection is zero. Distinct maximal ideals are comaximal, so the Chinese remainder theorem gives an isomorphism
\[
R\cong \prod_{i=1}^d R/\mathfrak m_i.
\]
Each quotient \(R/\mathfrak m_i\) is a field and still satisfies \(x^2=x\) for every element \(x\). If \(0\ne x\) in such a field, then
\[
x(x-1)=0
\]
forces \(x=1\). Thus each residue field has exactly two elements, so
\[
R/\mathfrak m_i\cong\mathbb F_2.
\]
Therefore
\[
R\cong \mathbb F_2^d\cong(\mathbb Z/2\mathbb Z)^d.
\]
:::
:::
