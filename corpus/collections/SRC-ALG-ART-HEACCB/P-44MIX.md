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
- event: source-checked
  by: OpenAI
  date: 2026-09-09
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
<1>1. The answer depends on the field $k$.
Set
\[
p=x-1,\qquad q=x+2,\qquad c=x^2+1.
\]
The exceptional characteristics are $2,3,5$.
::: {.proof}
One has $p=q$ exactly in characteristic $3$.
Also $p\mid c$ exactly when $c(1)=2=0$, i.e. in characteristic $2$, and $q\mid c$ exactly when $c(-2)=5=0$, i.e. in characteristic $5$.
Thus outside characteristics $2,3,5$, the polynomials $p,q,c$ are pairwise coprime, although $c$ itself may split into two irreducible linear factors.
:::

<1>2. Suppose first that $\operatorname{char}k\notin\{2,3,5\}$.
Let
\[
c=\prod_{r\in\mathcal R}r
\]
be the factorization of $c$ into distinct monic irreducibles in $k[x]$.
Then the elementary divisors are
\[
p^3,\ p,\ q,
\qquad
r^2,r^2,r^4\quad(r\in\mathcal R).
\]
::: {.proof}
The four cyclic summands contribute respectively
\[
p^3,\qquad c^2,\qquad pc^4,\qquad qc^2.
\]
Since $p,q$, and the irreducible factors $r$ of $c$ are pairwise coprime, the Chinese remainder theorem splits each cyclic summand into its prime-power parts, giving exactly the displayed list.
:::

<1>3. In the same generic case, the invariant factors are
\[
d_1=c^2,\qquad d_2=pc^2,\qquad d_3=p^3qc^4.
\]
::: {.proof}
For the prime $p$, the nonzero elementary-divisor exponents are $1,3$, so after padding to three slots they are $0,1,3$.
For $q$ they are $0,0,1$.
For every irreducible factor $r$ of $c$, they are $2,2,4$.
Multiplying the prime powers slotwise gives the displayed invariant factors, and clearly $d_1\mid d_2\mid d_3$.
:::

<1>4. Suppose $\operatorname{char}k=3$. Then $p=q$, and the elementary divisors are
\[
p^3,p,p,
\qquad
r^2,r^2,r^4\quad(r\mid c\text{ irreducible}).
\]
The invariant factors are
\[
pc^2,\qquad pc^2,\qquad p^3c^4.
\]
::: {.proof}
In characteristic $3$, $c(1)=2\ne0$, so $p$ is coprime to $c$.
The $p$-exponents are $1,1,3$, while each irreducible factor of $c$ has exponents $2,2,4$.
Aligning these exponent lists gives the stated invariant factors.
:::

<1>5. Suppose $\operatorname{char}k=5$. Put $r=x-2$. Then
\[
c=(x+2)(x-2)=qr.
\]
The elementary divisors are
\[
p^3,p,\qquad q^2,q^3,q^4,\qquad r^2,r^2,r^4,
\]
and the invariant factors are
\[
c^2,\qquad pqc^2,\qquad p^3c^4.
\]
::: {.proof}
The four original summands contribute
\[
p^3,\qquad q^2r^2,\qquad pq^4r^4,\qquad q^3r^2.
\]
Thus the exponent lists are $p:(1,3)$, $q:(2,3,4)$, and $r:(2,2,4)$. Padding and multiplying slotwise yields the displayed invariant factors.
:::

<1>6. Suppose $\operatorname{char}k=2$. Then
\[
c=x^2+1=(x+1)^2=p^2,
\qquad q=x.
\]
The elementary divisors are
\[
p^3,p^4,p^4,p^9,q,
\]
and the invariant factors are
\[
p^3,\qquad p^4,\qquad p^4,\qquad p^9q.
\]
::: {.proof}
The four summands become
\[
R/(p^3),\qquad R/(p^4),\qquad R/(p^9),\qquad R/(qp^4).
\]
Since $p$ and $q$ are coprime, the last summand splits into $R/(q)\oplus R/(p^4)$. Hence the $p$-exponents are $3,4,4,9$ and the single $q$-exponent is $1$. Padding the $q$-list with three zeros gives the stated invariant factors.
:::

<1>7. These cases exhaust all fields $k$.
::: {.proof}
By <1>1, the only possible collisions among $p$, $q$, and the factors of $c$ occur in characteristics $2,3,5$. Outside those characteristics, <1>2--<1>3 apply regardless of whether $c$ is irreducible or splits.
:::
:::
