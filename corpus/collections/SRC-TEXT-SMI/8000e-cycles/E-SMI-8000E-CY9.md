---
schema: qual/card@1
id: E-SMI-8000E-CY9
kind: problem
title: The commutator subgroup is characteristic
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared all three requested assertions with Smith 8000e cycles problem 9."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Tracked commutators under automorphisms, proved the quotient abelian, and showed every homomorphism to an abelian group kills G'."
---

::: {.exercise}
Prove that the commutator subgroup $G'$ of $G$ is a characteristic subgroup — hence normal — that $G/G'$ is abelian, and that if a homomorphism $f: G \to K$ exists where $K$ is abelian, then $\ker(f)$ contains $G'$.

[A subgroup $H$ of $G$ is a *characteristic* subgroup iff $f(H) = H$ for all automorphisms $f$ of $G$.]
:::

::: solution
Recall that
$$
G'=\langle [x,y]:x,y\in G\rangle,
\qquad
[x,y]=xyx^{-1}y^{-1}.
$$

<1>1. The commutator subgroup is characteristic.
::: proof
Let
$$
\varphi:G\longrightarrow G
$$
be an automorphism. For every $x,y\in G$,
$$
\begin{aligned}
\varphi([x,y])
&=\varphi(xy x^{-1}y^{-1})\\
&=\varphi(x)\varphi(y)\varphi(x)^{-1}\varphi(y)^{-1}\\
&=[\varphi(x),\varphi(y)].
\end{aligned}
$$
Thus $\varphi$ sends every commutator to a commutator, hence
$$
\varphi(G')\subseteq G'.
$$
Applying the same argument to $\varphi^{-1}$ gives the reverse inclusion, so
$$
\boxed{\varphi(G')=G'.}
$$
Therefore $G'$ is characteristic.

Every inner automorphism is an automorphism, so every characteristic subgroup
is normal. Hence
$$
G'\trianglelefteq G.
$$
:::

<1>2. The quotient $G/G'$ is abelian.
::: proof
For arbitrary $x,y\in G$, the commutator
$$
[x,y]=xyx^{-1}y^{-1}
$$
lies in $G'$. Therefore
$$
xyG'=yxG'.
$$
Equivalently,
$$
(xG')(yG')=(yG')(xG').
$$
Since this holds for every pair of cosets,
$$
\boxed{G/G'\text{ is abelian}.}
$$
:::

<1>3. Every homomorphism from $G$ to an abelian group kills $G'$.
::: proof
Let
$$
f:G\longrightarrow K
$$
be a homomorphism with $K$ abelian. Then for every $x,y\in G$,
$$
\begin{aligned}
f([x,y])
&=f(x)f(y)f(x)^{-1}f(y)^{-1}\\
&=1_K,
\end{aligned}
$$
because the elements of $K$ commute. Thus every commutator lies in
$\ker f$. Since $\ker f$ is a subgroup, it contains the subgroup generated
by all commutators. Hence
$$
\boxed{G'\le\ker f.}
$$
:::
:::
