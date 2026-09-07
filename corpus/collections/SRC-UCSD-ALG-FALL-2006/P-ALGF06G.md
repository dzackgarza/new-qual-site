---
schema: qual/card@1
id: P-ALGF06G
kind: problem
title: "Units, irreducibility, primality, and factorization in Z[sqrt(10)]"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Number Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 3.3 of the official UCSD Algebra Qualifying Examination, Fall 2006; all five parts and the norm hint agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the infinite unit family, irreducibility and nonprimality of 2, norm induction for atomicity, and the resulting failure of unique factorization. Part (d) is interpreted in the standard factorization sense for nonzero nonunits; literally including 0 would be false in this domain.
---

::: {.problem}
Let $R := \mathbb{Z}[\sqrt{10}] = \{a + b\sqrt{10} \mid a, b \in \mathbb{Z}\}$, viewed as a subring of the field of complex numbers with the usual operations.

(a) Show that the group of units $R^\times$ of $R$ is infinite.

(b) Show that the element $2$ is irreducible in $R$.

(c) Show that the element $2$ is not prime in $R$.

(d) Show that every element in $R$ can be written as a product of irreducible elements.

(e) Is $R$ a unique factorization domain?
Justify your answer.

Hint: Recall that there is a multiplicative norm map $N: \mathbb{Z}[\sqrt{10}] \to \mathbb{Z}$ given by $N(a + b\sqrt{10}) = a^2 - 10b^2$, for all $a, b \in \mathbb{Z}$.
:::

::: {.solution}
We use the multiplicative norm
\[
N(a+b\sqrt{10})=(a+b\sqrt{10})(a-b\sqrt{10})=a^2-10b^2.
\]
For a nonzero element of $R$, this norm is a nonzero integer.
Moreover, an element $u\in R$ is a unit if and only if $N(u)=\pm1$: necessity follows by taking norms in $uv=1$, while if $N(u)=\pm1$, then
\[
u^{-1}=\frac{\bar u}{N(u)}\in R.
\]

<1>1. The unit group $R^\times$ is infinite.
::: {.proof}
Set
\[
u:=3+\sqrt{10}.
\]
Then
\[
N(u)=9-10=-1,
\]
so $u$ is a unit; explicitly,
\[
(3+\sqrt{10})(\sqrt{10}-3)=1.
\]
Hence every power $u^k$, $k\ge0$, is a unit.
Under the real embedding $R\subset\mathbb R$, we have
\[
u=3+\sqrt{10}>1,
\]
so the positive real numbers $u^k$ are pairwise distinct.
Thus $R^\times$ contains infinitely many elements.
:::

<1>2. The element $2$ is irreducible in $R$.
::: {.proof}
Suppose
\[
2=\alpha\beta
\]
with nonzero $\alpha,\beta\in R$.
Taking norms gives
\[
4=N(2)=N(\alpha)N(\beta).
\]
If neither factor were a unit, then
\[
|N(\alpha)|\ge2,
\qquad
|N(\beta)|\ge2,
\]
so necessarily
\[
|N(\alpha)|=|N(\beta)|=2.
\]
Thus some integers $a,b$ would satisfy
\[
a^2-10b^2=2
\]
or
\[
a^2-10b^2=-2.
\]
Reducing modulo $5$ would give
\[
a^2\equiv2\pmod5
\]
or
\[
a^2\equiv3\pmod5.
\]
But the quadratic residues modulo $5$ are only $0,1,4$.
Hence no element of $R$ has norm $\pm2$.
Therefore in every factorization $2=\alpha\beta$, one factor is a unit, so $2$ is irreducible.
:::

<1>3. The irreducible element $2$ is not prime.
::: {.proof}
We have
\[
2\mid10=(\sqrt{10})(\sqrt{10}),
\]
because $10=2\cdot5$ in $R$.
However,
\[
2\nmid\sqrt{10}.
\]
Indeed, if
\[
\sqrt{10}=2(a+b\sqrt{10})
\]
for integers $a,b$, comparison of the coefficients of $1$ and $\sqrt{10}$ would give
\[
2a=0,
\qquad
2b=1,
\]
which is impossible.
Thus $2$ divides a product without dividing either factor, so $2$ is not prime.
:::

<1>4. Every nonzero nonunit of $R$ is a finite product of irreducibles.
::: {.proof}
We induct on the positive integer
\[
|N(\alpha)|
\]
for a nonzero nonunit $\alpha$.
Since $\alpha$ is not a unit, $|N(\alpha)|\ge2$.

If $\alpha$ is irreducible, there is nothing to prove.
Otherwise
\[
\alpha=\beta\gamma
\]
with nonunits $\beta$ and $\gamma$.
Then
\[
|N(\alpha)|=|N(\beta)|\,|N(\gamma)|,
\]
and both factors on the right are at least $2$.
Consequently
\[
2\le |N(\beta)|<|N(\alpha)|,
\qquad
2\le |N(\gamma)|<|N(\alpha)|.
\]
By induction, both $\beta$ and $\gamma$ are finite products of irreducibles, and hence so is $\alpha$.

Thus $R$ is atomic. As usual, the assertion concerns nonzero nonunits; units are accounted for by a unit factor, while $0$ cannot be a finite product of irreducibles in this domain.
:::

<1>5. The ring $R$ is not a unique factorization domain.
::: {.proof}
In a unique factorization domain every irreducible element is prime.
Indeed, if an irreducible $p$ divides $ab$, write $ab=pc$ and compare irreducible factorizations of both sides; uniqueness forces $p$ to be associate to an irreducible factor of $a$ or of $b$, so $p$ divides $a$ or $b$.

By <1>2, the element $2$ is irreducible in $R$, while by <1>3 it is not prime.
Therefore $R$ cannot be a unique factorization domain.
:::
:::
