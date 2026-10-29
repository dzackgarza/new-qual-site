---
schema: qual/card@1
id: P-UCLARA11F-10
kind: problem
title: Two fixed points force the identity
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2011 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $\Omega\subsetneq\CC$ be a simply connected domain and let $f:\Omega\to\Omega$ be holomorphic.
Suppose there are distinct points $z_1,z_2\in\Omega$ with $f(z_1)=z_1$ and $f(z_2)=z_2$.
Show that $f$ is the identity on $\Omega$.
:::

::: {.solution}

Since
\[
\Omega\subsetneq\CC
\]
is simply connected, the Riemann mapping theorem gives a biholomorphism
\[
\phi:\Omega\to\mathbb D.
\]

Define
\[
F=\phi\circ f\circ\phi^{-1}:\mathbb D\to\mathbb D.
\]

::: pf

::: pf-step

The points
\[
w_1=\phi(z_1),
\qquad
w_2=\phi(z_2)
\]
are distinct fixed points of \(F\).


::: pf-proof

Since \(f(z_j)=z_j\),
\[
F(w_j)
=
\phi(f(\phi^{-1}(w_j)))
=
\phi(f(z_j))
=
\phi(z_j)
=
w_j.
\]
The points are distinct because \(\phi\) is injective.

:::

:::

::: pf-step

Let
\[
\psi(\zeta)
=
\frac{\zeta-w_1}{1-\overline{w_1}\zeta}.
\]
Then \(\psi\) is an automorphism of \(\mathbb D\) satisfying
\[
\boxed{\psi(w_1)=0}.
\]


::: pf-proof

This is the standard disk automorphism carrying \(w_1\) to \(0\).

:::

:::

::: {.pf-step #s1-3}

One has
\[
\boxed{G(0)=0}.
\]


::: pf-proof

Since
\[
\psi^{-1}(0)=w_1
\]
and \(F(w_1)=w_1\),
\[
G(0)
=
\psi(F(w_1))
=
\psi(w_1)
=
0.
\]

:::

:::

::: pf-step

Let
\[
a=\psi(w_2).
\]
Then
\[
\boxed{a\ne0}.
\]


::: pf-proof

The automorphism \(\psi\) is injective and
\[
w_2\ne w_1.
\]
Since \(\psi(w_1)=0\), one must have \(\psi(w_2)\ne0\).

:::

:::

::: {.pf-step #s1-5}

The point \(a\) is also fixed by \(G\):
\[
\boxed{G(a)=a}.
\]


::: pf-proof

\[
\begin{aligned}
G(a)
&=
\psi(F(\psi^{-1}(a)))\\
&=
\psi(F(w_2))\\
&=
\psi(w_2)\\
&=
a.
\end{aligned}
\]

:::

:::

::: pf-step

By Schwarz's lemma,
\[
|G(\zeta)|
\le
|\zeta|
\]
for every \(\zeta\in\mathbb D\).


::: pf-proof

The map \(G:\mathbb D\to\mathbb D\) is holomorphic and fixes \(0\) by step [](#s1-3){.pf-ref}.

:::

:::

::: pf-step

At the nonzero point \(a\),
\[
|G(a)|=|a|.
\]


::: pf-proof

By step [](#s1-5){.pf-ref},
\[
G(a)=a.
\]

:::

:::

::: {.pf-step #s1-8}

Equality in Schwarz's lemma at the nonzero point \(a\) implies
\[
\boxed{
G(\zeta)=e^{i\theta}\zeta}
\]
for some real \(\theta\).


::: pf-proof

The equality case of Schwarz's lemma says that if
\[
|G(a)|=|a|
\]
at some nonzero \(a\in\mathbb D\), then \(G\) is a rotation.

:::

:::

::: {.pf-step #s1-9}

Since \(G(a)=a\) and \(a\ne0\),
\[
\boxed{e^{i\theta}=1}.
\]


::: pf-proof

From step [](#s1-8){.pf-ref},
\[
a=G(a)=e^{i\theta}a.
\]
Divide by \(a\ne0\).

:::

:::

::: pf-step

Hence
\[
\boxed{
G=\operatorname{id}_{\mathbb D}}.
\]


::: pf-proof

Step [](#s1-8){.pf-ref} becomes
\[
G(\zeta)=\zeta
\]
after step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

Therefore
\[
F
=
\psi^{-1}\circ G\circ\psi
=
\operatorname{id}_{\mathbb D}.
\]


::: pf-proof

Conjugating the identity map by \(\psi\) gives the identity map.

:::

:::

::: {.pf-step #s1-12}

Finally,
\[
f
=
\phi^{-1}\circ F\circ\phi
=
\operatorname{id}_{\Omega}.
\]


::: pf-proof

Use step [](#s1-11){.pf-ref} and the definition of \(F\).

:::

:::

::: {.pf-step #s1-13}

Thus
\[
\boxed{
f(z)=z
\qquad\text{for every }z\in\Omega}.
\]


::: pf-proof

This is step [](#s1-12){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-13){.pf-ref} is the required conclusion.

:::

:::

:::
