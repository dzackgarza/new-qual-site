---
schema: qual/card@1
id: P-O84SY
kind: problem
title: A group of order $84$ with $28$ Sylow $3$-subgroups has a normal Sylow $7$-subgroup
  $K$ with $|Z_G(K)|=28$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Centralizers and Normalizers
  - Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared all five parts with Summer 2014 problem 2 in the retained source extraction, including the required centralizer order 28."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the complete Sylow counts and cyclic automorphism group, the order-3 centralizer obstruction, and the characteristic involution that rules out centralizer order 14."
---

::: problem
Let $G$ be a finite group of order 84 with 28 Sylow $3$-subgroups.
For any subgroup $H$ of $G$, let $N_G(H)$ and $Z_G(H)$ be the normalizer and the centralizer of $H$ in $G$, respectively.

a. Show that $G$ has a normal Sylow $7$-subgroup.
Let $K$ denote this subgroup.
Describe $\mathrm{Aut}(K)$, the automorphism group of $K$.

b. Show that $Z_G(K)$ is a normal subgroup of $G$, and that $G/Z_G(K)$ is cyclic.
(Note: since $K$ is normal in $G$, $G$ acts on $K$ by conjugation.)

c. Let $Q$ be a Sylow $3$-subgroup of $G$.
Show that $N_G(Q) = Z_G(Q) = Q$.

d. Show that $|Z_G(K)|$ is not divisible by $3$.

e. Prove that $Z_G(K)$ must have order $28$.
:::

::: solution
Write $C=Z_G(K)$. We use $Z_G(H)$ for the elements of $G$
commuting with every element of $H$.

<1>1. The Sylow $7$-subgroup $K$ is normal and
$\operatorname{Aut}(K)\cong C_6$.

::: proof
Sylow's theorems give $n_7\mid12$ and $n_7\equiv1\pmod7$
[@DF04]. Among $1,2,3,4,6,12$, only $1$ has that congruence,
so $K$ is unique and therefore normal. It has order $7$ and
is cyclic; fix a generator $k$.

An automorphism must send $k$ to one of the six generators
$k^j$, $1\leq j\leq6$. Conversely each such assignment defines
an automorphism. Composition multiplies exponents modulo $7$,
giving $\operatorname{Aut}(K)\cong(\mathbb Z/7\mathbb Z)^\times$.
The successive powers of $3$ modulo $7$ are
$3,2,6,4,5,1$, so this group is cyclic of order $6$.
:::

<1>2. The subgroup $C$ is normal and $G/C$ is cyclic of order
dividing $6$.

::: proof
Normality of $K$ makes conjugation a homomorphism
$$
\theta:G\longrightarrow\operatorname{Aut}(K),\qquad
\theta(g)(k)=gkg^{-1}.
$$
Its kernel consists exactly of the elements commuting with all
of $K$, so $\ker\theta=C$. A kernel is normal. The first
isomorphism theorem identifies $G/C$ with a subgroup of the
cyclic group of order $6$ found in step <1>1 [@DF04].
:::

<1>3. For every Sylow $3$-subgroup $Q$,
$N_G(Q)=Z_G(Q)=Q$.

::: proof
Conjugation is transitive on the Sylow $3$-subgroups, and the
stabilizer of $Q$ is $N_G(Q)$. Thus
$[G:N_G(Q)]=n_3=28$, giving $|N_G(Q)|=84/28=3$.
Since $Q\subseteq N_G(Q)$ and $|Q|=3$, the normalizer is $Q$.
The cyclic group $Q$ centralizes itself, while any element
centralizing $Q$ normalizes it. Therefore
$Q\subseteq Z_G(Q)\subseteq N_G(Q)=Q$.
:::

<1>4. The integer $|C|$ is not divisible by $3$.

::: proof
Otherwise Cauchy's theorem would give $q\in C$ of order $3$
[@DF04]. Its subgroup $Q=\langle q\rangle$ would be Sylow in
$G$. Since $q$ commutes with every element of $K$, so does each
power of $q$, and hence $K\subseteq Z_G(Q)$. Step <1>3 would
then give $K\subseteq Q$, impossible for groups of orders $7$
and $3$.
:::

<1>5. The centralizer $C$ has order $28$.

::: proof
Put $d=[G:C]$. Step <1>2 gives $d\mid6$, and
$84=d|C|$. Step <1>4 forces $3\mid d$, so $d=3$ or $6$.
Consequently $|C|=28$ or $14$.

Suppose $|C|=14$. The abelian subgroup $K$ lies in $C$, and
the definition of $C$ gives $K\subseteq Z(C)$. The quotient
$C/K$ has order $2$ and is cyclic. Choose $z\in C$ whose
coset generates it. Every element of $C$ is $kz^j$ for some
$k\in K$ and integer $j$. Since $K$ is central, any two such
elements commute. Thus $C$ is abelian.

In this abelian group, all Sylow $2$-subgroups are normal, so
Sylow conjugacy implies there is exactly one. It has order $2$;
write it as $\{1,t\}$. The element $t$ is the unique element
of order $2$ in $C$. Since $C\lhd G$, conjugation by any
$g\in G$ permutes the elements of $C$ preserving their orders.
It must therefore fix $t$. Thus $t\in Z(G)$.

For a Sylow $3$-subgroup $Q$, this implies
$t\in Z_G(Q)=Q$ by step <1>3. An element of order $2$ cannot
belong to a group of order $3$. This contradiction excludes
$|C|=14$, leaving $|C|=28$ as required.
:::
:::
