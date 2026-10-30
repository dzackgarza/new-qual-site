---
schema: qual/card@1
id: E-PER08-3.4
kind: problem
title: $\operatorname{PSL}_2(\ZZ)$ as the free product $(\ZZ/2)*(\ZZ/3)$
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Exercise 3.4 of the vendored Perutz Fall 2008 Algebraic Topology I notes.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the Euclidean descent proving generation and the upper-half-plane ping-pong inequalities proving injectivity.
---

::: {.problem}
Let
$$
S=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
T=\begin{pmatrix}1&-1\\0&1\end{pmatrix},\qquad
U=ST=\begin{pmatrix}0&1\\-1&1\end{pmatrix}
$$
in $\operatorname{SL}_2(\ZZ)$.

1. Verify that $S^2=U^3=-I$.

2. Show that, for every $A\in\operatorname{SL}_2(\ZZ)$, there is $n\in\ZZ$ such that if
   $$
   AT^n=\begin{pmatrix}a&b\\c&d\end{pmatrix},
   $$
   then either $c=0$ or $\abs{d}\le \abs{c}/2$.

3. Explain how to find $\ell\ge0$ and integers $n_1,\dots,n_\ell$ such that either
   $$
   AT^{n_1}ST^{n_2}S\cdots ST^{n_\ell}
   $$
   or the same product followed by $S$ has lower-left entry zero.

4. Show that $S$ and $T$ generate $\operatorname{SL}_2(\ZZ)$.

5. Define
   $$
   \theta:(\ZZ/2)*(\ZZ/3)=\langle a,b\mid a^2,b^3\rangle\to\operatorname{PSL}_2(\ZZ)
   $$
   by $\theta(a)=\pm S$ and $\theta(b)=\pm U$.
   Using the Möbius action on the upper half-plane $\halfplane$, prove that for every nontrivial word $w$ the map $\mu_w$ corresponding to $\theta(w)$ satisfies $\mu_w(D)\cap D=\varnothing$, where
   $$
   D=\{z\in\halfplane:0<\operatorname{Re}z<1/2,\ \abs{z-1}>1\}.
   $$
   Deduce that $\theta$ is an isomorphism.

For the last part, the source suggests considering
$$
A=\{z\in\halfplane:\operatorname{Re}z>0\},\qquad
B=\{z\in\halfplane:\abs{z-1}>\max(1,\abs{z})\}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The displayed matrices satisfy $S^2=U^3=-I$.

::: pf-proof

Direct multiplication gives
$$
S^2=
\begin{pmatrix}0&1\\-1&0\end{pmatrix}^2
=
\begin{pmatrix}-1&0\\0&-1\end{pmatrix}
=-I.
$$
Also
$$
U^2=
\begin{pmatrix}0&1\\-1&1\end{pmatrix}^2
=
\begin{pmatrix}-1&1\\-1&0\end{pmatrix},
$$
so
$$
U^3=U^2U
=
\begin{pmatrix}-1&0\\0&-1\end{pmatrix}
=-I.
$$
Thus the classes $\pm S$ and $\pm U$ in $\operatorname{PSL}_2(\ZZ)$ have orders $2$ and $3$, respectively.

:::

:::

::: {.pf-step #s2}

Right multiplication by a power of $T$ performs Euclidean reduction on the lower row.

::: pf-proof

Write
$$
A=\begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix}.
$$
Since
$$
T^n=\begin{pmatrix}1&-n\\0&1\end{pmatrix},
$$
we have
$$
AT^n=
\begin{pmatrix}
\alpha&\beta-n\alpha\\
\gamma&\delta-n\gamma
\end{pmatrix}.
$$
Thus the lower-left entry remains $c=\gamma$, while the lower-right entry becomes
$$
d=\delta-n\gamma.
$$
If $\gamma=0$, there is nothing to prove. If $\gamma\neq0$, choose $n\in\ZZ$ nearest to $\delta/\gamma$. Then
$$
\abs{\frac{\delta}{\gamma}-n}\le\frac12,
$$
so
$$
\abs{d}=\abs{\delta-n\gamma}
\le\frac{\abs{\gamma}}{2}
=\frac{\abs{c}}{2}.
$$

:::

:::

