---
schema: qual/card@1
id: P-ALGS17G
kind: problem
title: 'All intermediate fields of the splitting field of $x^{11}-1$ over $\QQ$'
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Let $L/\mathbb{Q}$ be a splitting field for the polynomial $x^{11} - 1$.
Find all intermediate fields $L/M/\mathbb{Q}$.
For each intermediate field $M$ find an element $\alpha \in M$ such that $M = \mathbb{Q}(\alpha)$.
:::

::: {.solution}
<1>1. Let \(\zeta=\zeta_{11}\) be a primitive eleventh root of unity.
Then
\[
L=\QQ(\zeta),\qquad [L:\QQ]=\varphi(11)=10,
\]
and
\[
G:=\operatorname{Gal}(L/\QQ)\cong (\ZZ/11\ZZ)^\times\cong C_{10}.
\]
::: {.proof}
The roots of \(x^{11}-1\) are \(1,\zeta,\dots,\zeta^{10}\), so its splitting field is \(\QQ(\zeta)\). For prime \(11\), the cyclotomic polynomial \(\Phi_{11}\) has degree \(10\), and the automorphisms are \(\sigma_a(\zeta)=\zeta^a\) for \(a\in(\ZZ/11\ZZ)^\times\). The latter group is cyclic of order \(10\).
:::

<1>2. Since \(G\cong C_{10}\), it has exactly one subgroup of each order \(1,2,5,10\), and no others.
Hence \(L/\QQ\) has exactly four intermediate fields, of degrees \(10,5,2,1\) over \(\QQ\), respectively.
::: {.proof}
A cyclic group has a unique subgroup for each divisor of its order.
Apply the Galois correspondence.
:::

<1>3. The fields of degrees \(1\) and \(10\) are
\[
\QQ=\QQ(0),\qquad L=\QQ(\zeta).
\]
::: {.proof}
Immediate.
:::

<1>4. The unique degree-\(5\) intermediate field is
\[
M_5=\QQ(\zeta+\zeta^{-1}).
\]
::: {.proof}
Complex conjugation is the unique element of order \(2\) in \(G\), and its fixed field is the maximal real subfield.
The element \(t=\zeta+\zeta^{-1}\) is fixed by conjugation.
Moreover \(\zeta\) satisfies
\[
X^2-tX+1=0
\]
over \(\QQ(t)\), while \(\zeta\notin\RR\); hence \([L:\QQ(t)]=2\). Therefore \([\QQ(t):\QQ]=5\), so \(\QQ(t)\) is exactly the fixed field of complex conjugation.
:::

<1>5. Let
\[
R=\{1,3,4,5,9\}\subset (\ZZ/11\ZZ)^\times
\]
be the subgroup of quadratic residues, and put
\[
\eta=\sum_{r\in R}\zeta^r
=\zeta+\zeta^3+\zeta^4+\zeta^5+\zeta^9.
\]
Then \(\eta\) is fixed by the order-\(5\) subgroup \(R\le G\).
::: {.proof}
For \(a\in R\), multiplication by \(a\) permutes \(R\), so
\[
\sigma_a(\eta)=\sum_{r\in R}\zeta^{ar}=\eta.
\]
Thus \(\eta\in L^R\), the unique quadratic intermediate field.
:::

<1>6. If
\[
\eta'=\zeta^2+\zeta^6+\zeta^7+\zeta^8+\zeta^{10}
\]
is the corresponding sum over the nonresidues, then
\[
\eta+\eta'=-1,
\qquad
\eta\eta'=3.
\]
::: {.proof}
The first identity follows from
\[
1+\zeta+\cdots+\zeta^{10}=0.
\]
For the product, the coefficient of \(\zeta^k\) in \( \eta\eta'=\sum_{r\in R,\,n\notin R}\zeta^{r+n} \) is the number of pairs \((r,n)\) with \(r+n\equiv k\pmod{11}\). A direct count gives coefficient \(2\) when \(k\in R\), coefficient \(2\) when \(k\notin R\), and coefficient \(5\) when \(k=0\). Hence
\[
\eta\eta'=5+2\sum_{k=1}^{10}\zeta^k=5-2=3.
\]
:::

<1>7. Therefore \(\eta\) satisfies
\[
X^2+X+3=0,
\]
so
\[
\QQ(\eta)=\QQ(\sqrt{-11}).
\]
::: {.proof}
By <1>6, \(\eta\) and \(\eta'\) have sum \(-1\) and product \(3\), hence are the roots of \(X^2+X+3\), whose discriminant is \(-11\). Since \(-11\) is not a square in \(\QQ\), the polynomial is irreducible, so \([\QQ(\eta):\QQ]=2\). Thus \(\QQ(\eta)=L^R\), the unique quadratic intermediate field.
:::

<1>8. Consequently the complete list of intermediate fields, with primitive elements, is
\[
\begin{array}{c|c}
M & \alpha\text{ with }M=\QQ(\alpha)\\ \hline
\QQ & 0\\
\QQ(\sqrt{-11}) & \eta=\zeta+\zeta^3+\zeta^4+\zeta^5+\zeta^9\\
\QQ(\zeta+\zeta^{-1}) & \zeta+\zeta^{-1}\\
L & \zeta
\end{array}
\]
and there are no other intermediate fields.
::: {.proof}
Combine <1>2--<1>7.
:::
:::
