---
schema: qual/card@1
id: P-AMD-EKBYIW4X
kind: problem
title: Characteristically simple finite groups and minimal normal subgroups
classification:
  areas:
  - algebra
  topics:
  - Simple Groups
  - Normal Subgroups
  - Direct Products
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 5, Exercise 7. Restored
    the definitions, the three source parts, and the hint for part (a) involving
    a maximal internal direct product of isomorphic minimal normal subgroups.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Replaced the false claim that every minimal normal subgroup is simple. A
    maximal product of minimal normal subgroups is shown characteristic and
    hence equals G; only after obtaining the direct-product decomposition does
    minimal normality force each factor to be simple. The converse treats
    H=C_p by linear automorphisms and nonabelian simple H by classifying normal
    subgroups of H^n as products of coordinate factors.
---

::: {.problem}
Let $G$ be a finite group.
Call $G$ **characteristically simple** if it has no characteristic subgroups other than $1$ and $G$.
A nontrivial normal subgroup $N\trianglelefteq G$ is **minimal normal** if there is no normal subgroup $K\trianglelefteq G$ with
\[
1<K<N.
\]

(a) Suppose that $G$ is nontrivial and characteristically simple.
Prove that
\[
G\cong H^n
\]
for some simple group $H$ and some $n\ge1$.

Hint: let $N$ be a minimal normal subgroup of $G$.
Consider internal direct products
\[
N_1\times\cdots\times N_k
\]
in which every $N_i$ is a minimal normal subgroup of $G$ isomorphic to $N$, and choose one maximal under inclusion.
Show that it is characteristic in $G$, hence equals $G$, and then show that $N$ is simple.

(b) Does the converse hold?
That is, if $H$ is simple, is $H^n$ characteristically simple?

(c) If $N\trianglelefteq G$ is any minimal normal subgroup, prove that $N$ is characteristically simple and hence is a direct product of isomorphic simple groups.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $A,B\trianglelefteq G$ are distinct minimal normal subgroups, then
\[
A\cap B=1
\qquad\text{and}\qquad
[A,B]=1.
\]

::: pf-proof

The intersection $A\cap B$ is normal in $G$ and is contained in the minimal normal subgroup $A$.
Hence either
\[
A\cap B=1
\qquad\text{or}\qquad
A\cap B=A.
\]
The second possibility would give $A\le B$, and minimality of $B$ would force $A=B$, contrary to assumption.
Thus $A\cap B=1$.

Because $A$ and $B$ are both normal in $G$,
\[
[A,B]\le A\cap B=1.
\]
Therefore $A$ and $B$ commute elementwise.

:::

:::

::: pf-step

Let $N$ be a minimal normal subgroup of the nontrivial finite characteristically simple group $G$.
There is a maximal subgroup of the form
\[
M=N_1\times\cdots\times N_k,
\]
where every $N_i$ is a minimal normal subgroup of $G$ isomorphic to $N$.

::: pf-proof

Since $G$ is finite and nontrivial, it has a minimal nontrivial normal subgroup $N$.
The one-factor product $N$ belongs to the indicated collection.

