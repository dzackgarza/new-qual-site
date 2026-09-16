---
title: Jordan canonical form
order: 30
topics:
- Jordan Canonical Form
---

# Jordan canonical form

Let $A$ be an $n\times n$ matrix over a field $k$.
The Jordan canonical form of $A$ exists if and only if the characteristic polynomial $\chi_A$ splits over $k$; the [[algebra/linear-algebra/rational-canonical-form|rational canonical form]] exists over every field.

::: {.fact}
Make $V=k^n$ a $k[x]$-module with $x$ acting by $A$.
If $\chi_A$ splits, the elementary divisors of $V$ have the form $(x-\lambda)^e$, and the Jordan form of $A$ has one Jordan block $J_e(\lambda)$ for each elementary divisor $(x-\lambda)^e$.
:::

[[PR-5A2W4]]

[[L-CD6QT]]

## Jordan blocks from the minimal and characteristic polynomials

::: {.example title="From the two polynomials"}
Suppose $A$ is $5\times 5$ with
$$
\begin{aligned}
\min_A(t) &= (t-4)^2(t+6), \\
\chi_A(t) &= (t-4)^3(t+6)^2.
\end{aligned}
$$

For $\lambda = 4$, the block sizes sum to $3$ and the largest is $2$, so the blocks are $J_2(4) \oplus J_1(4)$.
For $\lambda = -6$, the block sizes sum to $2$ and the largest is $1$, so the blocks are $J_1(-6)\oplus J_1(-6)$.
:::

::: {.warnings title="The two polynomials do not determine the form"}
For $4\times 4$ matrices with $\min_A(t) = t^2$ and $\chi_A(t) = t^4$ there are two similarity classes, $J_2(0)\oplus J_2(0)$ and $J_2(0)\oplus J_1(0)\oplus J_1(0)$.
They are distinguished by $\dim\ker A$, which is $2$ and $3$ respectively.
In general, $\dim\ker(A-\lambda I)^k-\dim\ker(A-\lambda I)^{k-1}$ is the number of Jordan blocks for $\lambda$ of size at least $k$.
:::

## Existence

::: {.remark title="Sketch of existence"}
Assume $\chi_A$ splits over $k$, and let $f\colon V\to V$ be the linear map given by $A$.

- $V$ is a direct sum of $f$-invariant subspaces on each of which $f$ is indecomposable, and $f$ is block diagonal with respect to such a decomposition, so it suffices to treat indecomposable $f$.

- By Fitting's lemma, for every linear map $h\colon V\to V$ there is $m\geq 1$ with $V = \ker h^m \oplus \im h^m$, and both summands are $h$-invariant.

- Let $\lambda$ be an eigenvalue of $f$ with eigenvector $v$, and apply Fitting's lemma to $h\da f-\lambda I$.
  Since $v\in\ker h^m$ and $f$ is indecomposable, $V = \ker h^m$, so $h$ is nilpotent; let $k$ be its nilpotency index.

- Choose $w$ with $h^{k-1}w \neq 0$.
  The span $W$ of $w, hw, \ldots, h^{k-1}w$ is $h$-invariant, these vectors are linearly independent, and $W$ has an $h$-invariant complement; since $f$ is indecomposable, $W = V$ and $k=\dim V$.

- In the basis $h^{k-1}w,\ldots,hw,w$, the matrix of $f = \lambda I + h$ is the Jordan block $J_k(\lambda)$.
:::

## Generalized eigenspaces

[[L-W5S2W]]

::: {.remark title="The module structure"}
Make $V$ a $k[x]$-module by $p(x)\actson \vector v \da p(A)\vector v$, and for $\vector v\in V$ let
$$
\Ann(\vector v) \da \ts{ q(x) \in k[x] \st q(A)\vector v = 0}.
$$
A nonzero $\vector w$ is an eigenvector with eigenvalue $\lambda_i$ if and only if $x - \lambda_i \in \Ann(\vector w)$, and a generalized eigenvector for $\lambda_i$ if and only if
$$
(x-\lambda_i)^k\in \Ann(\vector w) \text{ for some } k \iff x-\lambda_i \in \sqrt{\Ann(\vector w)}.
$$
The generalized eigenspace for $\lambda_i$ is
$$
\begin{aligned}
V^{\lambda_i}
&\da \ts{\vector v\in V \st (A-\lambda_i I)^m \vector v = 0 \text{ for some }m } \\
&= \ts{\vector v\in V \st x-\lambda_i \in \sqrt{\Ann(\vector v)} },
\end{aligned}
$$
and $V^{\lambda_i} = \ker (A-\lambda_i I)^n$ for $n \da \dim V$.
If $\chi_A$ splits, then $V = \bigoplus_i V^{\lambda_i}$.
:::

::: {.proof title="of the generalized eigenspace decomposition"}
\envlist

- Write $\chi_A(x) = \prod_i (x-\lambda_i)^{n_i}$ with the $\lambda_i$ distinct, and set $V^{j} \da \ker (A-\lambda_j I)^n$.

- For each $j$, let $h_j(x) = \prod_{i\neq j}(x-\lambda_i)^{n_i}$ and $W^j \da \im(h_j(A))$.

- $W^j \subseteq \ker (A - \lambda_j I)^{n_j}\subseteq V^j$, since $(A-\lambda_j I)^{n_j} h_j(A) = \chi_A(A) = 0$ by Cayley--Hamilton.

- $\sum_j W^j = V$: the $h_j$ have no common factor, so there are $f_j\in k[x]$ with $\sum_j f_j h_j = 1$, hence $\sum_j f_j(A)h_j(A) = I$ and $\vector v = \sum_j f_j(A)h_j(A)\vector v\in\sum_j W^j$ for every $\vector v$.

- The sum is direct: $h_j(A)W^i = 0$ for $i\neq j$, because $(x-\lambda_i)^{n_i}$ divides $h_j$.
  Hence for $\vector w\in W^i$, $\vector w = \sum_j f_j(A)h_j(A)\vector w = f_i(A)h_i(A)\vector w$, and applying $f_i(A)h_i(A)$ to a relation $0 = \sum_j \vector w_j$ with $\vector w_j\in W^j$ gives $\vector w_i = 0$.

- $V^j = W^j$: for $i\neq j$, $A-\lambda_j I = (A-\lambda_i I) + (\lambda_i-\lambda_j)I$ is the sum of a nilpotent operator and a nonzero scalar on the invariant subspace $W^i$, hence invertible there.
  If $\vector v = \sum_i \vector w_i\in V^j$, then $0=(A-\lambda_j I)^n\vector v = \sum_i (A-\lambda_j I)^n\vector w_i$ with each term in $W^i$, so $\vector w_i = 0$ for $i\neq j$ and $\vector v\in W^j$.
:::

## Exercises

[[E-23SLE]]

[[E-I7ZD4]]

[[E-GEVBZ]]

[[E-2KJEL]]
