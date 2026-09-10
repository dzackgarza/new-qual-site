---
schema: qual/card@1
id: P-T3YQ4
kind: problem
title: Nilradical and infinitely many primes in $F[x]$
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Prime Ideals
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
(1) Define the **nilradical** $\operatorname{Nil}(R)$ of a commutative ring $R$, and state the characterization theorem relating it to the intersection of all prime ideals of $R$.
(2) Prove that the polynomial ring $F[x]$ over a field $F$ contains **infinitely many prime ideals**.
:::

::: solution
The nilradical is
\[
\operatorname{Nil}(R)=\sqrt{(0)}
=\{a\in R: a^m=0\text{ for some }m\ge1\}.
\]
The standard characterization is
\[
\boxed{\operatorname{Nil}(R)=\bigcap_{\mathfrak p\in\operatorname{Spec}R}\mathfrak p.}
\]
In particular, because $F[x]$ is a domain,
\[
\operatorname{Nil}(F[x])=(0).
\]

To prove that $F[x]$ has infinitely many prime ideals, suppose instead that its nonzero prime ideals are
\[
(p_1),\dots,(p_m),
\]
where each $p_i$ is irreducible. Set
\[
h=p_1\cdots p_m+1.
\]
Then $h$ is nonconstant, so it has an irreducible divisor $q\in F[x]$. Hence $(q)$ is a nonzero prime ideal. By the assumed list, $q$ is associate to some $p_j$. But then $p_j$ divides both $p_1\cdots p_m$ and $h$, hence divides
\[
h-p_1\cdots p_m=1,
\]
a contradiction.

Therefore $F[x]$ has infinitely many nonzero prime ideals, and hence infinitely many prime ideals.

The nilradical theorem is compatible with this conclusion, but it does not by itself force infinitude here: $(0)$ is already a prime ideal of the domain $F[x]$, so the intersection of any family of primes containing $(0)$ is automatically $(0)$.
:::
