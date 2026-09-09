---
schema: qual/card@1
id: P-ALGS06E
kind: problem
title: "Localization of Z[X]/(f) at non-zero divisors is a direct sum of fields"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
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
Let $f \in \mathbb{Z}[X] \setminus \mathbb{Z}$ such that $\gcd(f, f') = 1$.
Let $S$ be the set of non-zero divisors in the quotient ring $\mathbb{Z}[X]/(f)$.

(a) Show that the ring $S^{-1}(\mathbb{Z}[X]/(f))$ is isomorphic to a direct sum of fields.

(b) Specify the fields in (a) above if $f = X^5 - 1$.

(c) Is the hypothesis $\gcd(f, f') = 1$ necessary in order for the conclusion in (a) above to hold true?
Justify.
:::

::: {.solution}
<1>1. The hypothesis $\gcd(f,f')=1$ implies that $f$ is primitive and squarefree over $\mathbb Q$.
::: {.proof}
If the content of $f$ had a nonunit divisor $d\in\mathbb Z$, then $d$ would divide every coefficient of both $f$ and $f'$, contradicting $\gcd(f,f')=1$. Thus $f$ is primitive.

A polynomial over a field has a repeated irreducible factor exactly when it has a nonconstant common divisor with its derivative. Hence the image of $f$ in $\mathbb Q[X]$ is squarefree.
:::

<1>2. Write the factorization over $\mathbb Q$ as
\[
f=c f_1\cdots f_r,
\]
where $c\in\mathbb Q^\times$ and the $f_i\in\mathbb Q[X]$ are distinct monic irreducibles. Then
\[
\mathbb Q[X]/(f)\cong\prod_{i=1}^r K_i,
\qquad
K_i:=\mathbb Q[X]/(f_i).
\]
::: {.proof}
The ideals $(f_i)$ are pairwise comaximal in the PID $\mathbb Q[X]$. The Chinese remainder theorem therefore gives
\[
\mathbb Q[X]/(f)
\cong
\prod_{i=1}^r\mathbb Q[X]/(f_i).
\]
Each quotient is a field because $f_i$ is irreducible.
:::

<1>3. Every nonzero integer is a non-zero divisor in
\[
R:=\mathbb Z[X]/(f).
\]
::: {.proof}
Suppose $0\ne n\in\mathbb Z$ and $ng\in(f)$ in $\mathbb Z[X]$. Then $f$ divides $ng$ in $\mathbb Q[X]$, hence divides $g$ there because $n$ is a unit in $\mathbb Q[X]$. Since $f$ is primitive by <1>1, Gauss's lemma implies that $f$ divides $g$ in $\mathbb Z[X]$. Thus the class of $g$ in $R$ is zero.
:::

<1>4. Localizing $R$ at the nonzero integers gives
\[
(\mathbb Z\setminus\{0\})^{-1}R
\cong
\mathbb Q[X]/(f).
\]
::: {.proof}
Localization commutes with quotient, so
\[
(\mathbb Z\setminus\{0\})^{-1}(\mathbb Z[X]/(f))
\cong
\mathbb Q[X]/(f).
\]
By <1>3, this localization inverts only non-zero divisors.
:::

<1>5. The total quotient ring $S^{-1}R$ is isomorphic to the product of fields in <1>2.
::: {.proof}
Because the nonzero integers lie in $S$, the map $R\to S^{-1}R$ factors through the ring in <1>4. Under the decomposition
\[
\mathbb Q[X]/(f)\cong\prod_i K_i,
\]
a non-zero divisor is exactly a tuple with every coordinate nonzero, and such a tuple is already a unit. Therefore localizing further at the images of elements of $S$ changes nothing. Hence
\[
S^{-1}R
\cong
\mathbb Q[X]/(f)
\cong
\prod_{i=1}^rK_i.
\]
This proves part (a).
:::

<1>6. If $f=X^5-1$, then
\[
S^{-1}(\mathbb Z[X]/(X^5-1))
\cong
\mathbb Q\times\mathbb Q(\zeta_5).
\]
::: {.proof}
Over $\mathbb Q$,
\[
X^5-1=(X-1)\Phi_5(X),
\qquad
\Phi_5(X)=X^4+X^3+X^2+X+1.
\]
The fifth cyclotomic polynomial $\Phi_5$ is irreducible over $\mathbb Q$. Therefore <1>2 gives
\[
\mathbb Q[X]/(X^5-1)
\cong
\mathbb Q[X]/(X-1)\times\mathbb Q[X]/(\Phi_5)
\cong
\mathbb Q\times\mathbb Q(\zeta_5).
\]
This proves part (b).
:::

<1>7. The hypothesis $\gcd(f,f')=1$ is not necessary for the conclusion in part (a).
::: {.proof}
Take
\[
f=2X.
\]
Then $f'=2$, so $\gcd(f,f')=2\ne1$. Nevertheless
\[
R=\mathbb Z[X]/(2X)
\]
is reduced because
\[
(2X)=(2)\cap(X)
\]
in $\mathbb Z[X]$, an intersection of prime ideals. A reduced Noetherian ring with minimal primes $\mathfrak p_1,\dots,\mathfrak p_s$ has total quotient ring equal to the product of the fraction fields of the domains $R/\mathfrak p_i$. Here the two minimal primes are the images of $(2)$ and $(X)$, so
\[
S^{-1}R
\cong
\operatorname{Frac}(R/(2))\times\operatorname{Frac}(R/(X))
\cong
\mathbb F_2(X)\times\mathbb Q,
\]
a product of fields. Thus the stated gcd hypothesis is sufficient but not necessary.
:::
:::
