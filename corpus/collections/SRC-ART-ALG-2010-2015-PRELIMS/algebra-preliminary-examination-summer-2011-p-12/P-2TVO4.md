---
schema: qual/card@1
id: P-2TVO4
kind: problem
title: The splitting field of $(x^p-2)(x^q-2)$ over $\mathbb{Q}$
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Galois Theory
  - Roots of Unity
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked every part of Summer 2011 problem 6 on PDF page 12, including the odd-prime and nondivisibility hypotheses."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the Bezout recovery of both generators, coprimality in the degree calculation, existence of every automorphism, distinct conjugate complements, and the exact Sylow fixed field."
---

::: {.problem}
Let $p < q$ be two distinct odd primes such that $p \nmid q - 1$.
Let $n = pq$ and $\zeta_n$ be a primitive $n$-th root of unity in $\mathbb{C}$.

a. Show that the splitting field $E$ of $(x^p - 2)(x^q - 2)$ over $\mathbb{Q}$ is $\mathbb{Q}(\zeta_n, \sqrt[n]{2})$.

b. Determine $[E : \mathbb{Q}]$.

c. Find two subgroups of $\mathrm{Gal}(E/\mathbb{Q})$ of order $(p-1)(q-1)$.

d. Show that the Sylow $p$-subgroup of $\mathrm{Gal}(E/\mathbb{Q})$ is normal and determine its fixed field.
:::

::: hint
Since $\gcd(p,q)=1$, there are integers $a,b$ such that
$pa+qb=1$.
:::

::: solution
Put $\alpha=\sqrt[n]{2}>0$, $\zeta=\zeta_n$, and
$L=\mathbb Q(\zeta)$. Write $m=(p-1)(q-1)$.

<1>1. The splitting field is $E=\mathbb Q(\zeta,\alpha)$.

::: proof
The roots of $x^p-2$ are
$\alpha^q(\zeta^q)^j$, $0\leq j<p$; the roots of
$x^q-2$ are $\alpha^p(\zeta^p)^k$, $0\leq k<q$.
All lie in $\mathbb Q(\zeta,\alpha)$.
Conversely, the splitting field contains $\alpha^q$ and
$\alpha^p$, and their nonzero-root ratios give $\zeta^q$
and $\zeta^p$. Choose integers $a,b$ with $pa+qb=1$.
Then
$$
\alpha=(\alpha^p)^a(\alpha^q)^b,
\qquad \zeta=(\zeta^p)^a(\zeta^q)^b
$$
also belong to the splitting field. Negative exponents
are allowed because all four elements are nonzero.
This proves equality of the two fields.
:::

<1>2. The degree is
$$
\boxed{[E:\mathbb Q]=pq(p-1)(q-1)=nm}.
$$

::: proof
The polynomial $x^n-2$ is Eisenstein at two, so
$[\mathbb Q(\alpha):\mathbb Q]=n$ [@DF04].
The cyclotomic degree formula gives
$[L:\mathbb Q]=\varphi(pq)=(p-1)(q-1)=m$ [@DF04].
Neither $p$ nor $q$ divides $m$: for $p$ this uses
$p\nmid q-1$, and for $q$ it follows from
$p-1<q$ and $q\nmid q-1$. Thus $\gcd(n,m)=1$.

The degree $[E:\mathbb Q]$ is divisible by both $n$ and
$m$, since $E$ contains both subfields. It is consequently
divisible by their product $nm$. On the other hand,
$E=L(\alpha)$ and $\alpha$ satisfies $x^n-2$ over $L$,
so $[E:L]\leq n$ and $[E:\mathbb Q]\leq nm$.
Both bounds force equality. In particular $x^n-2$ remains
irreducible over $L$, and $[E:L]=n$.
:::

<1>3. The Galois group has the explicit form
$$
G=\{\tau^a\sigma_b:a\in\mathbb Z/n\mathbb Z,
\ b\in(\mathbb Z/n\mathbb Z)^\times\},
$$
where
$$
\tau(\alpha)=\zeta\alpha,\quad \tau(\zeta)=\zeta,
\qquad \sigma_b(\alpha)=\alpha,\quad \sigma_b(\zeta)=\zeta^b.
$$
They satisfy $\sigma_b\tau\sigma_b^{-1}=\tau^b$.

