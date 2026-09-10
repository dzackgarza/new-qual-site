---
schema: qual/card@1
id: P-FKTPQ
kind: problem
title: Prime and maximal ideals of $\ZZ[x]$
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Maximal Ideals
  - Polynomials
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
What are the prime ideals and maximal ideals of $\ZZ[x]$?
:::


::: {.solution}
The prime ideals of $\ZZ[x]$ are exactly:

- $(0)$;
- $(p)$ for a rational prime $p$;
- $(f)$ for a primitive irreducible nonconstant polynomial $f\in\ZZ[x]$;
- $(p,f)$ where $p$ is prime and the reduction $\bar f\in\FF_p[x]$ is irreducible.

Among these, the maximal ideals are exactly the ideals $(p,f)$ in the last family.

<1>1. Let $P\subseteq\ZZ[x]$ be prime. Then
\[
P\cap\ZZ=(0)
\quad\text{or}\quad
P\cap\ZZ=(p)
\]
for some prime integer $p$.
::: {.proof}
The contraction of a prime ideal along the inclusion $\ZZ\hookrightarrow\ZZ[x]$ is prime in $\ZZ$. The prime ideals of $\ZZ$ are $(0)$ and $(p)$.
:::

<1>2. If $P\cap\ZZ=(p)$, then either $P=(p)$ or
\[
P=(p,f)
\]
with $\bar f$ irreducible in $\FF_p[x]$.
::: {.proof}
Prime ideals of $\ZZ[x]$ containing $(p)$ correspond to prime ideals of
\[
\ZZ[x]/(p)\cong\FF_p[x].
\]
Since $\FF_p[x]$ is a PID, its prime ideals are $(0)$ and $(\bar f)$ for irreducible $\bar f$. Pulling them back gives the stated ideals.
:::

<1>3. If $P\cap\ZZ=(0)$ and $P\ne(0)$, then
\[
P=(f)
\]
for a primitive irreducible nonconstant $f\in\ZZ[x]$.
::: {.proof}
Localize at $S=\ZZ\setminus\{0\}$. Since $P\cap S=\varnothing$, the localization $S^{-1}P$ is a nonzero prime ideal of
\[
S^{-1}\ZZ[x]=\QQ[x].
\]
Hence
\[
S^{-1}P=(g)
\]
for an irreducible $g\in\QQ[x]$. Multiplying by a rational scalar, choose a primitive $f\in\ZZ[x]$ associated to $g$. By Gauss's lemma, $f$ is irreducible in $\ZZ[x]$, and the contraction of $(g)$ back to $\ZZ[x]$ is $(f)$. Since prime ideals disjoint from $S$ are recovered by contracting their localizations, $P=(f)$.
:::

<1>4. Every listed ideal is prime.
::: {.proof}
The quotient by $(0)$ is the domain $\ZZ[x]$. The quotient by $(p)$ is the domain $\FF_p[x]$. Since $\ZZ[x]$ is a UFD, a primitive irreducible $f$ is prime, so $(f)$ is prime. Finally,
\[
\ZZ[x]/(p,f)\cong\FF_p[x]/(\bar f),
\]
which is a field when $\bar f$ is irreducible.
:::

<1>5. The maximal ideals are exactly the $(p,f)$ with $\bar f$ irreducible modulo $p$.
::: {.proof}
The quotient in <1>4 shows each $(p,f)$ is maximal.

The ideal $(0)$ is not maximal. The ideal $(p)$ is not maximal because its quotient $\FF_p[x]$ is not a field. Finally, let $(f)$ be of the third type. Choose a prime $\ell$ for which the reduction of $f$ modulo $\ell$ is still nonconstant; such a prime exists because some nonconstant coefficient of $f$ is nonzero. If $\ell$ were invertible in $\ZZ[x]/(f)$, there would be $a,b\in\ZZ[x]$ with
\[
\ell a+fb=1.
\]
Reducing modulo $\ell$ would make the nonconstant polynomial $\bar f$ a unit in $\FF_\ell[x]$, impossible. Hence $\ZZ[x]/(f)$ is not a field, so $(f)$ is not maximal.
:::
:::
