---
schema: qual/card@1
id: P-PCSZ2
kind: problem
title: 'The identity bijection $J\rtimes_\varphi L\to J\times L$ is an isomorphism exactly for the trivial action'
classification:
  areas:
  - algebra
  topics:
  - Semidirect Products
  - Automorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both parts with June 2015 Groups 3 in the retained extraction; corrected the algebra classification and retained the identity-bijection qualification in the title."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Verified associativity and both inverse products, then tested the stated identity map on cross-factor products rather than an arbitrary abstract isomorphism."
---

::: {.problem}
Suppose $J$ and $L$ are groups, and $\varphi: L \to \mathrm{Aut}(J)$ is a group homomorphism.

a. Give a definition for the group $J \rtimes_\varphi L$.

b. The identity function gives a bijection of sets $J \rtimes_\varphi L \to J \times L$.
Prove that this function is a group isomorphism if and only if $\varphi$ is the trivial homomorphism sending everything to the identity.
:::

::: solution
Write $\varphi_\ell=\varphi(\ell)\in\operatorname{Aut}(J)$ for
$\ell\in L$.

<1>1. The semidirect product is the set $J\times L$ with multiplication
$$
(j,\ell)*(j',\ell')=
\bigl(j\varphi_\ell(j'),\ell\ell'\bigr).
$$

::: proof
For three pairs, multiplying the first two and then the third gives
$$
\bigl(j\varphi_\ell(j')\varphi_{\ell\ell'}(j''),
      \ell\ell'\ell''\bigr).
$$
Multiplying the last two and then the first gives
$$
\bigl(j\varphi_\ell(j'\varphi_{\ell'}(j'')),
      \ell\ell'\ell''\bigr).
$$
These are equal because $\varphi_\ell$ preserves multiplication
and $\varphi_{\ell\ell'}=\varphi_\ell\circ\varphi_{\ell'}$.
Thus the operation is associative.

The identity is $(1_J,1_L)$, since
$\varphi_{1_L}=\operatorname{id}_J$ and each automorphism fixes $1_J$.
The inverse of $(j,\ell)$ is
$$
\bigl(\varphi_{\ell^{-1}}(j^{-1}),\ell^{-1}\bigr).
$$
Multiplication in the first order gives first coordinate
$j\varphi_\ell\varphi_{\ell^{-1}}(j^{-1})=1_J$;
in the reverse order it gives
$\varphi_{\ell^{-1}}(j^{-1})\varphi_{\ell^{-1}}(j)=1_J$.
Both second coordinates are $1_L$. This verifies all group axioms.
:::

<1>2. The identity function on $J\times L$ is a group isomorphism
from this semidirect product to the direct product if and only if
$\varphi$ is trivial.

::: proof
If every $\varphi_\ell$ is the identity on $J$, the multiplication
in step <1>1 becomes $(j,\ell)*(j',\ell')=(jj',\ell\ell')$,
the direct-product multiplication. The identity function is then
an isomorphism.

Conversely, suppose this identity function preserves multiplication.
For any $j\in J$ and $\ell\in L$, multiplication in the semidirect
product gives
$$
(1_J,\ell)*(j,1_L)=(\varphi_\ell(j),\ell),
$$
whereas multiplication of the same pairs in the direct product gives
$(j,\ell)$. Preservation by the identity map implies
$\varphi_\ell(j)=j$ for every $j,\ell$. Thus every
$\varphi_\ell$ is the identity automorphism, proving the converse.
:::
:::
