---
schema: qual/card@1
id: P-ALGF14H
kind: problem
title: Irreducibility of $f$ and vanishing of $\minpoly(\alpha_1+\alpha_2)$ at pairwise sums
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 8 of the official UCSD Algebra Qualifying Exam, Fall 2014; both parts, the degree hypothesis, and the hint agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the tower-degree equalities, irreducibility statements, separability, and embedding count realizing every ordered pair of distinct roots.
---

::: {.problem}
Let $E/F$ be a field extension.
Let $f(x) \in F[x]$ be a polynomial of degree $n$ with $n$ distinct roots $\alpha_1, \ldots, \alpha_n$ in $E$.
Suppose $[F[\alpha_1, \alpha_2] : F] = n(n-1)$.

(i) Prove that $f(x)$ is irreducible over $F$ and $f(x)/(x-\alpha_1)$ is irreducible over $F[\alpha_1]$.

(ii) Suppose $g(x)$ is the minimal polynomial of $\alpha_1+\alpha_2$ over $F$.
Prove that $g(\alpha_i+\alpha_j) = 0$ for any $1 \leq i < j \leq n$.
(Hint: first show that $g(\alpha_1+\alpha_j) = 0$ for any $2 \leq j \leq n$; remember you can use the first part!)
:::


::: {.solution}
Because the roots are algebraic, we write \(F(\alpha_1,\alpha_2)\) for the field denoted \(F[\alpha_1,\alpha_2]\) in the statement.

<1>1. One has
\[
[F(\alpha_1):F]=n
\]
and
\[
[F(\alpha_1,\alpha_2):F(\alpha_1)]=n-1.
\]
::: {.proof}
Since \(\alpha_1\) is a root of the degree-\(n\) polynomial \(f\),
\[
[F(\alpha_1):F]\le n.
\]
Over \(F(\alpha_1)\), the element \(\alpha_2\) is a root of
\[
\frac{f(x)}{x-\alpha_1},
\]
which has degree \(n-1\).
Hence
\[
[F(\alpha_1,\alpha_2):F(\alpha_1)]\le n-1.
\]
The tower law gives
\[
n(n-1)
=[F(\alpha_1,\alpha_2):F]
=[F(\alpha_1,\alpha_2):F(\alpha_1)]
 [F(\alpha_1):F].
\]
The two factors on the right are at most \(n-1\) and \(n\), respectively, while their product attains the product of those upper bounds.
Therefore both bounds are equalities.
:::

<1>2. The polynomial \(f\) is irreducible over \(F\), and
\[
\frac{f(x)}{x-\alpha_1}
\]
is irreducible over \(F(\alpha_1)\).
::: {.proof}
Let \(m_1(x)\) be the minimal polynomial of \(\alpha_1\) over \(F\).
It divides \(f\), and by <1>1,
\[
\deg m_1=[F(\alpha_1):F]=n=\deg f.
\]
Thus \(f\) is a nonzero scalar multiple of \(m_1\), so \(f\) is irreducible.

Now let \(m_2(x)\) be the minimal polynomial of \(\alpha_2\) over \(F(\alpha_1)\).
It divides
\[
\frac{f(x)}{x-\alpha_1},
\]
and by <1>1,
\[
\deg m_2
=[F(\alpha_1,\alpha_2):F(\alpha_1)]
=n-1.
\]
The quotient \(f(x)/(x-\alpha_1)\) also has degree \(n-1\), so it is a nonzero scalar multiple of \(m_2\), hence irreducible over \(F(\alpha_1)\).
:::

<1>3. For every \(j\) with \(2\le j\le n\),
\[
g(\alpha_1+\alpha_j)=0.
\]
::: {.proof}
By <1>2, the minimal polynomial of \(\alpha_2\) over \(F(\alpha_1)\) is, up to a nonzero scalar,
\[
\frac{f(x)}{x-\alpha_1}.
\]
Its roots are precisely
\[
\alpha_2,\ldots,\alpha_n,
\]
and they are distinct by hypothesis.
Therefore for each \(j\ge2\), the assignment
\[
\alpha_2\longmapsto\alpha_j
\]
extends to an \(F(\alpha_1)\)-embedding
\[
\sigma_j:F(\alpha_1,\alpha_2)\longrightarrow E.
\]
Since
\[
g(\alpha_1+\alpha_2)=0
\]
and the coefficients of \(g\) lie in \(F\), applying \(\sigma_j\) gives
\[
0
=\sigma_j(g(\alpha_1+\alpha_2))
=g(\alpha_1+\alpha_j).
\]
:::

