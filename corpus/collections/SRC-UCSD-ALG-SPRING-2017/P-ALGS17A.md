---
schema: qual/card@1
id: P-ALGS17A
kind: problem
title: "Generalized dihedral groups and their properties"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Let $H$ be a finite abelian group, with product written multiplicatively.
Let $\mathbb{Z}_2 = \{e, a\}$, also written multiplicatively, so that $a^2 = e$.
The corresponding generalized dihedral group is the semidirect product $G = H \rtimes_\phi \mathbb{Z}_2$, where $\phi(a)$ is the automorphism of $H$ given by inverting elements, i.e.\ $[\phi(a)](h) = h^{-1}$.

(a) Suppose that $H = \mathbb{Z}_3 \times \mathbb{Z}_3$.
Find a presentation of $G = H \rtimes_\phi \mathbb{Z}_2$ with a brief justification.

(b) For which abelian groups $H$ is $G = H \rtimes_\phi \mathbb{Z}_2$ also abelian?

(c) Must $G = H \rtimes_\phi \mathbb{Z}_2$ be solvable?
:::

::: {.solution}
**(a).**

<1>1. Let \(x,y\) generate the two factors of \(H=C_3\times C_3\). Then
\[
G\cong\left\langle x,y,a\;\middle|\;x^3=y^3=a^2=1,\ [x,y]=1,\ axa=x^{-1},\ aya=y^{-1}\right\rangle.
\]
::: {.proof}
The relations \(x^3=y^3=1\) and \([x,y]=1\) present \(H\cong C_3\times C_3\). The relation \(a^2=1\) presents \(C_2\), and the conjugation relations specify exactly the semidirect-product action \(h\mapsto h^{-1}\) on both generators of \(H\). Hence the presented group is \(H\rtimes_\phi C_2\).
:::

**(b).**

<1>2. The generalized dihedral group \(G=H\rtimes_\phi C_2\) is abelian if and only if every element of \(H\) has order dividing \(2\).
::: {.proof}
Since \(H\) is already abelian, the only possible obstruction is commutation with \(a\). For \(h\in H\),
\[
aha^{-1}=h^{-1}.
\]
Thus \(a\) commutes with \(h\) iff \(h=h^{-1}\), equivalently \(h^2=e\). Therefore \(G\) is abelian exactly when \(h^2=e\) for all \(h\in H\), i.e. when \(H\) has exponent at most \(2\). For finite abelian \(H\), this means \(H\cong (C_2)^r\) for some \(r\ge0\).
:::

**(c).**

<1>3. The group \(G\) is always solvable.
::: {.proof}
The subgroup \(H\trianglelefteq G\) is abelian, and the quotient \(G/H\cong C_2\) is abelian.
Hence the commutator subgroup \(G'\) lies in \(H\), so \(G''=1\). Thus \(G\) is solvable of derived length at most \(2\).
:::
:::
