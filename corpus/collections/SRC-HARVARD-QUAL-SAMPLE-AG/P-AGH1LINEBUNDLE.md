---
schema: qual/card@1
id: P-AGH1LINEBUNDLE
kind: problem
title: $H^1$ and line bundles
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Line Bundles
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Wodzicki's question on H^1 and line bundles.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
What is the connection between $H^1$ and line bundles?
:::

::: {.solution}
The basic connection is
\[
\boxed{
\operatorname{Pic}(X)
\cong
H^1(X,\mathcal O_X^\times).
}
\]

::: pf

::: {.pf-step #cocycle-from-bundle}
A line bundle determines a Čech $1$-cocycle with values in $\mathcal O_X^\times$.

::: pf-proof
Let $\mathcal L$ be an invertible sheaf and choose an open cover
\[
X=\bigcup_iU_i
\]
on which $\mathcal L$ is trivial.  Choose generators
\[
e_i\in\Gamma(U_i,\mathcal L)
\]
for those trivializations.

On each overlap $U_{ij}=U_i\cap U_j$, there is a unique unit
\[
g_{ij}\in\mathcal O_X^\times(U_{ij})
\]
such that
\[
e_i=g_{ij}e_j.
\]
On a triple overlap,
\[
e_i=g_{ij}g_{jk}e_k=g_{ik}e_k,
\]
so
\[
g_{ij}g_{jk}=g_{ik}.
\]
Thus $(g_{ij})$ is a Čech $1$-cocycle with values in $\mathcal O_X^\times$.
:::

:::

::: pf-step
Changing the local trivializations changes the cocycle by a coboundary.

::: pf-proof
Replace
\[
e_i
\]
by
\[
e_i'=u_ie_i,
\qquad
u_i\in\mathcal O_X^\times(U_i).
\]
Then
\[
e_i'
=u_ig_{ij}e_j
=u_ig_{ij}u_j^{-1}e_j',
\]
so the new transition function is
\[
g_{ij}'=u_ig_{ij}u_j^{-1}.
\]
This is exactly multiplication by the Čech coboundary of the $0$-cochain $(u_i)$.
Hence the cohomology class of $(g_{ij})$ depends only on the isomorphism class of $\mathcal L$.
:::

:::

::: {.pf-step #bundle-from-cocycle}
Conversely, a Čech $1$-cocycle with values in $\mathcal O_X^\times$ glues the trivial line bundles on the $U_i$ to a line bundle on $X$.

::: pf-proof
Start with
\[
\mathcal O_{U_i}e_i
\]
on each $U_i$.  On $U_{ij}$ identify
\[
e_i=g_{ij}e_j.
\]
The cocycle identity
\[
g_{ij}g_{jk}=g_{ik}
\]
is exactly the compatibility condition for these identifications on triple overlaps.  The sheaf-gluing theorem therefore produces an invertible sheaf $\mathcal L$ on $X$.

Replacing $(g_{ij})$ by a coboundary-equivalent cocycle changes the local bases by units and gives an isomorphic line bundle.
:::

:::

::: {.pf-step #pic-h1-iso}
The constructions in steps [](#cocycle-from-bundle){.pf-ref} and [](#bundle-from-cocycle){.pf-ref} are inverse and respect the group laws, giving
\[
\boxed{
\operatorname{Pic}(X)\cong H^1(X,\mathcal O_X^\times).
}
\]

::: pf-proof
Starting from a line bundle, extracting its transition functions and gluing them back recovers the original bundle.  Starting from a cocycle, gluing and then reading the transition functions recovers the same cohomology class.

If $\mathcal L$ and $\mathcal M$ have transition functions $g_{ij}$ and $h_{ij}$, then
\[
\mathcal L\otimes\mathcal M
\]
has transition functions
\[
g_{ij}h_{ij}.
\]
Thus tensor product in $\operatorname{Pic}(X)$ corresponds to addition in the abelian cohomology group $H^1(X,\mathcal O_X^\times)$.
:::

:::

::: {.pf-step #exponential-sequence}
On a complex manifold, the exponential sequence refines the relation:
\[
0\longrightarrow2\pi i\,\mathbb Z
\longrightarrow\mathcal O_X
\xrightarrow{\exp}\mathcal O_X^\times
\longrightarrow1.
\]
Its long exact sequence contains
\[
H^1(X,\mathcal O_X)
\longrightarrow
\operatorname{Pic}(X)
\xrightarrow{c_1}
H^2(X,\mathbb Z).
\]

::: pf-proof
The exponential map is locally surjective because every nowhere-vanishing holomorphic function has a local holomorphic logarithm.  Its kernel consists of the locally constant functions with values in $2\pi i\mathbb Z$, giving the short exact sequence of sheaves.

Taking sheaf cohomology and using step [](#pic-h1-iso){.pf-ref} to identify
\[
H^1(X,\mathcal O_X^\times)=\operatorname{Pic}(X)
\]
gives the displayed part of the long exact sequence.  The connecting homomorphism is the first Chern class.
:::

:::

::: {.pf-step #jacobian-identification}
For a compact Riemann surface,
\[
\operatorname{Pic}^0(X)
\cong
H^1(X,\mathcal O_X)
/H^1(X,2\pi i\mathbb Z),
\]
which is its Jacobian.

::: pf-proof
Because $X$ is compact and connected,
\[
H^0(X,\mathcal O_X)=\mathbb C,
\qquad
H^0(X,\mathcal O_X^\times)=\mathbb C^\times.
\]
The exponential map $\mathbb C\to\mathbb C^\times$ is surjective, so exactness of the exponential sequence shows that
\[
H^1(X,2\pi i\mathbb Z)
\longrightarrow
H^1(X,\mathcal O_X)
\]
is injective.

By exactness in step [](#exponential-sequence){.pf-ref}, the kernel of
\[
c_1:\operatorname{Pic}(X)\to H^2(X,\mathbb Z)
\]
is the image of $H^1(X,\mathcal O_X)$, with kernel equal to the image of $H^1(X,2\pi i\mathbb Z)$.  The kernel of $c_1$ is precisely the degree-zero component $\operatorname{Pic}^0(X)$.  Therefore the quotient has the displayed form.
:::

:::

::: pf-qed
Step [](#pic-h1-iso){.pf-ref} identifies $\operatorname{Pic}(X)$ with $H^1(X,\mathcal O_X^\times)$; steps [](#exponential-sequence){.pf-ref} and [](#jacobian-identification){.pf-ref} relate it to $H^1(X,\mathcal O_X)$ through the exponential sequence and identify $\operatorname{Pic}^0$ of a compact Riemann surface with its Jacobian.
:::

:::
:::
