---
schema: qual/card@1
id: P-MMAQ-MLE74H7M42
kind: problem
title: Classification of finite fields
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Classify (with proof) all fields with finitely many elements.
:::


::: solution
Let \(F\) be a finite field. Its characteristic is a prime \(p\), so its prime subfield is \(\mathbb F_p\). Since \(F\) is finite-dimensional over \(\mathbb F_p\), say
\[
[F:\mathbb F_p]=n,
\]
we have
\[
|F|=p^n.
\]
Thus every finite field has prime-power order.

Conversely, fix a prime \(p\) and \(n\ge1\), and work in an algebraic closure \(\overline{\mathbb F_p}\). Let
\[
E=\{a\in\overline{\mathbb F_p}:a^{p^n}=a\}.
\]
If \(a,b\in E\), then in characteristic \(p\),
\[
(a+b)^{p^n}=a^{p^n}+b^{p^n}=a+b,
\]
and similarly \((ab)^{p^n}=ab\). Also, if \(a\ne0\), then \(a^{p^n-1}=1\), so
\[
(a^{-1})^{p^n}=a^{-1}.
\]
Hence \(E\) is a field. It is exactly the set of roots of
\[
X^{p^n}-X.
\]
The derivative of this polynomial is \(-1\), so all roots are simple. Therefore it has exactly \(p^n\) roots in the algebraic closure, and
\[
|E|=p^n.
\]
Thus a field of order \(p^n\) exists for every prime power.

Finally, let \(F\) be any field with \(p^n\) elements. Its multiplicative group \(F^\times\) has order \(p^n-1\), so for every nonzero \(a\in F\),
\[
a^{p^n-1}=1,
\]
and hence \(a^{p^n}=a\); this is also true for \(a=0\). Thus every element of \(F\) is a root of \(X^{p^n}-X\). Since this polynomial has exactly \(p^n\) roots in an algebraic closure, \(F\) is identified with the full root field \(E\) above.

Therefore, up to isomorphism, there is exactly one finite field of order \(p^n\) for each prime power \(p^n\), and there are no finite fields of any other order.
:::
