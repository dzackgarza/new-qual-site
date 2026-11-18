---
schema: qual/card@1
id: E-HAT-3.C-7
kind: problem
title: Primitive elements of $\ZZ_p[x]$
classification:
  areas:
  - topology
  topics:
  - H-Spaces
  - Hopf Algebras
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.C, Exercise 7; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the proof, including the case split. If $p=2$ or $\deg x$ is even the two tensor summands
    of $\Delta x$ commute, and the Frobenius identity makes every $x^{p^r}$ primitive. Conversely
    an exponent $m=p^rq$ with $q>1$ gives the mixed term $x^{(q-1)p^r}\otimes x^{p^r}$ with
    coefficient $q\ne0$ in $\ZZ_p$, and distinct total powers cannot cancel it. For $p$ odd and
    $\deg x$ odd, $y=x^2$ is primitive by the Koszul sign ($\Delta(x^2)=x^2\otimes1+1\otimes x^2$
    because the two cross terms cancel), so the primitives are spanned by $x$ and the
    $y^{p^r}=x^{2p^r}$; the odd part contributes only $x$ since $\Delta(xy^m)$ has the uncancelled
    mixed term $x\otimes y^m$ for $m>0$.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument above, with the case split made
    explicit: the binomial expansion of $(\Delta x)^n$ in the commuting case, primitivity of
    $x^n$ exactly for $n$ a prime power, passage from monomials to arbitrary elements by
    linear independence of the $x^a\otimes x^b$, then the odd case through $y=x^2$ primitive
    (Koszul sign) and the odd part $x\ZZ_p[y]$. Added on the card: the bidegree $(ad,bd)$
    independence argument that rules out cancellation, and the answer in both cases at once.
    Statement re-read in Hatcher, §3.C Exercise 7, printed p. 291, the page carrying the
    exercise. Not claimed: a retained solution set; the Hatcher sets in `tmp/sources` do not
    reach §3.C, so the argument is the card's own.
---

::: {.problem}
What are the primitive elements of the Hopf algebra $\ZZ_p[x]$ for $p$ prime?
:::

::: {.solution}
The statement is Hatcher, *Algebraic Topology* (2002), §3.C Exercise 7, printed p. 291. No retained solution set covers this exercise — the Hatcher sets in `tmp/sources` (Guanyu Li, DeMason, Sam 2008, Koukpari, the Stanford Math 215C sets) reach parts of Chapters 1–3 and none treats §3.C — so the argument below is the card's own.

Throughout $A=\ZZ_p[x]$ with $x$ primitive, $\Delta x=x\otimes1+1\otimes x$, products in $A\otimes A$ taken with the Koszul sign $(a\otimes b)(c\otimes d)=(-1)^{\abs{b}\abs{c}}ac\otimes bd$, and $d=\abs{x}>0$; $\binom nk$ denotes the binomial coefficient reduced modulo $p$. Two conventions are read off the exercise: the polynomial algebra structure on $x^n$ is the *product* under consideration, which for the Hopf algebra $H_*J(S^n)$ of Example 3C.7, printed p. 288, carries no sign in odd degrees, so $x^2\ne0$ even when $d$ is odd.

::: pf

