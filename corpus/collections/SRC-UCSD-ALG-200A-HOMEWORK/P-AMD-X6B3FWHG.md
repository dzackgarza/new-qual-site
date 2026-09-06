---
schema: qual/card@1
id: P-AMD-X6B3FWHG
kind: problem
title: The Frattini subgroup of a finite group is characteristic and nilpotent; $P/\Phi(P)$
  is the largest elementary abelian quotient of a $p$-group
classification:
  areas:
  - algebra
  topics:
  - Nilpotent Groups
  - Subgroups
  - p-Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 6, Exercise 3. Restored
    the definition of the Frattini subgroup, all three source parts, the
    Frattini-argument hint in part (b), and the precise smallest-normal-subgroup
    assertion in part (c).
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Automorphisms permute maximal subgroups, so Phi(G) is characteristic. For
    each Sylow subgroup S of Phi(G), Frattini's argument gives
    G=Phi(G)N_G(S); maximal-subgroup containment forces N_G(S)=G, so every
    Sylow subgroup of Phi(G) is normal and Phi(G) is nilpotent. For a p-group,
    maximal subgroups are normal of index p, forcing commutators and pth powers
    into Phi(P); hyperplanes in any elementary abelian quotient prove the
    minimality of Phi(P).
---

::: {.problem}
Let $G$ be a finite group.
Its **Frattini subgroup** is
\[
\Phi(G)=\bigcap_{M\text{ maximal in }G}M.
\]

(a) Prove that $\Phi(G)$ is characteristic in $G$.

(b) Prove that $\Phi(G)$ is nilpotent.

Hint: use Frattini's argument.

(c) Now let $P$ be a finite $p$-group.
Prove that $P/\Phi(P)$ is an elementary abelian $p$-group and that $\Phi(P)$ is the unique smallest normal subgroup with this property: if $N\trianglelefteq P$ and $P/N$ is elementary abelian, then
\[
\Phi(P)\le N.
\]
:::

::: {.solution}
<1>1. Every automorphism of $G$ permutes the maximal subgroups of $G$.
::: {.proof}
Let $\alpha\in\operatorname{Aut}(G)$ and let $M<G$ be maximal.
If
\[
\alpha(M)<K<G,
\]
then applying $\alpha^{-1}$ gives
\[
M<\alpha^{-1}(K)<G,
\]
contradicting maximality of $M$.
Hence $\alpha(M)$ is maximal.
Applying the same argument to $\alpha^{-1}$ shows that the induced map on maximal subgroups is a permutation.
:::

<1>2. The subgroup $\Phi(G)$ is characteristic in $G$.
::: {.proof}
By <1>1, for every $\alpha\in\operatorname{Aut}(G)$,
\[
\alpha(\Phi(G))
  =\alpha\left(\bigcap_{M\text{ maximal}}M\right)
  =\bigcap_{M\text{ maximal}}\alpha(M)
  =\Phi(G).
\]
This proves part (a).
:::

<1>3. Frattini's argument: if $N\trianglelefteq G$ and $S\in\operatorname{Syl}_p(N)$, then
\[
G=N\,N_G(S).
\]
::: {.proof}
Let $g\in G$.
Since $N\trianglelefteq G$, the subgroup
\[
gSg^{-1}
\]
is another Sylow $p$-subgroup of $N$.
By Sylow conjugacy inside $N$, there is $n\in N$ such that
\[
n(gSg^{-1})n^{-1}=S.
\]
Thus
\[
ng\in N_G(S),
\]
and therefore
\[
g=n^{-1}(ng)\in N\,N_G(S).
\]
Hence $G=N\,N_G(S)$.
:::

<1>4. Every Sylow subgroup of $\Phi(G)$ is normal in $G$.
::: {.proof}
Set
\[
F=\Phi(G).
\]
By <1>2, $F\trianglelefteq G$.
Let $S\in\operatorname{Syl}_p(F)$.
Frattini's argument <1>3 gives
\[
G=F\,N_G(S).
\]

Suppose $N_G(S)<G$.
Since $G$ is finite, $N_G(S)$ lies in some maximal subgroup $M<G$.
By definition of the Frattini subgroup,
\[
F\le M.
\]
Consequently
\[
G=F\,N_G(S)\le M<G,
\]
a contradiction.
Hence
\[
N_G(S)=G,
\]
so $S\trianglelefteq G$.
:::

<1>5. A finite group in which every Sylow subgroup is normal is nilpotent.
::: {.proof}
Let $K$ be such a group and choose one Sylow subgroup $S_p$ for each prime $p\mid |K|$.
If $p\ne q$, normality gives
\[
[S_p,S_q]\le S_p\cap S_q=1.
\]
Thus the Sylow subgroups commute pairwise, and their product has order
\[
\prod_{p\mid |K|}|S_p|=|K|.
\]
Hence
\[
K=\prod_{p\mid |K|}S_p
\]
is their internal direct product.

