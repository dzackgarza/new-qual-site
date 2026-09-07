---
schema: qual/card@1
id: P-ALGF19F
kind: problem
title: Irreducible factors of $x^{p^\ell} - x$ over $\mathbb{F}_p$; count of degree $\ell$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 6 of the official UCSD Algebra Qualifying Exam, Fall 2019 source; all three finite-field assertions agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified factor degrees by the subfield degree tower, divisibility using the field F_p[x]/(f), and the count by squarefreeness and degree bookkeeping.
---

::: problem
Suppose $\ell$ and $p$ are prime and $\mathbb{F}_p$ is a finite field of order $p$.

(a) Prove that the degree of an irreducible factor of $x^{p^\ell} - x$ is either $1$ or $\ell$.

(b) Suppose $f(x) \in \mathbb{F}_p[x]$ is a monic irreducible polynomial of degree $\ell$.
Prove that $f(x) \mid (x^{p^\ell} - x)$.

(c) Prove that there are exactly $\dfrac{p^\ell - p}{\ell}$ many monic irreducible polynomials of degree $\ell$ in $\mathbb{F}_p[x]$.
:::

::: {.solution}
Set
\[
g(x)=x^{p^\ell}-x\in\mathbb F_p[x].
\]

<1>1. The roots of $g$ in an algebraic closure form a field with $p^\ell$ elements.
::: {.proof}
In characteristic $p$, the Frobenius map satisfies
\[
(u+v)^{p^\ell}=u^{p^\ell}+v^{p^\ell}.
\]
Hence the set
\[
K:=\{u\in\overline{\mathbb F}_p:u^{p^\ell}=u\}
\]
is closed under addition, subtraction, and multiplication. If $u\in K$ is nonzero, then
\[
(u^{-1})^{p^\ell}=(u^{p^\ell})^{-1}=u^{-1},
\]
so $K$ is a field.

Moreover,
\[
g'(x)=p^\ell x^{p^\ell-1}-1=-1.
\]
Thus $g$ has no repeated roots. Since $g$ splits in the algebraic closure and has degree $p^\ell$, it has exactly $p^\ell$ distinct roots. Therefore
\[
|K|=p^\ell,
\qquad
[K:\mathbb F_p]=\ell.
\]
:::

<1>2. Every irreducible factor of $g$ has degree $1$ or $\ell$.
::: {.proof}
Let $h(x)\in\mathbb F_p[x]$ be an irreducible factor of $g$, and let $\alpha$ be a root of $h$ in $\overline{\mathbb F}_p$. Since $h\mid g$,
\[
\alpha^{p^\ell}=\alpha,
\]
so $\alpha\in K$ by <1>1.

Because $h$ is the minimal polynomial of $\alpha$ over $\mathbb F_p$,
\[
\deg h=[\mathbb F_p(\alpha):\mathbb F_p].
\]
The tower
\[
\mathbb F_p\subseteq\mathbb F_p(\alpha)\subseteq K
\]
shows that $\deg h$ divides
\[
[K:\mathbb F_p]=\ell.
\]
Since $\ell$ is prime,
\[
\deg h\in\{1,\ell\}.
\]
This proves part (a).
:::

<1>3. Every monic irreducible polynomial of degree $\ell$ divides $g$.
::: {.proof}
Let $f(x)\in\mathbb F_p[x]$ be monic and irreducible of degree $\ell$, and put
\[
L=\mathbb F_p[x]/(f).
\]
Then $L$ is a field with
\[
|L|=p^\ell.
\]
If $u\in L$ is nonzero, Lagrange's theorem in the multiplicative group $L^\times$ gives
\[
u^{p^\ell-1}=1,
\]
hence $u^{p^\ell}=u$; the same equality is trivial for $u=0$.

Let $\alpha$ be the residue class of $x$ in $L$. Then
\[
\alpha^{p^\ell}-\alpha=0.
\]
Since $f$ is the minimal polynomial of $\alpha$ over $\mathbb F_p$, it follows that
\[
f(x)\mid x^{p^\ell}-x.
\]
This proves part (b).
:::

<1>4. The polynomial $g$ has exactly $p$ monic linear factors, each with multiplicity one.
::: {.proof}
Every $a\in\mathbb F_p$ satisfies $a^p=a$, and iterating Frobenius gives
\[
a^{p^\ell}=a.
\]
Thus each $x-a$ divides $g$. These are the $p$ monic linear polynomials over $\mathbb F_p$.

By <1>1, $g'(x)=-1$, so $g$ is squarefree. Hence each of these linear factors occurs exactly once.
:::

<1>5. There are exactly
\[
\frac{p^\ell-p}{\ell}
\]
monic irreducible polynomials of degree $\ell$ over $\mathbb F_p$.
::: {.proof}
By <1>2, every irreducible factor of $g$ has degree $1$ or $\ell$. By <1>3, every monic irreducible polynomial of degree $\ell$ occurs as a factor of $g$, and by squarefreeness it occurs once.

Let $N$ be the number of monic irreducible polynomials of degree $\ell$. Comparing degrees in the factorization of $g$ and using <1>4 gives
\[
p^\ell=p+N\ell.
\]
Therefore
\[
N=\frac{p^\ell-p}{\ell}.
\]
This proves part (c).
:::
:::