<1>4. The finite extension \(F(\alpha_1,\alpha_2)/F\) is separable and has exactly \(n(n-1)\) \(F\)-embeddings into an algebraic closure of \(F\).
::: {.proof}
By <1>2, \(f\) is the minimal polynomial of \(\alpha_1\) up to a scalar.
The polynomial \(f\) has \(n\) distinct roots by hypothesis, so \(\alpha_1\) is separable over \(F\).
Likewise, the minimal polynomial of \(\alpha_2\) over \(F(\alpha_1)\) is proportional to
\[
\frac{f(x)}{x-\alpha_1},
\]
whose roots \(\alpha_2,\ldots,\alpha_n\) are distinct.
Thus \(\alpha_2\) is separable over \(F(\alpha_1)\).
Therefore the tower
\[
F\subseteq F(\alpha_1)\subseteq F(\alpha_1,\alpha_2)
\]
is separable.
Its degree is \(n(n-1)\) by hypothesis, so it has exactly \(n(n-1)\) \(F\)-embeddings into an algebraic closure.
:::

<1>5. For every ordered pair \((i,j)\) with \(i\neq j\), there is an \(F\)-embedding
\[
\sigma_{ij}:F(\alpha_1,\alpha_2)\longrightarrow E
\]
such that
\[
\sigma_{ij}(\alpha_1)=\alpha_i,
\qquad
\sigma_{ij}(\alpha_2)=\alpha_j.
\]
::: {.proof}
Let \(\sigma\) be any \(F\)-embedding of \(F(\alpha_1,\alpha_2)\) into an algebraic closure.
Because \(f(\alpha_1)=0\) and \(\sigma\) fixes \(F\),
\[
f(\sigma(\alpha_1))=0.
\]
Thus
\[
\sigma(\alpha_1)=\alpha_i
\]
for some \(i\).

The relation
\[
\frac{f(\alpha_2)}{\alpha_2-\alpha_1}=0
\]
is more cleanly expressed by saying that \(\alpha_2\) is a root of the polynomial
\[
q_{\alpha_1}(x):=\frac{f(x)}{x-\alpha_1}
\in F(\alpha_1)[x].
\]
Applying \(\sigma\) to its coefficients sends it to
\[
q_{\alpha_i}(x)=\frac{f(x)}{x-\alpha_i}.
\]
Therefore \(\sigma(\alpha_2)\) is a root of \(q_{\alpha_i}\), so
\[
\sigma(\alpha_2)=\alpha_j
\]
for some \(j\neq i\).
Hence every embedding determines an ordered pair of distinct roots, and its image lies in \(E\).

An embedding is completely determined by the images of the generators \(\alpha_1\) and \(\alpha_2\), so two embeddings giving the same ordered pair are equal.
Thus the \(n(n-1)\) embeddings from <1>4 inject into the set of \(n(n-1)\) ordered pairs \((i,j)\) with \(i\neq j\).
The two finite sets have the same cardinality, so every ordered pair occurs.
:::

<1>6. For all \(i\neq j\),
\[
g(\alpha_i+\alpha_j)=0.
\]
::: {.proof}
Choose the embedding \(\sigma_{ij}\) from <1>5.
Since
\[
g(\alpha_1+\alpha_2)=0
\]
and \(g\in F[x]\), applying \(\sigma_{ij}\) gives
\[
0
=\sigma_{ij}(g(\alpha_1+\alpha_2))
=g(\alpha_i+\alpha_j).
\]
In particular this holds for every \(1\le i<j\le n\), as required.
:::
:::
