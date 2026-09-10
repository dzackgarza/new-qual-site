---
schema: qual/card@1
id: P-MMAQ-YRTGM662ZN
kind: problem
title: The evaluation map $V\to(V^\vee)^\vee$ is injective, and an isomorphism if
  and only if $V$ is finite-dimensional
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Vector Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared the evaluation map and both assertions with Linear Algebra 3 on PDF page 2; the duals are algebraic duals over the arbitrary field F."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked linearity and separation by a coordinate functional, the finite-basis inverse, and the non-evaluation double-dual functional constructed from finite-support functions in the infinite-dimensional case."
---

::: problem
Let $V$ be a vector space over a field $F$.
The evaluation map $e\colon V \to (V^\vee)^\vee$ is defined by $e(v)(f) \da f(v)$ for $v\in V$ and $f\in V^\vee$.

1. Prove that $e$ is an injection.

2. Prove that $e$ is an isomorphism if and only if $V$ is finite dimensional.
:::

::: solution
Write $V^\vee=\operatorname{Hom}_F(V,F)$ for the algebraic
dual. We use basis existence and basis extension, valid
for arbitrary vector spaces by Zorn's lemma [@DF04].

<1>1. The map $e:V\to V^{\vee\vee}$ is linear and injective.

::: proof
For fixed $v$, evaluation $f\mapsto f(v)$ is linear
on $V^\vee$. For $a,b\in F$ and $v,w\in V$,
$$
e(av+bw)(f)=f(av+bw)=a e(v)(f)+b e(w)(f)
$$
for every $f$, so $e$ is linear.
If $v\ne0$, extend $\{v\}$ to a basis of $V$.
Assign value one to $v$ and zero to the other basis
vectors, and extend linearly to a functional $f$.
Then $e(v)(f)=1$, so $e(v)\ne0$. The kernel is
therefore zero.
:::

<1>2. When $V$ is finite-dimensional, $e$ is onto.

::: proof
Choose a basis $v_1,\ldots,v_n$ and let
$\varepsilon_i$ be its coordinate functionals.
Every $f\in V^\vee$ satisfies
$f=\sum_{i=1}^n f(v_i)\varepsilon_i$ by evaluation
on the basis. For $\Phi\in V^{\vee\vee}$ set
$v=\sum_{i=1}^n\Phi(\varepsilon_i)v_i$. Then
$$
\Phi(f)=\sum_{i=1}^n f(v_i)\Phi(\varepsilon_i)=f(v)=e(v)(f).
$$
Hence $\Phi=e(v)$, proving surjectivity. If $V=0$,
the same statement uses the empty basis and all
three spaces are zero. Together with step <1>1,
this proves the forward implication in part (2).
:::

<1>3. When $V$ is infinite-dimensional, $e$ is not onto.

::: proof
Choose a basis $(v_i)_{i\in I}$ with $I$ infinite.
Sending $f$ to $(f(v_i))_{i\in I}$ identifies $V^\vee$
with the full function space $F^I$: every assignment
on the basis extends uniquely by finite linear sums.
Let $D\subset F^I$ be the subspace of finite-support
functions, and let $\mathbf1$ be the constant-one
function. Since $I$ is infinite, $\mathbf1\notin D$.

On $D+F\mathbf1$ define
$\lambda_0(d+c\mathbf1)=c$. The sum is direct:
a nonzero constant function cannot have finite
support. Thus this rule is well defined and linear.
Extend a basis of this subspace to a basis of $F^I$
and assign value zero on the added basis vectors.
This extends $\lambda_0$ to a linear functional
$\lambda:F^I\to F$ with $\lambda(D)=0$ and
$\lambda(\mathbf1)=1$.

Via the identification above, $\lambda$ is an
element of $V^{\vee\vee}$. Suppose it equals $e(v)$.
Write $v=\sum_{i\in J}a_i v_i$ for a finite set $J$.
The coordinate functional $\varepsilon_i$ corresponds
to the function supported at $i$ with value one,
which belongs to $D$. Thus
$0=\lambda(\varepsilon_i)=\varepsilon_i(v)=a_i$
for every $i\in J$. Hence $v=0$, which would imply
$\lambda=0$, contrary to $\lambda(\mathbf1)=1$.
This constructs a double-dual element not in the
image and proves the converse implication.
:::
:::
