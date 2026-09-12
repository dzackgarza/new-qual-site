---
schema: qual/card@1
id: P-ZJT5A
kind: problem
title: Fundamental theorem of Galois theory, and the splitting field of $x^5-2$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Field Extensions
relations: []
review: draft
---

::: problem
What is Galois theory?
State the main theorem.
What is the splitting field of $x^5 - 2$ over $\QQ$?
What are the intermediate extensions?
Which extensions are normal, which are not, and why?
What are the Galois groups (over Q) of all intermediate extensions?
:::


::: {.solution}
Let
\[
\alpha=2^{1/5},\qquad \zeta=\zeta_5.
\]
The roots of $x^5-2$ are $\alpha,\zeta\alpha,\ldots,\zeta^4\alpha$, so its splitting field is
\[
L=\QQ(\alpha,\zeta).
\]
By Eisenstein at $2$, $[\QQ(\alpha):\QQ]=5$. The intersection $\QQ(\alpha)\cap\QQ(\zeta)$ has degree over $\QQ$ dividing both $[\QQ(\alpha):\QQ]=5$ and $[\QQ(\zeta):\QQ]=4$. Hence the intersection is $\QQ$, and therefore
\[
[L:\QQ]=20.
\]

Define
\[
\sigma(\alpha)=\zeta\alpha,\quad \sigma(\zeta)=\zeta,
\qquad
\tau(\alpha)=\alpha,\quad \tau(\zeta)=\zeta^2.
\]
Then
\[
\sigma^5=\tau^4=1,\qquad \tau\sigma\tau^{-1}=\sigma^2,
\]
so
\[
G:=\Gal(L/\QQ)\cong C_5\rtimes C_4.
\]

The fundamental theorem of Galois theory gives an inclusion-reversing bijection
\[
\{\QQ\subseteq E\subseteq L\}
\longleftrightarrow
\{H\le G\},
\qquad E=L^H.
\]
Moreover $E/\QQ$ is Galois exactly when $H\normal G$, in which case
\[
\Gal(E/\QQ)\cong G/H.
\]

The subgroups of $G$ are as follows.

<1>1. $G$ itself fixes $\QQ$.

<1>2. There is a unique subgroup of order $10$,
\[
H_{10}=\langle\sigma,\tau^2\rangle\cong D_{10}.
\]
It is normal of index $2$, and its fixed field is the unique quadratic subfield of $\QQ(\zeta)$:
\[
L^{H_{10}}=\QQ(\sqrt5).
\]
Thus $\Gal(\QQ(\sqrt5)/\QQ)\cong C_2$.

<1>3. The unique Sylow $5$-subgroup
\[
H_5=\langle\sigma\rangle\cong C_5
\]
is normal. Its fixed field is
\[
L^{H_5}=\QQ(\zeta),
\]
so
\[
\Gal(\QQ(\zeta)/\QQ)\cong C_4.
\]

<1>4. There are five conjugate subgroups of order $4$,
\[
H_{4,j}=\sigma^j\langle\tau\rangle\sigma^{-j}
\qquad(0\le j<5).
\]
Their fixed fields are the five conjugate degree-$5$ fields
\[
E_j=\QQ(\zeta^j\alpha).
\]
None is normal over $\QQ$. Since each $H_{4,j}$ is self-normalizing,
\[
\Aut_{\QQ}(E_j)\cong N_G(H_{4,j})/H_{4,j}=1.
\]

<1>5. There are five conjugate subgroups of order $2$,
\[
H_{2,j}=\sigma^j\langle\tau^2\rangle\sigma^{-j}.
\]
For $j=0$ the fixed field is
\[
F_0=\QQ\bigl(\alpha,\zeta+\zeta^{-1}\bigr),
\]
and the other four are its conjugates
\[
F_j=\QQ\bigl(\zeta^j\alpha,\zeta+\zeta^{-1}\bigr).
\]
Each has degree $10$ over $\QQ$ and is not normal. The normalizer of $H_{2,j}$ has order $4$, so
\[
\Aut_{\QQ}(F_j)\cong C_2.
\]

<1>6. The trivial subgroup fixes $L$ itself, and
\[
\Gal(L/\QQ)\cong C_5\rtimes C_4.
\]

Thus the normal intermediate extensions are exactly
\[
\QQ,\qquad \QQ(\sqrt5),\qquad \QQ(\zeta_5),\qquad L,
\]
while the five degree-$5$ and five degree-$10$ intermediate fields are nonnormal.
:::
