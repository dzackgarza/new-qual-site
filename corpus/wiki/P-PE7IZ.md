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
solved: false
---

::: problem
We prove a slightly stronger statement, namely:

**Theorem:**
$\ZZ$ is initial in the category of unital rings and ring homomorphisms.

This means that if we are given any such ring $R$, there is exactly one map $\ZZ \to R$.

Then, given an abelian group $A$, we can take $R = \hom_{\text{Ab}}(A, A)$, the hom set of abelian group endomorphisms, which is itself a unital ring.
This will imply that there is a unique map $\ZZ \to \hom_{\text{Ab}}(A, A)$, and since all such maps induce $\ZZ\dash$module structures on $A$, the result will follow.

*Proof:*
Let $R$ be arbitrary and $1_R$ be its multiplicative identity.
We first show that there exists a ring homomorphism $\ZZ \to R$, namely
\begin{align*}
\phi: \ZZ &\to R \\
n &\mapsto \sum_{i=1}^n 1_R
.\end{align*}

Note that $\phi(1) = 1_R$ and $\phi(-1) = -1_R$, and it is routine to check that $\phi$ is a ring homomorphism.

Now toward a contradiction, suppose there were another such ring homomorphism $\psi: \ZZ \to R$.
From the definition of a ring homomorphism, $\psi$ must satisfy,

\begin{align*}
\psi(1) &= 1_R \\
\psi(-1) &= -1_R
,\end{align*}

and by $\ZZ\dash$linearity, we must have 
$$
\psi(n) = \psi(\sum_{i=1}^n 1) = \sum_{i=1}^n \psi(1) = \sum_{i=1}^n 1_R = \phi(n),
$$

and so $\psi(x) = \phi(x)$ for every $x\in \ZZ$.
But this precisely means that $\psi = \phi$ as ring homomorphisms.
$\qed$
:::
