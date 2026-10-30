---
schema: qual/card@1
id: P-ARTALG-JU03-3
kind: problem
title: No GCD in polynomial ring and subring of Euclidean domain
classification:
  areas:
  - algebra
  topics:
  - Euclidean Domains
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---
::: {.problem}
(a) Let $R$ be the ring of all polynomials in $\QQ[x]$ having no $x$-term.
Show that $x^5$ and $x^6$ have no GCD in $R$.

(b) If $S$ is a Euclidean domain and $T$ is a subring of $S$, is it true that $T$ is a Euclidean domain?
Justify your answer.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The ring $R$ is exactly
$$
\QQ[x^2,x^3].
$$

::: pf-proof

A polynomial in $\QQ[x^2,x^3]$ is a $\QQ$-linear combination of monomials
$$
x^{2a+3b},
\qquad a,b\ge0.
$$
The attainable exponents are $0$ and every integer at least $2$, so such a polynomial has no $x$-term. Conversely, every monomial $x^n$ with $n\ge2$ lies in $\QQ[x^2,x^3]$: if $n$ is even, $x^n=(x^2)^{n/2}$; if $n\ge3$ is odd, $x^n=x^3(x^2)^{(n-3)/2}$. Hence every polynomial with zero $x$-coefficient lies in $\QQ[x^2,x^3]$.

:::

:::

::: {.pf-step #s2}

Both $x^2$ and $x^3$ are common divisors of $x^5$ and $x^6$ in $R$.

::: pf-proof

One has
$$
x^5=x^2x^3=x^3x^2,
$$
and
$$
x^6=x^2x^4=x^3x^3.
$$
All quotients $x^2,x^3,x^4$ belong to $R$ by step [](#s1){.pf-ref}. Thus both $x^2$ and $x^3$ divide both $x^5$ and $x^6$ in $R$.

:::

:::

::: {.pf-step #s3}

No common divisor of $x^5$ and $x^6$ in $R$ can be divisible by both $x^2$ and $x^3$.

::: pf-proof

Suppose $d\in R$ is a common divisor and
$$
x^2\mid d,
\qquad
x^3\mid d.
$$
Since $d\mid x^5$ in $R$, there is $u\in R$ with
$$
x^5=du.
$$
In the UFD $\QQ[x]$, every divisor of $x^5$ is an associate of $x^k$ for some $0\le k\le5$. Because $x^3\mid d$, one has $k\ge3$.

If $k=3$, then $x^2\mid d$ in $R$ would require the quotient $x$, which is not in $R$. If $k=4$, then $d\mid x^5$ in $R$ would require the quotient $x$, again impossible. If $k=5$, then $d\mid x^6$ in $R$ would require the quotient $x$, impossible. Thus no such $d$ exists.

:::

:::

::: {.pf-step #s4}

Therefore $x^5$ and $x^6$ have no gcd in $R$.

::: pf-proof

A greatest common divisor would be a common divisor divisible by every other common divisor. By step [](#s2){.pf-ref} it would therefore have to be divisible by both $x^2$ and $x^3$, contradicting step [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

A subring of a Euclidean domain need not be Euclidean.

::: pf-proof

Take
$$
S=\QQ[x]
$$
and
$$
T=\QQ[x^2,x^3]=R.
$$
The polynomial ring $\QQ[x]$ is Euclidean with the degree function. By step [](#s4){.pf-ref}, the elements $x^5,x^6\in T$ have no greatest common divisor in $T$.

Every Euclidean domain is a PID, and in a PID any two elements have a gcd: a generator of the ideal $(a,b)$ is a gcd of $a$ and $b$. Hence $T$ cannot be Euclidean.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves part (a), and step [](#s5){.pf-ref} provides the required counterexample for part (b).

:::

:::

:::
