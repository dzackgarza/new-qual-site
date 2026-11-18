---
schema: qual/card@1
id: E-HAT-3.2-4
kind: problem
title: Fixed points of self-maps of $\CP^n$
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.2, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 4. The printed bracketed pointer "[See Exercise 3 in §2.C for an example of a map without fixed points in this exceptional case.]" was missing and is restored.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the Lefschetz computation: $f^*$ is a ring map, so $f^*(\alpha^j)=d^j\alpha^j$, the odd
    cohomology vanishes, and $L(f)=1+d+\cdots+d^n$. For even $n$ this is $(r^{n+1}+1)/(r+1)>0$ when
    $d=-r<0$ and positive for $d\ge0$; for odd $n$ it factors as $(1-r)(1+r^2+\cdots+r^{n-1})$,
    vanishing exactly at $d=-1$.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 4 (p.229) including the bracketed pointer to Exercise 3 of §2.C. Rechecked the computation: f^*(alpha^j) = d^j alpha^j by Proposition 3.10 p.210 and Example 3.12 p.213, odd cohomology vanishes, so L(f) = 1+d+...+d^n; for even n and d = -r the sum is (r^{n+1}+1)/(r+1) > 0 and for d >= 0 positive, so L(f) != 0 and Theorem 2C.3 p.179 gives a fixed point; for odd n the sum vanishes only at d = -1. Not covered: the construction of an actual fixed-point-free map in the exceptional case, which the exercise refers to §2.C Ex.3 for.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the Lefschetz computation, which is what Queue D asks for on this card. The ring, the pullback of the generator, the Lefschetz number and the two parity cases are separate steps, with the two closed forms for the alternating sums written out; both published sets (Li §3.2 Ex 4 on PDF p. 54 and Sam §3.2 Ex 4 on printed pp. 13-14) give exactly this argument. Two repairs: the card cited Hatcher's Example 3.12 (printed p. 213) for the ring structure, but that example only announces the result, which is Theorem 3.19 on printed p. 220, now cited; and a duplicated paragraph repeating the argument sat after the proof outside any block, and is removed. The Lefschetz theorem locator, Theorem 2C.3 on printed p. 179, is confirmed against the book.
---

::: {.problem}
Apply the Lefschetz fixed point theorem to show that every map $f: \CP^n \to \CP^n$ has a fixed point if $n$ is even, using the fact that $f^*: H^*(\CP^n; \ZZ) \to H^*(\CP^n; \ZZ)$ is a ring homomorphism.
When $n$ is odd show there is a fixed point unless $f^*(\alpha) = -\alpha$, for $\alpha$ a generator of $H^2(\CP^n; \ZZ)$.
[See Exercise 3 in §2.C for an example of a map without fixed points in this exceptional case.]
:::

::: {.solution}
The published solutions are **Guanyu Li, *Hatcher.pdf*, §3.2 Exercise 4, PDF p. 54** (`tmp/sources/hatcher-solutions-guanyu-li.pdf`) and **Steven V. Sam, *Solutions to Algebraic Topology* (2008), §3.2 Exercise 4, printed pp. 13--14** (`tmp/sources/hatcher-solutions-sam-2008.pdf`); the Lefschetz computation, the two sign cases and the exceptional case $f^*(\alpha)=-\alpha$ are theirs. The statement is Hatcher, *Algebraic Topology* (2002), §3.2 Exercise 4, printed p. 229. One locator in both sets is corrected here: the ring structure is Hatcher's **Theorem 3.19, printed p. 220**, not his Example 3.12, which only announces it on printed p. 213 (Sam cites it as "Theorem 3.12", which Hatcher does not have).

::: pf

::: {.pf-step #ring}
$H^*(\CP^n;\ZZ)=\ZZ[\alpha]/(\alpha^{n+1})$ with $\abs{\alpha}=2$, so $H^{2j}(\CP^n;\ZZ)=\ZZ\cdot\alpha^j$ for $0\le j\le n$ and $H^{k}(\CP^n;\ZZ)=0$ for odd $k$.

::: pf-proof
This is Theorem 3.19 of §3.2, printed p. 220: the cohomology ring of $\CP^n$ with $\ZZ$ coefficients is the truncated polynomial ring on a class of degree $2$, and a truncated polynomial ring is free on $1,\alpha,\dots,\alpha^n$ in the degrees $0,2,\dots,2n$.
:::

:::

::: {.pf-step #pullback}
There is an integer $d$ with $f^*(\alpha)=d\alpha$, and then $f^*(\alpha^j)=d^j\alpha^j$ for $0\le j\le n$.

::: pf-proof
$H^2(\CP^n;\ZZ)=\ZZ\cdot\alpha$ is infinite cyclic, so the homomorphism $f^*$ in degree $2$ is multiplication by a unique integer $d$. $f^*$ is a ring homomorphism by Proposition 3.10, printed p. 210, so $f^*(\alpha^j)=f^*(\alpha)^j=(d\alpha)^j=d^j\alpha^j$; the classes $\alpha^j$ generate the free group in each even degree by step [](#ring){.pf-ref}.
:::

:::

::: {.pf-step #lefschetz-number}
$L(f)=1+d+d^2+\cdots+d^n$.

::: pf-proof
The Lefschetz number of a map of a finite complex is $L(f)=\sum_k(-1)^k\operatorname{tr}\bigl(f^*:H^k\to H^k\bigr)$. In degree $2j$ the trace is $d^j$, because the group is free of rank one on $\alpha^j$ and step [](#pullback){.pf-ref} scales it by $d^j$; in odd degrees the group vanishes; and the sign $(-1)^{2j}$ is $+1$. Summing over $0\le j\le n$ gives the claim.
:::

:::

::: {.pf-step #even}
If $n$ is even then $L(f)\ne0$, so $f$ has a fixed point.

::: pf-proof
If $d\ge0$ then every term $d^j$ is nonnegative and the first is $1$, so $L(f)\ge1$. If $d<0$, write $d=-r$ with $r\ge1$; then $n+1$ is odd and
$$
L(f)=1-r+r^2-\cdots-r^n=\frac{1-(-r)^{n+1}}{1+r}=\frac{1+r^{n+1}}{1+r}>0 .
$$
So $L(f)\ne0$ in either case. $\CP^n$ is a finite CW complex, so the Lefschetz fixed point theorem, Theorem 2C.3, printed p. 179, applies and gives a point $x$ with $f(x)=x$.
:::

:::

::: {.pf-step #odd}
If $n$ is odd then $L(f)=0$ exactly when $d=-1$, that is exactly when $f^*(\alpha)=-\alpha$; for every other $d$ the map has a fixed point.

::: pf-proof
Let $n$ be odd. If $d\ge0$ then $L(f)\ge1$ as in step [](#even){.pf-ref}. If $d=-r$ with $r\ge1$, then $n-1$ is even and
$$
L(f)=1-r+r^2-\cdots-r^n=(1-r)\bigl(1+r^2+r^4+\cdots+r^{n-1}\bigr),
$$
since expanding the right side telescopes to the alternating sum. The second factor is at least $1$, so $L(f)=0$ exactly when $r=1$, that is $d=-1$; and $d=-1$ is precisely $f^*(\alpha)=-\alpha$ by step [](#pullback){.pf-ref}. For all other $d$ the number $L(f)$ is nonzero, and Theorem 2C.3, printed p. 179, gives a fixed point. The one case left open is the exceptional $f^*(\alpha)=-\alpha$, for which the argument says nothing; §2.C Exercise 3 exhibits a map of that kind without fixed points.
:::

:::

:::
:::
