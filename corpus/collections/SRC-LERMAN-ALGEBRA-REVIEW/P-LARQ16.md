---
schema: qual/card@1
id: P-LARQ16
kind: problem
title: Homomorphisms of F[x]-modules as intertwining maps
classification:
  areas: [algebra]
  topics: [Module Theory, Linear Algebra]
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the F[x]-module description and homomorphism question with Lerman practice problem 16."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Proved both directions: F[x]-linearity implies F-linearity and intertwining, while an F-linear intertwiner commutes with every polynomial in the structure operator."
---

::: problem
An $F[x]$-module is an $F$-vector space $M$ with a linear map $T_M:M\to M$, where $x\cdot m=T_M(m)$.
Describe an $F[x]$-module homomorphism $\varphi:M\to N$ in terms of the linear maps $T_M$ and $T_N$.
:::

::: solution
The $F[x]$-module homomorphisms are exactly the $F$-linear maps satisfying
$$
\boxed{\varphi\circ T_M=T_N\circ\varphi.}
$$

<1>1. Every $F[x]$-module homomorphism is an $F$-linear intertwiner.
::: proof
Let $\varphi:M\to N$ be $F[x]$-linear. Since the constants $F$ embed in $F[x]$, for $a\in F$ and $m\in M$,
$$
\varphi(am)=a\varphi(m),
$$
and additivity is part of module-homomorphism structure. Thus $\varphi$ is $F$-linear.

Taking the scalar $x\in F[x]$ gives
$$
\varphi(T_Mm)
=\varphi(xm)
=x\varphi(m)
=T_N\varphi(m).
$$
Hence $\varphi T_M=T_N\varphi$.
:::

<1>2. Every $F$-linear intertwiner is $F[x]$-linear.
::: proof
Conversely, suppose $\varphi$ is $F$-linear and
$$
\varphi T_M=T_N\varphi.
$$
Induction gives
$$
\varphi T_M^j=T_N^j\varphi
$$
for every $j\ge0$. If
$$
p(x)=a_0+a_1x+\cdots+a_dx^d\in F[x],
$$
then the module action is $p(x)m=p(T_M)m$. Therefore
$$
\begin{aligned}
\varphi(p(x)m)
&=\varphi\left(\sum_{j=0}^d a_jT_M^jm\right)\\
&=\sum_{j=0}^d a_jT_N^j\varphi(m)\\
&=p(x)\varphi(m).
\end{aligned}
$$
Thus $\varphi$ respects multiplication by every element of $F[x]$, so it is an $F[x]$-module homomorphism.
:::
:::
