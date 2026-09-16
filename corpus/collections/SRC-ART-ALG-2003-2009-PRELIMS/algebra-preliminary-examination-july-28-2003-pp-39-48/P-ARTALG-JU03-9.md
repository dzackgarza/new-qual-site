---
schema: qual/card@1
id: P-ARTALG-JU03-9
kind: problem
title: 'Solvability of $S_4$, quartics, and a quintic counterexample'
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared all three solvability questions, both polynomial degrees, and both negative assertions with July 2003 problem 9 in the retained source extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the equivalence of the solvability criteria, every normal-series factor for S4, the faithful root action for reducible as well as irreducible quartics, and a radical tower containing all roots of the quintic."
---

::: {.problem}
(a) Given a group $G$, state the criteria that make $G$ a solvable group.
Use your definition to prove that $S_4$ is solvable.

(b) Let $g(x) \in \mathbb{Q}[x]$ have degree 4. Prove or disprove: $g(x)$ is not solvable by radicals.

(c) Let $g(x) \in \mathbb{Q}[x]$ have degree 5. Prove or disprove: $g(x)$ is not solvable by radicals.
:::

::: {.solution}
<1>1. A group is solvable when its derived series reaches the
trivial subgroup after finitely many steps. Equivalently, it has
a finite subnormal series with abelian factors.

::: {.proof}
Define $G^{(0)}=G$ and let $G^{(j+1)}$ be the subgroup generated
by all commutators $xyx^{-1}y^{-1}$ with $x,y\in G^{(j)}$.
Solvability means $G^{(n)}=1$ for some finite $n$.
Conjugation sends a commutator to the commutator of the conjugated
elements, so each commutator subgroup is normal in its parent.
The quotient by it is abelian because every commutator becomes trivial.
Thus a terminating derived series is a finite series with abelian
factors.

Conversely, suppose
$G=G_0\triangleright G_1\triangleright\cdots\triangleright G_n=1$
with every $G_j/G_{j+1}$ abelian. Then $[G_j,G_j]\subseteq G_{j+1}$.
Induction gives $G^{(j)}\subseteq G_j$: taking commutators preserves
the inclusion at each step. Therefore $G^{(n)}\subseteq G_n=1$,
so $G$ is solvable under the derived-series definition.
:::

<1>2. The group $S_4$ is solvable.

::: {.proof}
Let
$$
V=\{1,(12)(34),(13)(24),(14)(23)\}.
$$
Each of its three nonidentity elements is an involution, and the
product of two distinct ones is the third in either order.
Hence $V$ is an abelian subgroup of order $4$.
Conjugation in $S_4$ permutes these double transpositions, so
$V\lhd S_4$. Also $A_4\lhd S_4$, as the kernel of the sign map,
and $V\subseteq A_4$.
The series
$$
S_4\triangleright A_4\triangleright V\triangleright1
$$
has factors of orders $2$, $3$, and $4$. The first two are cyclic
because their orders are prime, and the last is the abelian group
$V\cong C_2\times C_2$. All factors are abelian, so step <1>1
proves solvability.
:::

<1>3. The assertion in part (b) is false: every degree-four
polynomial over $\mathbb Q$ is solvable by radicals.

::: {.proof}
Let $K$ be its splitting field. This is a finite Galois extension
because the base field has characteristic zero. Its Galois group
acts faithfully on the distinct roots: an automorphism fixing
all roots fixes their generated field $K$.
There are at most four distinct roots, so labeling them and fixing
any unused labels embeds $\operatorname{Gal}(K/\mathbb Q)$ in $S_4$.
This argument includes reducible polynomials and repeated roots.

A subgroup $H$ of a solvable group $G$ is solvable because
$H^{(j)}\subseteq G^{(j)}$ for every $j$, by induction on
commutators. Step <1>2 therefore makes the Galois group solvable.
The Galois criterion for solvability by radicals in characteristic
zero states that a polynomial is solvable by radicals exactly
when its splitting-field Galois group is solvable [@DF04].
Applying it proves the claim and disproves the proposed negation.
:::

<1>4. The assertion in part (c) is also false. An irreducible
counterexample is $g(x)=x^5-2$.

::: {.proof}
This polynomial is irreducible over $\mathbb Q$ by Eisenstein's
criterion at $2$ [@DF04]. Let $a=\sqrt[5]{2}$, and let $\zeta$
be a primitive fifth root of unity. Its five roots are
$a,\zeta a,\zeta^2a,\zeta^3a,\zeta^4a$.

The number $\zeta$ is a root of the quartic
$x^4+x^3+x^2+x+1$. By step <1>3, all roots of that quartic
lie in a radical extension of $\mathbb Q$. Choose a radical
tower ending in a field $M$ containing them. Adjoining $a$ is
one further radical adjunction, since $a^5=2\in M$.
The resulting field $M(a)$ contains all five displayed roots of
$g$. Thus $g$ is solvable by radicals. Degree five alone does
not imply the nonsolvability claimed in part (c).
:::
:::
