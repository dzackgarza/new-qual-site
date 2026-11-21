---
schema: qual/card@1
id: P-3YFNY
kind: problem
title: Cyclic vectors, the commutant, and equality of minimal and characteristic polynomials
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Rational Canonical Form
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card carried no audit list; this one records the change. Twenty-two steps asserted their claim
    with no justification and each now carries one: in part (a) the basis property, the expression of $Bv$
    through $p(A)$ and the commutation of $B$ with the powers of $A$ that makes the two maps agree on the
    basis; in the forward direction the degree count that rules out $\deg m_A < n$ and the Cayley--Hamilton
    divisibility that turns $\deg m_A \ge n$ into equality; and in the converse the $k[x]$-module
    structure, the invariant factor decomposition with its characteristic and minimal polynomials, the
    degree argument forcing a single invariant factor, and the passage of the quotient basis to
    $\{v, Av, \dots, A^{n-1}v\}$. Checked while writing: the degree argument needs each $d_i$ monic of
    positive degree, and the basis statement needs $\deg\chi_A = n$. One repair: the closing step had
    "Conclusion:" as its claim and now states the two conclusions. The statement is unchanged. The
    collection retains the UGA algebra qualifying exam of Fall 2018 and no solution sheet, so the
    argument is the card's own.
---

::: {.problem}
Let $A \in M_n(k)$ be an $n \times n$ matrix over a field $k$.

(a) Suppose that $v \in k^n$ is a column vector such that the set $\{v, A v, \dots, A^{n-1} v\}$ is linearly independent. Show that every matrix $B \in M_n(k)$ that commutes with $A$ ($A B = B A$) is a polynomial in $A$ with coefficients in $k$.

(b) Show that there exists a vector $v \in k^n$ such that $\{v, A v, \dots, A^{n-1} v\}$ is linearly independent if and only if the characteristic polynomial $\chi_A(x)$ equals the minimal polynomial $m_A(x)$.
:::

::: {.solution}
**Goal:** Prove that the centralizer of a cyclic operator is the polynomial algebra $k[A]$ in (a), and characterize cyclicity via $\chi_A(x) = m_A(x)$ in (b).

::: pf

::: pf-step
Part (a): Any commuting matrix $B$ is a polynomial in $A$.

::: pf-proof

::: pf-step
Since $\{v, A v, \dots, A^{n-1} v\}$ contains $n$ linearly independent vectors in $k^n$, it forms a basis $\mathcal{B} = \{v, A v, \dots, A^{n-1} v\}$ for $k^n$.

::: pf-proof
$n$ linearly independent vectors in an $n$-dimensional space form a basis, because a linearly independent set of size $n$ is maximal and spans the space.
:::

:::

::: pf-step
Since $\mathcal{B}$ spans $k^n$, the vector $B v \in k^n$ can be expressed as a linear combination of basis vectors:
$$B v = \sum_{j=0}^{n-1} c_j A^j v = p(A) v,$$
where $p(x) = \sum_{j=0}^{n-1} c_j x^j \in k[x]$.

::: pf-proof
A basis spans, so $Bv$ has an expression as a linear combination of the $A^j v$; collecting the coefficients into $p(x) = \sum_j c_j x^j$ turns that expression into $Bv = p(A)v$.
:::

:::

