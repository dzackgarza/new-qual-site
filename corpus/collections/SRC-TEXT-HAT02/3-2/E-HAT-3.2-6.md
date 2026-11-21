---
schema: qual/card@1
id: E-HAT-3.2-6
kind: problem
title: The $d$-th power map on $\CP^n$ in cohomology
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 6; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the reduction: on a coordinate line $\CP^1\subset\CP^n$ the map is $z\mapsto z^d$ of
    degree $d$, so $f^*(x)$ restricts to $dx$ and hence equals $dx$ because
    $H^2(\CP^n)\to H^2(\CP^1)$ is an isomorphism; multiplicativity then gives $f^*(x^k)=d^kx^k$,
    consistent with the degree $d^n$ of $f$ on the top class.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 6 (p.229) with the bracketed hint. Rechecked: the coordinate-line restriction is z -> z^d of degree d (Proposition 2.30 p.136, d simple preimages), H^2(CP^1) = Z with f^* = d by Theorem 3.2 p.195 and the definition of degree on p.134, so f^*x = dx on CP^n by naturality (Proposition 3.10 p.210) since i^* is an isomorphism in degree 2; multiplicativity gives f^*(x^k) = d^k x^k on H^{2k} = Z. The terse proofs ("cohomology of CP^n", the degree assertion, the restriction argument) now carry their citations. Not covered: nothing about the map on integral cohomology beyond the polynomial generator.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 6 of §3.2, printed p. 229, with Proposition 2.30 (printed
    p. 136), Theorem 3.2 (p. 195), Example 3.12 (p. 213) and Proposition 3.10 (p. 210), and
    compared with Guanyu Li's solution, his Exercise 3.2.5, printed p. 55, which computes the same
    map. The answer $f^*(x^k)=d^kx^k$ is right: on a coordinate line the map is $z\mapsto z^d$ of
    degree $d$, so $f^*x=dx$ there, and $i^*\colon H^2(\CP^n)\to H^2(\CP^1)$ being an isomorphism
    carries this to $\CP^n$ by naturality. Rewritten: three of the six steps were proved by naming
    earlier steps ('Step s4 and the ring homomorphism property', 'Step s5', 'Step s1') and the card
    closed with a `pf-qed` naming one label, which STYLE-08 forbids. Four steps now, one per claim,
    each carrying its argument. Not claimed: a certificate.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Issue #184: the page locators in the card's text are removed; Exercise 3.2.6, Example 3.12 and Proposition 3.10 are cited
    by number (or, where Hatcher prints none, by the section that carries them), each read in
    `tmp/sources/hatcher-2002-algebraic-topology.md`. The earlier events keep their text
    (QUAL-11); these citations supersede their page locators. No step changes.

---

::: {.problem}
Use cup products to compute the map $H^*(\CP^n; \ZZ) \to H^*(\CP^n; \ZZ)$ induced by the map $\CP^n \to \CP^n$ that is a quotient of the map $\CC^{n+1} \to \CC^{n+1}$ raising each coordinate to the $d$th power, $(z_0, \ldots, z_n) \mapsto (z_0^d, \ldots, z_n^d)$, for a fixed integer $d > 0$.
[First do the case $n = 1$.]
:::

::: {.solution}
Write $f$ for the map induced by $(z_0,\dots,z_n)\mapsto(z_0^d,\dots,z_n^d)$. The exercise is Exercise 6 of §3.2, and the answer is
$$
f^*(x^k)=d^k x^k\quad\text{on }H^{2k}(\CP^n;\ZZ),
$$
with $x$ the standard generator of $H^2$.

::: pf

::: {.pf-step #s1}

For $n=1$ the map is $[z_0:z_1]\mapsto[z_0^d:z_1^d]$, of degree $d$, so $f^*(x)=dx$ on $H^2(\CP^1;\ZZ)=\ZZ$.

::: pf-proof

Under $\CP^1=\CC\cup\{\infty\}$ the map is $z\mapsto z^d$: a point $y\ne0,\infty$ has the $d$ distinct preimages with $z^d=y$, at each of which the map is locally injective and so has local degree $1$, and Proposition 2.30 (printed p.~136) gives total degree $d$. Since $H^2(\CP^1;\ZZ)\cong\operatorname{Hom}(H_2(\CP^1),\ZZ)$ by Theorem 3.2 (printed p.~195), and $f_*[S^2]=d[S^2]$ is the definition of degree (printed p.~134), $f^*$ is multiplication by $d$ there.

:::

:::

::: {.pf-step #s2}

$H^*(\CP^n;\ZZ)=\ZZ[x]/(x^{n+1})$ with $\gradeddegree{x}=2$, so $H^{2k}=\ZZ$ for $k\le n$ and $0$ otherwise.

::: pf-proof

This is Example 3.12.

:::

:::

::: {.pf-step #s3}

$f^*(x)=dx$ for every $n$.

::: pf-proof

Let $i\colon\CP^1\hookrightarrow\CP^n$ be the inclusion of a coordinate line; $f$ preserves it, and $fi$ is the map of the first step. Naturality of $i^*$ (Proposition 3.10) gives $i^*f^*(x)=(fi)^*(x)=d\,i^*(x)$, and $i^*\colon H^2(\CP^n)\to H^2(\CP^1)$ is an isomorphism of copies of $\ZZ$, so $f^*(x)=dx$.

:::

:::

::: {.pf-step #s4}

$f^*(x^k)=d^k x^k$ on $H^{2k}(\CP^n;\ZZ)$, for $0\le k\le n$.

::: pf-proof

$f^*$ is a ring homomorphism for the cup product, so $f^*(x^k)=(f^*x)^k=(dx)^k=d^kx^k$, and $H^{2k}(\CP^n;\ZZ)=\ZZ\cdot x^k$ by the second step. Since $x^{n+1}=0$, this is also consistent with the top-degree computation $\deg f=d^n$.

:::

:::

:::
:::
