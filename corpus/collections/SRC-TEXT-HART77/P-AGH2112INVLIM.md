---
schema: qual/card@1
id: P-AGH2112INVLIM
kind: problem
title: Inverse limits of sheaves are computed section by section
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Inverse Limits
  - Universal Properties
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.1.12 statement and source-order placement after II.1.11.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $\theset{\mcf_i}$ be an inverse system of sheaves on $X$.
Show that the presheaf $U \mapsto \varprojlim \mcf_i(U)$ is a sheaf.
It is called the **inverse limit** of the system and is denoted $\varprojlim \mcf_i$.
Show that it has the universal property of an inverse limit in the category of sheaves.
:::

::: {.solution}
Let
\[
\mcp(U)=\varprojlim_i\mcf_i(U).
\]
Thus an element of $\mcp(U)$ is a compatible tuple
\[
(s_i)_i,
\qquad
s_i\in\mcf_i(U),
\]
such that every transition map of the inverse system sends the appropriate component to the next one.  Restriction maps are defined componentwise.

::: pf

::: {.pf-step #s1}

The presheaf $\mcp$ satisfies local uniqueness.

::: pf-proof

Let
\[
U=\bigcup_{\alpha}U_\alpha
\]
be an open cover, and suppose
\[
s=(s_i)_i,
\qquad
t=(t_i)_i
\]
in $\mcp(U)$ have equal restrictions to every $U_\alpha$.

For every index $i$, this says
\[
s_i|_{U_\alpha}=t_i|_{U_\alpha}
\qquad
\text{for every }\alpha.
\]
Since $\mcf_i$ is a sheaf,
\[
s_i=t_i.
\]
This holds for every $i$, hence the tuples $s$ and $t$ are equal in $\mcp(U)$.

:::

:::

::: {.pf-step #s2}

The presheaf $\mcp$ satisfies gluing.

::: pf-proof

Let
\[
U=\bigcup_\alpha U_\alpha
\]
and suppose compatible local sections
\[
s_\alpha=(s_{\alpha,i})_i
\in\mcp(U_\alpha)
\]
are given.

Fix an index $i$.  Compatibility of the $s_\alpha$ on overlaps implies that the component sections
\[
s_{\alpha,i}\in\mcf_i(U_\alpha)
\]
agree on every $U_\alpha\cap U_\beta$.  Since $\mcf_i$ is a sheaf, they glue uniquely to
\[
s_i\in\mcf_i(U).
\]

It remains to check that the tuple $(s_i)_i$ is compatible with the transition maps.  Let
\[
\theta_{ji}:\mcf_j\longrightarrow\mcf_i
\]
be a transition morphism.  On every $U_\alpha$,
\[
\theta_{ji}(s_j)|_{U_\alpha}
=\theta_{ji}(s_{\alpha,j})
=s_{\alpha,i}
=s_i|_{U_\alpha},
\]
because each local tuple $s_\alpha$ already lies in the inverse limit.  The sheaf uniqueness axiom for $\mcf_i$ therefore gives
\[
\theta_{ji}(s_j)=s_i.
\]
Hence
\[
s=(s_i)_i\in\mcp(U).
\]
By construction, $s$ restricts to every $s_\alpha$.

:::

:::

::: {.pf-step #s3}

Therefore
\[
\boxed{
U\longmapsto\varprojlim_i\mcf_i(U)
}
\]
is already a sheaf.

::: pf-proof

Step [](#s1){.pf-ref} proves uniqueness and step [](#s2){.pf-ref} proves existence of glued sections for every open cover.  These are precisely the sheaf axioms.

:::

:::

::: pf-step

For every $i$, component projection defines a canonical sheaf morphism
\[
\pi_i:\mcp\longrightarrow\mcf_i,
\]
and the $\pi_i$ are compatible with the inverse system.

::: pf-proof

On each open set $U$, define
\[
\pi_i(U)((s_j)_j)=s_i.
\]
This commutes with restrictions because restrictions in $\mcp$ are componentwise.  Compatibility with transition maps is exactly the defining compatibility condition on inverse-limit tuples.

:::

:::

::: {.pf-step #s5}

Let $\mcg$ be a sheaf with a compatible family of morphisms
\[
\phi_i:\mcg\longrightarrow\mcf_i.
\]
There is a sheaf morphism
\[
\Phi:\mcg\longrightarrow\mcp
\]
defined by
\[
\boxed{
\Phi(U)(s)=(\phi_i(U)(s))_i.
}
\]

::: pf-proof

For $s\in\mcg(U)$, compatibility of the morphisms $\phi_i$ with the inverse system says exactly that the tuple
\[
(\phi_i(U)(s))_i
\]
belongs to
\[
\varprojlim_i\mcf_i(U)=\mcp(U).
\]

Each $\phi_i$ commutes with restriction, so the tuple-valued maps $\Phi(U)$ do as well.  Thus they define a morphism of sheaves
\[
\Phi:\mcg\to\mcp.
\]
By construction,
\[
\pi_i\circ\Phi=\phi_i
\]
for every $i$.

:::

:::

::: {.pf-step #s6}

The morphism $\Phi$ in step [](#s5){.pf-ref} is unique with this property.

::: pf-proof

Suppose
\[
\Psi:\mcg\longrightarrow\mcp
\]
also satisfies
\[
\pi_i\circ\Psi=\phi_i
\]
for every $i$.

For an open $U$ and a section $s\in\mcg(U)$, the $i$th component of $\Psi(U)(s)$ is
\[
\pi_i(U)(\Psi(U)(s))
=\phi_i(U)(s).
\]
Thus every component of $\Psi(U)(s)$ agrees with the corresponding component of $\Phi(U)(s)$, so
\[
\Psi(U)(s)=\Phi(U)(s).
\]
Hence $\Psi=\Phi$.

:::

:::

::: {.pf-step #s7}

Consequently, the sheaf $\mcp$ with its projections $\pi_i$ is the inverse limit in the category of sheaves:
\[
\boxed{
\varprojlim_i\mcf_i(U)
=
\left(\varprojlim_i\mcf_i\right)(U)
\quad\text{for every open }U.
}
\]

::: pf-proof

Steps [](#s5){.pf-ref} and [](#s6){.pf-ref} are exactly the existence and uniqueness clauses in the universal property of a categorical inverse limit.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves the sectionwise construction is a sheaf, and step [](#s7){.pf-ref} proves it is the inverse limit in sheaves.

:::

:::

:::
