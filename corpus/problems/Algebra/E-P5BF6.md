---
schema: qual/card@1
id: E-P5BF6
kind: problem
title: Nilpotents, units, and zero-divisors in $R[x]$
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Rings
  - Polynomials
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

:::{.exercise}
Assume throughout that $R$ is a commutative ring with identity. Let $N(R)$ be the set of nilpotent elements, $ZD(R)$ the set of zero divisors, and $R\units$ the group of units.

- Show that every nilpotent element is either zero or a zero divisor.

- Show that if $n\in N(R)$, then $1+n$ is a unit. Deduce that $N(R)+R\units=R\units$.

- For $f(x)=\sum_{k=0}^d a_kx^k\in R[x]$, show that $f\in R[x]\units$ iff $a_0\in R\units$ and $a_k\in N(R)$ for every $k\ge1$.

- Show that $f(x)\in N(R[x])$ iff $a_k\in N(R)$ for every $k$.

- Show that $f\in ZD(R[x])$ iff $f\neq0$ and $rf(x)=0$ for some $0\neq r\in R$.
:::

::: {.solution}
<1>1. Every nilpotent element is either zero or a zero divisor.
::: {.proof}
Let $a\in R$ be nilpotent and nonzero. Choose the least $m\ge1$ such that $a^m=0$. Since $a\neq0$, one has $m\ge2$, and minimality gives $a^{m-1}\neq0$. Thus
\[
a\,a^{m-1}=0
\]
with both factors nonzero, so $a$ is a zero divisor.
:::

<1>2. If $n\in N(R)$, then $1+n$ is a unit; consequently $N(R)+R\units=R\units$.
::: {.proof}
Choose $N$ with $n^N=0$. Then
\[
(1+n)\sum_{j=0}^{N-1}(-n)^j=1,
\]
so $1+n$ is a unit.

Now let $u\in R\units$ and $n\in N(R)$. Since $R$ is commutative, $u^{-1}n$ is nilpotent, and
\[
u+n=u(1+u^{-1}n)
\]
is a product of units. Thus $N(R)+R\units\subseteq R\units$. The reverse inclusion follows from $0\in N(R)$.
:::

<1>3. A polynomial $f(x)=\sum_{k=0}^d a_kx^k$ is a unit in $R[x]$ if and only if $a_0$ is a unit and every $a_k$ for $k\ge1$ is nilpotent.
::: {.proof}
Suppose first that $a_0\in R\units$ and every $a_k$ for $k\ge1$ is nilpotent. Put
\[
h(x)=\sum_{k=1}^d a_kx^k.
\]
Each summand $a_kx^k$ is nilpotent. A finite sum of nilpotent elements in a commutative ring is nilpotent: if $t_i^{e_i}=0$, then every monomial in $(t_1+\cdots+t_r)^{e_1+\cdots+e_r}$ contains some $t_i^{e_i}$ as a factor. Hence $h$ is nilpotent, and so is $a_0^{-1}h$. By <1>2,
\[
f=a_0(1+a_0^{-1}h)
\]
is a unit.

Conversely, suppose $fg=1$ in $R[x]$. Comparing constant terms gives $a_0b_0=1$, so $a_0$ is a unit. Let $\mathfrak p$ be any prime ideal of $R$. Reducing modulo $\mathfrak p$ gives a unit $\overline f$ in the domain polynomial ring $(R/\mathfrak p)[x]$. Its only units are nonzero constants, so $a_k\in\mathfrak p$ for every $k\ge1$. Since this holds for every prime ideal, each such $a_k$ lies in the nilradical and is nilpotent.
:::

<1>4. A polynomial is nilpotent if and only if all its coefficients are nilpotent.
::: {.proof}
If every coefficient $a_k$ is nilpotent, then each term $a_kx^k$ is nilpotent, so their finite sum $f$ is nilpotent by the argument in <1>3.

Conversely, suppose $f^N=0$. For every prime ideal $\mathfrak p\subset R$, reduction modulo $\mathfrak p$ gives
\[
\overline f^{\,N}=0
\]
in the domain $(R/\mathfrak p)[x]$. Hence $\overline f=0$, so every coefficient $a_k$ lies in every prime ideal. Thus every $a_k$ lies in the nilradical and is nilpotent.
:::

<1>5. A nonzero polynomial $f\in R[x]$ is a zero divisor if and only if some nonzero scalar $r\in R$ annihilates it.
::: {.proof}
If $0\neq r\in R$ and $rf=0$, then the nonzero constant polynomial $r$ annihilates the nonzero polynomial $f$, so $f$ is a zero divisor.

Conversely, suppose $f$ is a zero divisor. Choose a nonzero polynomial
\[
g=b_0+b_1x+\cdots+b_mx^m
\]
of minimal degree among all nonzero $g$ satisfying $fg=0$. Write
\[
f=a_0+a_1x+\cdots+a_nx^n.
\]
The coefficient of $x^{n+m}$ in $fg$ is $a_nb_m$, so $a_nb_m=0$. Hence either $a_ng=0$ or $\deg(a_ng)<m$. But
\[
f(a_ng)=a_n(fg)=0.
\]
Minimality of $m$ therefore forces $a_ng=0$.

Replacing $f$ by $f-a_nx^n$ and repeating the same argument gives, by descending induction,
\[
a_i g=0
\qquad\text{for every }i.
\]
Choose any nonzero coefficient $b_j$ of $g$. Then $b_ja_i=0$ for every $i$, so with $r=b_j\neq0$ one has $rf=0$.
:::
:::
