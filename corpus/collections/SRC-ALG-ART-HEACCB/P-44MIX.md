---
schema: qual/card@1
id: P-44MIX
kind: problem
title: Elementary divisors and invariant factors of a given $k[x]$-module
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Modules
  - Canonical Forms
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
Let $R = k[x]$ for $k$ a field and let $M$ be the $R\dash$module given by
\[
M=\frac{k[x]}{(x-1)^{3}} \oplus \frac{k[x]}{\left(x^{2}+1\right)^{2}} \oplus \frac{k[x]}{(x-1)\left(x^{2}+1\right)^{4}} \oplus \frac{k[x]}{(x+2)\left(x^{2}+1\right)^{2}}
.\]
Describe the elementary divisors and invariant factors of $M$.
:::


::: {.solution}
Put \(q=x^2+1\). The answer depends on the field \(k\), because \(q\) need not be irreducible and in characteristics \(2,3,5\) some of the displayed factors coincide.

<1>1. Assume first that \(\operatorname{char}k\notin\{2,3,5\}\). Factor \(q=\pi_1\cdots\pi_r\) into distinct monic irreducibles in \(k[x]\), where \(r=1\) or \(2\). The elementary divisors are
\[
(x-1)^3,\quad x-1,\quad x+2,
\]
and, for each \(j=1,\dots,r\),
\[
\pi_j^2,\quad \pi_j^2,\quad \pi_j^4.
\]
::: {.proof}
In these characteristics, \(x-1\), \(x+2\), and \(q\) are pairwise coprime, and \(q\) is squarefree. Apply the Chinese remainder theorem separately to each cyclic summand. The two summands containing \(x-1\) contribute \((x-1)^3\) and \(x-1\); the last summand contributes \(x+2\); and the three summands containing \(q\) contribute exponents \(2,4,2\) for every irreducible factor of \(q\).
:::

<1>2. Under the same characteristic assumption, the invariant factors are
\[
q^2,\qquad (x-1)q^2,\qquad (x-1)^3(x+2)q^4.
\]
::: {.proof}
For each irreducible prime, arrange the exponents in nondecreasing order and pad on the left with zeros. For \(x-1\) the exponents are \(0,1,3\); for each irreducible factor of \(q\) they are \(2,2,4\); and for \(x+2\) they are \(0,0,1\). Multiplying the corresponding prime powers columnwise gives the three displayed invariant factors, each dividing the next.
:::

<1>3. If \(\operatorname{char}k=3\), then \(x+2=x-1\). The elementary divisors are
\[
(x-1)^3,\quad x-1,\quad x-1,
\]
together with, for each irreducible factor \(\pi\) of \(q\),
\[
\pi^2,\quad\pi^2,\quad\pi^4.
\]
The invariant factors are
\[
(x-1)q^2,\qquad (x-1)q^2,\qquad (x-1)^3q^4.
\]
::: {.proof}
Here \(q(1)=2\neq0\), so \(q\) remains coprime to \(x-1\). The \(x-1\)-primary exponents are \(1,1,3\), while the \(q\)-primary exponents are \(2,2,4\). Aligning them gives the stated invariant factors.
:::

<1>4. If \(\operatorname{char}k=5\), write \(q=(x+2)(x-2)\). The elementary divisors are
\[
(x-1)^3,\quad x-1,\quad (x+2)^2,\quad (x+2)^3,\quad (x+2)^4,\quad (x-2)^2,\quad (x-2)^2,\quad (x-2)^4,
\]
and the invariant factors are
\[
q^2,\qquad (x-1)(x+2)q^2,\qquad (x-1)^3q^4.
\]
::: {.proof}
The exponent multisets for the primes \(x-1\), \(x+2\), and \(x-2\) are respectively
\[
\{1,3\},\qquad\{2,3,4\},\qquad\{2,2,4\}.
\]
Pad the first list with a zero, sort all three lists increasingly, and multiply the aligned prime powers.
:::

<1>5. If \(\operatorname{char}k=2\), then
\[
q=(x+1)^2,\qquad x-1=x+1,\qquad x+2=x.
\]
The elementary divisors are
\[
(x+1)^3,\quad (x+1)^4,\quad (x+1)^4,\quad (x+1)^9,\quad x,
\]
and the invariant factors are
\[
(x+1)^3,\qquad (x+1)^4,\qquad (x+1)^4,\qquad x(x+1)^9.
\]
::: {.proof}
The four cyclic summands have \((x+1)\)-primary exponents \(3,4,9,4\), while only the last summand has an additional coprime factor \(x\). Sorting the \((x+1)\)-exponents gives \(3,4,4,9\), and the lone \(x\)-factor is placed in the last invariant factor.
:::

<1>6. These cases exhaust all fields \(k\).
::: {.proof}
The only possible collisions among the displayed factors occur when \(2=0\), \(3=0\), or \(5=0\): \(q\) is inseparable only in characteristic \(2\), \(x-1=x+2\) only in characteristic \(3\), and \(x+2\mid q\) only in characteristic \(5\).
:::
:::
