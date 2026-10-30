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

::: {.problem}
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

::: {.solution}

Let $\mathcal N=\{a\in R:a^n=0\text{ for some }n\geq1\}$.

::: pf

::: {.pf-step #s1-1}

The set $\mathcal N$ is an ideal of $R$.


::: pf-proof

The element $0$ is nilpotent. If $a^m=b^n=0$, then every term in the binomial expansion of $(a-b)^{m+n-1}$ contains at least $m$ factors $a$ or at least $n$ factors $b$, hence vanishes. Therefore $a-b$ is nilpotent. For any $r\in R$, $(ra)^m=r^ma^m=0$, proving closure under scalar multiplication.

:::

:::

::: {.pf-step #s1-2}

Every prime ideal of $R$ contains $\mathcal N$.


::: pf-proof

If $a^m=0\in\mathfrak p$ with $\mathfrak p$ prime, repeated application of the implication $uv\in\mathfrak p\Rightarrow u\in\mathfrak p$ or $v\in\mathfrak p$ yields $a\in\mathfrak p$. Thus $\mathcal N\subseteq\mathfrak p$.

:::

:::

::: {.pf-step #s1-3}

If $x$ is not nilpotent and $I$ is maximal among ideals disjoint from $S=\{x^n:n\geq1\}$, then $I$ is prime.


::: pf-proof

The ideal $I$ is proper, because $x\in S$ and $I\cap S=\varnothing$. Suppose $ab\in I$ but $a,b\notin I$. Then the larger ideals $I+(a)$ and $I+(b)$ cannot be disjoint from $S$ by maximality. Hence $x^m=i+ra$ and $x^n=j+sb$ for suitable $i,j\in I$, $r,s\in R$, and positive integers $m,n$. Multiplying gives
$$
x^{m+n}=ij+is b+jr a+rsab\in I,
$$
contradicting $I\cap S=\varnothing$. Therefore $a\in I$ or $b\in I$, proving primality.

:::

:::

::: {.pf-step #s1-4}

The nilradical equals the intersection of all prime ideals:
$$
\boxed{\mathcal N=\bigcap_{\mathfrak p\in\operatorname{Spec}R}\mathfrak p}.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives containment from left to right. Conversely, if $x\notin\mathcal N$, step [](#s1-3){.pf-ref} supplies a prime ideal disjoint from the powers of $x$, so in particular it does not contain $x$. Thus no nonnilpotent element belongs to the displayed intersection.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} establish parts (a)--(d), respectively.

:::

:::

:::
