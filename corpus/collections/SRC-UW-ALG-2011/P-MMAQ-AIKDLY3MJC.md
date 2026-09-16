---
schema: qual/card@1
id: P-MMAQ-AIKDLY3MJC
kind: problem
title: The nilradical is the intersection of all primes; $N(\mathbb{Z}/(m))$ and $N(\mathbb{C}[x,y]/(y^2-x^3))$
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Commutative Algebra
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $R$ be a commutative ring.
Recall that an element $r$ of $R$ is `\textit{nilpotent}`{=tex} if $r^n=0$ for some positive integer $n$ and that the `\textit{nilradical}`{=tex} of $R$ is the set $N(R)$ of nilpotent elements.

- Prove that
  \[
  N(R)=\bigcap_{P\text{ prime}}P.
  \]

  > Hint: given a non-nilpotent element $r$ of $R$, you may wish to construct a prime ideal that does not contain $r$ or its powers.

- Given a positive integer $m$, determine the nilradical of $\mathbb Z/(m)$.

- Determine the nilradical of $\mathbb C[x,y]/(y^2-x^3)$.

- Let $p(x,y)$ be a polynomial in $\mathbb C[x,y]$ such that for any complex number $a$, $p(a,a^{3/2})=0$.
  Prove that $p(x,y)$ is divisible by $y^2-x^3$.
:::


::: {.solution}
<1>1. For every commutative ring $R$,
\[
N(R)=\bigcap_{P\text{ prime}}P.
\]
::: {.proof}
If $r\in N(R)$, then $r^n=0$ for some $n$. Every prime ideal contains $0$, and if $r^n\in P$ with $P$ prime, repeated use of primality gives $r\in P$. Hence
\[
N(R)\subseteq\bigcap_P P.
\]

Conversely, suppose $r$ is not nilpotent. Let
\[
S=\{1,r,r^2,r^3,\ldots\}.
\]
Then $0\notin S$. Consider the set of ideals of $R$ disjoint from $S$, ordered by inclusion. Every chain has an upper bound given by its union, still disjoint from $S$, so Zorn's lemma gives a maximal such ideal $P$.

We claim $P$ is prime. Suppose $ab\in P$ but $a,b\notin P$. By maximality, both $P+(a)$ and $P+(b)$ meet $S$. Thus for some $m,n\ge0$,
\[
r^m=p_1+xa,\qquad r^n=p_2+yb
\]
with $p_1,p_2\in P$ and $x,y\in R$. Multiplying,
\[
r^{m+n}=p_1p_2+p_1yb+p_2xa+xyab\in P,
\]
contradicting $P\cap S=\varnothing$. Thus $P$ is prime and $r\notin P$. Hence any element lying in every prime ideal must be nilpotent.
:::

<1>2. If
\[
m=\prod_{i=1}^s p_i^{e_i}
\]
is the prime factorization of $m$, then
\[
N(\mathbb Z/(m))
=\bigl(\overline{p_1p_2\cdots p_s}\bigr).
\]
::: {.proof}
Write
\[
\operatorname{rad}(m)=p_1\cdots p_s.
\]
If $\bar a\in\mathbb Z/(m)$ is nilpotent, then $m\mid a^N$ for some $N$. Hence every prime divisor $p_i$ of $m$ divides $a^N$, and therefore divides $a$. Thus $\operatorname{rad}(m)\mid a$.

Conversely, if every $p_i$ divides $a$, choose $N\ge\max_i e_i$. Then
\[
p_i^{e_i}\mid a^N
\]
for every $i$, so $m\mid a^N$. Hence $\bar a$ is nilpotent. Therefore the nilpotent classes are exactly the multiples of $\operatorname{rad}(m)$ modulo $m$.
:::

<1>3. One has
\[
N\bigl(\mathbb C[x,y]/(y^2-x^3)\bigr)=0.
\]
::: {.proof}
The polynomial $y^2-x^3$ is irreducible in $\mathbb C[x,y]$. Indeed, regarding it as a monic quadratic in $y$ over the UFD $\mathbb C[x]$, reducibility would force $x^3$ to be a square in $\mathbb C[x]$, which it is not. Since $\mathbb C[x,y]$ is a UFD, irreducible elements are prime. Hence $(y^2-x^3)$ is a prime ideal, so the quotient is an integral domain. An integral domain has no nonzero nilpotent elements.
:::

<1>4. Let
\[
\phi:\mathbb C[x,y]\longrightarrow\mathbb C[t],
\qquad
\phi(x)=t^2,\quad \phi(y)=t^3.
\]
Then
\[
\ker\phi=(y^2-x^3).
\]
::: {.proof}
Certainly $y^2-x^3\in\ker\phi$. Conversely, divide any $p(x,y)\in\mathbb C[x,y]$ by the monic polynomial $y^2-x^3$ as a polynomial in $y$ over $\mathbb C[x]$. There are unique $q\in\mathbb C[x,y]$ and $a,b\in\mathbb C[x]$ such that
\[
p=q(y^2-x^3)+a(x)+y b(x).
\]
If $p\in\ker\phi$, then
\[
0=a(t^2)+t^3 b(t^2).
\]
The first summand contains only even powers of $t$, while the second contains only odd powers $t^{2j+3}$. Hence both summands vanish separately. Thus $a=0$ and $b=0$, so $p\in(y^2-x^3)$.
:::

<1>5. If $p(a,a^{3/2})=0$ for every complex $a$ in the sense of the cusp parametrization, then $y^2-x^3$ divides $p(x,y)$.
::: {.proof}
Take an arbitrary $t\in\mathbb C$ and set $a=t^2$, choosing the square root $t$, so that $a^{3/2}=t^3$. The hypothesis gives
\[
p(t^2,t^3)=0
\]
for every $t\in\mathbb C$. Hence the polynomial $\phi(p)\in\mathbb C[t]$ has infinitely many roots, so $\phi(p)=0$. By <1>4,
\[
p\in\ker\phi=(y^2-x^3).
\]
Therefore $y^2-x^3$ divides $p$.
:::
:::
