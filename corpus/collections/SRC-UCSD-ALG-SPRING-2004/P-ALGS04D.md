---
schema: qual/card@1
id: P-ALGS04D
kind: problem
title: "Unique polynomial interpolation via the Chinese Remainder Theorem"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $n_i$, $0 \leq i \leq m$ be integers.
Use the Chinese Remainder Theorem to prove there exists a unique polynomial $f(X) \in \mathbb{Q}[X]$ of degree $\leq m$ with $f(i) = n_i$ for $0 \leq i \leq m$.
:::

::: {.solution}
<1>1. For distinct \(i,j\in\{0,\dots,m\}\), the ideals \((X-i)\) and \((X-j)\) of \(\mathbf Q[X]\) are comaximal.
::: {.proof}
Because \(i-j\in\mathbf Q^\times\),
\[
1=\frac{1}{j-i}(X-i)-\frac{1}{j-i}(X-j).
\]
Thus
\[
(X-i)+(X-j)=\mathbf Q[X].
\]
:::

<1>2. By the Chinese Remainder Theorem,
\[
\mathbf Q[X]\Big/\Big(\prod_{i=0}^m(X-i)\Big)
\cong
\prod_{i=0}^m \mathbf Q[X]/(X-i)
\cong
\mathbf Q^{m+1}.
\]
::: {.proof}
The ideals \((X-i)\) are pairwise comaximal by <1>1, so their intersection equals their product and the CRT applies.
Evaluation at \(i\) identifies
\[
\mathbf Q[X]/(X-i)\cong\mathbf Q.
\]
:::

<1>3. There exists a polynomial \(F(X)\in\mathbf Q[X]\) such that
\[
F(i)=n_i
\qquad(0\le i\le m).
\]
::: {.proof}
Under the isomorphism in <1>2, the tuple
\[
(n_0,\dots,n_m)\in\mathbf Q^{m+1}
\]
has a preimage in the quotient.
Choose any polynomial representative \(F\) of that residue class.
Its image in the \(i\)-th factor is \(n_i\), which means \(F(i)=n_i\).
:::

<1>4. There is a representative \(f(X)\) of the same residue class with \(\deg f\le m\).
::: {.proof}
Let
\[
P(X)=\prod_{i=0}^m(X-i).
\]
Then \(\deg P=m+1\). Divide \(F\) by \(P\):
\[
F=QP+f,
\qquad
\deg f<m+1.
\]
Thus \(\deg f\le m\). Since \(P(i)=0\) for every \(i\), one has
\[
f(i)=F(i)=n_i.
\]
:::

<1>5. Such a polynomial \(f\) is unique among polynomials of degree at most \(m\).
::: {.proof}
Suppose \(f,g\in\mathbf Q[X]\) both have degree at most \(m\) and satisfy
\[
f(i)=g(i)=n_i
\qquad(0\le i\le m).
\]
Then \(f-g\) vanishes at the \(m+1\) distinct points \(0,1,\dots,m\), so
\[
P(X)=\prod_{i=0}^m(X-i)
\]
divides \(f-g\). But
\[
\deg(f-g)\le m<\deg P=m+1.
\]
Hence \(f-g=0\), so \(f=g\).
:::
:::
