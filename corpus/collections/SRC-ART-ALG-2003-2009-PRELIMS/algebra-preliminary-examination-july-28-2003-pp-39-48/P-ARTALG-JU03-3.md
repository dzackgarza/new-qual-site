---
schema: qual/card@1
id: P-ARTALG-JU03-3
kind: problem
title: No GCD in polynomial ring and subring of Euclidean domain
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
(a) Let $R$ be the ring of all polynomials in $\mathbb{Q}[x]$ having no $x$-term.
Show that $x^5$ and $x^6$ have no GCD in $R$.

(b) If $S$ is a Euclidean domain and $T$ is a subring of $S$, is it true that $T$ is a Euclidean domain?
Justify your answer.
:::

::: {.solution}
Let $R=\{f\in\QQ[x]: \text{the coefficient of } x \text{ in } f \text{ is } 0\}$.
It is a subring of $\QQ[x]$: for $f=\sum f_ix^i$ and $g=\sum g_ix^i$, the coefficient of $x$ in $fg$ is $f_0g_1+f_1g_0=0$.
Its units are the nonzero constants, since these are the units of $\QQ[x]$ and they lie in $R$.

<1>1. For $n\ge0$, an element $d\in R$ divides $x^n$ in $R$ if and only if $d=cx^k$ with $c\in\QQ^\times$, $0\le k\le n$, $k\ne1$, and $n-k\ne1$.

::: {.proof}
If $de=x^n$ with $d,e\in R$, unique factorization in $\QQ[x]$ gives $d=cx^k$ and $e=c^{-1}x^{n-k}$ with $c\in\QQ^\times$ and $0\le k\le n$.
A monomial $x^j$ lies in $R$ exactly when $j\ne1$, so $d,e\in R$ forces $k\ne1$ and $n-k\ne1$.
Conversely, under these conditions $e=c^{-1}x^{n-k}\in R$ and $de=x^n$.
:::

<1>2. The common divisors of $x^5$ and $x^6$ in $R$ are the elements $cx^k$ with $c\in\QQ^\times$ and $k\in\{0,2,3\}$.

::: {.proof}
By step <1>1, the divisors of $x^5$ are the $cx^k$ with $k\in\{0,2,3,5\}$, and the divisors of $x^6$ are the $cx^k$ with $k\in\{0,2,3,4,6\}$.
The common exponents are $0,2,3$.
:::

<1>3. For part (a), $x^5$ and $x^6$ have no greatest common divisor in $R$.

::: {.proof}
A greatest common divisor $g$ would be a common divisor divisible in $R$ by every common divisor, in particular by $x^2$ and by $x^3$.
By step <1>2, $g=cx^k$ with $k\in\{0,2,3\}$, and $x^3\mid g$ forces $k=3$.
Then $x^2\mid cx^3$ in $R$ would give $cx^3=x^2e$ with $e\in R$, so $e=cx\notin R$.
This contradiction shows that no such $g$ exists.
:::

<1>4. For part (b), the answer is no: $T=R$ is a subring of the Euclidean domain $S=\QQ[x]$ that is not a Euclidean domain.

::: {.proof}
The ring $\QQ[x]$ is Euclidean with the degree function.
A Euclidean domain is a principal ideal domain [@DF04].
In a principal ideal domain, a generator $d$ of the ideal $(a,b)$ is a greatest common divisor of $a$ and $b$: it divides $a$ and $b$, and writing $d=ua+vb$ shows that every common divisor of $a$ and $b$ divides $d$.
By step <1>3, $x^5$ and $x^6$ have no greatest common divisor in $R$, so $R$ is not a principal ideal domain and hence not Euclidean.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>3 answers part (a) and step <1>4 answers part (b).
:::
:::
