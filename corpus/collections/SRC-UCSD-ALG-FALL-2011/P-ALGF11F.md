---
schema: qual/card@1
id: P-ALGF11F
kind: problem
title: Tower of Galois extensions when automorphisms extend
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 6 of the official UCSD Algebra Qualifying Exam, Fall 2011; both parts agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the automorphism-count proof for the tower and the real fourth-root counterexample over Q.
---

::: {.problem}
(a) Suppose that $K \subseteq L \subseteq M$ are fields such that $L/K$ and $M/L$ are Galois, and that every automorphism of $L/K$ extends to an automorphism of $M$.
Prove that $M/K$ is Galois.

(b) Give an example of fields $K \subseteq L \subseteq M$ such that $L/K$ and $M/L$ are Galois, but $M/K$ is not Galois.
:::


::: {.solution}
<1>1. Under the hypotheses of part (a), \(M/K\) has at least \([M:K]\) distinct \(K\)-automorphisms.
::: {.proof}
Let
\[
A:=\{\sigma\in\operatorname{Aut}_K(M):\sigma(L)=L\}.
\]
Restriction to \(L\) gives a homomorphism
\[
\operatorname{res}:A\longrightarrow\operatorname{Gal}(L/K).
\]
By hypothesis, every automorphism of \(L/K\) extends to an automorphism of \(M\), so \(\operatorname{res}\) is surjective.
Its kernel consists exactly of the automorphisms of \(M\) fixing \(L\):
\[
\ker(\operatorname{res})=\operatorname{Gal}(M/L).
\]
Since \(L/K\) and \(M/L\) are Galois,
\[
|\operatorname{Gal}(L/K)|=[L:K]
\]
and
\[
|\operatorname{Gal}(M/L)|=[M:L].
\]
Therefore the finite-group exact sequence gives
\[
|A|
=|\operatorname{Gal}(M/L)|\,|\operatorname{Gal}(L/K)|
=[M:L][L:K]
=[M:K].
\]
Thus \(M\) has at least \([M:K]\) distinct \(K\)-automorphisms.
:::

<1>2. The extension \(M/K\) is Galois.
::: {.proof}
The tower is finite because both \(L/K\) and \(M/L\) are finite Galois extensions.
For every finite extension,
\[
|\operatorname{Aut}_K(M)|\le[M:K].
\]
By <1>1, the subgroup \(A\subseteq\operatorname{Aut}_K(M)\) already has exactly \([M:K]\) elements.
Hence
\[
|\operatorname{Aut}_K(M)|=[M:K].
\]
A finite extension has as many base-field automorphisms as its degree if and only if it is Galois.
Therefore \(M/K\) is Galois.
:::

<1>3. For part (b), take
\[
K=\mathbb Q,
\qquad
L=\mathbb Q(\sqrt2),
\qquad
M=\mathbb Q(\sqrt[4]{2}).
\]
Then \(L/K\) and \(M/L\) are Galois.
::: {.proof}
The extension
\[
\mathbb Q(\sqrt2)/\mathbb Q
\]
is quadratic in characteristic zero, hence Galois.

Put
\[
\alpha=\sqrt[4]{2}.
\]
Then
\[
M=L(\alpha),
\qquad
\alpha^2=\sqrt2.
\]
Thus \(\alpha\) has minimal polynomial
\[
x^2-\sqrt2
\]
over \(L\), and this polynomial splits in \(M\) as
\[
(x-\alpha)(x+\alpha).
\]
It is separable because the characteristic is zero.
Therefore \(M/L\) is Galois.
:::

<1>4. The extension \(M/K\) in <1>3 is not Galois.
::: {.proof}
The polynomial
\[
x^4-2
\]
is Eisenstein at \(2\), so it is the minimal polynomial of \(\alpha\) over \(\mathbb Q\).
Its roots are
\[
\alpha,-\alpha,i\alpha,-i\alpha.
\]
The field
\[
M=\mathbb Q(\alpha)
\]
is contained in \(\mathbb R\), so it does not contain \(i\alpha\).
Hence the minimal polynomial \(x^4-2\) does not split over \(M\).
Thus \(M/\mathbb Q\) is not normal, and therefore is not Galois.
:::
:::
