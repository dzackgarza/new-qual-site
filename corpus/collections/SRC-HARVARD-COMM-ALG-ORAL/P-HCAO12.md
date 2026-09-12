---
schema: qual/card@1
id: P-HCAO12
kind: problem
title: A polynomial ring over a unique factorization domain is a unique factorization domain
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Polynomials
  - Integral Domains
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $R$ be a unique factorization domain.
Prove that $R[x]$ is a unique factorization domain.
:::

::: solution
Let $K=\operatorname{Frac}(R)$.

For a nonzero polynomial $f\in R[x]$, define its content $c(f)$ to be a gcd of
its coefficients, determined up to a unit. A polynomial is primitive if its
content is a unit.

<1>1. The product of two primitive polynomials in $R[x]$ is primitive.
::: proof
Let $f,g\in R[x]$ be primitive. Suppose a prime element $p\in R$ divided every
coefficient of $fg$. Reducing modulo $(p)$ gives
\[
\overline f\,\overline g=0
\qquad\text{in }(R/(p))[x].
\]
In a UFD every prime element is prime, so $R/(p)$ is an integral domain.
Because $f$ and $g$ are primitive, neither has all coefficients divisible by
$p$, hence $\overline f\ne0$ and $\overline g\ne0$. Their product cannot be
zero in the polynomial ring over a domain, a contradiction. Thus no prime
divides all coefficients of $fg$, so $fg$ is primitive.
:::

<1>2. If $f\in R[x]$ is primitive, then $f$ is reducible in $R[x]$ if and only
if it is reducible in $K[x]$.
::: proof
Only the reverse implication needs proof. Suppose
\[
f=gh
\]
in $K[x]$ with $\deg g,\deg h>0$. Clearing denominators and dividing out the
contents, write
\[
g=a g_0,
\qquad
h=b h_0,
\]
where $a,b\in K^\times$ and $g_0,h_0\in R[x]$ are primitive. Then
\[
f=(ab)g_0h_0.
\]
By <1>1, $g_0h_0$ is primitive.

We claim that if two primitive polynomials $u,v\in R[x]$ satisfy
$u=\lambda v$ for some $\lambda\in K^\times$, then $\lambda$ is a unit of
$R$. Write $\lambda=r/s$ with $r,s\in R$ having no common prime factor. From
$su=rv$, every prime divisor of $s$ divides every coefficient of $rv$. Since
it does not divide $r$, it would divide every coefficient of $v$, contradicting
primitivity. Hence $s$ is a unit. Applying the same argument to
$v=\lambda^{-1}u$ shows that $r$ is a unit. Thus $\lambda\in R^\times$.

Applying this claim to $f=(ab)g_0h_0$ shows $ab\in R^\times$. Hence, after
multiplying one factor by this unit,
\[
f=g_0\,(ab\,h_0)
\]
is a nontrivial factorization in $R[x]$.
:::

<1>3. Every nonzero nonunit of $R[x]$ factors into irreducibles.
::: proof
Let $0\ne f\in R[x]$. Write
\[
f=c(f)f_0
\]
with $f_0$ primitive. Factor the constant $c(f)$ into irreducibles of the UFD
$R$.

Since $K[x]$ is a PID, hence a UFD, factor
\[
f_0=q_1\cdots q_m
\]
into irreducibles in $K[x]$. For each $q_i$, clear denominators and divide by
the content to obtain a primitive polynomial $p_i\in R[x]$ differing from
$q_i$ by a scalar in $K^\times$. Thus
\[
f_0=\lambda p_1\cdots p_m
\]
for some $\lambda\in K^\times$. Both sides apart from the scalar are primitive
by <1>1, so the scalar claim from <1>2 gives $\lambda\in R^\times$.

Each $p_i$ is irreducible in $R[x]$: otherwise it would be reducible in $K[x]$
by the easy direction of <1>2, contradicting irreducibility of $q_i$. The
irreducible factors of $c(f)$ remain irreducible as constant polynomials, since
any factorization of a nonzero constant in $R[x]$ has constant factors. Hence
$f$ factors into irreducibles in $R[x]$.
:::

<1>4. Factorization into irreducibles in $R[x]$ is unique up to order and
associates.
::: proof
Separate any factorization of $f$ into its constant irreducible factors and its
positive-degree primitive irreducible factors. The product of the constant
factors is, up to a unit, the content $c(f)$, whose factorization is unique in
$R$.

After dividing by the content, the remaining primitive factorization is a
factorization of $f_0$ in $K[x]$. By <1>2, each primitive irreducible of
$R[x]$ remains irreducible in $K[x]$. Uniqueness in the UFD $K[x]$ therefore
matches the positive-degree factors up to scalar associates. If two primitive
$R[x]$ polynomials are scalar associates in $K[x]$, the scalar claim in <1>2
shows that the scalar is a unit of $R$, so they are already associates in
$R[x]$. Thus the factorization is unique in $R[x]$.
:::

<1>5. Therefore $R[x]$ is a UFD.
::: proof
Existence is <1>3 and uniqueness is <1>4.
:::
:::