::: {.pf-step #commutes}
Because $A B = B A$, it follows by induction that $A^k B = B A^k$ for every integer $k \ge 0$.

::: pf-proof
Induction on $k$: the case $k = 0$ is trivial, and $A^{k+1}B = A(A^kB) = A(BA^k) = (AB)A^k = (BA)A^k = BA^{k+1}$ uses the induction hypothesis and $AB = BA$.
:::

:::

::: pf-step
Evaluate the action of $B$ on each basis vector $A^k v$ ($0 \le k \le n - 1$):
$$B (A^k v) = (B A^k) v = (A^k B) v = A^k (B v) = A^k (p(A) v) = p(A) (A^k v),$$
using that $A^k$ and $p(A)$ commute.

::: pf-proof
The chain $B(A^k v) = (BA^k)v = (A^kB)v = A^k(Bv) = A^k(p(A)v) = p(A)(A^k v)$ uses associativity of composition, the identity $A^kB = BA^k$ of step [](#commutes){.pf-ref}, the definition of $p$, and the fact that powers of $A$ commute with $p(A)$.
:::

:::

::: pf-step
Since the linear maps $B$ and $p(A)$ agree on all $n$ basis vectors of $\mathcal{B}$, they are equal as linear transformations on $k^n$.

::: pf-proof
Two linear maps that agree on a spanning set coincide, because their difference annihilates a basis of the space and a linear map that vanishes on a basis is zero.
:::

:::

::: pf-step
Thus $B = p(A)$, so $B$ is a polynomial in $A$.

::: pf-proof
The agreement on the basis gives $B = p(A)$ as maps, and $p$ has coefficients in $k$, so $B$ is a polynomial in $A$.
:::

:::

:::

:::

::: pf-step
Part (b) ($\implies$): Linear independence implies $\chi_A(x) = m_A(x)$.

::: pf-proof

::: pf-step
Suppose $\{v, A v, \dots, A^{n-1} v\}$ is linearly independent in $k^n$.

::: pf-proof
This is the hypothesis of the implication, recorded so that the steps that follow may use it.
:::

:::

::: pf-step
If $\deg m_A(x) = d < n$, write $m_A(x) = \sum_{j=0}^d a_j x^j$ with $a_d = 1$.

::: pf-proof
If the degree is $d < n$ the minimal polynomial can be written in the displayed form with leading coefficient $1$, which is legitimate because the minimal polynomial is monic by definition.
:::

:::

::: pf-step
Then $0 = m_A(A) v = \sum_{j=0}^d a_j A^j v$.

::: pf-proof
Evaluating the identity $m_A(A) = 0$, which holds by definition of the minimal polynomial, at the vector $v$ gives the displayed relation.
:::

:::

::: pf-step
Since $d < n$, this is a non-trivial linear combination of a subset of $\{v, A v, \dots, A^{n-1} v\}$ equaling zero, contradicting linear independence.

::: pf-proof
Because $d < n$ the relation involves only vectors among $v, Av, \dots, A^{n-1}v$, and its coefficients are not all zero because $m_A$ is monic of degree $d \ge 1$; so it is a nontrivial relation among those $n$ vectors, contradicting their linear independence.
:::

:::

::: pf-step
Thus $\deg m_A(x) \ge n$.

::: pf-proof
A contradiction follows from assuming the degree to be less than $n$, so the degree of the minimal polynomial is at least $n$.
:::

:::

::: pf-step
By the Cayley–Hamilton Theorem, $m_A(x) \mid \chi_A(x)$.

::: pf-proof
Cayley--Hamilton gives $\chi_A(A) = 0$, and the minimal polynomial is the monic generator of the ideal of polynomials annihilating $A$, so it divides every such polynomial.
:::

:::

::: pf-step
Since $\deg \chi_A(x) = n$ and both $m_A(x)$ and $\chi_A(x)$ are monic polynomials of degree $n$, we conclude $\chi_A(x) = m_A(x)$.

::: pf-proof
The minimal polynomial divides $\chi_A$ and has degree at least $n = \deg\chi_A$, so the two degrees are equal; both are monic, and a monic divisor of a monic polynomial of the same degree is that polynomial.
:::

:::

:::

:::

::: pf-step
Part (b) ($\impliedby$): $\chi_A(x) = m_A(x)$ implies existence of a cyclic vector.

::: pf-proof

::: pf-step
Regard $V = k^n$ as a finitely generated module over the principal ideal domain $k[x]$, where the action is given by $x \cdot w = A w$ for $w \in V$.

::: pf-proof
The formula $x \cdot w = Aw$ makes $V$ a $k[x]$-module because $A$ is $k$-linear, and the vectors of a $k$-basis of $V$ generate it as a $k[x]$-module, since a $k$-linear combination is in particular a $k[x]$-linear one.
:::

:::

::: pf-step
By the Structure Theorem for finitely generated modules over a PID (Invariant Factor Decomposition), there exist monic polynomials $d_1(x) \mid d_2(x) \mid \dots \mid d_r(x)$ in $k[x]$ such that
$$V \cong \bigoplus_{i=1}^r \frac{k[x]}{\langle d_i(x) \rangle}$$
as $k[x]$-modules.

::: pf-proof
The structure theorem for finitely generated modules over a principal ideal domain, in its invariant factor form, says the module is a finite direct sum of cyclic modules $k[x]/(d_i)$ with $d_1 \mid d_2 \mid \dots \mid d_r$; that is the displayed decomposition.
:::

:::

::: {.pf-step #invariants}
Under this decomposition:

- The characteristic polynomial is the product of all invariant factors: $\chi_A(x) = \prod_{i=1}^r d_i(x)$.
- The minimal polynomial is the largest invariant factor: $m_A(x) = d_r(x)$.

::: pf-proof
On a cyclic summand $k[x]/(d)$ with multiplication by $x$ the characteristic polynomial of that operator is $d$ and the minimal polynomial is $d$; on a direct sum the characteristic polynomials multiply, and the minimal polynomial is the least common multiple, which for a divisibility chain $d_1 \mid \dots \mid d_r$ is the largest one $d_r$.
:::

:::

::: pf-step
The hypothesis $\chi_A(x) = m_A(x)$ implies $\prod_{i=1}^r d_i(x) = d_r(x)$.

::: pf-proof
Substituting the two identities of step [](#invariants){.pf-ref} into the hypothesis $\chi_A = m_A$ gives $\prod_{i=1}^r d_i = d_r$.
:::

:::

::: pf-step
Since each $d_i(x)$ is monic of degree $\ge 1$, this equality forces $r = 1$ and $d_1(x) = \chi_A(x)$.

::: pf-proof
Each $d_i$ is monic of degree at least $1$, so $\prod_{i<r} d_i$ divides $d_r$ and has degree $\sum_{i<r}\deg d_i$; equality of the product with $d_r$ forces that degree to be $0$, hence $r - 1 = 0$, so $r = 1$ and $d_1 = d_r = \chi_A$.
:::

:::

::: pf-step
Therefore, $V \cong k[x]/\langle \chi_A(x) \rangle$ is a cyclic $k[x]$-module generated by the element $\bar{1} = 1 + \langle \chi_A(x) \rangle$.

::: pf-proof
A module isomorphic to $k[x]/(\chi_A)$ is cyclic, generated by the class of $1$, because the class of any polynomial $p$ is $p(x)$ times the class of $1$.
:::

:::

::: pf-step
Let $v \in V$ be the image of $\bar{1}$ under the isomorphism.

::: pf-proof
The module isomorphism is in particular a bijection, so the class of $1$ has a well-defined image $v$ in $V$.
:::

:::

::: pf-step
In the quotient ring $k[x]/\langle \chi_A(x) \rangle$, the elements $\{\bar{1}, \bar{x}, \bar{x}^2, \dots, \bar{x}^{n-1}\}$ form a $k$-vector space basis because $\deg \chi_A(x) = n$.

::: pf-proof
Division by the monic polynomial $\chi_A$ of degree $n$ gives every class a unique representative of degree less than $n$, so the classes of $1, x, \dots, x^{n-1}$ form a $k$-basis of the quotient.
:::

:::

::: pf-step
Applying the $k[x]$-module isomorphism, the corresponding elements $\{v, A v, A^2 v, \dots, A^{n-1} v\}$ form a $k$-basis for $V = k^n$, and are in particular linearly independent.

::: pf-proof
An isomorphism of $k[x]$-modules is $k$-linear, so it carries a $k$-basis to a $k$-basis; the class of $x^k$ is $x^k$ times the class of $1$, multiplication by $x^k$ corresponds to $A^k$, so that class is carried to $A^k v$.
:::

:::

:::

:::

::: pf-step
The matrix $B$ is a polynomial in $A$, and a cyclic vector exists exactly when $\chi_A(x) = m_A(x)$.

::: pf-proof
The matrix $B$ is a polynomial in $A$, and a cyclic vector exists if and only if $\chi_A(x) = m_A(x)$.
:::

:::

:::
:::
