---
schema: qual/card@1
id: P-APAS05E
kind: problem
title: No simple group of order $120$
classification:
  areas:
  - applied-algebra
  topics:
  - Group Theory
  - Classification
relations: []
review: draft
---

::: {.problem}
Prove that a group of order $120$ is not simple.
:::

::: {.solution}

Suppose, for contradiction, that $G$ is simple and
\[
|G|=120=2^3\cdot3\cdot5.
\]

::: pf

::: pf-step
The number $n_5$ of Sylow $5$-subgroups is $6$.

::: pf-proof
By Sylow's theorems,
\[
n_5\equiv1\pmod5,
\qquad
n_5\mid24.
\]
The only possibilities are $n_5=1$ or $n_5=6$.
If $n_5=1$, the unique Sylow $5$-subgroup is normal in $G$, contradicting simplicity. Hence
\[
n_5=6.
\]
:::

:::

::: pf-step
Conjugation on the six Sylow $5$-subgroups gives an injective homomorphism
\[
\rho:G\hookrightarrow S_6.
\]

::: pf-proof
Let $\Omega$ be the set of six Sylow $5$-subgroups. Conjugation defines an action of $G$ on $\Omega$, hence a homomorphism
\[
\rho:G\to\operatorname{Sym}(\Omega)\cong S_6.
\]
The action is transitive by Sylow's conjugacy theorem, so it is nontrivial. Thus $\ker\rho$ is a proper normal subgroup of $G$. Since $G$ is simple,
\[
\ker\rho=1.
\]
Therefore $\rho$ is injective.
:::

:::

::: pf-step
The image $\rho(G)$ is contained in $A_6$.

::: pf-proof
Compose $\rho$ with the sign homomorphism:
\[
G\xrightarrow{\rho}S_6\xrightarrow{\operatorname{sgn}}\{\pm1\}.
\]
Its kernel is normal in $G$. If this homomorphism were nontrivial, its kernel would have index $2$, hence would be a nontrivial proper normal subgroup because $|G|=120>2$. This contradicts simplicity.
Therefore the sign is trivial on $\rho(G)$, so
\[
\rho(G)\subseteq A_6.
\]
:::

:::

::: pf-step
The subgroup $\rho(G)$ has index $3$ in $A_6$.

::: pf-proof
Since $\rho$ is injective,
\[
|\rho(G)|=120.
\]
Also
\[
|A_6|=\frac{6!}{2}=360.
\]
Hence
\[
[A_6:\rho(G)]=\frac{360}{120}=3.
\]
:::

:::

::: pf-step
This is impossible, so $G$ is not simple.

::: pf-proof
We use the standard theorem that $A_n$ is simple for every $n\ge5$, in particular $A_6$ is simple.

If $H:=\rho(G)$ had index $3$ in $A_6$, left multiplication on the three cosets $A_6/H$ would define a homomorphism
\[
\psi:A_6\to S_3.
\]
This action is transitive, hence nontrivial, so $\ker\psi$ is a proper normal subgroup of $A_6$. Simplicity of $A_6$ forces
\[
\ker\psi=1.
\]
Thus $\psi$ would be injective. But this is impossible because
\[
|A_6|=360>6=|S_3|.
\]
The contradiction shows that the original assumption that $G$ is simple was false. Therefore every group of order $120$ is nonsimple.
:::

:::

:::

:::
