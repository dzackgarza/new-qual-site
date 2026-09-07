---
schema: qual/card@1
id: P-ALGF19C
kind: problem
title: Units of $A[x]$ via units and nilradical of $A$
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 3 of the official UCSD Algebra Qualifying Exam, Fall 2019 source; the unit characterization and hint agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified necessity by reduction modulo every prime ideal and sufficiency by showing the positive-degree part is nilpotent and summing a finite geometric inverse.
---

::: problem
Suppose $A$ is a unital commutative ring.
Let $A[x]$ be the ring of polynomials, $A^\times$ be the group of units of $A$, and $\mathrm{Nil}(A)$ be the nilradical of $A$.
Prove that
\[
A[x]^\times = \{ a_0 + a_1 x + \cdots + a_n x^n \mid a_0 \in A^\times,\; a_1,\ldots,a_n \in \mathrm{Nil}(A),\; n \in \mathbb{Z}^+ \},
\]
where $A[x]^\times$ is the group of units of $A[x]$.
(Hint.
Without proof you can use that $\sum_i a_i x^i \mapsto \sum_i (a_i + \mathfrak{a}) x^i$ is a ring homomorphism from $A[x]$ to $(A/\mathfrak{a})[x]$ for any $\mathfrak{a} \trianglelefteq A$.
Show that if $u$ is a unit and $n$ is nilpotent, then $u + n = u(1 + u^{-1}n)$ is a unit.)
:::

::: {.solution}
Write
\[
f(x)=a_0+a_1x+\cdots+a_nx^n\in A[x].
\]

<1>1. If $f(x)$ is a unit, then $a_0\in A^\times$.
::: {.proof}
Suppose
\[
f(x)g(x)=1
\]
for some $g(x)\in A[x]$. Evaluating at $x=0$ gives
\[
a_0g(0)=1.
\]
Hence $a_0$ is a unit of $A$.
:::

<1>2. If $f(x)$ is a unit, then every $a_i$ with $i\ge1$ lies in every prime ideal of $A$.
::: {.proof}
Let $\mathfrak p$ be a prime ideal of $A$. Reduction modulo $\mathfrak p$ sends $f$ to a unit
\[
\overline f(x)
=
\overline a_0+\overline a_1x+\cdots+\overline a_nx^n
\]
of $(A/\mathfrak p)[x]$.

The ring $A/\mathfrak p$ is an integral domain. If two nonzero polynomials over an integral domain are multiplied, their degrees add. Therefore the only units of $(A/\mathfrak p)[x]$ are the nonzero constant polynomials. Thus
\[
\overline a_i=0
\qquad(i\ge1),
\]
so
\[
a_i\in\mathfrak p
\qquad(i\ge1).
\]
Since $\mathfrak p$ was arbitrary, each $a_i$ with $i\ge1$ lies in every prime ideal of $A$.
:::

<1>3. An element of $A$ that lies in every prime ideal is nilpotent.
::: {.proof}
It is enough to prove the contrapositive. Let $r\in A$ be non-nilpotent and set
\[
S=\{1,r,r^2,\ldots\}.
\]
Then $0\notin S$, so $S^{-1}A$ is a nonzero ring. Choose a maximal ideal $\mathfrak m$ of $S^{-1}A$, and let $\mathfrak p$ be its inverse image in $A$. Then $\mathfrak p$ is prime and is disjoint from $S$. In particular
\[
r\notin\mathfrak p.
\]
Thus a non-nilpotent element cannot lie in every prime ideal.
:::

<1>4. If $f(x)$ is a unit, then
\[
a_0\in A^\times,
\qquad
a_1,\ldots,a_n\in\operatorname{Nil}(A).
\]
::: {.proof}
The assertion about $a_0$ is <1>1. By <1>2, each positive-degree coefficient lies in every prime ideal, and by <1>3 each such coefficient is nilpotent.
:::

<1>5. If $a_1,\ldots,a_n$ are nilpotent, then
\[
h(x):=a_1x+\cdots+a_nx^n
\]
is nilpotent in $A[x]$.
::: {.proof}
For each $i\ge1$, choose $e_i\ge1$ with
\[
a_i^{e_i}=0.
\]
Set
\[
N=1+\sum_{i=1}^n(e_i-1).
\]
Every coefficient occurring in $h(x)^N$ is a sum of products of $N$ elements chosen from $a_1,\ldots,a_n$. In every such product, some $a_i$ occurs at least $e_i$ times; otherwise the total number of factors would be at most
\[
\sum_{i=1}^n(e_i-1)=N-1.
\]
That product is therefore zero. Hence
\[
h(x)^N=0.
\]
:::

<1>6. If $a_0\in A^\times$ and $a_1,\ldots,a_n\in\operatorname{Nil}(A)$, then $f(x)$ is a unit.
::: {.proof}
By <1>5, $h=f-a_0$ is nilpotent. Therefore
\[
u:=a_0^{-1}h
\]
is nilpotent as well; say $u^N=0$. Since
\[
f=a_0(1+u),
\]
and
\[
(1+u)(1-u+u^2-\cdots+(-u)^{N-1})=1,
\]
both factors on the right are units. Hence $f$ is a unit of $A[x]$.
:::

<1>7. The stated description of $A[x]^\times$ follows.
::: {.proof}
Necessity is <1>4 and sufficiency is <1>6. Thus a polynomial is a unit exactly when its constant coefficient is a unit and every positive-degree coefficient is nilpotent.
:::
:::
