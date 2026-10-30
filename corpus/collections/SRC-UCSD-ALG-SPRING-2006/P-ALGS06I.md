---
schema: qual/card@1
id: P-ALGS06I
kind: problem
title: "Degree and Galois group of $\\sin(2\\pi/p)$ over $\\QQ$"
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

::: {.problem}
(a) Let $p$ be an odd prime.
Show that $\sin\!\left(\frac{2\pi}{p}\right)$ is algebraic over $\QQ$ and determine its degree over $\QQ$.

(b) Show that $\QQ\!\left(\sin\!\left(\frac{2\pi}{p}\right)\right)$ is a Galois extension of $\QQ$ and determine its Galois group over $\QQ$.

(c) Find all $p$'s such that $p^{1/3} \in \RR$ is contained in $\QQ\!\left(\sin\!\left(\frac{2\pi}{p}\right)\right)$.
:::

::: {.solution}
Let
$$
\xi=e^{2\pi i/(4p)}.
$$
Then $\xi$ is a primitive $4p$-th root of unity.

::: pf

::: {.pf-step #s1}

The element $\sin(2\pi/p)$ generates the maximal real subfield of $\QQ(\xi)$.

::: pf-proof

Using $\sin\theta=\cos(\pi/2-\theta)$,
$$
\sin\!\left(\frac{2\pi}{p}\right)
=
\cos\!\left(\frac{(p-4)\pi}{2p}\right)
=
\frac{\xi^{p-4}+\xi^{-(p-4)}}2.
$$
Because $p$ is odd,
$$
\gcd(p-4,4p)=1,
$$
so $\eta:=\xi^{p-4}$ is again a primitive $4p$-th root of unity. Hence
$$
\QQ\!\left(\sin\frac{2\pi}{p}\right)
=
\QQ(\eta+\eta^{-1}).
$$
Now $\eta$ satisfies
$$
T^2-(\eta+\eta^{-1})T+1=0,
$$
so $[\QQ(\eta):\QQ(\eta+\eta^{-1})]\le2$. Complex conjugation is a nontrivial automorphism of $\QQ(\eta)$ fixing $\eta+\eta^{-1}$, so this degree is exactly $2$. Thus $\QQ(\eta+\eta^{-1})$ is the maximal real subfield of $\QQ(\eta)=\QQ(\xi)$.

:::

:::

::: pf-step

Therefore
$$
\left[\QQ\!\left(\sin\frac{2\pi}{p}\right):\QQ\right]=p-1.
$$

::: pf-proof

Since $p$ is odd,
$$
[\QQ(\xi):\QQ]=\varphi(4p)=\varphi(4)\varphi(p)=2(p-1).
$$
By step [](#s1){.pf-ref} the desired field has index $2$ in $\QQ(\xi)$, so its degree over $\QQ$ is $p-1$. This also proves algebraicity.

:::

:::

::: {.pf-step #s3}

The extension $\QQ(\sin(2\pi/p))/\QQ$ is Galois, with
$$
\operatorname{Gal}\!\left(\QQ\!\left(\sin\frac{2\pi}{p}\right)/\QQ\right)
\cong
(\ZZ/4p\ZZ)^\times/\{\pm1\}
\cong
(\ZZ/p\ZZ)^\times
\cong C_{p-1}.
$$

::: pf-proof

The cyclotomic extension $\QQ(\xi)/\QQ$ is Galois with abelian group
$$
(\ZZ/4p\ZZ)^\times.
$$
Its maximal real subfield is the fixed field of complex conjugation, corresponding to the subgroup $\{\pm1\}$. Since the ambient Galois group is abelian, this subgroup is normal, so the fixed field is Galois over $\QQ$, with quotient Galois group
$$
(\ZZ/4p\ZZ)^\times/\{\pm1\}.
$$
By the Chinese remainder theorem,
$$
(\ZZ/4p\ZZ)^\times
\cong
(\ZZ/4\ZZ)^\times\times(\ZZ/p\ZZ)^\times.
$$
Each coset modulo $\{\pm1\}$ has a unique representative congruent to $1\pmod4$, so restriction to the second factor identifies the quotient with $(\ZZ/p\ZZ)^\times$. The latter is cyclic of order $p-1$.

:::

:::

::: pf-step

There is no odd prime $p$ such that $p^{1/3}\in\QQ(\sin(2\pi/p))$.

::: pf-proof

Set
$$
K=\QQ\!\left(\sin\frac{2\pi}{p}\right).
$$
By step [](#s3){.pf-ref}, $K/\QQ$ is cyclic Galois. Hence every intermediate field of $K/\QQ$ is Galois over $\QQ$, because every subgroup of a cyclic group is normal.

Suppose $p^{1/3}\in K$. Then $\QQ(p^{1/3})$ is an intermediate field. The polynomial
$$
T^3-p
$$
is irreducible over $\QQ$ by Eisenstein's criterion at $p$, so $[\QQ(p^{1/3}):\QQ]=3$. But $\QQ(p^{1/3})\subset\RR$, while the other two roots $\omega p^{1/3}$ and $\omega^2p^{1/3}$ are nonreal. Therefore $\QQ(p^{1/3})/\QQ$ is not normal, hence not Galois, a contradiction.

Thus no such prime exists.

:::

:::

:::

:::
