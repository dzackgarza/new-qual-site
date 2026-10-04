---
schema: qual/card@1
id: P-AGXHWSUPPORT
kind: problem
title: The support of a section is closed, while the support of a sheaf need not be
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Support
  - Skyscraper Sheaves
relations: []
review: draft
---

::: {.problem}
Let $\mcf\in \Sh(X)$ and $s\in \mcf(U)$ be a section, and define
$$
\supp s \coloneqq \{p\in U : s_p\neq0\}\subseteq U,
\qquad
\supp \mcf \coloneqq \{p\in X : \mcf_p\neq0\}\subseteq X,
$$
where $s_p$ denotes the germ of $s$ in the stalk $\mcf_p$.
Show that $\supp s$ is closed in $U$ but $\supp \mcf$ need not be closed in $X$.
:::

::: {.solution}
<1>1. The complement $U\setminus\supp s$ is open in $U$.

::: {.proof}
Let $p\in U\setminus\supp s$. Then $s_p=0$ in the stalk $\mcf_p$. By the definition of equality of germs, there is an open neighborhood $V_p\subseteq U$ of $p$ such that
$$
s|_{V_p}=0.
$$
For every $q\in V_p$, the germ $s_q$ is therefore zero, so $V_p\subseteq U\setminus\supp s$. Thus every point of $U\setminus\supp s$ has an open neighborhood contained in that complement.
:::

<1>2. The support $\supp s$ is closed in $U$.

::: {.proof}
This is the complement statement from step <1>1.
:::

<1>3. There exists a sheaf whose support is not closed.

<2>1. Let $X=\RR$, let $q=0$, and define a presheaf $\mathcal P$ of abelian groups by
$$
\mathcal P(V)=
\begin{cases}
\ZZ,&0\notin V,\\
0,&0\in V,
\end{cases}
$$
with identity restriction maps between open sets avoiding $0$ and the unique zero restriction map whenever the source group is $0$. Let $\mathcal F=\mathcal P^{\mathrm{sh}}$ be its sheafification.

::: {.proof}
The displayed rule defines a presheaf: identity restrictions are identities, and every composition involving a restriction from the zero group is again the unique zero homomorphism. Sheafification therefore produces a sheaf $\mathcal F$ on $X$ with the same stalks as $\mathcal P$.
:::

<2>2. The stalk $\mathcal F_0$ is zero.

::: {.proof}
Every open neighborhood $V$ of $0$ contains $0$, so $\mathcal P(V)=0$. Hence
$$
\mathcal P_0=\varinjlim_{0\in V}\mathcal P(V)=0.
$$
Sheafification preserves stalks, so $\mathcal F_0=0$.
:::

<2>3. For every $p\neq0$, the stalk $\mathcal F_p$ is isomorphic to $\ZZ$.

::: {.proof}
Choose an open neighborhood $W$ of $p$ with $0\notin W$. The neighborhoods $V$ of $p$ contained in $W$ are cofinal among all neighborhoods of $p$, and for all such $V$ one has $\mathcal P(V)=\ZZ$ with identity transition maps. Therefore
$$
\mathcal P_p\cong\ZZ.
$$
Again using invariance of stalks under sheafification gives $\mathcal F_p\cong\ZZ$.
:::

<2>4. The support of $\mathcal F$ is
$$
\boxed{\supp\mathcal F=\RR\setminus\{0\}},
$$
which is not closed in $\RR$.

::: {.proof}
Steps <2>2 and <2>3 show that the stalk is zero exactly at $0$. Thus the support is $\RR\setminus\{0\}$. This set is not closed because its closure is all of $\RR$.
:::

<2>5. Q.E.D.

::: {.proof}
Step <2>4 gives the required counterexample for the support of a sheaf.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>2 proves that the support of every section is closed in its domain, and step <1>3 shows that the support of a sheaf need not be closed.
:::
:::
