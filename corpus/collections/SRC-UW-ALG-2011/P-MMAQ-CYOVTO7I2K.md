---
schema: qual/card@1
id: P-MMAQ-CYOVTO7I2K
kind: problem
title: Whether $\mathbb{Z}[x]/(x^2+x+1)$ is Noetherian, Artinian, or an integrally
  closed domain
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let `\begin{align*} R=\mathbb Z[x]/(x^2+x+1). \end{align*}`{=tex}

- Answer the following questions with suitable justification.

  - Is $R$ a Noetherian ring?

  - Is $R$ an Artinian ring?

- Prove that $R$ is an integrally closed domain.
:::


::: solution
<1>1. The ring
\[
R=\mathbb Z[x]/(x^2+x+1)
\]
is a Noetherian integral domain.
::: {.proof}
The ring $\mathbb Z$ is Noetherian, so by the Hilbert basis theorem $\mathbb Z[x]$ is Noetherian. Every quotient of a Noetherian ring is Noetherian, hence $R$ is Noetherian.

Also $x^2+x+1$ is irreducible over $\mathbb Q$, since its discriminant is $-3$, not a square in $\mathbb Q$. Being primitive, it is irreducible in $\mathbb Z[x]$ by Gauss's lemma. Since $\mathbb Z[x]$ is a UFD, irreducible elements are prime, so $(x^2+x+1)$ is prime and the quotient $R$ is a domain.
:::

<1>2. The ring $R$ is not Artinian.
::: {.proof}
The image of $2$ in $R$ is not a unit: indeed,
\[
R/(2)\cong \mathbb F_2[x]/(x^2+x+1)
\]
is a nonzero ring. Consider the descending chain of ideals
\[
(2)\supseteq(2^2)\supseteq(2^3)\supseteq\cdots.
\]
Each inclusion is strict. If $(2^n)=(2^{n+1})$, then
\[
2^n=2^{n+1}r
\]
for some $r\in R$. Since $R$ is a domain by <1>1, cancellation gives $1=2r$, contradicting that $2$ is not a unit. Thus the descending chain condition fails, so $R$ is not Artinian.
:::

<1>3. Let
\[
\omega=\frac{-1+\sqrt{-3}}2.
\]
Then
\[
R\cong\mathbb Z[\omega],
\qquad
\operatorname{Frac}(R)=\mathbb Q(\sqrt{-3}).
\]
::: {.proof}
The element $\omega$ satisfies
\[
\omega^2+\omega+1=0.
\]
Since this polynomial is irreducible over $\mathbb Q$, evaluation at $\omega$ induces an injective homomorphism
\[
\mathbb Z[x]/(x^2+x+1)\longrightarrow\mathbb C
\]
with image $\mathbb Z[\omega]$. Its fraction field is
\[
\mathbb Q(\omega)=\mathbb Q(\sqrt{-3}).
\]
:::

<1>4. Every element of $\mathbb Q(\sqrt{-3})$ that is integral over $\mathbb Z$ lies in $\mathbb Z[\omega]$.
::: {.proof}
Let $\alpha\in\mathbb Q(\sqrt{-3})$ be integral over $\mathbb Z$. Its conjugate $\bar\alpha$ is also integral, so its trace and norm
\[
T=\alpha+\bar\alpha,
\qquad
N=\alpha\bar\alpha
\]
are rational algebraic integers and therefore integers.

Write
\[
\alpha=\frac{T+q\sqrt{-3}}2
\]
for some $q\in\mathbb Q$. Since
\[
T^2-4N=(\alpha-\bar\alpha)^2=-3q^2,
\]
we have $3q^2\in\mathbb Z$. Write $q=a/b$ in lowest terms. Then $b^2\mid3a^2$; coprimality gives $b^2\mid3$, hence $b=1$. Thus $q\in\mathbb Z$.

Moreover,
\[
4N=T^2+3q^2.
\]
Modulo $4$, this forces $T$ and $q$ to have the same parity: if exactly one were odd, the right side would be congruent to $1$ or $3$ modulo $4$. Hence
\[
\alpha
=\frac{T+q\sqrt{-3}}2
=\frac{T+q}{2}+q\omega\in\mathbb Z[\omega].
\]
:::

<1>5. The domain $R$ is integrally closed.
::: {.proof}
Let $\alpha\in\operatorname{Frac}(R)$ be integral over $R$. By <1>3,
\[
\operatorname{Frac}(R)=\mathbb Q(\sqrt{-3}).
\]
The ring $R=\mathbb Z[\omega]$ is integral over $\mathbb Z$ because $\omega$ satisfies the monic polynomial $x^2+x+1$. Since $\alpha$ is integral over $R$, transitivity of integrality implies that $\alpha$ is integral over $\mathbb Z$. By <1>4, $\alpha\in\mathbb Z[\omega]=R$. Therefore $R$ is integrally closed.
:::
:::
