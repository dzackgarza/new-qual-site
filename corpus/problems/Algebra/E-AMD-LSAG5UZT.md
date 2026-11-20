---
schema: qual/card@1
id: E-AMD-LSAG5UZT
kind: problem
title: Groups of order $p^3$ have a normal subgroup of order $p^2$
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5
  date: 2026-08-30
- event: source-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source part (b) read "Suppose N = <h> is cyclic and classify all possibilities for G if |h| = p^3, |h| = p", which is inconsistent since |N| = p^2; the statement takes h to be an element of G of largest order. The source hint "Sylow and semidirect products" moved to a hint block.'
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The seventeen leaf steps of parts (a) and (b) asserted their claim with no proof body; each
    now carries one. No claim, no numbering and no statement is changed. Cited by number only:
    the class equation with the orbit-stabilizer identification of a class size with an index,
    Cauchy's theorem, Lagrange's theorem, the correspondence theorem for subgroups of a
    quotient, the lemma that a group with cyclic central quotient is abelian, and von Dyck's
    theorem for the identification with the unitriangular matrices. Checked: that a noncentral
    class has size $p$ or $p^2$, that the Heisenberg relations give exactly $p^3$ distinct
    elements, and that exponent $2$ forces commutativity. One proof was previously missing in
    substance rather than in form — step 4.6 asserted that $[x,y]$ generates $Z(G)$ without
    saying why it is nontrivial — and the new proof supplies it: were $[x,y]=1$, the generators
    $x,y$ would commute modulo a central subgroup, making $G$ abelian.
---

::: {.exercise}
Let $p$ be a prime and let $G$ be a group with $\abs{G} = p^3$.

(a) Prove that $G$ has a normal subgroup $N$ of order $p^2$.

(b) Let $h \in G$ be an element of largest order. Classify all possibilities for $G$ if (i) $\abs h = p^3$; (ii) $\abs h = p$.
:::

::: {.hint}
Sylow and semidirect products.
:::

::: {.hint}
For a central $z$ of order $p$, the quotient $G/\generators{z}$ has order $p^2$ and is abelian; the preimage of a subgroup of order $p$ is normal of order $p^2$.
:::

::: {.solution}

::: pf