::: {.pf-step #setup}
$x$ is primitive, $\Delta$ is an algebra homomorphism into $A\otimes A$, and the monomials $x^a\otimes x^b$ are linearly independent over $\ZZ_p$.

::: pf-proof
$\Delta x=x\otimes1+1\otimes x$ is the hypothesis, and a counit $\varepsilon$ with $\varepsilon(x)=0$ exists because $x$ is primitive. A Hopf algebra's coproduct is a map of algebras into the signed tensor product, so $\Delta(x^n)=(\Delta x)^n$ for $n\ge0$. The elements $x^a\otimes x^b$ have bidegree $\bigl(ad,bd\bigr)$, and $d>0$, so $x^a\otimes x^b$ lies in the span of the basis monomials of $A\otimes A$ of that bidegree, which is one-dimensional when $a$ and $b$ are the only pair with those degrees; hence the $x^a\otimes x^b$ are $\ZZ_p$-linearly independent. Consequently two different $\ZZ_p$-linear combinations of monomials are distinct, and cancellation between monomials cannot occur.

:::

:::

::: {.pf-step #expansion}
If $d$ is even or $p=2$, then
$$
\Delta(x^n)=\sum_{k=0}^{n}\binom nk\,x^{k}\otimes x^{n-k}.
$$

::: pf-proof
The cross terms of $(\Delta x)^n$ commute when $d$ is even, since then $\abs{x\otimes1}\abs{1\otimes x}=d\cdot0=0$ and also $d\cdot d$ is even; they commute when $p=2$ because then $+1=-1$. In either case the number of ways to choose the $k$ factors contributing $x\otimes1$ out of $n$ is $\binom nk$, and the product of those with the remaining $x^{n-k}$ factors is $x^{k}\otimes x^{n-k}$ by step [](#setup){.pf-ref}.

:::

:::

::: {.pf-step #power}
In the situation of step [](#expansion){.pf-ref}, $x^{n}$ is primitive exactly when $n$ is a power of $p$.

::: pf-proof
$1\otimes x^n$ and $x^n\otimes1$ are the extreme terms $k=0$ and $k=n$ of the expansion, so $x^n$ is primitive exactly when every coefficient $\binom nk$ with $0<k<n$ vanishes in $\ZZ_p$. If $n=p^r$ then $p$ divides $\binom{p^r}{k}$ for $0<k<p^r$, by the usual divisibility of intermediate binomial coefficients of a prime power, so every such coefficient vanishes. Otherwise $n=p^rq$ with $r\ge0$ and $q>1$, $p\nmid q$; taking $k=p^r$ gives $\binom{p^rq}{p^r}\equiv q\not\equiv0\pmod p$, so the mixed term $x^{(q-1)p^r}\otimes x^{p^r}$ survives with nonzero coefficient, and by linear independence no other monomial can cancel it. Hence $x^n$ is not primitive.

:::

:::

::: {.pf-step #linear}
In the situation of step [](#expansion){.pf-ref}, an element $f=\sum_{n\ge0}c_nx^n$ is primitive exactly when $c_n=0$ for every $n$ that is not a power of $p$.

::: pf-proof
$\Delta$ is $\ZZ_p$-linear, so
$$
\Delta f-f\otimes1-1\otimes f=\sum_{n\ge0}c_n\sum_{0<k<n}\binom nk\,x^{k}\otimes x^{n-k}.
$$
By linear independence of the monomials, the coefficient of $x^{k}\otimes x^{n-k}$ in this sum comes from $n=k+(n-k)$ alone, that is, it is $c_n\binom nk$. So the sum vanishes exactly when $c_n\binom nk=0$ in $\ZZ_p$ for all $0<k<n$ and all $n$, which by step [](#power){.pf-ref} holds exactly when every $c_n$ with $n$ not a power of $p$ is zero.

:::

:::

::: {.pf-step #odd-evenpart}
If $p$ is odd and $d$ is odd, $y\coloneqq x^{2}$ is primitive, and the primitive elements of the even part $\ZZ_p[y]\subset A$ are the $\ZZ_p$-linear combinations of $y,y^{p},y^{p^{2}},\ldots$.

::: pf-proof
$(\Delta x)^2=x^2\otimes1+x\otimes x+(-1)^{d\cdot d}x\otimes x+1\otimes x^2$; as $d$ is odd, $(-1)^{d^2}=-1$, and $1+(-1)=0$ in $\ZZ_p$ because $p$ is odd, so $\Delta y=y\otimes1+1\otimes y$. The degree of $y$ is $2d$, which is even, so step [](#expansion){.pf-ref} and step [](#power){.pf-ref} apply verbatim with $y$ in place of $x$: $y^{m}$ is primitive exactly when $m$ is a power of $p$. The even part of $A$ is spanned by the even powers of $x$, that is, by the $y^{m}$, and the argument of step [](#linear){.pf-ref} carries over unchanged, so the primitives of the even part are the spans of $y^{p^r}$.

:::

:::

::: {.pf-step #odd-oddpart}
If $p$ is odd and $d$ is odd, the only primitive elements of $A$ in odd degrees are the multiples of $x$.

::: pf-proof
Every element of odd degree has the form $f=x\,g(y)$ with $g(y)=\sum_m g_my^m$, since the odd powers of $x$ are $x\,y^{m}$. As $\Delta$ is multiplicative, $\Delta f=\Delta x\cdot\Delta g(y)=(x\otimes1+1\otimes x)\sum_m g_m(y\otimes1+1\otimes y)^m$. For $m\ge1$ the monomial $x\otimes y^{m}$ occurs in this sum with coefficient $g_m$, coming from the term $x\otimes1$ times $1\otimes y^{m}$, and no other term of the product has bidegree $\bigl(d,2dm\bigr)$: any further contribution either carries an $x$-factor in the second slot or two $x$-factors in the first. On the other hand $f\otimes1+1\otimes f=xg(y)\otimes1+1\otimes xg(y)$ has no term of bidegree $\bigl(d,2dm\bigr)$ with $m\ge1$. So primitivity forces $g_m=0$ for every $m\ge1$, that is, $f=g_0x$.

:::

:::

::: {.pf-step #answer}
The primitive elements of $\ZZ_p[x]$ are: the $\ZZ_p$-linear combinations of $x,x^{p},x^{p^{2}},\ldots$ when $d$ is even or $p=2$; and the $\ZZ_p$-linear combinations of $x,x^{2},x^{2p},x^{2p^{2}},\ldots$ when $p$ is odd and $d$ is odd.

::: pf-proof
In the first case step [](#linear){.pf-ref} gives the answer directly. In the second, $A$ is the direct sum of its even part $\ZZ_p[y]$ and the set of odd-degree elements $x\ZZ_p[y]$, and a sum of a primitive element of each part is primitive; step [](#odd-evenpart){.pf-ref} gives $y,y^p,y^{p^2},\ldots$, that is $x^2,x^{2p},x^{2p^2},\ldots$, and step [](#odd-oddpart){.pf-ref} gives the multiples of $x$.

:::

:::

:::
:::
