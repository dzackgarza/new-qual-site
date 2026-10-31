---
schema: qual/card@1
id: P-AGH2120SUPPSUBSHEAF
kind: problem
title: The subsheaf of sections supported in a closed subset
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Support
  - Flasque Sheaves
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.1.20 statement and source-order placement after II.1.19.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $Z$ be a closed subset of $X$ and let $\mcf$ be a sheaf on $X$.
Define $\Gamma_Z(X, \mcf)$ to be the subgroup of $\Gamma(X, \mcf)$ consisting of all sections whose support is contained in $Z$.

(a) Show that the presheaf $V \mapsto \Gamma_{Z \intersect V}\qty{V, \restrictionof{\mcf}{V}}$ is a sheaf.
It is called the \dfn{subsheaf of $\mcf$ with supports in $Z$} and is denoted $\mch_Z^0(\mcf)$.

(b) Let $U = X \sm Z$ and let $j: U \to X$ be the inclusion.
Show that there is an exact sequence of sheaves on $X$
$$
0 \to \mch_Z^0(\mcf) \to \mcf \to j_*\qty{\restrictionof{\mcf}{U}}.
$$
Furthermore, if $\mcf$ is flasque, show that the map $\mcf \to j_*\qty{\restrictionof{\mcf}{U}}$ is surjective.
:::

::: {.solution}
For every open $V\subseteq X$, put
$$
\mch(V)
=
\Gamma_{Z\cap V}(V,\mcf\restrict_V)
=
\{s\in\mcf(V) \st \supp s\subseteq Z\cap V\}.
$$

::: pf

::: {.pf-step #s1}

Restriction of sections makes $\mch$ a subpresheaf of $\mcf$.

::: pf-proof

Let $W\subseteq V$ and let
$$
s\in\mch(V).
$$
For every $P\in W\setminus Z$, the germ $s_P$ is zero because
$$
\supp s\subseteq Z\cap V.
$$
The germ of the restriction $s\restrict_W$ at $P$ is the same germ $s_P$, hence is zero.  Therefore
$$
\supp (s\restrict_W)\subseteq Z\cap W,
$$
so
$$
s\restrict_W\in\mch(W).
$$
Thus the restriction maps of $\mcf$ restrict to maps for $\mch$.

:::

:::

::: {.pf-step #s2}

The presheaf $\mch$ satisfies the sheaf uniqueness axiom.

::: pf-proof

Let
$$
V=\bigcup_iV_i
$$
and let
$$
s,t\in\mch(V)
$$
have equal restrictions to every $V_i$.  They are also sections of the sheaf $\mcf$, so the uniqueness axiom for $\mcf$ gives
$$
s=t.
$$

:::

:::

::: {.pf-step #s3}

The presheaf $\mch$ satisfies the sheaf gluing axiom.

::: pf-proof

Let
$$
V=\bigcup_iV_i
$$
and let compatible sections
$$
s_i\in\mch(V_i)
$$
be given.  Since $\mcf$ is a sheaf, they glue uniquely to a section
$$
s\in\mcf(V).
$$

We must show
$$
\supp s\subseteq Z\cap V.
$$
Let
$$
P\in V\setminus Z.
$$
Choose $i$ with $P\in V_i$.  Because
$$
s_i\in\mch(V_i),
$$
its germ at $P$ is zero:
$$
(s_i)_P=0.
$$
But
$$
s\restrict_{V_i}=s_i,
$$
so
$$
s_P=(s_i)_P=0.
$$
Thus no point of $V\setminus Z$ belongs to the support of $s$, proving the required containment.

:::

:::

::: {.pf-step #s4}

Hence $\mch$ is a sheaf, denoted
$$
\boxed{\mch_Z^0(\mcf).}
$$

::: pf-proof

Step [](#s1){.pf-ref} gives the presheaf structure, and steps [](#s2){.pf-ref} and [](#s3){.pf-ref} give the two sheaf axioms.

:::

:::

::: {.pf-step #s5}

Let
$$
U=X\setminus Z,
\qquad
j:U\hookrightarrow X.
$$
There is a natural restriction morphism
$$
\rho:\mcf\longrightarrow j_*(\mcf\restrict_U).
$$
On an open set $V\subseteq X$, it is
$$
\rho_V:\mcf(V)
\longrightarrow
\mcf(V\cap U),
\qquad
s\longmapsto s\restrict_{V\cap U}.
$$

::: pf-proof

Since $U$ is open,
$$
(j_*(\mcf\restrict_U))(V)
=(\mcf\restrict_U)(V\cap U)
=\mcf(V\cap U).
$$
The ordinary restriction maps of $\mcf$ therefore define the displayed morphism, and compatibility with further restrictions is automatic.

:::

:::

::: {.pf-step #s6}

For every open $V\subseteq X$,
$$
\boxed{\ker\rho_V=\mch_Z^0(\mcf)(V).}
$$

::: pf-proof

Suppose first that
$$
s\in\ker\rho_V.
$$
Then
$$
s\restrict_{V\cap U}=0.
$$
Hence
$$
s_P=0
$$
for every $P\in V\cap U=V\setminus Z$.  Therefore
$$
\supp s\subseteq Z\cap V,
$$
so
$$
s\in\mch_Z^0(\mcf)(V).
$$

Conversely, suppose
$$
s\in\mch_Z^0(\mcf)(V).
$$
Then every germ of
$$
s\restrict_{V\cap U}
$$
is zero.  A section of a sheaf whose germs are all zero is itself zero: each point has a neighborhood on which the section vanishes, and the sheaf uniqueness axiom glues these local zeroes.  Thus
$$
s\restrict_{V\cap U}=0,
$$
so $s\in\ker\rho_V$.

:::

:::

::: {.pf-step #s7}

Therefore there is an exact sequence of sheaves
$$
\boxed{
0
\longrightarrow
\mch_Z^0(\mcf)
\longrightarrow
\mcf
\xrightarrow{\rho}
j_*(\mcf\restrict_U).
}
$$

::: pf-proof

The first map is the inclusion of the subsheaf from step [](#s4){.pf-ref}.  Step [](#s6){.pf-ref} identifies its image on every open set with the kernel of $\rho$.  Hence the sequence is exact at the first two nonzero terms; equivalently, it is exact as a sequence of sheaves.

:::

:::

::: {.pf-step #s8}

If $\mcf$ is flasque, then
$$
\rho:\mcf\longrightarrow j_*(\mcf\restrict_U)
$$
is surjective.

::: pf-proof

Let $V\subseteq X$ be open.  The restriction map occurring in step [](#s5){.pf-ref} is
$$
\mcf(V)
\longrightarrow
\mcf(V\cap U).
$$
Since
$$
V\cap U\subseteq V
$$
and $\mcf$ is flasque, this map is surjective.

Thus $\rho$ is in fact surjective on sections over every open $V$, and therefore certainly surjective as a morphism of sheaves.

:::

:::

::: {.pf-step #s9}

In the flasque case the sequence of step [](#s7){.pf-ref} extends to a short exact sequence
$$
\boxed{
0
\longrightarrow
\mch_Z^0(\mcf)
\longrightarrow
\mcf
\longrightarrow
j_*(\mcf\restrict_U)
\longrightarrow0.
}
$$

::: pf-proof

Combine exactness from step [](#s7){.pf-ref} with the surjectivity in step [](#s8){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove part (a), steps [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} prove the exact sequence in part (b), and steps [](#s8){.pf-ref} and [](#s9){.pf-ref} prove its surjectivity assertion for flasque $\mcf$.

:::

:::

:::
