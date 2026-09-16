---
schema: qual/card@1
id: P-MMAQ-M66PYTIML7
kind: problem
title: Classification of groups of order $182$
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Classification
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the full classification request and order 182 with Groups 1 in the retained source extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked existence of the normal cyclic subgroup of order 91, splitting by an involution, all four possible actions, and the characteristic-subgroup argument distinguishing their isomorphism classes."
---

::: {.problem}
Classify the groups of order $182 = 2 \cdot 7 \cdot 13$.
:::

::: {.solution}
There are exactly four isomorphism classes:
$$
C_{182},\qquad C_7\times D_{26},\qquad
D_{14}\times C_{13},\qquad D_{182},
$$
where $C_m$ is cyclic of order $m$ and $D_{2m}$ is the
dihedral group of order $2m$.

<1>1. Every group $G$ of order $182$ has a normal cyclic
subgroup $N$ of order $91$.

::: {.proof}
Sylow's theorems give $n_7\mid26$ and $n_7\equiv1\pmod7$
[@DF04]. Among $1,2,13,26$, only $1$ has this congruence.
Thus the Sylow $7$-subgroup $P$ is normal. The quotient
$G/P$ has order $26$. Its Sylow $13$-subgroup is unique,
since its number divides $2$ and is congruent to $1$
modulo $13$. Its inverse image $N$ is normal in $G$
and has order $7\cdot13=91$.

In $N$, the Sylow $13$-subgroup $Q$ is unique because its
number divides $7$ and is $1$ modulo $13$. The Sylow
$7$-subgroup is also unique, since its number divides
$13$ and $13\not\equiv1\pmod7$. Both are cyclic and
normal. Their intersection is trivial by Lagrange's theorem.
For $u\in P$ and $v\in Q$, normality puts
$uvu^{-1}v^{-1}$ in both subgroups, so they commute.
Multiplication therefore identifies $P\times Q$ with $N$:
it is a homomorphism with trivial kernel between groups of
order $91$. A pair of generators has order $91$, proving
that $N$ is cyclic.
:::

<1>2. Every such $G$ is obtained from $C_{91}$ by an
automorphism whose square is the identity, and exactly four qualify.

::: {.proof}
Cauchy's theorem gives an element $s\in G$ of order two
[@DF04]. Since $N$ has odd order, $s\notin N$.
As $[G:N]=2$, every element has a unique form $a^i s^e$,
where $a$ generates $N$, $i\in\mathbb Z/91\mathbb Z$,
and $e\in\{0,1\}$. Conjugation has the form
$sas^{-1}=a^u$ for a unit $u$ modulo $91$. The relation
$s^2=1$ forces $u^2\equiv1\pmod{91}$.

Modulo each of the primes $7$ and $13$, the equation
$(u-1)(u+1)=0$ forces $u=1$ or $u=-1$.
The Chinese remainder theorem gives one residue modulo
$91$ for each pair of signs [@DF04]. Thus the possibilities
are precisely
$$
(u\bmod7,u\bmod13)=(1,1),(1,-1),(-1,1),(-1,-1).
$$
Each is a unit and satisfies the required square equation.

Conversely, for any such $u$, define multiplication on
$(\mathbb Z/91\mathbb Z)\times(\mathbb Z/2\mathbb Z)$ by
$$
(i,e)(j,f)=(i+u^e j,e+f).
$$
This is well defined because $u^2=1$. Both ways of
associating a triple give first coordinate
$i+u^e j+u^{e+f}k$ and second coordinate $e+f+h$.
The identity is $(0,0)$ and the inverse of $(i,e)$ is
$(-u^{-e}i,-e)$. Hence this is a group of order $182$.
The rule $(i,e)\mapsto a^i s^e$ is an isomorphism onto
any $G$ with the given conjugation action.
:::

<1>3. The four actions give the displayed four groups,
and none of them are isomorphic to one another.

::: {.proof}
Identify $C_{91}$ with $C_7\times C_{13}$. The signs
in step <1>2 specify whether the involution fixes or
inverts each factor. Fixing both gives
$C_{91}\times C_2\cong C_{182}$. Inverting just one
gives the corresponding dihedral factor and the other
cyclic factor. Inverting both gives $D_{182}$, since
inversion on $C_7\times C_{13}$ is inversion on $C_{91}$.

To distinguish these groups intrinsically, observe that
$N$ is exactly the set of odd-order elements of $G$.
Elements of $N$ have odd order by Lagrange's theorem,
whereas an element outside $N$ has nontrivial image in
$G/N\cong C_2$ and therefore has even order. Thus any
isomorphism $G_u\to G_v$ takes $N_u$ to $N_v$.
With the generators of step <1>2, it must take
$a\mapsto b^k$ for a unit $k$ modulo $91$, and
$s\mapsto b^j t$ for some $j$. Since $N_v$ is abelian,
conjugation by $b^j t$ acts on $N_v$ in the same way as
conjugation by $t$. Applying the isomorphism to
$sas^{-1}=a^u$ therefore gives $b^{kv}=b^{ku}$.
Canceling the unit $k$ modulo $91$ yields $u=v$.
The four residues in step <1>2 are distinct, so the four
groups are pairwise nonisomorphic. The preceding steps
prove that the list is exhaustive.
:::
:::
