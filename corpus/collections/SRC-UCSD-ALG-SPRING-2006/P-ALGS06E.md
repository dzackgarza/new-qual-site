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
<1>1. Put $R=\mathbb Z[X]/(f)$. The hypothesis $\gcd(f,f')=1$ implies that $f$ is primitive and squarefree in $\mathbb Q[X]$.
::: {.proof}
A nontrivial content of $f$ divides both $f$ and $f'$, so the gcd hypothesis forces the content to be $1$. Over the characteristic-zero field $\mathbb Q$, a polynomial is squarefree exactly when it is relatively prime to its derivative.
:::

<1>2. Every nonzero integer is a non-zero-divisor on $R$, and therefore the total quotient ring $S^{-1}R$ contains
\[
\mathbb Q\otimes_{\mathbb Z}R\cong \mathbb Q[X]/(f).
\]
::: {.proof}
If $0\ne n\in\mathbb Z$ and $ng\in(f)$ in $\mathbb Z[X]$, then $g\in(f)\mathbb Q[X]$. Since $f$ is primitive, Gauss's lemma gives
\[
(f)\mathbb Q[X]\cap\mathbb Z[X]=(f),
\]
so $g\in(f)$. Thus multiplication by $n$ on $R$ is injective.
:::

<1>3. Factor $f$ in $\mathbb Q[X]$ as
\[
f=c f_1\cdots f_t,
\]
where the $f_i$ are distinct monic irreducible polynomials. Then
\[
\mathbb Q[X]/(f)\cong\bigoplus_{i=1}^t \mathbb Q[X]/(f_i).
\]
::: {.proof}
The factors $f_i$ are pairwise coprime because $f$ is squarefree. The Chinese remainder theorem gives the displayed decomposition, and each quotient $\mathbb Q[X]/(f_i)$ is a field.
:::

<1>4. Localizing further at the images of the elements of $S$ does not change the ring in <1>3. Hence
\[
S^{-1}R\cong\bigoplus_{i=1}^t \mathbb Q[X]/(f_i).
\]
::: {.proof}
In a finite product of fields, an element is a non-zero-divisor exactly when all of its components are nonzero, which is equivalent to being a unit. Thus every denominator from $S$ is already invertible after passing to the ring in <1>3.
:::

<1>5. If $f=X^5-1$, then
\[
X^5-1=(X-1)(X^4+X^3+X^2+X+1),
\]
and the second factor is the cyclotomic polynomial $\Phi_5$, irreducible over $\mathbb Q$. Therefore
\[
S^{-1}R\cong \mathbb Q\oplus\mathbb Q(\zeta_5).
\]
::: {.proof}
The first factor gives $\mathbb Q[X]/(X-1)\cong\mathbb Q$, while
\[
\mathbb Q[X]/(\Phi_5)\cong\mathbb Q(\zeta_5).
\]
:::

<1>6. The hypothesis $\gcd(f,f')=1$ is not necessary. Take $f=2X$. Then
\[
\gcd(f,f')=\gcd(2X,2)=2,
\]
but the total quotient ring of $\mathbb Z[X]/(2X)$ is
\[
\mathbb Q\oplus\mathbb F_2(X).
\]
::: {.proof}
The ideal $(2X)$ is radical and has exactly the two minimal primes $(2)$ and $(X)$, because
\[
(2X)=(2)\cap(X).
\]
We use the standard total-quotient-ring theorem for a reduced Noetherian ring with minimal primes $\mathfrak p_1,\dots,\mathfrak p_s$:
\[
Q(R)\cong\bigoplus_i\operatorname{Frac}(R/\mathfrak p_i).
\]
Applying it here gives
\[
Q(\mathbb Z[X]/(2X))
\cong \operatorname{Frac}(\mathbb Z)\oplus\operatorname{Frac}(\mathbb F_2[X])
=\mathbb Q\oplus\mathbb F_2(X).
\]
Thus the conclusion of part (a) can hold even though the gcd hypothesis fails.
:::
:::
