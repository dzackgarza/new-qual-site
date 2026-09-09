---
schema: qual/card@1
id: P-3WBSO
kind: problem
title: Dirichlet's theorem on primes in arithmetic progressions
classification:
  areas:
  - algebra
  topics:
  - Number Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
What is Dirichlet's theorem about primes in arithmetic progression?
What can you say about the density of such primes?
:::


::: {.solution}
Let $q\ge2$ and let $a$ be an integer with $\gcd(a,q)=1$.

<1>1. Dirichlet's theorem says that there are infinitely many primes $p$ satisfying
\[
p\equiv a\pmod q.
\]
::: {.proof}
This is Dirichlet's theorem on primes in arithmetic progressions: every reduced residue class modulo $q$ contains infinitely many primes. The coprimality condition is necessary, since if $\gcd(a,q)>1$, then all sufficiently large integers in the progression share a nontrivial divisor with $q$.
:::

<1>2. A stronger asymptotic theorem gives
\[
\pi(x;q,a)\sim \frac{\operatorname{Li}(x)}{\varphi(q)},
\]
where $\pi(x;q,a)$ counts primes $p\le x$ with $p\equiv a\pmod q$.
::: {.proof}
This is the prime-number theorem for arithmetic progressions. It refines Dirichlet's infinitude theorem by giving the asymptotic frequency of primes in each reduced residue class.
:::

<1>3. Consequently the primes are asymptotically equidistributed among the $\varphi(q)$ reduced residue classes modulo $q$.
::: {.proof}
The ordinary prime-number theorem gives
\[
\pi(x)\sim\operatorname{Li}(x).
\]
Therefore <1>2 implies
\[
\frac{\pi(x;q,a)}{\pi(x)}\longrightarrow\frac1{\varphi(q)}.
\]
Thus the relative natural density among all primes is $1/\varphi(q)$. The same value is also the Dirichlet density.
:::
:::
