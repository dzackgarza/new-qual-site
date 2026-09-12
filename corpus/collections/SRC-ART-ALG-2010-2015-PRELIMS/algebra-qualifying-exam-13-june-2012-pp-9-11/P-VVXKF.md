---
schema: qual/card@1
id: P-VVXKF
kind: problem
title: Sylow subgroup counts and exclusion of proper subgroups of index at most four
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked June 2012 Groups 1 on retained PDF page 9; the source also omits proper in part (b). Corrected the subject to algebra and made the necessary qualification explicit."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked all stated Sylow-count consequences and the faithful coset action, including why a proper subgroup makes the kernel proper and why infinite simple groups are also excluded."
---

::: {.problem}
a. Let $G$ be a finite group of order $p^k m$ where $p$ is prime and $(p,m) = 1$.
Let $n_p$ be the number of subgroups of $G$ of order $p^k$.
State as many facts as you can about the value of $n_p$.
(No proofs are required for your answers in this part.)

b. Show that a non-abelian simple group $G$ has no proper subgroup of index $\leq 4$.

(You may assume without proof that the alternating group $A_5$ is the smallest non-abelian simple group.)
:::

::: remark
The proper-subgroup qualification in part (b) is necessary:
every group is a subgroup of itself of index $1$. Thus
the nontrivial assertion excludes indices $2,3,4$.
:::

::: solution
<1>1. For part (a), the Sylow count satisfies
$$
1\leq n_p\leq m,\qquad n_p\mid m,\qquad
n_p\equiv1\pmod p.
$$
For any Sylow $p$-subgroup $P$, one also has
$$
n_p=[G:N_G(P)].
$$
Moreover, $n_p=1$ if and only if $G$ has a normal Sylow
$p$-subgroup. In that case this Sylow subgroup is
characteristic. If $n_p>1$, then $n_p\geq p+1$.

::: proof
Existence, conjugacy, divisibility, and the congruence are
the Sylow theorems [@DF04]. The bound $n_p\leq m$
follows from the positive divisibility $n_p\mid m$.
Conjugation acts transitively on the Sylow subgroups,
and the stabilizer of $P$ is its normalizer $N_G(P)$;
the orbit-stabilizer formula gives the displayed index.

A unique Sylow subgroup is fixed by all conjugations,
so is normal. Conversely, normality makes its
conjugacy orbit a singleton, and Sylow conjugacy then
gives uniqueness. Every automorphism of $G$ preserves
subgroup orders and therefore permutes the Sylow
$p$-subgroups; a unique one is consequently
characteristic. Finally, a positive integer larger
than $1$ and congruent to $1$ modulo $p$ is at least
$p+1$.
:::

<1>2. A nonabelian simple group has no proper subgroup
of index at most $4$.

::: proof
Suppose $H<G$ has finite index $n\leq4$. Properness
implies $2\leq n\leq4$. The action on the left cosets
defines a homomorphism
$$
\rho:G\longrightarrow\operatorname{Sym}(G/H)\cong S_n,
\qquad \rho(g)(aH)=gaH.
$$
Its kernel is a normal subgroup of $G$. It is not all
of $G$: if $g\notin H$, then $\rho(g)$ moves the
coset $H$ to the different coset $gH$. Simplicity
therefore makes the kernel trivial.

Thus $G$ embeds in $S_n$, so it is finite and
$|G|\leq n!\leq24$. The permitted fact that $A_5$
is the smallest nonabelian simple group gives instead
$|G|\geq|A_5|=5!/2=60$, a contradiction. The argument
does not assume beforehand that the simple group is
finite; finiteness follows from the faithful action.
:::
:::
