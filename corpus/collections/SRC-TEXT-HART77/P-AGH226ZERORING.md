---
schema: qual/card@1
id: P-AGH226ZERORING
kind: problem
title: The spectrum of the zero ring is the initial scheme
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Initial Objects
  - Spectra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.2.6 statement and source-order placement after II.2.5.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Describe the spectrum of the zero ring, and show that it is an initial object for the category of schemes.

According to the conventions in use, all ring homomorphisms must take $1$ to $1$.
Since $0 = 1$ in the zero ring, each ring $R$ admits a unique homomorphism to the zero ring, but there is no homomorphism from the zero ring to $R$ unless $0 = 1$ in $R$.
:::

::: {.solution}
Let $0$ denote the zero ring, in which
\[
0=1.
\]

::: pf

::: {.pf-step #zero-ring-no-primes}
The zero ring has no prime ideals.

::: pf-proof
By definition, a prime ideal is a proper ideal.  The zero ring has only one ideal,
\[
(0)=(1)=0,
\]
which is the whole ring and hence is not proper.  Therefore there are no prime ideals.
:::

:::

::: {.pf-step #specz-ero-empty}
Consequently
\[
\boxed{\operatorname{Spec}0=\varnothing}
\]
as a topological space.

::: pf-proof
The points of the spectrum are the prime ideals, and step [](#zero-ring-no-primes){.pf-ref} shows that there are none.
:::

:::

::: {.pf-step #structure-sheaf-empty-scheme}
The structure sheaf on $\operatorname{Spec}0$ is the unique sheaf of rings on the empty space, with
\[
\mathcal O_{\operatorname{Spec}0}(\varnothing)=0.
\]
Thus $\operatorname{Spec}0$ is the empty scheme.

::: pf-proof
The empty topological space has only the open set $\varnothing$.  For a sheaf of unital rings, the sheaf axiom for the empty covering forces the ring of sections on $\varnothing$ to have exactly one element.  The unique one-element unital ring is the zero ring.

This agrees with the affine formula
\[
\Gamma(\operatorname{Spec}0,\mathcal O)=0.
\]
:::

:::

::: {.pf-step #unique-continuous-map-from-empty}
For every scheme $X$, there is exactly one continuous map
\[
\varnothing\longrightarrow |X|.
\]

::: pf-proof
A function with empty domain is uniquely determined because it has no values to choose.
:::

:::

::: {.pf-step #unique-sheaf-morphism-from-empty}
For this continuous map $f:\varnothing\to X$, there is exactly one morphism of sheaves of rings
\[
f^\sharp:\mathcal O_X\longrightarrow f_*\mathcal O_{\varnothing}.
\]

::: pf-proof
For every open set $U\subseteq X$,
\[
(f_*\mathcal O_{\varnothing})(U)
=\mathcal O_{\varnothing}(f^{-1}U)
=\mathcal O_{\varnothing}(\varnothing)
=0.
\]
There is exactly one unital ring homomorphism
\[
\mathcal O_X(U)\longrightarrow0,
\]
because the target has $1=0$.  These unique maps automatically commute with all restrictions, so they define a unique sheaf morphism.
:::

:::

::: {.pf-step #pair-is-morphism-locally-ringed}
The pair from steps [](#unique-continuous-map-from-empty){.pf-ref} and [](#unique-sheaf-morphism-from-empty){.pf-ref} is automatically a morphism of locally ringed spaces.

::: pf-proof
The locality condition for a morphism of locally ringed spaces is a condition on the induced map of stalks at each point of the source.  The source has no points, so there are no stalk maps to check.  Thus the condition is vacuous.
:::

:::

::: {.pf-step #spec-zero-initial}
Hence for every scheme $X$,
\[
\boxed{
\operatorname{Hom}_{\mathrm{Sch}}(\operatorname{Spec}0,X)
\text{ is a singleton}.
}
\]
Therefore $\operatorname{Spec}0$ is the initial object of the category of schemes.

::: pf-proof
Steps [](#unique-continuous-map-from-empty){.pf-ref}, [](#unique-sheaf-morphism-from-empty){.pf-ref} and [](#pair-is-morphism-locally-ringed){.pf-ref} construct a unique scheme morphism from the empty scheme to $X$.  This is exactly the universal property of an initial object.
:::

:::

::: pf-step
The ring-theoretic direction is consistent with this variance: every ring $R$ has a unique unital homomorphism
\[
R\longrightarrow0,
\]
and the contravariant functor $\operatorname{Spec}$ turns it into the unique scheme morphism
\[
\operatorname{Spec}0\longrightarrow\operatorname{Spec}R.
\]

::: pf-proof
There is only one set map from $R$ to the one-element ring, and it preserves all ring operations and the identity because $1_0=0_0$.  Contravariance reverses its direction on spectra.
:::

:::

::: pf-qed
Steps [](#zero-ring-no-primes){.pf-ref}, [](#specz-ero-empty){.pf-ref} and [](#structure-sheaf-empty-scheme){.pf-ref} describe $\operatorname{Spec}0$, and steps [](#unique-continuous-map-from-empty){.pf-ref}, [](#unique-sheaf-morphism-from-empty){.pf-ref}, [](#pair-is-morphism-locally-ringed){.pf-ref} and [](#spec-zero-initial){.pf-ref} prove its initial property.
:::

:::

:::
