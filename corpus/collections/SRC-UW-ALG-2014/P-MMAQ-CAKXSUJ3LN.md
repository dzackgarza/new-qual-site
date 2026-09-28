---
schema: qual/card@1
id: P-MMAQ-CAKXSUJ3LN
kind: problem
title: Rational irreps of $C_p$ of dimensions $1$ and $p-1$, and abelian groups whose
  rational representations are absolutely irreducible
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $C_p$ denote the cyclic group of order $p$.

-   Show that $C_p$ has two irreducible representations over
    $\mathbb Q$ (up to isomorphism), one of dimension 1
    and one of dimension $p-1$.

-   Let $G$ be a finite group, and let $\rho:G\rightarrow
    \GL_n(\mathbb Q)$ be a representation of $G$ over $\mathbb Q$.
    Let $\rho_{\mathbb C}:G\rightarrow\GL_n(\mathbb C)$ denote
    $\rho$ followed by the inclusion $\GL_n(\mathbb Q)\rightarrow
    \GL_n(\mathbb C)$. Thus $\rho_{\mathbb C}$ is a representation
    of $G$ over $\mathbb C$, called the *complexification*
    of $\rho$. We say that an irreducible representation $\rho$
    of $G$ is *absolutely irreducible* if its
    complexification remains irreducible over $\mathbb C$.\\
    Now suppose $G$ is abelian and that every representation
    of $G$ over $\mathbb Q$ is absolutely irreducible. Show that
    $G\cong(C_2)^k$ for some $k$ (i.e., is a product of
    cyclic groups of order 2).
:::


::: {.solution}
<1>1. As a \(\mathbb Q\)-algebra,
\[
\mathbb Q[C_p]\cong \mathbb Q[x]/(x^p-1)
\cong \mathbb Q[x]/(x-1)\times \mathbb Q[x]/(\Phi_p(x)).
\]
::: {.proof}
If \(g\) generates \(C_p\), the map \(\mathbb Q[x]\to\mathbb Q[C_p]\) sending \(x\mapsto g\) has kernel \((x^p-1)\). Since
\[
x^p-1=(x-1)\Phi_p(x)
\]
and the two factors are coprime over \(\mathbb Q\), the Chinese remainder theorem gives the product decomposition. The cyclotomic polynomial \(\Phi_p\) is irreducible over \(\mathbb Q\), so
\[
\mathbb Q[x]/(\Phi_p(x))\cong\mathbb Q(\zeta_p).
\]
:::

<1>2. Hence \(C_p\) has exactly two irreducible rational representations up to isomorphism: the trivial representation of dimension \(1\), and one representation of dimension \(p-1\).
::: {.proof}
The simple modules over a finite product of fields are exactly the simple modules coming from one factor. Thus the two simple \(\mathbb Q[C_p]\)-modules are
\[
\mathbb Q
\quad\text{and}\quad
\mathbb Q(\zeta_p).
\]
Their dimensions over \(\mathbb Q\) are \(1\) and
\[
[\mathbb Q(\zeta_p):\mathbb Q]=\varphi(p)=p-1.
\]
:::

<1>3. If \(p>2\), the \((p-1)\)-dimensional rational irreducible representation of \(C_p\) is not absolutely irreducible.
::: {.proof}
After extending scalars to \(\mathbb C\),
\[
\mathbb Q(\zeta_p)\otimes_{\mathbb Q}\mathbb C
\cong
\bigoplus_{j=1}^{p-1}\mathbb C_{\chi_j},
\]
where \(\chi_j(g)=\zeta_p^j\). Thus its complexification is a direct sum of \(p-1>1\) one-dimensional characters.
:::

<1>4. The nontrivial two-dimensional rational irreducible representation of \(C_4\) is not absolutely irreducible.
::: {.proof}
We have
\[
\mathbb Q[C_4]\cong
\mathbb Q[x]/(x^4-1),
\]
and the factor \(x^2+1\) gives the simple module
\[
\mathbb Q(i),
\]
of dimension \(2\). After complexification,
\[
\mathbb Q(i)\otimes_{\mathbb Q}\mathbb C
\cong\mathbb C\oplus\mathbb C,
\]
corresponding to the two characters sending a generator of \(C_4\) to \(i\) and \(-i\). Hence this rational irreducible is not absolutely irreducible.
:::

<1>5. Under the hypothesis in the problem, every element of the finite abelian group \(G\) has order dividing \(2\).
::: {.proof}
Suppose instead that \(G\) has an element of order greater than \(2\). By the structure theorem for finite abelian groups, one of the following holds:

- some odd prime \(p\) divides the order of an element of \(G\), in which case \(G\) has a quotient isomorphic to \(C_p\); or
- the exponent of \(G\) is divisible by \(4\), in which case \(G\) has a quotient isomorphic to \(C_4\).

Let \(q:G\twoheadrightarrow H\) be such a quotient. Inflate along \(q\) the rational irreducible representation of \(H\) from <1>3 or <1>4. Inflation preserves irreducibility because a subspace is \(G\)-stable exactly when it is \(H\)-stable, and its complexification remains reducible because the action still factors through \(H\). This contradicts the hypothesis that every irreducible rational representation of \(G\) is absolutely irreducible.
:::

<1>6. Therefore
\[
G\cong(C_2)^k
\]
for some \(k\ge0\).
::: {.proof}
By <1>5, every nonidentity element of the finite abelian group \(G\) has order \(2\). Thus \(G\) is naturally a vector space over \(\mathbb F_2\). Since it is finite, it has finite dimension \(k\), so as an abelian group
\[
G\cong (C_2)^k.
\]
:::
:::
