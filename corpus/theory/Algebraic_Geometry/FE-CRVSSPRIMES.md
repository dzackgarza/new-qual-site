---
schema: qual/card@1
id: FE-CRVSSPRIMES
kind: example
title: Fixing the curve and varying $p$, and the density of supersingular primes
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Characteristic p
  - Complex Multiplication
relations:
- kind: uses
  target: T-CRVHASSE
- kind: uses
  target: T-CRVCM
- kind: related-to
  target: T-CRVCMCFT
review: draft
prompts:
- Fix an elliptic curve over $\QQ$ and reduce it mod $p$ --- for how many $p$ is the reduction supersingular?
- Work out the supersingular primes of $y^2 = x^3 - x$ by hand.
- How does complex multiplication change the answer?
- Given a curve over $\QQ$, what test rules out complex multiplication?
---

::: {.example title="The setup"}
Let $X = V(f) \subseteq \PP^2_{/\ZZ}$ with $f \in \ZZ[x,y,z]$ a cubic whose base change to $\CC$ is smooth.
For all but finitely many primes the reduction $X_{(p)} \subseteq \PP^2_{/\FF_p}$ is again smooth.
Let
$$
B \coloneqq \theset{ p \st X_{(p)} \text{ is smooth over } \bar\FF_p \text{ and has Hasse invariant } 0 } .
$$
The set $B$ depends on whether $X_{/\CC}$ has complex multiplication:

- With CM by an order in an imaginary quadratic field $K$: for $p$ of good reduction, $p \in B$ exactly when $p$ does not split in $K$, that is when $p$ is inert or ramified.
  This is Deuring's theorem.
  Half the primes split, so $B$ has density $\tfrac{1}{2}$.

- Without CM: $B$ has density $0$ (Serre), and $B$ is infinite (Elkies).
  The asymptotic $\abs{\theset{p \in B \st p \leq x}} \sim c\,\tfrac{\sqrt x}{\log x}$ is the Lang--Trotter conjecture, which is open.
:::

::: {.remark title="Status of the three claims"}
Deuring's criterion is an equivalence, and the density $\tfrac12$ follows from it by Chebotarev's density theorem, or by Dirichlet's theorem when the splitting condition is a congruence.
Density zero in the non-CM case is Serre's theorem, proved from the distribution of Frobenius traces.
Elkies proved infinitude in the non-CM case for elliptic curves over $\QQ$, and more generally over number fields with a real embedding.
The $\sqrt x/\log x$ growth is a conjecture.
:::

::: {.example title="$y^2 = x^3 - x$, worked out"}
Here $\lambda = -1$, $j = 1728$, and the curve has CM by $\ZZ[i]$.
For an odd prime $p$, apply the Hasse-invariant criterion with $m = \tfrac{p-1}{2}$ and $g(x) = x(x^2-1)$,
$$
g(x)^m = x^m (x^2-1)^m ,
$$
so the coefficient of $x^{p-1} = x^{2m}$ is the coefficient of $x^m$ in $(x^2-1)^m$.
Only even powers appear there, so that coefficient is $0$ when $m$ is odd, and $(-1)^{m/2}\binom{m}{m/2}$ when $m$ is even --- which is prime to $p$, since $m < p$.
Hence
$$
X_{(p)} \text{ supersingular}
\iff m = \tfrac{p-1}{2} \text{ is odd}
\iff p \equiv 3 \bmod 4 .
$$
The condition $p \equiv 3 \bmod 4$ is exactly the condition that $p$ stays prime in $\ZZ[i]$, as Deuring's theorem predicts.
By Dirichlet these have density $\tfrac{1}{2}$ and there are infinitely many.
:::

::: {.example title="$y^2 = x(x-1)(x-3)$, the contrast"}
Here $\lambda = 3$ and
$$
j = 2^8 \cdot \frac{(9-3+1)^3}{9 \cdot 4} = \frac{2^6 \cdot 7^3}{3^2} \notin \ZZ .
$$
Computing $h_p(3) \bmod p$ for the primes of good reduction, the only supersingular prime below $120$ is $p = 23$.
The density-zero statement follows from the non-CM theorem above, and $j\notin\overline{\ZZ}$ rules out complex multiplication entirely.
:::

::: {.remark}
For a curve with CM by an order in $K$ and a prime $p$ of good reduction, the endomorphism ring of the reduction over $\bar\FF_p$ contains that order.
When $p$ splits in $K$, the reduction is ordinary and its endomorphism ring is an order in $K$; when $p$ is inert or ramified, the reduction is supersingular and its endomorphism ring is a maximal order in a quaternion algebra.
Whether $p$ splits in $K$ is decided by the Legendre symbol $\qty(\tfrac{d_K}{p})$, a congruence condition on $p$.

Without CM, a prime $p \geq 5$ of good reduction is supersingular exactly when the Frobenius trace $a_p$ is $0$, and the density-zero theorem, Elkies' theorem, and the Lang--Trotter conjecture concern how often $a_p$ vanishes.

A CM $j$-invariant is an algebraic integer, so a $j$-invariant that is not an algebraic integer, in particular a non-integral rational $j$, rules out CM.
:::
