---
schema: qual/card@1
id: P-MAXAT-6-13
kind: problem
title: $\CP^n$ is not a nontrivial product of complex manifolds
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 6, problem 13 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
$\CP ^ { n }$ cannot be expressed non-trivially as a product of complex manifolds.
:::

::: {.solution}

In fact, the stronger topological statement holds: for $n>0$, $\CP^n$ is not homotopy equivalent to a product $X\times Y$ of two connected positive-dimensional closed manifolds. Hence it cannot be biholomorphic to a nontrivial product of complex manifolds.

::: pf

::: {.pf-step #s1-1}

Suppose, for contradiction, that
$$
\CP^n\cong X\times Y
$$
with $X$ and $Y$ connected compact complex manifolds of positive complex dimensions $r$ and $s$, where
$$
r+s=n.
$$


::: pf-proof

A product decomposition of complex manifolds is in particular a diffeomorphism of their underlying smooth manifolds. Positive-dimensional factors have positive real dimensions $2r$ and $2s$.

:::

:::

::: {.pf-step #s1-2}

Since
$$
H^1(\CP^n;\ZZ)=0,
$$
the Kunneth theorem gives
$$
H^1(X;\ZZ)=H^1(Y;\ZZ)=0.
$$


::: pf-proof

For connected spaces,
$$
H^1(X\times Y;\ZZ)
\cong H^1(X;\ZZ)\oplus H^1(Y;\ZZ).
$$
The left side is zero because $X\times Y\cong\CP^n$. Hence both summands vanish.

:::

:::

::: {.pf-step #s1-3}

In degree two, Kunneth gives
$$
H^2(\CP^n;\ZZ)
\cong H^2(X;\ZZ)\oplus H^2(Y;\ZZ).
$$


::: pf-proof

The degree-two Kunneth decomposition contains
$$
H^2(X)\otimes H^0(Y),\quad
H^1(X)\otimes H^1(Y),\quad
H^0(X)\otimes H^2(Y),
$$
together with the corresponding Tor terms. Connectedness gives $H^0\cong\ZZ$, and step [](#s1-2){.pf-ref} kills the degree-one contributions and their Tor terms. Since the product cohomology in degree two is the torsion-free group $\ZZ$, the displayed direct-sum identification follows.

:::

:::

::: {.pf-step #s1-4}

Both groups
$$
H^2(X;\ZZ),\qquad H^2(Y;\ZZ)
$$
are nonzero.


::: pf-proof

Every compact complex manifold is canonically oriented. Since $X$ has real dimension $2r>0$, its fundamental class is nonzero. If $H^2(X;\ZZ)$ were zero, then every degree-two class on the product would come from $Y$. But the generator
$$
h\in H^2(\CP^n;\ZZ)
$$
satisfies
$$
h^n\ne0.
$$
Under the product identification, if $h$ came entirely from $Y$, then
$$
h^{s+1}=0
$$
for dimensional reasons, and since $s<n$ this would force $h^n=0$, a contradiction. Thus $H^2(X)\ne0$. The same argument with the factors interchanged gives $H^2(Y)\ne0$.

:::

:::

::: {.pf-step #s1-5}

Step [](#s1-3){.pf-ref} is impossible because
$$
H^2(\CP^n;\ZZ)\cong\ZZ
$$
has rank one, whereas the right-hand side contains two nonzero free summands.


::: pf-proof

The direct sum in step [](#s1-3){.pf-ref} is isomorphic to the torsion-free group $\ZZ$, so each summand is torsion-free. By step [](#s1-4){.pf-ref} both are nonzero; hence each has rank at least one and their direct sum has rank at least two. This contradicts the rank-one left-hand side.

:::

:::

::: {.pf-step #s1-6}

Therefore no such nontrivial product decomposition exists:
$$
\boxed{
\CP^n\not\cong X\times Y
\quad\text{for }\dim_{\CC}X,\dim_{\CC}Y>0.}
$$


::: pf-proof

The contradiction in step [](#s1-5){.pf-ref} disproves the assumption in step [](#s1-1){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required indecomposability statement.

:::

:::

:::