::: {.pf-step #s3}

Repeatedly applying step [](#s2){.pf-ref} and then $S$ forces the lower-left entry to zero.

::: pf-proof

Suppose after some stage the current matrix has lower row $(c,d)$ with $c\neq0$. By step [](#s2){.pf-ref}, choose $n$ so that after right multiplication by $T^n$ the lower row is
$$
(c,d')
\qquad\text{with}\qquad
\abs{d'}\le\frac{\abs{c}}{2}.
$$
Now right multiply by $S$. Since
$$
(c,d')S=(-d',c),
$$
the new lower-left entry is $-d'$. If it is nonzero, then
$$
0<\abs{d'}\le\frac{\abs{c}}{2}<\abs{c}.
$$
Thus each nonterminal $T^nS$ step strictly decreases the positive integer given by the absolute value of the lower-left entry.

A strictly decreasing sequence of positive integers must terminate. Hence after finitely many choices $n_1,\dots,n_\ell$, either the product
$$
AT^{n_1}ST^{n_2}S\cdots ST^{n_\ell}
$$
already has lower-left entry zero, or the final reduction has zero lower-right entry and one additional multiplication by $S$ moves that zero into the lower-left position. This is exactly the form asserted in the problem.

:::

:::

::: {.pf-step #s4}

The matrices $S$ and $T$ generate $\operatorname{SL}_2(\ZZ)$.

::: pf-proof

Let $A\in\operatorname{SL}_2(\ZZ)$. By step [](#s3){.pf-ref}, there is a word $W$ in $S$ and powers of $T$ such that
$$
AW=
\begin{pmatrix}a&b\\0&d\end{pmatrix}
\in\operatorname{SL}_2(\ZZ).
$$
The determinant condition gives
$$
ad=1.
$$
Since $a,d\in\ZZ$, either $a=d=1$ or $a=d=-1$.

If $a=d=1$, then
$$
AW=
\begin{pmatrix}1&b\\0&1\end{pmatrix}
=T^{-b}.
$$
If $a=d=-1$, then
$$
AW=
\begin{pmatrix}-1&b\\0&-1\end{pmatrix}
=-T^b
=S^2T^b.
$$
In either case $AW\in\langle S,T\rangle$. Since $W\in\langle S,T\rangle$ as well,
$$
A=(AW)W^{-1}\in\langle S,T\rangle.
$$
Thus
$$
\operatorname{SL}_2(\ZZ)=\langle S,T\rangle.
$$

:::

:::

::: {.pf-step #s5}

The homomorphism
$$
\theta:(\ZZ/2)*(\ZZ/3)\to\operatorname{PSL}_2(\ZZ)
$$
is surjective.

::: pf-proof

By step [](#s1){.pf-ref}, the assignments
$$
a\longmapsto\pm S,
\qquad
b\longmapsto\pm U
$$
respect $a^2=1$ and $b^3=1$, so $\theta$ is well defined.

Since $U=ST$, in $\operatorname{PSL}_2(\ZZ)$ we have
$$
\pm T=(\pm S)^{-1}(\pm U).
$$
By step [](#s4){.pf-ref}, the classes of $S$ and $T$ generate $\operatorname{PSL}_2(\ZZ)$; hence the classes of $S$ and $U$ generate it. Therefore $\theta$ is surjective.

For injectivity, let the Möbius transformations associated with $\pm S$ and $\pm U$ be
$$
s(z)=-\frac1z,
\qquad
u(z)=\frac1{1-z}.
$$
Then
$$
u^2(z)=\frac{z-1}{z},
\qquad
u^3(z)=z.
$$
Let
$$
\mathcal A=\{z\in\halfplane:\operatorname{Re}z>0\},
$$
$$
\mathcal B=\{z\in\halfplane:\abs{z-1}>\max(1,\abs{z})\}.
$$
Since
$$
\abs{z-1}>\abs{z}
\iff
\operatorname{Re}z<\frac12,
$$
we have
$$
D=\mathcal A\cap\mathcal B.
$$

:::

:::

::: pf-step

The generators satisfy the required ping-pong inclusions.

::: pf-proof

First suppose $z\notin\mathcal B$. If $\operatorname{Re}z<0$, then
$$
\abs{z-1}^2-\abs{z}^2=1-2\operatorname{Re}z>1
$$
and also $\abs{z-1}>1$, which would put $z$ in $\mathcal B$, a contradiction. Hence
$$
\operatorname{Re}z\ge0.
$$
Therefore
$$
\operatorname{Re}s(z)
=\operatorname{Re}\left(-\frac1z\right)
=-\frac{\operatorname{Re}z}{\abs{z}^2}
\le0,
$$
so
$$
s(\halfplane\setminus\mathcal B)
\subseteq
\halfplane\setminus\mathcal A.
\tag{1}
$$

Now suppose $z\notin\mathcal A$, so $\operatorname{Re}z\le0$. For $u(z)=1/(1-z)$,
$$
\abs{u(z)-1}=\frac{\abs{z}}{\abs{1-z}}.
$$
But
$$
\abs{1-z}^2-\abs{z}^2=1-2\operatorname{Re}z\ge1,
$$
so $\abs{u(z)-1}<1$. Hence $u(z)\notin\mathcal B$.

For $u^2(z)=(z-1)/z$,
$$
\abs{u^2(z)-1}=\frac1{\abs{z}},
\qquad
\abs{u^2(z)}=\frac{\abs{z-1}}{\abs{z}}.
$$
Since $\operatorname{Im}z>0$ and $\operatorname{Re}z\le0$, we have $\abs{z-1}>1$, so
$$
\abs{u^2(z)-1}<\abs{u^2(z)}.
$$
Thus $u^2(z)\notin\mathcal B$. Consequently
$$
u(\halfplane\setminus\mathcal A),\
u^2(\halfplane\setminus\mathcal A)
\subseteq
\halfplane\setminus\mathcal B.
\tag{2}
$$

We also need the initial step from $D$. If $z\in D$, then $\operatorname{Re}z>0$, so
$$
s(z)\notin\mathcal A.
\tag{3}
$$
For $u(z)$, the inequality $\operatorname{Re}z<1/2$ gives
$$
\abs{z}<\abs{1-z},
$$
so
$$
\abs{u(z)-1}=\frac{\abs{z}}{\abs{1-z}}<1;
$$
hence $u(z)\notin\mathcal B$. Finally, because $\abs{z-1}>1$,
$$
\abs{u^2(z)-1}=\frac1{\abs{z}}
<
\frac{\abs{z-1}}{\abs{z}}
=\abs{u^2(z)},
$$
so $u^2(z)\notin\mathcal B$. Therefore
$$
u(D),\
u^2(D)\subseteq\halfplane\setminus\mathcal B.
\tag{4}
$$

:::

:::

::: {.pf-step #s7}

Every nontrivial reduced word sends $D$ disjointly from itself.

::: pf-proof

Every nontrivial element of
$$
(\ZZ/2)*(\ZZ/3)
$$
has a reduced form whose factors alternate between the nonidentity element $a$ of $\ZZ/2$ and a nonidentity power $b$ or $b^2$ of $\ZZ/3$.

Read such a reduced word from right to left, which is the order in which its Möbius transformations act.

If the rightmost factor is $a$, then by (3) it sends $D$ into $\halfplane\setminus\mathcal A$. The next factor, necessarily $b$ or $b^2$, sends that set into $\halfplane\setminus\mathcal B$ by (2). The next $a$ sends it back into $\halfplane\setminus\mathcal A$ by (1), and so on.

If the rightmost factor is $b$ or $b^2$, then by (4) it sends $D$ into $\halfplane\setminus\mathcal B$. The next $a$ sends that set into $\halfplane\setminus\mathcal A$ by (1), and the same alternation continues.

Thus the final image $\mu_w(D)$ lies entirely in either
$$
\halfplane\setminus\mathcal A
\quad\text{or}\quad
\halfplane\setminus\mathcal B.
$$
Since
$$
D\subseteq\mathcal A\cap\mathcal B,
$$
it follows that
$$
\boxed{\mu_w(D)\cap D=\varnothing}.
$$

:::

:::

::: pf-step

The homomorphism $\theta$ is injective, hence an isomorphism.

::: pf-proof

If $1\neq w\in(\ZZ/2)*(\ZZ/3)$, then by step [](#s7){.pf-ref}
$$
\mu_w(D)\cap D=\varnothing.
$$
In particular, $\mu_w$ is not the identity Möbius transformation, since the identity sends $D$ to itself. Therefore
$$
\theta(w)\neq1
$$
in $\operatorname{PSL}_2(\ZZ)$. Hence
$$
\ker\theta=\{1\}.
$$
Together with surjectivity from step [](#s5){.pf-ref},
$$
\boxed{\operatorname{PSL}_2(\ZZ)\cong(\ZZ/2)*(\ZZ/3)}.
$$

:::

:::

:::

:::
