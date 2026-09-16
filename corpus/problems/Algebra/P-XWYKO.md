---
schema: qual/card@1
id: P-XWYKO
kind: problem
title: A single Jordan block of size $6$ for $T$ with $p_T(x)=\chi_T(x)=x^6$
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Nilpotence
  - Minimal and Characteristic Polynomials
relations: []
review: draft
---

::: {.problem}
Let $V$ be $6$-dimensional and let $T\in\operatorname{End}(V)$ satisfy
\[
T^6=0,
\qquad
T^5\ne0.
\]
Show that $T$ has a single Jordan block of size $6$.
:::

::: {.solution}
Since $T^6=0$, the minimal polynomial is a power of $x$:
\[
m_T(x)=x^r
\]
for some $r\le6$. The condition $T^5\ne0$ forces $r>5$, so
\[
m_T(x)=x^6.
\]

Because $\dim V=6$, the characteristic polynomial has degree $6$. Since the only eigenvalue is $0$,
\[
\chi_T(x)=x^6.
\]

In Jordan form, the exponent of $x$ in the minimal polynomial is the size of the largest Jordan block. Thus the largest block has size $6$. But the sum of all Jordan-block sizes is also $6$. Therefore there can be only one block:
\[
J(T)=J_6(0)
=
\begin{pmatrix}
0&1&0&0&0&0\\
0&0&1&0&0&0\\
0&0&0&1&0&0\\
0&0&0&0&1&0\\
0&0&0&0&0&1\\
0&0&0&0&0&0
\end{pmatrix}.
\]
:::
