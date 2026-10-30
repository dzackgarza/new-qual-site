---
schema: qual/card@1
id: P-NORI-GT-4-09
kind: problem
title: Rational functions invariant under $X\mapsto X+1$ in characteristic zero
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 4.9 of the retained Nori Galois Theory Problems PDF.
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-09-28
  note: The extraction left NUL bytes for sigma; restored from the sigma the same sentences use.
---

::: {.problem}
Given an automorphism $\sigma$ of a ring $R$, denote by $R^{\sigma}$ the subring $\{a \in R \st a = \sigma a\}$.

Let $F$ be a field of characteristic zero. Define $\sigma f(X) = f(X+1)$ for all $f \in F[X]$. Note that $\sigma$ also gives rise to an automorphism of its fraction field $F(X)$. Prove that $F = F[X]^{\sigma} = F(X)^{\sigma}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $f\in F[X]$ is nonconstant, then
$$
f(X+1)\ne f(X).
$$


::: pf-proof

Write
$$
f(X)=a_dX^d+\text{lower-degree terms},
\qquad
 d\ge1,
\qquad
 a_d\ne0.
$$
Then
$$
f(X+1)-f(X)
$$
has leading term
$$
da_dX^{d-1}.
$$
Since $F$ has characteristic $0$, the scalar $d$ is nonzero in $F$. Hence
$$
da_d\ne0,
$$
so the difference is not the zero polynomial.

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\boxed{F[X]^\sigma=F}.
$$


::: pf-proof

Every constant polynomial is fixed by $\sigma$. Step [](#s1-1){.pf-ref} shows that no nonconstant polynomial is fixed.

:::

:::

::: {.pf-step #s1-3}

Let
$$
r(X)\in F(X)
$$
satisfy
$$
r(X+1)=r(X).
$$
If $r$ has a pole $\alpha$ in an algebraic closure $\overline F$, then every
$$
\alpha+n,
\qquad n\in\ZZ,
$$
is also a pole of $r$.


::: pf-proof

The identity
$$
r(X+1)=r(X)
$$
holds in $\overline F(X)$ as well. If $r$ has a pole at $\alpha$, then replacing $X$ by $X-1$ gives
$$
r(X)=r(X-1),
$$
so $r$ has a pole at $\alpha+1$. Iterating gives poles at $\alpha+n$ for all positive $n$. Using the original identity in the opposite direction gives the negative translates as well.

:::

:::

::: {.pf-step #s1-4}

In characteristic $0$, the elements
$$
\alpha+n
\qquad(n\in\ZZ)
$$
are pairwise distinct.


::: pf-proof

If
$$
\alpha+m=\alpha+n,
$$
then
$$
m-n=0
$$
in $\overline F$. Since the characteristic is $0$, the natural map
$$
\ZZ\hookrightarrow\overline F
$$
is injective, so $m=n$.

:::

:::

::: {.pf-step #s1-5}

A $\sigma$-invariant rational function has no finite pole.


::: pf-proof

If it had one finite pole, steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} would produce infinitely many distinct poles. A rational function has only finitely many finite poles, namely the roots of its denominator after cancellation. Contradiction.

:::

:::

::: {.pf-step #s1-6}

Hence every $\sigma$-invariant element of $F(X)$ actually lies in $F[X]$.


::: pf-proof

Write
$$
r=\frac fg
$$
with coprime $f,g\in F[X]$. If $g$ were nonconstant, it would have a root in $\overline F$, producing a finite pole of $r$. Step [](#s1-5){.pf-ref} rules this out. Thus $g$ is constant and $r\in F[X]$.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{F(X)^\sigma=F}.
$$


::: pf-proof

By step [](#s1-6){.pf-ref}, every invariant rational function is a polynomial. Step [](#s1-2){.pf-ref} says the only invariant polynomials are constants.

:::

:::

::: {.pf-step #s1-8}

Consequently
$$
\boxed{F=F[X]^\sigma=F(X)^\sigma}.
$$


::: pf-proof

Combine steps [](#s1-2){.pf-ref} and [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is exactly the required assertion.

:::

:::

:::
