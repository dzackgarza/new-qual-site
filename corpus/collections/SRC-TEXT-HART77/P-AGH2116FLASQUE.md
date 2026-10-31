---
schema: qual/card@1
id: P-AGH2116FLASQUE
kind: problem
title: Flasque sheaves and the exactness of sections
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Flasque Sheaves
  - Exact Sequences
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.1.16 statement and source-order placement after II.1.15.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
A sheaf $\mcf$ on a topological space $X$ is \dfn{flasque} if for every inclusion $V \subseteq U$ of open sets the restriction map $\mcf(U) \to \mcf(V)$ is surjective.

(a) Show that a constant sheaf on an irreducible topological space is flasque.

(b) If
$$
0 \to \mcf' \to \mcf \to \mcf'' \to 0
$$
is an exact sequence of sheaves and $\mcf'$ is flasque, then for any open set $U$ the sequence
$$
0 \to \mcf'(U) \to \mcf(U) \to \mcf''(U) \to 0
$$
of abelian groups is also exact.

(c) If
$$
0 \to \mcf' \to \mcf \to \mcf'' \to 0
$$
is an exact sequence of sheaves and $\mcf'$ and $\mcf$ are flasque, then $\mcf''$ is flasque.

(d) If $f: X \to Y$ is a continuous map and $\mcf$ is a flasque sheaf on $X$, then $f_* \mcf$ is a flasque sheaf on $Y$.

(e) Let $\mcf$ be any sheaf on $X$.
Define a new sheaf $\mcg$, called the sheaf of \dfn{discontinuous sections} of $\mcf$, as follows: for each open set $U \subseteq X$, let $\mcg(U)$ be the set of maps $s: U \to \Union_{P \in U} \mcf_P$ such that $s(P) \in \mcf_P$ for each $P \in U$.
Show that $\mcg$ is a flasque sheaf and that there is a natural injective morphism $\mcf \to \mcg$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

A constant sheaf on an irreducible topological space is flasque.

::: pf-proof

Let $A$ be an abelian group and let $\underline A$ denote the constant sheaf on an irreducible space $X$.

Every nonempty open subset $U\subseteq X$ is irreducible.  A section of $\underline A$ over $U$ is a locally constant map
$$
U\longrightarrow A
$$
with $A$ discrete.  Such a map must be constant: if it took a value $a$ and some other value, the preimage of $a$ and the preimage of $A \setminus \theset{a}$ would be disjoint nonempty open subsets of $U$, but any two nonempty open subsets of an irreducible space meet.

Hence
$$
\underline A(U)\cong A
$$
for every nonempty open $U$, and restriction between two nonempty opens is the identity on $A$.  Restriction to the empty set is also surjective.  Thus every restriction map is surjective, so $\underline A$ is flasque.

:::

:::

