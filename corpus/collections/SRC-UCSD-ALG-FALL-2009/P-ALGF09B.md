---
schema: qual/card@1
id: P-ALGF09B
kind: problem
title: "Normal subgroup and abelianness for a group of order p(p+1)"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 2 of the official UCSD Algebra Qualifying Examination, Fall 2009; both parts and all hypotheses agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the Sylow counting argument giving a unique normal subgroup H of order p+1, the semidirect-product decomposition, and the centralizer argument proving H is abelian.
---

::: {.problem}
Let $G$ be a group with $|G| = p(p+1)$, where $p$ is an odd prime and $(p+1) = 2^n$ is a power of 2. Suppose further that $G$ does not have a normal Sylow $p$-subgroup.

(a) Show that $G$ has a normal subgroup $H$ of order $p+1$.
Show that $G$ is isomorphic to a semidirect product $H \rtimes \mathbb{Z}_p$.

(b) Prove that the subgroup $H$ in part (a) is abelian.

Hint: Given a nonidentity element $x \in H$, consider the possible size of the centralizer subgroup $C_G(x)$.
:::

::: {.solution}
Write
\[
|G|=p(p+1)=p2^n.
\]

<1>1. The number of Sylow $p$-subgroups is $p+1$.
::: {.proof}
Let $n_p$ denote the number of Sylow $p$-subgroups.
By Sylow's theorem,
\[
n_p\mid p+1
\qquad\text{and}\qquad
n_p\equiv1\pmod p.
\]
Since $G$ has no normal Sylow $p$-subgroup, $n_p\neq1$.
Every divisor of $p+1$ lies between $1$ and $p+1$, and the only integers in that interval congruent to $1$ modulo $p$ are $1$ and $p+1$.
Hence
\[
n_p=p+1.
\]
:::

<1>2. A Sylow $2$-subgroup $H$ is unique, hence normal, and has order $p+1$.
::: {.proof}
Each Sylow $p$-subgroup has order $p$.
Distinct such subgroups intersect only in the identity, since an intersection of two groups of prime order is either trivial or the whole subgroup.
By <1>1, the Sylow $p$-subgroups therefore contain
\[
(p+1)(p-1)=p^2-1
\]
distinct nonidentity elements.

The group $G$ has
\[
p(p+1)=p^2+p
\]
elements altogether.
After removing those $p^2-1$ nonidentity $p$-elements, exactly
\[
(p^2+p)-(p^2-1)=p+1
\]
elements remain, including the identity.
Thus exactly $p$ nonidentity elements of $G$ do not lie in a Sylow $p$-subgroup.

Let $H$ be any Sylow $2$-subgroup.
Then
\[
|H|=2^n=p+1,
\]
so $H$ has exactly $p$ nonidentity elements.
None of them can lie in a subgroup of order $p$, because a $2$-group and a group of order $p$ have trivial intersection.
Hence the $p$ nonidentity elements of $H$ are precisely all of the nonidentity elements left over above.
This description is independent of the choice of Sylow $2$-subgroup, so every Sylow $2$-subgroup has the same elements.
Therefore $H$ is unique and hence normal in $G$.
:::

<1>3. One has
\[
G\cong H\rtimes\mathbb Z_p.
\]
::: {.proof}
Let $P$ be a Sylow $p$-subgroup.
Then $|P|=p$, so
\[
P\cong\mathbb Z_p.
\]
Since $|H|=p+1$ and $|P|=p$ are coprime,
\[
H\cap P=1.
\]
Because $H\triangleleft G$, the product $HP$ is a subgroup, and
\[
|HP|=\frac{|H||P|}{|H\cap P|}=p(p+1)=|G|.
\]
Thus $G=HP$.
Therefore $G$ is the internal semidirect product
\[
G=H\rtimes P\cong H\rtimes\mathbb Z_p.
\]
:::

<1>4. If $1\neq x\in H$, then $p$ does not divide $|C_G(x)|$.
::: {.proof}
Suppose instead that $p\mid |C_G(x)|$.
By Cauchy's theorem, $C_G(x)$ contains an element $y$ of order $p$.
Let
\[
P:=\langle y\rangle.
\]
Then $x$ centralizes $P$, hence normalizes $P$, so
\[
x\in N_G(P).
\]
By <1>1,
\[
[G:N_G(P)]=n_p=p+1,
\]
and therefore
\[
|N_G(P)|=p.
\]
Since $P\subseteq N_G(P)$ also has order $p$, one has
\[
N_G(P)=P.
\]
Thus $x\in P$.
But $x\in H$ and $H\cap P=1$, contradicting $x\neq1$.
Hence $p\nmid |C_G(x)|$.
:::

<1>5. The subgroup $H$ is abelian.
::: {.proof}
Fix $1\neq x\in H$.
Because $H\triangleleft G$, every conjugate of $x$ lies in $H$.
Hence the conjugacy class of $x$ has at most
\[
|H|-1=p
\]
elements.
By <1>4, the centralizer $C_G(x)$ has order a power of $2$, say $2^k$ with $0\le k\le n$.
The orbit-stabilizer formula for conjugation gives
\[
|x^G|=[G:C_G(x)]
=\frac{p2^n}{2^k}
=p2^{n-k}.
\]
Since $|x^G|\le p$, necessarily $k=n$.
Thus
\[
|C_G(x)|=2^n=|H|.
\]
The centralizer is a $2$-subgroup, so by uniqueness of the Sylow $2$-subgroup from <1>2,
\[
C_G(x)=H.
\]
Therefore $x$ commutes with every element of $H$.
Since this holds for every nonidentity $x\in H$ (and trivially for $x=1$),
\[
H=Z(H),
\]
so $H$ is abelian.
:::
:::
