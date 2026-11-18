---
schema: qual/card@1
id: P-CASP07B
kind: problem
title: "Zero-free disk for bounded analytic functions and characterization of extremal functions"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, correct as it
    stood. Added: the normalisation h = f/M with a = alpha/M in (0,1] and the observation that a
    nonconstant h with |h| <= 1 has |h| < 1 inside the disc, which is what puts h in the range
    where Schwarz-Pick applies; the Schwarz-Pick inequality with both sides identified; the
    computation e^{i theta} = -a/z_0; and, for the "find all" part, the converse verification
    that each displayed function satisfies |f| <= M, f(0) = alpha real positive, and vanishes
    on the circle, together with the case a = 1 where the maximum principle forces f = M and no
    extremal exists. Not claimed: a retained solution set; the provenance names the examination
    paper.
---

::: {.problem}
Let $f(z)$ be analytic with $\abs{f(z)} \leq M$ in $\DD$ and $f(0) = \alpha > 0$.

(a) Show that $f(z)$ has no zeros in the disk $\abs{z} < \alpha/M$.

(b) Find all functions $f(z)$ (satisfying the above) such that $f(z)$ has a zero on the circle $\abs{z} = \alpha/M$.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Spring 2007 complex-analysis examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose.

Throughout $f$ is analytic on $\DD$ with $\abs f\le M$ and $f(0)=\alpha>0$; for $M=0$ there is nothing to prove, so assume $M>0$ and put $h=f/M$, $a=\alpha/M\in(0,1]$.

::: pf

::: {.pf-step #normalise}
$h$ is holomorphic on $\DD$ with $\abs h\le1$ and $h(0)=a\in(0,1]$; if $h$ is nonconstant then $\abs{h}<1$ on $\DD$.

::: pf-proof
$\abs h=\abs f/M\le1$ and $h(0)=\alpha/M$. A nonconstant holomorphic function cannot attain its maximum modulus at an interior point, so $\abs h<1$ throughout $\DD$ unless $h$ is constant of modulus $1$.

:::

:::

::: {.pf-step #part-a}
$f$, hence $h$, has no zero with $\abs z<a$.

::: pf-proof
Let $h(z_0)=0$. Schwarz–Pick applied to $h$ at $0$ and $z_0$,
$$
\abs{\frac{h(z_0)-h(0)}{1-\overline{h(0)}\,h(z_0)}}\le\abs{\frac{0-z_0}{1-\overline{z_0}\cdot0}},
$$
reads $a\le\abs{z_0}$, since the left side is $\abs{h(0)}=a$. So no zero satisfies $\abs{z_0}<a$.

:::

:::

::: {.pf-step #extremals-interior}
Assume $a<1$ and let $h(z_0)=0$ with $\abs{z_0}=a$. Then $h$ is a disk automorphism and
$$
h(z)=e^{i\theta}\frac{z-z_0}{1-\overline{z_0}z},\qquad e^{i\theta}=-\frac{a}{z_0}.
$$

::: pf-proof
At the pair of distinct points $0\ne z_0$ the Schwarz–Pick inequality of step [](#part-a){.pf-ref} is an equality, so the equality case makes $h$ an automorphism of $\DD$, and every automorphism has the displayed form. Evaluating at $0$: $a=h(0)=e^{i\theta}(-z_0)$, so $e^{i\theta}=-a/z_0$.

:::

:::

::: {.pf-step #extremals-form}
For $a<1$ the extremals are exactly
$$
f(z)=-M\,\frac{a}{z_0}\,\frac{z-z_0}{1-\overline{z_0}z},\qquad \abs{z_0}=a=\alpha/M,
$$
and for $a=1$ there are none.

::: pf-proof
The form follows from step [](#extremals-interior){.pf-ref} on multiplying by $M$. Conversely, each such $f$ has $\abs f\le M$ because the automorphism factor has modulus $\le1$; $f(0)=-M(a/z_0)(-z_0)=\alpha$, which is real and positive; and $f(z_0)=0$ while $\abs{z_0}=a=\alpha/M$, so the zero lies on the required circle — provided $a<1$, which keeps $z_0\in\DD$. If $a=1$ then $h(0)=1=\max\abs h$, so the maximum modulus principle gives $h\equiv1$ and $f\equiv M$, which has no zeros at all.

:::

:::

::: {.pf-step #conclusion}
(a) $f$ is zero-free on $\abs z<\alpha/M$; (b) the functions with a zero on the circle are those displayed in step [](#extremals-form){.pf-ref} when $\alpha<M$, and none when $\alpha=M$.

::: pf-proof
Step [](#part-a){.pf-ref} is (a); step [](#extremals-form){.pf-ref} is (b), including the case $\alpha=M$.

:::

:::

:::
:::
