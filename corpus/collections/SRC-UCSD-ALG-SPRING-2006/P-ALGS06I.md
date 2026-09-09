---
schema: qual/card@1
id: P-ALGS06I
kind: problem
title: "Algebraic degree and Galois group of sin(2π/p) over Q"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
  note: Checked against Question 4.2 of the official UCSD Algebra Qualifying Examination, Spring 2006; all three parts agree with the source.
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
  note: The proof identifies the field as the maximal real subfield of the 4p-th cyclotomic field and uses cyclic Galois correspondence to exclude cube roots of p.
---

::: problem
(a) Let $p$ be an odd prime.
Show that $\sin\!\left(\frac{2\pi}{p}\right)$ is algebraic over $\mathbb{Q}$ and determine its degree over $\mathbb{Q}$.

(b) Show that $\mathbb{Q}\!\left(\sin\!\left(\frac{2\pi}{p}\right)\right)$ is a Galois extension of $\mathbb{Q}$ and determine its Galois group over $\mathbb{Q}$.

(c) Find all $p$'s such that $p^{1/3} \in \mathbb{R}$ is contained in $\mathbb{Q}\!\left(\sin\!\left(\frac{2\pi}{p}\right)\right)$.
:::

::: {.solution}
Let
\[
\xi=e^{2\pi i/(4p)}.
\]
Then \(\xi\) is a primitive \(4p\)-th root of unity.

<1>1. The element \(\sin(2\pi/p)\) generates the maximal real subfield of \(\mathbb Q(\xi)\).
::: {.proof}
Using \(\sin\theta=\cos(\pi/2-\theta)\),
\[
\sin\!\left(\frac{2\pi}{p}\right)
=
\cos\!\left(\frac{(p-4)\pi}{2p}\right)
=
\frac{\xi^{p-4}+\xi^{-(p-4)}}2.
\]
Because \(p\) is odd,
\[
\gcd(p-4,4p)=1,
\]
so \(\eta:=\xi^{p-4}\) is again a primitive \(4p\)-th root of unity. Hence
\[
\mathbb Q\!\left(\sin\frac{2\pi}{p}\right)
=
\mathbb Q(\eta+\eta^{-1}).
\]
Now \(\eta\) satisfies
\[
T^2-(\eta+\eta^{-1})T+1=0,
\]
so \([\mathbb Q(\eta):\mathbb Q(\eta+\eta^{-1})]\le2\). Complex conjugation is a nontrivial automorphism of \(\mathbb Q(\eta)\) fixing \(\eta+\eta^{-1}\), so this degree is exactly \(2\). Thus \(\mathbb Q(\eta+\eta^{-1})\) is the maximal real subfield of \(\mathbb Q(\eta)=\mathbb Q(\xi)\).
:::

<1>2. Therefore
\[
\left[\mathbb Q\!\left(\sin\frac{2\pi}{p}\right):\mathbb Q\right]=p-1.
\]
::: {.proof}
Since \(p\) is odd,
\[
[\mathbb Q(\xi):\mathbb Q]=\varphi(4p)=\varphi(4)\varphi(p)=2(p-1).
\]
By <1>1 the desired field has index \(2\) in \(\mathbb Q(\xi)\), so its degree over \(\mathbb Q\) is \(p-1\). This also proves algebraicity.
:::

<1>3. The extension \(\mathbb Q(\sin(2\pi/p))/\mathbb Q\) is Galois, with
\[
\operatorname{Gal}\!\left(\mathbb Q\!\left(\sin\frac{2\pi}{p}\right)/\mathbb Q\right)
\cong
(\mathbb Z/4p\mathbb Z)^\times/\{\pm1\}
\cong
(\mathbb Z/p\mathbb Z)^\times
\cong C_{p-1}.
\]
::: {.proof}
The cyclotomic extension \(\mathbb Q(\xi)/\mathbb Q\) is Galois with abelian group
\[
(\mathbb Z/4p\mathbb Z)^\times.
\]
Its maximal real subfield is the fixed field of complex conjugation, corresponding to the subgroup \(\{\pm1\}\). Since the ambient Galois group is abelian, this subgroup is normal, so the fixed field is Galois over \(\mathbb Q\), with quotient Galois group
\[
(\mathbb Z/4p\mathbb Z)^\times/\{\pm1\}.
\]
By the Chinese remainder theorem,
\[
(\mathbb Z/4p\mathbb Z)^\times
\cong
(\mathbb Z/4\mathbb Z)^\times\times(\mathbb Z/p\mathbb Z)^\times.
\]
Each coset modulo \(\{\pm1\}\) has a unique representative congruent to \(1\pmod4\), so restriction to the second factor identifies the quotient with \((\mathbb Z/p\mathbb Z)^\times\). The latter is cyclic of order \(p-1\).
:::

<1>4. There is no odd prime \(p\) such that \(p^{1/3}\in\mathbb Q(\sin(2\pi/p))\).
::: {.proof}
Set
\[
K=\mathbb Q\!\left(\sin\frac{2\pi}{p}\right).
\]
By <1>3, \(K/\mathbb Q\) is cyclic Galois. Hence every intermediate field of \(K/\mathbb Q\) is Galois over \(\mathbb Q\), because every subgroup of a cyclic group is normal.

Suppose \(p^{1/3}\in K\). Then \(\mathbb Q(p^{1/3})\) is an intermediate field. The polynomial
\[
T^3-p
\]
is irreducible over \(\mathbb Q\) by Eisenstein's criterion at \(p\), so \([\mathbb Q(p^{1/3}):\mathbb Q]=3\). But \(\mathbb Q(p^{1/3})\subset\mathbb R\), while the other two roots \(\omega p^{1/3}\) and \(\omega^2p^{1/3}\) are nonreal. Therefore \(\mathbb Q(p^{1/3})/\mathbb Q\) is not normal, hence not Galois, a contradiction.

Thus no such prime exists.
:::
:::
