---
schema: qual/card@1
id: P-APAF11A
kind: problem
title: Character table of $S_4$ via Murnaghan–Nakayama; restriction of $A^{(2,2)}$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
  - Character Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: problem
Suppose that $\lambda=(\lambda_1\geq\lambda_2\geq\cdots\geq\lambda_k)$ is a partition of $n$.
Then $A^\lambda$ denotes the irreducible representation of the symmetric group $S_n$ such that the Frobenius image of $\chi^{A^\lambda}=\chi^\lambda$ is the Schur function $S_\lambda(x_1,\ldots,x_N)$ where $N>n$, and $S_{\lambda_1}\times\cdots\times S_{\lambda_k}$ denotes the Young subgroup of $S_n$ corresponding to $\lambda$.

(a) Use the Murnaghnam–Nakayama rule to compute the character table of $S_4$.

(b) Express $\chi^{A^{(2,2)}}\downarrow_{S_2\times S_2}^{S_4}$ as a sum of irreducible characters of $S_2\times S_2$.
(Hint: First write out the character table for $S_2\times S_2$.)
:::


::: {.solution}
Let the conjugacy classes of $S_4$ be indexed by cycle type in the order
\[
(1^4),\quad (2,1^2),\quad (2^2),\quad (3,1),\quad (4).
\]
Their sizes are respectively
\[
1,6,3,8,6.
\]

<1>1. By the Murnaghan--Nakayama rule, the irreducible character table of $S_4$ is
\[
\begin{array}{c|rrrrr}
\lambda &(1^4)&(2,1^2)&(2^2)&(3,1)&(4)\\ \hline
(4)       &1& 1& 1& 1& 1\\
(3,1)     &3& 1&-1& 0&-1\\
(2,2)     &2& 0& 2&-1& 0\\
(2,1,1)   &3&-1&-1& 0& 1\\
(1^4)     &1&-1& 1& 1&-1
\end{array}.
\]
::: {.proof}
We use the Murnaghan--Nakayama rule in the form
\[
\chi^\lambda_{(r,\mu)}
=
\sum_{\nu}\,(-1)^{\operatorname{ht}(\lambda/\nu)-1}\chi^\nu_\mu,
\]
where the sum is over partitions $\nu$ obtained from $\lambda$ by removing a rim hook of size $r$.

For the identity class, the values are the dimensions $f^\lambda$, computed from the hook-length formula:
\[
f^{(4)}=1,\quad f^{(3,1)}=3,\quad f^{(2,2)}=2,\quad f^{(2,1,1)}=3,\quad f^{(1^4)}=1.
\]

For the one-row partition $(4)$, every removable rim hook has height $1$, so every character value is $1$.
For the one-column partition $(1^4)$, a rim hook of length $r$ has height $r$, hence contributes $(-1)^{r-1}$; therefore this row is
\[
1,-1,1,1,-1,
\]
the sign character.

For $\lambda=(3,1)$:
- at cycle type $(2,1^2)$, the unique removable $2$-rim hook is the horizontal strip consisting of the two rightmost boxes of the first row. It has height $1$ and leaves $(1,1)$, so the value is $f^{(1,1)}=1$;
- at $(2^2)$, after that removal the remaining partition is $(1,1)$, whose value on a transposition is $-1$, so the value is $-1$;
- at $(3,1)$, there is no removable $3$-rim hook leaving a Young diagram, so the value is $0$;
- at $(4)$, the whole diagram is a rim hook of height $2$, giving $-1$.
Thus the row is $3,1,-1,0,-1$.

For $\lambda=(2,2)$:
- at $(2,1^2)$, the two removable $2$-rim hooks have opposite signs and leave one-box-count contributions of equal size, so the value is $0$;
- at $(2^2)$, the two successive removals contribute $1+1=2$;
- at $(3,1)$, the unique admissible $3$-rim hook has height $2$, so the value is $-1$;
- there is no rim hook of length $4$ because the $2\times2$ diagram contains a $2\times2$ block, so the value is $0$.
Hence the row is $2,0,2,-1,0$.

Finally, $(2,1,1)$ is conjugate to $(3,1)$, and conjugating a partition tensors the corresponding irreducible representation with the sign representation. Therefore its row is obtained by multiplying the $(3,1)$ row by the sign row, giving
\[
3,-1,-1,0,1.
\]
This yields the displayed table.
:::

<1>2. Let
\[
H=S_2\times S_2
=\{1,(12),(34),(12)(34)\}.
\]
The restricted character of $A^{(2,2)}$ on these four elements is
\[
\chi^{(2,2)}\!\downarrow_H=(2,0,0,2).
\]
::: {.proof}
The identity has cycle type $(1^4)$, each of $(12)$ and $(34)$ has cycle type $(2,1^2)$, and $(12)(34)$ has cycle type $(2^2)$. Reading the $(2,2)$ row of <1>1 gives the values
\[
2,0,0,2.
\]
:::

<1>3. The four irreducible characters of $H\cong C_2\times C_2$ are
\[
\begin{array}{c|rrrr}
&1&(12)&(34)&(12)(34)\\ \hline
\mathbf 1\boxtimes\mathbf 1&1&1&1&1\\
\mathbf 1\boxtimes\operatorname{sgn}&1&1&-1&-1\\
\operatorname{sgn}\boxtimes\mathbf 1&1&-1&1&-1\\
\operatorname{sgn}\boxtimes\operatorname{sgn}&1&-1&-1&1
\end{array}.
\]
::: {.proof}
Each factor $S_2$ has exactly two irreducible characters, the trivial and sign characters. Since $H$ is a direct product, its irreducible characters are their external tensor products, producing the four rows displayed.
:::

<1>4. Therefore
\[
\chi^{A^{(2,2)}}\!\downarrow_{S_2\times S_2}^{S_4}
=
(\mathbf 1\boxtimes\mathbf 1)
+
(\operatorname{sgn}\boxtimes\operatorname{sgn}).
\]
::: {.proof}
For an irreducible character $\theta$ of $H$, its multiplicity in the restriction is
\[
\langle (2,0,0,2),\theta\rangle_H
=
\frac14\sum_{h\in H}(2,0,0,2)(h)\overline{\theta(h)}.
\]
For $\mathbf 1\boxtimes\mathbf 1$ this equals
\[
\frac14(2+2)=1,
\]
and for $\operatorname{sgn}\boxtimes\operatorname{sgn}$ it equals
\[
\frac14(2+2)=1.
\]
For each of the two mixed characters it equals
\[
\frac14(2-2)=0.
\]
Hence the restriction is exactly the sum displayed above. This proves part (b).
:::
:::
