---
schema: qual/card@1
id: P-EMAL3
kind: problem
title: "Double dual evaluation map"
classification:
  areas:
  - algebra
  topics:
  - Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both assertions and the evaluation formula with Linear Algebra 3 in the retained source extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked linearity and injectivity, the explicit finite-basis inverse including the zero space, and construction of a non-evaluation functional for every infinite basis and every field."
---

::: problem
Let $V$ be a vector space over a field $F$.
The evaluation map $e : V \to (V^\vee)^\vee$ is defined by $e(v)(f) := f(v)$ for $v \in V$ and $f \in V^\vee$.

(a) Prove that $e$ is an injection.

(b) Prove that $e$ is an isomorphism if and only if $V$ is finite dimensional.
:::

::: solution
Here $V^\vee=\operatorname{Hom}_F(V,F)$ is the algebraic
dual. We use the basis-extension theorem for vector spaces,
which follows from Zorn's lemma [@DF04].

<1>1. Evaluation defines an injective linear map $e$.

::: proof
For each $v\in V$, the map $f\mapsto f(v)$ is linear on
$V^\vee$, so $e(v)$ belongs to the double dual. For
$a,b\in F$, $v,w\in V$, and $f\in V^\vee$, one has
$$
e(av+bw)(f)=f(av+bw)=a f(v)+b f(w).
$$
This proves linearity of $e$. If $v\ne0$, extend the
linearly independent set $\{v\}$ to a basis. Assign value
one to $v$ and zero to every other basis vector, and extend
linearly to $f\in V^\vee$. Then $e(v)(f)=1$, so $e(v)$
is not zero. Thus the kernel of $e$ is zero.
:::

<1>2. Evaluation is surjective when $V$ is finite-dimensional.

::: proof
Let $v_1,\ldots,v_n$ be a basis with coordinate functionals
$\delta_1,\ldots,\delta_n$. Every $f\in V^\vee$ equals
$\sum_{i=1}^n f(v_i)\delta_i$, since these two functionals
have the same values on the basis. Given
$\Phi\in(V^\vee)^\vee$, set
$$
v=\sum_{i=1}^n\Phi(\delta_i)v_i.
$$
Then for every $f$,
$$
e(v)(f)=\sum_{i=1}^n\Phi(\delta_i)f(v_i)
=\Phi\left(\sum_{i=1}^n f(v_i)\delta_i\right)=\Phi(f).
$$
Therefore $e(v)=\Phi$. This also includes $n=0$, with
empty sums and all spaces zero. Together with step <1>1,
surjectivity makes $e$ an isomorphism.
:::

<1>3. Evaluation is not surjective when $V$ is infinite-dimensional.

::: proof
Choose an infinite basis $(v_i)_{i\in I}$. For each $i$,
let $\delta_i$ be the corresponding coordinate functional.
Also let $f_0\in V^\vee$ have value one on every $v_i$.
These prescriptions define linear functionals, because
every vector has a unique finite expansion in the basis.

Let $W\subseteq V^\vee$ be the linear span of the
$\delta_i$. Every element of $W$ vanishes on all but
finitely many basis vectors. In contrast, $f_0(v_i)=1$
for every $i$. Hence $f_0\notin W$, and the sum
$W+Ff_0$ is direct. Define
$$
\Phi_0:W\oplus Ff_0\longrightarrow F,
\qquad \Phi_0(w+cf_0)=c.
$$
The direct-sum expression proves that this is well defined
and linear. Extend a basis of $W\oplus Ff_0$ to a basis
of $V^\vee$, and extend $\Phi_0$ by assigning zero to
the added basis vectors. This gives a linear functional
$\Phi\in(V^\vee)^\vee$ with
$$
\Phi(\delta_i)=0\quad(i\in I),\qquad \Phi(f_0)=1.
$$

If $\Phi=e(v)$, then $\delta_i(v)=0$ for every $i$.
All coordinates of $v$ would vanish, so $v=0$ and
$e(v)=0$. This contradicts $\Phi(f_0)=1$. Thus $\Phi$
is not an evaluation functional. This construction uses
no restriction on the cardinality or characteristic of $F$.

Consequently $e$ fails to be an isomorphism in every
infinite-dimensional case. Steps <1>1 and <1>2 establish
both requested assertions.
:::
:::
