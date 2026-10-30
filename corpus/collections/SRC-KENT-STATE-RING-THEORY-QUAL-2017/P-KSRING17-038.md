---
schema: qual/card@1
id: P-KSRING17-038
kind: problem
title: Splitting of $x^3+1$ over $\ZZ_p$ for $p\equiv 1 \pmod 6$
classification:
  areas: [algebra]
  topics:
  - Finite Fields
  - Roots of Unity
  - Splitting of Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 38 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Show that if $p$ is a prime such that $p \equiv 1 \pmod{6}$, then $x^{3} + 1$ splits in $\ZZ_{p}[x]$.
:::

::: {.solution}

Assume
$$
p\equiv1\pmod6.
$$

::: pf

::: {.pf-step #s1-1}

The integer
$$
p-1
$$
is divisible by $3$.


::: pf-proof

The congruence
$$
p\equiv1\pmod6
$$
means
$$
p-1
$$
is divisible by $6$, hence in particular by $3$.

:::

:::

::: pf-step

The multiplicative group
$$
\FF_p^\times
$$
contains an element
$$
\omega
$$
of order $3$.


::: pf-proof

The group
$$
\FF_p^\times
$$
has order
$$
p-1.
$$
By step [](#s1-1){.pf-ref},
$$
3\mid\abs{\FF_p^\times}.
$$
Cauchy's theorem for finite groups therefore gives an element
$$
\omega\in\FF_p^\times
$$
of order $3$.

:::

:::

::: pf-step

The elements
$$
1,\omega,\omega^2
$$
are the three distinct roots of
$$
t^3-1
$$
in $\FF_p$.


::: pf-proof

Because
$$
\omega^3=1,
$$
each of
$$
1,\omega,\omega^2
$$
satisfies
$$
t^3=1.
$$
They are distinct because $\omega$ has order exactly $3$.

The polynomial
$$
t^3-1
$$
has degree $3$, so it has at most three roots in the field $\FF_p$. Hence these are all of its roots.

:::

:::

::: {.pf-step #s1-4}

The elements
$$
-1,
\qquad
-\omega,
\qquad
-\omega^2
$$
are three distinct roots of
$$
x^3+1.
$$


::: pf-proof

If
$$
\eta^3=1,
$$
then
$$
(-\eta)^3+1
=
-\eta^3+1
=
0.
$$
Apply this to
$$
\eta\in\{1,\omega,\omega^2\}.
$$
The three negatives remain distinct.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
x^3+1
=
(x+1)(x+\omega)(x+\omega^2)
}
$$
in
$$
\FF_p[x].
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, the monic cubic
$$
x^3+1
$$
has the three distinct roots
$$
-1,-\omega,-\omega^2.
$$
A monic degree-$3$ polynomial is therefore the product of the corresponding monic linear factors.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} shows that $x^3+1$ splits completely over $\FF_p$.

:::

:::

:::
