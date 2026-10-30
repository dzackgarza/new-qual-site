---
schema: qual/card@1
id: E-SS8.EX-11
kind: problem
title: $\abs{\frac{f(z)-f(0)}{M^2-\overline{f(0)}f(z)}}\le\frac{\abs z}{MR}$ for $\abs f\le M$ on $D(0,R)$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Repaired the non-strict bound so the displayed Möbius quotient is defined in the extremal constant
    case.
- event: source-checked
  by: claude-opus-5.5
  date: 2026-10-31
  note: Restored the book's bound |f|<=M; the solution treats the constant case |f|=M, where the quotient
    is undefined.
---

::: {.exercise}
Show that if $f : D ( 0 , R ) \to \CC$ is holomorphic, with $\abs{ f ( z ) } \leq M$ for some $M > 0 ,$ then

$$
\abs{ \frac {f (z) - f (0)}{M ^ {2} - \overline {{f (0)}} f (z)} } \leq \frac {\abs{ z }}{M R}.
$$

[Hint: Use the Schwarz lemma.]
:::

::: {.solution}
If $\abs{f(z_0)}=M$ for some $z_0$, the maximum modulus principle makes $f$ a constant of modulus $M$. Then both numerator and denominator vanish, and the quotient is undefined. So assume $f$ is not such a constant. The maximum modulus principle then gives $\abs{f}<M$ on $D(0,R)$.

Define
$$
g(\zeta)=\frac{f(R\zeta)}{M},\qquad \zeta\in\DD.
$$
Then $g:\DD\to\DD$. Put $a=g(0)=f(0)/M$ and let
$$
\phi_a(w)=\frac{w-a}{1-\overline a\,w},
$$
the automorphism of $\DD$ carrying $a$ to $0$. The function
$$
h=\phi_a\circ g
$$
is holomorphic from $\DD$ to itself and satisfies $h(0)=0$. Schwarz's lemma yields
$$
\abs{h(\zeta)}\le\abs{\zeta}.
$$
For $z=R\zeta$, this becomes
$$
\abs{\frac{f(z)/M-f(0)/M}{1-\overline{f(0)}f(z)/M^2}}
\le \frac{\abs{z}}{R}.
$$
Simplifying,
$$
M\abs{\frac{f(z)-f(0)}{M^2-\overline{f(0)}f(z)}}
\le\frac{\abs{z}}{R},
$$
and hence
$$
\boxed{
\abs{\frac{f(z)-f(0)}{M^2-\overline{f(0)}f(z)}}
\le\frac{\abs{z}}{MR}}.
$$
:::

::: {.remark title="Variations"}
If $f\colon D(a,R)\to D(0,M)$ is holomorphic with $f(a)=0$, then $\abs{f(z)}\le\frac{M}{R}\abs{z-a}$.
Apply the main inequality to $z\mapsto f(z+a)$ on $D(0,R)$; since its value at $0$ is $0$, the inequality reads $\frac{\abs{f(z+a)}}{M^2}\le\frac{\abs z}{MR}$.
:::
