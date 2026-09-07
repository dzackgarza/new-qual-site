---
schema: qual/card@1
id: P-ALGF10D
kind: problem
title: "Every finite separable extension is simple"
classification:
  areas:
  - algebra
  topics:
  - Field Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 4 of the official UCSD Algebra Qualifying Examination, Fall 2010; the statement and Galois-theory hint agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the primitive-element argument via the finite Galois correspondence when the base field is infinite, with the finite-field case handled by cyclicity of the multiplicative group.
---

::: {.problem}
Let $E$ be a finite separable extension of $F$.
Show that $E = F(a)$ for some $a$ in $E$.

Hint: Use the Fundamental Theorem of Galois Theory.
:::


::: {.solution}
We prove the finite and infinite base-field cases separately.

<1>1. If \(F\) is finite, then \(E/F\) is simple.
::: {.proof}
Because \([E:F]<\infty\), the field \(E\) is finite.
The multiplicative group \(E^\times\) of a finite field is cyclic.
Choose a generator \(a\in E^\times\).
Then \(F(a)\) contains every power of \(a\), hence every nonzero element of \(E\), and of course it contains \(0\).
Therefore
\[
F(a)=E.
\]
:::

<1>2. Suppose \(F\) is infinite. Then there are only finitely many intermediate fields between \(F\) and \(E\).
::: {.proof}
Let \(N\) be the normal closure of \(E/F\).
Since \(E/F\) is finite and separable, \(N/F\) is a finite Galois extension.
Set
\[
G:=\operatorname{Gal}(N/F),
\qquad
H:=\operatorname{Gal}(N/E).
\]
By the fundamental theorem of Galois theory, intermediate fields
\[
F\subseteq K\subseteq E
\]
correspond to subgroups \(J\) of the finite group \(G\) satisfying
\[
H\subseteq J\subseteq G.
\]
A finite group has only finitely many subgroups.
Hence \(E/F\) has only finitely many intermediate fields.
:::

<1>3. A finite-dimensional vector space over an infinite field is not the union of finitely many proper linear subspaces.
::: {.proof}
Let \(V\) be finite-dimensional over an infinite field \(F\), and suppose
\[
V=V_1\cup\cdots\cup V_r
\]
with each \(V_i\) proper.
For each \(i\), choose a nonzero linear functional
\[
\ell_i:V\to F
\]
that vanishes on \(V_i\).
Then the polynomial function
\[
P(v):=\prod_{i=1}^r \ell_i(v)
\]
vanishes on all of \(V\).
But \(P\) is a nonzero polynomial: the symmetric algebra of the dual space is an integral domain, and each \(\ell_i\neq0\).
A nonzero polynomial over an infinite field cannot vanish at every point of \(F^d\), after choosing a basis \(V\cong F^d\).
This contradiction proves the claim.
:::

<1>4. If \(F\) is infinite, then \(E=F(a)\) for some \(a\in E\).
::: {.proof}
By <1>2, list the proper intermediate fields as
\[
K_1,\ldots,K_r.
\]
Each \(K_i\) is a proper \(F\)-linear subspace of the finite-dimensional \(F\)-vector space \(E\).
By <1>3,
\[
E\neq K_1\cup\cdots\cup K_r.
\]
Choose
\[
a\in E\setminus\bigcup_{i=1}^r K_i.
\]
Then \(F(a)\) is an intermediate field.
If \(F(a)\neq E\), it would equal one of the proper intermediate fields \(K_i\), forcing \(a\in K_i\), a contradiction.
Thus
\[
E=F(a).
\]
:::

<1>5. Therefore every finite separable extension is simple.
::: {.proof}
The finite-field case is <1>1 and the infinite-field case is <1>4.
:::
:::
