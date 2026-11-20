---
schema: qual/card@1
id: PR-2ZW5Z
kind: proposition
title: Multiplicativity of the norm $N_{K/\QQ}$ and units of $\OO_K$
slogan: 'Number-field norms multiply, are integral on $\OO_K$, and detect units by norm $\pm1$.'
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Number Theory
relations: []
review: draft
---

::: {.proposition}
Let $K$ be a number field with ring of integers $\OO_K$.
Write $N(a)\coloneqq N_{K/\QQ}(a)$ for the [[D-8SVC3|norm]] of $a$.

- For all $a, b \in K$, $N(ab) = N(a)N(b)$.

- $N(\OO_K) \subseteq \ZZ$.

- For $a, b \in \OO_K$, if $a$ [[D-AVBIP|divides]] $b$ in $\OO_K$, then $N(a) \divides N(b)$ in $\ZZ$.

- For $a \in \OO_K$, $a$ is a [[D-QQIQZ|unit]] of $\OO_K$ if and only if $N(a) = \pm 1$.
:::

::: {.proof}
Multiplicativity is the proposition on [[D-8SVC3]], and it is used below in the form $N(ab)=N(a)N(b)$.

For integrality, let $\sigma_1,\ldots,\sigma_r$ be the distinct embeddings of $K$ into an algebraic closure of $\QQ$, so that
$$
N(a)=\bigl(\sigma_1(a)\cdots\sigma_r(a)\bigr)^{[K:\QQ]_i}
$$
by [@Hun74, chapter V, §7, Definition 7.1].
An element of $\OO_K$ is an algebraic integer, that is, a root of a monic polynomial $g\in\ZZ[x]$ [@Hun74, chapter V, §3, Exercise 18].
Each $\sigma_i$ fixes $\QQ$, so $g(\sigma_i(a))=\sigma_i(g(a))=0$ and $\sigma_i(a)$ is an algebraic integer as well; sums and products of algebraic integers are algebraic integers [@Hun74, chapter V, §3, Exercise 18(d)], so $N(a)$ is an algebraic integer.
It lies in $\QQ$ by [@Hun74, chapter V, §7, Theorem 7.3(iii)], and an algebraic integer in $\QQ$ is an integer [@Hun74, chapter V, §3, Exercise 18(b)], so $N(\OO_K)\subseteq\ZZ$.

If $a\divides b$ in $\OO_K$, say $b=ac$ with $c\in\OO_K$, then $N(b)=N(a)N(c)$ with $N(c)\in\ZZ$ by the previous paragraph, so $N(a)\divides N(b)$ in $\ZZ$.

For the unit criterion, let $a\in\OO_K$.
If $a$ is a unit, then $1=N(1)=N(a)N(\inverseof{a})$ and both factors lie in $\ZZ$, so $N(a)=\pm1$.

Conversely let $N(a)=\pm1$, and let $f=x^n+c_{n-1}x^{n-1}+\cdots+c_0$ be the minimal polynomial of $a$ over $\QQ$.
It is monic with integer coefficients: $a$ is a root of a monic $g\in\ZZ[x]$ and $f$ divides $g$ in $\QQ[x]$, and Gauss's lemma [@Hun74, chapter III, §6, Lemma 6.11] turns that into $f\in\ZZ[x]$, since writing $f=F/m$ and $g=fh$ with $h=H/k$, where $F$ and $H$ are primitive, leaves $mk\,g=FH$ with content $(FH)=1$ and content $(mk\,g)=mk$, whence $mk=1$.
By [@Hun74, chapter V, §7, Theorem 7.3(iii)] applied to $F=\QQ(a)$ and $K=\QQ$ the constant term is $c_0=(-1)^nN_{\QQ}^{\QQ(a)}(a)$, and parts (i), (ii) and (iv) of the same theorem give
$$
N(a)=N_{\QQ}^{\QQ(a)}(a)^{[K:\QQ(a)]}=\bigl((-1)^nc_0\bigr)^{[K:\QQ(a)]}.
$$
A positive integer power of the integer $(-1)^nc_0$ equals $\pm1$ only when $c_0=\pm1$.
Then $f(a)=0$ reads
$$
a\,\bigl(a^{n-1}+c_{n-1}a^{n-2}+\cdots+c_1\bigr)=-c_0=\mp1,
$$
and the second factor lies in $\ZZ[a]\subseteq\OO_K$, so $a$ is a unit of $\OO_K$.
:::
