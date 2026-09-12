---
schema: qual/card@1
id: E-SMI-8000E-GG4
kind: problem
title: Every finite abelian group is a Galois group over Q via cyclotomic extensions
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Checked the Smith packet pointer and the Dummit--Foote Corollary 28 argument; the required number-theoretic input is the existence of primes congruent to 1 modulo a prescribed integer."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Proved the needed prime-congruence input using cyclotomic polynomials, then used the structure theorem, CRT, cyclotomic Galois groups, and Galois correspondence to realize an arbitrary finite abelian group."
---

::: {.exercise}
Work problems 14, 15, 16, 17, page 557 of Dummit and Foote, then deduce Corollary 28, page 600: every finite abelian group occurs as the Galois group over $\QQ$ of some subextension of a cyclotomic extension.
:::

::: solution
We make explicit the number-theoretic input supplied by the cited exercise
chain and then carry out the deduction of Corollary 28 [@DF04].

<1>1. For every positive integer $m$, there are infinitely many primes $p$ with $p\equiv1\pmod m$.
::: proof
The case $m=1$ is immediate, so assume $m>1$. We use the standard
cyclotomic-polynomial fact: if a prime $q$ does not divide $m$ and
$$
q\mid\Phi_m(a),
$$
then the image of $a$ in $\mathbf F_q^\times$ has order exactly $m$. Hence
$$
m\mid(q-1),
$$
so $q\equiv1\pmod m$ [@DF04].

Suppose, toward a contradiction, that the primes congruent to $1$ modulo $m$
are exactly
$$
p_1,\ldots,p_r.
$$
Choose a positive integer $t$ large enough that
$$
|\Phi_m(t m p_1\cdots p_r)|>1,
$$
which is possible because $\Phi_m$ is a nonconstant monic polynomial, and set
$$
a=t m p_1\cdots p_r.
$$
Because $m>1$, the cyclotomic polynomial has constant term
$$
\Phi_m(0)=1.
$$
Thus every prime dividing $a$ is coprime to $\Phi_m(a)$. Since
$|\Phi_m(a)|>1$, choose a prime
$$
q\mid\Phi_m(a).
$$
Then $q\nmid a$, in particular $q\nmid m$ and $q\ne p_i$ for every $i$.
By the cyclotomic-order fact above,
$$
q\equiv1\pmod m,
$$
contradicting completeness of the list $p_1,\ldots,p_r$. Hence infinitely
many such primes exist.
:::

<1>2. Write the given finite abelian group as a product of cyclic groups.
::: proof
Let $A$ be any finite abelian group. By the structure theorem for finite
abelian groups, there are positive integers $n_1,\ldots,n_r$ such that
$$
A\cong C_{n_1}\times\cdots\times C_{n_r}.
$$
We may discard any factor with $n_i=1$.
:::

<1>3. Choose distinct primes whose unit groups have the required cyclic quotients.
::: proof
By step <1>1, choose distinct primes
$$
p_i\equiv1\pmod{n_i}
$$
for $1\le i\le r$. Since $p_i$ is prime,
$$
(\mathbf Z/p_i\mathbf Z)^\times
$$
is cyclic of order $p_i-1$. Because $n_i\mid p_i-1$, it has a unique subgroup
$H_i$ of order
$$
\frac{p_i-1}{n_i},
$$
and therefore
$$
(\mathbf Z/p_i\mathbf Z)^\times/H_i\cong C_{n_i}.
$$
:::

<1>4. Assemble the cyclic quotients inside one cyclotomic Galois group.
::: proof
Put
$$
N=p_1p_2\cdots p_r.
$$
The Chinese remainder theorem gives
$$
(\mathbf Z/N\mathbf Z)^\times
\cong
\prod_{i=1}^r(\mathbf Z/p_i\mathbf Z)^\times.
$$
Let
$$
H=H_1\times\cdots\times H_r
$$
under this identification. Then
$$
\begin{aligned}
(\mathbf Z/N\mathbf Z)^\times/H
&\cong
\prod_{i=1}^r
\bigl((\mathbf Z/p_i\mathbf Z)^\times/H_i\bigr)\\
&\cong C_{n_1}\times\cdots\times C_{n_r}\\
&\cong A.
\end{aligned}
$$
:::

<1>5. Apply cyclotomic Galois theory and the fundamental theorem of Galois theory.
::: proof
Let
$$
L=\mathbf Q(\zeta_N).
$$
Cyclotomic Galois theory gives
$$
\operatorname{Gal}(L/\mathbf Q)
\cong(\mathbf Z/N\mathbf Z)^\times
$$
via
$$
a\longmapsto(\zeta_N\mapsto\zeta_N^a)
$$
[@DF04]. Let the subgroup corresponding to $H$ under this isomorphism again
be denoted $H$, and set
$$
K=L^H.
$$

The ambient Galois group is abelian, so $H$ is normal. Hence
$K/\mathbf Q$ is Galois, and the fundamental theorem of Galois theory yields
$$
\operatorname{Gal}(K/\mathbf Q)
\cong\operatorname{Gal}(L/\mathbf Q)/H
\cong A.
$$
Thus
$$
\boxed{\text{every finite abelian group occurs as }
\operatorname{Gal}(K/\mathbf Q)
\text{ for a subfield }K\subseteq\mathbf Q(\zeta_N).}
$$
:::
:::