::: proof
Since $x^n-2$ is irreducible over $L$, sending $\alpha$
to its root $\zeta\alpha$ defines an $L$-embedding of $E$
into itself. Its image contains $\alpha=\zeta^{-1}(\zeta\alpha)$,
so it is the automorphism $\tau$, of order exactly $n$.

For each unit $b$ modulo $n$, the cyclotomic automorphism
$\gamma_b$ of $L$ sends $\zeta$ to $\zeta^b$ [@DF04].
Every element of $E$ has a unique expression
$\sum_{j=0}^{n-1}c_j\alpha^j$, $c_j\in L$.
Define $\sigma_b$ by applying $\gamma_b$ to each coefficient.
This preserves addition. It preserves multiplication because
products are reduced using $\alpha^n=2$, whose right side
is fixed by $\gamma_b$. Its inverse is $\sigma_{b^{-1}}$.
Thus these are genuine field automorphisms with the asserted
values, and $\sigma_b\sigma_c=\sigma_{bc}$.

The conjugation identity follows by evaluating both sides
on $\alpha$ and $\zeta$, which generate $E$.
The maps $\tau^a\sigma_b$ are all distinct: their values
on $\zeta$ determine $b$, and their values on $\alpha$
then determine $a$. The splitting field is Galois in
characteristic zero and has degree $nm$, so these $nm$
automorphisms exhaust its Galois group [@DF04].
:::

<1>4. Two distinct subgroups of order $m$ are
$$
H_0=\{\sigma_b:b\in(\mathbb Z/n\mathbb Z)^\times\},
\qquad
H_1=\tau H_0\tau^{-1}
=\{\tau^{1-b}\sigma_b:b\in(\mathbb Z/n\mathbb Z)^\times\}.
$$

::: proof
The composition rule in step <1>3 makes $H_0$ a subgroup
isomorphic to $(\mathbb Z/n\mathbb Z)^\times$, of order
$m$. Its conjugate $H_1$ is a subgroup of the same order.
The displayed description of $H_1$ follows from
$\sigma_b\tau^{-1}=\tau^{-b}\sigma_b$.
Every element of $H_0$ fixes $\alpha$, while every element
of $H_1$ fixes $\tau(\alpha)=\zeta\alpha$.
But $\sigma_{-1}\in H_0$ sends $\zeta\alpha$ to
$\zeta^{-1}\alpha\ne\zeta\alpha$, since $\zeta$ has
odd order $n>2$. Hence $\sigma_{-1}\notin H_1$,
proving that these two subgroups are distinct.
:::

<1>5. The unique Sylow $p$-subgroup and its fixed field are
$$
P=\langle\tau^q\rangle,
\qquad
\boxed{E^P=\mathbb Q(\zeta_n,\sqrt[q]{2})}.
$$

::: proof
Since $|G|=pqm$ and $p\nmid qm$, a Sylow $p$-subgroup
has order $p$. The element $\tau^q$ has order $p$, so
its subgroup $P$ is Sylow. Conjugation by $\tau$ fixes
$\tau^q$, and conjugation by $\sigma_b$ sends it to
$\tau^{bq}$, another generator of $P$ because $p\nmid b$.
The elements $\tau$ and all $\sigma_b$ generate $G$,
so $P$ is normal in $G$. Sylow conjugacy then makes it
the unique Sylow $p$-subgroup [@DF04].

Put $M=\mathbb Q(\zeta,\alpha^p)$, noting that
$\alpha^p=\sqrt[q]{2}$. The subgroup $P$ fixes both
generators, because
$(\tau^q)(\alpha^p)=\zeta^{pq}\alpha^p=\alpha^p$.
Thus $M\subseteq E^P$. Also $E=M(\alpha)$ and $\alpha$
satisfies $T^p-\alpha^p\in M[T]$, so $[E:M]\leq p$.
The $p$ elements
$\tau^{qj}(\alpha)=\zeta^{qj}\alpha$, $0\leq j<p$,
are distinct, and each is a root of the minimal polynomial
of $\alpha$ over $E^P$, because these automorphisms fix
its coefficients. Hence $[E:E^P]\geq p$.
The tower law yields
$$
p\leq[E:E^P]\leq[E:M]\leq p,
$$
so equality holds throughout and $[E^P:M]=1$.
Therefore $E^P=M$, as claimed.
:::
:::
