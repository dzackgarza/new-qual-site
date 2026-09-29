---
schema: qual/card@1
id: P-BERK91S-08
kind: problem
title: Rank and simple spectrum of an irreducible symmetric tridiagonal matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-23
  note: Compared the real symmetric tridiagonal matrix, nonzero off-diagonal entries, and both conclusions with Problem 8 in the retained MinerU Flash extraction of Spring91.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $T$ be a real symmetric tridiagonal $n\times n$ matrix with diagonal entries $a_1,\ldots,a_n$ and nonzero off-diagonal entries $b_1,\ldots,b_{n-1}$:
$$
T=\begin{pmatrix}
a_1&b_1&&&0\\
b_1&a_2&b_2&&\\
&b_2&a_3&\ddots&\\
&&\ddots&\ddots&b_{n-1}\\
0&&&b_{n-1}&a_n
\end{pmatrix}.
$$
Prove that

(a) $\operatorname{rank}T\ge n-1$;

(b) $T$ has $n$ distinct eigenvalues.
:::

::: {.solution}
Let $I_n$ be the identity matrix. For $\lambda\in\RR$, let
$E_\lambda\coloneqq\ker(T-\lambda I_n)\subseteq\RR^n$.

::: pf

::: {.pf-step #s1}

For every $\lambda\in\RR$, $\dim E_\lambda\le1$.

::: pf-proof

Let $v=(v_1,\ldots,v_n)\in E_\lambda$. For $n=1$, the coordinate
$v_1$ determines $v$. For $n\ge2$, the first row of $Tv=\lambda v$
gives
$$
v_2=\frac{\lambda-a_1}{b_1}v_1.
$$
For $2\le j\le n-1$, the $j$th row gives
$$
v_{j+1}
=\frac{(\lambda-a_j)v_j-b_{j-1}v_{j-1}}{b_j}.
$$
Every denominator is nonzero by hypothesis. These equations determine
$v_2,\ldots,v_n$ successively from $v_1$; in particular, $v_1=0$
forces $v=0$. Thus the linear map
$$
E_\lambda\longrightarrow\RR,
\qquad v\longmapsto v_1,
$$
is injective, and $\dim E_\lambda\le1$.

:::

:::

::: {.pf-step #s2}

Part (a) holds: $\operatorname{rank}T\ge n-1$.

::: pf-proof

Taking $\lambda=0$ in step [](#s1){.pf-ref} gives $\dim\ker T\le1$.
The rank-nullity theorem therefore yields
$$
\operatorname{rank}T=n-\dim\ker T\ge n-1.
$$

:::

:::

::: {.pf-step #s3}

Part (b) holds: $T$ has $n$ distinct eigenvalues.

::: pf-proof

Since $T$ is real and symmetric, the [[T-WQHMA|spectral theorem]]
gives a basis of $\RR^n$ consisting of eigenvectors with real
eigenvalues. Let $\lambda_1,\ldots,\lambda_m$ be its distinct
eigenvalues. The corresponding eigenspaces give the direct sum
$$
\RR^n=E_{\lambda_1}\oplus\cdots\oplus E_{\lambda_m}.
$$
Each $E_{\lambda_j}$ is nonzero and has dimension at most $1$ by
step [](#s1){.pf-ref}, so each has dimension $1$. Taking dimensions gives
$$
n=\sum_{j=1}^m\dim E_{\lambda_j}=m.
$$
Hence the number of distinct eigenvalues is $n$.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} prove parts (a) and (b), respectively.

:::

:::

:::
