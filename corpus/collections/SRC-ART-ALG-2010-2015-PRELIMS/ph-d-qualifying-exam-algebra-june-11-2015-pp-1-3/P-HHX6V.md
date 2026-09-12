---
schema: qual/card@1
id: P-HHX6V
kind: problem
title: Direct summands are pure; a pure submodule of a finitely generated torsion
  module over a PID is a direct summand
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the stated single-equation definition of purity and all three parts with June 2015 Rings 2 in the retained extraction; corrected the algebra and PID classification."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the projection argument, equality of annihilator ideals over the arbitrary ring, and a well-defined section on each cyclic quotient summand, including the zero quotient."
---

::: {.problem}
Let $D$ be a commutative ring with unit.
A submodule $N$ of the $D$-module $M$ is said to be pure in $M$ just in case for every $y \in N$ and $a \in D$, $ax = y$ is solvable in $N$ if solvable in $M$.

a. Show that if $N$ is a direct summand of $M$ then $N$ is pure in $M$.

b. Show that if $N$ is pure in $M$, $z \in M$, and $\mathrm{ann}(z+N) = (d)$, then there is $w \in M$ with $z+N = w+N$ and $\mathrm{ann}(w) = (d)$.

c. Show that if $N$ is pure in $M$, $M$ is a finitely generated torsion module, and $D$ is a p.i.d., then $N$ is a direct summand of $M$.
:::

::: solution
For an element $v$ of a $D$-module, write
$\operatorname{ann}_D(v)=\{a\in D:av=0\}$.
We use exactly the single-equation definition of purity in the question.

<1>1. A direct summand is pure, proving part (a).

::: proof
Suppose $M=N\oplus N'$ and let $\pi:M\to N$ be the projection
onto $N$. It is $D$-linear and restricts to the identity on $N$.
If $y\in N$, $a\in D$, and $ax=y$ has a solution $x\in M$,
then
$$
a\pi(x)=\pi(ax)=\pi(y)=y.
$$
Thus $\pi(x)\in N$ solves the same equation, as required.
:::

<1>2. A coset with principal annihilator has a representative
with that same annihilator, proving part (b).

::: proof
Since $d\in\operatorname{ann}_D(z+N)$, the element $dz$ lies
in $N$. The equation $dx=dz$ has the solution $z\in M$.
Purity supplies a solution $n\in N$. Put $w=z-n$.
Then $w+N=z+N$ and $dw=dz-dn=0$, so
$(d)\subseteq\operatorname{ann}_D(w)$.

Conversely, if $aw=0$, then
$a(z+N)=a(w+N)=0$ in $M/N$. Thus
$a\in\operatorname{ann}_D(z+N)=(d)$.
This proves the reverse inclusion and hence
$\operatorname{ann}_D(w)=(d)$.
No assumption that $d$ is nonzero or a nonunit is needed.
:::

<1>3. Under the hypotheses in part (c), the quotient map
$q:M\to M/N$ admits a $D$-linear section.

::: proof
The quotient $Q=M/N$ is finitely generated, by the images of a
finite generating set of $M$. It is torsion: a nonzero scalar
annihilating a representative also annihilates its coset.
The structure theorem over the PID $D$ therefore gives
$$
Q\cong\bigoplus_{i=1}^r D/(d_i)
$$
for nonzero nonunits $d_i\in D$ [@DF04]. The empty sum is
allowed when $Q=0$. Let $u_i\in Q$ correspond to $1$ in the
$i$th cyclic summand, so $\operatorname{ann}_D(u_i)=(d_i)$.
Choose $z_i\in M$ with $q(z_i)=u_i$. By step <1>2, there is
$w_i\in M$ with $q(w_i)=u_i$ and
$\operatorname{ann}_D(w_i)=(d_i)$.

Define
$$
s:Q\longrightarrow M,\qquad
s\left(\sum_{i=1}^r a_i u_i\right)=\sum_{i=1}^r a_i w_i.
$$
In the displayed direct sum, two coefficient lists represent the
same element exactly when their $i$th coefficients differ by a
multiple of $d_i$ for every $i$. Since $d_iw_i=0$, those changes
do not change the proposed value of $s$. Thus $s$ is well-defined
and $D$-linear. Moreover $q(s(u_i))=u_i$ for all generators,
so $q\circ s=\operatorname{id}_Q$. For $Q=0$, the zero map is
the required section.
:::

<1>4. The section yields the direct summand in part (c).

::: proof
For every $m\in M$,
$$
m=(m-s(q(m)))+s(q(m)),
$$
where the first term lies in $\ker q=N$ and the second in
$s(Q)$. If $s(u)\in N$, applying $q$ gives
$u=q(s(u))=0$, and hence $s(u)=0$.
Therefore $N\cap s(Q)=0$ and $M=N\oplus s(Q)$.
:::
:::
