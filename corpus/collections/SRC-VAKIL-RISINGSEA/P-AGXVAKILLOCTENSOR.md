---
schema: qual/card@1
id: P-AGXVAKILLOCTENSOR
kind: problem
title: Localization of a module as a tensor product with $S^{-1}A$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Localization
  - Tensor Products
  - Universal Properties
relations: []
review: draft
---

::: {.problem}
If $S\subseteq A$ is multiplicative and $M\in \mods{A}$, describe a natural isomorphism
$$
\eta: (S^{-1}A)\tensor_A M \to S^{-1}M
$$
of both $S^{-1}A\dash$modules and $A\dash$modules.
:::

::: {.solution}
Recall that $S^{-1}M$ is the set of fractions $m/s$ with $m\in M$, $s\in S$, where $m/s = m'/s'$ exactly when $t(s'm - sm') = 0$ for some $t\in S$; the same rule with $M = A$ defines $S^{-1}A$.
The tensor product $S^{-1}A\tensor_A M$ is an $S^{-1}A$-module through the left factor, $\frac{b}{t}\cdot\qty{\frac{a}{s}\tensor m} = \frac{ba}{ts}\tensor m$, and $S^{-1}M$ is an $S^{-1}A$-module by $\frac{b}{t}\cdot\frac{m}{s} = \frac{bm}{ts}$.
Both are $A$-modules by restriction of scalars along $A\to S^{-1}A$, $r\mapsto r/1$.
Every element of $S^{-1}A\tensor_A M$ is a finite sum of elementary tensors, so two additive maps out of it that agree on elementary tensors are equal.

::: pf

::: {.pf-step #eta-defined}
There is an $A$-linear map $\eta$ with
$$
\eta\qty{\frac{a}{s}\tensor m} = \frac{am}{s}.
$$

::: pf-proof
Define $\phi : S^{-1}A\cross M\to S^{-1}M$ by $\phi(a/s, m) = am/s$.
It is well defined: if $a/s = a'/s'$, then $t(s'a - sa') = 0$ for some $t\in S$, so $t(s'(am) - s(a'm)) = (t(s'a - sa'))m = 0$, and $am/s = a'm/s'$.
It is additive in the first variable, since
$$
\phi\qty{\frac{a}{s} + \frac{a'}{s'}, m} = \frac{(s'a + sa')m}{ss'} = \frac{am}{s} + \frac{a'm}{s'},
$$
and additive in $m$ because $a(m + m') = am + am'$.
It is $A$-balanced: for $r\in A$, $\phi(ra/s, m) = ram/s = \phi(a/s, rm)$.
The universal property of $\tensor_A$ gives the additive map $\eta$, and $\eta(r\cdot x) = r\cdot\eta(x)$ holds on elementary tensors by the same computation, so $\eta$ is $A$-linear.
:::

:::

::: {.pf-step #eta-linear}
$\eta$ is $S^{-1}A$-linear.

::: pf-proof
On an elementary tensor,
$$
\eta\qty{\frac{b}{t}\cdot\qty{\frac{a}{s}\tensor m}} = \eta\qty{\frac{ba}{ts}\tensor m} = \frac{bam}{ts} = \frac{b}{t}\cdot\frac{am}{s} = \frac{b}{t}\cdot\eta\qty{\frac{a}{s}\tensor m}.
$$
Both sides are additive in the tensor, so they agree everywhere.
:::

:::

::: {.pf-step #psi-defined}
The rule $\psi(m/s) = \frac{1}{s}\tensor m$ is a well-defined additive map $S^{-1}M\to S^{-1}A\tensor_A M$.

::: pf-proof
Suppose $m/s = m'/s'$, so $t(s'm - sm') = 0$ for some $t\in S$.
Moving elements of $A$ across $\tensor_A$,
$$
\frac{1}{s}\tensor m = \frac{ts'}{tss'}\tensor m = \frac{1}{tss'}\tensor ts'm = \frac{1}{tss'}\tensor tsm' = \frac{ts}{tss'}\tensor m' = \frac{1}{s'}\tensor m'.
$$
For additivity,
$$
\psi\qty{\frac{m}{s} + \frac{m'}{s'}} = \frac{1}{ss'}\tensor(s'm + sm') = \frac{s'}{ss'}\tensor m + \frac{s}{ss'}\tensor m' = \frac{1}{s}\tensor m + \frac{1}{s'}\tensor m'.
$$
:::

:::

::: {.pf-step #inverse}
$\psi$ is a two-sided inverse of $\eta$.

::: pf-proof
For every fraction, $\eta(\psi(m/s)) = \eta\qty{\frac{1}{s}\tensor m} = m/s$.
For every elementary tensor,
$$
\psi\qty{\eta\qty{\frac{a}{s}\tensor m}} = \psi\qty{\frac{am}{s}} = \frac{1}{s}\tensor am = \frac{a}{s}\tensor m.
$$
The map $\psi\circ\eta$ is additive by steps [](#eta-defined){.pf-ref} and [](#psi-defined){.pf-ref} and fixes every elementary tensor, so it is the identity.
:::

:::

::: {.pf-step #natural}
$\eta$ is natural in $M$.

::: pf-proof
Let $h : M\to M'$ be $A$-linear, inducing $\id\tensor h$ on tensor products and $S^{-1}h(m/s) = h(m)/s$ on localizations.
On an elementary tensor,
$$
S^{-1}h\qty{\eta\qty{\frac{a}{s}\tensor m}} = \frac{h(am)}{s} = \frac{a\,h(m)}{s} = \eta'\qty{(\id\tensor h)\qty{\frac{a}{s}\tensor m}},
$$
where $\eta'$ is the map of step [](#eta-defined){.pf-ref} for $M'$.
Both composites are additive, so $S^{-1}h\circ\eta = \eta'\circ(\id\tensor h)$.
:::

:::

::: pf-qed
By steps [](#eta-defined){.pf-ref}, [](#eta-linear){.pf-ref} and [](#inverse){.pf-ref}, the map
$$
\boxed{\eta : S^{-1}A\tensor_A M\to S^{-1}M,\qquad \frac{a}{s}\tensor m\mapsto\frac{am}{s}}
$$
is a bijective $S^{-1}A$-linear map with inverse $m/s\mapsto\frac{1}{s}\tensor m$, hence an isomorphism of $S^{-1}A$-modules.
Restriction of scalars along $A\to S^{-1}A$ makes it an isomorphism of $A$-modules, and step [](#natural){.pf-ref} shows that it is natural in $M$.
:::

:::
:::
