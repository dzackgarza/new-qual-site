---
schema: qual/card@1
id: P-KSRING17-033
kind: problem
title: 'The ring $C[0,1]$: units, idempotents and nilpotents'
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 33 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $R = C[0, 1]$ be the set of all continuous real-valued functions on $[0, 1]$. Define addition and multiplication on $R$ as follows. For $f, g \in R$ and $x \in [0, 1]$,
$$
(f + g)(x) = f(x) + g(x) \quad \text{and} \quad (fg)(x) = f(x)g(x).
$$

(a) Show that $R$ with these operations is a commutative ring with identity.

(b) Find the units of $R$.

(c) If $f \in R$ and $f^{2} = f$, then $f = 0_{R}$ or $f = 1_{R}$.

(d) If $n$ is a positive integer and $f \in R$ is such that $f^{n} = 0_{R}$, then $f = 0_{R}$.
:::

::: {.solution}

Let
$$
R=C([0,1],\RR).
$$

::: pf

::: pf-step

The set $R$ is closed under the stated addition and multiplication.


::: pf-proof

If
$$
f,g\in R,
$$
then
$$
f+g
$$
and
$$
fg
$$
are continuous real-valued functions on $[0,1]$, because sums and products of continuous functions are continuous. Hence both lie in $R$.

:::

:::

::: {.pf-step #s1-2}

With these operations, $R$ is a commutative ring with identity.


::: pf-proof

All ring axioms hold pointwise because they hold in $\RR$.
For example,
$$
((f+g)+h)(x)
=
(f(x)+g(x))+h(x)
=
f(x)+(g(x)+h(x))
=
(f+(g+h))(x).
$$
Associativity and commutativity of multiplication and distributivity are identical pointwise verifications.

The additive identity is the constant zero function
$$
0_R(x)=0,
$$
and the additive inverse of $f$ is the function
$$
(-f)(x)=-f(x).
$$
The multiplicative identity is the constant function
$$
1_R(x)=1.
$$
Thus $R$ is a commutative ring with identity.

:::

:::

::: {.pf-step #s1-3}

If
$$
f\in R
$$
is a unit, then
$$
f(x)\ne0
$$
for every
$$
x\in[0,1].
$$


::: pf-proof

If $f$ is a unit, there exists
$$
g\in R
$$
such that
$$
fg=1_R.
$$
Evaluating at any
$$
x\in[0,1]
$$
gives
$$
f(x)g(x)=1.
$$
Hence
$$
f(x)\ne0.
$$

:::

:::

::: {.pf-step #s1-4}

If
$$
f(x)\ne0
$$
for every
$$
x\in[0,1],
$$
then $f$ is a unit.


::: pf-proof

Define
$$
g(x)
\coloneqq
\frac1{f(x)}.
$$
Because $f$ is continuous and nowhere zero, the reciprocal function $g$ is continuous. Hence
$$
g\in R.
$$
Pointwise,
$$
(fg)(x)
=
f(x)\frac1{f(x)}
=
1,
$$
so
$$
fg=1_R.
$$
Thus $f$ is a unit.

:::

:::

::: {.pf-step #s1-5}

Therefore the units of $R$ are exactly the nowhere-zero functions:
$$
\boxed{
R^\times
=
\{f\in R:f(x)\ne0\text{ for all }x\in[0,1]\}.
}
$$


::: pf-proof

Combine steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

If
$$
f^2=f,
$$
then for every
$$
x\in[0,1],
$$
one has
$$
f(x)\in\{0,1\}.
$$


::: pf-proof

Evaluating the identity
$$
f^2=f
$$
at $x$ gives
$$
f(x)^2=f(x).
$$
Thus
$$
f(x)(f(x)-1)=0
$$
in the field $\RR$, so
$$
f(x)=0
\quad\text{or}\quad
f(x)=1.
$$

:::

:::

::: {.pf-step #s1-7}

Every idempotent in $R$ is either $0_R$ or $1_R$.


::: pf-proof

By step [](#s1-6){.pf-ref}, the image of $f$ lies in
$$
\{0,1\}.
$$
The interval
$$
[0,1]
$$
is connected, and the continuous image of a connected space is connected. The only connected subsets of the discrete set
$$
\{0,1\}
$$
are the singletons.
Hence $f$ is constant, equal either to $0$ or to $1$. Therefore
$$
\boxed{
f=0_R
\quad\text{or}\quad
f=1_R.
}
$$

:::

:::

::: {.pf-step #s1-8}

If
$$
f^n=0_R
$$
for some positive integer $n$, then
$$
f=0_R.
$$


::: pf-proof

For each
$$
x\in[0,1],
$$
evaluating
$$
f^n=0_R
$$
gives
$$
f(x)^n=0.
$$
Since $\RR$ has no nonzero nilpotent elements,
$$
f(x)=0.
$$
This holds for every $x$, so
$$
\boxed{f=0_R.}
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part (a), step [](#s1-5){.pf-ref} proves part (b), step [](#s1-7){.pf-ref} proves part (c), and step [](#s1-8){.pf-ref} proves part (d).

:::

:::

:::