::: {.pf-step #p3-has-normal-p2-subgroup}
(a) $G$ has a normal subgroup of order $p^2$.

::: pf-proof

::: pf-step
$G$ is a $p$-group, so the class equation
$$\abs G = \abs{Z(G)} + \sum_{i} [G : C_G(x_i)]$$
over representatives $x_i$ of the noncentral conjugacy classes has every index $[G:C_G(x_i)]$ divisible by $p$.

::: pf-proof
The group $G$ is the disjoint union of its conjugacy classes, and a class has one element exactly when the element is central; so $\abs G=\abs{Z(G)}+\sum_i\abs{\text{class}(x_i)}$ over the noncentral classes. The orbit-stabilizer theorem identifies the class size of $x_i$ with the index $[G:C_G(x_i)]$ of its centralizer. For a noncentral $x_i$ the centralizer is a proper subgroup of $G$, and $\abs G=p^3$, so that index is $p$ or $p^2$, in either case divisible by $p$.
:::

:::

::: {.pf-step #class-equation-nontrivial-center}
Hence $p \mid \abs{Z(G)}$, so $Z(G) \neq 1$.

::: pf-proof
Reduce the class equation modulo $p$: the left side is $p^3\equiv0$ and every summand is $\equiv0$ by step 1.1, so $\abs{Z(G)}\equiv0\pmod p$. The centre contains the identity, so $\abs{Z(G)}\ge1$, and a positive multiple of $p$ is at least $p$; hence $Z(G)$ has a nonidentity element.
:::

:::

::: pf-step
By Cauchy's theorem applied to $Z(G)$, pick $z \in Z(G)$ with $\abs z = p$.

::: pf-proof
$Z(G)$ is a finite abelian group whose order is divisible by $p$ by step 2, and Cauchy's theorem provides an element of order $p$ in a finite group of order divisible by $p$; that element lies in $Z(G)$ and has order $p$ in $G$.
:::

:::

::: pf-step
$\generators z \normal G$, because a central subgroup is normalized by every element of $G$.

::: pf-proof
For $g\in G$ we have $gzg^{-1}=z$ because $z\in Z(G)$, so $g\generators zg^{-1}=\generators z$; a subgroup carried to itself by every conjugation is normal.
:::

:::

::: pf-step
$\abs{G/\generators z} = p^3/p = p^2$, and every group of order $p^2$ is abelian: if $Q$ has order $p^2$ then $Q/Z(Q)$ is cyclic by step [](#class-equation-nontrivial-center){.pf-ref} applied to $Q$, and a group with cyclic central quotient is abelian.

::: pf-proof
The quotient has order $\abs G/\abs{\generators z}=p^3/p=p^2$ by Lagrange. For the second clause, the argument of steps 1.1 and 2 applied to a group $Q$ of order $p^2$ gives $\abs{Z(Q)}\ne1$, so $\abs{Z(Q)}$ is $p$ or $p^2$; if it is $p^2$ then $Q$ is abelian, and if it is $p$ then $Q/Z(Q)$ has order $p$, hence is cyclic, and a group whose central quotient is cyclic is abelian, again a contradiction. So $Q$ is abelian in either case.
:::

:::

::: pf-step
By Cauchy's theorem, $G/\generators z$ has a subgroup $\bar H$ with $\abs{\bar H} = p$, and $\bar H \normal G/\generators z$ because that quotient is abelian.

::: pf-proof
The quotient has order $p^2$ by step 5, so its order is divisible by $p$ and Cauchy's theorem gives an element of order $p$, whose generated subgroup $\bar H$ has order $p$. In an abelian group every subgroup is normal, and the quotient is abelian by step 5.
:::

:::

::: pf-step
Let $N$ be the preimage of $\bar H$ under $\pi: G \to G/\generators z$. The correspondence theorem gives $N \normal G$, and
$$\abs N = \abs{\bar H}\cdot \abs{\generators z} = p \cdot p = p^2 .$$

::: pf-proof
The correspondence theorem bijects the subgroups of $G$ containing $\generators z$ with the subgroups of the quotient, and carries normality to normality; $N=\pi^{-1}(\bar H)$ is normal because $\bar H$ is. The preimage is a union of the cosets of $\generators z$ lying in $\bar H$, of which there are $\abs{\bar H}$, each of size $p$; hence $\abs N=p\cdot p$.
:::

:::

:::

:::

::: pf-step
(b) If $h$ has largest order in $G$, then (i) $\abs h = p^3$ gives $G \cong \ZZ/p^3$, and (ii) $\abs h = p$ gives $G \cong (\ZZ/p)^3$ or, for odd $p$, the Heisenberg group of order $p^3$.

::: pf-proof

::: {.pf-step #cyclic-case-order-p3}
(i) If $\abs h = p^3$ then $G \cong \ZZ/p^3$.

::: pf-proof

::: pf-step
$\generators h \leq G$ has $p^3 = \abs G$ elements, so $\generators h = G$.

::: pf-proof
The order of the cyclic subgroup generated by $h$ equals the order of $h$, which is $p^3=\abs G$; a subgroup with as many elements as the group is the group.
:::

:::

::: pf-step
A cyclic group is determined up to isomorphism by its order.

::: pf-proof
The map $\ZZ/n\ZZ\to\generators g$, $\bar k\mapsto g^k$, is a well-defined surjective homomorphism because $g^n=1$ generates, and it is injective because $g^k=1$ forces $n\mid k$; so a cyclic group of order $n$ is isomorphic to $\ZZ/n\ZZ$. With step 3.1, $G\cong\ZZ/p^3$.
:::

:::

:::

:::

::: {.pf-step #exponent-p-case}
(ii) If $\abs h = p$ for an element of largest order, then $G$ has exponent $p$, and $G$ is one of two groups.

::: pf-proof

::: pf-step
Every nonidentity element of $G$ has order $p$, since $p$ is the largest order occurring.

::: pf-proof
An element's order divides $\abs G=p^3$ by Lagrange, so it is $1$, $p$ or $p^2$; the hypothesis is that no element has order $p^3$ and $h$ of order $p$ realizes the largest order, so $p^2$ does not occur either. Hence every nonidentity element has order $p$, which is the assertion that the exponent is $p$.
:::

:::

::: {.pf-step #exponent-p-abelian-case}
Suppose first that $G$ is abelian. Then $G$ is a vector space over $\FF_p$ of dimension $3$, so $G \cong (\ZZ/p)^3$.

::: pf-proof
For an abelian group of exponent $p$, scalar multiplication by $\bar k\in\FF_p$ is well defined because $kg$ depends only on $k$ mod $p$, and it makes $G$ a module over the field $\FF_p$, that is a vector space. A finite abelian group that is a vector space over $\FF_p$ is isomorphic to $(\ZZ/p)^d$ where $p^d=\abs G$; here $d=3$.
:::

:::

::: pf-step
Suppose instead that $G$ is nonabelian. Then $\abs{Z(G)} \neq p^3$, and $\abs{Z(G)} \neq p^2$, since $G/Z(G)$ cyclic forces $G$ abelian. With $Z(G) \neq 1$ from step [](#class-equation-nontrivial-center){.pf-ref} this gives $\abs{Z(G)} = p$.

::: pf-proof
$\abs{Z(G)}=p^3$ means $Z(G)=G$, that is $G$ abelian. If $\abs{Z(G)}=p^2$ then $G/Z(G)$ has order $p$, hence is cyclic, and a group whose central quotient is cyclic is abelian — the standard lemma, proved by choosing a generator $aZ(G)$ and writing every element as $a^iz$ with $z$ central, so that any two elements commute. Both are excluded, and $\abs{Z(G)}$ is a positive power of $p$ by step 2, so it is $p$.
:::

:::

::: pf-step
So $G/Z(G)$ has order $p^2$ and is not cyclic, hence $G/Z(G) \cong (\ZZ/p)^2$.

::: pf-proof
$\abs{G/Z(G)}=\abs G/\abs{Z(G)}=p^3/p=p^2$ by step 4.3. It is not cyclic, since a cyclic central quotient would make $G$ abelian. A group of order $p^2$ is $\ZZ/p^2$ or $\ZZ/p\times\ZZ/p$ by the classification of abelian groups of order $p^2$ together with step 1.5 (every such group is abelian); the cyclic one is excluded, so the quotient is $(\ZZ/p)^2$.
:::

:::

::: pf-step
Choose $x, y \in G$ whose images generate $G/Z(G)$, and write $Z(G) = \generators z$. Then $G = \generators{x, y, z}$.

::: pf-proof
A generating set of the quotient lifts to a set generating $G$ together with $Z(G)$: every $g\in G$ has $gZ(G)$ a product of powers of $xZ(G)$ and $yZ(G)$, so $g=x^ay^bz$ for some integers and some $z\in Z(G)$. Since $Z(G)=\generators z$ by step 4.3, the three elements $x,y,z$ generate $G$.
:::

:::

::: pf-step
The commutator $[x,y]$ lies in $Z(G)$, because $G/Z(G)$ is abelian, and $[x,y] \neq 1$, because $x$ and $y$ do not commute. So $\generators{[x,y]} = Z(G)$, and after replacing $z$ by $[x,y]$ we may take
$$x^p = y^p = z^p = 1, \qquad [x,y] = z, \qquad z \text{ central}.$$

::: pf-proof
In a group with abelian quotient $G/Z(G)$, the commutator of any two elements lies in $Z(G)$: $[x,y]Z(G)=[xZ(G),yZ(G)]=Z(G)$. Were $[x,y]=1$ then $x$ and $y$ would commute, and since $x$ and $y$ generate $G$ modulo the central subgroup, $G$ would be abelian, contrary to the case. So $[x,y]$ is a nonidentity element of $Z(G)$, which has order $p$ by step 4.3, hence generates it; taking $z=[x,y]$ gives the commutator relation. Finally $x^p=y^p=1$ and $z^p=1$ because every element of $G$ has order $p$ by step 4.1, and $z$ is central by construction.
:::

:::

::: pf-step
These relations write every element of $G$ once as $x^a y^b z^c$ with $0 \leq a,b,c < p$, so they present a single group of order $p^3$, namely the group of upper unitriangular $3\times 3$ matrices over $\FF_p$,
$$G \cong \theset{ \begin{pmatrix} 1 & a & c \\ 0 & 1 & b \\ 0 & 0 & 1\end{pmatrix} \st a,b,c \in \FF_p } \cong (\ZZ/p)^2 \semidirect \ZZ/p .$$

::: pf-proof
Since $z$ is central and $[x,y]=z$, every word in $x,y$ can be brought to the form $x^ay^bz^c$, so the $p^3$ such elements span $G$; as $\abs G=p^3$ they are all distinct and each element has exactly one expression, which is the first assertion. The unitriangular matrices with entries $a,b,c$ multiply by the rule $(a,b,c)(a',b',c')=(a+a',b+b',c+c'+ab')$, and putting $X=(1,0,0)$, $Y=(0,1,0)$, $Z=(0,0,1)$ gives $X^p=Y^p=Z^p=1$, $Z$ central and $[X,Y]=Z$, so they satisfy the same relations and the map $x\mapsto X$, $y\mapsto Y$, $z\mapsto Z$ is an isomorphism by von Dyck's theorem, both groups having order $p^3$.
:::

:::

::: pf-step
This case is empty for $p = 2$: exponent $2$ forces $g^2 = 1$ for all $g$, hence $(gh)^2 = 1$ and $gh = hg$, so $G$ is abelian and step [](#exponent-p-abelian-case){.pf-ref} applies.

::: pf-proof
If every element has order $2$ then $g^2=1$ for all $g$; from $(gh)^2=1$ and $(gh)^2=ghgh$ we get $ghgh=1$, and multiplying on the left by $g^{-1}=g$ and on the right by $h^{-1}=h$ gives $hg=gh$. So $G$ is abelian, and the nonabelian case treated in steps 4.3 to 4.7 cannot occur when $p=2$; the only exponent-$2$ group of order $8$ is $(\ZZ/2)^3$.
:::

:::

:::

:::

:::

:::

:::
:::
