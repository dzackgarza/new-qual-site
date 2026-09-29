---
schema: qual/card@1
id: P-AMD-UDMVXK7S
kind: problem
title: Groups of order $pq$ with $p<q$ and $p\mid q-1$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Semidirect Products
  - Sylow Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 5, Exercise 2. Restored
    the requests to prove that there are precisely two isomorphism classes and
    to give and justify a presentation for the nonabelian class.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    The Sylow q-subgroup is unique, so every group is C_q semidirect C_p.
    Aut(C_q) is cyclic of order q-1. The trivial action gives C_pq, while every
    nontrivial action is injective with the same unique image of order p and
    differs only by an automorphism of C_p. Thus all nontrivial actions give
    one nonabelian isomorphism class. Its standard presentation is verified by
    normal forms and an explicit semidirect-product model of order pq.
---

::: {.problem}
Let $p<q$ be primes such that
\[
p\mid q-1.
\]
Prove that there are precisely two groups of order $pq$ up to isomorphism.
Find a presentation for the nonabelian group and justify that the presentation is correct.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every group $G$ of order $pq$ has a unique Sylow $q$-subgroup.

::: pf-proof

Let $n_q$ denote the number of Sylow $q$-subgroups.
Sylow's theorem gives
\[
n_q\equiv1\pmod q
\qquad\text{and}\qquad
n_q\mid p.
\]
Thus $n_q\in\{1,p\}$.
Since $p<q$, the value $p$ is not congruent to $1$ modulo $q$.
Therefore
\[
n_q=1.
\]
If $Q$ is the Sylow $q$-subgroup, then
\[
Q\normal G
\qquad\text{and}\qquad
Q\cong C_q.
\]

:::

:::

