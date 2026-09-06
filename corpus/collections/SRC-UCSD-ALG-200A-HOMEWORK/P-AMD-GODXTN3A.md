---
schema: qual/card@1
id: P-AMD-GODXTN3A
kind: problem
title: A finite group is nilpotent iff elements of coprime order commute
classification:
  areas:
  - algebra
  topics:
  - Nilpotent Groups
  - Sylow Theory
  - Direct Products
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 6, Exercise 2(a).
    Restored the statement for a finite group G and replaced the corrupted
    shorthand saying that |G| itself is nilpotent.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Proved the needed Sylow characterization of finite nilpotence. A finite
    nilpotent group satisfies the normalizer condition, forcing every Sylow
    subgroup to be normal. Conversely, pairwise commuting Sylow subgroups form
    their full internal direct product, and finite p-groups and finite direct
    products of nilpotent groups are nilpotent. The coprime-order criterion then
    follows in both directions.
---

::: {.problem}
Let $G$ be a finite group.
Prove that $G$ is nilpotent if and only if, whenever $a,b\in G$ have relatively prime orders, then
\[
ab=ba.
\]
:::

::: {.solution}
<1>1. A nilpotent group satisfies the normalizer condition: if $H<G$, then
\[
H<N_G(H).
\]
::: {.proof}
Let
\[
1=Z_0(G)\le Z_1(G)\le\cdots\le Z_c(G)=G
\]
be an upper central series for $G$, so
\[
Z_{i+1}(G)/Z_i(G)=Z(G/Z_i(G)).
\]

Choose the least $i\ge1$ such that
\[
Z_i(G)\nleq H.
\]
Then $Z_{i-1}(G)\le H$.
Choose
\[
x\in Z_i(G)\setminus H.
\]
For every $h\in H$, centrality of $xZ_{i-1}(G)$ in $G/Z_{i-1}(G)$ gives
\[
[x,h]\in Z_{i-1}(G)\le H.
\]
Thus $xHx^{-1}=H$, so
\[
x\in N_G(H)\setminus H.
\]
Hence $H<N_G(H)$.
:::

<1>2. If $G$ is finite and nilpotent, every Sylow subgroup of $G$ is normal.
::: {.proof}
Let $P\in\operatorname{Syl}_p(G)$ and put
\[
N=N_G(P).
\]
The subgroup $P$ is normal in $N$ and is a Sylow $p$-subgroup of $N$, hence it is the unique Sylow $p$-subgroup of $N$.
Therefore
\[
P\operatorname{char}N.
\]
It follows that every element normalizing $N$ also normalizes $P$, so
\[
N_G(N)\le N_G(P)=N.
\]
The reverse inclusion is automatic, hence
\[
N_G(N)=N.
\]

If $N<G$, <1>1 would imply
\[
N<N_G(N),
\]
a contradiction.
Thus $N=G$, so $P\trianglelefteq G$.
:::

<1>3. Distinct normal Sylow subgroups commute elementwise.
::: {.proof}
Let $P\trianglelefteq G$ be a Sylow $p$-subgroup and $Q\trianglelefteq G$ a Sylow $q$-subgroup with $p\ne q$.
Since both are normal,
\[
[P,Q]\le P\cap Q.
\]
But $|P|$ and $|Q|$ are relatively prime, so
\[
P\cap Q=1.
\]
Hence
\[
[P,Q]=1.
\]
:::

<1>4. A finite nilpotent group is the internal direct product of its Sylow subgroups.
::: {.proof}
Let
\[
|G|=\prod_{i=1}^r p_i^{e_i}
\]
and choose $P_i\in\operatorname{Syl}_{p_i}(G)$.
By <1>2 every $P_i$ is normal, and by <1>3 the $P_i$ commute pairwise.

Therefore
\[
P_1\cdots P_r
\]
is an internal direct product.
Its order is
\[
\prod_{i=1}^r |P_i|
  =\prod_{i=1}^r p_i^{e_i}
  =|G|.
\]
Hence
\[
G=P_1\times\cdots\times P_r.
\]
:::

