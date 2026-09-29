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
A sheaf $\mcf$ on a topological space $X$ is **flasque** if for every inclusion $V \subseteq U$ of open sets the restriction map $\mcf(U) \to \mcf(V)$ is surjective.

a. Show that a constant sheaf on an irreducible topological space is flasque.

b. If
\[
0 \to \mcf' \to \mcf \to \mcf'' \to 0
\]
is an exact sequence of sheaves and $\mcf'$ is flasque, then for any open set $U$ the sequence
\[
0 \to \mcf'(U) \to \mcf(U) \to \mcf''(U) \to 0
\]
of abelian groups is also exact.

c. If
\[
0 \to \mcf' \to \mcf \to \mcf'' \to 0
\]
is an exact sequence of sheaves and $\mcf'$ and $\mcf$ are flasque, then $\mcf''$ is flasque.

d. If $f: X \to Y$ is a continuous map and $\mcf$ is a flasque sheaf on $X$, then $f_* \mcf$ is a flasque sheaf on $Y$.

e. Let $\mcf$ be any sheaf on $X$.
Define a new sheaf $\mcg$, called the sheaf of **discontinuous sections** of $\mcf$, as follows: for each open set $U \subseteq X$, let $\mcg(U)$ be the set of maps $s: U \to \Union_{P \in U} \mcf_P$ such that $s(P) \in \mcf_P$ for each $P \in U$.
Show that $\mcg$ is a flasque sheaf and that there is a natural injective morphism $\mcf \to \mcg$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

A constant sheaf on an irreducible topological space is flasque.

::: pf-proof

Let $A$ be an abelian group and let $\underline A$ denote the constant sheaf on an irreducible space $X$.

Every nonempty open subset $U\subseteq X$ is irreducible.  A section of $\underline A$ over $U$ is a locally constant map
\[
U\longrightarrow A
\]
with $A$ discrete.  Such a map must be constant: if it took two distinct values, the inverse images of those values would give disjoint nonempty open subsets whose union disconnects the image partition, contradicting irreducibility.

Hence
\[
\underline A(U)\cong A
\]
for every nonempty open $U$, and restriction between two nonempty opens is the identity on $A$.  Restriction to the empty set is also surjective.  Thus every restriction map is surjective, so $\underline A$ is flasque.

:::

:::

