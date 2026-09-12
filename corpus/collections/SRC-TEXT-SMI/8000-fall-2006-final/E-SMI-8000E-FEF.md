---
schema: qual/card@1
id: E-SMI-8000E-FEF
kind: problem
title: Proof choice — existence of algebraic closures or embedding into algebraically closed fields
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared both proof choices with Smith 8000 Fall 2006 final part F; solved option (ii)."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Used Zorn's lemma on partial k-embeddings L→F and extended a maximal embedding across one algebraic element by sending it to a root of the transported minimal polynomial in the algebraically closed field F."
---

::: {.exercise}
Prove one:

(i) Every field $k$ has an algebraic closure;

or

(ii) If $E$ is an algebraic field extension of $k$ (not necessarily finite), and $F$ is an algebraically closed field containing $k$, there is a field homomorphism $E \to F$ which is the identity on $k$.
:::

::: solution
We prove option (ii).

<1>1. Partially order all partial $k$-embeddings of subfields of $E$ into $F$.
::: proof
Let $\mathcal P$ be the set of pairs $(L,\varphi)$ such that
$$
k\subseteq L\subseteq E
$$
is an intermediate field and
$$
\varphi:L\longrightarrow F
$$
is a field homomorphism restricting to the identity on $k$.

The set is nonempty because $(k,\operatorname{id}_k)\in\mathcal P$. Order
$\mathcal P$ by extension:
$$
(L,\varphi)\le (L',\varphi')
$$
if $L\subseteq L'$ and $\varphi'|_L=\varphi$.
:::

<1>2. Every chain has an upper bound.
::: proof
Let
$$
\{(L_i,\varphi_i)\}_{i\in I}
$$
be a chain. Put
$$
L=\bigcup_{i\in I}L_i.
$$
Because the $L_i$ are totally ordered by inclusion, $L$ is a field. Define
$$
\varphi:L\longrightarrow F
$$
by choosing $i$ with $x\in L_i$ and setting
$$
\varphi(x)=\varphi_i(x).
$$
This is well-defined: if $x\in L_i\cap L_j$, one of the two partial
embeddings extends the other, so they agree on $x$. The same chain argument
shows that $\varphi$ respects addition and multiplication. It fixes $k$, so
$(L,\varphi)$ is an upper bound for the chain.

By Zorn's lemma, $\mathcal P$ has a maximal element, say
$$
(L,\varphi).
$$
:::

<1>3. A maximal partial embedding must already be defined on all of $E$.
::: proof
Suppose instead that $L\ne E$, and choose
$$
\alpha\in E\setminus L.
$$
Because $E/k$ is algebraic, $\alpha$ is algebraic over $k$, hence also over
$L$. Let
$$
m(X)\in L[X]
$$
be the minimal polynomial of $\alpha$ over $L$.

Apply $\varphi$ to the coefficients of $m$ to obtain
$$
m^\varphi(X)\in\varphi(L)[X]\subseteq F[X].
$$
Since $F$ is algebraically closed, $m^\varphi$ has a root
$$
\beta\in F.
$$

The coefficient map $\varphi:L\to F$ together with $X\mapsto\beta$ gives a
homomorphism
$$
L[X]\longrightarrow F.
$$
Its kernel contains $(m)$ because $m^\varphi(\beta)=0$. Since $m$ is
irreducible, the quotient
$$
L[X]/(m)\cong L(\alpha)
$$
is a field. The induced homomorphism
$$
\widetilde\varphi:L(\alpha)\longrightarrow F
$$
is nonzero, hence injective, and extends $\varphi$. It also fixes $k$.
Thus
$$
(L,\varphi)<(L(\alpha),\widetilde\varphi),
$$
contradicting maximality.

Therefore $L=E$.
:::

<1>4. Conclude the required embedding exists.
::: proof
The maximal map from step <1>2 is therefore a field homomorphism
$$
\boxed{\varphi:E\longrightarrow F}
$$
whose restriction to $k$ is the identity.
:::
:::
