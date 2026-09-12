---
schema: qual/card@1
id: P-EMAG7
kind: problem
title: Groups of orders $15$ and $30$
classification:
  areas:
  - algebra
  topics:
  - Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the request to classify all groups of both orders with Groups 7 in the retained Emory source extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the normal cyclic subgroup construction, all four actions modulo fifteen, existence of each multiplication law, and the distinct counts of involutions."
---

::: problem
Classify all groups of order 15 and of order 30.
:::

::: solution
Write $C_m=\mathbb Z/m\mathbb Z$, and let $D_{2m}$ denote
the dihedral group of order $2m$. There is one isomorphism
class of order $15$, namely $C_{15}$. There are four of
order $30$:
$$
C_{30},\qquad C_3\times D_{10},\qquad
D_6\times C_5,\qquad D_{30}.
$$

<1>1. Every group of order $15$ is cyclic.

::: proof
Sylow's theorems give $n_5\mid3$, $n_5\equiv1\pmod5$
and $n_3\mid5$, $n_3\equiv1\pmod3$ [@DF04]. The only
possibilities are $n_5=n_3=1$. Thus the subgroups $P,Q$
of orders $3,5$ are normal. Their intersection is trivial
because its order divides both primes. For $a\in P,b\in Q$,
the commutator $aba^{-1}b^{-1}$ lies in both subgroups
by normality and is therefore one. Hence multiplication
$P\times Q\to G$ is a homomorphism with trivial kernel.
Both groups have order $15$, so it is an isomorphism.
The prime-order factors are cyclic, and a pair of generators
has order $\operatorname{lcm}(3,5)=15$.
:::

<1>2. Every group $G$ of order $30$ has a normal cyclic
subgroup $N$ of order $15$ and an involution outside $N$.

::: proof
Act on the thirty-element set $G$ by left multiplication,
and compose the resulting permutation representation with
the sign homomorphism to obtain
$\varepsilon:G\to\{1,-1\}$ [@DF04]. By Cauchy's theorem
there is $t\in G$ of order two [@DF04]. The permutation
$x\mapsto tx$ has no fixed point, since $tx=x$ would give
$t=1$. Its cycles therefore consist of fifteen disjoint
transpositions, so $\varepsilon(t)=(-1)^{15}=-1$.
The homomorphism is onto and its kernel $N$ is normal
of order $15$. Step <1>1 makes $N$ cyclic. Also
$t\notin N$, and $\langle t\rangle\cap N=1$.
:::

<1>3. There are precisely four possibilities for the
multiplication in $G$.

::: proof
Let $a$ generate $N$. Since $[G:N]=2$, each element
is uniquely $a^i t^e$, where $i\in\mathbb Z/15\mathbb Z$
and $e\in\{0,1\}$. Normality gives $tat^{-1}=a^u$ for
a unit $u$ modulo $15$. Since $t^2=1$, one has
$u^2\equiv1\pmod{15}$. Modulo each prime $3,5$ this
means $u=1$ or $-1$. The Chinese remainder theorem
therefore gives exactly
$$
u=1,4,11,14\pmod{15}.
$$
The signs modulo $(3,5)$ are respectively
$(1,1),(1,-1),(-1,1),(-1,-1)$.

For each such $u$, multiplication on
$(\mathbb Z/15\mathbb Z)\times(\mathbb Z/2\mathbb Z)$ is
$$
(i,e)(j,f)=(i+u^e j,e+f).
$$
It is well defined because $u^2=1$. Both associations
of a product of $(i,e),(j,f),(k,h)$ give
$(i+u^e j+u^{e+f}k,e+f+h)$. The identity is $(0,0)$,
and the inverse of $(i,e)$ is $(-u^{-e}i,-e)$.
Thus each formula really defines a group of order $30$.
For any $G$ above the bijection $(i,e)\mapsto a^i t^e$
preserves this multiplication, so these possibilities
are exhaustive.

Under $C_{15}\cong C_3\times C_5$, the signs describe
which cyclic factors the involution inverts. The trivial
action gives $C_{30}$; inversion on the order-five
factor alone gives $C_3\times D_{10}$; inversion on the
order-three factor alone gives $D_6\times C_5$; and
inversion on both gives $D_{30}$. Here the usual dihedral
law is precisely $(i,e)(j,f)=(i+(-1)^e j,e+f)$.
:::

<1>4. These four groups are pairwise nonisomorphic.

::: proof
The odd-order subgroup $N$ contains no involution.
Outside $N$, the square of $(i,1)$ is $((1+u)i,0)$.
Since $(i,1)$ is never the identity, it has order two
exactly when $(1+u)i=0$ modulo $15$.
For $u=1$ this requires $i=0$, giving one involution.
For $u=4$ it requires $3\mid i$, giving five.
For $u=11$ it requires $5\mid i$, giving three.
For $u=14$ every $i$ works, giving fifteen.
An isomorphism preserves element orders. The different
involution counts $1,5,3,15$ therefore distinguish all
four groups, completing both classifications.
:::
:::
