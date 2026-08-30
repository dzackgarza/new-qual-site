---
title: Jordan canonical form
order: 30
problems:
  topics:
  - Jordan Canonical Form
---

# Jordan canonical form

The elementary divisor decomposition, read as a matrix.
It exists exactly when $\chi_A$ splits; when it does not, the [[algebra/linear-algebra/rational-canonical-form|rational form]] is the substitute.

> A useful reference: [Matt Baker's post on the Jordan canonical form](https://mattbaker.blog/2015/07/31/the-jordan-canonical-form/).

:::{.fact}
The Jordan form corresponds to the **elementary divisors**.

:::

[[PR-5A2W4]]

[[L-CD6QT]]

## Reading the blocks off

:::{.example title="From the two polynomials"}
Suppose $A$ is $5\times 5$ with
\[
\min_A(t) &= (t-4)^2(t+6) \\
\chi_A(t) &= (t-4)^3(t+6)^2
.\]

For $\lambda = 4$: the blocks total size $3$ and the largest is size $2$, so the blocks are $J_1 \oplus J_2$.
For $\lambda = -6$: the blocks total size $2$ and the largest is size $1$, so they are $J_1\oplus J_1$.

:::

:::{.warnings title="The two polynomials are not always enough"}
$\min_A$ and $\chi_A$ do not determine the form.
For $4\times 4$ matrices with $\min_A(t) = t^2$ and $\chi_A(t) = t^4$ there are two classes, $J_2\oplus J_2$ and $J_2\oplus J_1\oplus J_1$.
When they fail to decide, the extra data is $\dim\ker(A-\lambda I)^k$: the successive differences count the blocks of size at least $k$.

:::

## Why it exists

:::{.remark title="Sketch"}
\envlist

- Call $f: V\to V$ decomposable when $V$ splits into a direct sum of $f\dash$invariant subspaces; then $f$ is block diagonal and restricts to indecomposable maps, so only those need treating.
- For indecomposable $h$ there is an $m\geq 1$ with $V = \ker h^m \oplus \im h^m$.
- Take an eigenvalue, $fv = \lambda v$, and apply this to $h\da f-\lambda I$.
  Since $V$ is indecomposable and $v\in\ker h$, this forces $V = \ker h^m$, so $h$ is nilpotent of some minimal degree $k$.
- Choose a cyclic vector $w$ with $h^kw=0$ and $h^{k-1}w \neq 0$; then $\ts{w, hw, \cdots, h^{k-1}w}$ is a basis, and $k = \dim V$ since a smaller $k$ would give a proper invariant subspace.
- The matrix of a cyclic vector is a Jordan block.

:::

## Generalized eigenspaces

[[L-W5S2W]]

:::{.remark title="The module picture"}
Writing $\Ann(\vector v)$ for the annihilator of $\vector v$, view $V$ as a $k[x]\dash$module by $p(x)\actson \vector v \da p(A)\vector v$, so that
\[
\Ann(\vector v) \da \ts{ q(x) \in k[x] \st q(A)(\vector v) = 0}
.\]
Then $\vector w$ is an eigenvector with eigenvalue $\lambda_i$ exactly when $A - \lambda_i I \in \Ann(\vector w)$, and a *generalized* eigenvector exactly when
\[
(A-\lambda_i I)^k\in \Ann(\vector w) \text{ for some } k \iff A-\lambda_i I \in \sqrt{\Ann(\vector w)}
.\]
So the generalized eigenspace is
\[
V^{\lambda_i}
&\da \ts{\vector v\in V \st (A-\lambda_i I)^n \vector v = 0 \text{ for some }n } \\
&= \ts{\vector v\in V \st A-\lambda_i I \in \sqrt{\Ann(\vector v)} }
,\]
the theorem is $V \cong \bigoplus_i V^{\lambda_i}$, and $V^{\lambda_i} = \ker (A-\lambda_i I)^n$ for $n \da \dim V$.
Taking radicals is what turns eigenvectors into generalized ones, which is the whole difference between diagonalizable and not.

:::

:::{.proof title="of the generalized eigenspace decomposition"}
\envlist

- Write $\chi_A(x) = \prod (x-\lambda_i)^{n_i}$ and set $V^{j} \da \ker (A-\lambda_j I)^n$.
- Fix $j$, let $h_j(x) = \prod_{i\neq j}(x-\lambda_i)^{n_i}$ be $\chi_A$ with the $\lambda_j$ factor deleted, and set $W^j \da \im(h_j(A))$.
- $W^j \subseteq V^j$: since $0 = \chi_A(A) = (A-\lambda_j I)^{n_j} h_j(A)$, in fact $W^j \subseteq \ker (A - \lambda_j)^{n_j}$.
- $\sum V^j = V$: the $h_i$ are coprime, so Euclid gives $\sum_i f_i h_i = 1$, hence $\sum f_i(A)h_i(A) = I$ and every $\vector v$ lies in $\sum W^j$.
- The sum is direct: if $0 = \sum w_i$ with $w_i\in W^i$, use $h_j(w_i) = 0$ for $i\neq j$ and $\vector w_i = \sum_j f_j(A)h_j(A)\vector w_i = f_i(A)h_i(A)\vector w_i$ to get $w_i = 0$.

:::

## Exercises

[[E-23SLE]]
[[E-I7ZD4]]
[[E-GEVBZ]]
[[E-2KJEL]]
