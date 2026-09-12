---
schema: qual/card@1
id: P-X7EHF
kind: problem
title: The nilradical is an ideal contained in every prime, primes avoiding powers
  of a non-nilpotent, and the nilradical is the intersection of all primes
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Prime Ideals
  - Zorn's Lemma
relations: []
review: draft
---

::: problem
Let $R$ be a commutative ring with $1\neq 0$.
Recall that $x\in R$ is *nilpotent* iff $x^n = 0$ for some positive integer $n$.

a.
Show that the collection of nilpotent elements in $R$ forms an ideal.

b.
Show that if $x$ is nilpotent, then $x$ is contained in every prime ideal of $R$.

c.
  Suppose $x\in R$ is not nilpotent and let $S = \theset{x^n \suchthat n\in \NN}$.
  There is at least on ideal of $R$ disjoint from $S$, namely $(0)$.

  By Zorn's lemma the set of ideals disjoint from $S$ has a maximal element with respect to inclusion, say $I$.
  In other words, $I$ is disjoint from $S$ and if $J$ is any ideal disjoint from $S$ with $I\subseteq J \subseteq R$ then $J=I$ or $J=R$.

  Show that $I$ is a prime ideal.

d. 
Deduce from (a) and (b) that the set of nilpotent elements of $R$ is the intersection of all prime ideals of $R$.
:::

::: solution
(a) Let $\mathcal N$ be the set of nilpotent elements of $R$. Certainly
$0\in\mathcal N$. If $a^m=0$ and $b^n=0$, then every term in the binomial
expansion of
\[
(a+b)^{m+n-1}
\]
contains either a factor $a^m$ or a factor $b^n$, so
$(a+b)^{m+n-1}=0$. Thus $a+b\in\mathcal N$. Also, for $r\in R$,
\[
(ra)^m=r^m a^m=0,
\]
so $ra\in\mathcal N$. Hence $\mathcal N$ is an ideal.

(b) Let $\mathfrak p$ be prime and let $x^n=0$. Since
$x^n\in\mathfrak p$, primality implies $x\in\mathfrak p$ by repeatedly
factoring $x^n=x\cdot x^{n-1}$. Thus every nilpotent element belongs to every
prime ideal.

(c) Let $I$ be maximal among ideals disjoint from
$S=\{x^n:n\in\NN\}$. Suppose $ab\in I$ but $a\notin I$ and $b\notin I$.
Then both $I+(a)$ and $I+(b)$ properly contain $I$, so maximality implies that
each meets $S$. Hence for some $m,n\ge1$,
\[
x^m=i_1+r_1a,
\qquad
x^n=i_2+r_2b
\]
with $i_1,i_2\in I$ and $r_1,r_2\in R$. Multiplying gives
\[
x^{m+n}
=i_1i_2+i_1r_2b+i_2r_1a+r_1r_2ab\in I,
\]
contradicting $I\cap S=\varnothing$. Therefore $a\in I$ or $b\in I$, so
$I$ is prime.

(d) Part (b) gives
\[
\mathcal N\subseteq\bigcap_{\mathfrak p\text{ prime}}\mathfrak p.
\]
Conversely, if $x$ is not nilpotent, part (c) produces a prime ideal $I$
disjoint from $\{x^n:n\ge1\}$; in particular $x\notin I$. Thus $x$ is not in
the intersection of all prime ideals. Hence
\[
\boxed{\mathcal N=\bigcap_{\mathfrak p\text{ prime}}\mathfrak p}.
\]
The last step uses part (c) in addition to the earlier parts.
:::
