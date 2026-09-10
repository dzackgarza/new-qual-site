---
schema: qual/card@1
id: P-TB7BG
kind: problem
title: Jordan canonical form of a nilpotent matrix
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Jordan Canonical Form
  - Matrices
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the statement and lower-shift block convention with original packet page 5, Rings and modules 3."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
  note: "Replaced the false minimal-polynomial and integer-divisibility inferences by a direct invariant-complement construction."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Verified the chain independence, projection formula, commutation identity, induction, and zero-operator case."
---

::: {.problem}
A square matrix $N$ over the complex numbers is nilpotent just in case $N^a=0$ for some positive integer $a$.
Show that every nilpotent $N$ is similar to a matrix of the form $$\begin{bmatrix}N_1&&&\\&N_2&&\\&&\ddots&\\&&&N_s\end{bmatrix}$$ where each $N_i$ is a square matrix of the form $$\begin{bmatrix}0&&&&\\1&0&&&\\&1&\ddots&&\\&&\ddots&0&\\&&&1&0\end{bmatrix}.$$
:::

::: {.solution}
Let $T$ be the operator represented by $N$ on $V=\mathbb C^n$.
We prove the assertion by induction on $n$. For $n=0$ the empty direct
sum is the required form. Suppose $n>0$ and the assertion holds in
smaller dimensions. Let $r\geq1$ be the least integer with $T^r=0$.

<1>1. There is an invariant subspace $U$ with basis
$v,Tv,\ldots,T^{r-1}v$.

::: proof
Minimality of $r$ gives $v\in V$ with $T^{r-1}v\ne0$.
If $\sum_{j=0}^{r-1}a_jT^jv=0$ is a nonzero linear relation, let $k$
be the least index with $a_k\ne0$. Applying $T^{r-1-k}$ gives
$a_kT^{r-1}v=0$: every term with larger index is killed by $T^r=0$.
This is a contradiction. The chain is therefore independent, and its
span $U$ is invariant because $T(T^{r-1}v)=0$.
:::

<1>2. The subspace $U$ has a $T$-invariant complement.

::: proof
Extend the chain in step <1>1 to a basis of $V$. Define a linear
functional $\ell:V\to\mathbb C$ to be $1$ on $T^{r-1}v$ and $0$
on every other vector of this basis. Define
$$
\pi(w)=\sum_{j=0}^{r-1}\ell\bigl(T^{r-1-j}w\bigr)T^jv.
$$
For $0\leq k<r$, the coefficient of $T^jv$ in $\pi(T^kv)$ is
$\ell(T^{r-1-j+k}v)$. It is $1$ when $j=k$, $0$ when $k<j$ by
the definition of $\ell$, and $0$ when $k>j$ because then the
exponent is at least $r$. Thus $\pi|_U$ is the identity.

Moreover, $T^r=0$ gives
$$
\pi(Tw)=\sum_{j=1}^{r-1}\ell(T^{r-j}w)T^jv
       =T\pi(w).
$$
These sums are empty and both sides are zero when $r=1$.
Consequently $W=\ker\pi$ is $T$-invariant. Since $\pi$ maps into
$U$ and restricts to its identity, every $w\in V$ has the unique
decomposition
$$
w=\pi(w)+(w-\pi(w))\in U\oplus W.
$$
Indeed, the second term lies in $\ker\pi$ and $U\cap\ker\pi=0$.
:::

<1>3. Combining bases of $U$ and $W$ produces the asserted blocks.

::: proof
On the ordered basis $v,Tv,\ldots,T^{r-1}v$ of $U$, the matrix of
$T|_U$ has ones immediately below the diagonal and all other entries
zero. The restriction $T|_W$ is nilpotent and $\dim W=n-r<n$.
By induction it has a basis with the required block diagonal matrix.
Concatenating these two bases gives a basis of $V$ in which $T$ has
the stated form. If $S$ has these basis vectors as columns in the
original coordinates, then $S$ is invertible and $S^{-1}NS$ is
exactly that block diagonal matrix.
:::
:::

::: remark
An arbitrary equality $N^a=0$ only implies that the minimal polynomial
divides $x^a$. It does not imply equality: for a nonempty zero matrix,
$N^2=0$ but the minimal polynomial is $x$. Also,
$x^b\mid x^c$ means $b\leq c$, not integer divisibility $b\mid c$.
:::
