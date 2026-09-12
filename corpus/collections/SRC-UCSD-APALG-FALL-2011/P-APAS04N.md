---
schema: qual/card@1
id: P-APAS04N
kind: problem
title: Permutation representation from cosets; fixed-point character on $S_n$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Permutations
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

::: problem
Let $H$ be a subgroup of $G$ and let $G=\tau_1 H+\cdots+\tau_k H$ be its coset decomposition.
Define a permutation representation $L$ of $G$ by
\begin{align}
\sigma\langle\tau_1 H,\ldots,\tau_k H\rangle
&=\langle\sigma\tau_1 H,\ldots,\sigma\tau_k H\rangle\\
&=\langle\tau_1 H,\ldots,\tau_k H\rangle L(\sigma)
\end{align}
so that $L(\sigma)_{i,j}=\chi(\tau_i H=\sigma\tau_j H)$.

(a) Prove that $L$ is a representation.

(b) Consider the special case where $G=S_n$ and $H=S_{n-1}\times S_1=\{\sigma\in S_n:\sigma(n)=n\}$.

(i) Show that the coset decomposition of $G$ relative to $H$ is given by
\[
G=H+(1,n)H+\cdots+(n-1,n)H
\]
where $(i,n)$ denotes the transposition which interchanges $i$ and $n$.

(ii) Show that $\chi^L(\sigma)=\operatorname{fix}(\sigma)$ where $\operatorname{fix}(\sigma)$ denotes the number of fixed points of $\sigma$.

(c) In the special case where $G=S_4$ and $H=S_3\times S_1$, use part (b) to decompose $L$ as a sum of irreducible representations of $S_4$.
:::

::: {.solution}
<1>1. The matrices $L(\sigma)$ define a representation of $G$ on the set of left cosets $G/H$.
::: {.proof}
Left multiplication gives an action
\[
G\times G/H\to G/H,\qquad (\sigma,\tau H)\mapsto \sigma\tau H.
\]
Relative to the ordered coset basis $(\tau_1H,\ldots,\tau_kH)$, the matrix $L(\sigma)$ is exactly the permutation matrix of this action: its $j$-th column has a $1$ in the unique row $i$ such that
\[
\sigma\tau_jH=\tau_iH.
\]
Because left multiplication satisfies
\[
(\sigma\rho)(\tau H)=\sigma(\rho(\tau H)),
\]
the corresponding permutation matrices satisfy
\[
L(\sigma\rho)=L(\sigma)L(\rho),
\qquad L(e)=I.
\]
Thus $L$ is a representation. This proves part (a).
:::

<1>2. For $G=S_n$ and $H=\{\sigma:\sigma(n)=n\}$, two permutations $\tau,\rho$ lie in the same left coset modulo $H$ if and only if
\[
\tau(n)=\rho(n).
\]
::: {.proof}
One has
\[
\tau H=\rho H
\iff \rho^{-1}\tau\in H
\iff (\rho^{-1}\tau)(n)=n
\iff \tau(n)=\rho(n).
\]
:::

<1>3. Hence
\[
S_n=H+(1,n)H+\cdots+(n-1,n)H.
\]
::: {.proof}
The representative $e$ sends $n$ to $n$, while $(i,n)$ sends $n$ to $i$. Thus the displayed $n$ representatives have pairwise distinct images of $n$. By <1>2 they lie in distinct left cosets. Since
\[
[S_n:H]=\frac{n!}{(n-1)!}=n,
\]
they form all left cosets. This proves part (b)(i).
:::

<1>4. For every $\sigma\in S_n$,
\[
\chi^L(\sigma)=\operatorname{fix}(\sigma).
\]
::: {.proof}
The trace of a permutation matrix is the number of basis vectors fixed by the permutation. Thus $\chi^L(\sigma)$ is the number of cosets $\tau H$ such that
\[
\sigma\tau H=\tau H.
\]
By <1>2, this is equivalent to
\[
\sigma(\tau(n))=\tau(n).
\]
As $\tau H$ runs through the cosets, the values $\tau(n)$ run once through $\{1,\ldots,n\}$. Hence fixed cosets are in bijection with fixed points of $\sigma$, proving part (b)(ii).
:::

<1>5. For $S_4$, the permutation module is
\[
\mathbb C^4=\mathbb C(1,1,1,1)\oplus W,
\qquad
W=\{(x_1,x_2,x_3,x_4):x_1+x_2+x_3+x_4=0\}.
\]
Both summands are $S_4$-stable; the first is the trivial representation and $W$ has character
\[
\chi_W=\operatorname{fix}-1.
\]
::: {.proof}
Permuting coordinates fixes $(1,1,1,1)$ and preserves the sum of coordinates, so both subspaces are invariant. Their dimensions are $1$ and $3$, and their direct sum is all of $\mathbb C^4$. By <1>4, the full permutation character is $\operatorname{fix}$, so subtracting the trivial character gives $\chi_W=\operatorname{fix}-1$.
:::

<1>6. The representation $W$ is irreducible and is $A^{(3,1)}$. Therefore
\[
L\cong A^{(4)}\oplus A^{(3,1)}.
\]
::: {.proof}
On the five conjugacy classes of $S_4$ of cycle types
\[
(1^4),(2,1^2),(2^2),(3,1),(4),
\]
the character $\chi_W=\operatorname{fix}-1$ has values
\[
3,1,-1,0,-1.
\]
The class sizes are $1,6,3,8,6$, so
\[
\langle\chi_W,\chi_W\rangle
=\frac1{24}\left(9+6+3+0+6\right)=1.
\]
Hence $W$ is irreducible. The unique irreducible of $S_4$ with partition label $(3,1)$ has dimension $3$ and this character, so $W\cong A^{(3,1)}$; the constant line is $A^{(4)}$. This proves part (c).
:::
:::
