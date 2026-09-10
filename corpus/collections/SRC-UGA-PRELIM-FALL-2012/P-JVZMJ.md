---
schema: qual/card@1
id: P-JVZMJ
kind: problem
title: Smooth negations of a quantified inequality, the extreme value theorem, and
  a biconditional
classification:
  areas:
  - prelim
  topics:
  - Logic and Quantifiers
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Write the negations of these sentences in as "smooth" a way as possible.
(In particular, you may not simply append "It is not the case that ...". Also, you should make explicit any "hidden" quantifiers.)

a. There is a real number $x$ such that for every real number $y$, $|x-y|>1$.
b. A real-valued function that is continuous on a closed interval attains a minimum value on that interval.
c. $3n+1$ is even if and only if $n^2+4$ is prime.
:::

::: solution
(a) The negation is:
\[
\text{For every real }x\text{ there exists a real }y\text{ such that }|x-y|\le1.
\]

(b) Making the hidden quantifiers explicit, the original assertion says that for every closed interval $[a,b]$ and every continuous $f:[a,b]\to\mathbb R$, there exists $x\in[a,b]$ such that $f(x)\le f(y)$ for every $y\in[a,b]$. Its negation is therefore:
\[
\text{There exist }a\le b\text{ and continuous }f:[a,b]\to\mathbb R\text{ such that for every }x\in[a,b]
\]
\[
\text{there exists }y\in[a,b]\text{ with }f(y)<f(x).
\]

(c) Interpreting $n$ as an arbitrary integer, the negation of the biconditional is that there exists an integer $n$ for which exactly one side holds; equivalently,
\[
\text{either }3n+1\text{ is even and }n^2+4\text{ is composite,}
\]
or
\[
3n+1\text{ is odd and }n^2+4\text{ is prime.}
\]
:::
