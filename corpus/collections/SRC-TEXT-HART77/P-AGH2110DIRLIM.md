---
schema: qual/card@1
id: P-AGH2110DIRLIM
kind: problem
title: Direct limits of sheaves are the sheafification of the sectionwise limit
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Direct Limits
  - Universal Properties
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.1.10 statement and its source-order placement immediately after II.1.9.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $\theset{\mcf_i}$ be a direct system of sheaves and morphisms on $X$.
Define the direct limit of the system, denoted $\varinjlim \mcf_i$, to be the sheaf associated to the presheaf $U \mapsto \varinjlim \mcf_i(U)$.

Show that this is a direct limit in the category of sheaves on $X$: given a sheaf $\mcg$ and a collection of morphisms $\mcf_i \to \mcg$ compatible with the maps of the direct system, there exists a unique map $\varinjlim \mcf_i \to \mcg$ such that for each $i$ the original map $\mcf_i \to \mcg$ is the composite $\mcf_i \to \varinjlim \mcf_i \to \mcg$.
:::

::: {.solution}
Let
\[
\mcp(U)=\varinjlim_i\mcf_i(U)
\]
with restriction maps induced from those of the $\mcf_i$.  Thus $\mcp$ is the sectionwise direct-limit presheaf, and by definition
\[
\mcf:=\varinjlim_i\mcf_i=\mcp^+
\]
is its associated sheaf.  Write
\[
\eta:\mcp\longrightarrow\mcp^+
\]
for the sheafification map.

::: pf

::: {.pf-step #s1}

For every $i$ there is a canonical sheaf morphism
\[
\lambda_i:\mcf_i\longrightarrow\mcf.
\]
These morphisms are compatible with the transition maps of the direct system.

::: pf-proof

For every open $U\subseteq X$, the direct-limit maps give
\[
\mcf_i(U)\longrightarrow\varinjlim_j\mcf_j(U)=\mcp(U).
\]
These commute with restriction maps, so they define a presheaf morphism
\[
\mcf_i\longrightarrow\mcp.
\]
Composing with
\[
\eta:\mcp\longrightarrow\mcp^+=\mcf
\]
gives $\lambda_i$.  Compatibility follows sectionwise from compatibility of the canonical maps into a direct limit.

:::

:::

::: {.pf-step #s2}

Let $\mcg$ be a sheaf and suppose we are given compatible morphisms
\[
\phi_i:\mcf_i\longrightarrow\mcg.
\]
There is a unique presheaf morphism
\[
\phi:\mcp\longrightarrow\mcg
\]
whose composite with $\mcf_i\to\mcp$ is $\phi_i$ for every $i$.

::: pf-proof

Fix an open set $U\subseteq X$.  The maps on sections
\[
\phi_i(U):\mcf_i(U)\longrightarrow\mcg(U)
\]
are compatible with the direct system.  By the universal property of the direct limit in the category of groups, modules, or sets under consideration, there is a unique map
\[
\phi(U):\varinjlim_i\mcf_i(U)\longrightarrow\mcg(U)
\]
whose restriction to each $\mcf_i(U)$ is $\phi_i(U)$.

For an inclusion $V\subseteq U$, both composites
\[
\mcp(U)\rightrightarrows\mcg(V)
\]
obtained by restricting before or after $\phi$ agree on the image of every $\mcf_i(U)$, because each $\phi_i$ is a morphism of sheaves.  The direct-limit universal property therefore makes the two composites equal.  Hence the maps $\phi(U)$ assemble to a presheaf morphism $\phi:\mcp\to\mcg$.

Uniqueness also holds open set by open set by the same direct-limit universal property.

:::

:::

::: {.pf-step #s3}

The presheaf morphism $\phi$ factors uniquely through the sheafification:
\[
\boxed{
\begin{array}{ccc}
\mcp&\xrightarrow{\eta}&\mcf=\mcp^+\\
&\searrow_{\phi}&\downarrow{\scriptstyle\Phi}\\
&&\mcg,
\end{array}
}
\]
for a unique sheaf morphism
\[
\Phi:\mcf\longrightarrow\mcg.
\]

::: pf-proof

Sheafification is left adjoint to the inclusion of sheaves into presheaves.  Equivalently, for every presheaf $\mcp$ and every sheaf $\mcg$, composition with the sheafification map induces a bijection
\[
\operatorname{Hom}_{\mathrm{Sh}(X)}(\mcp^+,\mcg)
\xrightarrow{\sim}
\operatorname{Hom}_{\mathrm{PSh}(X)}(\mcp,\mcg).
\]
Apply this universal property to the presheaf morphism $\phi$ from step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

The morphism $\Phi$ satisfies
\[
\Phi\circ\lambda_i=\phi_i
\qquad
\text{for every }i.
\]

::: pf-proof

By step [](#s1){.pf-ref}, $\lambda_i$ is the composite
\[
\mcf_i\longrightarrow\mcp\xrightarrow{\eta}\mcf.
\]
By step [](#s3){.pf-ref},
\[
\Phi\circ\eta=\phi.
\]
Therefore
\[
\Phi\circ\lambda_i
=\phi\circ(\mcf_i\to\mcp)
=\phi_i
\]
by the defining property of $\phi$ in step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s5}

The morphism $\Phi$ is the unique sheaf morphism with the property in step [](#s4){.pf-ref}.

::: pf-proof

Suppose
\[
\Psi:\mcf\longrightarrow\mcg
\]
is another sheaf morphism satisfying
\[
\Psi\circ\lambda_i=\phi_i
\]
for every $i$.

Precompose with the sheafification map:
\[
\Psi\circ\eta:\mcp\longrightarrow\mcg.
\]
For every $i$, its composite with $\mcf_i\to\mcp$ is $\phi_i$.  By uniqueness in step [](#s2){.pf-ref},
\[
\Psi\circ\eta=\phi=\Phi\circ\eta.
\]
The sheafification universal property in step [](#s3){.pf-ref} then implies
\[
\Psi=\Phi.
\]

:::

:::

::: {.pf-step #s6}

Hence
\[
\boxed{
\mcf=\left(U\longmapsto\varinjlim_i\mcf_i(U)\right)^+
}
\]
with the maps $\lambda_i$ is the direct limit of the system $\{\mcf_i\}$ in the category of sheaves on $X$.

::: pf-proof

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} establish exactly the existence and uniqueness demanded by the categorical universal property of the colimit.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is the assertion of the exercise.

:::

:::

:::
