---
schema: qual/card@1
id: P-UMNCP-F11-02
kind: problem
title: A nowhere-zero entire function has an entire logarithm
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Fall 2011, 2 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Let $h$ be a nowhere-zero entire function.
Prove that there exists an entire function $g$ such that
$$
e^g=h.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The logarithmic derivative
$$
\frac{h'}h
$$
is entire.


::: pf-proof

The functions
$$
h'
\quad\text{and}\quad
h
$$
are entire, and by hypothesis
$$
h(z)\ne0
$$
for every
$$
z\in\CC.
$$
Therefore the quotient is entire.

:::

:::

::: {.pf-step #s1-2}

There exists an entire function $G$ such that
$$
\boxed{
G'(z)
=
\frac{h'(z)}{h(z)}}.
$$


::: pf-proof

Every entire function has an entire primitive because
$$
\CC
$$
is simply connected. Apply this to the entire function from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

The entire function
$$
H(z)
\coloneqq
h(z)e^{-G(z)}
$$
has derivative identically zero.


::: pf-proof

Differentiate:
$$
\begin{aligned}
H'(z)
&=
h'(z)e^{-G(z)}
-h(z)G'(z)e^{-G(z)}\\
&=
e^{-G(z)}
\left(
h'(z)-h(z)G'(z)
\right).
\end{aligned}
$$
Using step [](#s1-2){.pf-ref},
$$
h(z)G'(z)
=
h(z)\frac{h'(z)}{h(z)}
=
h'(z).
$$
Hence
$$
H'(z)=0
$$
for every $z$.

:::

:::

::: {.pf-step #s1-4}

There is a nonzero constant
$$
c\in\CC^*
$$
such that
$$
\boxed{
h(z)=ce^{G(z)}}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
H
$$
is constant on the connected plane:
$$
H(z)\equiv c.
$$
Since both
$$
h(z)
$$
and
$$
e^{-G(z)}
$$
are nowhere zero, one has
$$
c\ne0.
$$
Rearranging
$$
h(z)e^{-G(z)}=c
$$
gives the displayed formula.

:::

:::

::: {.pf-step #s1-5}

Choose
$$
\lambda\in\CC
$$
such that
$$
e^\lambda=c.
$$
Then
$$
g
\coloneqq
G+\lambda
$$
is entire and satisfies
$$
\boxed{e^g=h}.
$$


::: pf-proof

Every nonzero complex number has a complex logarithm, so such a
$$
\lambda
$$
exists. The function
$$
g=G+\lambda
$$
is entire. By step [](#s1-4){.pf-ref},
$$
e^{g(z)}
=
e^{G(z)}e^\lambda
=
ce^{G(z)}
=
h(z).
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} constructs the required entire logarithm.

:::

:::

:::
