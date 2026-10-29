---
schema: qual/card@1
id: P-XRTSC
kind: problem
title: Rank-nullity over division rings, and left inverses of rectangular matrices
classification:
  areas:
  - algebra
  topics:
  - Rank and Nullity
  - Free Modules
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The problem block held a worked argument (a proof of rank-nullity over a division ring and of the one-sided inverse criteria) instead of a statement; it is replaced by the statement that argument answers. The removed argument claimed that rank A < m gives a pair of linearly dependent columns, which is false, and the correct second solution is kept as a structured proof.
---

::: {.problem}
Let $D$ be a division ring.

(a) Prove the rank-nullity theorem for a $D$-linear map $\phi:D^m\to D^n$: $m=\dim_D\ker\phi+\dim_D\im\phi$.

(b) Show that $A\in M_{n\times m}(D)$ has a left inverse if and only if $\rank A=m$.

(c) Show that $A\in M_{n\times m}(D)$ has a right inverse if and only if $\rank A=n$.
:::

::: {.solution}
Regard $D^m$ and $D^n$ as right vector spaces over $D$, with a matrix acting on column vectors by left multiplication, and write $e_1,\ldots,e_m$ for the standard basis of $D^m$.
Every vector space over a division ring has a basis, and every linearly independent set extends to a basis.

::: pf

::: {.pf-step #rank-nullity}
(a) $m=\dim_D\ker\phi+\dim_D\im\phi$.

::: pf-proof
Choose a basis $u_1,\ldots,u_k$ of $\ker\phi$ and extend it by $w_1,\ldots,w_l$ to a basis of $D^m$.
The vectors $\phi(w_1),\ldots,\phi(w_l)$ span $\im\phi$.
They are independent: if $\sum_j\phi(w_j)c_j=0$, then $\sum_j w_jc_j\in\ker\phi$, so it is a combination of the $u_i$, and independence of the basis forces every $c_j=0$.
Hence $\dim\im\phi=l=m-k$.
:::

:::

::: pf-step
(b) $A$ has a left inverse if and only if $\rank A=m$.

::: pf-proof
If $BA=I_m$ and $Av=0$, then $v=BAv=0$, so $\ker A=0$ and $\rank A=m$ by step [](#rank-nullity){.pf-ref}.
Conversely, if $\rank A=m$, then $\ker A=0$ by step [](#rank-nullity){.pf-ref}, so $Ae_1,\ldots,Ae_m$ is a basis of $\im A$.
Extend it to a basis of $D^n$ and let $B:D^n\to D^m$ be the linear map with $B(Ae_i)=e_i$ and sending the added basis vectors to $0$.
Then $BA=I_m$.
:::

:::

::: pf-step
(c) $A$ has a right inverse if and only if $\rank A=n$.

::: pf-proof
If $AB=I_n$, then every $v\in D^n$ equals $A(Bv)$, so $A$ is surjective and $\rank A=n$.
Conversely, if $\rank A=n$, then $A$ is surjective; choose $x_i\in D^m$ with $Ax_i=e_i$ for the standard basis $e_1,\ldots,e_n$ of $D^n$, and let $B$ be the linear map with $Be_i=x_i$.
Then $AB=I_n$.
:::

:::

:::

:::
