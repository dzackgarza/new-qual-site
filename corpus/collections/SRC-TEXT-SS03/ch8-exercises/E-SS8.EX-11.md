---
schema: qual/card@1
id: E-SS8.EX-11
kind: problem
title: $\abs{\frac{f(z)-f(0)}{M^2-\overline{f(0)}f(z)}}\le\frac{\abs z}{MR}$ for $\abs f<M$ on $D(0,R)$
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
  note: Repaired the non-strict bound so the displayed Möbius quotient is defined in the extremal constant case.
---

::: {.exercise}
11. Show that if $f : D ( 0 , R ) \to \CC$ is holomorphic, with $| f ( z ) | < M$ for some $M > 0 ,$ then

$$
\left| \frac {f (z) - f (0)}{M ^ {2} - \overline {{f (0)}} f (z)} \right| \leq \frac {| z |}{M R}.
$$

[Hint: Use the Schwarz lemma.]
:::

::: {.solution}
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
|h(\zeta)|\le|\zeta|.
$$
For $z=R\zeta$, this becomes
$$
\left|\frac{f(z)/M-f(0)/M}{1-\overline{f(0)}f(z)/M^2}\right|
\le \frac{|z|}{R}.
$$
Simplifying,
$$
M\left|\frac{f(z)-f(0)}{M^2-\overline{f(0)}f(z)}\right|
\le\frac{|z|}{R},
$$
and hence
$$
\boxed{
\left|\frac{f(z)-f(0)}{M^2-\overline{f(0)}f(z)}\right|
\le\frac{|z|}{MR}}.
$$
:::
