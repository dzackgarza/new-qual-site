---
schema: qual/card@1
id: P-APAF21J
kind: problem
title: Conjugacy-class scalars $\omega_\alpha^\lambda$ in Specht modules; the case $\alpha=(d)$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
(a) Given a Young diagram $\alpha\vdash d$, identify the corresponding conjugacy class $C_\alpha\subset S(d)$ with the formal sum of its elements, so that it becomes an element of the group algebra $\mathbb{C}S(d)$.
Given another Young diagram $\lambda\vdash d$, show that $C_\alpha$ acts in the corresponding irreducible representation $V^\lambda$ of $\mathbb{C}S(d)$ as multiplication by a scalar $\omega_\alpha^\lambda$, and express this number in terms of the character of $V^\lambda$.

(b) Compute $\omega_\alpha^\lambda$ explicitly in the case that $\alpha=(d)$ is the Young diagram consisting of a single row of $d$ cells.
:::

::: {.solution}
For a partition
\[
\alpha=(1^{m_1}2^{m_2}\cdots)\vdash d,
\]
write
\[
z_\alpha=\prod_{j\ge1}j^{m_j}m_j!.
\]
Then the conjugacy class of cycle type $\alpha$ has size
\[
|C_\alpha|=\frac{d!}{z_\alpha}.
\]

<1>1. The class sum
\[
C_\alpha:=\sum_{g\in C_\alpha}g\in\mathbb C S_d
\]
is central in the group algebra.
::: {.proof}
For every $h\in S_d$,
\[
hC_\alpha h^{-1}
=\sum_{g\in C_\alpha}hgh^{-1}.
\]
Conjugation by $h$ permutes the elements of the conjugacy class $C_\alpha$, so the right-hand side is again $C_\alpha$. Thus $hC_\alpha=C_\alpha h$ for every $h$, hence $C_\alpha\in Z(\mathbb C S_d)$.
:::

<1>2. On the irreducible module $V^\lambda$, the class sum $C_\alpha$ acts by a scalar:
\[
\rho_\lambda(C_\alpha)=\omega_\alpha^\lambda I.
\]
::: {.proof}
By <1>1, the operator $\rho_\lambda(C_\alpha)$ commutes with every $\rho_\lambda(h)$ for $h\in S_d$. Since $V^\lambda$ is irreducible over $\mathbb C$, Schur's lemma implies that every such commuting endomorphism is scalar.
:::

<1>3. The scalar is
\[
\boxed{
\omega_\alpha^\lambda
=\frac{|C_\alpha|\chi^\lambda(\alpha)}{\chi^\lambda(1)}
=\frac{d!}{z_\alpha}\frac{\chi^\lambda(\alpha)}{f^\lambda},}
\]
where $f^\lambda=\dim V^\lambda=\chi^\lambda(1)$.
::: {.proof}
Take traces in the identity from <1>2. On one hand,
\[
\operatorname{tr}(\rho_\lambda(C_\alpha))
=\sum_{g\in C_\alpha}\chi^\lambda(g)
=|C_\alpha|\chi^\lambda(\alpha),
\]
because the character is constant on conjugacy classes. On the other hand,
\[
\operatorname{tr}(\omega_\alpha^\lambda I)
=\omega_\alpha^\lambda\dim V^\lambda.
\]
Equating the two traces gives the formula.
:::

<1>4. Suppose now that $\alpha=(d)$, so $C_{(d)}$ is the class of $d$-cycles. Then
\[
|C_{(d)}|=(d-1)!.
\]
::: {.proof}
For the partition $(d)$ one has $m_d=1$ and all other $m_j=0$, so
\[
z_{(d)}=d.
\]
Hence
\[
|C_{(d)}|=\frac{d!}{d}=(d-1)!.
\]
:::

<1>5. The irreducible character value on a $d$-cycle is
\[
\chi^\lambda((d))=
\begin{cases}
(-1)^r,&\lambda=(d-r,1^r)\text{ for some }0\le r\le d-1,\\
0,&\text{otherwise}.
\end{cases}
\]
::: {.proof}
Apply the Murnaghan--Nakayama rule to a permutation consisting of one cycle of length $d$. One must remove a rim hook of length $d$ from the Young diagram of $\lambda$, leaving the empty diagram. Thus the whole diagram of $\lambda$ must itself be a rim hook.

A Young diagram is a rim hook precisely when it is connected and contains no $2\times2$ square. For a partition diagram this is equivalent to being a hook
\[
\lambda=(d-r,1^r).
\]
Such a hook has height $r+1$, so Murnaghan--Nakayama assigns the sign
\[
(-1)^{(r+1)-1}=(-1)^r.
\]
If $\lambda$ is not a hook there is no admissible rim-hook removal, so the character value is $0$.
:::

<1>6. For a hook partition $\lambda=(d-r,1^r)$,
\[
f^\lambda=\binom{d-1}{r}.
\]
::: {.proof}
By the hook-length formula,
\[
f^\lambda=\frac{d!}{\prod_{u\in\lambda}h(u)}.
\]
For the hook $(d-r,1^r)$, the corner box has hook length $d$; the remaining boxes in the first row have hook lengths
\[
d-r-1,d-r-2,\ldots,1,
\]
and the remaining boxes in the first column have hook lengths
\[
r,r-1,\ldots,1.
\]
Therefore
\[
\prod_{u\in\lambda}h(u)=d(d-r-1)!r!,
\]
so
\[
f^\lambda
=\frac{d!}{d(d-r-1)!r!}
=\frac{(d-1)!}{(d-1-r)!r!}
=\binom{d-1}{r}.
\]
:::

<1>7. Hence for the class of $d$-cycles,
\[
\boxed{
\omega_{(d)}^\lambda=
\begin{cases}
(-1)^r r!(d-1-r)!,&\lambda=(d-r,1^r),\\
0,&\lambda\text{ is not a hook}.
\end{cases}}
\]
::: {.proof}
If $\lambda$ is not a hook, <1>5 gives $\chi^\lambda((d))=0$, so <1>3 gives $\omega_{(d)}^\lambda=0$.
For $\lambda=(d-r,1^r)$, combine <1>3--<1>6:
\[
\omega_{(d)}^\lambda
=\frac{(d-1)!(-1)^r}{\binom{d-1}{r}}
=(-1)^r r!(d-1-r)!.
\]
:::
:::
