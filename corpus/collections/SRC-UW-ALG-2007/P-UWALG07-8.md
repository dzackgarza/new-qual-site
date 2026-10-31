---
schema: qual/card@1
id: P-UWALG07-8
kind: problem
title: Unit quaternions, $\SU(2)$, and $\SU(2)/U(1)\cong S^2$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Let $\quaternions$ be the ring of quaternions with standard basis $1,i,j,k$ and identify $\CC$ with the subring $\RR+\RR i$ of $\quaternions$.

(a) Use the action of $\quaternions$ on itself by left multiplication to explain why there is a ring homomorphism $\varphi:\quaternions\to M_2(\CC)$, where $M_2(\CC)$ denotes the ring of $2\times2$ matrices.
(Warning: there are two ways to view $\quaternions$ as a $\CC$-vector space, through right and left multiplication by elements in the subring $\RR+\RR i$.)

(b) Say why $\varphi$ is injective.

(c) The special unitary group $\SU(2)$ consists of all $2\times2$ complex matrices $u$ such that $\det(u)=1$ and $uu^*=u^*u=1$ where $u^*$ is the conjugate transpose, i.e., the transpose of the matrix whose entries are the complex conjugates of the entries in $u$.
Show that $\varphi$ restricts to an isomorphism between the group of unit quaternions (those of length one) and $\SU(2)$.

(d) Use this to prove that $\SU(2)$ acts transitively on the Riemann sphere $\CC\PP^1$ defined as the $1$-dimensional subspaces in $\CC^2$.
(Hint: use the action of $M_2(\CC)$ on $\CC^2$ by left multiplication.)

(e) Let $U(1)$ denote the image in $\SU(2)$ of the multiplicative subgroup of $\CC-\{0\}$ consisting of the complex numbers $z\in\CC\subset\quaternions$ of length one.
Show that the coset space $\SU(2)/U(1)$ is isomorphic to the $2$-sphere $S^2$.

Remark.
The solution to this problem gives a realization of the Hopf fibration $S^3\to S^2$ with fibers $S^1$ because the group of unit quaternions is isomorphic to the $3$-sphere $S^3$.
:::

::: {.solution}
Write $\quaternions=\{a+jb: a,b\in\CC\}$ with $j^2=-1$ and $jc=\overline c\,j$ for $c\in\CC$, so that with $b=x_2-x_3i$,
$$
a+jb=(x_0+x_1i)+j(x_2-x_3i)=x_0+x_1i+x_2j+x_3k
$$
is the usual quaternion.
The pair $(a,b)$ holds *right* $\CC$-coordinates: $1$ and $j$ are a $\CC$-basis of $\quaternions$ as a right $\CC$-vector space, every element being uniquely $1\cdot\alpha+j\cdot\beta$, and right multiplication by $\lambda\in\CC$ sends $(\alpha,\beta)$ to $(\alpha\lambda,\beta\lambda)$.
Multiplying out, with $j\beta=\overline\beta\,j$, $jb=\overline b\,j$ and $jbj=-\overline b$, gives the product rule
$$
(a+jb)(\alpha+j\beta)=\bigl(a\alpha-\overline b\,\beta\bigr)+j\bigl(b\alpha+\overline a\,\beta\bigr),
$$
and with $\overline q=\overline a-jb$ it gives $q\overline q=\abs a^2+\abs b^2$.

::: pf