Each finite $p$-group is nilpotent.
Indeed, induction on its order uses the class equation to obtain a nontrivial center; the quotient by the center is a smaller $p$-group, and nilpotence of that quotient implies nilpotence of the group because if
\[
\gamma_{c+1}(S_p/Z(S_p))=1,
\]
then
\[
\gamma_{c+1}(S_p)\le Z(S_p)
\]
and hence
\[
\gamma_{c+2}(S_p)=1.
\]

Finally, lower central series commute with finite direct products:
\[
\gamma_i(A\times B)=\gamma_i(A)\times\gamma_i(B).
\]
Therefore a finite direct product of nilpotent groups is nilpotent, so $K$ is nilpotent.
:::

<1>6. The Frattini subgroup $\Phi(G)$ is nilpotent.
::: {.proof}
By <1>4, every Sylow subgroup of $\Phi(G)$ is normal in $G$, hence also normal in $\Phi(G)$.
Apply <1>5 to the finite group $\Phi(G)$.
This proves part (b).
:::

<1>7. If $P$ is a finite $p$-group and $H<P$, then
\[
H<N_P(H).
\]
::: {.proof}
Let $H$ act by left multiplication on the finite set $P/H$ of left cosets.
Every orbit has size a power of $p$.
Since $H<P$,
\[
|P:H|
\]
is divisible by $p$.

A coset $xH$ is fixed by every element of $H$ exactly when
\[
x^{-1}Hx=H,
\]
that is, exactly when $x\in N_P(H)$.
Hence the number of fixed cosets is
\[
|N_P(H):H|.
\]
The orbit decomposition gives
\[
|P:H|\equiv |N_P(H):H|\pmod p.
\]
Thus $p$ divides $|N_P(H):H|$.
Since this index is positive, it is at least $p$, so
\[
H<N_P(H).
\]
:::

<1>8. Every maximal subgroup $M$ of a finite $p$-group $P$ is normal and has index $p$.
::: {.proof}
By <1>7,
\[
M<N_P(M)\le P.
\]
Maximality of $M$ forces
\[
N_P(M)=P,
\]
so $M\trianglelefteq P$.

The quotient $P/M$ is therefore a nontrivial finite $p$-group.
Since $M$ is maximal, $P/M$ has no nontrivial proper subgroup.
Every nontrivial finite $p$-group has a subgroup of order $p$, so this is possible only when
\[
|P/M|=p.
\]
Thus $[P:M]=p$.
:::

<1>9. For a finite $p$-group $P$,
\[
[P,P]\le\Phi(P)
\qquad\text{and}\qquad
x^p\in\Phi(P)\quad\text{for every }x\in P.
\]
::: {.proof}
Let $M$ be any maximal subgroup of $P$.
By <1>8,
\[
P/M\cong C_p.
\]
The quotient is abelian, so
\[
[P,P]\le M.
\]
It has exponent $p$, so for every $x\in P$,
\[
x^p\in M.
\]
Since these containments hold for every maximal subgroup $M$, intersecting all such $M$ gives
\[
[P,P]\le\Phi(P)
\]
and
\[
x^p\in\Phi(P)
\]
for every $x\in P$.
:::

<1>10. The quotient $P/\Phi(P)$ is an elementary abelian $p$-group.
::: {.proof}
By <1>9, the quotient is abelian and every element has order dividing $p$.
It is finite because $P$ is finite.
Hence it is a finite-dimensional vector space over $\mathbb F_p$, equivalently a finite direct product of copies of $C_p$.
Thus $P/\Phi(P)$ is elementary abelian.
:::

<1>11. If $N\trianglelefteq P$ and $P/N$ is elementary abelian, then
\[
\Phi(P)\le N.
\]
::: {.proof}
Set
\[
V=P/N.
\]
If $V=0$, then $N=P$ and the conclusion is immediate.
Otherwise, view $V$ as a finite-dimensional vector space over $\mathbb F_p$.

The intersection of all codimension-one subspaces of $V$ is $0$.
Indeed, for any nonzero $v\in V$, extend $v$ to a basis and choose a linear functional
\[
f:V\to\mathbb F_p
\]
with $f(v)=1$; then $\ker f$ is a hyperplane not containing $v$.

Let $\pi:P\to V$ be the quotient map.
The inverse image under $\pi$ of each hyperplane $W<V$ is a subgroup $M$ with
\[
[P:M]=[V:W]=p,
\]
so $M$ is maximal in $P$.
Therefore
\[
\Phi(P)
  \le \bigcap_{W\text{ hyperplane}}\pi^{-1}(W)
  =\pi^{-1}\left(\bigcap_{W\text{ hyperplane}}W\right)
  =\pi^{-1}(0)
  =N.
\]
:::

<1>12. The subgroup $\Phi(P)$ is the unique smallest normal subgroup $N\trianglelefteq P$ for which $P/N$ is elementary abelian.
::: {.proof}
By <1>2, $\Phi(P)$ is characteristic in $P$, hence normal, and by <1>10 its quotient is elementary abelian.
By <1>11, every normal subgroup $N$ with elementary abelian quotient contains $\Phi(P)$.
This proves the claimed minimality and uniqueness, completing part (c).
:::

<1>13. Q.E.D.
::: {.proof}
Parts (a), (b), and (c) are <1>2, <1>6, and <1>12.
:::
:::
