---
schema: qual/card@1
id: P-ALGF19G
kind: problem
title: Splitting field of $x^5 - 5$; non-abelian Galois; no root in $\mathbb{Q}[\zeta_{25}]$
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

::: problem
For a positive integer $n$, let $\zeta_n = e^{2\pi i/n}$ be a primitive $n$-th root of unity in $\mathbb{C}$.

(a) Prove that $\mathbb{Q}[\sqrt[5]{5}, \zeta_5]$ is a splitting field of $x^5 - 5$ over $\mathbb{Q}$.

(b) Prove that $\mathbb{Q}[\sqrt[5]{5}, \zeta_5]/\mathbb{Q}$ is a non-abelian Galois extension; that means it is a Galois extension and $\mathrm{Gal}(\mathbb{Q}[\sqrt[5]{5}, \zeta_5]/\mathbb{Q})$ is not abelian.

(c) Prove that $x^5 - 5$ does not have a zero in $\mathbb{Q}[\zeta_{25}]$.
:::

::: {.solution}
Let
\[
\alpha=\sqrt[5]{5},
\qquad
\zeta=\zeta_5,
\qquad
K=\mathbb Q(\alpha,\zeta).
\]

<1>1. The field $K$ is the splitting field of $x^5-5$ over $\mathbb Q$.
::: {.proof}
The five roots of $x^5-5$ in $\mathbb C$ are
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

<1>2. The degree of $K$ over $\mathbb Q$ is $20$.
::: {.proof}
The polynomial
\[
x^5-5
\]
is Eisenstein at $5$, so
\[
[\mathbb Q(\alpha):\mathbb Q]=5.
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
[\mathbb Q(\zeta):\mathbb Q]=4.
\]

The intersection
\[
E:=\mathbb Q(\alpha)\cap\mathbb Q(\zeta)
\]
has degree over $\mathbb Q$ dividing both $5$ and $4$, hence
\[
E=\mathbb Q.
\]
The extension $\mathbb Q(\zeta)/\mathbb Q$ is Galois, so the standard compositum degree formula gives
\[
[K:\mathbb Q]
=
[\mathbb Q(\alpha):\mathbb Q]
[\mathbb Q(\zeta):\mathbb Q]
=20.
\]
Consequently
\[
[K:\mathbb Q(\zeta)]=5,
\qquad
[K:\mathbb Q(\alpha)]=4.
\]
:::

<1>3. There is an automorphism $\sigma\in\operatorname{Gal}(K/\mathbb Q)$ such that
\[
\sigma(\alpha)=\zeta\alpha,
\qquad
\sigma(\zeta)=\zeta.
\]
::: {.proof}
By <1>2, the minimal polynomial of $\alpha$ over $\mathbb Q(\zeta)$ has degree $5$. Since it divides $x^5-5$, it equals $x^5-5$.
The element $\zeta\alpha$ is another root of this polynomial in $K$. Hence the $\mathbb Q(\zeta)$-embedding sending
\[
\alpha\longmapsto\zeta\alpha
\]
is an automorphism of $K$. It fixes $\zeta$ by construction.
:::

<1>4. There is an automorphism $\tau\in\operatorname{Gal}(K/\mathbb Q)$ such that
\[
\tau(\alpha)=\alpha,
\qquad
\tau(\zeta)=\zeta^2.
\]
::: {.proof}
By <1>2,
\[
[K:\mathbb Q(\alpha)]=4.
\]
Therefore the minimal polynomial of $\zeta$ over $\mathbb Q(\alpha)$ has degree $4$. It divides $\Phi_5$, so it is $\Phi_5$ itself.
Since $\zeta^2$ is another root of $\Phi_5$ in $K$, the $\mathbb Q(\alpha)$-embedding
\[
\zeta\longmapsto\zeta^2
\]
is an automorphism of $K$. It fixes $\alpha$.
:::

<1>5. The Galois group $\operatorname{Gal}(K/\mathbb Q)$ is non-abelian.
::: {.proof}
By <1>1, $K$ is a splitting field over the characteristic-zero field $\mathbb Q$, so $K/\mathbb Q$ is Galois.

Using <1>3 and <1>4,
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
Since $\zeta^2\ne\zeta$, the automorphisms $\sigma$ and $\tau$ do not commute. Thus $\operatorname{Gal}(K/\mathbb Q)$ is non-abelian. This proves part (b).
:::

<1>6. If $x^5-5$ had a zero in $\mathbb Q(\zeta_{25})$, then $K$ would be a subfield of $\mathbb Q(\zeta_{25})$.
::: {.proof}
Set
\[
L=\mathbb Q(\zeta_{25}).
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
K=\mathbb Q(\alpha,\zeta)\subseteq L.
\]
:::

<1>7. The polynomial $x^5-5$ has no zero in $\mathbb Q(\zeta_{25})$.
::: {.proof}
The cyclotomic extension
\[
L=\mathbb Q(\zeta_{25})/\mathbb Q
\]
is Galois with abelian Galois group
\[
\operatorname{Gal}(L/\mathbb Q)\cong(\mathbb Z/25\mathbb Z)^\times.
\]
Every subgroup of an abelian group is normal. Hence every intermediate field of $L/\mathbb Q$ is Galois over $\mathbb Q$, with Galois group a quotient of the abelian group $\operatorname{Gal}(L/\mathbb Q)$; in particular that Galois group is abelian.

If $x^5-5$ had a zero in $L$, then <1>6 would give $K\subseteq L$. This would force $K/\mathbb Q$ to have abelian Galois group, contradicting <1>5. Therefore $x^5-5$ has no zero in $\mathbb Q(\zeta_{25})$. This proves part (c).
:::
:::
