---
schema: qual/card@1
id: P-DYEG6
kind: problem
title: Separable extensions, separability over finite fields, and an inseparable finite
  extension
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

::: {.problem}
Let $L/K$ be a finite extension of fields.

a.
Define what it means for $L/K$ to be *separable*.

b.
Show that if $K$ is a finite field, then $L/K$ is always separable.

c.
Give an example of a finite extension $L/K$ that is not separable.
:::

::: {.solution}
<1>1. The extension $L/K$ is separable if every $\alpha\in L$ has a minimal polynomial over $K$ with no repeated roots in an algebraic closure.

::: {.proof}
This is the definition of a separable algebraic field extension.
:::

<1>2. Every finite extension of a finite field is separable.

::: {.proof}
Let $K=\mathbb F_q$ with $q=p^e$. The Frobenius map $a\mapsto a^p$ is injective on the finite field $K$ and hence surjective. Thus every coefficient in $K$ has a $p$-th root in $K$.

Suppose an element of a finite extension had an inseparable irreducible minimal polynomial $f\in K[x]$. Since $f$ is irreducible and $\gcd(f,f')\neq1$, one has $f'=0$. Therefore all exponents appearing in $f$ are divisible by $p$, and $f(x)=\sum_j a_jx^{pj}$. Choosing $b_j\in K$ with $b_j^p=a_j$ gives
\[
f(x)=\left(\sum_j b_jx^j\right)^p,
\]
contradicting irreducibility of the nonconstant polynomial $f$. Hence every element of the extension is separable.
:::

<1>3. For any prime $p$, the finite extension
\[
\boxed{\mathbb F_p(t^{1/p})/\mathbb F_p(t)}
\]
is not separable.

::: {.proof}
Let $K=\mathbb F_p(t)$, with $t$ transcendental, and choose $\alpha$ satisfying $\alpha^p=t$. The polynomial $x^p-t\in K[x]$ is irreducible: viewed in $\mathbb F_p[t][x]$, it is Eisenstein at the prime element $t$, and Gauss's lemma gives irreducibility over $K$. Consequently $[K(\alpha):K]=p$. But
\[
x^p-t=(x-\alpha)^p
\]
over $K(\alpha)$, so its only root has multiplicity $p$. Thus $\alpha$ is inseparable over $K$, and the extension is not separable.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1, <1>2, and <1>3 respectively establish parts (a), (b), and (c).
:::
:::