By step [](#s1){.pf-ref}, distinct minimal normal subgroups intersect trivially and commute, so every product of distinct members of the collection is indeed an internal direct product.
Since $G$ is finite, there is a member maximal under inclusion; call it $M$.

:::

:::

::: {.pf-step #s3}

Every minimal normal subgroup $L\trianglelefteq G$ that is isomorphic to $N$ is contained in $M$.

::: pf-proof

Suppose $L\nleq M$.
Since $M$ is a product of normal subgroups, $M\trianglelefteq G$.
Hence
\[
L\cap M\trianglelefteq G.
\]
By minimality of $L$ and the assumption $L\nleq M$,
\[
L\cap M=1.
\]
Because both $L$ and $M$ are normal,
\[
[L,M]\le L\cap M=1.
\]
Thus $LM$ is the internal direct product
\[
M\times L,
\]
which is strictly larger than $M$ and whose factors are all minimal normal subgroups isomorphic to $N$.
This contradicts maximality of $M$.
Therefore $L\le M$.

:::

:::

::: {.pf-step #s4}

The subgroup $M$ is characteristic in $G$.

::: pf-proof

Let $\alpha\in\operatorname{Aut}(G)$.
For each factor $N_i$, the image $\alpha(N_i)$ is again a minimal normal subgroup of $G$ and is isomorphic to $N_i\cong N$.
By step [](#s3){.pf-ref},
\[
\alpha(N_i)\le M.
\]
Therefore
\[
\alpha(M)\le M.
\]
Applying the same argument to $\alpha^{-1}$ gives
\[
\alpha^{-1}(M)\le M,
\]
which is equivalent to $M\le\alpha(M)$.
Hence
\[
\alpha(M)=M.
\]
Since this holds for every automorphism $\alpha$, the subgroup $M$ is characteristic.

:::

:::

::: {.pf-step #s5}

We have
\[
G=M=N_1\times\cdots\times N_k.
\]

::: pf-proof

The subgroup $M$ is nontrivial and characteristic by step [](#s4){.pf-ref}. Since $G$ is characteristically simple,
\[
M=G.
\]

:::

:::

::: {.pf-step #s6}

Each factor $N_i$ in step [](#s5){.pf-ref} is simple.

::: pf-proof

Fix $i$, and write
\[
G=N_i\times C,
\qquad
C=\prod_{j\ne i}N_j.
\]
Let $K\trianglelefteq N_i$.
Since $C$ centralizes $N_i$, it centralizes $K$.
Thus $K$ is normalized both by $N_i$ and by $C$, hence by all of $G$.
Therefore
\[
K\trianglelefteq G.
\]
But $N_i$ is minimal normal in $G$, so
\[
K=1
\qquad\text{or}\qquad
K=N_i.
\]
Thus $N_i$ is simple.

:::

:::

::: {.pf-step #s7}

Part (a) follows: there is a simple group $H$ and an integer $n\ge1$ such that
\[
G\cong H^n.
\]

::: pf-proof

Take $H=N$.
By construction every factor $N_i$ is isomorphic to $N$, and by step [](#s6){.pf-ref} it is simple.
Then step [](#s5){.pf-ref} gives
\[
G\cong N^k=H^k.
\]

:::

:::

::: {.pf-step #s8}

If $H=C_p$ is a cyclic simple group of prime order, then $H^n$ is characteristically simple.

::: pf-proof

Identify
\[
H^n\cong \mathbb F_p^n
\]
as an additive group.
Its automorphism group is $\operatorname{GL}_n(\mathbb F_p)$.

Let $K$ be a nontrivial characteristic subgroup and choose $0\ne v\in K$.
For every nonzero $w\in\mathbb F_p^n$, there is an invertible linear map carrying $v$ to $w$.
Since $K$ is invariant under every automorphism, every nonzero $w$ lies in $K$.
Hence
\[
K=\mathbb F_p^n=H^n.
\]
Thus the only characteristic subgroups are $1$ and $H^n$.

:::

:::

::: {.pf-step #s9}

Let $H$ be nonabelian simple and set
\[
G=H_1\times\cdots\times H_n,
\qquad H_i\cong H.
\]
Every normal subgroup of $G$ is a product of a subset of the coordinate factors $H_i$.

::: pf-proof

Let $K\trianglelefteq G$.
Fix $i$.
If the projection of $K$ to $H_i$ is trivial, then $K$ has no $H_i$-component.

Suppose instead that the projection is nontrivial.
Choose
\[
x=(x_1,\ldots,x_n)\in K
\]
with $x_i\ne1$.
Since a nonabelian simple group has trivial center, there is $h\in H_i$ with
\[
[x_i,h]\ne1.
\]
Regard $h$ as an element of the $i$th coordinate factor.
Normality of $K$ gives
\[
[x,h]\in K.
\]
All coordinates of this commutator except the $i$th are trivial, so
\[
1\ne[x,h]\in K\cap H_i.
\]
The subgroup $K\cap H_i$ is normal in the simple group $H_i$, hence
\[
H_i\le K.
\]

Therefore, for each $i$, either the projection of $K$ to $H_i$ is trivial or $H_i\le K$.
It follows that $K$ is exactly the product of the coordinate factors on which it has nontrivial projection.

:::

:::

::: {.pf-step #s10}

If $H$ is nonabelian simple, then $H^n$ is characteristically simple.

::: pf-proof

Let $K$ be characteristic in $H^n$.
In particular $K\trianglelefteq H^n$, so by step [](#s9){.pf-ref} it is a product of some subset of the coordinate factors.

Every permutation of the $n$ coordinates is an automorphism of $H^n$.
Since $K$ is characteristic, its subset of coordinate factors must be invariant under every permutation.
The only such subsets are the empty set and the full set.
Hence
\[
K=1
\qquad\text{or}\qquad
K=H^n.
\]

:::

:::

::: {.pf-step #s11}

The converse in part (b) holds for every simple group $H$.

::: pf-proof

Every abelian simple group is cyclic of prime order, so the abelian case is step [](#s8){.pf-ref}. The nonabelian case is step [](#s10){.pf-ref}. Therefore $H^n$ is characteristically simple whenever $H$ is simple.

:::

:::

::: {.pf-step #s12}

If $N\trianglelefteq G$ is minimal normal, then $N$ is characteristically simple.

::: pf-proof

Let $K$ be characteristic in $N$.
Since $N\trianglelefteq G$, characteristicity of $K$ in $N$ implies
\[
K\trianglelefteq G.
\]
Also $K\le N$.
By minimal normality of $N$,
\[
K=1
\qquad\text{or}\qquad
K=N.
\]
Thus $N$ is characteristically simple.

:::

:::

::: {.pf-step #s13}

If $N\trianglelefteq G$ is minimal normal, then
\[
N\cong H^n
\]
for some simple group $H$ and some $n\ge1$.

::: pf-proof

The subgroup $N$ is finite, nontrivial, and characteristically simple by step [](#s12){.pf-ref}. Apply part (a), namely step [](#s7){.pf-ref}, to the group $N$ itself.

:::

:::

::: pf-qed

Parts (a), (b), and (c) are steps [](#s7){.pf-ref}, [](#s11){.pf-ref} and [](#s13){.pf-ref}, respectively.

:::

:::

:::