<1>5. If $G$ is nilpotent and $a,b\in G$ have relatively prime orders, then $a$ and $b$ commute.
::: {.proof}
Use the decomposition from <1>4:
\[
G=P_1\times\cdots\times P_r.
\]
Write
\[
a=a_1\cdots a_r,
\qquad
b=b_1\cdots b_r,
\qquad
a_i,b_i\in P_i.
\]
If $a_i\ne1$, then $p_i$ divides $|a|$; if $b_i\ne1$, then $p_i$ divides $|b|$.
Since
\[
\gcd(|a|,|b|)=1,
\]
for each $i$ at least one of $a_i,b_i$ is trivial.
Components in distinct Sylow factors commute by <1>3. Hence every component of $a$ commutes with every component of $b$, and therefore
\[
ab=ba.
\]
:::

<1>6. Conversely, suppose that every two elements of relatively prime orders in $G$ commute.
Then any two Sylow subgroups for distinct primes commute elementwise.
::: {.proof}
Let $P\in\operatorname{Syl}_p(G)$ and $Q\in\operatorname{Syl}_q(G)$ with $p\ne q$.
For arbitrary
\[
x\in P,
\qquad
y\in Q,
\]
the order of $x$ is a power of $p$ and the order of $y$ is a power of $q$.
Thus
\[
\gcd(|x|,|y|)=1.
\]
By hypothesis, $xy=yx$.
Therefore
\[
[P,Q]=1.
\]
:::

<1>7. Under the hypothesis of <1>6, $G$ is the internal direct product of one Sylow subgroup for each prime divisor of $|G|$.
::: {.proof}
Write
\[
|G|=\prod_{i=1}^r p_i^{e_i}
\]
and choose $P_i\in\operatorname{Syl}_{p_i}(G)$.
By <1>6 the $P_i$ commute pairwise, so their product
\[
P_1\cdots P_r
\]
is a subgroup of $G$.

Because the factor orders are pairwise relatively prime and the factors commute, multiplication gives an injective homomorphism
\[
P_1\times\cdots\times P_r
  \longrightarrow G.
\]
Indeed, if $x_1\cdots x_r=1$ with $x_i\in P_i$, then
\[
x_i=(\prod_{j\ne i}x_j)^{-1}.
\]
The left side has $p_i$-power order, while the right side has order dividing a product of powers of primes different from $p_i$; hence $x_i=1$.
Thus the kernel is trivial.

Its image therefore has order
\[
\prod_{i=1}^r |P_i|=|G|,
\]
so the image is all of $G$.
Hence
\[
G=P_1\times\cdots\times P_r.
\]
:::

<1>8. Every finite $p$-group is nilpotent.
::: {.proof}
We induct on the order of a finite $p$-group $P$.
The trivial group is nilpotent.
If $P\ne1$, the class equation gives
\[
Z(P)\ne1.
\]
The quotient $P/Z(P)$ is a smaller $p$-group, hence nilpotent by induction.
Say
\[
\gamma_{c+1}(P/Z(P))=1.
\]
For the quotient map $\pi:P\to P/Z(P)$, induction on the lower central series gives
\[
\gamma_i(P/Z(P))=\pi(\gamma_i(P))
\]
for every $i$.
Thus
\[
\gamma_{c+1}(P)\le Z(P),
\]
and consequently
\[
\gamma_{c+2}(P)
  =[P,\gamma_{c+1}(P)]
  \le[P,Z(P)]
  =1.
\]
Hence $P$ is nilpotent.
:::

<1>9. A finite direct product of nilpotent groups is nilpotent.
::: {.proof}
For two groups $A,B$, induction on $i$ gives
\[
\gamma_i(A\times B)=\gamma_i(A)\times\gamma_i(B).
\]
Thus if
\[
\gamma_{c+1}(A)=1
\qquad\text{and}\qquad
\gamma_{d+1}(B)=1,
\]
then
\[
\gamma_{\max(c,d)+1}(A\times B)=1.
\]
Induction on the number of factors proves the finite-product statement.
:::

<1>10. Under the coprime-order commutativity hypothesis, $G$ is nilpotent.
::: {.proof}
By <1>7,
\[
G=P_1\times\cdots\times P_r
\]
for Sylow subgroups $P_i$.
Each $P_i$ is nilpotent by <1>8, so $G$ is nilpotent by <1>9.
:::

<1>11. Q.E.D.
::: {.proof}
The forward implication is <1>5 and the reverse implication is <1>10.
:::
:::
