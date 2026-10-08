---
schema: qual/card@1
id: P-GFO6Q
kind: problem
title: Maximal ideals of finite-dimensional $\CC$-algebras have codimension $1$, and
  classification in dimension $2$
classification:
  areas:
  - algebra
  topics:
  - Algebras
  - Maximal Ideals
  - Classification
relations: []
review: draft
---

::: {.problem}
Let $R$ be a finite-dimensional unital algebra over $\mathbb{C}$. The codimension of a $\mathbb{C}$-subspace $I \subseteq R$ is defined by
$$
\operatorname{codim}_R I = \dim_{\mathbb{C}} R - \dim_{\mathbb{C}} I.
$$

(a) Show that every maximal ideal $\mathfrak{m} \subset R$ has codimension $1$.

(b) Suppose that $\dim_{\mathbb{C}} R = 2$. Show that there exists a surjective homomorphism of $\mathbb{C}$-algebras from the polynomial ring $\mathbb{C}[t]$ to $R$.

(c) Classify all unital $\mathbb{C}$-algebras $R$ with $\dim_{\mathbb{C}} R = 2$ up to isomorphism, and list their maximal ideals.
:::

::: {.solution}
<1>1. Part (a) is false for noncommutative algebras.

::: {.proof}
Let $R=M_2(\mathbb C)$. This is a simple unital $\mathbb C$-algebra: if a nonzero two-sided ideal contains a matrix $A=(a_{ij})$ with $a_{ij}\neq0$, multiplication by matrix units yields $E_{ki}AE_{jl}=a_{ij}E_{kl}$, so the ideal contains every matrix unit and therefore equals $R$. Thus $(0)$ is a maximal two-sided ideal and
\[
\boxed{\operatorname{codim}_R(0)=4\neq1}.
\]
If the term "ideal" denotes a left ideal, the claim also fails: a maximal left ideal of $M_2(\mathbb C)$ has codimension two. Under the additional hypothesis that $R$ is commutative, however, (a) is true: $R/\mathfrak m$ is a finite field extension of the algebraically closed field $\mathbb C$, hence equals $\mathbb C$ and has dimension one.
:::

<1>2. If $\dim_{\mathbb C}R=2$, then a surjective $\mathbb C$-algebra homomorphism $\mathbb C[t]\to R$ exists.

::: {.proof}
Choose $u\in R$ outside $\mathbb C1_R$. The two elements $1_R,u$ form a vector-space basis of $R$. Since every element is a linear combination of $1_R$ and $u$, the unital homomorphism $\mathbb C[t]\to R$ sending $t\mapsto u$ is surjective. (Its existence is well-defined even without an initial commutativity assumption because the domain is the polynomial algebra on one generator.)
:::

<1>3. Up to isomorphism, the two-dimensional unital complex algebras are
\[
\boxed{\mathbb C\times\mathbb C\quad\text{and}\quad
\mathbb C[\varepsilon]/(\varepsilon^2)}.
\]
The first has maximal ideals $\mathbb C\times0$ and $0\times\mathbb C$; the second has the unique maximal ideal $(\varepsilon)$.

::: {.proof}
By step <1>2, $R\cong\mathbb C[t]/(f)$ for an ideal $(f)$ of $\mathbb C[t]$. Since $\dim_{\mathbb C}R=2$, the monic generator $f$ has degree two. Over $\mathbb C$, it factors as $(t-a)(t-b)$. If $a\neq b$, the Chinese remainder theorem gives $R\cong\mathbb C\times\mathbb C$, whose maximal ideals are the kernels of the two projections. If $a=b$, translation of $t$ gives $R\cong\mathbb C[\varepsilon]/(\varepsilon^2)$; every element $c+d\varepsilon$ with $c\neq0$ is a unit, and its nonunits form the unique maximal ideal $(\varepsilon)$. These rings are not isomorphic because the second has a nonzero nilpotent element while the first is reduced.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 supplies the counterexample to part (a) as stated and explains its commutative variant; steps <1>2 and <1>3 prove parts (b) and (c).
:::
:::

::: {.remark}
The original solution is superseded: the claim that every maximal two-sided ideal of a finite-dimensional complex algebra has codimension one fails for matrix algebras.
:::
