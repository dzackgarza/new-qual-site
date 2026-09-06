---
schema: qual/card@1
id: P-AMD-2BZTOEMW
kind: problem
title: A group of order $p(p+1)$ has a normal subgroup of order $p$ or $p+1$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 4, Exercise 7. Restored
    that p is prime and retained the source hint's centralizer/conjugacy-class
    route for the case with more than one Sylow p-subgroup.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Sylow congruence gives n_p=1 or p+1. In the second case the p+1 Sylow
    p-subgroups account for p^2-1 nonidentity elements, leaving exactly p
    nonidentity elements of order different from p. For such an x, the
    self-normalizing Sylow p-subgroups imply C_G(x) has no p-torsion. Hence
    the conjugacy class of x has size divisible by p but at most p, so it has
    size p and |C_G(x)|=p+1. This centralizer is exactly the conjugacy-invariant
    complement of the elements of order p, and is therefore normal.
---

::: {.problem}
Let $p$ be a prime and let $G$ be a finite group with
\[
|G|=p(p+1).
\]
Prove that $G$ has either a normal subgroup of order $p$ or a normal subgroup of order $p+1$.
:::

::: {.solution}
Let $n_p$ denote the number of Sylow $p$-subgroups of $G$.

<1>1. One has
\[
n_p\in\{1,p+1\}.
\]
::: {.proof}
Since $p$ occurs to the first power in $|G|=p(p+1)$, a Sylow $p$-subgroup has order $p$.
Sylow's theorem gives
\[
n_p\equiv1\pmod p
\qquad\text{and}\qquad
n_p\mid p+1.
\]
In particular,
\[
1\le n_p\le p+1.
\]
The only positive integers in this interval congruent to $1$ modulo $p$ are $1$ and $p+1$.
Hence
\[
n_p\in\{1,p+1\}.
\]
:::

<1>2. If $n_p=1$, then $G$ has a normal subgroup of order $p$.
::: {.proof}
The unique Sylow $p$-subgroup is normal and has order $p$.
:::

Assume from now on that
\[
n_p=p+1.
\]

<1>3. Distinct Sylow $p$-subgroups intersect trivially, and their nonidentity elements account for exactly
\[
(p+1)(p-1)=p^2-1
\]
elements of $G$.
::: {.proof}
Every Sylow $p$-subgroup has prime order $p$.
Two distinct subgroups of order $p$ can intersect only in the identity, since a nontrivial intersection would have order $p$ and force the subgroups to be equal.
Thus the $p+1$ Sylow $p$-subgroups have pairwise disjoint sets of $p-1$ nonidentity elements.
Their union therefore contains
\[
(p+1)(p-1)=p^2-1
\]
nonidentity elements.
:::

<1>4. Exactly $p$ nonidentity elements of $G$ have order different from $p$.
::: {.proof}
The group has
\[
|G|=p^2+p
\]
elements.
By <1>3, exactly $p^2-1$ of them are nonidentity elements of order $p$.
After removing those elements and the identity, the number remaining is
\[
p^2+p-(p^2-1)-1=p.
\]
These remaining elements are precisely the nonidentity elements whose order is not $p$.
:::

<1>5. For every Sylow $p$-subgroup $P$ of $G$,
\[
N_G(P)=P.
\]
::: {.proof}
By the orbit-stabilizer formula for the conjugation action of $G$ on its Sylow $p$-subgroups,
\[
[G:N_G(P)]=n_p=p+1.
\]
Therefore
\[
|N_G(P)|=\frac{|G|}{p+1}=p.
\]
Since $P\le N_G(P)$ and $|P|=p$, it follows that
\[
N_G(P)=P.
\]
:::

<1>6. Choose a nonidentity element $x\in G$ whose order is not $p$.
Then $C_G(x)$ contains no nonidentity element of order $p$.
::: {.proof}
Such an $x$ exists by <1>4. Suppose, for contradiction, that $y\in C_G(x)$ has order $p$.
Then
\[
P=\langle y\rangle
\]
is a Sylow $p$-subgroup of $G$.
Because $x$ commutes with $y$, it normalizes $P$, so
\[
x\in N_G(P).
\]
By <1>5,
\[
N_G(P)=P.
\]
Hence $x\in P$, forcing $x$ to have order $1$ or $p$, contrary to the choice of $x$.
Therefore $C_G(x)$ has no nonidentity element of order $p$.
:::

<1>7. The order of $C_G(x)$ is not divisible by $p$ and hence divides $p+1$.
::: {.proof}
If $p$ divided $|C_G(x)|$, Cauchy's theorem would give an element of order $p$ in $C_G(x)$, contradicting <1>6. Thus
\[
p\nmid |C_G(x)|.
\]
Since $C_G(x)\le G$, Lagrange's theorem gives
\[
|C_G(x)|\mid p(p+1).
\]
Because $p$ is coprime to $p+1$ and does not divide $|C_G(x)|$, it follows that
\[
|C_G(x)|\mid p+1.
\]
:::

<1>8. The conjugacy class of $x$ has exactly $p$ elements, and
\[
|C_G(x)|=p+1.
\]
::: {.proof}
The conjugacy-class formula gives
\[
|x^G|=[G:C_G(x)]=\frac{p(p+1)}{|C_G(x)|}.
\]
By <1>7, $|C_G(x)|$ divides $p+1$, so $|x^G|$ is divisible by $p$.
Conjugation preserves element order, so every element of $x^G$ is nonidentity and has order different from $p$.
By <1>4 there are exactly $p$ such elements in all of $G$.
Therefore
\[
|x^G|\le p.
\]
Since $|x^G|$ is a positive multiple of $p$, one must have
\[
|x^G|=p.
\]
Consequently
\[
|C_G(x)|=\frac{|G|}{|x^G|}
=\frac{p(p+1)}p
=p+1.
\]
:::

<1>9. The subgroup $C_G(x)$ consists exactly of the identity together with all elements of $G$ whose order is not $p$.
::: {.proof}
By <1>6, every nonidentity element of $C_G(x)$ has order different from $p$.
By <1>8,
\[
|C_G(x)|=p+1,
\]
so $C_G(x)$ contains exactly $p$ nonidentity elements.
By <1>4, the whole group $G$ has exactly $p$ nonidentity elements whose order is not $p$.
Hence $C_G(x)$ contains all of them.
:::

<1>10. The subgroup $C_G(x)$ is normal in $G$.
::: {.proof}
Let
\[
S=\{1\}\cup\{g\in G:\operatorname{ord}(g)\ne p\}.
\]
By <1>9,
\[
C_G(x)=S.
\]
Conjugation preserves element order, so $S$ is invariant under conjugation by every element of $G$.
Therefore
\[
C_G(x)\normal G.
\]
:::

<1>11. The group $G$ has a normal subgroup of order $p$ or $p+1$.
::: {.proof}
If $n_p=1$, <1>2 gives a normal subgroup of order $p$.
If $n_p=p+1$, <1>8 and <1>10 give the normal subgroup $C_G(x)$ of order $p+1$.
Thus one of the required normal subgroups always exists.
:::
:::
