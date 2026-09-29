---
schema: qual/card@1
id: P-APAF22F
kind: problem
title: Symmetric square is a subrepresentation; character formula via $\chi(g^2)$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite group and let $V$ be a finite-dimensional complex representation of $G$ with character $\chi$.
Consider the operator $\sigma$ on $V \otimes V$ which swaps factors.
Let $S^2(V)$ be the subspace invariant under $\sigma$.

(a) Show that $S^2(V)$ is a $G$-subrepresentation of $V \otimes V$.

(b) Let $\chi_2$ be the character of $S^2(V)$.
Show that
\[
\chi_2(g) = \frac{1}{2}\bigl(\chi(g)^2 + \chi(g^2)\bigr)
\]
for all $g \in G$ (the product in $G$ is written as multiplication).

[Hint: Consider a basis of eigenvectors for $g$ acting on $V$ and use this to find a basis of eigenvectors for $S^2(V)$.]
:::

::: {.solution}

::: pf

::: {.pf-step #sigma-commutes-with-g-action}
The flip map
\[
\sigma(v\otimes w)=w\otimes v
\]
commutes with the diagonal action of $G$ on $V\otimes V$.

::: pf-proof
For $g\in G$ and pure tensors,
\[
\sigma\bigl(g\cdot(v\otimes w)\bigr)
=\sigma(gv\otimes gw)
=gw\otimes gv
=g\cdot(w\otimes v)
=g\cdot\sigma(v\otimes w).
\]
By linearity, $\sigma g=g\sigma$ on all of $V\otimes V$.
:::

:::

::: {.pf-step #s2v-is-subrepresentation}
Hence
\[
S^2(V)=\ker(\sigma-I)
\]
is a $G$-subrepresentation of $V\otimes V$.

::: pf-proof
If $u\in S^2(V)$, then $\sigma u=u$. By step [](#sigma-commutes-with-g-action){.pf-ref},
\[
\sigma(gu)=g\sigma(u)=gu,
\]
so $gu\in S^2(V)$ for every $g\in G$. This proves part (a).
:::

:::

::: {.pf-step #eigenbasis-of-s2v}
Fix $g\in G$. Since $g$ has finite order, its action on $V$ is diagonalizable over $\mathbb C$. Choose an eigenbasis
\[
v_1,\ldots,v_n,
\qquad
gv_i=\lambda_i v_i.
\]
Then a basis of $S^2(V)$ is
\[
v_i\otimes v_i\quad(1\le i\le n),
\qquad
v_i\otimes v_j+v_j\otimes v_i\quad(1\le i<j\le n).
\]

::: pf-proof
Because $g$ has finite order, its minimal polynomial divides $x^m-1$ for some $m$, and $x^m-1$ has distinct roots over $\mathbb C$, so $g$ is diagonalizable.
The displayed vectors are the standard basis of the $+1$-eigenspace of the flip on $V\otimes V$.
:::

:::

::: {.pf-step #eigenvalues-on-s2v}
On the basis in step [](#eigenbasis-of-s2v){.pf-ref}, the eigenvalues of $g$ acting on $S^2(V)$ are
\[
\lambda_i^2\quad(1\le i\le n),
\qquad
\lambda_i\lambda_j\quad(1\le i<j\le n).
\]
Hence
\[
\chi_2(g)
=\sum_i\lambda_i^2+\sum_{i<j}\lambda_i\lambda_j.
\]

::: pf-proof
For the diagonal tensors,
\[
g(v_i\otimes v_i)=\lambda_i^2(v_i\otimes v_i).
\]
For $i<j$,
\[
g(v_i\otimes v_j+v_j\otimes v_i)
=\lambda_i\lambda_j(v_i\otimes v_j+v_j\otimes v_i).
\]
Taking the trace gives the stated sum.
:::

:::

::: {.pf-step #chi2-formula}
Therefore
\[
\boxed{\chi_2(g)=\frac12\bigl(\chi(g)^2+\chi(g^2)\bigr)}.
\]

::: pf-proof
Since
\[
\chi(g)=\sum_i\lambda_i,
\qquad
\chi(g^2)=\sum_i\lambda_i^2,
\]
we have
\[
\chi(g)^2
=\sum_i\lambda_i^2+2\sum_{i<j}\lambda_i\lambda_j.
\]
Thus
\[
\frac12\bigl(\chi(g)^2+\chi(g^2)\bigr)
=\sum_i\lambda_i^2+\sum_{i<j}\lambda_i\lambda_j
=\chi_2(g)
\]
by step [](#eigenvalues-on-s2v){.pf-ref}. This proves part (b).
:::

:::

::: pf-qed
Step [](#s2v-is-subrepresentation){.pf-ref} answers part (a); step [](#chi2-formula){.pf-ref} answers part (b).
:::

:::

:::
