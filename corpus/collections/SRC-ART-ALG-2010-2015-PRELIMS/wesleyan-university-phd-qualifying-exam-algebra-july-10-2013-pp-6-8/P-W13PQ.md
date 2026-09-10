---
schema: qual/card@1
id: P-W13PQ
kind: problem
title: Sylow's theorem, and groups of order $pq$ are cyclic when $p \nmid q-1$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Cyclic Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked July 2013 Groups 1 on PDF page 6; the source explicitly has p not dividing q-1, a symbol lost in the retained text extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the full Sylow statement, both unique-subgroup deductions, commutation via the intersection, and the exact order of the cyclic generator."
---

::: problem
a. State all parts of Sylow's Theorem.

b. Show that if $0 < p < q$ are primes and $p \nmid q - 1$, then any group of order $pq$ is cyclic.
:::

::: solution
<1>1. Sylow's theorems have the following form.

Let $H$ be a finite group and let $\ell$ be prime. Write
$|H|=\ell^am$ with $\ell\nmid m$. A Sylow $\ell$-subgroup
is a subgroup of order $\ell^a$. Such subgroups exist.
Every $\ell$-subgroup is contained in a Sylow $\ell$-subgroup,
and any two Sylow $\ell$-subgroups are conjugate in $H$.
For a Sylow subgroup $S$, their number satisfies
$$
n_\ell=[H:N_H(S)],\qquad n_\ell\mid m,
\qquad n_\ell\equiv1\pmod\ell.
$$
In particular, $S$ is normal exactly when $n_\ell=1$ [@DF04].

<1>2. Under the hypotheses of part (b), both Sylow subgroups
of $G$ are normal.

::: proof
For the Sylow $q$-subgroups, one has $n_q\mid p$ and
$n_q\equiv1\pmod q$. Thus $n_q=1$ or $p$. Since $p<q$,
the latter is impossible. The Sylow $q$-subgroup $Q$ is unique.
Similarly $n_p=1$ or $q$ and $n_p\equiv1\pmod p$.
The hypothesis $p\nmid q-1$ rules out $n_p=q$, so the
Sylow $p$-subgroup $P$ is also unique. Uniqueness implies
normality because conjugation preserves subgroup orders.
:::

<1>3. The group $G$ is cyclic of order $pq$.

::: proof
Lagrange's theorem gives $P\cap Q=\{1\}$, since its order
divides both distinct primes. For $x\in P$ and $y\in Q$,
normality of both subgroups puts the commutator
$xyx^{-1}y^{-1}$ in $P\cap Q$. Thus $x$ and $y$ commute.
The multiplication map $P\times Q\to G$, $(x,y)\mapsto xy$,
is therefore a homomorphism. Its kernel is trivial, since
$xy=1$ forces $x=y^{-1}\in P\cap Q$. Both its domain and
codomain have order $pq$, so it is an isomorphism.

Each of $P,Q$ has prime order and is cyclic. If $x,y$ are
generators, then $(x,y)^d=1$ exactly when both $p$ and $q$
divide $d$, that is, exactly when $pq\mid d$. Hence $(x,y)$
has order $pq$, and its image generates $G$.
:::
:::