::: {.pf-step #s2}

Suppose
\[
0\longrightarrow\mathcal F'
\xrightarrow{\iota}
\mathcal F
\xrightarrow{q}
\mathcal F''
\longrightarrow0
\]
is exact and $\mathcal F'$ is flasque.  Then for every open $U\subseteq X$, the map
\[
q(U):\mathcal F(U)\longrightarrow\mathcal F''(U)
\]
is surjective.

::: pf-proof

Fix
\[
s''\in\mathcal F''(U).
\]
If $U=\varnothing$ there is nothing to prove, so assume $U\ne\varnothing$.

Consider pairs $(V,s)$ where $V\subseteq U$ is open and
\[
s\in\mathcal F(V)
\]
satisfies
\[
q(s)=s''|_V.
\]
Order these pairs by extension:
\[
(V,s)\le (W,t)
\]
if $V\subseteq W$ and $t|_V=s$.

The collection is nonempty.  Indeed, surjectivity of the map of stalks
\[
\mathcal F_P\to\mathcal F''_P
\]
at any $P\in U$ gives a germ lifting $s''_P$; represent that germ by a local section and shrink the neighborhood until its image equals $s''$ there.

Every chain has an upper bound: the domains form a nested family of opens, and the sections agree on inclusions by definition of the order, so the sheaf gluing axiom produces a section on their union.  Zorn's lemma therefore gives a maximal pair
\[
(V,s).
\]

We claim $V=U$.  Suppose not and choose
\[
P\in U\setminus V.
\]
As above, choose an open neighborhood $W\subseteq U$ of $P$ and
\[
t\in\mathcal F(W)
\]
with
\[
q(t)=s''|_W.
\]

On $V\cap W$,
\[
q(t-s)=0.
\]
Exactness identifies the kernel sheaf of $q$ with $\mathcal F'$, so there is
\[
a\in\mathcal F'(V\cap W)
\]
whose image under $\iota$ is
\[
t|_{V\cap W}-s|_{V\cap W}.
\]

Because $\mathcal F'$ is flasque, extend $a$ to
\[
\widetilde a\in\mathcal F'(W).
\]
Replace $t$ by
\[
t'=t-\iota(\widetilde a).
\]
Then $q(t')=s''|_W$ and
\[
t'|_{V\cap W}=s|_{V\cap W}.
\]
Hence $s$ and $t'$ glue to a section on
\[
V\cup W,
\]
still lifting $s''$.  Since $P\in W\setminus V$, this strictly enlarges the maximal pair, contradiction.

Therefore $V=U$, so $s''$ has a global lift in $\mathcal F(U)$.

:::

:::

::: {.pf-step #s3}

Under the hypotheses of step [](#s2){.pf-ref}, for every open $U$ the sequence
\[
\boxed{
0\longrightarrow\mathcal F'(U)
\longrightarrow\mathcal F(U)
\longrightarrow\mathcal F''(U)
\longrightarrow0
}
\]
is exact.

::: pf-proof

The global-section functor is always left exact, so exactness holds at the first two terms.  Step [](#s2){.pf-ref} supplies the missing surjectivity onto $\mathcal F''(U)$.

:::

:::

::: {.pf-step #s4}

If $\mathcal F'$ and $\mathcal F$ are flasque in an exact sequence
\[
0\to\mathcal F'\to\mathcal F\to\mathcal F''\to0,
\]
then $\mathcal F''$ is flasque.

::: pf-proof

Let $V\subseteq U$ be open and take
\[
s''\in\mathcal F''(V).
\]
By step [](#s3){.pf-ref} applied to the open $V$, lift $s''$ to
\[
s\in\mathcal F(V).
\]
Since $\mathcal F$ is flasque, extend $s$ to
\[
\widetilde s\in\mathcal F(U).
\]
Its image
\[
q(\widetilde s)\in\mathcal F''(U)
\]
restricts to $s''$.  Therefore
\[
\mathcal F''(U)\to\mathcal F''(V)
\]
is surjective for every inclusion $V\subseteq U$, so $\mathcal F''$ is flasque.

:::

:::

::: {.pf-step #s5}

If $f:X\to Y$ is continuous and $\mathcal F$ is flasque on $X$, then $f_*\mathcal F$ is flasque on $Y$.

::: pf-proof

For an open $U\subseteq Y$,
\[
(f_*\mathcal F)(U)=\mathcal F(f^{-1}(U)).
\]
If $V\subseteq U$, then
\[
f^{-1}(V)\subseteq f^{-1}(U).
\]
The restriction map
\[
(f_*\mathcal F)(U)
=\mathcal F(f^{-1}(U))
\longrightarrow
\mathcal F(f^{-1}(V))
=(f_*\mathcal F)(V)
\]
is therefore surjective by flasqueness of $\mathcal F$.

:::

:::

::: {.pf-step #s6}

The presheaf $\mathcal G$ of discontinuous sections is a sheaf.

::: pf-proof

For an open $U\subseteq X$,
\[
\mathcal G(U)
=\prod_{P\in U}\mathcal F_P
\]
as an abelian group: a section is simply a choice
\[
s(P)\in\mathcal F_P
\]
for every $P\in U$.  Restriction is literal restriction of the underlying function.

If such functions agree on overlaps of an open cover, they glue uniquely pointwise to a function on the union.  Thus the sheaf axioms hold.

:::

:::

::: {.pf-step #s7}

The sheaf $\mathcal G$ is flasque.

::: pf-proof

Let $V\subseteq U$ and
\[
s\in\mathcal G(V).
\]
Define
\[
\widetilde s(P)=
\begin{cases}
s(P),&P\in V,\\
0\in\mathcal F_P,&P\in U\setminus V.
\end{cases}
\]
This is an element of $\mathcal G(U)$ and restricts to $s$.  Hence every restriction map
\[
\mathcal G(U)\to\mathcal G(V)
\]
is surjective.

:::

:::

::: {.pf-step #s8}

There is a natural injective sheaf morphism
\[
\boxed{
\eta:\mathcal F\hookrightarrow\mathcal G,
\qquad
s\longmapsto(P\mapsto s_P).
}
\]

::: pf-proof

For each open $U$, define
\[
\eta_U(s)(P)=s_P.
\]
Taking germs commutes with restriction, so the $\eta_U$ define a morphism of sheaves.

Suppose
\[
\eta_U(s)=0.
\]
Then
\[
s_P=0
\]
for every $P\in U$.  For each $P$, equality of the germ with zero gives an open neighborhood $P\in U_P\subseteq U$ on which
\[
s|_{U_P}=0.
\]
The $U_P$ cover $U$, so the uniqueness axiom for $\mathcal F$ gives
\[
s=0.
\]
Thus every $\eta_U$ is injective.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a), step [](#s3){.pf-ref} proves part (b), step [](#s4){.pf-ref} proves part (c), step [](#s5){.pf-ref} proves part (d), and steps [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref} prove part (e).

:::

:::

:::