::: {.pf-step #s2}

Every group $G$ of order $pq$ is isomorphic to a semidirect product
\[
C_q\rtimes_\psi C_p
\]
for some homomorphism
\[
\psi:C_p\longrightarrow\operatorname{Aut}(C_q).
\]

::: pf-proof

Let $Q$ be the unique Sylow $q$-subgroup from step [](#s1){.pf-ref} and let $P$ be any Sylow $p$-subgroup.
Then
\[
|Q|=q,
\qquad
|P|=p,
\qquad
Q\cap P=\{1\}.
\]
Since $Q\normal G$, the product $QP$ is a subgroup, and
\[
|QP|=\frac{|Q||P|}{|Q\cap P|}=pq=|G|.
\]
Hence $G=QP$.
Conjugation by $P$ preserves $Q$ and defines a homomorphism
\[
\psi:P\longrightarrow\operatorname{Aut}(Q).
\]
The internal semidirect-product theorem gives
\[
G\cong Q\rtimes_\psi P.
\]
Since groups of prime order are cyclic,
\[
Q\cong C_q,
\qquad
P\cong C_p.
\]

:::

:::

::: {.pf-step #s3}

The group $\operatorname{Aut}(C_q)$ is cyclic of order $q-1$ and has a unique subgroup of order $p$.

::: pf-proof

Choose a generator $a$ of $C_q$.
Every automorphism is determined by
\[
a\longmapsto a^u
\]
for a unique $u\in(\mathbb Z/q\mathbb Z)^\times$, so
\[
\operatorname{Aut}(C_q)\cong(\mathbb Z/q\mathbb Z)^\times.
\]
The multiplicative group of the finite field $\mathbb F_q$ is cyclic of order $q-1$.
Thus $\operatorname{Aut}(C_q)$ is cyclic of order $q-1$.
Because $p\mid q-1$, a cyclic group of order $q-1$ has a unique subgroup of order $p$.

:::

:::

::: {.pf-step #s4}

The trivial action gives the cyclic group $C_{pq}$.

::: pf-proof

If $\psi$ is trivial, then the semidirect product is the direct product
\[
C_q\rtimes_\psi C_p=C_q\times C_p.
\]
Since $p$ and $q$ are coprime,
\[
C_q\times C_p\cong C_{pq}.
\]

:::

:::

::: {.pf-step #s5}

Every nontrivial homomorphism
\[
\psi:C_p\longrightarrow\operatorname{Aut}(C_q)
\]
is injective and has the same image.

::: pf-proof

The kernel of $\psi$ is a subgroup of the group $C_p$ of prime order.
If $\psi$ is nontrivial, its kernel cannot be all of $C_p$, so
\[
\ker\psi=\{1\}.
\]
Thus $\psi$ is injective and its image has order $p$.
By step [](#s3){.pf-ref}, $\operatorname{Aut}(C_q)$ has a unique subgroup of order $p$, so every nontrivial $\psi$ has that same image.

:::

:::

::: {.pf-step #s6}

All nontrivial actions give isomorphic semidirect products.

::: pf-proof

Let $P=C_p=\langle b\rangle$, and let
\[
U\le\operatorname{Aut}(C_q)
\]
be the unique subgroup of order $p$ from step [](#s3){.pf-ref}. Choose a generator $\tau$ of $U$ and let
\[
\psi_0(b)=\tau.
\]
For any nontrivial action $\psi$, step [](#s5){.pf-ref} gives $\operatorname{im}\psi=U$.
Hence
\[
\psi(b)=\tau^m
\]
for some $m$ with $1\le m<p$.
The map
\[
\rho_m:C_p\longrightarrow C_p,
\qquad
b\longmapsto b^m,
\]
is an automorphism, and
\[
\psi=\psi_0\circ\rho_m.
\]
Define
\[
F:C_q\rtimes_\psi C_p\longrightarrow C_q\rtimes_{\psi_0}C_p,
\qquad
F(h,k)=(h,\rho_m(k)).
\]
For $(h_1,k_1),(h_2,k_2)$ in the source,
\[
\begin{aligned}
F\bigl((h_1,k_1)(h_2,k_2)\bigr)
&=F\bigl(h_1\psi(k_1)(h_2),k_1k_2\bigr)\\
&=\bigl(h_1\psi_0(\rho_m(k_1))(h_2),\rho_m(k_1)\rho_m(k_2)\bigr)\\
&=F(h_1,k_1)F(h_2,k_2).
\end{aligned}
\]
Since $\rho_m$ is bijective, $F$ is bijective.
Therefore all nontrivial actions yield isomorphic semidirect products.

:::

:::

::: {.pf-step #s7}

Fix an integer $r$ whose residue class modulo $q$ has order $p$ in $(\mathbb Z/q\mathbb Z)^\times$.
Then the nontrivial semidirect product has presentation
\[
\left\langle a,b\ \middle|\ a^q=1,\ b^p=1,\ bab^{-1}=a^r\right\rangle.
\]

::: pf-proof

By step [](#s3){.pf-ref}, $(\mathbb Z/q\mathbb Z)^\times$ contains an element of order $p$; choose an integer representative $r$.
Let
\[
A=C_q=\langle a\rangle,
\qquad
B=C_p=\langle b\rangle,
\]
and define the action of $B$ on $A$ by
\[
bab^{-1}=a^r.
\]
This is well defined because the automorphism $a\mapsto a^r$ has order $p$.
Thus the resulting semidirect product
\[
S=C_q\rtimes C_p
\]
has order $pq$ and satisfies the three displayed relations.
Consequently the presented group
\[
\Gamma=\left\langle a,b\ \middle|\ a^q=1,\ b^p=1,\ bab^{-1}=a^r\right\rangle
\]
surjects onto $S$.

Conversely, the relation
\[
ba=a^r b
\]
allows every word in $a^{\pm1},b^{\pm1}$ to be rewritten with all powers of $a$ to the left and all powers of $b$ to the right.
Using $a^q=b^p=1$, every element of $\Gamma$ therefore has a representative
\[
a^i b^j,
\qquad
0\le i<q,
\quad
0\le j<p.
\]
Hence
\[
|\Gamma|\le pq.
\]
Since $\Gamma$ surjects onto the group $S$ of order $pq$,
\[
|\Gamma|\ge pq.
\]
Thus $|\Gamma|=pq$, and the surjection $\Gamma\to S$ is an isomorphism.
This proves that the presentation is correct.

:::

:::

::: {.pf-step #s8}

The semidirect product in step [](#s7){.pf-ref} is nonabelian.

::: pf-proof

The residue class of $r$ has order $p>1$, so
\[
r\not\equiv1\pmod q.
\]
Therefore
\[
bab^{-1}=a^r\ne a,
\]
so $a$ and $b$ do not commute.
Hence the group is nonabelian.

:::

:::

::: pf-step

There are precisely two groups of order $pq$ up to isomorphism.

::: pf-proof

By step [](#s2){.pf-ref}, every group of order $pq$ is determined up to isomorphism by an action of $C_p$ on $C_q$.
The trivial action gives the abelian group $C_{pq}$ by step [](#s4){.pf-ref}. Every nontrivial action gives the single nonabelian isomorphism class of step [](#s6){.pf-ref}, represented by the presentation in step [](#s7){.pf-ref}. The two classes are not isomorphic because one is abelian and the other is not by step [](#s8){.pf-ref}. Therefore there are exactly two isomorphism classes.

:::

:::

:::

:::
