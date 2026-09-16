---
schema: qual/card@1
id: P-MMAQ-6GE2BXA773
kind: problem
title: Order of $\GL_2(\FF_p)$ and its subgroups of order $p$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Finite Fields
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $p$ be a positive prime number, $\mathbb F_p$ the field with $p$ elements, and let $G=\text{GL}_2(\mathbb F_p)$.

- Compute the order of $G$, $|G|$.

- Write down an explicit isomorphism from $\mathbb Z/p\mathbb Z$ to `\begin{align*} U=\left\{
  \begin{pmatrix}
    1 & a\\
    0 & 1
  \end{pmatrix}
  \bigg|a\in\mathbb F_p\right\}. \end{align*}`{=tex}

- How many subgroups of order $p$ does $G$ have?

  > Hint: compute $gug\inv$ for $g\in G$ and $u\in U$; use this to find the size of the normalizer of $U$ in $G$.
:::


::: {.solution}
<1>1. The order of $G=\operatorname{GL}_2(\mathbb F_p)$ is
\[
|G|=(p^2-1)(p^2-p)=p(p-1)^2(p+1).
\]
::: {.proof}
The first column of an invertible $2\times2$ matrix may be any nonzero vector in $\mathbb F_p^2$, giving $p^2-1$ choices. Once it is chosen, the second column may be any vector not in its one-dimensional span, giving $p^2-p$ choices.
:::

<1>2. The map
\[
\varphi:\mathbb Z/p\mathbb Z\longrightarrow U,
\qquad
\bar a\longmapsto
\begin{pmatrix}1&a\\0&1\end{pmatrix}
\]
is an isomorphism of groups.
::: {.proof}
Matrix multiplication gives
\[
\begin{pmatrix}1&a\\0&1\end{pmatrix}
\begin{pmatrix}1&b\\0&1\end{pmatrix}
=
\begin{pmatrix}1&a+b\\0&1\end{pmatrix},
\]
so $\varphi$ is a homomorphism from the additive group of $\mathbb F_p$. It is visibly bijective.
:::

<1>3. The subgroup $U$ is a Sylow $p$-subgroup of $G$.
::: {.proof}
By <1>2, $|U|=p$. From <1>1,
\[
|G|=p(p-1)^2(p+1),
\]
and neither $p-1$ nor $p+1$ is divisible by $p$. Hence the highest power of $p$ dividing $|G|$ is $p$ itself.
:::

<1>4. The normalizer of $U$ is the subgroup
\[
N_G(U)=
\left\{
\begin{pmatrix}a&b\\0&d\end{pmatrix}:
 a,d\in\mathbb F_p^\times,\ b\in\mathbb F_p
\right\}.
\]
::: {.proof}
Every nonidentity element of $U$ has the form
\[
u_t=\begin{pmatrix}1&t\\0&1\end{pmatrix},\qquad t\ne0,
\]
and its fixed-point space is exactly the line
\[
L=\mathbb F_p e_1.
\]
If $gUg^{-1}=U$, then for nontrivial $u\in U$, the fixed line of $gug^{-1}$ is $gL$. But every nontrivial element of $U$ has fixed line $L$, so $gL=L$. Thus $g$ is upper triangular.

Conversely, if
\[
g=\begin{pmatrix}a&b\\0&d\end{pmatrix}
\]
with $a,d\ne0$, then a direct calculation gives
\[
g\begin{pmatrix}1&t\\0&1\end{pmatrix}g^{-1}
=
\begin{pmatrix}1&(a/d)t\\0&1\end{pmatrix}\in U.
\]
Hence every invertible upper-triangular matrix normalizes $U$.
:::

<1>5. There are exactly $p+1$ subgroups of order $p$ in $G$.
::: {.proof}
By <1>3, the subgroups of order $p$ are exactly the Sylow $p$-subgroups, and all Sylow $p$-subgroups are conjugate. Therefore their number is
\[
[G:N_G(U)].
\]
By <1>4,
\[
|N_G(U)|=p(p-1)^2,
\]
so
\[
[G:N_G(U)]
=\frac{p(p-1)^2(p+1)}{p(p-1)^2}
=p+1.
\]
:::
:::
