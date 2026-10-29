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

::: {.problem}
Let $f \in \ZZ[X] \setminus \ZZ$ such that $\gcd(f, f') = 1$.
Let $S$ be the set of non-zero divisors in the quotient ring $\ZZ[X]/(f)$.

(a) Show that the ring $S^{-1}(\ZZ[X]/(f))$ is isomorphic to a direct sum of fields.

(b) Specify the fields in (a) above if $f = X^5 - 1$.

(c) Is the hypothesis $\gcd(f, f') = 1$ necessary in order for the conclusion in (a) above to hold true?
Justify.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The hypothesis $\gcd(f,f')=1$ implies that $f$ is primitive and squarefree over $\QQ$.

::: pf-proof

If the content of $f$ had a nonunit divisor $d\in\ZZ$, then $d$ would divide every coefficient of both $f$ and $f'$, contradicting $\gcd(f,f')=1$. Thus $f$ is primitive.

A polynomial over a field has a repeated irreducible factor exactly when it has a nonconstant common divisor with its derivative. Hence the image of $f$ in $\QQ[X]$ is squarefree.

:::

:::

::: {.pf-step #s2}

Write the factorization over $\QQ$ as
\[
f=c f_1\cdots f_r,
\]
where $c\in\QQ^\times$ and the $f_i\in\QQ[X]$ are distinct monic irreducibles. Then
\[
\QQ[X]/(f)\cong\prod_{i=1}^r K_i,
\qquad
K_i:=\QQ[X]/(f_i).
\]

::: pf-proof

The ideals $(f_i)$ are pairwise comaximal in the PID $\QQ[X]$. The Chinese remainder theorem therefore gives
\[
\QQ[X]/(f)
\cong
\prod_{i=1}^r\QQ[X]/(f_i).
\]
Each quotient is a field because $f_i$ is irreducible.

:::

:::

::: {.pf-step #s3}

Every nonzero integer is a non-zero divisor in
\[
R:=\ZZ[X]/(f).
\]

::: pf-proof

Suppose $0\ne n\in\ZZ$ and $ng\in(f)$ in $\ZZ[X]$. Then $f$ divides $ng$ in $\QQ[X]$, hence divides $g$ there because $n$ is a unit in $\QQ[X]$. Since $f$ is primitive by step [](#s1){.pf-ref}, Gauss's lemma implies that $f$ divides $g$ in $\ZZ[X]$. Thus the class of $g$ in $R$ is zero.

:::

:::

::: {.pf-step #s4}

Localizing $R$ at the nonzero integers gives
\[
(\ZZ\setminus\{0\})^{-1}R
\cong
\QQ[X]/(f).
\]

::: pf-proof

Localization commutes with quotient, so
\[
(\ZZ\setminus\{0\})^{-1}(\ZZ[X]/(f))
\cong
\QQ[X]/(f).
\]
By step [](#s3){.pf-ref}, this localization inverts only non-zero divisors.

:::

:::

::: pf-step

The total quotient ring $S^{-1}R$ is isomorphic to the product of fields in step [](#s2){.pf-ref}.

::: pf-proof

Because the nonzero integers lie in $S$, the map $R\to S^{-1}R$ factors through the ring in step [](#s4){.pf-ref}. Under the decomposition
\[
\QQ[X]/(f)\cong\prod_i K_i,
\]
a non-zero divisor is exactly a tuple with every coordinate nonzero, and such a tuple is already a unit. Therefore localizing further at the images of elements of $S$ changes nothing. Hence
\[
S^{-1}R
\cong
\QQ[X]/(f)
\cong
\prod_{i=1}^rK_i.
\]
This proves part (a).

:::

:::

::: pf-step

If $f=X^5-1$, then
\[
S^{-1}(\ZZ[X]/(X^5-1))
\cong
\QQ\times\QQ(\zeta_5).
\]

::: pf-proof

Over $\QQ$,
\[
X^5-1=(X-1)\Phi_5(X),
\qquad
\Phi_5(X)=X^4+X^3+X^2+X+1.
\]
The fifth cyclotomic polynomial $\Phi_5$ is irreducible over $\QQ$. Therefore step [](#s2){.pf-ref} gives
\[
\QQ[X]/(X^5-1)
\cong
\QQ[X]/(X-1)\times\QQ[X]/(\Phi_5)
\cong
\QQ\times\QQ(\zeta_5).
\]
This proves part (b).

:::

:::

::: pf-step

The hypothesis $\gcd(f,f')=1$ is not necessary for the conclusion in part (a).

::: pf-proof

Take
\[
f=2X.
\]
Then $f'=2$, so $\gcd(f,f')=2\ne1$. Nevertheless
\[
R=\ZZ[X]/(2X)
\]
is reduced because
\[
(2X)=(2)\cap(X)
\]
in $\ZZ[X]$, an intersection of prime ideals. A reduced Noetherian ring with minimal primes $\mathfrak p_1,\dots,\mathfrak p_s$ has total quotient ring equal to the product of the fraction fields of the domains $R/\mathfrak p_i$. Here the two minimal primes are the images of $(2)$ and $(X)$, so
\[
S^{-1}R
\cong
\operatorname{Frac}(R/(2))\times\operatorname{Frac}(R/(X))
\cong
\mathbb F_2(X)\times\QQ,
\]
a product of fields. Thus the stated gcd hypothesis is sufficient but not necessary.

:::

:::

:::

:::
