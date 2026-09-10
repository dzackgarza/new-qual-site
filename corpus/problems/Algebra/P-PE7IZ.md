---
schema: qual/card@1
id: P-PE7IZ
kind: problem
title: $\ZZ$ is initial among unital rings, so every abelian group has a unique $\ZZ$-module
  structure
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Abelian Groups
  - Rings
relations: []
review: draft
---

::: problem
Prove that $\ZZ$ is initial in the category of unital rings and unital ring homomorphisms. Deduce that every abelian group has a unique $\ZZ$-module structure.
:::

::: {.solution}
<1>1. $\ZZ$ is initial among unital rings.
::: {.proof}
Let $R$ be a unital ring. Define
\[
\phi:\ZZ\to R,
\qquad
\phi(n)=n\cdot1_R,
\]
where for $n>0$ this is a sum of $n$ copies of $1_R$, for $n<0$ it is the negative of $(-n)\cdot1_R$, and $\phi(0)=0$.

Then
\[
\phi(m+n)=\phi(m)+\phi(n),\qquad
\phi(mn)=\phi(m)\phi(n),\qquad
\phi(1)=1_R,
\]
so $\phi$ is a unital ring homomorphism.

If $\psi:\ZZ\to R$ is any unital ring homomorphism, then $\psi(1)=1_R$, hence additivity forces
\[
\psi(n)=n\cdot1_R=\phi(n)
\]
for every $n\in\ZZ$. Thus $\phi$ is unique.
:::

<1>2. Every abelian group has a unique $\ZZ$-module structure.
::: {.proof}
For an abelian group $A$, the endomorphism ring $\End_{\mathbf{Ab}}(A)$ is unital. A $\ZZ$-module structure on $A$ is equivalent to a unital ring homomorphism
\[
\ZZ\to\End_{\mathbf{Ab}}(A).
\]
By <1>1 there is exactly one such homomorphism. Explicitly,
\[
n\cdot a=
\begin{cases}
a+\cdots+a,&n>0,\\
0,&n=0,\\
-((-n)\cdot a),&n<0.
\end{cases}
\]
:::
:::
