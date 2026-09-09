---
schema: qual/card@1
id: P-PCLDH
kind: problem
title: Separable extensions
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Field Extensions
  - Finite Fields
relations: []
review: draft
---

::: problem
Define a separable algebraic extension. Explain why algebraic extensions of characteristic-$0$ fields and of finite fields are separable, and give an inseparable example.
:::

::: {.solution}
An algebraic extension $L/K$ is **separable** if the minimal polynomial over $K$ of every $\alpha\in L$ has distinct roots in an algebraic closure; equivalently, every irreducible polynomial over $K$ having a root in $L$ is separable.

<1>1. Characteristic $0$ fields are perfect.
::: {.proof}
If $f\in K[x]$ is irreducible and $\operatorname{char}K=0$, then $f'\ne0$. Since $f$ is irreducible, $\gcd(f,f')=1$, so $f$ has no repeated roots. Thus every algebraic extension is separable.
:::

<1>2. Finite fields are perfect.
::: {.proof}
Let $K=\FF_q$. The Frobenius map
\[
x\mapsto x^p
\]
is injective, hence surjective because $K$ is finite. Therefore every element is a $p$th power. An irreducible polynomial with zero derivative would have the form $g(x^p)$, and surjectivity of Frobenius would make it a $p$th power of a polynomial over $K$, contradicting irreducibility unless it were linear. Hence every irreducible polynomial is separable.
:::

Thus $\QQ$ and every finite field have no inseparable algebraic extensions.

<1>3. Inseparable example.
::: {.proof}
Let
\[
K=\FF_p(t^p)\subset L=\FF_p(t).
\]
Then $t$ satisfies
\[
x^p-t^p\in K[x],
\]
which equals $(x-t)^p$ over $L$. Its derivative is zero, and $t\notin K$, so the minimal polynomial of $t$ over $K$ is inseparable. Hence $L/K$ is not separable.
:::
:::