::: {.pf-step #s2}

Suppose
$$
0\longrightarrow\mcf'
\xrightarrow{\iota}
\mcf
\xrightarrow{q}
\mcf''
\longrightarrow0
$$
is exact and $\mcf'$ is flasque.  Then for every open $U\subseteq X$, the map
$$
q(U):\mcf(U)\longrightarrow\mcf''(U)
$$
is surjective.

::: pf-proof

Fix
$$
s''\in\mcf''(U).
$$
If $U=\varnothing$ there is nothing to prove, so assume $U\ne\varnothing$.

Consider pairs $(V,s)$ where $V\subseteq U$ is open and
$$
s\in\mcf(V)
$$
satisfies
$$
q(s)=s''\restrict_V.
$$
Order these pairs by extension:
$$
(V,s)\le (W,t)
$$
if $V\subseteq W$ and $t\restrict_V=s$.

The collection is nonempty.  Indeed, surjectivity of the map of stalks
$$
\mcf_P\to\mcf''_P
$$
at any $P\in U$ gives a germ lifting $s''_P$; represent that germ by a local section and shrink the neighborhood until its image equals $s''$ there.

Every chain has an upper bound: the domains form a nested family of opens, and the sections agree on inclusions by definition of the order, so the sheaf gluing axiom produces a section on their union.  Zorn's lemma therefore gives a maximal pair
$$
(V,s).
$$

We claim $V=U$.  Suppose not and choose
$$
P\in U\setminus V.
$$
As above, choose an open neighborhood $W\subseteq U$ of $P$ and
$$
t\in\mcf(W)
$$
with
$$
q(t)=s''\restrict_W.
$$

On $V\cap W$,
$$
q(t-s)=0.
$$
Exactness identifies the kernel sheaf of $q$ with $\mcf'$, so there is
$$
a\in\mcf'(V\cap W)
$$
whose image under $\iota$ is
$$
t\restrict_{V\cap W}-s\restrict_{V\cap W}.
$$

Because $\mcf'$ is flasque, extend $a$ to
$$
\widetilde a\in\mcf'(W).
$$
Replace $t$ by
$$
t'=t-\iota(\widetilde a).
$$
Then $q(t')=s''\restrict_W$ and
$$
t'\restrict_{V\cap W}=s\restrict_{V\cap W}.
$$
Hence $s$ and $t'$ glue to a section on
$$
V\cup W,
$$
still lifting $s''$.  Since $P\in W\setminus V$, this strictly enlarges the maximal pair, contradiction.

Therefore $V=U$, so $s''$ has a global lift in $\mcf(U)$.

:::

:::

::: {.pf-step #s3}

Under the hypotheses of step [](#s2){.pf-ref}, for every open $U$ the sequence
$$
\boxed{
0\longrightarrow\mcf'(U)
\longrightarrow\mcf(U)
\longrightarrow\mcf''(U)
\longrightarrow0
}
$$
is exact.

::: pf-proof

The global-section functor is always left exact, so exactness holds at the first two terms.  Step [](#s2){.pf-ref} supplies the missing surjectivity onto $\mcf''(U)$.

:::

:::

::: {.pf-step #s4}

If $\mcf'$ and $\mcf$ are flasque in an exact sequence
$$
0\to\mcf'\to\mcf\to\mcf''\to0,
$$
then $\mcf''$ is flasque.

::: pf-proof

Let $V\subseteq U$ be open and take
$$
s''\in\mcf''(V).
$$
By step [](#s3){.pf-ref} applied to the open $V$, lift $s''$ to
$$
s\in\mcf(V).
$$
Since $\mcf$ is flasque, extend $s$ to
$$
\widetilde s\in\mcf(U).
$$
Its image
$$
q(\widetilde s)\in\mcf''(U)
$$
restricts to $s''$.  Therefore
$$
\mcf''(U)\to\mcf''(V)
$$
is surjective for every inclusion $V\subseteq U$, so $\mcf''$ is flasque.

:::

:::

::: {.pf-step #s5}

If $f:X\to Y$ is continuous and $\mcf$ is flasque on $X$, then $f_*\mcf$ is flasque on $Y$.

::: pf-proof

For an open $U\subseteq Y$,
$$
(f_*\mcf)(U)=\mcf(f^{-1}(U)).
$$
If $V\subseteq U$, then
$$
f^{-1}(V)\subseteq f^{-1}(U).
$$
The restriction map
$$
(f_*\mcf)(U)
=\mcf(f^{-1}(U))
\longrightarrow
\mcf(f^{-1}(V))
=(f_*\mcf)(V)
$$
is therefore surjective by flasqueness of $\mcf$.

:::

:::

::: {.pf-step #s6}

The presheaf $\mcg$ of discontinuous sections is a sheaf.

::: pf-proof

For an open $U\subseteq X$,
$$
\mcg(U)
=\prod_{P\in U}\mcf_P
$$
as an abelian group: a section is simply a choice
$$
s(P)\in\mcf_P
$$
for every $P\in U$.  Restriction is literal restriction of the underlying function.

If such functions agree on overlaps of an open cover, they glue uniquely pointwise to a function on the union.  Thus the sheaf axioms hold.

:::

:::

::: {.pf-step #s7}

The sheaf $\mcg$ is flasque.

::: pf-proof

Let $V\subseteq U$ and
$$
s\in\mcg(V).
$$
Define
$$
\widetilde s(P)=
\begin{cases}
s(P),&P\in V,\\
0\in\mcf_P,&P\in U\setminus V.
\end{cases}
$$
This is an element of $\mcg(U)$ and restricts to $s$.  Hence every restriction map
$$
\mcg(U)\to\mcg(V)
$$
is surjective.

:::

:::

::: {.pf-step #s8}

There is a natural injective sheaf morphism
$$
\boxed{
\eta:\mcf\hookrightarrow\mcg,
\qquad
s\longmapsto(P\mapsto s_P).
}
$$

::: pf-proof

For each open $U$, define
$$
\eta_U(s)(P)=s_P.
$$
Taking germs commutes with restriction, so the $\eta_U$ define a morphism of sheaves.

Suppose
$$
\eta_U(s)=0.
$$
Then
$$
s_P=0
$$
for every $P\in U$.  For each $P$, equality of the germ with zero gives an open neighborhood $P\in U_P\subseteq U$ on which
$$
s\restrict_{U_P}=0.
$$
The $U_P$ cover $U$, so the uniqueness axiom for $\mcf$ gives
$$
s=0.
$$
Thus every $\eta_U$ is injective.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a), step [](#s3){.pf-ref} proves part (b), step [](#s4){.pf-ref} proves part (c), step [](#s5){.pf-ref} proves part (d), and steps [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref} prove part (e).

:::

:::

:::
