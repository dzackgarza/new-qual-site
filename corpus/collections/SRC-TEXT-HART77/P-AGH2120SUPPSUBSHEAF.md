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

a. Show that the presheaf $V \mapsto \Gamma_{Z \intersect V}\qty{V, \ro{\mcf}{V}}$ is a sheaf.
It is called the **subsheaf of $\mcf$ with supports in $Z$** and is denoted $\mathcal{H}_Z^0(\mcf)$.

b. Let $U = X \sm Z$ and let $j: U \to X$ be the inclusion.
Show that there is an exact sequence of sheaves on $X$
\[
0 \to \mathcal{H}_Z^0(\mcf) \to \mcf \to j_*\qty{\ro{\mcf}{U}}.
\]
Furthermore, if $\mcf$ is flasque, show that the map $\mcf \to j_*\qty{\ro{\mcf}{U}}$ is surjective.
:::

::: {.solution}
For every open $V\subseteq X$, put
\[
\mathcal H(V)
=
\Gamma_{Z\cap V}(V,\mathcal F|_V)
=
\{s\in\mathcal F(V):\operatorname{supp}s\subseteq Z\cap V\}.
\]

<1>1. Restriction of sections makes $\mathcal H$ a subpresheaf of $\mathcal F$.
::: {.proof}
Let $W\subseteq V$ and let
\[
s\in\mathcal H(V).
\]
For every $P\in W\setminus Z$, the germ $s_P$ is zero because
\[
\operatorname{supp}s\subseteq Z\cap V.
\]
The germ of the restriction $s|_W$ at $P$ is the same germ $s_P$, hence is zero.  Therefore
\[
\operatorname{supp}(s|_W)\subseteq Z\cap W,
\]
so
\[
s|_W\in\mathcal H(W).
\]
Thus the restriction maps of $\mathcal F$ restrict to maps for $\mathcal H$.
:::

<1>2. The presheaf $\mathcal H$ satisfies the sheaf uniqueness axiom.
::: {.proof}
Let
\[
V=\bigcup_iV_i
\]
and let
\[
s,t\in\mathcal H(V)
\]
have equal restrictions to every $V_i$.  They are also sections of the sheaf $\mathcal F$, so the uniqueness axiom for $\mathcal F$ gives
\[
s=t.
\]
:::

<1>3. The presheaf $\mathcal H$ satisfies the sheaf gluing axiom.
::: {.proof}
Let
\[
V=\bigcup_iV_i
\]
and let compatible sections
\[
s_i\in\mathcal H(V_i)
\]
be given.  Since $\mathcal F$ is a sheaf, they glue uniquely to a section
\[
s\in\mathcal F(V).
\]

We must show
\[
\operatorname{supp}s\subseteq Z\cap V.
\]
Let
\[
P\in V\setminus Z.
\]
Choose $i$ with $P\in V_i$.  Because
\[
s_i\in\mathcal H(V_i),
\]
its germ at $P$ is zero:
\[
(s_i)_P=0.
\]
But
\[
s|_{V_i}=s_i,
\]
so
\[
s_P=(s_i)_P=0.
\]
Thus no point of $V\setminus Z$ belongs to the support of $s$, proving the required containment.
:::

<1>4. Hence $\mathcal H$ is a sheaf, denoted
\[
\boxed{\mathcal H_Z^0(\mathcal F).}
\]
::: {.proof}
Step <1>1 gives the presheaf structure, and <1>2--<1>3 give the two sheaf axioms.
:::

<1>5. Let
\[
U=X\setminus Z,
\qquad
j:U\hookrightarrow X.
\]
There is a natural restriction morphism
\[
\rho:\mathcal F\longrightarrow j_*(\mathcal F|_U).
\]
On an open set $V\subseteq X$, it is
\[
\rho_V:\mathcal F(V)
\longrightarrow
\mathcal F(V\cap U),
\qquad
s\longmapsto s|_{V\cap U}.
\]
::: {.proof}
Since $U$ is open,
\[
(j_*(\mathcal F|_U))(V)
=(\mathcal F|_U)(V\cap U)
=\mathcal F(V\cap U).
\]
The ordinary restriction maps of $\mathcal F$ therefore define the displayed morphism, and compatibility with further restrictions is automatic.
:::

<1>6. For every open $V\subseteq X$,
\[
\boxed{\ker\rho_V=\mathcal H_Z^0(\mathcal F)(V).}
\]
::: {.proof}
Suppose first that
\[
s\in\ker\rho_V.
\]
Then
\[
s|_{V\cap U}=0.
\]
Hence
\[
s_P=0
\]
for every $P\in V\cap U=V\setminus Z$.  Therefore
\[
\operatorname{supp}s\subseteq Z\cap V,
\]
so
\[
s\in\mathcal H_Z^0(\mathcal F)(V).
\]

Conversely, suppose
\[
s\in\mathcal H_Z^0(\mathcal F)(V).
\]
Then every germ of
\[
s|_{V\cap U}
\]
is zero.  A section of a sheaf whose germs are all zero is itself zero: each point has a neighborhood on which the section vanishes, and the sheaf uniqueness axiom glues these local zeroes.  Thus
\[
s|_{V\cap U}=0,
\]
so $s\in\ker\rho_V$.
:::

<1>7. Therefore there is an exact sequence of sheaves
\[
\boxed{
0
\longrightarrow
\mathcal H_Z^0(\mathcal F)
\longrightarrow
\mathcal F
\xrightarrow{\rho}
j_*(\mathcal F|_U).
}
\]
::: {.proof}
The first map is the inclusion of the subsheaf from <1>4.  Step <1>6 identifies its image on every open set with the kernel of $\rho$.  Hence the sequence is exact at the first two nonzero terms; equivalently, it is exact as a sequence of sheaves.
:::

<1>8. If $\mathcal F$ is flasque, then
\[
\rho:\mathcal F\longrightarrow j_*(\mathcal F|_U)
\]
is surjective.
::: {.proof}
Let $V\subseteq X$ be open.  The restriction map occurring in <1>5 is
\[
\mathcal F(V)
\longrightarrow
\mathcal F(V\cap U).
\]
Since
\[
V\cap U\subseteq V
\]
and $\mathcal F$ is flasque, this map is surjective.

Thus $\rho$ is in fact surjective on sections over every open $V$, and therefore certainly surjective as a morphism of sheaves.
:::

<1>9. In the flasque case the sequence of <1>7 extends to a short exact sequence
\[
\boxed{
0
\longrightarrow
\mathcal H_Z^0(\mathcal F)
\longrightarrow
\mathcal F
\longrightarrow
j_*(\mathcal F|_U)
\longrightarrow0.
}
\]
::: {.proof}
Combine exactness from <1>7 with the surjectivity in <1>8.
:::

<1>10. Q.E.D.
::: {.proof}
Steps <1>1--<1>4 prove part (a), <1>5--<1>7 prove the exact sequence in part (b), and <1>8--<1>9 prove its surjectivity assertion for flasque $\mathcal F$.
:::
:::
