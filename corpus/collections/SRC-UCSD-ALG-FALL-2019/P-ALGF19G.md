---
schema: qual/card@1
id: P-ALGF19G
kind: problem
title: Splitting field of $x^5 - 5$; non-abelian Galois; no root in $\QQ[\zeta_{25}]$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 7 of the official UCSD Algebra Qualifying Exam, Fall 2019 source; the splitting-field, non-abelian Galois, and cyclotomic-field assertions agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the degree-20 splitting field, exhibited two noncommuting automorphisms, and ruled out a fifth root of 5 in Q(zeta_25) because every subextension of an abelian Galois extension is abelian Galois.
---

::: {.problem}
For a positive integer $n$, let $\zeta_n = e^{2\pi i/n}$ be a primitive $n$-th root of unity in $\CC$.

(a) Prove that $\QQ[\sqrt[5]{5}, \zeta_5]$ is a splitting field of $x^5 - 5$ over $\QQ$.

(b) Prove that $\QQ[\sqrt[5]{5}, \zeta_5]/\QQ$ is a non-abelian Galois extension; that means it is a Galois extension and $\mathrm{Gal}(\QQ[\sqrt[5]{5}, \zeta_5]/\QQ)$ is not abelian.

(c) Prove that $x^5 - 5$ does not have a zero in $\QQ[\zeta_{25}]$.
:::

::: {.solution}
Let
\[
\alpha=\sqrt[5]{5},
\qquad
\zeta=\zeta_5,
\qquad
K=\QQ(\alpha,\zeta).
\]

::: pf

::: {.pf-step #s1}

The field $K$ is the splitting field of $x^5-5$ over $\QQ$.

::: pf-proof

The five roots of $x^5-5$ in $\CC$ are
\[
\alpha,
\zeta\alpha,
\zeta^2\alpha,
\zeta^3\alpha,
\zeta^4\alpha.
\]
All of them lie in $K$, so $x^5-5$ splits over $K$. Conversely, a field containing all five roots contains both $\alpha$ and
\[
\frac{\zeta\alpha}{\alpha}=\zeta.
\]
Thus it contains $K$. Hence $K$ is precisely the splitting field. This proves part (a).

:::

:::

::: {.pf-step #s2}

The degree of $K$ over $\QQ$ is $20$.

::: pf-proof

The polynomial
\[
x^5-5
\]
is Eisenstein at $5$, so
\[
[\QQ(\alpha):\QQ]=5.
\]
Also $\zeta$ has cyclotomic polynomial
\[
\Phi_5(x)=x^4+x^3+x^2+x+1.
\]
Its translate
\[
\Phi_5(x+1)=x^4+5x^3+10x^2+10x+5
\]
is Eisenstein at $5$, so $\Phi_5$ is irreducible and
\[
[\QQ(\zeta):\QQ]=4.
\]

The intersection
\[
E:=\QQ(\alpha)\cap\QQ(\zeta)
\]
has degree over $\QQ$ dividing both $5$ and $4$, hence
\[
E=\QQ.
\]
The extension $\QQ(\zeta)/\QQ$ is Galois, so the standard compositum degree formula gives
\[
[K:\QQ]
=
[\QQ(\alpha):\QQ]
[\QQ(\zeta):\QQ]
=20.
\]
Consequently
\[
[K:\QQ(\zeta)]=5,
\qquad
[K:\QQ(\alpha)]=4.
\]

:::

:::

::: {.pf-step #s3}

There is an automorphism $\sigma\in\operatorname{Gal}(K/\QQ)$ such that
\[
\sigma(\alpha)=\zeta\alpha,
\qquad
\sigma(\zeta)=\zeta.
\]

::: pf-proof

By step [](#s2){.pf-ref}, the minimal polynomial of $\alpha$ over $\QQ(\zeta)$ has degree $5$. Since it divides $x^5-5$, it equals $x^5-5$.
The element $\zeta\alpha$ is another root of this polynomial in $K$. Hence the $\QQ(\zeta)$-embedding sending
\[
\alpha\longmapsto\zeta\alpha
\]
is an automorphism of $K$. It fixes $\zeta$ by construction.

:::

:::

::: {.pf-step #s4}

There is an automorphism $\tau\in\operatorname{Gal}(K/\QQ)$ such that
\[
\tau(\alpha)=\alpha,
\qquad
\tau(\zeta)=\zeta^2.
\]

::: pf-proof

By step [](#s2){.pf-ref},
\[
[K:\QQ(\alpha)]=4.
\]
Therefore the minimal polynomial of $\zeta$ over $\QQ(\alpha)$ has degree $4$. It divides $\Phi_5$, so it is $\Phi_5$ itself.
Since $\zeta^2$ is another root of $\Phi_5$ in $K$, the $\QQ(\alpha)$-embedding
\[
\zeta\longmapsto\zeta^2
\]
is an automorphism of $K$. It fixes $\alpha$.

:::

:::

::: {.pf-step #s5}

The Galois group $\operatorname{Gal}(K/\QQ)$ is non-abelian.

::: pf-proof

By step [](#s1){.pf-ref}, $K$ is a splitting field over the characteristic-zero field $\QQ$, so $K/\QQ$ is Galois.

Using steps [](#s3){.pf-ref} and [](#s4){.pf-ref},
\[
(\tau\sigma)(\alpha)
=
\tau(\zeta\alpha)
=
\zeta^2\alpha,
\]
whereas
\[
(\sigma\tau)(\alpha)
=
\sigma(\alpha)
=
\zeta\alpha.
\]
Since $\zeta^2\ne\zeta$, the automorphisms $\sigma$ and $\tau$ do not commute. Thus $\operatorname{Gal}(K/\QQ)$ is non-abelian. This proves part (b).

:::

:::

::: {.pf-step #s6}

If $x^5-5$ had a zero in $\QQ(\zeta_{25})$, then $K$ would be a subfield of $\QQ(\zeta_{25})$.

::: pf-proof

Set
\[
L=\QQ(\zeta_{25}).
\]
Suppose $\beta\in L$ satisfies
\[
\beta^5=5.
\]
Every complex root of $x^5-5$ is $\zeta^j\alpha$ for some $j\in\{0,1,2,3,4\}$. Thus
\[
\beta=\zeta^j\alpha
\]
for some $j$.

Since
\[
\zeta=\zeta_{25}^5\in L,
\]
we obtain
\[
\alpha=\zeta^{-j}\beta\in L.
\]
Therefore both $\alpha$ and $\zeta$ lie in $L$, so
\[
K=\QQ(\alpha,\zeta)\subseteq L.
\]

:::

:::

::: pf-step

The polynomial $x^5-5$ has no zero in $\QQ(\zeta_{25})$.

::: pf-proof

The cyclotomic extension
\[
L=\QQ(\zeta_{25})/\QQ
\]
is Galois with abelian Galois group
\[
\operatorname{Gal}(L/\QQ)\cong(\ZZ/25\ZZ)^\times.
\]
Every subgroup of an abelian group is normal. Hence every intermediate field of $L/\QQ$ is Galois over $\QQ$, with Galois group a quotient of the abelian group $\operatorname{Gal}(L/\QQ)$; in particular that Galois group is abelian.

If $x^5-5$ had a zero in $L$, then step [](#s6){.pf-ref} would give $K\subseteq L$. This would force $K/\QQ$ to have abelian Galois group, contradicting step [](#s5){.pf-ref}. Therefore $x^5-5$ has no zero in $\QQ(\zeta_{25})$. This proves part (c).

:::

:::

:::

:::
