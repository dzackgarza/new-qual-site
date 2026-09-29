---
schema: qual/card@1
id: P-HCAO18
kind: problem
title: Factorization and prime elements in rings of holomorphic functions
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Holomorphic Functions
  - Prime Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $\Omega \subseteq \mathbb C$ be a domain.
Let $\mathcal O(\Omega)$ be the ring of holomorphic functions on $\Omega$, and let $\mathcal O_F(\Omega)$ be its subring of functions with finitely many zeros.

Is either ring a unique factorization domain?
What are the prime elements in these rings?
:::

::: {.solution}
Interpret $\mathcal O_F(\Omega)$ as the subring consisting of $0$ together with
the nonzero holomorphic functions having only finitely many zeros.

The ring $\mathcal O(\Omega)$ is not a UFD, while $\mathcal O_F(\Omega)$ is a
UFD. In both rings, the prime elements are exactly the associates of the
functions
\[
z\longmapsto z-a,
\qquad a\in\Omega.
\]

::: pf

::: {.pf-step #units-are-zero-free}
The units in either ring are exactly the zero-free holomorphic functions.

::: pf-proof
If $u$ has no zeros, then $1/u$ is holomorphic on $\Omega$ and is also zero-free,
so $u$ is a unit in both rings. Conversely, if $uv=1$, then $u$ cannot vanish.
:::

:::

::: {.pf-step #z-minus-a-is-prime}
For every $a\in\Omega$, the function $z-a$ is prime in both rings.

::: pf-proof
Suppose
\[
(z-a)\mid fg.
\]
Then $(fg)(a)=0$, so $f(a)=0$ or $g(a)=0$. If $f(a)=0$, holomorphic division
at a zero gives
\[
f(z)=(z-a)h(z)
\]
with $h$ holomorphic on $\Omega$, hence $(z-a)\mid f$; similarly if $g(a)=0$.

If $f\in\mathcal O_F(\Omega)$, then $h$ has one fewer zero counted with
multiplicity and still lies in $\mathcal O_F(\Omega)$, so the same divisibility
argument works in that subring.
:::

:::

::: {.pf-step #irreducibles-are-z-minus-a}
Every irreducible element in either ring is associate to $z-a$ for some
$a\in\Omega$.

::: pf-proof
Let $f$ be a nonzero nonunit. By step [](#units-are-zero-free){.pf-ref} it has a zero $a\in\Omega$, so
\[
f=(z-a)h
\]
for some holomorphic $h$.

If $f$ is irreducible, then one of the two factors is a unit. The factor
$z-a$ is not a unit, hence $h$ must be a unit. Thus $f$ is associate to
$z-a$. By step [](#z-minus-a-is-prime){.pf-ref} these irreducibles are prime.
:::

:::

::: {.pf-step #ofdomain-factors-into-primes}
Every nonzero nonunit in $\mathcal O_F(\Omega)$ factors into prime
elements.

::: pf-proof
Let the zeros of $f$ be
\[
a_1,\ldots,a_r
\]
with multiplicities $m_1,\ldots,m_r$. Repeated holomorphic division gives
\[
f(z)=u(z)\prod_{i=1}^r(z-a_i)^{m_i},
\]
where $u$ has no zeros. By step [](#units-are-zero-free){.pf-ref}, $u$ is a unit, and by step [](#z-minus-a-is-prime){.pf-ref} each $z-a_i$ is
prime.
:::

:::

::: {.pf-step #ofdomain-factorization-unique}
Factorization in $\mathcal O_F(\Omega)$ is unique up to order and units.

::: pf-proof
The multiplicity of a zero of a product is the sum of the multiplicities of
that zero in the factors. Hence any factorization of $f$ into the primes from
step [](#z-minus-a-is-prime){.pf-ref} must contain exactly $m_i$ factors associate to $z-a_i$ for each $i$.
The remaining factor is zero-free and therefore a unit by step [](#units-are-zero-free){.pf-ref}.
:::

:::

::: pf-step
Therefore $\mathcal O_F(\Omega)$ is a UFD.

::: pf-proof
Existence is step [](#ofdomain-factors-into-primes){.pf-ref} and uniqueness is step [](#ofdomain-factorization-unique){.pf-ref}.
:::

:::

::: {.pf-step #function-with-infinite-zeros}
There exists a nonzero function in $\mathcal O(\Omega)$ with infinitely
many zeros.

::: pf-proof
Choose an infinite discrete subset $A\subset\Omega$. The Weierstrass theorem
for general plane domains gives a holomorphic function on $\Omega$ whose zero
set is exactly $A$, with prescribed positive multiplicities. In particular,
there is a nonzero holomorphic function with infinitely many zeros.
:::

:::

::: pf-step
The ring $\mathcal O(\Omega)$ is not a UFD.

::: pf-proof
Let $f$ be the function from step [](#function-with-infinite-zeros){.pf-ref}. If $f$ were a finite product of irreducibles,
then by step [](#irreducibles-are-z-minus-a){.pf-ref} each irreducible factor would be associate to some $z-a$ and hence
would contribute only one zero. A finite product of such factors has only
finitely many zeros, contradicting the construction of $f$.
:::

:::

:::
:::
