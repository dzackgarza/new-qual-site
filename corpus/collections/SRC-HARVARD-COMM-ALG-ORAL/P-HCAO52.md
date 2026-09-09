---
schema: qual/card@1
id: P-HCAO52
kind: problem
title: A surjective endomorphism of a Noetherian ring is an automorphism
classification:
  areas:
  - algebra
  topics:
  - Noetherian Rings
  - Homomorphisms
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $A$ be a Noetherian ring.
Show that every surjective ring endomorphism $f:A\to A$ is an automorphism.
:::

::: solution
Let
\[
K_n=\ker(f^n),\qquad n\ge1.
\]
Then $K_1\subseteq K_2\subseteq\cdots$ is an ascending chain of ideals.

<1>1. Since $A$ is Noetherian, the chain stabilizes: for some $n$,
\[
K_n=K_{n+1}.
\]
::: proof
This is the ascending chain condition on ideals.
:::

<1>2. The kernel of $f$ is zero.
::: proof
Let $a\in\ker f$. Surjectivity of $f^n$ gives $b\in A$ with $f^n(b)=a$.
Then
\[
f^{n+1}(b)=f(a)=0,
\]
so $b\in K_{n+1}=K_n$. Hence $a=f^n(b)=0$.
:::

Thus $f$ is injective as well as surjective, hence an automorphism.
:::
