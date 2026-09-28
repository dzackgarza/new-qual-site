---
schema: qual/card@1
id: P-MMAQ-ONXNRKJ737
kind: problem
title: The sum of group elements is central and nilpotent in $\mathbb{F}[G]$ when
  $\mathrm{char}\,\mathbb{F}=p$ and $|G|=p^n$, so $\mathbb{F}[G]$ is not semisimple
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $\mathbb F$ be a field of characteristic $p$, and $G$ a group of order $p^n$.
Let $R=\mathbb F[G]$ be the group ring (group algebra) of $G$ over $\mathbb F$, and let $u:=\sum_{x\in G}x$ (so $u$ is an element of $R$).

- Prove that $u$ lies in the center of $R$.

- Verify that $Ru$ is a 2-sided ideal of $R$.

- Show there exists a positive integer $k$ such that $u^k=0$.
  Conclude that for such a $k$, $(Ru)^k=0$.

- Show that $R$ is **not** a semi-simple ring.

  > **Warning:** Please use the definition of a semi-simple ring: do **not** use the result that a finite length ring fails to be semisimple if and only if it has a non-zero nilpotent ideal.
:::


::: {.solution}
<1>1. The element
\[
u=\sum_{x\in G}x
\]
lies in the center of $R=\mathbb F[G]$.
::: {.proof}
For any $g\in G$,
\[
gu=\sum_{x\in G}gx=\sum_{y\in G}y=u
\]
because left multiplication by $g$ permutes the elements of $G$. Similarly,
\[
ug=\sum_{x\in G}xg=u.
\]
Thus $gu=ug$ for every basis element $g\in G$, and therefore $u$ commutes with every element of $R$.
:::

<1>2. One has
\[
Ru=\mathbb F u,
\]
and $Ru$ is a nonzero two-sided ideal of $R$.
::: {.proof}
If
\[
r=\sum_{g\in G}a_g g,
\]
then by <1>1,
\[
ru=\sum_{g\in G}a_g(gu)=\left(\sum_{g\in G}a_g\right)u.
\]
Hence $Ru\subseteq\mathbb F u$, while the reverse inclusion is immediate since $\mathbb F\subseteq R$. Thus $Ru=\mathbb F u$. Because the group elements form an $\mathbb F$-basis of $R$, the element $u$ is nonzero. Finally, centrality of $u$ gives
\[
(Ru)R=R(uR)=R(Ru)\subseteq Ru,
\]
so $Ru$ is two-sided.
:::

<1>3. The element $u$ is square-zero:
\[
u^2=0.
\]
Consequently
\[
(Ru)^2=0.
\]
::: {.proof}
Using $xu=u$ for every $x\in G$,
\[
u^2=\left(\sum_{x\in G}x\right)u
=\sum_{x\in G}u
=|G|u=p^n u=0
\]
because $\operatorname{char}\mathbb F=p$. Thus one may take $k=2$. Since $Ru=\mathbb F u$ by <1>2, every product of two elements of $Ru$ is a scalar multiple of $u^2$, hence is zero.
:::

<1>4. The ring $R$ is not semisimple.
::: {.proof}
Assume for contradiction that $R$ is semisimple as a left $R$-module. Then every submodule of the semisimple module $R$ is a direct summand, so there is a left ideal $J$ such that
\[
R=Ru\oplus J.
\]
Let
\[
\pi:R\longrightarrow Ru
\]
be the projection along $J$. This map is left $R$-linear. Put
\[
e=\pi(1)\in Ru.
\]
For every $r\in R$,
\[
\pi(r)=\pi(r\cdot1)=r\pi(1)=re.
\]
Since $\pi$ restricts to the identity on $Ru$, in particular $\pi(e)=e$. Hence
\[
e^2=\pi(e)=e.
\]
But $e\in Ru$ and $(Ru)^2=0$ by <1>3, so $e^2=0$. Thus $e=0$, which would imply
\[
\pi(r)=re=0
\]
for every $r\in R$, contradicting that $\pi$ is the identity on the nonzero submodule $Ru$. Therefore $R$ is not semisimple.
:::
:::
