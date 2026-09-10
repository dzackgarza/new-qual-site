---
schema: qual/card@1
id: P-F12IN
kind: problem
title: $A \subseteq f^{-1}(f(A))$, with equality iff $f$ is injective
classification:
  areas:
  - prelim
  topics:
  - Functions and Relations
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $f: X \to Y$ be a (not necessarily invertible) function, and $A \subseteq X$.

(a) Prove that $A \subseteq f^{-1}(f(A))$.

(b) Prove that if $f$ is injective (one-to-one) then $A = f^{-1}(f(A))$.

(c) Give an example for which $A \neq f^{-1}(f(A))$.
:::

::: solution
(a) If $x\in A$, then $f(x)\in f(A)$, so by definition $x\in f^{-1}(f(A))$. Thus
\[
A\subseteq f^{-1}(f(A)).
\]

(b) Suppose $f$ is injective and $x\in f^{-1}(f(A))$. Then $f(x)\in f(A)$, so there exists $a\in A$ with $f(x)=f(a)$. Injectivity gives $x=a\in A$. Thus the reverse inclusion holds and
\[
A=f^{-1}(f(A)).
\]

(c) Let $X=\{0,1\}$, $Y=\{0\}$, let $f$ be constant, and take $A=\{0\}$. Then
\[
f^{-1}(f(A))=X\ne A.
\]
:::
