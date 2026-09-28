---
schema: qual/card@1
id: P-APAS18G
kind: problem
title: Linear independence of standard monomials for a Gröbner basis
classification:
  areas:
  - applied-algebra
  topics:
  - Gröbner Bases
relations: []
review: draft
---

::: {.problem}
Let $k$ be a field and let $I\subseteq k[x_1,\ldots,x_n]$ be an ideal.
Fix a monomial order $<$ and let $G=\{g_1,\ldots,g_s\}$ be a Gröbner basis for $I$ with respect to $<$.

(a) Explain why the set of cosets
\[
\bigl\{m+I:\ m\text{ a monomial in }x_1,\ldots,x_n\text{ and }\operatorname{LM}(g_i)\nmid m\text{ for }1\leq i\leq s\bigr\}
\]
is linearly independent in the quotient $k[x_1,\ldots,x_n]/I$.

(b) Is the conclusion of (a) still true if $G$ is a basis for $I$ which is not necessarily Gröbner?
Prove or give a counterexample.
:::

::: {.solution}
Let \(\mathcal S\) be the set of monomials not divisible by any \(\operatorname{LM}(g_i)\). Because \(G\) is a Gröbner basis,
\[
\operatorname{in}(I)=\langle \operatorname{LM}(g_1),\ldots,\operatorname{LM}(g_s)\rangle.
\]
Suppose there were a nontrivial linear relation among the corresponding cosets:
\[
\sum_{j=1}^r c_jm_j\in I,
\]
where the \(m_j\in\mathcal S\) are distinct and not all \(c_j\) vanish. Let \(m\) be the largest \(m_j\) occurring with nonzero coefficient. Then
\[
\operatorname{LM}\!\left(\sum_j c_jm_j\right)=m.
\]
Since the polynomial lies in \(I\), its leading monomial belongs to \(\operatorname{in}(I)\), so some \(\operatorname{LM}(g_i)\) divides \(m\). This contradicts \(m\in\mathcal S\). Therefore the displayed cosets are linearly independent in \(k[x_1,\ldots,x_n]/I\).

For (b), the conclusion can fail if the chosen generators are not a Gröbner basis. Take
\[
k=\mathbb Q,\qquad I=(x,y)\subset\mathbb Q[x,y]
\]
with lexicographic order \(x>y\), and let
\[
G=\{x+y,\ x-y\}.
\]
Because \(2\) is invertible in \(\mathbb Q\), these two polynomials generate \(I\). Their leading monomials are both \(x\). Hence, if one used the criterion from part (a) with this non-Gröbner generating set, every monomial not divisible by \(x\), in particular \(y\), would be declared standard. But
\[
y+I=0
\]
in the quotient, so these cosets are not linearly independent. Indeed \(G\) is not a Gröbner basis, since \(\operatorname{in}(I)=(x,y)\) while \(\langle\operatorname{LM}(G)\rangle=(x)\).
:::