::: {.pf-step #part-a}
(a) Left multiplication $L_q(x)=qx$ is right $\CC$-linear for every $q\in\quaternions$, and $q\mapsto L_q$ is a ring homomorphism $\varphi\colon\quaternions\to M_2(\CC)$, namely
$$
\varphi(a+jb)=\begin{pmatrix}a&-\overline b\\ b&\overline a\end{pmatrix}
$$
in the right $\CC$-basis $(1,j)$.

::: pf-proof
For $x\in\quaternions$ and $\lambda\in\CC$, associativity in $\quaternions$ gives $L_q(x\lambda)=(qx)\lambda=L_q(x)\lambda$, so $L_q$ is right $\CC$-linear; a right-linear endomorphism of a free right $\CC$-module is written as a matrix acting on the left of coordinate columns, so $L_q\in\operatorname{End}_\CC(\quaternions)\cong M_2(\CC)$ once the basis $(1,j)$ is fixed.
Since $L_{q_1q_2}=L_{q_1}L_{q_2}$ and $L_1=\operatorname{id}$, the assignment $q\mapsto L_q$ is a ring homomorphism.
By the product rule $L_q(1)=a\cdot1+j\cdot b$, and $L_q(j)=aj+jbj=aj-\overline b=j\overline a-\overline b$, so the two columns are $(a,b)$ and $(-\overline b,\overline a)$.
The left $\CC$-structure on $\quaternions$ is the one this argument must not use: left multiplication by $\lambda$ fails to commute with $L_q$ once $q\notin\CC$, so $L_q$ is not left $\CC$-linear.
:::

:::

::: {.pf-step #part-b}
(b) $\varphi$ is injective.

::: pf-proof
If $\varphi(q)=0$ then $L_q=0$, so $q=q\cdot1=L_q(1)=0$.
A ring homomorphism whose kernel is trivial is injective.
:::

:::

::: {.pf-step #norm}
For $q=a+jb$ one has $\det\varphi(q)=\abs q^2=\abs a^2+\abs b^2$ and $\varphi(q)^*\varphi(q)=\abs q^2I_2$.

::: pf-proof
The determinant is $a\overline a-(-\overline b)b=\abs a^2+\abs b^2$, which is $\abs q^2$ by the preamble.
The conjugate transpose is
$$
\varphi(q)^*=\begin{pmatrix}\overline a&\overline b\\ -b&a\end{pmatrix},
$$
and the four entries of $\varphi(q)^*\varphi(q)$ are $\abs a^2+\abs b^2$, $0$, $0$ and $\abs b^2+\abs a^2$.
:::

:::

::: {.pf-step #part-c}
(c) $\varphi$ restricts to an isomorphism from the group of unit quaternions to $\SU(2)$.

::: pf-proof
Every nonzero quaternion is a unit, since $\overline q/\abs q^2$ is its two-sided inverse, and $\abs{q_1q_2}^2=\det\varphi(q_1q_2)=\det\varphi(q_1)\det\varphi(q_2)=\abs{q_1}^2\abs{q_2}^2$, so the unit quaternions form a group.
If $\abs q=1$ then step [](#norm){.pf-ref} gives $\varphi(q)^*\varphi(q)=I_2$ and $\det\varphi(q)=1$, that is $\varphi(q)\in\SU(2)$.
Conversely let $U=\begin{pmatrix}a&c\\ b&d\end{pmatrix}\in\SU(2)$.
From $\det U=ad-bc=1$ the inverse is $U^{-1}=\begin{pmatrix}d&-c\\ -b&a\end{pmatrix}$, and $U^{-1}=U^*=\begin{pmatrix}\overline a&\overline b\\ \overline c&\overline d\end{pmatrix}$ gives $d=\overline a$ and $c=-\overline b$; then $U=\varphi(a+jb)$, and $\abs a^2+\abs b^2=\det U=1$ exhibits $U$ as the image of the unit quaternion $a+jb$.
The restriction of the injective ring homomorphism $\varphi$ to the unit group is therefore a bijective homomorphism onto $\SU(2)$.
:::

:::

::: {.pf-step #part-d}
(d) $\SU(2)$ acts transitively on $\CC\PP^1$.

::: pf-proof
The matrices of $\SU(2)$ act on $\CC^2$ by left multiplication and carry one-dimensional subspaces to one-dimensional subspaces, so they act on the set of lines.
Let $\ell\subseteq\CC^2$ be a line and choose a unit vector $v\in\ell$; every unit vector is $(a,b)$ with $\abs a^2+\abs b^2=1$, and by step [](#part-c){.pf-ref} the first column of $\varphi(a+jb)$ is $(a,b)$.
Hence $\varphi(a+jb)e_1=v$, and this element of $\SU(2)$ carries the line $\CC e_1$ to $\ell$.
:::

:::

::: {.pf-step #part-e}
(e) The stabilizer in $\SU(2)$ of the line $\CC e_1$ is the image of the unit circle of $\CC$ under $\varphi$, and $\SU(2)/U(1)$ is homeomorphic to $S^2$.

::: pf-proof
Let $U=\varphi(a+jb)\in\SU(2)$ carry $\CC e_1$ to itself.
Then $Ue_1=(a,b)$ is a nonzero multiple of $e_1=(1,0)$, so $b=0$; conversely every $U=\varphi(a)=\operatorname{diag}(a,\overline a)$ with $\abs a=1$ fixes both coordinate lines.
So the stabilizer is $\{\operatorname{diag}(z,\overline z): \abs z=1\}=\varphi(\{z\in\CC:\abs z=1\})$, the group $U(1)$ of the statement.
The orbit map $\SU(2)\to\CC\PP^1$, $U\mapsto U(\CC e_1)$, is continuous and surjective by step [](#part-d){.pf-ref}, so it induces a continuous bijection $\SU(2)/U(1)\to\CC\PP^1$.
The group $\SU(2)$ is a closed bounded subset of the matrix space $M_2(\CC)\cong\RR^8$, hence compact, and $\CC\PP^1$ is Hausdorff; a continuous bijection from a compact space to a Hausdorff space is a homeomorphism, so $\SU(2)/U(1)\cong\CC\PP^1$.
The Riemann sphere $\CC\PP^1$ is homeomorphic to $S^2$ by stereographic projection.
:::

:::

:::
:::
