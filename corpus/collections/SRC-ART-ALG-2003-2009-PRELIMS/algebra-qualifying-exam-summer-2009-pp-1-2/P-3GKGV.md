---
schema: qual/card@1
id: P-3GKGV
kind: problem
title: Quotients of Artinian rings, Artinian domains are fields, and primes are maximal
classification:
  areas:
  - prelim
  topics:
  - Artinian Rings
  - Rings
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
A ring is called left (resp.
right) Artinian if every descending chain of left (resp.
right) ideals $I_1\supset I_2\supset I_3\cdots$ eventually terminates (i.e. there is some $N$ such that $I_k=I_N$ for $k\ge N$). A ring is called Artinian if it is both left and right Artinian.
a. Let $A$ be a left Artinian ring and suppose that $f: A\to R$ is a surjective homomorphism.
Prove that $R$ is left Artinian.
b. Show that an Artinian integral domain $A$ is a field.
(Hint: for a nonzero element $a\in A$, consider the ideals $(a),(a^2),(a^3),\dots$.)
c. Show that every prime ideal in a commutative Artinian ring is maximal.
:::

::: {.solution}
<1>1. A surjective homomorphic image of a left Artinian ring is left Artinian.
::: {.proof}
Let
\[
J_1\supseteq J_2\supseteq J_3\supseteq\cdots
\]
be a descending chain of left ideals of \(R\). Since \(f:A\to R\) is surjective, each preimage \(f^{-1}(J_i)\) is a left ideal of \(A\), and
\[
f^{-1}(J_1)\supseteq f^{-1}(J_2)\supseteq f^{-1}(J_3)\supseteq\cdots.
\]
Because \(A\) is left Artinian, there is \(N\) such that
\[
f^{-1}(J_i)=f^{-1}(J_N)
\qquad(i\ge N).
\]
Applying \(f\) and using surjectivity gives
\[
J_i=f(f^{-1}(J_i))=f(f^{-1}(J_N))=J_N
\qquad(i\ge N).
\]
Thus every descending chain of left ideals of \(R\) stabilizes.
:::

<1>2. Every Artinian integral domain is a field.
::: {.proof}
Let \(A\) be an Artinian integral domain and let \(0\ne a\in A\). The descending chain
\[
(a)\supseteq(a^2)\supseteq(a^3)\supseteq\cdots
\]
stabilizes, so for some \(n\ge1\),
\[
(a^n)=(a^{n+1}).
\]
Hence \(a^n\in(a^{n+1})\), so there exists \(b\in A\) with
\[
a^n=a^{n+1}b.
\]
Because \(A\) is a domain and \(a^n\ne0\), cancellation gives
\[
1=ab.
\]
Thus every nonzero element of \(A\) is a unit, so \(A\) is a field.
:::

<1>3. Every prime ideal in a commutative Artinian ring is maximal.
::: {.proof}
Let \(\mathfrak p\) be a prime ideal of the commutative Artinian ring \(A\). The quotient \(A/\mathfrak p\) is an integral domain. By <1>1, applied to the quotient map
\[
A\twoheadrightarrow A/\mathfrak p,
\]
the quotient is Artinian. By <1>2 it is therefore a field. Hence \(\mathfrak p\) is maximal.
:::
:::
