---
schema: qual/card@1
id: P-MAXAT-3-06
kind: problem
title: Cohomology rings of the loop spaces $\Omega\CP^n$ and $\Omega\RP^n$
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 3, problem 6 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Find the cohomology ring of $\Omega \CP^{n}$, $\Omega \RP^{n}$. (Hint: use a spectral sequence argument)
:::

::: {.solution}

Use integral coefficients and based loop spaces. Write $\Gamma_{mathbb Z}(y)$ for the divided-power algebra with basis $\gamma_j(y)$, $j\geq0$, and multiplication
$$
\gamma_i(y)\gamma_j(y)=\binom{i+j}{i}\gamma_{i+j}(y).
$$

::: pf

::: {.pf-step #s1-1}

Looping the Hopf fibration
$$
S^1\longrightarrow S^{2n+1}\longrightarrow\CP^n
$$
gives a fibration
$$
\Omega S^{2n+1}\longrightarrow\Omega\CP^n
\longrightarrow S^1.
$$


::: pf-proof

For any fibration $F\to E\to B$, the associated homotopy-fiber sequence contains
$$
\Omega E\to\Omega B\to F.
$$
Apply this to the Hopf fibration. Since $\Omega S^1$ is discrete and the relevant identity component is contractible, the displayed part is the resulting fibration over $S^1$.

:::

:::

::: {.pf-step #s1-2}

The fibration in step [](#s1-1){.pf-ref} splits up to homotopy:
$$
\Omega\CP^n\simeq S^1\times\Omega S^{2n+1}.
$$


::: pf-proof

The connecting map $\Omega\CP^n\to S^1$ induces an isomorphism on $\pi_1$: from the long exact sequence of the Hopf fibration,
$$
\pi_2(\CP^n)\cong\pi_1(S^1)\cong\ZZ.
$$
A loop representing the corresponding generator gives a homotopy section $S^1\to\Omega\CP^n$. The fiber is the H-space $\Omega S^{2n+1}$, and multiplication by the section gives the stated homotopy product decomposition.

:::

:::

::: {.pf-step #s1-3}

The path-loop Serre spectral sequence for
$$
\Omega S^{2n+1}\to PS^{2n+1}\to S^{2n+1}
$$
gives
$$
H^*(\Omega S^{2n+1};\ZZ)
\cong\Gamma_{mathbb Z}(y_{2n}),
\qquad \gradeddegree{y_{2n}}=2n.
$$


::: pf-proof

The total space $PS^{2n+1}$ is contractible. In the cohomology Serre spectral sequence, the sphere's top class in bidegree $(2n+1,0)$ must transgress to a generator in fiber degree $2n$. Multiplicativity then forces one free rank-one group in each degree $2nj$, and comparison of products through the transgression gives
$$
\gamma_i(y)\gamma_j(y)=\binom{i+j}{i}\gamma_{i+j}(y),
$$
the divided-power multiplication. Equivalently, this is dual to
$$
H_*(\Omega S^{2n+1};\ZZ)\cong\ZZ[t_{2n}].
$$

:::

:::

::: {.pf-step #s1-4}

Hence
$$
\boxed{
H^*(\Omega\CP^n;\ZZ)
\cong\Lambda_{mathbb Z}(a_1)\otimes
\Gamma_{mathbb Z}(y_{2n}).}
$$


::: pf-proof

Apply the Künneth theorem to step [](#s1-2){.pf-ref}. The cohomology of $S^1$ is $\Lambda(a_1)$, and step [](#s1-3){.pf-ref} gives the other factor. Both are torsion-free, so there are no Tor terms.

:::

:::

::: {.pf-step #s1-5}

For $n\geq2$, the covering
$$
S^n\to\RP^n
$$
identifies each path component of $\Omega\RP^n$ with a space homotopy equivalent to $\Omega S^n$, and there are exactly two components.


::: pf-proof

The components of a based loop space are indexed by $\pi_1$, so
$$
\pi_0(\Omega\RP^n)=\pi_1(\RP^n)=\ZZ/2.
$$
Every null-homotopic based loop lifts uniquely to a based loop in the universal cover $S^n$, giving a homeomorphism of the identity component with $\Omega S^n$. Multiplication by any loop representing the nontrivial element of $\pi_1$ is a homotopy equivalence from the identity component to the other component.

:::

:::

::: {.pf-step #s1-6}

Therefore, as a graded ring,
$$
\boxed{
H^*(\Omega\RP^n;\ZZ)
\cong
H^*(\Omega S^n;\ZZ)\times
H^*(\Omega S^n;\ZZ),
\qquad n\geq2.}
$$


::: pf-proof

Step [](#s1-5){.pf-ref} gives $\Omega\RP^n$ as the disjoint union of two components, each homotopy equivalent to $\Omega S^n$. Cohomology sends a finite disjoint union to the direct product of the component rings.

:::

:::

::: {.pf-step #s1-7}

If $n=2m+1$ is odd, then the component ring has the explicit presentation
$$
H^*(\Omega S^{2m+1};\ZZ)
\cong\Gamma_{mathbb Z}(z_{2m}),
$$
so
$$
\boxed{
H^*(\Omega\RP^{2m+1};\ZZ)
\cong\Gamma(z_{2m})\times\Gamma(z_{2m}).}
$$


::: pf-proof

Apply step [](#s1-3){.pf-ref} with $2n+1$ replaced by $2m+1$, then substitute into step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

For even $n$, the integral component ring is the graded shuffle algebra dual to the tensor Hopf algebra
$$
H_*(\Omega S^n;\ZZ)\cong T(t_{n-1});
$$
step [](#s1-6){.pf-ref} remains the complete reduction of the projective-space calculation to the standard sphere-loop calculation.


::: pf-proof

The James--Bott--Samelson calculation gives
$$
H_*(\Omega S^n;\ZZ)\cong T(\widetilde H_*(S^{n-1};\ZZ))=T(t_{n-1}).
$$
The cohomology ring is its graded Hopf dual, whose multiplication is the signed shuffle product. When $n$ is even, $\gradeddegree{t}=n-1$ is odd, so the Koszul signs are essential and the ring is not the ordinary divided-power algebra of step [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the ring for $\Omega\CP^n$, and steps [](#s1-5){.pf-ref} through [](#s1-8){.pf-ref} give the ring of $\Omega\RP^n$ componentwise, including the explicit odd-dimensional presentation.

:::

:::

:::
