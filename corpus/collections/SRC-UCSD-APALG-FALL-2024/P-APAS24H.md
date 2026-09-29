---
schema: qual/card@1
id: P-APAS24H
kind: problem
title: Irreducibility of the standard representation of $S_n$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
  - Permutations
relations: []
review: draft
---

::: {.problem}
State the definition of the standard representation of the symmetric group and compute its character in terms of the enumeration of fixed points in permutations.
Using character theory or otherwise, prove that the standard representation is irreducible.
:::

::: {.solution}

Assume \(n\ge2\). Let \(S_n\) act on \(\mathbb C^n\) by permuting the standard basis \(e_1,\ldots,e_n\). The **standard representation** is the invariant subspace
\[
V:=\left\{(z_1,\ldots,z_n)\in\mathbb C^n:\sum_{i=1}^n z_i=0\right\}.
\]
Equivalently,
\[
\mathbb C^n=\mathbb C(1,\ldots,1)\oplus V,
\]
where the first summand is the trivial representation.

::: pf

::: {.pf-step #character-formula}
The character of the permutation representation \(\mathbb C^n\) is
\[
\chi_{\mathrm{perm}}(\sigma)=\operatorname{fix}(\sigma).
\]
Hence the standard character is
\[
\chi_V(\sigma)=\operatorname{fix}(\sigma)-1.
\]

::: pf-proof
In the standard basis, the matrix of \(\sigma\) is a permutation matrix. Its diagonal entry in position \(i\) is \(1\) exactly when \(\sigma(i)=i\), so its trace is the number of fixed points. Since
\[
\mathbb C^n\cong\mathbf1\oplus V,
\]
characters add under direct sums, giving
\[
\chi_V=\chi_{\mathrm{perm}}-1.
\]
:::

:::

::: {.pf-step #sum-of-fixed-points}
One has
\[
\sum_{\sigma\in S_n}\operatorname{fix}(\sigma)=n!.
\]

::: pf-proof
Count pairs \((\sigma,i)\) with \(\sigma(i)=i\). For each \(i\), there are \((n-1)!\) permutations fixing \(i\). Hence the number of such pairs is
\[
n(n-1)!=n!.
\]
On the other hand, summing over \(\sigma\) counts the same pairs as \(\sum_\sigma\operatorname{fix}(\sigma)\).
:::

:::

::: {.pf-step #sum-of-squared-fixed-points}
One has
\[
\sum_{\sigma\in S_n}\operatorname{fix}(\sigma)^2=2n!.
\]

::: pf-proof
The square \(\operatorname{fix}(\sigma)^2\) counts ordered pairs \((i,j)\) of fixed points of \(\sigma\). Count triples \((\sigma,i,j)\) with \(\sigma(i)=i\) and \(\sigma(j)=j\).

If \(i=j\), there are \(n(n-1)!=n!\) such triples.
If \(i\ne j\), there are \(n(n-1)(n-2)!=n!\) such triples.
Thus the total is \(2n!\).
:::

:::

::: {.pf-step #standard-character-norm-one}
The standard character has norm \(1\):
\[
\langle\chi_V,\chi_V\rangle=1.
\]

::: pf-proof
Using steps [](#character-formula){.pf-ref}, [](#sum-of-fixed-points){.pf-ref} and [](#sum-of-squared-fixed-points){.pf-ref},
\[
\begin{aligned}
\langle\chi_V,\chi_V\rangle
&=\frac1{n!}\sum_{\sigma\in S_n}|\operatorname{fix}(\sigma)-1|^2\\
&=\frac1{n!}\left(
\sum_\sigma\operatorname{fix}(\sigma)^2
-2\sum_\sigma\operatorname{fix}(\sigma)
+\sum_\sigma1
\right)\\
&=\frac{2n!-2n!+n!}{n!}=1.
\end{aligned}
\]
:::

:::

::: {.pf-step #standard-rep-irreducible}
Therefore the standard representation of \(S_n\) is irreducible for \(n\ge2\).

::: pf-proof
For a finite group over \(\mathbb C\), a character is irreducible if and only if its inner product with itself is \(1\). Apply step [](#standard-character-norm-one){.pf-ref}.

For \(n=1\), the sum-zero subspace is \(0\), so the usual nonzero irreducibility statement is vacuous only after excluding this degenerate case.
:::

:::

::: pf-qed
Step [](#character-formula){.pf-ref} computes the character; step [](#standard-rep-irreducible){.pf-ref} proves irreducibility.
:::

:::

:::
