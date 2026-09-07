---
schema: qual/card@1
id: P-ALGF20B
kind: problem
title: Characteristic Hall subgroup of odd order when Sylow $2$-subgroup is cyclic
classification:
  areas:
  - algebra
  topics:
  - Group Theory
  - Sylow Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 2 of the official UCSD Algebra Qualifying Exam, Fall 2020 source; the order hypothesis and cyclic Sylow 2-subgroup hypothesis agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the Burnside-transfer argument for a normal odd-order complement and the uniqueness argument making that complement characteristic.
---

::: problem
Suppose that $G$ is a group with $|G| = 2^k m$, where $m$ is odd and $k \geq 0$.
Assume that $G$ has a cyclic Sylow $2$-subgroup.
Prove that $G$ has a characteristic subgroup $H$ which has order $m$.
:::

::: {.solution}
Let $P$ be a cyclic Sylow $2$-subgroup of $G$, so
\[
|P|=2^k.
\]

<1>1. If $k=0$, the conclusion holds with $H=G$.
::: {.proof}
In this case $|G|=m$, and $G$ is characteristic in itself.
Hence assume from now on that $k\ge 1$.
:::

<1>2. The normalizer of $P$ centralizes $P$:
\[
N_G(P)=C_G(P).
\]
::: {.proof}
Conjugation gives an injective homomorphism
\[
N_G(P)/C_G(P)\hookrightarrow \operatorname{Aut}(P).
\]
Since $P$ is cyclic of order $2^k$,
\[
|\operatorname{Aut}(P)|=\varphi(2^k),
\]
which is a power of $2$.

On the other hand, $P\subseteq C_G(P)$ because $P$ is abelian, and $P$ is a Sylow $2$-subgroup of $N_G(P)$. Therefore
\[
[N_G(P):C_G(P)]\mid [N_G(P):P],
\]
and the latter index is odd. Thus $[N_G(P):C_G(P)]$ is both a power of $2$ and odd, so it equals $1$.
:::

<1>3. If two elements of $P$ are conjugate in $G$, then they are equal.
::: {.proof}
Suppose $a\in P$ and $g^{-1}ag\in P$. Put
\[
b=g^{-1}ag.
\]
Because $P$ is cyclic, it is abelian, so $P\le C_G(b)$. Also $g^{-1}Pg\le C_G(b)$, since $P\le C_G(a)$. Both $P$ and $g^{-1}Pg$ have order $2^k$, hence both are Sylow $2$-subgroups of $C_G(b)$.

By the Sylow conjugacy theorem inside $C_G(b)$, there exists $c\in C_G(b)$ such that
\[
c^{-1}(g^{-1}Pg)c=P.
\]
Thus $gc\in N_G(P)$. By <1>2, $gc\in C_G(P)$, so
\[
a=(gc)^{-1}a(gc)=c^{-1}g^{-1}agc=c^{-1}bc=b.
\]
Hence conjugacy inside $G$ does not fuse distinct elements of $P$.
:::

<1>4. The transfer homomorphism
\[
V:G\longrightarrow P
\]
is surjective.
::: {.proof}
Since $P$ is abelian, the transfer from $G$ to $P/P'$ takes values in $P$ itself. For $u\in P$, decompose the right cosets of $P$ in $G$ into orbits under right multiplication by the cyclic group $\langle u\rangle$. If an orbit has length $r$, the corresponding factor in the transfer formula is a $G$-conjugate of $u^r$ which lies in $P$.

By <1>3, that conjugate must equal $u^r$. Multiplying over all orbits therefore gives
\[
V(u)=u^{\sum r}=u^{[G:P]}=u^m.
\]
Because $m$ is odd and $|P|=2^k$, the map
\[
P\longrightarrow P,
\qquad
u\longmapsto u^m
\]
is an automorphism of the cyclic group $P$. Hence the restriction $V|_P$ is surjective, and therefore $V$ is surjective.
:::

<1>5. The kernel
\[
H:=\ker V
\]
is a normal subgroup of order $m$.
::: {.proof}
By <1>4, $V$ is a surjective homomorphism onto $P$, so the first isomorphism theorem gives
\[
[G:H]=|P|=2^k.
\]
Consequently
\[
|H|=\frac{|G|}{2^k}=m.
\]
As a kernel, $H$ is normal in $G$.
:::

<1>6. The subgroup $H$ is characteristic in $G$.
::: {.proof}
First, $H$ is the unique normal subgroup of $G$ having order $m$. Indeed, if $K\trianglelefteq G$ also has order $m$, then $HK$ is a subgroup because both $H$ and $K$ are normal, and
\[
|HK|=\frac{|H||K|}{|H\cap K|}
\]
is odd. Since the largest odd divisor of $|G|=2^k m$ is $m$, we have $|HK|\le m$. But $H\subseteq HK$ and $|H|=m$, so $HK=H$, whence $K\subseteq H$. Equal orders give $K=H$.

Every automorphism of $G$ sends a normal subgroup of order $m$ to another normal subgroup of order $m$. By uniqueness it fixes $H$. Therefore $H$ is characteristic.
:::
:::
