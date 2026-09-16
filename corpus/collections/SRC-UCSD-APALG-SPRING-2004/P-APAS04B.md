---
schema: qual/card@1
id: P-APAS04B
kind: problem
title: Vanishing Hermitian forms; normality via norms and inner products
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
  - Norms
  - Normal Operators
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
(a) Let $A\in M_n$. Show that if $z^HAz=0$ for all $z\in\mathbb{C}^n$ then $A=0$.

(b) Give a $2\times 2$ example of $A\in M_2(\mathbb{R})$, where $A\neq 0$, but $x^TAx=0$
for all $x\in\mathbb{R}^2$.

(c) Show that $A\in M_n$ is normal iff $\|Ax\|_2=\|A^Hx\|_2$ for all $x\in\mathbb{C}^n$.

(d) Show that $A\in M_n$ is normal iff $(Ax,Ay)=(A^Hx,A^Hy)$ for all
$x,y\in\mathbb{C}^n$.

(Notation: $M_n$ denotes the set of $n\times n$ complex matrices; $M_2(\mathbb{R})$
denotes the set of $2\times 2$ real matrices.)
:::

::: {.solution}
<1>1. If $z^HAz=0$ for every $z\in\mathbb C^n$, then every diagonal entry of $A$ is
zero.
::: {.proof}
Write $A=(a_{ij})$ and let $e_i$ be the $i$th standard basis vector. Taking $z=e_i$
gives
\[
0=e_i^HAe_i=a_{ii}.
\]
Thus $a_{ii}=0$ for every $i$.
:::

<1>2. Every off-diagonal entry of $A$ is also zero; hence $A=0$.
::: {.proof}
Fix $i\neq j$. Taking $z=e_i+e_j$ and using <1>1 gives
\[
0=(e_i+e_j)^HA(e_i+e_j)=a_{ij}+a_{ji}.
\]
Taking $z=e_i+i e_j$ gives
\[
0=(e_i+i e_j)^HA(e_i+i e_j)=i a_{ij}-i a_{ji}.
\]
Hence $a_{ij}+a_{ji}=0$ and $a_{ij}-a_{ji}=0$, so $a_{ij}=a_{ji}=0$. Since this holds
for every $i\neq j$, all entries of $A$ vanish.
:::

<1>3. For part (b), the matrix
\[
A=\begin{pmatrix}0&1\\-1&0\end{pmatrix}
\]
is nonzero and satisfies $x^TAx=0$ for every $x\in\mathbb R^2$.
::: {.proof}
For $x=(u,v)^T$,
\[
x^TAx=(u,v)\begin{pmatrix}v\\-u\end{pmatrix}=uv-vu=0.
\]
The matrix is visibly nonzero.
:::

<1>4. If $A$ is normal, then $\|Ax\|_2=\|A^Hx\|_2$ for every $x\in\mathbb C^n$.
::: {.proof}
Normality means $A^HA=AA^H$. Therefore
\[
\|Ax\|_2^2=x^HA^HAx=x^HAA^Hx=\|A^Hx\|_2^2.
\]
Both norms are nonnegative, so they are equal.
:::

<1>5. Conversely, if $\|Ax\|_2=\|A^Hx\|_2$ for every $x$, then $A$ is normal.
::: {.proof}
For every $x$,
\[
0=\|Ax\|_2^2-\|A^Hx\|_2^2
 =x^H(A^HA-AA^H)x.
\]
Applying part (a), proved in <1>1--<1>2, to the matrix $A^HA-AA^H$ gives
\[
A^HA-AA^H=0.
\]
Thus $A$ is normal.
:::

<1>6. If $A$ is normal, then $(Ax,Ay)=(A^Hx,A^Hy)$ for every $x,y\in\mathbb C^n$.
::: {.proof}
Using the standard Hermitian inner product $(u,v)=u^Hv$ and $A^HA=AA^H$,
\[
(Ax,Ay)=x^HA^HAy=x^HAA^Hy=(A^Hx,A^Hy).
\]
:::

<1>7. Conversely, if $(Ax,Ay)=(A^Hx,A^Hy)$ for all $x,y$, then $A$ is normal.
::: {.proof}
Setting $y=x$ gives
\[
\|Ax\|_2^2=\|A^Hx\|_2^2
\]
for every $x$. By <1>5, $A$ is normal.
:::
:::
