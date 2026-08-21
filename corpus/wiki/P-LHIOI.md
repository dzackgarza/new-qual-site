---
schema: qual/card@1
id: P-LHIOI
kind: problem
title: If $A=Ra$ with $ra=0$ and $(r,s)=(1)$, then $A=sA$ and $A[s]=0$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Cyclic Groups
  - Torsion
relations: []
review: draft
solved: false
---

::: problem
Since $(r, s) = (1)$, we can find $t_1, t_2 \in R$ such that
\[
\begin{align*}
t_1r + t_2 s = 1 &\implies t_1ra + t_2 sa = 1a  &\\
&\implies t_1(ra) + t_2 sa = a &\\
&\implies t_2 sa = a &\text{since $ra=0$}\\
&\implies s(t_2 a) = a &\text{since $R$ is commutative}
,\end{align*}
\]

which implies that $a \in sA$ and thus $A \subseteq sA$.
However, we always have $sA \subseteq A$ for modules, so this shows that $A = sA$.

To see that $A[s] = \theset{x\in A \mid sx = 0} = 0$, let $x\in A[s]$; we will show $x=0$.
Since $x\in A = Ra$, we have $x = r_1 a$, and in particular
$$
ra = 0 \implies rx = r r_1 a = r_1 (ra) = 0.
$$

So we now have $rx = 0$ and $sx=0$, and we can write
\[
\begin{align*}
x &= (t_1 r + t_2 s)x \\
&= t_1 (rx) + t_2 (sx) \\
&= t_1 0 + t_2 0 \\
&= 0
.\end{align*}
\]

So $x = 0$ and thus $A[s] = 0$.
$\qed$
:::
