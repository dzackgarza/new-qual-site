---
schema: qual/card@1
id: P-AMD-WFZJNWCF
kind: problem
title: Finite groups whose maximal subgroups have prime index are solvable
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Sylow Theory
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 5, Exercise 6. Restored
    the three-part source statement and its normalizer hint, replacing the
    corrupted shorthand in the card.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Part (a) compares the Sylow counts in G and H through the common normalizer.
    Part (b) places a nonnormal Sylow subgroup in a maximal subgroup; its prime
    index would be both congruent to 1 mod p and at most the largest prime p, a
    contradiction. Part (c) proves quotient inheritance and then uses induction,
    with the extension criterion and solvability of finite p-groups supplied
    explicitly.
---

::: {.problem}
Let $G$ be a finite group such that every maximal subgroup of $G$ has prime index.

(a) Let $P\in\operatorname{Syl}_p(G)$ and suppose
\[
N_G(P)\le H\le G.
\]
Prove that
\[
[G:H]\equiv1\pmod p.
\]

Hint: $P$ is a Sylow $p$-subgroup of $H$ and $N_G(P)=N_H(P)$.

(b) Let $p$ be the largest prime dividing $|G|$.
Show that $G$ has a normal Sylow $p$-subgroup.

(c) Conclude by induction on $|G|$ that $G$ is solvable.
:::

::: {.solution}
<1>1. Let $P\in\operatorname{Syl}_p(G)$ and suppose $N_G(P)\le H\le G$.
Then $P\in\operatorname{Syl}_p(H)$ and
\[
N_H(P)=N_G(P).
\]
::: {.proof}
Since
\[
P\le N_G(P)\le H,
\]
the subgroup $P$ lies in $H$.
No $p$-subgroup of $H$ can have order larger than $P$, because $H\le G$ and $P$ is already Sylow in $G$.
Hence $P$ is Sylow in $H$.

Also
\[
N_H(P)=H\cap N_G(P).
\]
The assumption $N_G(P)\le H$ therefore gives
\[
N_H(P)=N_G(P).
\]
:::

<1>2. Under the hypotheses of <1>1,
\[
[G:H]\equiv1\pmod p.
\]
::: {.proof}
The number of Sylow $p$-subgroups of a finite group is the index of the normalizer of one of them.
Thus
\[
n_p(G)=[G:N_G(P)]
\qquad\text{and}\qquad
n_p(H)=[H:N_H(P)].
\]
By Sylow's theorem,
\[
n_p(G)\equiv n_p(H)\equiv1\pmod p.
\]
Using <1>1 and the index formula,
\[
[G:N_G(P)]
  =[G:H]\,[H:N_G(P)]
  =[G:H]\,[H:N_H(P)].
\]
Reducing modulo $p$ gives
\[
1\equiv [G:H]\cdot1\pmod p,
\]
so
\[
[G:H]\equiv1\pmod p.
\]
This proves part (a).
:::

<1>3. Let $p$ be the largest prime dividing $|G|$ and let $P\in\operatorname{Syl}_p(G)$.
Then $P\trianglelefteq G$.
::: {.proof}
Suppose instead that $P$ is not normal.
Then
\[
N_G(P)<G.
\]
Because $G$ is finite, $N_G(P)$ is contained in some maximal subgroup $M<G$.
By hypothesis,
\[
[G:M]=q
\]
for some prime $q$.

Applying <1>2 with $H=M$ gives
\[
q=[G:M]\equiv1\pmod p.
\]
Since $q=[G:M]$ divides $|G|$, the prime $q$ is a prime divisor of $|G|$.
The maximality of $p$ therefore gives
\[
q\le p.
\]
But a positive integer congruent to $1$ modulo $p$ and larger than $1$ is at least $p+1$, so
\[
q\ge p+1,
\]
a contradiction.

Hence $N_G(P)=G$, which is equivalent to $P\trianglelefteq G$.
This proves part (b).
:::

<1>4. If $N\trianglelefteq K$ and both $N$ and $K/N$ are solvable, then $K$ is solvable.
::: {.proof}
Choose $r,s\ge0$ such that
\[
(K/N)^{(r)}=1
\qquad\text{and}\qquad
N^{(s)}=1.
\]
For the quotient map $\pi:K\to K/N$,
\[
\pi\bigl(K^{(r)}\bigr)=(K/N)^{(r)}=1,
\]
so $K^{(r)}\le N$.
Therefore
\[
K^{(r+s)}=(K^{(r)})^{(s)}\le N^{(s)}=1.
\]
Thus $K$ is solvable.
:::

<1>5. Every finite $p$-group is solvable.
::: {.proof}
We induct on the order of a finite $p$-group $P$.
The trivial group is solvable.
If $P$ is nontrivial and abelian, it is solvable.
If $P$ is nonabelian, the class equation gives
\[
1<Z(P)<P.
\]
Both $Z(P)$ and $P/Z(P)$ are smaller $p$-groups, so they are solvable by induction.
Since $Z(P)\trianglelefteq P$, <1>4 implies that $P$ is solvable.
:::

<1>6. The prime-index condition on maximal subgroups passes from $G$ to every quotient $G/N$.
::: {.proof}
Let $N\trianglelefteq G$, and let $\overline M$ be a maximal subgroup of $G/N$.
Let $M$ be its inverse image in $G$.
Then
\[
N\le M<G.
\]
If $M<K<G$, then
\[
\overline M<K/N<G/N,
\]
contradicting maximality of $\overline M$.
Hence $M$ is maximal in $G$.
By hypothesis, $[G:M]$ is prime, and the correspondence theorem gives
\[
[G/N:\overline M]=[G:M].
\]
Thus every maximal subgroup of $G/N$ has prime index.
:::

<1>7. The group $G$ is solvable.
::: {.proof}
We induct on $|G|$.
The trivial group is solvable.

Assume $G\ne1$, let $p$ be the largest prime dividing $|G|$, and choose $P\in\operatorname{Syl}_p(G)$.
By <1>3,
\[
P\trianglelefteq G.
\]
By <1>5, the $p$-group $P$ is solvable.

By <1>6, the quotient $G/P$ again has the property that every maximal subgroup has prime index.
Since
\[
|G/P|<|G|,
\]
the induction hypothesis gives that $G/P$ is solvable.
Applying <1>4 to
\[
P\trianglelefteq G
\]
shows that $G$ is solvable.
This proves part (c).
:::

<1>8. Q.E.D.
::: {.proof}
<1>2, <1>3, and <1>7.
:::
:::
